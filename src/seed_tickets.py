"""Phase 2: create sample customers and tickets in JSM from a CSV.

Load one batch of rows at a time, on different days, so response times reflect
how the tickets were actually worked:

    python src/seed_tickets.py --rows 1-10 --dry-run   # check the rows, no network
    python src/seed_tickets.py --rows 1-10             # batch 1

Each new issue key is saved to data/seeded_tickets.csv next to its CSV id.
Rows already listed there are skipped, so a rerun never creates a duplicate.
Turn customer notifications off before the first run (PRD Phase 0, step 6).
"""
import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import jsm

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CSV = ROOT / "data" / "tickets_seed.csv"
SEEDED = ROOT / "data" / "seeded_tickets.csv"
SEEDED_FIELDS = ["csv_id", "issue_key", "customer_email", "account_id", "created_at"]

# The only columns this script reads. The expected_ columns are the triage
# answer key and are never sent to JSM.
COLUMNS = ["id", "customer_name", "customer_email", "request_type", "summary", "description"]

REQUEST_TYPES = [
    "Booking problem",
    "Reschedule or cancel",
    "Chat assistant (Iris) question",
    "Confirmation email not received",
    "Something is broken (bug report)",
    "General question",
]


def parse_rows(spec):
    """Turn '1-10' or '1,4,7-9' into a set of ids."""
    ids = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            ids.update(range(int(lo), int(hi) + 1))
        elif part:
            ids.add(int(part))
    return ids


def read_tickets(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        missing = [c for c in COLUMNS if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"{path} is missing columns: {', '.join(missing)}")
        tickets = [{c: (row[c] or "").strip() for c in COLUMNS} for row in reader]

    problems = []
    for t in tickets:
        if t["request_type"] not in REQUEST_TYPES:
            problems.append(f"row {t['id']}: unknown request type {t['request_type']!r}")
        if not t["customer_email"].endswith("@example.com"):
            problems.append(f"row {t['id']}: use an @example.com address")
        if not t["summary"] or not t["description"]:
            problems.append(f"row {t['id']}: summary and description are required")
    if problems:
        sys.exit("\n".join(problems))
    return tickets


def load_seeded():
    if not SEEDED.exists():
        return {}
    with open(SEEDED, newline="", encoding="utf-8") as f:
        return {row["csv_id"]: row for row in csv.DictReader(f)}


def save_seeded(row):
    new_file = not SEEDED.exists()
    with open(SEEDED, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SEEDED_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(row)


def find_customer(email, desk_id):
    """Find the accountId of a customer that already exists."""
    for c in jsm.paged(f"/rest/servicedeskapi/servicedesk/{desk_id}/customer", query=email):
        if (c.get("emailAddress") or "").lower() == email.lower():
            return c["accountId"]
    users = jsm.get("/rest/api/3/user/search", query=email)
    exact = [u for u in users if (u.get("emailAddress") or "").lower() == email.lower()]
    if exact:
        return exact[0]["accountId"]
    if len(users) == 1:  # email hidden by privacy settings, but the search is unambiguous
        return users[0]["accountId"]
    return None


def ensure_customer(name, email, desk_id, known):
    """Create the customer, or reuse the existing one, and add them to the desk."""
    if email in known:
        return known[email]
    try:
        account_id = jsm.post(
            "/rest/servicedeskapi/customer", {"email": email, "displayName": name}
        )["accountId"]
    except jsm.JSMError as e:
        if e.status != 400:
            raise
        account_id = find_customer(email, desk_id)  # 400 means the account already exists
        if not account_id:
            raise
    jsm.post(f"/rest/servicedeskapi/servicedesk/{desk_id}/customer", {"accountIds": [account_id]})
    known[email] = account_id
    return account_id


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--csv", default=str(DEFAULT_CSV), help="ticket CSV (default data/tickets_seed.csv)")
    parser.add_argument("--rows", required=True, help="CSV ids to load, such as 1-10 or 1,4,7-9")
    parser.add_argument("--dry-run", action="store_true", help="check and print the rows without calling JSM")
    args = parser.parse_args()

    wanted = parse_rows(args.rows)
    tickets = [t for t in read_tickets(args.csv) if int(t["id"]) in wanted]
    seeded = load_seeded()
    todo = [t for t in tickets if t["id"] not in seeded]
    for t in tickets:
        if t["id"] in seeded:
            print(f"skip  row {t['id']:>2}: already loaded as {seeded[t['id']]['issue_key']}")

    if args.dry_run:
        for t in todo:
            print(f"would row {t['id']:>2}: [{t['request_type']}] {t['summary']}  ({t['customer_email']})")
        print(f"\n{len(todo)} ticket(s) would be created. Nothing was sent.")
        return

    if not todo:
        print("Nothing to load.")
        return

    print("Reminder: customer notifications must be off (Project settings, Customer notifications).\n")
    desk_id = jsm.service_desk_id()
    type_ids = jsm.request_types(desk_id)
    missing = [rt for rt in REQUEST_TYPES if rt not in type_ids]
    if missing:
        sys.exit(f"These request types are not in JSM yet: {', '.join(missing)}")

    known = {row["customer_email"]: row["account_id"] for row in seeded.values()}
    for t in todo:
        account_id = ensure_customer(t["customer_name"], t["customer_email"], desk_id, known)
        created = jsm.post(
            "/rest/servicedeskapi/request",
            {
                "serviceDeskId": desk_id,
                "requestTypeId": type_ids[t["request_type"]],
                "requestFieldValues": {"summary": t["summary"], "description": t["description"]},
                "raiseOnBehalfOf": account_id,
            },
        )
        save_seeded(
            {
                "csv_id": t["id"],
                "issue_key": created["issueKey"],
                "customer_email": t["customer_email"],
                "account_id": account_id,
                "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            }
        )
        print(f"made  row {t['id']:>2}: {created['issueKey']}  [{t['request_type']}] {t['summary']}")


if __name__ == "__main__":
    main()
