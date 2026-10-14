# Salon website fixes

Changes for the SalonWebsite repo, found while checking the help articles (issue #6) against the code at `bb7f960` and against iconht.studio on October 14, 2026. The item numbers match "Second code check" in `kb/articles.md`.

The live-site checks themselves are finished, including the reminder cron timing (see the end of this file).

## How each fix reaches the live site

- **Website and API** (`client/`, `api/`, `packages/`): push to `main` and Vercel deploys it.
- **Iris** (`supabase/functions/chat/`): deployed on its own with `npm run deploy:chat`. A push to `main` alone does not change Iris.
- **Database** (`supabase/migrations/`): run the new migration against the live Supabase project.

## Summary

| # | Fix | Who sees it | Where | Deploy |
|---|---|---|---|---|
| 11 | Booking form warns of a fee the salon does not charge | Customers | `client/src/components/BookingWizard/StepContact.tsx:197-198` | Website |
| 1 | Home page says "Every day, 10am to 8pm" | Customers | `client/src/pages/Home.tsx:47` | Website |
| 2 | Home page promises rescheduling on the website | Customers | `client/src/pages/Home.tsx:46`, `:243` | Website |
| 3 | Daily booking limit shows a generic error | Customers | `client/src/components/BookingWizard/StepContact.tsx:70-78` | Website |
| 7 | Iris cancels with one tap, no confirm | Customers | `supabase/functions/chat/handlers.ts:856-892` | Iris |
| 4 | Iris **Sign in** button sends guests to the home page | Customers | `client/src/components/chat/ContactForm.tsx:203-218` | Website |
| 8 | Moving a booking does not reset its reminder | Customers | `api/_lib/booking.ts:446-448` | Website |
| 5 | Iris **Message the salon** shares one rate limit across all users | Customers | `api/contact.ts:42` | Website |
| 9 | Admin Promotions screen says offers show "on the site" | Owner | `client/src/pages/admin/AdminPromotions.tsx:176`, `:285` | Website |
| 10 | Promotion with a blank start date saved in the evening shows as Scheduled | Owner | `api/admin/services.ts:193-195` | Website |
| 6 | Guest bookings never join an account made later | Customers | `api/customer/appointments.ts` | Website (needs a decision first) |

Suggested order: 11, 1 and 2 first (wrong information on the live site, text-only changes), then 3, 7 and 4, then the rest.

---

## 11. Booking form warns of a fee the salon does not charge

**Live now:** the required checkbox on **Your Details** reads "I agree to the cancellation policy. Appointments cancelled less than 24 hours in advance may be subject to a late cancellation fee." The owner confirmed on October 7, 2026 that there is no cancellation fee.

**Change** `client/src/components/BookingWizard/StepContact.tsx:197-198` to:

> I agree to the cancellation policy. Please cancel at least 24 hours in advance if you can, so we can offer the time to someone else.

**Articles after the fix:** none. KB-04 already says there is no fee. Remove the "expect a few customers to ask" note from KB-04's live check.

## 1. Home page hours are wrong

**Live now:** the home page shows two different hours. The hero says "Open 7 days · 10am–7:30pm, Sun to 6pm · walk-ins welcome" (`Home.tsx:97`, correct). The **Open 7 Days** feature card says "Every day, 10am to 8pm — appointments and walk-ins welcome." (`Home.tsx:47`, wrong).

**Change** the `desc` on `Home.tsx:47` to:

> Mon–Sat 10am to 7:30pm, Sun to 6pm — appointments and walk-ins welcome.

**Articles after the fix:** none. KB-08 already has the right hours.

## 2. Home page promises rescheduling on the website

**Live now:** "Book, reschedule, or cancel 24/7 — no phone calls needed." (`Home.tsx:46`) and "Book online in under two minutes — reschedule or cancel anytime." (`Home.tsx:243`). The website has no reschedule button. Only Iris can move a booking, and only for customers who were signed in when they booked.

**Change** `Home.tsx:46` to:

> Book or cancel online 24/7. Signed in? Iris can move your booking too.

**Change** `Home.tsx:243` to:

> Book online in under two minutes — cancel anytime from your confirmation email.

**Articles after the fix:** none.

## 3. Daily booking limit shows a generic error

**Live now:** a fourth online booking in 24 hours with the same email or phone shows "Something went wrong. Please try again." The API already returns a clear message with status 429 (`api/_lib/booking.ts:229-230`): "You've reached the daily limit for online bookings. Please call us on (718) 255-6940 and we'll sort it out." The booking page throws it away because it only handles 409.

**Change** the `catch` in `StepContact.tsx:70-78` to show the server's message for a 429:

```tsx
} catch (err) {
  if (err instanceof ApiError && err.status === 409) {
    setSubmitError(
      'This time slot was just taken. Please go back and choose a different time.'
    );
  } else if (err instanceof ApiError && err.status === 429) {
    setSubmitError(err.message);
  } else {
    setSubmitError('Something went wrong. Please try again.');
  }
}
```

`ApiError.message` is the API's `error` field (`client/src/api/client.ts:65-67`). The per-IP limit (10 bookings an hour) also returns 429, with "Too many requests. Please try again later.", which is also better than the generic text.

**Articles after the fix:** KB-01, the "Online booking takes up to 3 bookings in 24 hours" line. Replace "A fourth shows **Something went wrong. Please try again.**" with "A fourth shows **You've reached the daily limit for online bookings.**"

## 7. Iris cancels with one tap

**Live now:** **Cancel** on an appointment card in Iris cancels straight away (`supabase/functions/chat/handlers.ts:856-892`). Booking and moving both ask first: moving shows "Move it to [date] at [time]?" with **Yes, move it** (`handlers.ts:628-643`). One mistaken tap cancels a real booking, and there is no undo.

**Change:** make **Cancel** ask first, the same way moving does. Point the card's **Cancel** button at a new step that replies "Cancel your [service] on [date] at [time]?" with two chips:

- **Yes, cancel it**, which calls the existing `handleCancelAppointment` with the appointment id
- **Keep it**, which goes back to **My appointments**

Keep the existing ownership check in `handleCancelAppointment` as it is. Deploy with `npm run deploy:chat`.

**Articles after the fix:**

- KB-04, "With Iris" steps: step 3 becomes "Tap **Cancel** on the appointment.", then a new step 4 "Tap **Yes, cancel it**.", then step 5 is the current step 4.
- KB-05: the first **Good to know** line becomes "Iris books, moves or cancels an appointment only when you tap a confirm button."
- `kb/articles.md` feature table, Iris row: drop "Cancelling has no confirm step…".

## 4. Iris's **Sign in** button sends guests to the home page

**Live now:** when a guest taps **My appointments** or asks Iris to move a booking, Iris shows a **Sign in to see your appointments** card. Its **Sign in** button is a link to `/profile` (`client/src/components/chat/ContactForm.tsx:210-215`), and `/profile` sends a signed-out visitor to the home page. The sign-in pop-up never opens.

**Change:** make the button open the sign-in pop-up directly. `CustomerAuthModal` takes only `onClose` (`client/src/components/auth/CustomerAuthModal.tsx:12`), so `SignInCard` can render it itself. Add `import CustomerAuthModal from '@/components/auth/CustomerAuthModal';` and drop the `Link` import, which nothing else in the file uses:

```tsx
export function SignInCard() {
  const [authOpen, setAuthOpen] = useState(false);
  return (
    <div className="card-lux bg-white p-3.5">
      <h3 className="mb-1.5 font-serif text-[15px] font-semibold">Sign in to see your appointments</h3>
      <p className="mb-3 text-xs text-muted-foreground">
        Or use the cancellation link in your confirmation email, or give the salon a call.
      </p>
      <button
        type="button"
        onClick={() => setAuthOpen(true)}
        className="inline-flex w-full items-center justify-center rounded-full bg-rose-500 px-4 py-2 text-sm font-semibold text-white transition-colors hover:bg-rose-600"
      >
        Sign in
      </button>
      {authOpen && <CustomerAuthModal onClose={() => setAuthOpen(false)} />}
    </div>
  );
}
```

Check after deploying that Iris notices the new sign-in without a page reload. If it does not, the customer has to tap **My appointments** again.

**Articles after the fix:** none.

## 8. Moving a booking does not reset its reminder

**Live now:** a move updates only the date and time (`api/_lib/booking.ts:446-448`). The reminder cron skips any row with `reminder_sent = true` (`api/cron/reminders.ts:115`). So if the reminder for the old date already went out, the new date never gets one.

**Change** the update in `booking.ts:448` to:

```ts
.update({ appointment_date: newDate, appointment_time: newTime, reminder_sent: false })
```

A move to today, or to tomorrow after that morning's run, still gets no reminder, which matches what KB-07 already says.

**Articles after the fix:** none.

## 5. Iris **Message the salon** shares one rate limit

**Live now:** Iris already forwards the visitor's address in an `X-Client-IP` header (`supabase/functions/chat/vercel.ts:55-61`), and `/api/appointments` uses it (`api/appointments.ts:56-61`, `rateLimitIdentity`). `/api/contact` does not: it calls `enforceRateLimit(req, res, 'contact')` with no identifier (`api/contact.ts:42`), so every Iris message counts against the Supabase server's address. Three Iris messages in an hour from anyone block the rest of the hour for everyone, and they see **I couldn't send that just now**.

**Change:** give `api/contact.ts` the same `rateLimitIdentity` helper as `api/appointments.ts` (trust `X-Client-IP` only when `X-Internal-Token` checks out), and pass it in:

```ts
if (!(await enforceRateLimit(req, res, 'contact', rateLimitIdentity(req)))) return;
```

The global daily contact cap (`contactGlobal`) stays as it is.

**Articles after the fix:** none. KB-09's **I couldn't send that just now** line stays useful for real failures.

## 9. Admin Promotions screen says offers show "on the site"

**Live now:** the Promotions tab says "Offers shown on the site and quoted word-for-word by Iris." (`AdminPromotions.tsx:176`) and "No promotions yet. Add one and it appears on the site straight away." (`:285`). Promotions show only in Iris, under **Current offers**.

**Change:**

- `:176` to "Offers Iris shows under **Current offers**, quoted word for word. Write the offer exactly as…" (keep the rest of the sentence).
- `:285` to "No promotions yet. Add one and Iris shows it straight away."

If the owner wants offers on the booking page too, that is a feature, not a wording fix. The fixed threading banner in the booking page would then be replaced by the promotions list.

**Articles after the fix:** KB-10, drop "even though the Promotions screen says offers appear "on the site"".

## 10. A blank promotion start date uses the UTC date

**Live now:** when **Starts** is left blank, the API leaves `starts_on` out (`api/admin/services.ts:193-195`) and the database fills it with `CURRENT_DATE` (`supabase/migrations/017_promotions.sql:47`), which is the UTC date. Iris and the admin badge use the New York date. A promotion saved after 8 PM in summer time (7 PM in winter) starts "tomorrow", shows **Scheduled** and stays out of Iris until midnight.

**Change** `services.ts:195` so the API always sends a start date, using the existing `salonToday()` in `api/_lib/dates.ts:36` (add `import { salonToday } from '../_lib/dates';`):

```ts
starts_on: starts_on || salonToday(),
```

No migration is needed.

**Articles after the fix:** KB-10, drop the "Adding a promotion in the evening" line.

## 6. Guest bookings never join an account made later

**Live now:** a booking is linked to an account only if the customer was signed in when they booked (`user_id`, `api/_lib/booking.ts:248`). **My Appointments** lists bookings by `user_id` (`api/customer/appointments.ts:39`). A customer who books as a guest and then creates an account with the same email never sees that booking, and cannot move it with Iris.

**Decide first.** The usual fix is to link a guest's bookings to their account when they sign in: set `user_id` on rows where `user_id` is null and `client_email` matches the account email. Do this **only if the account's email is confirmed**. Otherwise anyone could sign up with someone else's email and see their bookings.

**Change, if you go ahead:** at the start of the GET handler in `api/customer/appointments.ts`, when `user.email_confirmed_at` is set, run that update before listing.

**Articles after the fix:**

- KB-03: drop the "A booking made as a guest stays a guest booking…" line.
- KB-07: drop the "Booked as a guest?…" line, and step 3 can say "Open **My Appointments**".
- `kb/articles.md`: real edge case 2 no longer happens.

---

## Checked: reminder cron timing

Checked on October 14, 2026 in Vercel **Observability** → `/api/cron/reminders` → **Compute**, last 12 hours: one run between 9:00 and 9:05 AM New York time (13:00 to 13:05 UTC), status 2xx, 0% errors, one call to Resend. That fits the 13:00 UTC schedule in `vercel.json` (9 AM New York time now, 8 AM after November 1), so KB-07's "the morning of the day before" holds.

The **Logs** view on the Hobby plan keeps one hour only, but Observability keeps 12 hours, so this is the place to look next time.
