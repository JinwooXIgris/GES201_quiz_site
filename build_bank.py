"""
Builder script for GES 201 Question Bank (350+ Questions)
Strictly adheres to all course materials:
- Central Test / CA (C-UI-GES201)
- Textbook chapters (Dr. Akinjobi, Prof. Kehinde, Dr. Ojebuyi, Dr. Egbokhare)
- J.M. Synge's Riders to the Sea
- Buchi Emecheta's Second-Class Citizen
- Selected 8 Poems and extended anthology
"""
import json
import os

questions = []

def add_q(category, source, text_ref, skill, difficulty, q_text, opts, correct_letter, explanation, confidence="high"):
    q_id = f"q_{len(questions) + 1:03d}"
    formatted_opts = []
    correct_opt_str = ""
    for letter, opt in zip(["A", "B", "C", "D"], opts):
        entry = f"{letter}. {opt}"
        formatted_opts.append(entry)
        if letter == correct_letter:
            correct_opt_str = entry

    questions.append({
        "id": q_id,
        "category": category,
        "source": source,
        "text_reference": text_ref,
        "skill_tested": skill,
        "difficulty": difficulty,
        "question": q_text,
        "options": formatted_opts,
        "correct_answer": correct_opt_str,
        "explanation": explanation,
        "confidence": confidence
    })

# ==========================================
# 1. ACTUAL CENTRAL TEST (CA) QUESTIONS (32 Questions)
# ==========================================
add_q("drama", "CA", "Riders to the Sea", "literary_analysis", "medium",
      "How does Synge present the relationship between humans and nature in his Riders to the Sea?",
      ["Nature is powerful and indifferent", "Nature is supportive", "Humans and nature are equal", "Humans control nature"],
      "A", "In Riders to the Sea, Synge depicts the ocean as an omnipotent, uncaring natural force that relentlessly destroys human life regardless of prayers or morality.")

add_q("drama", "CA", "Riders to the Sea", "literary_conflict", "easy",
      "What is the main conflict in J.M. Synge’s Riders to the Sea?",
      ["Humans vs. nature", "Tradition vs. modernity", "Rich vs. poor", "Family vs. neighbors"],
      "A", "The tragedy centers fundamentally on the struggle between the vulnerable island inhabitants and the merciless sea.")

add_q("novel", "CA", "Second-Class Citizen (Chapter 1)", "thematic_analysis", "easy",
      "In Buchi Emecheta’s Second-Class Citizen, the statement that Adah’s birth is not recorded because 'she was a girl' foregrounds the theme of...",
      ["political oppression", "gender discrimination", "racism", "migration"],
      "B", "The deliberate omission of recording Adah's birth date purely because of her female sex directly highlights patriarchal gender discrimination in society.")

add_q("stress", "CA", "Morphology & Stress Rules", "word_stress", "medium",
      "Place the primary stress on this word: UNPROFESSIONAL",
      ["un-pro-fes-SION-nal", "un-pro-FES-sion-nal", "un-PRO-fes-sion-nal", "un-pro-fes-sion-NAL"],
      "B", "The negative prefix 'un-' and the suffix '-al' do not shift root stress; 'proFESsion' retains primary stress on the second syllable of the root.")

add_q("literary_terms", "CA", "Textbook Ch 3 (p. 53)", "genre_classification", "easy",
      "Prose is broadly divided into two categories. What are they?",
      ["Fiction and non-fiction", "flash fiction and snappy narrative", "biography and autobiography", "play and novel"],
      "A", "According to the course text (Prof. Kehinde, p. 53), prose works are broadly classified into fiction (imagined narratives) and non-fiction (factual accounts).")

add_q("stress", "CA", "Suffix Stress Rules (-ology)", "word_stress", "medium",
      "Place the primary stress on this word: AUDIOLOGY",
      ["au-di-O-lo-gy", "au-DI-o-lo-gy", "au-di-o-LO-gy", "AU-di-o-lo-gy"],
      "A", "Words ending in the suffix '-ology' take primary stress on the antepenultimate syllable (the vowel 'o' immediately preceding -logy): au-di-O-lo-gy.")

add_q("sound", "CA", "Vowel Phonemes", "vowel_identification", "medium",
      "Choose the word that contains the vowel sound represented by the given phonetic symbol: /e/",
      ["legal", "settler", "vehicle", "pea"],
      "B", "'Settler' contains the short front vowel /e/ in its initial syllable. In contrast, 'legal' (/iː/), 'vehicle' (/iː/), and 'pea' (/iː/) feature long /iː/.")

add_q("sound", "CA", "Inflectional Phonology (-ed)", "consonant_identification", "medium",
      "Choose the option that has the same consonant sound as the one emphasised: psychED",
      ["wanted", "thorough", "asked", "both"],
      "C", "In 'psyched' the root ends in voiceless /k/, so '-ed' is pronounced /t/. 'Asked' also ends in /kt/ (/t/), while 'wanted' is /-ɪd/, and 'thorough'/'both' feature /θ/.")

