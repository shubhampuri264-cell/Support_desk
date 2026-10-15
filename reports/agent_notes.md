# Agent notes

Anything surprising from working the sample tickets as the agent (PRD Phase 2, step 4). Newest batch last.

## Batch 1: SUP-1 to SUP-10 (October 15, 2026)

Seeded and worked the same afternoon. All ten resolved with a public reply that links a help article; first response and resolution both under 20 minutes.

- **The site had no resolution values, so no ticket could stop its resolution clock.** The **Resolved** transition requires a resolution, the list was empty, and **Time to resolution** stops only when a resolution is set. Resolving SUP-1 without one moved it to Done with the clock still running. Added a **Done** resolution (Jira settings, Issues, Resolutions) and reopened and resolved SUP-1 again, so its history shows one reopen.
- **No parking or transit information anywhere** (SUP-7). KB-08 had the address and hours only. Answered the same day: there is no salon parking, only curbside or public parking, and the 7 train stops right across the street. Added to KB-08 in `kb/articles.md` and on the live page (version 2).
- **Customers expect text reminders** (SUP-10). The site sends emails only, and that stays the case for now (confirmed October 15, 2026). KB-07 already says so.
- **Old bookings still carry the old fee warning** (SUP-8). Bookings made before the October 14 fix saw "may be subject to a late cancellation fee", so a sick customer worried about a charge. Expect this until those bookings are past.
- **Support cannot change a booking itself.** Several replies offered to move or cancel a booking for the customer, but only the owner has the admin login, and admin can only cancel (no move, no email edit, no booking on someone's behalf, and no email to the customer when she cancels). Decided the same day: the help desk never changes bookings. Replies and articles send customers to self-service or to the salon's phone, (718) 255-6940, to confirm, cancel or reschedule. KB-01, KB-03, KB-04, KB-07 and KB-09 were updated in `kb/articles.md` and on the live pages. The replies already posted on SUP-1, SUP-3, SUP-5 and SUP-8 still offer to do it for the customer; they were left as posted.
- **A real bug from a sample ticket** (SUP-6): the booking form hides the API's clear 400 and 404 messages behind "Something went wrong", so a page left open overnight cannot book. Escalated in `reports/bug_escalations.md`.
- **Wrong request types are easy to spot but left as filed** (SUP-10 filed as General question). Changing them would make the request type reports in Phase 4 tidier, but the original choice is what the triage score compares against.
