"""Phase 3: score the triage helper against your hand labels. Writes nothing to JSM.

    python src/eval_triage.py --pick-holdout   # once, before any prompt tuning
    python src/eval_triage.py                  # classify all 40 seed tickets and score them

The held-out ids in data/triage_holdout.txt are never used for tuning. Their
score is printed on its own, and that is the number to trust if the prompt
was ever changed after looking at results.

A ticket counts as a match only when the tool would have labeled it on its
own: a needs-human result is never a match, even if its guess was right.
Every run saves its rows to reports/triage_eval_<timestamp>.csv.
"""
import argparse
import csv
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import triage

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "data" / "tickets_seed.csv"
HOLDOUT = ROOT / "data" / "triage_holdout.txt"
REPORTS = ROOT / "reports"
HOLDOUT_SIZE = 10
HUMAN = "human"


def read_labeled():
    with open(SEED, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    problems = []
    for r in rows:
        if r["expected_category"] not in triage.CATEGORIES:
            problems.append(f"row {r['id']}: expected_category {r['expected_category']!r}")
        if r["expected_priority"] not in triage.PRIORITY_NAMES:
            problems.append(f"row {r['id']}: expected_priority {r['expected_priority']!r}")
    if problems:
        sys.exit("Fill in the answer key first:\n" + "\n".join(problems))
    return rows


def pick_holdout(rows):
    if HOLDOUT.exists():
        sys.exit(f"{HOLDOUT.name} already exists. The held-out set is chosen once and never changed.")
    ids = sorted(random.SystemRandom().sample([int(r["id"]) for r in rows], HOLDOUT_SIZE))
    HOLDOUT.write_text("\n".join(str(i) for i in ids) + "\n", encoding="utf-8")
    print(f"Held out {len(ids)} tickets, saved to {HOLDOUT.relative_to(ROOT)}. Do not read them while tuning.")


def read_holdout():
    if not HOLDOUT.exists():
        sys.exit("Run with --pick-holdout first, before any prompt tuning.")
    return {line.strip() for line in HOLDOUT.read_text(encoding="utf-8").splitlines() if line.strip()}


def score(rows, field):
    labeled = [r for r in rows if r["needs_human"] == "no"]
    return sum(r[f"expected_{field}"] == r[f"predicted_{field}"] for r in labeled)


def print_scores(results):
    groups = [
        ("all", results),
        ("tuning", [r for r in results if r["set"] == "tuning"]),
        ("held out", [r for r in results if r["set"] == "held out"]),
    ]
    header = f"{'':<22}" + "".join(f"{name + f' ({len(rows)})':>16}" for name, rows in groups)
    print(header)
    for label, fn in [
        ("category match", lambda rows: score(rows, "category")),
        ("priority match", lambda rows: score(rows, "priority")),
        ("sent to a human", lambda rows: sum(r["needs_human"] == "yes" for r in rows)),
    ]:
        print(f"{label:<22}" + "".join(f"{f'{fn(rows)}/{len(rows)}':>16}" for _, rows in groups))


def print_confusion(results):
    columns = list(triage.CATEGORIES) + [HUMAN]
    counts = Counter(
        (r["expected_category"], HUMAN if r["needs_human"] == "yes" else r["predicted_category"])
        for r in results
    )
    print("\nCategory confusion (rows: your label, columns: tool's label)")
    print(f"{'':<14}" + "".join(f"{c[:8]:>9}" for c in columns))
    for expected in triage.CATEGORIES:
        print(f"{expected:<14}" + "".join(f"{counts[(expected, c)] or '.':>9}" for c in columns))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pick-holdout", action="store_true", help=f"choose {HOLDOUT_SIZE} held-out ids once")
    args = parser.parse_args()

    rows = read_labeled()
    if args.pick_holdout:
        pick_holdout(rows)
        return
    holdout = read_holdout()

    classifier = triage.Classifier()
    results = []
    for r in rows:
        result = classifier.classify(r["summary"], r["description"])
        t = result.triage
        results.append(
            {
                "id": r["id"],
                "set": "held out" if r["id"] in holdout else "tuning",
                "expected_category": r["expected_category"],
                "predicted_category": t.category if t else "",
                "expected_priority": r["expected_priority"],
                "predicted_priority": t.priority if t else "",
                "sentiment": t.sentiment if t else "",
                "article_id": t.article_id if t else "",
                "confidence": f"{t.confidence:.2f}" if t else "",
                "needs_human": "yes" if result.needs_human else "no",
                "problem": result.problem or "",
            }
        )
        print(f"row {r['id']:>2}: {triage.describe(result)}")

    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"triage_eval_{datetime.now():%Y%m%d_%H%M%S}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0]))
        writer.writeheader()
        writer.writerows(results)

    print(f"\nModel: {triage.MODEL}\n")
    print_scores(results)
    print_confusion(results)
    print(f"\nRows saved to {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