add_q("drama", "CA", "Riders to the Sea", "philosophical_theme", "medium",
      "What lesson can be drawn from Maurya’s final words in J.M. Synge’s Riders to the Sea?",
      ["Religion solves all problems", "Death is unavoidable and must be accepted", "People should avoid the sea", "Wealth is more important than life"],
      "B", "Maurya's concluding assertion ('No man at all can be living for ever, and we must be satisfied') reflects stoic resignation and acceptance of mortality.")

add_q("drama", "CA", "Riders to the Sea", "plot_comprehension", "easy",
      "What causes Bartley’s death in J.M. Synge’s Riders to the Sea?",
      ["A storm", "A boat accident", "The gray pony knocks him into the sea", "Illness"],
      "C", "As reported by the islanders, while Bartley was riding the red mare, the gray pony he was leading knocked him over the cliff into the sea where the surf swept him away.")

add_q("drama", "CA", "Riders to the Sea", "symbolism", "easy",
      "What does the sea mainly represent in J.M. Synge’s Riders to the Sea?",
      ["Freedom", "Adventure", "Wealth", "Death and danger"],
      "D", "The sea functions as a lethal antagonist embodying inescapable death, catastrophe, and cosmic peril.")

add_q("novel", "CA", "Second-Class Citizen", "irony_analysis", "medium",
      "One major irony in Buchi Emecheta’s Second-Class Citizen is that...",
      ["Adah never becomes educated", "Adah refuses to travel abroad", "education does not automatically eradicate patriarchal attitudes", "Francis becomes poorer in England"],
      "C", "Despite Francis obtaining Western schooling and migrating to Britain, his mindset remains entrenched in patriarchal subjugation and abusive entitlement.")

add_q("literary_terms", "CA", "Textbook Ch 3 (p. 53)", "figures_of_speech", "easy",
      "A figure of speech where a part of something represents the whole thing or vice versa is called _______.",
      ["Metonymy", "Simile", "Synecdoche", "Symbolism"],
      "C", "Synecdoche is the precise rhetorical device wherein a part represents the whole (e.g., 'all hands on deck', 'twenty sails') or whole for a part.")

add_q("stress", "CA", "Suffix Stress Rules (-tion)", "word_stress", "easy",
      "Place the primary stress on this word: FALSIFICATION",
      ["FAL-si-fi-ca-tion", "fal-s-i-FI-ca-tion", "fal-si-fi-CA-tion", "fal-sI-fi-ca-tion"],
      "C", "English words ending in '-tion' consistently take primary stress on the penultimate syllable immediately before the suffix: fal-si-fi-CA-tion.")

add_q("drama", "CA", "Riders to the Sea", "plot_comprehension", "medium",
      "What is Maurya doing when she goes out in J.M. Synge’s Riders to the Sea?",
      ["Visiting the priest", "Trying to bless Bartley", "Going to the market", "Looking for fish"],
      "B", "Maurya leaves the cottage carrying bread and Michael's staff to intercept Bartley at the spring well and bestow the mother's blessing she initially withheld.")

add_q("novel", "CA", "Second-Class Citizen", "characterization", "medium",
      "Adah’s mother in Buchi Emecheta’s Second-Class Citizen can best be described as...",
      ["entirely cruel and heartless", "politically radical", "a product of patriarchal conditioning and societal expectations", "economically independent"],
      "C", "Adah's mother enforces patriarchal norms not necessarily out of intrinsic malice, but because her consciousness has been thoroughly shaped by societal gender conditioning.")

add_q("drama", "CA", "Riders to the Sea", "setting", "easy",
      "J.M. Synge’s Riders to the Sea is set where?",
      ["Dublin", "Scotland", "London", "An island off the west of Ireland"],
      "D", "The drama is explicitly set in an Aran Islands cottage off the rugged western coast of Ireland.")

add_q("sound", "CA", "Consonant Phonemes & Silent Letters", "consonant_identification", "medium",
      "Choose the word that contains the consonant sound represented by the given phonetic symbol: /t/",
      ["worth", "subtle", "warmed", "depot"],
      "B", "In 'subtle' (/ˈsʌt.əl/), the letter 'b' is silent and 't' realizes /t/. In 'warmed' '-ed' is /d/, in 'depot' 't' is silent (/ˈdep.əʊ/), and 'worth' ends in /θ/.")

add_q("poem", "CA", "My Heart Leaps Up (Wordsworth)", "figures_of_speech", "easy",
      "\"The Child is father of the Man\" is an example of ---",
      ["paradox", "hyperbole", "metaphor", "irony"],
      "A", "The phrase appears contradictory on the surface, but reveals the profound truth that childhood experiences mold adult moral character, making it a classic paradox.")

add_q("novel", "CA", "Second-Class Citizen", "thematic_analysis", "medium",
      "Francis’s refusal to support Adah’s ambitions in Buchi Emecheta’s Second-Class Citizen demonstrates...",
      ["intellectual superiority", "religious intolerance", "political rebellion", "toxic masculinity and insecurity"],
      "D", "Francis sabotages Adah's career and literary aspirations because her competence threatens his fragile ego and patriarchal dominance.")

