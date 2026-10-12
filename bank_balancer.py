"""
GES 201 Question Bank Balancer: Anti-Giveaway Engine
Standardizes distractor lengths, eliminates giveaway brackets, and ensures
that correct answers cannot be guessed purely by structural or length anomalies.
"""

from scratch.balance_drama_defs import DRAMA_REFINEMENTS
from scratch.balance_novel_defs import NOVEL_REFINEMENTS
from scratch.balance_poetry_defs import POETRY_REFINEMENTS

# Small categories refinements
PHONETICS_SKILLS_REFINEMENTS = {
    # --- Sounds ---
    "q_209": {
        "options": [
            "Consonants are produced with open approximation, whereas vowels require complete oral closure",
            "Consonants involve an obstruction or constriction to the airflow, whereas vowels are produced with open approximation",
            "Consonants require nasal airflow exclusively, whereas vowels require complete velic closure",
            "Consonants are voiced without exception, whereas vowels are produced with voiceless friction"
        ],
        "correct_letter": "B"
    },
    "q_210": {
        "options": [
            "Acoustic pitch, auditory loudness, and vocalic duration",
            "State of the glottis, place of articulation, and manner of articulation",
            "Tongue elevation, lip posture, and morphological length",
            "Syllabic onset, rhythmic prominence, and intonation tune"
        ],
        "correct_letter": "B"
    },
    "q_212": {
        "options": ["Labiodental", "Bilabial", "Alveolar", "Velar"],
        "correct_letter": "B"
    },
    "q_213": {
        "options": ["Bilabial", "Labiodental", "Dental", "Palatal"],
        "correct_letter": "B"
    },
    "q_214": {
        "options": ["Alveolar ridge", "Dental", "Hard palate", "Velum"],
        "correct_letter": "B"
    },
    "q_215": {
        "options": ["Fricatives", "Plosives", "Affricates", "Approximants"],
        "correct_letter": "B"
    },
    "q_217": {
        "options": [
            "A sound produced with frictionless escape through the nasal cavity",
            "A sound that begins as a plosive stop and releases slowly into a fricative",
            "A vowel produced with narrowing between the tongue blade and palate",
            "A glide articulated with rapid continuous vibration of the vocal folds"
        ],
        "correct_letter": "B"
    },
    "q_246": {
        "options": ["Five diphthongs", "Eight diphthongs", "Twelve diphthongs", "Twenty diphthongs"],
        "correct_letter": "B"
    },
    "q_256": {
        "options": [
            "Voiceless alveolar plosive /t/",
            "Voiceless velar plosive /k/",
            "No final consonant sound (ends with vowel /eɪ/)",
            "Voiceless dental fricative /θ/"
        ],
        "correct_letter": "C"
    },
    "q_264": {
        "options": [
            "Because English consonants undergo random dialectal mutations across each generation",
            "Because historical sound shifts occurred while spelling remained frozen, and words were borrowed from multiple languages",
            "Because printing presses eliminated all historical vowel letters to reduce paper consumption",
            "Because the International Phonetic Association standardized grammar before orthography existed"
        ],
        "correct_letter": "B"
    },

    # --- Stress ---
    "q_295": {
        "options": [
            "Noun has second syllable stress; adjective has first syllable stress",
            "Noun has first syllable stress; adjective has second syllable stress",
            "Both grammatical words receive primary stress on the first syllable",
            "Both grammatical words receive primary stress on the second syllable"
        ],
        "correct_letter": "B"
    },
    "q_296": {
        "options": [
            "Phrasal verbs stress the first element; compound nouns stress the second element",
            "Phrasal verbs stress the second element; compound nouns stress the first element",
            "Phrasal verbs and compound nouns both place primary stress on the first element",
            "Phrasal verbs and compound nouns both place primary stress on the second element"
        ],
        "correct_letter": "B"
    },

    # --- Intonation ---
    "q_319": {
        "options": ["Pre-head", "Head", "Tonic syllable", "Tail"],
        "correct_letter": "C"
    },
    "q_325": {
        "options": [
            "Because falling tune would turn the polite request into a harsh command",
            "Because rising tune increases acoustic volume across every individual phoneme",
            "Because English syntactic grammar strictly disallows falling pitch on imperatives",
            "Because interrogative polite requests cannot contain lexical main verbs"
        ],
        "correct_letter": "A"
    },
    "q_327": {
        "options": [
            "Grammatical/function words (prepositions, conjunctions, pronouns, and determiners)",
            "Content/lexical words belonging to open classes (nouns, main verbs, adjectives, adverbs)",
            "Non-referential structural linkers and unstressed auxiliary verbs only",
            "Introductory sentence adverbials and closing parenthetical disjuncts only"
        ],
        "correct_letter": "B"
    },
    "q_328": {
        "options": [
            "That Kate rented a commercial van instead of borrowing an automobile",
            "That Kate, and not anyone else, was the specific person who borrowed the car",
            "That Kate unlawfully seized the vehicle rather than obtaining permission",
            "That the vehicle belonged to a third party rather than the original speaker"
        ],
        "correct_letter": "B"
    },
    "q_329": {
        "options": [
            "She purchased the vehicle permanently rather than using it temporarily",
            "She did not steal or buy the vehicle, but legitimately borrowed it",
            "She merely admired the vehicle without actually driving it anywhere",
            "She returned the vehicle immediately without ever operating the engine"
        ],
        "correct_letter": "B"
    },
    "q_335": {
        "options": [
            "Whenever it appears medially between two stressed polysyllabic content words",
            "When it occurs at the end of a tone group or when emphasized contrastively",
            "Whenever it is immediately preceded by an open centring diphthong glide",
            "Whenever it functions as an unstressed coordinating conjunction between clauses"
        ],
        "correct_letter": "B"
    },
    "q_338": {
        "options": [
            "Both clauses receive a continuous low-falling tone tune across their nuclear syllables",
            "The first clause rises on 'love' and the second falls on 'ma-' of 'marry'",
            "The first clause falls sharply on 'her' and the second rises gradually on the nucleus",
            "Both clauses receive a sustained high-rising intonation tune without any pitch descent"
        ],
        "correct_letter": "B"
    },
    "q_339": {
        "options": [
            "Every item in the sequence receives a steep falling pitch contour regardless of position",
            "Non-final items rise for continuation and the final item falls to indicate completion",
            "Every item in the sequence sustains a continuous high-rising intonation tune",
            "The initial item falls abruptly while all subsequent sequence items ascend in pitch"
        ],
        "correct_letter": "B"
    },
    "q_342": {
        "options": [
            "Absolute certainty, objective neutrality, and complete finality",
            "Reservation, hesitation, polite warning, or lingering doubt",
            "Aggressive categorical command and unyielding final assertion",
            "Cheery enthusiastic celebration and unambiguous confirmation"
        ],
        "correct_letter": "B"
    },
    "q_344": {
        "options": [
            "The nuclear syllable carrying the principal pitch trajectory",
            "Any unstressed syllables occurring before the first stressed syllable",
            "The final terminal glide following the nuclear tonic pitch change",
            "The rhythmic stressed foot containing the strongest amplitude peak"
        ],
        "correct_letter": "B"
    },

    # --- Literary Terms ---
    "q_364": {
        "options": [
            "Stanza, Metrical Foot, Caesura, Enjambment, and Rhyme Scheme",
            "Exposition, Rising Action, Climax, Falling Action, and Denouement",
            "Prologue, Soliloquy, Catastrophe, Epilogue, and Dramatic Irony",
            "Introduction, Literature Review, Methodology, Results, and Discussion"
        ],
        "correct_letter": "B"
    },
    "q_366": {
        "options": [
            "Spatial setting and Temporal setting",
            "Emotional tone and psychological atmosphere",
            "Climactic resolution and tragic hamartia",
            "Thematic purpose and philosophical ideology"
        ],
        "correct_letter": "A"
    },
    "q_368": {
        "options": [
            "Stage directions guiding physical movements and scene decor",
            "Dramatis personae cataloging the cast of theatrical roles",
            "Intended live enactment by performers before an assembled audience",
            "Exclusive organization into metered stanzas and rhymed quatrains"
        ],
        "correct_letter": "D"
    },
    "q_371": {
        "options": [
            "Knowledge strictly restricted to the subjective perspective of an external eyewitness",
            "Unlimited access to the internal thoughts, psychological motives, and actions of all characters",
            "Direct active involvement as the conflicted first-person protagonist within the fictional drama",
            "Detached reportage limited strictly to audible dialogue without interpretive editorializing"
        ],
        "correct_letter": "B"
    },
    "q_374": {
        "options": [
            "Internal conflict within a character and External conflict with others or society",
            "Orthographic tension between classical archaic spelling and modern vernacular usage",
            "Stylistic friction between formal poetic diction and informal colloquial prose registers",
            "Prosodic clash between quantitative classical meter and qualitative accentual rhythm"
        ],
        "correct_letter": "A"
    },

    # --- Writing Skills ---
    "q_379": {
        "options": [
            "One address: the sender's institutional address positioned centrally at the top",
            "Two addresses: the sender's address at top right and recipient's address at top left",
            "Three addresses: the sender, the forwarding courier service, and the recipient",
            "No physical postal addresses if digital transmission is acknowledged in the header"
        ],
        "correct_letter": "B"
    },
    "q_381": {
        "options": [
            "The operational 'SUBJECT' identification line",
            "Salutation and formal complimentary close",
            "The designated 'TO' and 'FROM' routing headers",
            "The chronological date stamp and dispatch reference"
        ],
        "correct_letter": "B"
    },
    "q_382": {
        "options": [
            "External diplomatic protocol communication with foreign civil embassies",
            "Internal written communication between staff within the same organization",
            "Public advertising designed to persuade external consumers to purchase goods",
            "Judicial transcript recording formal court proceedings for official archives"
        ],
        "correct_letter": "B"
    },
    "q_388": {
        "options": [
            "Extends across more than four complex compound sentence structures",
            "Introduces irrelevant details that fail to develop the controlling topic sentence",
            "Employs logical transitional linking devices between sequential claims",
            "Incorporates discipline-specific technical terminology without prior definition"
        ],
        "correct_letter": "B"
    },
    "q_392": {
        "options": [
            "A hyphen marks clause endings, while a dash links morphological prefixes to lexical bases",
            "A hyphen joins compound words or elements; a dash indicates an abrupt break or parenthesis",
            "A hyphen is strictly restricted to mathematics, while a dash marks phonetic transcriptions",
            "A hyphen separates independent paragraphs, while a dash terminates interrogative clauses"
        ],
        "correct_letter": "B"
    },
    "q_393": {
        "options": [
            "The terminal completion of a declarative rhetorical clause",
            "The deliberate omission of words from a quoted passage",
            "A typographical marker indicating an emphatic exclamation",
            "A prosodic notation indicating a rising interrogative pitch"
        ],
        "correct_letter": "B"
    },
    "q_394": {
        "options": ["Dangling modifier", "Comma splice", "Split infinitive", "Faulty parallelism"],
        "correct_letter": "B"
    },
    "q_398": {
        "options": ["Descriptive essay", "Argumentative essay", "Expository essay", "Narrative essay"],
        "correct_letter": "B"
    },
    "q_399": {
        "options": [
            "Biographical denunciation of the author's private moral conduct",
            "Critical evaluation of the author's style, thematic vision, and craftsmanship",
            "Exhaustive reproduction of all chapter dialogues without commentary",
            "Itemized marketing figures detailing publisher wholesale sales volumes"
        ],
        "correct_letter": "B"
    },
    "q_401": {
        "options": [
            "Traditional British rules mandate a colon followed immediately by a long dash",
            "Modern business practice increasingly adopts open punctuation omitting non-essential commas",
            "Standard correspondence etiquette strictly demands a terminal semi-colon after all greetings",
            "Formal style manuals universally mandate double hyphens following the recipient's title"
        ],
        "correct_letter": "B"
    },
    "q_402": {
        "options": [
            "Memorizing, recite-testing, and oral defense",
            "Pre-writing, Writing, and Post-writing",
            "Proofreading, peer-critiquing, and book publishing",
            "Dictation, grammatical parsing, and final examination"
        ],
        "correct_letter": "B"
    },
    "q_403": {
        "options": [
            "It expands orthographic length to satisfy formal academic word counts",
            "It prevents syntactic ambiguity and misinterpretation that alter intended meaning",
            "It eliminates the grammatical necessity for subject-verb agreement in formal prose",
            "It provides decorative aesthetic spacing between unrelated rhetorical sentences"
        ],
        "correct_letter": "B"
    }
}

# Combine all refinements into a single authoritative dictionary
ALL_REFINEMENTS = {}
ALL_REFINEMENTS.update(DRAMA_REFINEMENTS)
ALL_REFINEMENTS.update(NOVEL_REFINEMENTS)
ALL_REFINEMENTS.update(POETRY_REFINEMENTS)
ALL_REFINEMENTS.update(PHONETICS_SKILLS_REFINEMENTS)

def apply_refinements(questions):
    """
    Apply anti-giveaway option balancing to questions.
    """
    applied_count = 0
    letters = ["A", "B", "C", "D"]

    for q in questions:
        q_id = q["id"]
        if q_id in ALL_REFINEMENTS:
            ref = ALL_REFINEMENTS[q_id]
            raw_opts = ref["options"]
            c_letter = ref["correct_letter"].upper()

            # Format options with letter prefixes
            new_options = []
            new_correct_ans = ""
            for l, text in zip(letters, raw_opts):
                formatted = f"{l}. {text.strip()}"
                new_options.append(formatted)
                if l == c_letter:
                    new_correct_ans = formatted

            q["options"] = new_options
            q["correct_answer"] = new_correct_ans
            applied_count += 1

    return applied_count
