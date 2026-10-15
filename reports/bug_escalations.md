# Bug escalations from the sample tickets

Every ticket labeled `bug` in Phase 2 is escalated to engineering here, and the ticket's internal note links its section. The tickets are sample tickets, so these escalations are not filed as issues in the SalonWebsite repo. Where the bug is real in the SalonWebsite code, the section says so, and it can be filed there as a real issue.

Code references are to SalonWebsite `acfbbc9`.

## SUP-6

**Booking form shows "Something went wrong" for errors that already have a clear message**

- **Ticket:** SUP-6 (sample ticket 6), Something is broken (bug report), priority medium.
- **Customer report:** left the booking page open overnight, picked a keratin treatment and a time in the morning, and got **Something went wrong** on **Confirm Booking**, twice.
- **What happens:** the booking API rejects a stale request with a clear reason: 404 **Service not found** when the owner has turned the service off (`api/_lib/booking.ts:113-123`, `api/appointments.ts:66-68`), and 400 for a date or time outside the booking window or a stylist who no longer offers the service (`api/appointments.ts:69-74`). The booking form only passes the server's message through for 409 and 429, and shows **Something went wrong. Please try again.** for everything else (`client/src/components/BookingWizard/StepContact.tsx:70-81`). Retrying gives the same error, so the customer is stuck.
- **Real in the code:** yes.
- **Proposed fix:** in `StepContact.tsx`, handle 400 and 404 too: show the server's message, or "Something changed since you opened this page. Please reload and choose your service and time again."
- **Told the customer:** reload iconht.studio/book and book again; if the service is missing after a reload, call the salon. Linked KB-01.
- **Status:** escalated October 15, 2026.