add_q("drama", "CA", "Riders to the Sea", "character_motivation", "easy",
      "In J.M. Synge’s Riders to the Sea, what does Maurya fear most?",
      ["Losing Bartley to the sea", "Lack of food", "Losing her husband to the pirates", "Hunger"],
      "A", "Maurya is tormented by the impending reality of losing Bartley, her last surviving male offspring, to the predatory ocean.")

add_q("novel", "CA", "Second-Class Citizen (Chapter 6)", "historical_social_context", "easy",
      "The phrase “Sorry, No Coloureds” in Buchi Emecheta’s Second-Class Citizen chiefly exposes...",
      ["institutional racism in Britain", "educational inequality", "tribal prejudice in Nigeria", "marital instability"],
      "A", "This sign, encountered by Adah while house-hunting in London, reflects rampant color-bar and housing discrimination in post-war Britain.")

add_q("novel", "CA", "Second-Class Citizen", "thematic_analysis", "easy",
      "Which of the following themes is LEAST central to Buchi Emecheta’s Second-Class Citizen?",
      ["Patriarchy", "Migration", "Environmental degradation", "Racism"],
      "C", "The novel focuses on gender discrimination, race, migration, and domestic struggle; environmental degradation is not treated in the work.")

add_q("sound", "CA", "Consonant Phonemes (/ʒ/)", "consonant_identification", "medium",
      "Choose the word that contains the consonant sound represented by the given phonetic symbol: /ʒ/",
      ["join", "mirage", "knowledge", "hedge"],
      "B", "'Mirage' (/mɪˈrɑːʒ/) ends with the voiced palato-alveolar fricative /ʒ/. 'Join', 'knowledge', and 'hedge' all feature the voiced affricate /dʒ/.")

add_q("stress", "CA", "Suffix Stress Rules (-ic)", "word_stress", "easy",
      "Place the primary stress on this word: DEMOCRATIC",
      ["de-mo-cra-TIC", "de-mo-CRA-tic", "de-MO-cra-tic", "DE-mo-cra-tic"],
      "B", "The adjectival suffix '-ic' pulls primary stress onto the penultimate syllable: de-mo-CRA-tic.")

add_q("drama", "CA", "Riders to the Sea", "cultural_context", "medium",
      "As indicated in J.M. Synge’s Riders to the Sea, what does Maurya’s statement about young men leaving things behind suggest about their society?",
      ["Old people are wealthy", "People do not value family", "Death of young men is common", "Young people are careless"],
      "C", "Her lament highlights the grim demographic reality of the island: premature maritime death is so frequent that the elderly outlive the youth.")

add_q("literary_terms", "CA", "Textbook Ch 3 (p. 61)", "dramatic_devices", "easy",
      "Playwrights deploy ______ to ease tension in tragedy.",
      ["comic relief", "comic release", "humour", "comedy"],
      "A", "Comic relief is the standard technical literary term for introducing humorous episodes to ease tragic tension.")

add_q("drama", "CA", "Riders to the Sea", "setting_and_occupation", "easy",
      "What is the main occupation of the family that is represented in J.M. Synge’s Riders to the Sea?",
      ["Trading", "Teaching", "Farming", "Fishing and sea-faring"],
      "D", "The family and island community depend entirely on fishing, animal husbandry, and maritime seafaring for survival.")

add_q("literary_terms", "CA", "Textbook Ch 3 (p. 45)", "narrative_devices", "easy",
      "A clue to an event that will happen later in a work of art is _____________",
      ["flashforward", "prospect", "foreshadowing", "flashback"],
      "C", "Foreshadowing refers to hints or clues inserted by an author to prefigure upcoming narrative events.")

add_q("novel", "CA", "Second-Class Citizen", "thematic_vision", "medium",
      "Which statement best summarises the feminist vision of Buchi Emecheta’s Second-Class Citizen?",
      ["Women must struggle against structures that limit their humanity and potential.", "African traditions should never be questioned.", "Marriage is the ultimate fulfilment for women.", "Women should reject education for motherhood."],
      "A", "Emecheta's protagonist demonstrates that women must resist institutional and domestic patriarchal barriers to achieve personal selfhood and autonomy.")

add_q("stress", "CA", "Suffix Stress Rules (-ious)", "word_stress", "hard",
      "Place the primary stress on this word: LASCIVIOUS",
      ["la-SCI-vi-ous", "la-sci-VI-ous", "LA-sci-vi-ous", "la-sci-vi-OUS"],
      "A", "In words ending in '-ious', the primary stress falls on the antepenultimate syllable (or penultimate before the diphthong glide): la-SCI-vi-ous.")

add_q("literary_terms", "CA", "Textbook Ch 3 (p. 61)", "genre_definition", "easy",
      "A genre of literature that directly imitates human action on stage is __________",
      ["drama", "prose", "comedy", "poetry"],
      "A", "Drama is distinctively defined by its performance on stage through direct imitation (mimesis) of human actions by living actors.")

print(f"Added {len(questions)} CA questions.")
