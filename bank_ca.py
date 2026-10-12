"""
Central Test (CA) Questions - Verbatim from UI LMS CBT 2025/2026
"""

def get_ca_questions():
    raw = [
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "literary_analysis", "difficulty": "medium",
            "question": "How does Synge present the relationship between humans and nature in his Riders to the Sea?",
            "options": ["Nature is powerful and indifferent", "Nature is supportive", "Humans and nature are equal", "Humans control nature"],
            "correct_letter": "A",
            "explanation": "In Riders to the Sea, Synge portrays nature (the sea) as an omnipotent, uncaring force that inexorably claims human lives."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "literary_conflict", "difficulty": "easy",
            "question": "What is the main conflict in J.M. Synge’s Riders to the Sea?",
            "options": ["Humans vs. nature", "Tradition vs. modernity", "Rich vs. poor", "Family vs. neighbors"],
            "correct_letter": "A",
            "explanation": "The central drama revolves around the struggle of islanders to survive against the destructive power of the sea."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen (Chapter 1)",
            "skill_tested": "thematic_analysis", "difficulty": "easy",
            "question": "In Buchi Emecheta’s Second-Class Citizen, the statement that Adah’s birth is not recorded because “she was a girl” foregrounds the theme of.....",
            "options": ["political oppression", "gender discrimination", "racism", "migration"],
            "correct_letter": "B",
            "explanation": "Omitting Adah's birth record because she was female directly establishes patriarchal gender discrimination."
        },
        {
            "category": "stress", "source": "CA", "text_reference": "Textbook Ch 2 (Prefixation)",
            "skill_tested": "word_stress", "difficulty": "medium",
            "question": "Place the primary stress on this word: UNPROFESSIONAL",
            "options": ["un-pro-fes-SION-nal", "un-pro-FES-sion-nal", "un-PRO-fes-sion-nal", "un-pro-fes-sion-NAL"],
            "correct_letter": "B",
            "explanation": "The prefix 'un-' and suffix '-al' do not change the root stress; 'proFESsion' retains stress on the second syllable."
        },
        {
            "category": "literary_terms", "source": "CA", "text_reference": "Textbook Ch 3 (p. 53)",
            "skill_tested": "genre_classification", "difficulty": "easy",
            "question": "Prose is broadly divided into two categories. What are they?",
            "options": ["Fiction and non-fiction", "flash fiction and snappy narrative", "biography and autobiography", "play and novel"],
            "correct_letter": "A",
            "explanation": "The course textbook explicitly states that prose works are broadly classified into fiction and non-fiction."
        },
        {
            "category": "stress", "source": "CA", "text_reference": "Textbook Ch 2 (Suffix -ology)",
            "skill_tested": "word_stress", "difficulty": "medium",
            "question": "Place the primary stress on this word: AUDIOLOGY",
            "options": ["au-di-O-lo-gy", "au-DI-o-lo-gy", "au-di-o-LO-gy", "AU-di-o-lo-gy"],
            "correct_letter": "A",
            "explanation": "Suffix '-ology' places primary stress on the antepenultimate syllable (on the 'o' before -logy): au-di-O-lo-gy."
        },
        {
            "category": "sound", "source": "CA", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Choose the word that contains the vowel sound represented by the given phonetic symbol: /e/",
            "options": ["legal", "settler", "vehicle", "pea"],
            "correct_letter": "B",
            "explanation": "'Settler' contains the short front vowel /e/. 'Legal' (/iː/), 'vehicle' (/iː/), and 'pea' (/iː/) have long /iː/."
        },
        {
            "category": "sound", "source": "CA", "text_reference": "Textbook Ch 2 (Morpheme -ed)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Choose the option that has the same consonant sound as the one emphasised: psychED",
            "options": ["wanted", "thorough", "asked", "both"],
            "correct_letter": "C",
            "explanation": "In 'psyched' the root ends in voiceless /k/, giving '-ed' the sound /t/. 'Asked' also ends with /kt/ (/t/)."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "philosophical_theme", "difficulty": "medium",
            "question": "What lesson can be drawn from Maurya’s final words in J.M. Synge’s Riders to the Sea?",
            "options": ["Religion solves all problems", "Death is unavoidable and must be accepted", "People should avoid the sea", "Wealth is more important than life"],
            "correct_letter": "B",
            "explanation": "Maurya concludes: 'No man at all can be living for ever, and we must be satisfied,' showing stoic acceptance of mortality."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "plot_comprehension", "difficulty": "easy",
            "question": "What causes Bartley’s death in J.M. Synge’s Riders to the Sea?",
            "options": ["A storm", "A boat accident", "The gray pony knocks him into the sea", "Illness"],
            "correct_letter": "C",
            "explanation": "The gray pony knocked Bartley over the cliff into the sea, where the rough waves drowned him."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "symbolism", "difficulty": "easy",
            "question": "What does the sea mainly represent in J.M. Synge’s Riders to the Sea?",
            "options": ["Freedom", "Adventure", "Wealth", "Death and danger"],
            "correct_letter": "D",
            "explanation": "The sea functions as a cruel, inexorable adversary representing danger and relentless death."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen",
            "skill_tested": "irony_analysis", "difficulty": "medium",
            "question": "One major irony in Buchi Emecheta’s Second-Class Citizen is that...",
            "options": ["Adah never becomes educated", "Adah refuses to travel abroad", "education does not automatically eradicate patriarchal attitudes", "Francis becomes poorer in England"],
            "correct_letter": "C",
            "explanation": "Even though Francis receives Western education and relocates to England, his misogynistic patriarchal attitudes persist."
        },
        {
            "category": "literary_terms", "source": "CA", "text_reference": "Textbook Ch 3 (p. 53)",
            "skill_tested": "figures_of_speech", "difficulty": "easy",
            "question": "A figure of speech where a part of something represents the whole thing or vice versa is called _______.",
            "options": ["Metonymy", "Simile", "Synecdoche", "Symbolism"],
            "correct_letter": "C",
            "explanation": "Synecdoche is using a part to stand for the whole (e.g. 'twenty sails' for ships) or the whole for a part."
        },
        {
            "category": "stress", "source": "CA", "text_reference": "Textbook Ch 2 (Suffix -tion)",
            "skill_tested": "word_stress", "difficulty": "easy",
            "question": "Place the primary stress on this word: FALSIFICATION",
            "options": ["FAL-si-fi-ca-tion", "fal-s-i-FI-ca-tion", "fal-si-fi-CA-tion", "fal-sI-fi-ca-tion"],
            "correct_letter": "C",
            "explanation": "Words ending in '-tion' take primary stress on the penultimate syllable (before -tion): fal-si-fi-CA-tion."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "plot_comprehension", "difficulty": "medium",
            "question": "What is Maurya doing when she goes out in J.M. Synge’s Riders to the Sea?",
            "options": ["Visiting the priest", "Trying to bless Bartley", "Going to the market", "Looking for fish"],
            "correct_letter": "B",
            "explanation": "Maurya hurries to the spring well with bread to bless Bartley, whom she had failed to bless upon departure."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen",
            "skill_tested": "characterization", "difficulty": "medium",
            "question": "Adah’s mother in Buchi Emecheta’s Second-Class Citizen can best be described as...",
            "options": ["entirely cruel and heartless", "politically radical", "a product of patriarchal conditioning and societal expectations", "economically independent"],
            "correct_letter": "C",
            "explanation": "Ma's discriminatory behavior towards Adah stems from internalized patriarchal societal norms favoring males."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "setting", "difficulty": "easy",
            "question": "J.M. Synge’s Riders to the Sea is set where?",
            "options": ["Dublin", "Scotland", "London", "An island off the west of Ireland"],
            "correct_letter": "D",
            "explanation": "The drama is set in an Aran Islands cottage off the western coast of Ireland."
        },
        {
            "category": "sound", "source": "CA", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Choose the word that contains the consonant sound represented by the given phonetic symbol: /t/",
            "options": ["worth", "subtle", "warmed", "depot"],
            "correct_letter": "B",
            "explanation": "In 'subtle', 'b' is silent and 't' is sounded as /t/. 'Depot' has silent 't', 'warmed' has /d/, and 'worth' has /θ/."
        },
        {
            "category": "poem", "source": "CA", "text_reference": "Wordsworth: My Heart Leaps Up",
            "skill_tested": "figures_of_speech", "difficulty": "easy",
            "question": "“The Child is father of the Man” is an example of ---",
            "options": ["paradox", "hyperbole", "metaphor", "irony"],
            "correct_letter": "A",
            "explanation": "It is a paradox: an apparently self-contradictory statement that expresses a profound psychological truth."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen",
            "skill_tested": "character_analysis", "difficulty": "medium",
            "question": "Francis’s refusal to support Adah’s ambitions in Buchi Emecheta’s Second-Class Citizen demonstrates...",
            "options": ["intellectual superiority", "religious intolerance", "political rebellion", "toxic masculinity and insecurity"],
            "correct_letter": "D",
            "explanation": "Francis feels intimidated by Adah's capability and lashes out through abusive control and insecure masculinity."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "character_motivation", "difficulty": "easy",
            "question": "In J.M. Synge’s Riders to the Sea, what does Maurya fear most?",
            "options": ["Losing Bartley to the sea", "Lack of food", "Losing her husband to the pirates", "Hunger"],
            "correct_letter": "A",
            "explanation": "Having lost all her other men, Maurya's consuming fear is losing Bartley, her last living son."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen (Chapter 6)",
            "skill_tested": "thematic_analysis", "difficulty": "easy",
            "question": "The phrase “Sorry, No Coloureds” in Buchi Emecheta’s Second-Class Citizen chiefly exposes...",
            "options": ["institutional racism in Britain", "educational inequality", "tribal prejudice in Nigeria", "marital instability"],
            "correct_letter": "A",
            "explanation": "The sign encapsulates the overt, widespread racial discrimination faced by non-white migrants seeking housing in 1960s England."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen",
            "skill_tested": "thematic_analysis", "difficulty": "easy",
            "question": "Which of the following themes is LEAST central to Buchi Emecheta’s Second-Class Citizen?",
            "options": ["Patriarchy", "Migration", "Environmental degradation", "Racism"],
            "correct_letter": "C",
            "explanation": "The novel explores gender, race, poverty, and migration; environmental degradation is not a theme."
        },
        {
            "category": "sound", "source": "CA", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Choose the word that contains the consonant sound represented by the given phonetic symbol: /ʒ/",
            "options": ["join", "mirage", "knowledge", "hedge"],
            "correct_letter": "B",
            "explanation": "'Mirage' (/mɪˈrɑːʒ/) features the voiced palato-alveolar fricative /ʒ/. The other words contain the affricate /dʒ/."
        },
        {
            "category": "stress", "source": "CA", "text_reference": "Textbook Ch 2 (Suffix -ic)",
            "skill_tested": "word_stress", "difficulty": "easy",
            "question": "Place the primary stress on this word: DEMOCRATIC",
            "options": ["de-mo-cra-TIC", "de-mo-CRA-tic", "de-MO-cra-tic", "DE-mo-cra-tic"],
            "correct_letter": "B",
            "explanation": "The suffix '-ic' places stress on the penultimate syllable: de-mo-CRA-tic."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "cultural_context", "difficulty": "medium",
            "question": "As indicated in J.M. Synge’s Riders to the Sea, what does Maurya’s statement about young men leaving things behind suggest about their society?",
            "options": ["Old people are wealthy", "People do not value family", "Death of young men is common", "Young people are careless"],
            "correct_letter": "C",
            "explanation": "Because young fishermen constantly perish at sea, it has become tragically routine for elders to survive the youth."
        },
        {
            "category": "literary_terms", "source": "CA", "text_reference": "Textbook Ch 3 (p. 61)",
            "skill_tested": "dramatic_devices", "difficulty": "easy",
            "question": "Playwrights deploy ______ to ease tension in tragedy.",
            "options": ["comic relief", "comic release", "humour", "comedy"],
            "correct_letter": "A",
            "explanation": "Comic relief is used in dramatic tragedies to provide momentary emotional release for the audience."
        },
        {
            "category": "drama", "source": "CA", "text_reference": "Riders to the Sea",
            "skill_tested": "setting_and_occupation", "difficulty": "easy",
            "question": "What is the main occupation of the family that is the represented in J.M. Synge’s Riders to the Sea?",
            "options": ["Trading", "Teaching", "Farming", "Fishing and sea-faring"],
            "correct_letter": "D",
            "explanation": "The male characters earn their livelihood entirely through seafaring and fishing in the perilous Atlantic."
        },
        {
            "category": "literary_terms", "source": "CA", "text_reference": "Textbook Ch 3 (p. 45)",
            "skill_tested": "narrative_devices", "difficulty": "easy",
            "question": "A clue to an event that will happen later in a work of art is _____________",
            "options": ["flashforward", "prospect", "foreshadowing", "flashback"],
            "correct_letter": "C",
            "explanation": "Foreshadowing provides advance hints or suggestions of future plot developments."
        },
        {
            "category": "novel", "source": "CA", "text_reference": "Second-Class Citizen",
            "skill_tested": "thematic_vision", "difficulty": "medium",
            "question": "Which statement best summarises the feminist vision of Buchi Emecheta’s Second-Class Citizen?",
            "options": ["Women must struggle against structures that limit their humanity and potential.", "African traditions should never be questioned.", "Marriage is the ultimate fulfilment for women.", "Women should reject education for motherhood."],
            "correct_letter": "A",
            "explanation": "Adah's journey asserts that women must actively resist systemic and domestic oppression to realize full humanity."
        },
        {
            "category": "stress", "source": "CA", "text_reference": "Textbook Ch 2 (Suffix -ious)",
            "skill_tested": "word_stress", "difficulty": "hard",
            "question": "Place the primary stress on this word: LASCIVIOUS",
            "options": ["la-SCI-vi-ous", "la-sci-VI-ous", "LA-sci-vi-ous", "la-sci-vi-OUS"],
            "correct_letter": "A",
            "explanation": "In 'lascivious', the primary stress falls on the second syllable (antepenultimate): la-SCI-vi-ous."
        },
        {
            "category": "literary_terms", "source": "CA", "text_reference": "Textbook Ch 3 (p. 61)",
            "skill_tested": "genre_definition", "difficulty": "easy",
            "question": "A genre of literature that directly imitates human action on stage is __________",
            "options": ["drama", "prose", "comedy", "poetry"],
            "correct_letter": "A",
            "explanation": "Drama represents human actions directly through performance and dialogue by actors on a stage."
        }
    ]
    return raw
