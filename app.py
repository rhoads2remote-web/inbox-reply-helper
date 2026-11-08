"""Review-first email follow-up triage demo. This program never sends email."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from typing import Any


def load_data(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as source:
        return json.load(source)


def make_draft(thread: dict[str, Any]) -> str:
    name = thread.get("from_name", "there").strip() or "there"
    context = thread.get("reply_context", "this").strip() or "this"
    return (
        f"Hi {name}, just following up on {context}. "
        "Is this still needed? I can send an update shortly."
    )


def review_threads(
    data: dict[str, Any], *, today: date, overdue_after: int
) -> list[tuple[dict[str, Any], int]]:
    selected: list[tuple[dict[str, Any], int]] = []
    for thread in data.get("threads", []):
        if not thread.get("needs_response", False):
            continue

        last_message = date.fromisoformat(thread["last_message_date"])
        age_days = max(0, (today - last_message).days)
        selected.append((thread, age_days))

    selected.sort(key=lambda item: item[1], reverse=True)
    return selected


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Flag reviewed threads that may need a reply and print unsent suggestions."
    )
    parser.add_argument("--input", type=Path, default=Path("sample_threads.json"))
    parser.add_argument("--overdue-after", type=int, default=2)
    args = parser.parse_args()

    if args.overdue_after < 0:
        parser.error("--overdue-after must be zero or greater")

    data = load_data(args.input)
    today = date.fromisoformat(data["as_of"]) if data.get("as_of") else date.today()
    results = review_threads(data, today=today, overdue_after=args.overdue_after)

    if not results:
        print("Nothing needs a reply.")
        return

    for index, (thread, age_days) in enumerate(results, start=1):
        status = "OVERDUE" if age_days >= args.overdue_after else "REPLY NEEDED"
        print(f"{index}. {status} ({age_days} days) — {thread['subject']}")
        print(f"   Thread: {thread['summary']}")
        print(f"   Draft:  {make_draft(thread)}")
        print()

    print("These are suggestions only. Review them before sending; this demo cannot send email.")


if __name__ == "__main__":
    main()
