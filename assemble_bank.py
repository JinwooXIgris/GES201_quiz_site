"""
Assembly and Validation Script for GES 201 Question Bank
Combines all modules, validates consistency, checks uniqueness, and outputs data/questions.json
"""
import json
import os

from bank_ca import get_ca_questions
from bank_drama import get_drama_questions
from bank_novel import get_novel_questions
from bank_poetry import get_poetry_questions
from bank_sounds import get_sounds_questions
from bank_stress import get_stress_questions
from bank_intonation import get_intonation_questions
from bank_literary import get_literary_questions
from bank_writing import get_writing_questions

def assemble():
    all_raw = []
    all_raw.extend(get_ca_questions())
    all_raw.extend(get_drama_questions())
    all_raw.extend(get_novel_questions())
    all_raw.extend(get_poetry_questions())
    all_raw.extend(get_sounds_questions())
    all_raw.extend(get_stress_questions())
    all_raw.extend(get_intonation_questions())
    all_raw.extend(get_literary_questions())
    all_raw.extend(get_writing_questions())

    print(f"Total raw questions collected: {len(all_raw)}")

    final_questions = []
    seen_texts = set()

    for idx, item in enumerate(all_raw):
        q_text = item["question"].strip()
        if q_text in seen_texts:
            print(f"Warning: Duplicate question text detected: {q_text[:50]}...")
            continue
        seen_texts.add(q_text)

        q_id = f"q_{len(final_questions) + 1:03d}"
        raw_options = item["options"]
        correct_letter = item["correct_letter"].strip().upper()

        letters = ["A", "B", "C", "D"]
        formatted_options = []
        correct_answer_str = ""

        for l, opt in zip(letters, raw_options):
            # Clean if opt already starts with letter
            opt_clean = opt.strip()
            if len(opt_clean) > 2 and opt_clean[0].upper() in letters and opt_clean[1] in [".", ")", ":", "-"]:
                opt_clean = opt_clean[2:].strip()
            entry = f"{l}. {opt_clean}"
            formatted_options.append(entry)
            if l == correct_letter:
                correct_answer_str = entry

        if not correct_answer_str:
            raise ValueError(f"Correct letter '{correct_letter}' not found in options for question {q_id}: {q_text}")

        final_questions.append({
            "id": q_id,
            "category": item["category"],
            "source": item.get("source", "predicted"),
            "text_reference": item["text_reference"],
            "skill_tested": item["skill_tested"],
            "difficulty": item.get("difficulty", "medium"),
            "question": q_text,
            "options": formatted_options,
            "correct_answer": correct_answer_str,
            "explanation": item["explanation"].strip(),
            "confidence": item.get("confidence", "high" if item.get("source") in ["CA", "textbook"] else "medium")
        })

    # Apply anti-giveaway balancer refinements
    from bank_balancer import apply_refinements
    balanced_count = apply_refinements(final_questions)
    print(f"Applied anti-giveaway balancing to {balanced_count} questions.")

    os.makedirs("data", exist_ok=True)
    out_file = os.path.join("data", "questions.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=2, ensure_ascii=False)

    print(f"Successfully assembled and wrote {len(final_questions)} questions to {out_file}!")

    # Summary Statistics
    cat_counts = {}
    source_counts = {}
    diff_counts = {}
    for q in final_questions:
        cat_counts[q["category"]] = cat_counts.get(q["category"], 0) + 1
        source_counts[q["source"]] = source_counts.get(q["source"], 0) + 1
        diff_counts[q["difficulty"]] = diff_counts.get(q["difficulty"], 0) + 1

    print("\n--- Category Breakdown ---")
    for c, cnt in sorted(cat_counts.items()):
        print(f"  {c}: {cnt}")

    print("\n--- Source Breakdown ---")
    for s, cnt in sorted(source_counts.items()):
        print(f"  {s}: {cnt}")

    print("\n--- Difficulty Breakdown ---")
    for d, cnt in sorted(diff_counts.items()):
        print(f"  {d}: {cnt}")

if __name__ == "__main__":
    assemble()
