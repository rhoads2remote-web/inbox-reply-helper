# Inbox Reply Helper

A privacy-conscious starter project for spotting email threads that may need a reply and preparing follow-up text for a person to review.

The prototype reads a local JSON export, flags threads that are explicitly marked as needing a response, and prints a suggested reply beside a short thread summary. It does not connect to an inbox, create Gmail drafts, or send messages.

## What it demonstrates

- A configurable overdue threshold (two days by default)
- A review-first workflow that shows the thread context next to a reply suggestion
- No send function or mailbox credentials
- Fictional sample data only

## Run it

Requires Python 3.10 or newer. From this folder, run:

```bash
python app.py --input sample_threads.json
```

To change the overdue threshold:

```bash
python app.py --input sample_threads.json --overdue-after 3
```

The sample file contains an `as_of` date so the output is repeatable. Remove `as_of` from your own JSON file to use today's date.

## Input format

Each thread has a subject, a short summary, the other person's first name, the last message date, a boolean `needs_response` review field, and a short `reply_context` used to personalize the example draft.

```json
{
  "as_of": "2026-11-09",
  "threads": [
    {
      "subject": "Project timeline",
      "summary": "Jordan asked whether the revised timeline is ready.",
      "from_name": "Jordan",
      "last_message_date": "2026-11-05",
      "needs_response": true,
      "reply_context": "the revised timeline"
    }
  ]
}
```

`needs_response` is deliberately explicit in this starter. A real inbox classifier should be reviewed against false positives and should explain why it selected each thread. Keep human approval between any suggested reply and sending it.

## Safety and privacy

- Do not commit mailbox exports, real email addresses, message content, OAuth credentials, or access tokens.
- Keep sample data fictional.
- If you add a Gmail integration, use OAuth and the narrowest practical scopes. Read-only access is enough for triage; creating drafts requires additional permission. Keep sending as a separate, explicit action that requires approval.
- Review every reply before sending. The prototype does not send email.

## Example output

```text
1. OVERDUE (4 days) — Project timeline
   Thread: Jordan asked whether the revised timeline is ready.
   Draft:
   Hi Jordan, just following up on the revised timeline. Is this still needed? I can send an update shortly.
```

## GitHub

See [GITHUB_SETUP.md](GITHUB_SETUP.md) for instructions to create a GitHub repository and push this folder.
