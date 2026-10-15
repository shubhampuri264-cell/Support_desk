# Agent notes

Anything surprising from working the sample tickets as the agent (PRD Phase 2, step 4). Newest batch last.

## Batch 1: SUP-1 to SUP-10 (October 15, 2026)

Seeded and worked the same afternoon. All ten resolved with a public reply that links a help article; first response and resolution both under 20 minutes.

- **The site had no resolution values, so no ticket could stop its resolution clock.** The **Resolved** transition requires a resolution, the list was empty, and **Time to resolution** stops only when a resolution is set. Resolving SUP-1 without one moved it to Done with the clock still running. Added a **Done** resolution (Jira settings, Issues, Resolutions) and reopened and resolved SUP-1 again, so its history shows one reopen.
- **No parking or transit information anywhere** (SUP-7). KB-08 has the address and hours only. Ask the owner what to tell customers about parking and the nearest subway stop, and add it to KB-08.
- **Customers expect text reminders** (SUP-10). The site sends emails only. Worth raising with the owner as a feature request; until then KB-07 covers the reminder email.
- **Old bookings still carry the old fee warning** (SUP-8). Bookings made before the October 14 fix saw "may be subject to a late cancellation fee", so a sick customer worried about a charge. Expect this until those bookings are past.
- **Support cannot change a booking itself.** Several replies offer to move or cancel a booking for the customer, but only the owner has the admin login. Each of those requests needs a hand-off to the salon. Decide with the owner how support passes them on (email, a shared note, or agent access to admin).
- **A real bug from a sample ticket** (SUP-6): the booking form hides the API's clear 400 and 404 messages behind "Something went wrong", so a page left open overnight cannot book. Escalated in `reports/bug_escalations.md`.
- **Wrong request types are easy to spot but left as filed** (SUP-10 filed as General question). Changing them would make the request type reports in Phase 4 tidier, but the original choice is what the triage score compares against.
