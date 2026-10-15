# How the sample tickets are labeled

`expected_category` and `expected_priority` in `tickets_seed.csv` are the answer key for the triage score (PRD Phase 3, step 6). They were filled in before the triage tool was ever run on these tickets, using the rules below. Claude drafted them on October 15, 2026; the owner of this repo reviewed and approved every row.

## Category

The category is what the customer actually needs, not the request type they picked.

| Category | Use it when the customer |
|---|---|
| `booking` | is trying to make a new booking: availability, the form, the daily limit, choosing a service or stylist |
| `reschedule` | wants to move or cancel a booking that already exists, including asking Iris to move it |
| `iris` | has a question about the chat assistant itself: what it can do, what it said, why typing is off |
| `confirmation` | is missing an email (confirmation or reminder), or asks why no text came |
| `bug` | hit something the site did wrong, or a gap engineering should fix, even when there is a workaround |
| `general` | asks about the salon: hours, location, parking, prices, group or bridal services |

Mix: 12 reschedule, 8 booking, 6 iris, 6 confirmation, 4 bug, 4 general.

## Priority

| Priority | Use it when |
|---|---|
| `high` | the appointment is today or tomorrow and the customer needs an answer or action before it; or a real booking is wrong (such as the wrong day); or the customer is angry and says they will go elsewhere |
| `medium` | the customer cannot finish something (book, change, get an email) or is unsure a booking exists, and nothing is due within a day |
| `low` | a how-to or information question, or a change the customer can make themselves with no time pressure |

Mix: 6 high, 13 medium, 21 low.

## Filed under the wrong request type on purpose

| id | Filed as | True category | Why |
|---|---|---|---|
| 10 | General question | confirmation | asks why no reminder text came; the site sends emails, not texts |
| 11 | Something is broken (bug report) | iris | "Typed messages are unavailable" is Iris's designed fallback, not a fault |
| 25 | Chat assistant (Iris) question | reschedule | a guest wants to move a booking; Iris refusing is by design |
| 37 | Booking problem | general | asks whether the salon does bridal party hair |

## Dated details

Tickets 8 and 16 describe the site before fixes that are now live: the booking form's late fee warning (removed October 14, 2026) and the time zone bug (fixed October 7, 2026). Read them as bookings made before those fixes.
