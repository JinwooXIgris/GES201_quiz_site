/**
 * GES 201: Use of English II — CBT Master Quiz & Exam Simulator
 * Complete JavaScript Application Logic
 */

(function () {
  'use strict';

  // ==========================================
  // App Global State
  // ==========================================
  const state = {
    allQuestions: [],
    categories: {},
    
    // Option shuffle cache: qId -> { shuffledOptions: [...], originalToShuffled: Map }
    // This ensures each question keeps its shuffled order for the entire session
    optionShuffleCache: new Map(),
    
    // Practice Mode
    practice: {
      filteredQuestions: [],
      currentIndex: 0,
      userAnswers: {}, // qId -> selected original option string
      score: 0,
      totalAnswered: 0
    },

    // Timed Exam Simulator
    exam: {
      active: false,
      questions: [],
      currentIndex: 0,
      userAnswers: {}, // qId -> selected original option string
      flagged: new Set(),
      timerInterval: null,
      remainingSeconds: 20 * 60,
      totalSeconds: 20 * 60,
      historyRecord: null
    },

    // Flashcards
    flashcards: {
      deck: [],
      currentIndex: 0,
      isFlipped: false
    },

    // Question Bank Browser
    bank: {
      filtered: []
    },

    // User Progress / Local Storage
    progress: {
      totalAttempted: 0,
      totalCorrect: 0,
      savedMistakes: [], // list of question IDs
      examHistory: []   // list of exam attempt objects
    }
  };

  // ==========================================
  // Option Shuffling & Re-lettering System
  // ==========================================
  const OPTION_LETTERS = ['A', 'B', 'C', 'D', 'E'];

  /**
   * Get shuffled options for a question. Returns an array of objects:
   * [{ letter: 'A', text: '...content without prefix...', originalOption: 'B. ...full original...' }, ...]
   * Cached per question ID so navigating back shows the same order.
   */
  function getShuffledOptions(q) {
    if (state.optionShuffleCache.has(q.id)) {
      return state.optionShuffleCache.get(q.id);
    }

    // Strip original letter prefixes and shuffle
    const parsed = q.options.map(opt => ({
      originalOption: opt,
      text: opt.replace(/^[A-E]\\.\s*/, '')
    }));

    // Fisher-Yates shuffle
    for (let i = parsed.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [parsed[i], parsed[j]] = [parsed[j], parsed[i]];
    }

    // Assign fresh sequential letters
    const shuffled = parsed.map((item, idx) => ({
      letter: OPTION_LETTERS[idx] || String.fromCharCode(65 + idx),
      text: item.text,
      originalOption: item.originalOption
    }));

    state.optionShuffleCache.set(q.id, shuffled);
    return shuffled;
  }

  /**
   * Find the new display letter for the correct answer after shuffling.
   */
  function getShuffledCorrectLetter(q) {
    const shuffled = getShuffledOptions(q);
    const match = shuffled.find(s => s.originalOption === q.correct_answer);
    return match ? match.letter : '?';
  }

  // ==========================================
  // LocalStorage Persistence
  // ==========================================
  const STORAGE_KEY = 'ges201_cbt_master_v1';

  function loadProgress() {
    try {
      const saved = localStorage.getItem(STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        state.progress = {
          totalAttempted: parsed.totalAttempted || 0,
          totalCorrect: parsed.totalCorrect || 0,
          savedMistakes: Array.isArray(parsed.savedMistakes) ? parsed.savedMistakes : [],
          examHistory: Array.isArray(parsed.examHistory) ? parsed.examHistory : []
        };
      }
    } catch (e) {
      console.warn('Could not load user progress from localStorage:', e);
    }
    updateHeaderCounters();
  }

  function saveProgress() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.progress));
    } catch (e) {
      console.warn('Could not save user progress to localStorage:', e);
    }
    updateHeaderCounters();
  }

  function updateHeaderCounters() {
    const mistakesCountEl = document.getElementById('header-mistakes-count');
    if (mistakesCountEl) {
      mistakesCountEl.textContent = state.progress.savedMistakes.length;
    }
  }

  // ==========================================
  // Initialization & Data Loading
  // ==========================================
  async function initApp() {
    initTheme();
    loadProgress();
    initTabNavigation();

    try {
      if (window.GES201_EMBEDDED_QUESTIONS && Array.isArray(window.GES201_EMBEDDED_QUESTIONS)) {
        state.allQuestions = window.GES201_EMBEDDED_QUESTIONS;
      } else {
        const response = await fetch('data/questions.json');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        state.allQuestions = await response.json();
      }
      console.log(`Loaded ${state.allQuestions.length} questions successfully.`);

      const totalQEl = document.getElementById('header-total-q');
      if (totalQEl) totalQEl.textContent = state.allQuestions.length;

      // Initialize all application views
      initPracticeMode();
      initExamSimulator();
      initFlashcards();
      initQuestionBank();
      initAnalytics();

      // Keyboard navigation
      initKeyboardShortcuts();

    } catch (error) {
      console.error('Failed to load questions.json:', error);
      alert('Error loading question bank. Please ensure data/questions.json is present.');
    }
  }

  // ==========================================
  // Theme Toggle (Dark / Light)
  // ==========================================
  function initTheme() {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const savedTheme = localStorage.getItem('ges201_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    if (themeToggleBtn) {
      themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('ges201_theme', newTheme);
        updateThemeIcon(newTheme);
      });
    }
  }

  function updateThemeIcon(theme) {
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (!themeToggleBtn) return;
    const icon = themeToggleBtn.querySelector('i');
    if (icon) {
      icon.className = theme === 'dark' ? 'fa-solid fa-moon' : 'fa-solid fa-sun';
    }
  }

  // ==========================================
  // Tab Navigation
  // ==========================================
  function initTabNavigation() {
    const navTabs = document.querySelectorAll('.nav-tab');
    navTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const targetTab = tab.getAttribute('data-tab');
        
        // Prevent accidental exit from active exam without confirmation
        if (state.exam.active && targetTab !== 'exam') {
          if (!confirm('You have an active timed exam in progress! Are you sure you want to navigate away?')) {
            return;
          }
        }

        navTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('active'));
        const activePane = document.getElementById(`tab-${targetTab}`);
        if (activePane) activePane.classList.add('active');

        // View specific refresh
        if (targetTab === 'analytics') renderAnalytics();
        if (targetTab === 'flashcards') renderFlashcard();
        if (targetTab === 'bank') renderBankList();
      });
    });
  }

  // ==========================================
  // 1. PRACTICE MODE
  // ==========================================
  function initPracticeMode() {
    const categorySelect = document.getElementById('practice-category');
    const difficultySelect = document.getElementById('practice-difficulty');
    const sourceSelect = document.getElementById('practice-source');
    const applyFilterBtn = document.getElementById('start-filtered-practice');
    const resetFiltersBtn = document.getElementById('reset-practice-filters');

    const prevBtn = document.getElementById('practice-prev-btn');
    const nextBtn = document.getElementById('practice-next-btn');
    const bookmarkBtn = document.getElementById('practice-bookmark');

    function applyFilters(shuffle = true) {
      const cat = categorySelect.value;
      const diff = difficultySelect.value;
      const src = sourceSelect.value;

      state.practice.filteredQuestions = state.allQuestions.filter(q => {
        const matchCat = (cat === 'all') || (q.category === cat);
        const matchDiff = (diff === 'all') || (q.difficulty === diff);
        const matchSrc = (src === 'all') || (q.source === src);
        return matchCat && matchDiff && matchSrc;
      });

      if (shuffle) {
        state.practice.filteredQuestions = shuffleArray([...state.practice.filteredQuestions]);
      }

      state.practice.currentIndex = 0;
      state.practice.userAnswers = {};
      state.practice.score = 0;
      state.practice.totalAnswered = 0;

      renderPracticeQuestion();
    }

    if (applyFilterBtn) {
      applyFilterBtn.addEventListener('click', () => applyFilters(true));
    }

    if (resetFiltersBtn) {
      resetFiltersBtn.addEventListener('click', () => {
        categorySelect.value = 'all';
        difficultySelect.value = 'all';
        sourceSelect.value = 'all';
        applyFilters(true);
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.practice.currentIndex > 0) {
          state.practice.currentIndex--;
          renderPracticeQuestion();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.practice.currentIndex < state.practice.filteredQuestions.length - 1) {
          state.practice.currentIndex++;
          renderPracticeQuestion();
        }
      });
    }

    if (bookmarkBtn) {
      bookmarkBtn.addEventListener('click', togglePracticeBookmark);
    }

    // Initial setup
    applyFilters(true);
  }

  function renderPracticeQuestion() {
    const qList = state.practice.filteredQuestions;
    if (!qList.length) {
      document.getElementById('practice-question-text').textContent = 'No questions match the selected filters. Please adjust criteria.';
      document.getElementById('practice-options').innerHTML = '';
      document.getElementById('practice-explanation-box').classList.add('hidden');
      return;
    }

    const q = qList[state.practice.currentIndex];
    const cardEl = document.getElementById('practice-card');

    // Meta bar
    document.getElementById('practice-q-num').textContent = `Question ${state.practice.currentIndex + 1} of ${qList.length}`;
    
    const catBadge = document.getElementById('practice-category-badge');
    catBadge.textContent = formatCategory(q.category);

    const diffBadge = document.getElementById('practice-difficulty-badge');
    diffBadge.textContent = q.difficulty;
    diffBadge.className = `chip chip-difficulty diff-${q.difficulty}`;

    const srcBadge = document.getElementById('practice-source-badge');
    srcBadge.textContent = formatSource(q.source);

    // Reference
    document.getElementById('practice-ref-text').innerHTML = `<i class="fa-solid fa-book-bookmark"></i> Reference: ${escapeHTML(q.text_reference)} [${q.skill_tested}]`;

    // Prompt Text
    document.getElementById('practice-question-text').innerHTML = escapeHTML(q.question);

    // Bookmark icon status
    updatePracticeBookmarkIcon(q.id);

    // Options rendering (shuffled + re-lettered to prevent giveaways)
    const optionsContainer = document.getElementById('practice-options');
    optionsContainer.innerHTML = '';

    const answeredChoice = state.practice.userAnswers[q.id]; // stored as original option string
    const explanationBox = document.getElementById('practice-explanation-box');
    const shuffledOpts = getShuffledOptions(q);

    shuffledOpts.forEach(sOpt => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';

      btn.innerHTML = `
        <span class="option-letter">${sOpt.letter}</span>
        <span class="option-content">${escapeHTML(sOpt.text)}</span>
      `;

      if (answeredChoice) {
        btn.disabled = true;
        if (sOpt.originalOption === q.correct_answer) {
          btn.classList.add('correct');
        } else if (sOpt.originalOption === answeredChoice) {
          btn.classList.add('wrong');
        }
      } else {
        btn.addEventListener('click', () => handlePracticeAnswer(q, sOpt.originalOption));
      }

      optionsContainer.appendChild(btn);
    });

    // Explanation Box state
    if (answeredChoice) {
      explanationBox.classList.remove('hidden');
      const isCorrect = (answeredChoice === q.correct_answer);
      const statusTitle = document.getElementById('explanation-title');
      const statusIcon = document.getElementById('explanation-icon');

      if (isCorrect) {
        statusTitle.textContent = 'Correct Answer!';
        statusTitle.parentElement.className = 'explanation-status correct';
        statusIcon.className = 'fa-solid fa-circle-check';
      } else {
        const correctLetter = getShuffledCorrectLetter(q);
        statusTitle.textContent = `Incorrect! Correct answer is: ${correctLetter}`;
        statusTitle.parentElement.className = 'explanation-status wrong';
        statusIcon.className = 'fa-solid fa-circle-xmark';
      }

      document.getElementById('practice-explanation-text').innerHTML = escapeHTML(q.explanation);
    } else {
      explanationBox.classList.add('hidden');
    }

    // Tally update
    document.getElementById('practice-score-tally').textContent = 
      `Answered: ${state.practice.totalAnswered} | Score: ${state.practice.score}`;

    // Button states
    document.getElementById('practice-prev-btn').disabled = (state.practice.currentIndex === 0);
    document.getElementById('practice-next-btn').disabled = (state.practice.currentIndex === qList.length - 1);
  }

  function handlePracticeAnswer(question, selectedOption) {
    if (state.practice.userAnswers[question.id]) return;

    state.practice.userAnswers[question.id] = selectedOption;
    state.practice.totalAnswered++;

    const isCorrect = (selectedOption === question.correct_answer);
    if (isCorrect) {
      state.practice.score++;
      state.progress.totalCorrect++;
    } else {
      // Automatically add to saved mistakes for targeted review
      if (!state.progress.savedMistakes.includes(question.id)) {
        state.progress.savedMistakes.push(question.id);
      }
    }
    state.progress.totalAttempted++;
    saveProgress();

    renderPracticeQuestion();
  }

  function togglePracticeBookmark() {
    const qList = state.practice.filteredQuestions;
    if (!qList.length) return;
    const q = qList[state.practice.currentIndex];

    const idx = state.progress.savedMistakes.indexOf(q.id);
    if (idx > -1) {
      state.progress.savedMistakes.splice(idx, 1);
    } else {
      state.progress.savedMistakes.push(q.id);
    }
    saveProgress();
    updatePracticeBookmarkIcon(q.id);
  }

  function updatePracticeBookmarkIcon(qId) {
    const btn = document.getElementById('practice-bookmark');
    if (!btn) return;
    const isBookmarked = state.progress.savedMistakes.includes(qId);
    btn.innerHTML = isBookmarked ? 
      '<i class="fa-solid fa-bookmark text-amber"></i>' : 
      '<i class="fa-regular fa-bookmark"></i>';
  }

  // ==========================================
  // 2. TIMED CBT EXAM SIMULATOR
  // ==========================================
  function initExamSimulator() {
    const startExamBtn = document.getElementById('start-exam-btn');
    const submitEarlyBtn = document.getElementById('submit-exam-early-btn');
    const confirmModal = document.getElementById('confirm-submit-modal');
    const cancelModalBtn = document.getElementById('modal-cancel-btn');
    const confirmModalBtn = document.getElementById('modal-confirm-btn');

    const prevBtn = document.getElementById('exam-prev-btn');
    const nextBtn = document.getElementById('exam-next-btn');
    const clearBtn = document.getElementById('exam-clear-choice-btn');
    const flagBtn = document.getElementById('exam-flag-btn');

    const retakeBtn = document.getElementById('retake-exam-btn');
    const saveMistakesBtn = document.getElementById('save-mistakes-to-practice-btn');

    if (startExamBtn) {
      startExamBtn.addEventListener('click', launchExamSession);
    }

    if (submitEarlyBtn) {
      submitEarlyBtn.addEventListener('click', showSubmitConfirmationModal);
    }

    if (cancelModalBtn) {
      cancelModalBtn.addEventListener('click', () => confirmModal.classList.add('hidden'));
    }

    if (confirmModalBtn) {
      confirmModalBtn.addEventListener('click', () => {
        confirmModal.classList.add('hidden');
        finishExamSession();
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.exam.currentIndex > 0) {
          state.exam.currentIndex--;
          renderExamQuestion();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.exam.currentIndex < state.exam.questions.length - 1) {
          state.exam.currentIndex++;
          renderExamQuestion();
        }
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener('click', () => {
        const q = state.exam.questions[state.exam.currentIndex];
        delete state.exam.userAnswers[q.id];
        renderExamQuestion();
        renderExamPalette();
      });
    }

    if (flagBtn) {
      flagBtn.addEventListener('click', () => {
        const q = state.exam.questions[state.exam.currentIndex];
        if (state.exam.flagged.has(q.id)) {
          state.exam.flagged.delete(q.id);
        } else {
          state.exam.flagged.add(q.id);
        }
        renderExamQuestion();
        renderExamPalette();
      });
    }

    if (retakeBtn) {
      retakeBtn.addEventListener('click', () => {
        document.getElementById('exam-results-stage').classList.add('hidden');
        document.getElementById('exam-lobby').classList.remove('hidden');
      });
    }

    if (saveMistakesBtn) {
      saveMistakesBtn.addEventListener('click', () => {
        alert('All missed questions have been saved to your Weak Areas deck for revision!');
        // switch tab to analytics
        document.querySelector('.nav-tab[data-tab="analytics"]').click();
      });
    }

    // Review Filters
    const reviewAllBtn = document.getElementById('filter-review-all');
    const reviewWrongBtn = document.getElementById('filter-review-wrong');
    if (reviewAllBtn && reviewWrongBtn) {
      reviewAllBtn.addEventListener('click', () => {
        reviewAllBtn.classList.add('active');
        reviewWrongBtn.classList.remove('active');
        renderExamReviewList(false);
      });
      reviewWrongBtn.addEventListener('click', () => {
        reviewWrongBtn.classList.add('active');
        reviewAllBtn.classList.remove('active');
        renderExamReviewList(true);
      });
    }
  }

  function launchExamSession() {
    const qCount = parseInt(document.getElementById('exam-q-count').value, 10) || 32;
    const durationMinutes = parseInt(document.getElementById('exam-duration').value, 10) || 20;
    const mixType = document.getElementById('exam-mix').value;

    let pool = [];
    if (mixType === 'ca_focused') {
      const caItems = state.allQuestions.filter(q => q.source === 'CA');
      const otherItems = state.allQuestions.filter(q => q.source !== 'CA');
      pool = [...caItems, ...shuffleArray(otherItems)];
    } else if (mixType === 'balanced') {
      // Draw balanced quotas across primary domains
      const dramaQ = shuffleArray(state.allQuestions.filter(q => q.category === 'drama')).slice(0, 6);
      const novelQ = shuffleArray(state.allQuestions.filter(q => q.category === 'novel')).slice(0, 6);
      const poemQ = shuffleArray(state.allQuestions.filter(q => q.category === 'poem')).slice(0, 6);
      const soundQ = shuffleArray(state.allQuestions.filter(q => q.category === 'sound')).slice(0, 5);
      const stressQ = shuffleArray(state.allQuestions.filter(q => q.category === 'stress')).slice(0, 5);
      const otherQ = shuffleArray(state.allQuestions.filter(q => ['intonation', 'literary_terms', 'writing_skills'].includes(q.category))).slice(0, 4);
      pool = shuffleArray([...dramaQ, ...novelQ, ...poemQ, ...soundQ, ...stressQ, ...otherQ]);
    } else {
      pool = shuffleArray([...state.allQuestions]);
    }

    state.exam.questions = pool.slice(0, qCount);
    state.exam.currentIndex = 0;
    state.exam.userAnswers = {};
    state.exam.flagged.clear();
    state.exam.active = true;
    state.exam.remainingSeconds = durationMinutes * 60;
    state.exam.totalSeconds = durationMinutes * 60;

    // View swap
    document.getElementById('exam-lobby').classList.add('hidden');
    document.getElementById('exam-results-stage').classList.add('hidden');
    document.getElementById('exam-stage').classList.remove('hidden');

    startExamTimer();
    renderExamQuestion();
    renderExamPalette();
  }

  function startExamTimer() {
    clearInterval(state.exam.timerInterval);
    updateTimerDisplay();

    state.exam.timerInterval = setInterval(() => {
      state.exam.remainingSeconds--;
      updateTimerDisplay();

      if (state.exam.remainingSeconds <= 0) {
        clearInterval(state.exam.timerInterval);
        alert('Time is up! Your examination is being automatically submitted.');
        finishExamSession();
      }
    }, 1000);
  }

  function updateTimerDisplay() {
    const timerText = document.getElementById('exam-timer-display');
    const timerBox = document.getElementById('timer-box');
    if (!timerText) return;

    const m = Math.floor(state.exam.remainingSeconds / 60);
    const s = state.exam.remainingSeconds % 60;
    timerText.textContent = `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;

    if (state.exam.remainingSeconds < 180) { // under 3 minutes
      timerBox.classList.add('warning');
    } else {
      timerBox.classList.remove('warning');
    }
  }

  function renderExamQuestion() {
    const q = state.exam.questions[state.exam.currentIndex];
    if (!q) return;

    document.getElementById('exam-current-q-num').textContent = `Question ${state.exam.currentIndex + 1} of ${state.exam.questions.length}`;
    document.getElementById('exam-category-chip').textContent = formatCategory(q.category);
    
    const diffChip = document.getElementById('exam-diff-chip');
    diffChip.textContent = q.difficulty;
    diffChip.className = `chip chip-difficulty diff-${q.difficulty}`;

    document.getElementById('exam-ref-display').innerHTML = `<i class="fa-solid fa-book-bookmark"></i> Reference: ${escapeHTML(q.text_reference)}`;
    document.getElementById('exam-question-text').innerHTML = escapeHTML(q.question);

    // Flag button status
    const flagBtn = document.getElementById('exam-flag-btn');
    if (state.exam.flagged.has(q.id)) {
      flagBtn.classList.add('flagged');
      flagBtn.innerHTML = '<i class="fa-solid fa-flag"></i> Flagged';
    } else {
      flagBtn.classList.remove('flagged');
      flagBtn.innerHTML = '<i class="fa-regular fa-flag"></i> Flag';
    }

    // Render Options (shuffled + re-lettered, no instant feedback in exam mode!)
    const container = document.getElementById('exam-options-container');
    container.innerHTML = '';
    const selected = state.exam.userAnswers[q.id]; // stored as original option string
    const shuffledOpts = getShuffledOptions(q);

    shuffledOpts.forEach(sOpt => {
      const btn = document.createElement('button');
      btn.className = 'option-btn';
      if (selected === sOpt.originalOption) {
        btn.classList.add('selected');
      }

      btn.innerHTML = `
        <span class="option-letter">${sOpt.letter}</span>
        <span class="option-content">${escapeHTML(sOpt.text)}</span>
      `;

      btn.addEventListener('click', () => {
        state.exam.userAnswers[q.id] = sOpt.originalOption;
        renderExamQuestion();
        renderExamPalette();
      });

      container.appendChild(btn);
    });

    // Nav buttons
    document.getElementById('exam-prev-btn').disabled = (state.exam.currentIndex === 0);
    document.getElementById('exam-next-btn').disabled = (state.exam.currentIndex === state.exam.questions.length - 1);
  }

  function renderExamPalette() {
    const grid = document.getElementById('exam-palette-grid');
    grid.innerHTML = '';

    let answeredCount = 0;

    state.exam.questions.forEach((q, idx) => {
      const btn = document.createElement('button');
      btn.className = 'palette-btn';
      btn.textContent = idx + 1;

      if (idx === state.exam.currentIndex) {
        btn.classList.add('active');
      }

      const isAnswered = Boolean(state.exam.userAnswers[q.id]);
      const isFlagged = state.exam.flagged.has(q.id);

      if (isAnswered) {
        btn.classList.add('answered');
        answeredCount++;
      }
      if (isFlagged) {
        btn.classList.add('flagged');
      }

      btn.addEventListener('click', () => {
        state.exam.currentIndex = idx;
        renderExamQuestion();
        renderExamPalette();
      });

      grid.appendChild(btn);
    });

    document.getElementById('palette-answered-count').textContent = `${answeredCount} / ${state.exam.questions.length}`;
    document.getElementById('palette-flagged-count').textContent = state.exam.flagged.size;
  }

  function showSubmitConfirmationModal() {
    const total = state.exam.questions.length;
    const answered = Object.keys(state.exam.userAnswers).length;
    const unanswered = total - answered;

    const summaryText = document.getElementById('modal-submit-summary');
    summaryText.textContent = `You have answered ${answered} out of ${total} questions. ${unanswered > 0 ? `${unanswered} question(s) remain unanswered.` : 'All questions answered!'}`;

    document.getElementById('confirm-submit-modal').classList.remove('hidden');
  }

  function finishExamSession() {
    clearInterval(state.exam.timerInterval);
    state.exam.active = false;

    let correctCount = 0;
    const totalQ = state.exam.questions.length;
    const categoryStats = {};

    state.exam.questions.forEach(q => {
      const chosen = state.exam.userAnswers[q.id];
      const isCorrect = (chosen === q.correct_answer);

      if (isCorrect) correctCount++;
      else {
        // Log to saved mistakes
        if (!state.progress.savedMistakes.includes(q.id)) {
          state.progress.savedMistakes.push(q.id);
        }
      }

      // Track category stats
      if (!categoryStats[q.category]) {
        categoryStats[q.category] = { correct: 0, total: 0 };
      }
      categoryStats[q.category].total++;
      if (isCorrect) categoryStats[q.category].correct++;
    });

    const elapsedSeconds = state.exam.totalSeconds - Math.max(0, state.exam.remainingSeconds);
    const scorePercent = Math.round((correctCount / totalQ) * 100);
    // UI LMS scales to 35 marks
    const lmsGrade = ((correctCount / totalQ) * 35).toFixed(2);

    // Save to history
    const record = {
      date: new Date().toISOString(),
      score: correctCount,
      total: totalQ,
      percent: scorePercent,
      lmsGrade: lmsGrade,
      timeSpentSec: elapsedSeconds
    };
    state.progress.examHistory.unshift(record);
    state.progress.totalAttempted += totalQ;
    state.progress.totalCorrect += correctCount;
    saveProgress();

    // Show Results View
    document.getElementById('exam-stage').classList.add('hidden');
    const resultsStage = document.getElementById('exam-results-stage');
    resultsStage.classList.remove('hidden');

    document.getElementById('results-score-percent').textContent = `${scorePercent}%`;
    document.getElementById('results-meta-summary').innerHTML = 
      `You scored <strong>${correctCount} out of ${totalQ}</strong> (Equivalent to <strong>${lmsGrade} / 35.0 marks</strong> on UI LMS Central Test scale).`;
    
    document.getElementById('res-correct-count').textContent = correctCount;
    document.getElementById('res-wrong-count').textContent = (totalQ - correctCount);
    
    const m = Math.floor(elapsedSeconds / 60);
    const s = elapsedSeconds % 60;
    document.getElementById('res-time-spent').textContent = `${m}m ${s}s`;

    const heading = document.getElementById('results-grade-heading');
    if (scorePercent >= 80) heading.textContent = '🌟 Outstanding Mastery! (First Class Grade)';
    else if (scorePercent >= 65) heading.textContent = '👏 Great Job! (Strong Second Class Upper)';
    else if (scorePercent >= 50) heading.textContent = '👍 Good Effort! Keep practicing weak areas.';
    else heading.textContent = '⚠️ Revision Needed. Review your mistakes below.';

    // Render Category Breakdown Bars
    renderCategoryBars(categoryStats);

    // Render Detailed Review
    renderExamReviewList(false);
  }

  function renderCategoryBars(catStats) {
    const container = document.getElementById('results-category-bars');
    container.innerHTML = '';

    for (const [cat, data] of Object.entries(catStats)) {
      const pct = Math.round((data.correct / data.total) * 100);
      const div = document.createElement('div');
      div.className = 'cat-bar-item';
      div.innerHTML = `
        <div class="cat-bar-header">
          <span>${formatCategory(cat)}</span>
          <span>${data.correct}/${data.total} (${pct}%)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" style="width: ${pct}%"></div>
        </div>
      `;
      container.appendChild(div);
    }
  }

  function renderExamReviewList(mistakesOnly = false) {
    const list = document.getElementById('results-review-list');
    list.innerHTML = '';

    state.exam.questions.forEach((q, idx) => {
      const chosen = state.exam.userAnswers[q.id];
      const isCorrect = (chosen === q.correct_answer);

      if (mistakesOnly && isCorrect) return;

      const item = document.createElement('div');
      item.className = `review-item ${isCorrect ? 'correct' : 'wrong'}`;

      item.innerHTML = `
        <div class="review-question-title">
          <span>Q${idx + 1}. ${escapeHTML(q.question)}</span>
        </div>
        <div class="review-answer-grid">
          <div>
            <strong>Your Choice:</strong> 
            <span class="${isCorrect ? 'text-emerald' : 'text-rose'}">
              ${chosen ? escapeHTML(chosen) : '<em>Unanswered</em>'}
            </span>
          </div>
          <div>
            <strong>Correct Answer:</strong> 
            <span class="text-emerald"><strong>${escapeHTML(q.correct_answer)}</strong></span>
          </div>
        </div>
        <div class="explanation-content">
          <small><i class="fa-solid fa-circle-info"></i> ${escapeHTML(q.explanation)}</small>
        </div>
      `;

      list.appendChild(item);
    });
  }

  // ==========================================
  // 3. FLASHCARDS MODE
  // ==========================================
  function initFlashcards() {
    const catSelect = document.getElementById('fc-category-select');
    const cardEl = document.getElementById('flashcard-element');
    const flipBtn = document.getElementById('fc-flip-btn');
    const prevBtn = document.getElementById('fc-prev-btn');
    const nextBtn = document.getElementById('fc-next-btn');
    const shuffleBtn = document.getElementById('fc-shuffle-btn');

    function applyDeckFilter(shuffle = false) {
      const cat = catSelect.value;
      state.flashcards.deck = state.allQuestions.filter(q => (cat === 'all' || q.category === cat));
      if (shuffle) {
        state.flashcards.deck = shuffleArray([...state.flashcards.deck]);
      }
      state.flashcards.currentIndex = 0;
      state.flashcards.isFlipped = false;
      renderFlashcard();
    }

    if (catSelect) {
      catSelect.addEventListener('change', () => applyDeckFilter(false));
    }

    if (cardEl) {
      cardEl.addEventListener('click', toggleFlashcardFlip);
    }

    if (flipBtn) {
      flipBtn.addEventListener('click', toggleFlashcardFlip);
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (state.flashcards.currentIndex > 0) {
          state.flashcards.currentIndex--;
          state.flashcards.isFlipped = false;
          renderFlashcard();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (state.flashcards.currentIndex < state.flashcards.deck.length - 1) {
          state.flashcards.currentIndex++;
          state.flashcards.isFlipped = false;
          renderFlashcard();
        }
      });
    }

    if (shuffleBtn) {
      shuffleBtn.addEventListener('click', () => applyDeckFilter(true));
    }

    // Initial setup
    state.flashcards.deck = [...state.allQuestions];
    renderFlashcard();
  }

  function toggleFlashcardFlip() {
    const cardEl = document.getElementById('flashcard-element');
    state.flashcards.isFlipped = !state.flashcards.isFlipped;
    if (state.flashcards.isFlipped) {
      cardEl.classList.add('flipped');
    } else {
      cardEl.classList.remove('flipped');
    }
  }

  function renderFlashcard() {
    const deck = state.flashcards.deck;
    const cardEl = document.getElementById('flashcard-element');
    if (!deck.length) return;

    if (!state.flashcards.isFlipped) {
      cardEl.classList.remove('flipped');
    } else {
      cardEl.classList.add('flipped');
    }

    const q = deck[state.flashcards.currentIndex];

    // Counter
    document.getElementById('fc-counter').textContent = `Card ${state.flashcards.currentIndex + 1} of ${deck.length}`;

    // Front Face
    document.getElementById('fc-cat-badge').textContent = formatCategory(q.category);
    document.getElementById('fc-diff-badge').textContent = q.difficulty;
    document.getElementById('fc-ref').textContent = `Reference: ${q.text_reference}`;
    document.getElementById('fc-question').innerHTML = escapeHTML(q.question);

    // Back Face
    document.getElementById('fc-correct-answer').textContent = q.correct_answer;
    document.getElementById('fc-explanation').innerHTML = escapeHTML(q.explanation);
    document.getElementById('fc-skill').textContent = `Skill: ${q.skill_tested}`;

    // Nav buttons
    document.getElementById('fc-prev-btn').disabled = (state.flashcards.currentIndex === 0);
    document.getElementById('fc-next-btn').disabled = (state.flashcards.currentIndex === deck.length - 1);
  }

  // ==========================================
  // 4. QUESTION BANK BROWSER
  // ==========================================
  function initQuestionBank() {
    const searchInput = document.getElementById('bank-search-query');
    const catSelect = document.getElementById('bank-filter-category');
    const diffSelect = document.getElementById('bank-filter-difficulty');
    const srcSelect = document.getElementById('bank-filter-source');

    [searchInput, catSelect, diffSelect, srcSelect].forEach(el => {
      if (el) {
        el.addEventListener('input', renderBankList);
      }
    });

    renderBankList();
  }

  function renderBankList() {
    const searchVal = (document.getElementById('bank-search-query').value || '').toLowerCase();
    const catVal = document.getElementById('bank-filter-category').value;
    const diffVal = document.getElementById('bank-filter-difficulty').value;
    const srcVal = document.getElementById('bank-filter-source').value;

    const matched = state.allQuestions.filter(q => {
      const matchCat = (catVal === 'all') || (q.category === catVal);
      const matchDiff = (diffVal === 'all') || (q.difficulty === diffVal);
      const matchSrc = (srcVal === 'all') || (q.source === srcVal);

      const matchSearch = !searchVal || 
        q.question.toLowerCase().includes(searchVal) ||
        q.text_reference.toLowerCase().includes(searchVal) ||
        q.explanation.toLowerCase().includes(searchVal) ||
        q.options.some(opt => opt.toLowerCase().includes(searchVal));

      return matchCat && matchDiff && matchSrc && matchSearch;
    });

    document.getElementById('bank-match-count').textContent = `Showing ${matched.length} of ${state.allQuestions.length} questions`;

    const list = document.getElementById('bank-list-wrapper');
    list.innerHTML = '';

    // Render in chunks for high rendering speed (first 50)
    const toRender = matched.slice(0, 50);

    toRender.forEach(q => {
      const card = document.createElement('div');
      card.className = 'bank-card';

      // Bank browser also shows shuffled options for consistency
      const shuffledOpts = getShuffledOptions(q);
      const optionsHtml = shuffledOpts.map(sOpt => {
        const isCorrect = (sOpt.originalOption === q.correct_answer);
        return `<div class="bank-opt-item ${isCorrect ? 'is-correct' : ''}">${escapeHTML(sOpt.letter + '. ' + sOpt.text)}</div>`;
      }).join('');

      card.innerHTML = `
        <div class="bank-card-header">
          <div class="quiz-badges">
            <span class="chip chip-id">${q.id}</span>
            <span class="chip chip-category">${formatCategory(q.category)}</span>
            <span class="chip chip-difficulty">${q.difficulty}</span>
            <span class="chip chip-source">${formatSource(q.source)}</span>
          </div>
          <small class="text-dim">${escapeHTML(q.text_reference)}</small>
        </div>
        <div class="bank-q-text">${escapeHTML(q.question)}</div>
        <div class="bank-options-list">${optionsHtml}</div>
        <div class="bank-card-details">
          <strong><i class="fa-solid fa-circle-info"></i> Explanation:</strong> ${escapeHTML(q.explanation)}
        </div>
      `;

      list.appendChild(card);
    });

    if (matched.length > 50) {
      const note = document.createElement('div');
      note.className = 'empty-state';
      note.innerHTML = `<p>Showing first 50 results. Use the search box above to refine your query further.</p>`;
      list.appendChild(note);
    }
  }

  // ==========================================
  // 5. ANALYTICS & WEAK AREAS
  // ==========================================
  function initAnalytics() {
    const drillBtn = document.getElementById('start-mistakes-drill-btn');
    const clearMistakesBtn = document.getElementById('clear-mistakes-btn');
    const resetHistoryBtn = document.getElementById('reset-history-btn');

    if (drillBtn) {
      drillBtn.addEventListener('click', () => {
        if (!state.progress.savedMistakes.length) {
          alert('You have no saved mistakes logged yet!');
          return;
        }
        // Load only saved mistakes into practice mode
        const mistakeQuestions = state.allQuestions.filter(q => state.progress.savedMistakes.includes(q.id));
        state.practice.filteredQuestions = shuffleArray(mistakeQuestions);
        state.practice.currentIndex = 0;
        state.practice.userAnswers = {};
        state.practice.score = 0;
        state.practice.totalAnswered = 0;

        // Switch to practice tab
        document.querySelector('.nav-tab[data-tab="practice"]').click();
        renderPracticeQuestion();
      });
    }

    if (clearMistakesBtn) {
      clearMistakesBtn.addEventListener('click', () => {
        if (confirm('Clear all saved mistakes from your revision deck?')) {
          state.progress.savedMistakes = [];
          saveProgress();
          renderAnalytics();
        }
      });
    }

    if (resetHistoryBtn) {
      resetHistoryBtn.addEventListener('click', () => {
        if (confirm('Reset all exam history and performance statistics?')) {
          state.progress.examHistory = [];
          state.progress.totalAttempted = 0;
          state.progress.totalCorrect = 0;
          saveProgress();
          renderAnalytics();
        }
      });
    }

    renderAnalytics();
  }

  function renderAnalytics() {
    // Top metric cards
    document.getElementById('stats-total-attempted').textContent = state.progress.totalAttempted;
    
    const accuracy = state.progress.totalAttempted > 0 ?
      Math.round((state.progress.totalCorrect / state.progress.totalAttempted) * 100) : 0;
    document.getElementById('stats-overall-accuracy').textContent = `${accuracy}%`;

    document.getElementById('stats-exams-completed').textContent = state.progress.examHistory.length;
    document.getElementById('stats-saved-mistakes').textContent = state.progress.savedMistakes.length;

    // Render Saved Mistakes list
    const mistakesContainer = document.getElementById('mistakes-list-container');
    mistakesContainer.innerHTML = '';

    if (!state.progress.savedMistakes.length) {
      mistakesContainer.innerHTML = `
        <div class="empty-state">
          <i class="fa-solid fa-circle-check text-emerald"></i>
          <p>No mistakes logged yet! All answers are currently mastered.</p>
        </div>
      `;
    } else {
      const missedQs = state.allQuestions.filter(q => state.progress.savedMistakes.includes(q.id));
      missedQs.forEach(q => {
        const item = document.createElement('div');
        item.className = 'review-item wrong';
        item.style.marginBottom = '0.75rem';
        item.innerHTML = `
          <div class="review-question-title">${escapeHTML(q.question)}</div>
          <div style="font-size: 0.88rem; margin: 0.35rem 0;">
            <span class="text-emerald"><strong>Correct Answer:</strong> ${escapeHTML(q.correct_answer)}</span>
          </div>
          <div class="explanation-content"><small>${escapeHTML(q.explanation)}</small></div>
        `;
        mistakesContainer.appendChild(item);
      });
    }

    // Render Exam History list
    const historyContainer = document.getElementById('exam-history-list');
    historyContainer.innerHTML = '';

    if (!state.progress.examHistory.length) {
      historyContainer.innerHTML = `
        <div class="empty-state">
          <i class="fa-solid fa-stopwatch"></i>
          <p>No CBT mock attempts recorded yet. Launch the Timed CBT Exam to test your skills!</p>
        </div>
      `;
    } else {
      state.progress.examHistory.slice(0, 5).forEach((rec, idx) => {
        const item = document.createElement('div');
        item.className = 'cat-bar-item';
        const dateStr = new Date(rec.date).toLocaleDateString(undefined, {
          month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit'
        });
        const m = Math.floor(rec.timeSpentSec / 60);
        const s = rec.timeSpentSec % 60;

        item.innerHTML = `
          <div class="cat-bar-header">
            <strong>Attempt #${state.progress.examHistory.length - idx} (${dateStr})</strong>
            <span class="${rec.percent >= 70 ? 'text-emerald' : 'text-amber'}">${rec.score}/${rec.total} (${rec.percent}%) • ${rec.lmsGrade}/35</span>
          </div>
          <small class="text-dim">Time: ${m}m ${s}s</small>
        `;
        historyContainer.appendChild(item);
      });
    }
  }

  // ==========================================
  // Keyboard Shortcuts
  // ==========================================
  function initKeyboardShortcuts() {
    window.addEventListener('keydown', (e) => {
      // Don't trigger when typing in search input
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;

      const activeTab = document.querySelector('.nav-tab.active')?.getAttribute('data-tab');

      // Spacebar for flashcards
      if (activeTab === 'flashcards' && e.code === 'Space') {
        e.preventDefault();
        toggleFlashcardFlip();
        return;
      }

      // Arrows for flashcards
      if (activeTab === 'flashcards') {
        if (e.key === 'ArrowRight') {
          document.getElementById('fc-next-btn').click();
        } else if (e.key === 'ArrowLeft') {
          document.getElementById('fc-prev-btn').click();
        }
      }

      // Option keys (1-4 or A-D) in practice or exam
      if (['practice', 'exam'].includes(activeTab)) {
        let optIndex = -1;
        if (['1', 'a', 'A'].includes(e.key)) optIndex = 0;
        if (['2', 'b', 'B'].includes(e.key)) optIndex = 1;
        if (['3', 'c', 'C'].includes(e.key)) optIndex = 2;
        if (['4', 'd', 'D'].includes(e.key)) optIndex = 3;

        if (optIndex > -1) {
          const containerId = activeTab === 'practice' ? 'practice-options' : 'exam-options-container';
          const optionButtons = document.querySelectorAll(`#${containerId} .option-btn`);
          if (optionButtons[optIndex] && !optionButtons[optIndex].disabled) {
            optionButtons[optIndex].click();
          }
        }

        // Enter or ArrowRight for Next
        if (e.key === 'ArrowRight' || e.key === 'Enter') {
          const nextBtnId = activeTab === 'practice' ? 'practice-next-btn' : 'exam-next-btn';
          const nextBtn = document.getElementById(nextBtnId);
          if (nextBtn && !nextBtn.disabled) nextBtn.click();
        }
        if (e.key === 'ArrowLeft') {
          const prevBtnId = activeTab === 'practice' ? 'practice-prev-btn' : 'exam-prev-btn';
          const prevBtn = document.getElementById(prevBtnId);
          if (prevBtn && !prevBtn.disabled) prevBtn.click();
        }
      }
    });
  }

  // ==========================================
  // Helper Utilities
  // ==========================================
  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function formatCategory(cat) {
    const map = {
      drama: 'Drama (Synge)',
      novel: 'Prose (Emecheta)',
      poem: 'Selected Poems',
      sound: 'English Sounds',
      stress: 'Word Stress',
      intonation: 'Intonation',
      literary_terms: 'Literary Terms',
      writing_skills: 'Writing Skills',
      CA: 'Central Test (CA)'
    };
    return map[cat] || cat;
  }

  function formatSource(src) {
    const map = {
      CA: 'Real CA Test',
      textbook: 'Course Textbook',
      predicted: 'Predicted Exam'
    };
    return map[src] || src;
  }

  function escapeHTML(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  // Run application on DOM load
  document.addEventListener('DOMContentLoaded', initApp);

})();
