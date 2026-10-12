"""
Comprehensive Question Bank: English Sounds & Phonetics (60 Questions)
Based on Chapter 2 (Dr. Adenike Akinjobi, Department of English, University of Ibadan).
"""

def get_sounds_questions():
    return [
        # --- Airstream & Organs of Speech ---
        {
            "category": "sound", "source": "textbook", "text_reference": "Textbook Ch 2 (p. 14)",
            "skill_tested": "airstream_mechanism", "difficulty": "easy",
            "question": "Which airstream mechanism is exclusively utilized in the production of normal English speech sounds?",
            "options": ["Velaric ingressive", "Pulmonic egressive", "Glottalic egressive", "Pharyngeal ingressive"],
            "correct_letter": "B",
            "explanation": "English speech sounds are produced exclusively using the pulmonic egressive airstream mechanism—lung air pushed outwards."
        },
        {
            "category": "sound", "source": "textbook", "text_reference": "Textbook Ch 2 (p. 14)",
            "skill_tested": "organs_of_speech", "difficulty": "medium",
            "question": "What is the primary function of the vocal cords during the production of voiced speech sounds?",
            "options": ["They remain completely wide open and motionless", "They vibrate rapidly as airstream forces through the glottis", "They close the nasal cavity completely", "They press against the alveolar ridge"],
            "correct_letter": "B",
            "explanation": "When vocal cords are brought close together, air rushing from the lungs causes them to vibrate, generating voicing."
        },
        {
            "category": "sound", "source": "textbook", "text_reference": "Textbook Ch 2 (p. 14)",
            "skill_tested": "consonant_definition", "difficulty": "easy",
            "question": "How are consonant sounds fundamentally distinguished from vowel sounds in articulatory phonetics?",
            "options": ["Consonants are produced with open approximation, whereas vowels require complete oral closure", "Consonants involve an obstruction or constriction to the airflow, whereas vowels are produced with open approximation", "Consonants require nasal airflow exclusively, whereas vowels require complete velic closure", "Consonants are voiced without exception, whereas vowels are produced with voiceless friction"],
            "correct_letter": "B",
            "explanation": "Consonants are articulated with total, partial, or intermittent obstruction to the airstream; vowels involve free, unimpeded airflow (open approximation)."
        },
        {
            "category": "sound", "source": "textbook", "text_reference": "Textbook Ch 2 (p. 14)",
            "skill_tested": "parameters_of_consonants", "difficulty": "medium",
            "question": "What are the three classical parameters required to describe an English consonant sound?",
            "options": ["Acoustic pitch, auditory loudness, and vocalic duration", "State of the glottis, place of articulation, and manner of articulation", "Tongue elevation, lip posture, and morphological length", "Syllabic onset, rhythmic prominence, and intonation tune"],
            "correct_letter": "B",
            "explanation": "Consonants are classified by voicing (voiced/voiceless), place of articulation, and manner of articulation."
        },
        {
            "category": "sound", "source": "textbook", "text_reference": "Textbook Ch 2 (p. 14)",
            "skill_tested": "nasal_articulation", "difficulty": "medium",
            "question": "When producing nasal consonants (/m/, /n/, /ŋ/), what position does the soft palate (velum) assume?",
            "options": ["It is raised against the pharynx to block the nasal cavity", "It is lowered to allow lung air to escape through the nasal cavity", "It vibrates against the tongue", "It remains completely rigid and closed"],
            "correct_letter": "B",
            "explanation": "The velum lowers, opening the nasal passage so air resonates and exits through the nose."
        },

        # --- Consonant Phonemes & Places/Manners ---
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "place_of_articulation", "difficulty": "easy",
            "question": "The consonant sounds /p/, /b/, and /m/ are classified as which place of articulation?",
            "options": ["Labiodental", "Bilabial", "Alveolar", "Velar"],
            "correct_letter": "B",
            "explanation": "/p/, /b/, and /m/ are bilabial consonants produced by bringing both lips together."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "place_of_articulation", "difficulty": "easy",
            "question": "The consonants /f/ and /v/ are classified as:",
            "options": ["Bilabial", "Labiodental", "Dental", "Palatal"],
            "correct_letter": "B",
            "explanation": "/f/ and /v/ are labiodentals produced by contact between the lower lip and upper incisors."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "place_of_articulation", "difficulty": "medium",
            "question": "The phonetic sounds /θ/ (as in 'thin') and /ð/ (as in 'this') are articulated at which position?",
            "options": ["Alveolar ridge", "Dental", "Hard palate", "Velum"],
            "correct_letter": "B",
            "explanation": "/θ/ and /ð/ are dental fricatives formed with the tongue tip against or behind the upper front teeth."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "manner_of_articulation", "difficulty": "medium",
            "question": "Consonants produced by a complete closure of the vocal tract followed by a sudden explosive release are called:",
            "options": ["Fricatives", "Plosives", "Affricates", "Approximants"],
            "correct_letter": "B",
            "explanation": "Plosives (/p, b, t, d, k, ɡ/) involve complete closure, pressure build-up, and sudden audible explosion."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "manner_of_articulation", "difficulty": "medium",
            "question": "Consonants produced by narrowing the vocal tract to create audible friction noise without total closure are:",
            "options": ["Plosives", "Fricatives", "Nasals", "Laterals"],
            "correct_letter": "B",
            "explanation": "Fricatives (/f, v, θ, ð, s, z, ʃ, ʒ, h/) are continuous friction sounds created by forcing air through a narrow gap."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "manner_of_articulation", "difficulty": "hard",
            "question": "What is an affricate consonant in English phonology?",
            "options": ["A sound produced with frictionless escape through the nasal cavity", "A sound that begins as a plosive stop and releases slowly into a fricative", "A vowel produced with narrowing between the tongue blade and palate", "A glide articulated with rapid continuous vibration of the vocal folds"],
            "correct_letter": "B",
            "explanation": "Affricates (/tʃ/ in 'church', /dʒ/ in 'judge') combine a complete stop with a gradual fricative release."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 15)",
            "skill_tested": "lateral_sound", "difficulty": "easy",
            "question": "Which English phoneme is the sole 'lateral' consonant?",
            "options": ["/r/", "/l/", "/w/", "/j/"],
            "correct_letter": "B",
            "explanation": "/l/ is a lateral approximant because air escapes freely along the sides (lateral margins) of the tongue."
        },

        # --- The Inflectional -ed and -s Morphemes ---
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 16)",
            "skill_tested": "morpheme_ed", "difficulty": "medium",
            "question": "In which of the following words is the regular past tense suffix '-ed' pronounced as /t/?",
            "options": ["robbed", "laughed", "played", "needed"],
            "correct_letter": "B",
            "explanation": "The root 'laugh' ends in voiceless /f/, so '-ed' assimilates to voiceless /t/ (/lɑːft/). 'Robbed' and 'played' end in /d/, 'needed' in /-ɪd/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 16)",
            "skill_tested": "morpheme_ed", "difficulty": "medium",
            "question": "In which word is the past tense morpheme '-ed' pronounced as an extra syllable /-ɪd/?",
            "options": ["brushed", "judged", "decided", "kissed"],
            "correct_letter": "C",
            "explanation": "Roots ending in /t/ or /d/ require the epenthetic vowel /-ɪd/, hence 'decided' (/dɪˈsaɪdɪd/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 16)",
            "skill_tested": "morpheme_ed", "difficulty": "medium",
            "question": "Which option has the past tense '-ed' pronounced as voiced /d/?",
            "options": ["worked", "washed", "begged", "trapped"],
            "correct_letter": "C",
            "explanation": "'Beg' ends in voiced /ɡ/, so '-ed' is voiced /d/ (/bɛɡd/). In 'worked', 'washed', and 'trapped', the root ends in a voiceless stop/fricative, producing /t/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 16)",
            "skill_tested": "morpheme_s", "difficulty": "medium",
            "question": "In which plural noun is the '-s' suffix pronounced as voiceless /s/?",
            "options": ["dogs", "pens", "books", "boys"],
            "correct_letter": "C",
            "explanation": "'Book' ends in voiceless /k/, so the plural suffix remains voiceless /s/. 'Dogs', 'pens', and 'boys' end in voiced sounds, taking /z/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (p. 16)",
            "skill_tested": "morpheme_s", "difficulty": "medium",
            "question": "In which noun is the plural ending pronounced as /-ɪz/?",
            "options": ["caps", "fans", "churches", "tables"],
            "correct_letter": "C",
            "explanation": "Nouns ending in sibilants (/s, z, ʃ, ʒ, tʃ, dʒ/) take /-ɪz/ to avoid consonant clusters; 'church' ends in /tʃ/, giving /ˈtʃɜːtʃɪz/."
        },

        # --- Silent Letters in English ---
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_b", "difficulty": "medium",
            "question": "In which word is the letter 'b' completely silent?",
            "options": ["timber", "subtle", "table", "marble"],
            "correct_letter": "B",
            "explanation": "In 'subtle' (/ˈsʌt.əl/), the letter 'b' is completely unpronounced (as in debt, doubt, climb, comb)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_t", "difficulty": "medium",
            "question": "In which of the following words is the letter 't' silent?",
            "options": ["metal", "listen", "mortal", "total"],
            "correct_letter": "B",
            "explanation": "In 'listen' (/ˈlɪs.ən/), the 't' is silent (as in castle, whistle, fasten, depot)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_k", "difficulty": "easy",
            "question": "Which word features an initial silent 'k'?",
            "options": ["kitten", "knight", "kitchen", "kettle"],
            "correct_letter": "B",
            "explanation": "Initial 'kn-' clusters in English always have silent 'k' (knight = /naɪt/, knee = /niː/, know = /nəʊ/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_g", "difficulty": "medium",
            "question": "In which word is the letter 'g' silent?",
            "options": ["ghost", "sign", "glide", "gather"],
            "correct_letter": "B",
            "explanation": "In 'sign' (/saɪn/), 'g' is silent (as in design, campaign, foreign, phlegm, gnaw)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_w", "difficulty": "medium",
            "question": "In which word is the letter 'w' silent?",
            "options": ["sweet", "sword", "swim", "sweep"],
            "correct_letter": "B",
            "explanation": "'Sword' is pronounced /sɔːd/; the 'w' is completely silent."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_p", "difficulty": "medium",
            "question": "In which word is the letter 'p' silent?",
            "options": ["receipt", "pocket", "carpet", "copper"],
            "correct_letter": "A",
            "explanation": "'Receipt' is pronounced /rɪˈsiːt/; the 'p' is silent (as in psychology, psalm, pneumonia)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_l", "difficulty": "medium",
            "question": "In which of the following words is the letter 'l' silent?",
            "options": ["film", "palm", "silver", "elder"],
            "correct_letter": "B",
            "explanation": "'Palm' is pronounced /pɑːm/; 'l' is silent (as in calm, half, chalk, walk, talk)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_h", "difficulty": "easy",
            "question": "In which word is the initial letter 'h' silent?",
            "options": ["house", "honour", "hospital", "heavy"],
            "correct_letter": "B",
            "explanation": "'Honour' begins with silent 'h' (/ˈɒn.ər/), as do 'hour', 'heir', and 'honest'."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Silent Letters)",
            "skill_tested": "silent_s", "difficulty": "medium",
            "question": "In which word is the letter 's' silent?",
            "options": ["island", "simple", "castle", "system"],
            "correct_letter": "A",
            "explanation": "'Island' is pronounced /ˈaɪ.lənd/; the 's' is silent (as in aisle and isle)."
        },

        # --- Consonant Phoneme Identification ---
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Which of the following words contains the voiced palato-alveolar fricative /ʒ/?",
            "options": ["leisure", "gesture", "soldier", "nature"],
            "correct_letter": "A",
            "explanation": "'Leisure' (/ˈleʒ.ər/) contains /ʒ/. 'Gesture' and 'soldier' contain /dʒ/, while 'nature' contains /tʃ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Choose the word containing the voiceless palato-alveolar affricate /tʃ/:",
            "options": ["machine", "champagne", "question", "chef"],
            "correct_letter": "C",
            "explanation": "'Question' is pronounced /ˈkwes.tʃən/ (affricate /tʃ/). 'Machine', 'champagne', and 'chef' feature the fricative /ʃ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Which word begins with the voiceless palato-alveolar fricative /ʃ/?",
            "options": ["sugar", "salt", "soap", "solar"],
            "correct_letter": "A",
            "explanation": "In 'sugar' (and 'sure'), initial 'su-' is pronounced /ʃ/ (/ˈʃʊɡ.ər/). The other words begin with /s/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "hard",
            "question": "In the word 'gigantic', what are the pronunciations of the two 'g' letters respectively?",
            "options": ["First is /ɡ/, second is /dʒ/", "First is /dʒ/, second is /ɡ/", "Both are /ɡ/", "Both are /dʒ/"],
            "correct_letter": "B",
            "explanation": "As noted by Dr. Akinjobi in the course text (p. 13), 'gigantic' is pronounced /dʒaɪˈɡæn.tɪk/; the first 'g' is /dʒ/ and the second is /ɡ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "velar_nasal", "difficulty": "medium",
            "question": "In which of the following words is the 'ng' pronounced as simple velar nasal /ŋ/ without a following /ɡ/ sound?",
            "options": ["finger", "singer", "anger", "hunger"],
            "correct_letter": "B",
            "explanation": "In morphologically derived 'singer' (sing + -er), 'ng' is purely /ŋ/ (/ˈsɪŋ.ər/). In roots like 'finger', 'anger', and 'hunger', 'ng' is pronounced /ŋɡ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "dental_consonant", "difficulty": "medium",
            "question": "Choose the word that contains the voiced dental fricative /ð/:",
            "options": ["thin", "breathe", "breath", "path"],
            "correct_letter": "B",
            "explanation": "The verb 'breathe' ends in voiced /ð/ (/briːð/). 'Thin', 'breath' (noun), and 'path' contain voiceless /θ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "dental_consonant", "difficulty": "medium",
            "question": "Which of the following contains the voiceless dental fricative /θ/?",
            "options": ["father", "clothing", "method", "smooth"],
            "correct_letter": "C",
            "explanation": "'Method' (/ˈmeθ.əd/) has voiceless /θ/. 'Father', 'clothing', and 'smooth' contain voiced /ð/."
        },

        # --- Vowel Phonemes & Diphthongs ---
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Which word contains the long high front vowel /iː/?",
            "options": ["quay", "sit", "head", "women"],
            "correct_letter": "A",
            "explanation": "'Quay' is pronounced /kiː/ with long /iː/. 'Head' has /e/, 'sit' has /ɪ/, and 'women' has /ˈwɪm.ɪn/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Choose the word containing the low central short vowel /ʌ/:",
            "options": ["blood", "move", "pool", "book"],
            "correct_letter": "A",
            "explanation": "'Blood' and 'flood' feature the short central vowel /ʌ/ (/blʌd/). 'Move' and 'pool' have /uː/, and 'book' has /ʊ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Which word contains the long back vowel /ɔː/?",
            "options": ["caught", "cot", "cup", "car"],
            "correct_letter": "A",
            "explanation": "'Caught' (/kɔːt/) features the long back vowel /ɔː/. 'Cot' has short /ɒ/, 'cup' has /ʌ/, and 'car' has /ɑː/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Choose the word containing the short back rounded vowel /ɒ/:",
            "options": ["swan", "warn", "barn", "burn"],
            "correct_letter": "A",
            "explanation": "'Swan' is pronounced /swɒn/ with short /ɒ/. 'Warn' has /ɔː/, 'barn' has /ɑː/, and 'burn' has /ɜː/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Which word contains the central vowel /ɜː/?",
            "options": ["girl", "glare", "guard", "gear"],
            "correct_letter": "A",
            "explanation": "'Girl' (/ɡɜːl/) contains the long central unrounded vowel /ɜː/ (as in bird, heard, nurse)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "schwa_vowel", "difficulty": "easy",
            "question": "What is the common name for the unstressed central vowel /ə/ in English phonetics?",
            "options": ["Diphthong", "Schwa", "Glottal stop", "Monophthong"],
            "correct_letter": "B",
            "explanation": "The unstressed mid-central vowel /ə/ is called the 'schwa'—the most frequent vowel in spoken English."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Diphthongs)",
            "skill_tested": "diphthong_classification", "difficulty": "medium",
            "question": "How many total diphthongs exist in standard Received Pronunciation (RP) English?",
            "options": ["Five diphthongs", "Eight diphthongs", "Twelve diphthongs", "Twenty diphthongs"],
            "correct_letter": "B",
            "explanation": "Standard British English has 8 diphthongs: 3 centring (/ɪə, eə, ʊə/) and 5 closing (/eɪ, aɪ, ɔɪ, əʊ, aʊ/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Diphthongs)",
            "skill_tested": "diphthong_identification", "difficulty": "medium",
            "question": "Which word contains the closing diphthong /aʊ/?",
            "options": ["boat", "doubt", "bought", "boot"],
            "correct_letter": "B",
            "explanation": "'Doubt' is pronounced /daʊt/ with the diphthong /aʊ/ (as in now, cow, loud)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Diphthongs)",
            "skill_tested": "diphthong_identification", "difficulty": "medium",
            "question": "Choose the word that contains the centring diphthong /eə/:",
            "options": ["air", "ear", "tour", "our"],
            "correct_letter": "A",
            "explanation": "'Air' (/eə/) is a centring diphthong gliding towards schwa (as in care, bare, stair). 'Ear' is /ɪə/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "hard",
            "question": "In which word is the vowel sound identical to the vowel in 'clerk' (/ɑː/)?",
            "options": ["clergyman", "heart", "perk", "clerkship"],
            "correct_letter": "B",
            "explanation": "In standard British RP, 'clerk' is pronounced /klɑːk/; 'heart' also has the long open back vowel /ɑː/ (/hɑːt/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "hard",
            "question": "Which word contains the vowel /e/ as in 'bed'?",
            "options": ["heifer", "receive", "people", "debris"],
            "correct_letter": "A",
            "explanation": "'Heifer' is pronounced /ˈhef.ər/ with the short front vowel /e/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Minimal Pairs)",
            "skill_tested": "minimal_pairs", "difficulty": "medium",
            "question": "Which pair of words represents a valid minimal pair contrasting /p/ and /b/?",
            "options": ["pin and bin", "pat and tap", "pit and spit", "pack and backer"],
            "correct_letter": "A",
            "explanation": "'Pin' and 'bin' differ by only one single phoneme in the same position (/p/ vs /b/), making them a minimal pair."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Minimal Pairs)",
            "skill_tested": "minimal_pairs", "difficulty": "medium",
            "question": "Which of the following pairs is a minimal pair contrasting /s/ and /ʃ/?",
            "options": ["seat and sheet", "see and saw", "sip and slip", "sock and lock"],
            "correct_letter": "A",
            "explanation": "'Seat' (/siːt/) and 'sheet' (/ʃiːt/) differ solely by the initial consonant contrast between /s/ and /ʃ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Minimal Pairs)",
            "skill_tested": "minimal_pairs", "difficulty": "medium",
            "question": "Which pair of words contrasts /iː/ and /ɪ/?",
            "options": ["sheep and ship", "pen and pan", "pull and pool", "cat and cut"],
            "correct_letter": "A",
            "explanation": "'Sheep' (/ʃiːp/) has long /iː/, whereas 'ship' (/ʃɪp/) has short /ɪ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Phonetic Symbol)",
            "skill_tested": "phonetic_transcription", "difficulty": "medium",
            "question": "What is the initial consonant sound in the word 'psychology'?",
            "options": ["/p/", "/s/", "/k/", "/ps/"],
            "correct_letter": "B",
            "explanation": "Initial 'p' before 's' is silent; the word begins with voiceless alveolar fricative /s/ (/saɪˈkɒl.ə.dʒi/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Phonetic Symbol)",
            "skill_tested": "phonetic_transcription", "difficulty": "hard",
            "question": "Which phonetic symbol accurately represents the vowel sound in 'plaid'?",
            "options": ["/eɪ/", "/æ/", "/e/", "/aɪ/"],
            "correct_letter": "B",
            "explanation": "In standard English, 'plaid' is pronounced /plæd/ with the short open front vowel /æ/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Phonetic Symbol)",
            "skill_tested": "phonetic_transcription", "difficulty": "medium",
            "question": "In the word 'bouquet', what is the final consonant sound?",
            "options": ["/t/", "/k/", "There is no final consonant sound; the 't' is silent", "/θ/"],
            "correct_letter": "C",
            "explanation": "'Bouquet' is borrowed from French and pronounced /buˈkeɪ/; the final 't' is silent."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "Which of the following words contains the consonant sound /j/?",
            "options": ["juice", "ewe", "joke", "jeep"],
            "correct_letter": "B",
            "explanation": "'Ewe' (female sheep) is pronounced /juː/ and begins with the palatal approximant /j/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "hard",
            "question": "In which word is the consonant sound /w/ present?",
            "options": ["one", "who", "wrist", "wrong"],
            "correct_letter": "A",
            "explanation": "'One' is pronounced /wʌn/ and begins phonetically with /w/. In 'who', 'wrist', and 'wrong', 'w' is silent."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Choose the word containing the short high back vowel /ʊ/:",
            "options": ["could", "cool", "rude", "food"],
            "correct_letter": "A",
            "explanation": "'Could' (/kʊd/) contains short /ʊ/. 'Cool', 'rude', and 'food' have long /uː/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "hard",
            "question": "In the word 'bury', which vowel sound is present in the first syllable?",
            "options": ["/ʊ/", "/uː/", "/e/", "/ɜː/"],
            "correct_letter": "C",
            "explanation": "'Bury' is pronounced /ˈber.i/ with the short front vowel /e/ (homophone with 'berry')."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "hard",
            "question": "Which of the following words contains the voiced fricative /z/?",
            "options": ["cats", "dogs", "parks", "cloths"],
            "correct_letter": "B",
            "explanation": "Because 'dog' ends in voiced /ɡ/, its plural suffix is pronounced as voiced /z/ (/dɒɡz/)."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "consonant_identification", "difficulty": "medium",
            "question": "In the word 'luxury', what consonant sound is represented by the letter 'x'?",
            "options": ["/ks/", "/ɡz/ or /kʃ/", "/z/", "/s/"],
            "correct_letter": "B",
            "explanation": "'Luxury' is pronounced /ˈlʌk.ʃər.i/ with /kʃ/ or /ˈlʌɡ.ʒər.i/."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_identification", "difficulty": "medium",
            "question": "Which word has the same vowel sound as in 'key' (/iː/)?",
            "options": ["quay", "grey", "they", "obey"],
            "correct_letter": "A",
            "explanation": "'Quay' is pronounced /kiː/, exactly homophonous with 'key'."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Consonants)",
            "skill_tested": "silent_letter_summary", "difficulty": "easy",
            "question": "Why does English spelling frequently fail to match phonetic pronunciation?",
            "options": ["Because English consonants undergo random dialectal mutations across each generation", "Because historical sound shifts occurred while spelling remained frozen, and words were borrowed from multiple languages", "Because printing presses eliminated all historical vowel letters to reduce paper consumption", "Because the International Phonetic Association standardized grammar before orthography existed"],
            "correct_letter": "B",
            "explanation": "Historical developments (the Great Vowel Shift) and borrowings from Latin, French, Greek, and Germanic roots created a non-phonetic orthography."
        },
        {
            "category": "sound", "source": "predicted", "text_reference": "Textbook Ch 2 (Vowels)",
            "skill_tested": "vowel_classification", "difficulty": "easy",
            "question": "How many pure vowel sounds (monophthongs) exist in Received Pronunciation (RP) English?",
            "options": ["5 pure vowels", "12 pure vowels", "24 pure vowels", "44 pure vowels"],
            "correct_letter": "B",
            "explanation": "There are 12 monophthongs (pure vowels) and 8 diphthongs, giving 20 total vowel phonemes."
        }
    ]
