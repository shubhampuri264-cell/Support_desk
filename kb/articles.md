# Help center articles

Drafts of every help article before it goes into the JSM knowledge base. Articles describe only features confirmed on the live site.

## Feature check (issue #5)

Checked against the Salon website code on October 6, 2026. Every item still needs a check on the live site, because the deployed version or the owner's settings in the admin page can differ from the code.

### What the site does

| Feature | How it works |
|---|---|
| Booking | Four steps: service, stylist, date and time, your details. The stylist step is skipped when only one stylist offers the service. There is no "anyone available" option. Guests can book; signed-in customers have the booking linked to their account |
| Required details | Full name, email, phone (digits, spaces, `-`, `+`, `()`), and a ticked cancellation policy box. Notes and the marketing opt-in are optional |
| Availability | Start times every 30 minutes from opening. The whole service must end by closing time. Bookable up to 180 days ahead, with no minimum notice; the calendar greys out later dates. Times are the salon's New York time, whatever the visitor's time zone. A day with no times shows the reason (date passed, beyond 180 days, salon closed) or "No availability on this date". A time is taken only if it overlaps another booking or a slot the owner blocked |
| Confirmation | The page shows "Booking Confirmed!" with the date, time and an 8 character booking reference. A confirmation email follows. Bookings are confirmed immediately |
| Cancelling | The cancel link in the confirmation email (with a "Confirm Cancellation" click), the profile page for signed-in customers, or Iris. No cutoff is enforced. The booking form says cancelling under 24 hours ahead "may be subject to a late cancellation fee", but nothing charges it. The owner confirmed on October 7, 2026 that the salon charges no cancellation fee |
| Rescheduling | Signed-in customers: through Iris, to a new date and time with the same service and stylist. Guests: through the link in the confirmation email. In the code, that link is "Cancel appointment", and the cancellation email then offers "Book a new appointment", so a guest moves a booking in two steps. The live-site check confirms whether the deployed site does it in one step. The profile page has no reschedule button |
| Iris chat assistant | Books, shows "My appointments", cancels, reschedules, and shows prices, service details, offers, hours and location. It can also pass a message to the salon. Bookings and moves only happen when the customer taps a confirm button, and a confirm card expires after 10 minutes. Cancelling has no confirm step: the **Cancel** button on an appointment card cancels at once |
| Iris buttons | Book an appointment, My appointments, Prices, Current offers, Hours & location, Start over, and a Call button. When typed messages are unavailable, the message box reads "Typed messages are unavailable right now, the buttons above still work" |
| Emails | Booking confirmation, cancellation, "Your Appointment Has Moved" after a reschedule, a reminder the day before, a review request the day after (only if the owner set a review link), contact form copies and password resets |
| Text messages | **None.** The code has unused settings for a text provider, but sends no texts |
| Customer accounts | Sign up, sign in, password reset, and a profile page listing appointments with Cancel and "Resend Email" (once per 5 minutes per appointment) |
| Contact form | Name, email and a message of 10 to 1,000 characters. It goes to the owner's inbox with reply-to set to the customer. Limited to 3 messages an hour per visitor. On failure it asks the customer to call |
| Hours | Monday to Saturday 10:00 AM to 7:30 PM, Sunday 10:00 AM to 6:00 PM, open every day. The owner confirmed the closing times on October 7, 2026; the opening time comes from the code. Walk-ins are welcome |
| Services and prices | Stored in the database and editable by the owner, so check the live prices. Hair services are with the hair stylist; threading, waxing, facials, lashes and brows are with the beauty specialist. The booking page shows prices but not service lengths |
| Offers | A fixed banner on the booking page ("Eyebrow threading is free with any facial or special treatment service"). Promotions the owner adds in admin appear only in Iris, not on the booking page |
| Payments | **None.** The site takes no payment, card or deposit. The cancellation email says "you have not been charged" |
| Admin (owner only) | Log in at `/admin/login`. Tabs: Dashboard, Appointments (search, filter, status, notes, CSV export), Services (add, edit, price, length, on or off), Promotions, Block Slots. Stylists and opening hours cannot be managed in admin. Changes the owner makes in admin send the customer no email, by design: the owner calls or emails the client herself |

### Differences from the PRD

1. **No text messages.** Rename the request type to "Confirmation email not received" and article 7 to "I did not get a confirmation email".
2. **Two ways to reschedule.** Signed-in customers use Iris; guests use the link in their confirmation email. Article 3 has to cover both paths.
3. **No payments on the site, and the owner does not want to add them.** Phase 3B therefore uses a made-up business instead (plan B, decided October 7, 2026).
4. **A service added in admin cannot be booked online** until it is linked to a stylist, and admin has no way to do that. Customers see "We can't book X online right now. Please call us." Article 10 must say so.
5. **Admin promotions show only in Iris.** Article 10 must say so.
6. **Customer accounts exist** (not in the PRD list). Articles 1, 3, 4 and 7 can use the profile page and the Resend Email button.

### Live-site checklist (you)

Before a test booking, tell the owner or block the slot. A real booking lands on her calendar and sends her an alert, and every email counts against the site's daily email limit. Cancel any test booking right after.

- [ ] Booking: four steps, stylist step skipped for a one-stylist service, reference number on the confirmation page
- [ ] Confirmation email arrives, from which address, and how long it takes; check the spam folder
- [ ] Cancel through the email link
- [ ] Signed in: profile shows the appointment with Cancel and Resend Email
- [ ] Iris: book, My appointments, cancel, reschedule while signed in, prices, offers, hours and location, message the salon
- [ ] Iris as a guest: the reschedule refusal message
- [ ] Contact form sends
- [ ] Hours and prices on the site match the table above
- [ ] Admin tabs (only with the owner's login, or ask her)
- [x] Vercel production settings: customer emails reach customers, so `EMAIL_DEV_OVERRIDE` is not redirecting them and `RESEND_API_KEY` is set (verified October 7, 2026). The sender address is still checked in KB-07
- [x] Owner's inbox: customers receive their booking, cancellation and reschedule emails, and the owner receives hers at her business inbox (verified October 7, 2026)
- [x] Iris is deployed and works on the live site, with typing on and its safeguards in place (confirmed October 7, 2026)
- [ ] Iris runs from the Supabase chat function, which is deployed on its own (`npm run deploy:chat`), so `origin/main` does not prove what Iris says. Compare Iris's live replies with the wording in KB-03 to KB-06
- [ ] Work through the **Live check** list at the end of each article below

### Article list after the check

1. How do I book an appointment?
2. How do I choose a service and stylist?
3. How do I reschedule my appointment? (signed in: Iris; guest: the link in the confirmation email)
4. How do I cancel my appointment? (email link, profile, Iris; the 24 hour note)
5. Using the chat assistant (Iris)
6. Iris didn't understand me, or won't let me type (use the buttons)
7. I did not get a confirmation email (spam folder, check the email address, Resend Email, call)
8. What are the salon's hours and where is it?
9. How do I contact the salon? (contact form, phone, Iris)
10. Internal, owner only: adding a service or a promotion (and why a new service may not be bookable online)

### Real edge cases (ideas for sample tickets)

These come from the code and make realistic tickets. The labels in `data/tickets_seed.csv` stay yours.

1. A guest asks how to move an appointment they booked without an account.
2. A customer created an account after booking as a guest and cannot see the booking under "My appointments".
3. A same-day booking, or a next-day booking made after the morning email run, gets no reminder.
4. A family hits the limit of 3 online bookings a day per email or phone.
5. A customer sees "We can't book X online right now" for a new service.
6. A visitor in a time zone ahead of New York gets an appointment on the wrong day. **Fixed October 7, 2026** (SalonWebsite commit `bb7f960`, confirmed on the live site). Bookings made before the fix may still be on the wrong day, so ticket 16 stays as a pre-fix report.
7. Iris says there are no offers while the booking page shows the threading offer.
8. A long "Message the salon" sent through Iris fails.
9. The Iris confirm card expired ("That confirmation has expired").
10. A page left open shows times for a retired service, then fails with "Something went wrong".
11. A customer asks why they did not get a text.

### Second code check (October 7, 2026)

A closer read of the SalonWebsite code for the article wording turned up these problems. They are product issues for engineering, not article topics. File the ones you confirm on the live site as issues in the SalonWebsite repo yourself.

1. **Hours disagree.** The home page says "Every day, 10am to 8pm" (`client/src/pages/Home.tsx:47`). The booking rules, the Location page and Iris all use Monday to Saturday 10:00 AM to 7:30 PM, Sunday 10:00 AM to 6:00 PM. The owner confirmed 7:30 PM and 6:00 PM on October 7, 2026, so the home page is the one to fix.
2. **The home page promises rescheduling on the website** ("Book, reschedule, or cancel 24/7", `Home.tsx:46`), but only Iris can move a booking, and only for signed-in customers.
3. **The daily booking limit shows a generic error.** The fourth online booking in a day with the same email or phone shows "Something went wrong. Please try again." The clearer message in `api/_lib/booking.ts:230` never reaches the booking page.
4. **Iris's "Sign in" button for guests goes to `/profile`,** which sends a signed-out visitor to the home page instead of opening the sign-in pop-up.
5. **"Message the salon" in Iris may share one rate limit across all users,** because it calls `/api/contact` without the customer's IP address.
6. **Guest bookings never join an account** created later with the same email, so they do not appear in My Appointments.

Found while checking the article drafts against the code (SalonWebsite `bb7f960`):

7. **Iris's Cancel button cancels straight away.** Booking and moving need a confirm tap, but **Cancel** on an appointment card has none (`supabase/functions/chat/handlers.ts:856-892`). One mistaken tap cancels the booking.
8. **Moving a booking does not reset its reminder.** The move changes only the date and time (`api/_lib/booking.ts:446-448`). If the reminder for the old date already went out, the new date gets no reminder.
9. **The admin Promotions screen says offers appear "on the site"** ("Offers shown on the site…", "it appears on the site straight away", `client/src/pages/admin/AdminPromotions.tsx:176` and `:285`), but only Iris shows them.
10. **A blank promotion start date uses the database's UTC date.** Iris and the admin badge use the New York date, so a promotion saved in the evening (after 8 PM in summer time, 7 PM in winter) with **Starts** left blank shows as **Scheduled** and stays out of Iris until midnight (`supabase/migrations/017_promotions.sql:47`).

Found from the owner's answers (October 7, 2026):

11. **The booking form warns of a fee the salon does not charge.** The cancellation policy box says cancelling within 24 hours "may be subject to a late cancellation fee" (`client/src/components/BookingWizard/StepContact.tsx:198`). The owner confirmed there is no cancellation fee, so customers who cancel late may worry about a charge that never comes.

## Articles

Each article follows the same shape: a title phrased the way a customer searches, who it is for, numbered steps with one action each, and what to do if it still does not work. Words in **bold** are the exact labels on the site. Article 10 is internal: publish it to agents only.

The owner answered on October 7, 2026: the salon charges no cancellation fee (article 4), closes at 7:30 PM Monday to Saturday and 6:00 PM on Sunday (article 8), welcomes walk-ins (article 8), and is happy with the salon's name, address, phone and email appearing in the help center (article 9).

Every label and rule below was checked against the SalonWebsite code at commit `bb7f960` (`origin/main` on October 7, 2026). Each article ends with a **Live check** list: things the code supports but only the live site, a real inbox or the owner can confirm. Tick each item during the live-site check, fix the article if the site differs, and delete the list before pasting the article into JSM.

---

### KB-01. How do I book an appointment?

**Who this is for:** anyone booking online, with or without an account.

**Steps**

1. Go to iconht.studio/book.
2. Under **Choose a Service**, click the service you want.
3. Under **Choose a Stylist**, click a stylist. If only one stylist offers the service, this step is skipped.
4. Under **Pick a Date & Time**, click a date.
5. Under **Available times on** [your date], click a time.
6. Under **Your Details**, enter your full name, phone and email.
7. Tick the box to agree to the cancellation policy.
8. Click **Confirm Booking**.
9. Note the **Booking ref** on the **Booking Confirmed!** page. A confirmation email follows.

**Good to know**

- Your booking is confirmed as soon as you see **Booking Confirmed!**. There is no deposit and no card payment.
- Sign in first (**Sign In** at the top of the page; on a phone, open the menu) if you want the booking to appear under **My Appointments** later.
- You can book up to 180 days ahead. Later dates are greyed out on the calendar.
- Times are the salon's local time (New York). Booking from another time zone? Pick the time you will be at the salon.
- A date with no free times says so, for example **No availability on this date**. Pick another date.
- Online booking takes up to 3 bookings in 24 hours with the same email or phone. A fourth shows **Something went wrong. Please try again.** Booking for a larger family or group? Book the first three online and call (718) 255-6940 for the rest.
- If you see **This time slot was just taken**, someone booked it a moment before you. Go back and pick another time.
- You can also book through the chat assistant. See KB-05.

**If it still does not work**

Raise a **Booking problem** request. Tell us the service, the date and time you wanted, and the exact message you saw. A screenshot helps. Or call (718) 255-6940.

#### Live check (remove before publishing)

- [ ] iconht.studio/book loads, and steps 2 to 9 match the live labels
- [ ] Make one test booking (tell the owner first, cancel it after): **Booking Confirmed!** shows a **Booking ref**, and the confirmation email arrives. Note the sender, how long it took, and whether it landed in spam
- [ ] Which services skip **Choose a Stylist** live. This comes from the stylist links in the database, not the code
- [x] **Ask Iris** shows on the live site (the "book through the chat assistant" line depends on it). Iris is live (confirmed October 7, 2026)
- [ ] Optional, only with the owner's OK: a fourth booking with the same email in 24 hours shows **Something went wrong. Please try again.** If engineering fixes that message first (second code check, item 3), update this article

---

### KB-02. How do I choose a service and stylist?

**Who this is for:** anyone deciding what to book or who to book with.

**Steps**

1. Go to iconht.studio/book.
2. Look through the services and their prices. They are grouped by type, such as **Hair Services** and **Facial Services**.
3. Click the service you want.
4. If **Choose a Stylist** appears, click the stylist you want.
5. If you go straight to **Pick a Date & Time**, only one stylist offers that service, and your booking is with them.

**Good to know**

- Hair services are with our hair stylist. Threading, waxing, facials, lashes and brows are with our threading and facial specialist. A few services, such as Hot Oil Hair Massage, are offered by both, so you pick.
- There is no "anyone available" option. Pick a stylist, then choose from their open times.
- A price range such as **$200–300** depends on your hair length and texture. **Price on consultation** means the stylist quotes in the salon.
- The booking page shows prices but not how long each service takes. Tap **Prices** in Iris to see the length of each service, or ask us.
- The **Special Offer** banner on the booking page: eyebrow threading is free with any facial or special treatment service.
- If you see **We can't book [service] online right now. Please call us**, that service can only be booked by phone for now: call (718) 255-6940.

**If it still does not work**

Not sure which service to book? Raise a **General question** request. A service will not book? Raise a **Booking problem** request with the service name and the message you saw.

#### Live check (remove before publishing)

- [ ] Category headings on the live booking page match step 2
- [ ] Hot Oil Hair Massage shows **Choose a Stylist** with both stylists, and the hair services go straight to **Pick a Date & Time**. Both depend on the stylist links in the database
- [ ] The **$200–300** example is still a live price (the code's data has it for Balayage). If not, swap in a range that is
- [ ] Which services show **Price on consultation** (in the code's data, only Cut and Style)
- [ ] Iris's **Prices** list shows "· N min" next to each service
- [ ] Ask the owner whether the threading offer still runs, since the banner is fixed in the code

---

### KB-03. How do I reschedule my appointment?

**Who this is for:** anyone who wants to move an appointment. How you do it depends on whether you were signed in when you booked.

**If you were signed in when you booked: move it with Iris**

1. Sign in with **Sign In** at the top of the page.
2. Click **Ask Iris** at the bottom right of the page.
3. Tap **My appointments**.
4. Tap **Move** on the appointment you want to change.
5. Tap the new day.
6. Tap the new time.
7. Check the details and tap **Yes, move it**.
8. Look for the email **Your Icon Studio Appointment Has Moved**.

Iris keeps the same service and stylist. To change the service or stylist, cancel and book again.

**If you booked as a guest: cancel, then book the new time**

1. Open iconht.studio/book in a new tab and check that the new time you want is free.
2. Open your confirmation email, **Your Icon Studio Appointment is Confirmed!**.
3. Click **Cancel appointment**.
4. Click **Confirm Cancellation**.
5. Click **Book a New Appointment**.
6. Book the new time (see KB-01).

**Good to know**

- The **My Appointments** page has a **Cancel** button but no move button. Use Iris to move a booking.
- Iris offers the next 6 days with free times. For a date further out, use the guest steps above or call.
- A booking made as a guest stays a guest booking, even if you create an account later with the same email. Iris then says **You haven't got anything booked at the moment.** Use the guest steps above.
- Booked as a guest and asked Iris to move it? Iris asks you to sign in or use the link in your confirmation email. Use the guest steps above.
- Changing an appointment for today? Call (718) 255-6940 so the salon knows straight away.

**If it still does not work**

Raise a **Reschedule or cancel** request with your name, your booking reference, your current appointment and the time you want instead. Or call (718) 255-6940.

#### Live check (remove before publishing)

- [ ] Signed in: move a test booking with Iris end to end (steps 1 to 8), and the **Your Icon Studio Appointment Has Moved** email arrives
- [ ] As a guest: Iris refuses to move and points to the email link. Note its exact words
- [ ] Click **Cancel appointment** in a real confirmation email: it opens iconht.studio/booking/cancel with a token, then **Confirm Cancellation** and **Book a New Appointment** appear. The confirmation email builds this link slightly differently from the other emails, so a real click is the only proof
- [ ] **Sign In** and **Ask Iris** appear where the steps say, on a computer and on a phone

---

### KB-04. How do I cancel my appointment?

**Who this is for:** anyone who needs to cancel. There are three ways.

**From your confirmation email (works for everyone)**

1. Open your confirmation email, **Your Icon Studio Appointment is Confirmed!**.
2. Click **Cancel appointment**.
3. Click **Confirm Cancellation**.
4. Look for **Appointment Cancelled** on the page and a cancellation email.

Moved your appointment before? The **Your Icon Studio Appointment Has Moved** email has a **Cancel this appointment** link that does the same. The link in your first email still works too.

**From your account (if you were signed in when you booked)**

1. Sign in with **Sign In** at the top of the page.
2. Open the account menu and click **My Appointments**.
3. Find the appointment under **Upcoming Appointments**.
4. Click **Cancel**.
5. Click **OK** when your browser asks **Cancel this appointment? This cannot be undone.** Choosing **Cancel** in that box keeps your appointment.
6. Check that the appointment has moved to **Past Appointments**. No other message appears.

**With Iris (if you are signed in)**

1. Click **Ask Iris** at the bottom right of the page.
2. Tap **My appointments**.
3. Tap **Cancel** on the appointment. Iris cancels it straight away, without asking again.
4. Look for **That's cancelled, and a confirmation is on its way to your email.**

**Good to know**

- Cancelling cannot be undone. To change the time instead, see KB-03.
- The salon charges no cancellation fee, even within 24 hours of your appointment. The website never takes payment or card details.
- Please cancel as early as you can. If it is less than 24 hours before your appointment, a quick call to (718) 255-6940 helps the salon fill the slot.
- **Already Cancelled** means the appointment was cancelled before. Nothing else is needed.
- Lost the email? If you were signed in when you booked, use **Resend Email** on **My Appointments** (see KB-07). If you booked as a guest, contact us and we will cancel it for you. The reminder email has no cancel link.

**If it still does not work**

Raise a **Reschedule or cancel** request with your name, phone number and the date and time of the appointment. Or call (718) 255-6940.

#### Live check (remove before publishing)

- [x] Owner: no cancellation fee (confirmed October 7, 2026). The **Good to know** list now says so. The booking form still warns of a possible late fee (second code check, item 11), so expect a few customers to ask until engineering changes that wording
- [ ] Cancel a test booking through the email link: **Confirm Cancellation**, then **Appointment Cancelled**, then the cancellation email arrives
- [ ] Open the same link again and see **Already Cancelled**
- [ ] Profile cancel on an iPhone and an Android phone: the pop-up is the browser's own, so its button names may differ from **OK** and **Cancel**. After OK, the row moves to **Past Appointments**
- [ ] Iris cancel: one tap cancels, and the reply matches step 4. If engineering adds a confirm step (second code check, item 7), rewrite the Iris steps

---

### KB-05. Using the chat assistant (Iris)

**Who this is for:** anyone who wants to book or get answers in a chat instead of the forms.

Iris is the salon's AI assistant. It can book you in, show, move and cancel your appointments (when you are signed in), show prices and current offers, give the hours and location, and pass a message to the salon.

**Steps**

1. Click **Ask Iris** at the bottom right of any page.
2. Tap a button, such as **Book an appointment**, **My appointments**, **Prices**, **Current offers** or **Hours & location**, or type your question.
3. To book, follow Iris's questions, fill in **Your details** and tap **Review booking**. Nothing is booked yet.
4. Check the details and tap **Confirm booking**.
5. Look for **You're booked in.** and the confirmation email.

**Good to know**

- Iris books or moves an appointment only when you tap a confirm button. Tapping **Cancel** on an appointment in Iris cancels it straight away.
- A confirm card lasts 10 minutes. If you see **That confirmation has expired or was already used**, nothing was booked twice: start again and pick your time.
- Sign in first to see or change your appointments in Iris.
- **Current offers** lists the promotions the salon is running now. The free eyebrow threading offer is on the booking page and may not appear here.
- **Start over** takes you back to the main buttons. It also clears a booking you have not confirmed yet.
- **Call (718) 255-6940** rings the salon.

**If it still does not work**

Raise a **Chat assistant (Iris) question** request. Tell us what you typed or tapped, what Iris replied, and roughly when. A screenshot helps.

#### Live check (remove before publishing)

- [x] **Ask Iris** shows on the live site (confirmed October 7, 2026). Still glance that it sits at the bottom right, as step 1 says
- [ ] Book a test appointment through Iris (tell the owner, cancel after): **Review booking**, **Confirm booking**, **You're booked in.** and the confirmation email
- [ ] What **Current offers** shows today. With no promotions, the database may hold a placeholder card titled "No current offers", or Iris says "There aren't any offers running at the moment."
- [x] Typing works on the live site, with its safeguards in place (confirmed October 7, 2026)

---

### KB-06. Iris didn't understand me, or won't let me type

**Who this is for:** anyone whose chat with Iris went in circles, or who sees **Typed messages are unavailable right now — the buttons above still work.**

**Why it happens:** typed questions use AI. Iris turns typing off when the AI is switched off, when the site has had a lot of typed messages that day, or when messages come in very fast. The buttons keep working, and they cover booking, appointments, prices, offers and hours.

**Steps**

1. Tap **Start over** to see the main buttons.
2. Tap the button for what you need: **Book an appointment**, **My appointments**, **Prices**, **Current offers** or **Hours & location**.
3. Keep tapping the buttons until you finish.
4. For anything the buttons do not cover, tap **Message the salon** if Iris offers it, or call (718) 255-6940.

**Good to know**

- If Iris says **Sorry, I didn't quite catch that.**, try a shorter question, such as "move my appointment" or "price of a facial", or tap a button.
- Typed messages can be up to 500 characters.
- Sent several messages quickly and saw **We've hit the limit for messages for now — sorry about that.**? Tap any button to carry on.
- No buttons at all, or **This conversation has ended. Please call the salon on (718) 255-6940.**? Open the site in a new tab to start a fresh chat, or call.
- You can always book on the website without Iris. See KB-01.

**If it still does not work**

Raise a **Chat assistant (Iris) question** request with what you asked and roughly when.

#### Live check (remove before publishing)

- [x] Typing is on, with its safeguards in place (confirmed October 7, 2026), so KB-05's "or type your question" stands
- [ ] The unavailable message reads exactly as in "Who this is for", with the dash
- [ ] A new tab starts a fresh chat with the main buttons
- [ ] Optional: send 6 typed messages within a minute, see the limit message, then tap a button and check typing comes back

---

### KB-07. I did not get a confirmation email

**Who this is for:** anyone who booked and has no email yet.

**Steps**

1. Wait a few minutes. Emails usually arrive quickly but can be delayed.
2. Search your inbox, spam, junk and promotions folders for **Your Icon Studio Appointment is Confirmed!** from Icon Studio (noreply@iconht.studio).
3. If you were signed in when you booked, open **My Appointments** to see your booking.
4. Click **Resend Email** on the appointment. The button changes to **Sent ✓**.
5. Still nothing after 5 minutes? Contact us (below).

**Good to know**

- Your booking is confirmed once you saw **Booking Confirmed!**. The email is a copy of the details and holds your cancel link.
- **Resend Email** works once every 5 minutes per appointment, and only a few times an hour from the same device. If a pop-up says **Please wait a few minutes before resending again.**, wait and try later.
- Booked as a guest? Your booking is not under **My Appointments**, even if you create an account later. Contact us (below).
- A reminder email, **Reminder: Your Icon Studio Appointment is Tomorrow**, goes out the morning of the day before your appointment. A booking made for today, or for tomorrow after that morning's reminders went out, gets no reminder.
- The salon does not send text messages.
- Think you typed your email wrong? Contact us with the right one.

**If it still does not work**

Raise a **Confirmation email not received** request with your name, phone number, the date and time you booked, your booking reference if you have it, and the email address you meant to use.

#### Live check (remove before publishing)

- [x] Customers receive their own emails, not redirected to the owner (verified October 7, 2026)
- [ ] The sender in step 2 is right. The code defaults to `Icon Studio <noreply@iconht.studio>`, but the site settings can change it
- [ ] Test booking emails reach a Gmail and an Outlook inbox, not spam. Note how long they take, and change step 1 if "a few minutes" is wrong
- [ ] **Resend Email** on a signed-in test booking: the button shows **Sent ✓**, a second email arrives, and a second click within 5 minutes (after reloading the page) shows the pop-up
- [ ] Reminder timing: the Vercel cron log shows when reminders really run. The schedule is 13:00 UTC, which is 9 AM New York time now and 8 AM after November 1, but on the Hobby plan a cron can fire any time in that hour
- [ ] The Resend dashboard: the free plan sends 100 emails a day, and the site only logs a `[quota]` warning in Vercel as it gets close. Check recent days stayed under it, and look for bounces

---

### KB-08. What are the salon's hours and where is it?

**Who this is for:** anyone planning a visit.

**Icon Studio**, 39-46 Queens Blvd, Sunnyside, NY 11104

| Day | Hours |
|---|---|
| Monday to Saturday | 10:00 AM to 7:30 PM |
| Sunday | 10:00 AM to 6:00 PM |

**Steps to find it on the site**

1. Click **Location & Hours** at the bottom of any page, or **Location** at the top.
2. Click the address to open it in Google Maps.

You can also tap **Hours & location** in Iris.

**Good to know**

- The salon is open 7 days a week. Walk-ins are welcome.
- Online, a service has to finish by closing time, so the last time you can book depends on how long the service takes. For a later start, call (718) 255-6940.

**If it still does not work**

For anything else about getting here, raise a **General question** request or call (718) 255-6940.

#### Live check (remove before publishing)

- [x] Owner confirmed closing at 7:30 PM Monday to Saturday and 6:00 PM on Sunday (October 7, 2026), matching the table. The home page's "Every day, 10am to 8pm" is wrong (second code check, item 1). The 10:00 AM opening comes from the code; she did not contradict it
- [x] Owner confirmed walk-ins are welcome (October 7, 2026)
- [ ] The address link on the Location page opens the right pin in Google Maps

---

### KB-09. How do I contact the salon?

**Who this is for:** anyone with a question the help articles do not answer.

**Ways to reach us**

- **Phone:** (718) 255-6940. Best for anything about today.
- **Email:** ks@iconht.studio, also shown at the bottom of every page.
- **Contact form:** iconht.studio/contact. Replies come by email.
- **Iris:** ask Iris to pass on a message, or tap **Message the salon** when Iris offers it. Fill in the short form and tap **Send message**. Iris replies **Sent. The salon will come back to you by email.**
- **This help center:** raise a request and track it here.

**Steps for the contact form**

1. Go to iconht.studio/contact.
2. Enter your name and email.
3. Write your message (10 to 1,000 characters).
4. Click **Send Message**.
5. Look for **Message Sent!**. The salon replies to the email you entered.

**Good to know**

- The form takes up to 3 messages an hour. If you see **Too many requests. Please try again later.**, your message is still in the box: wait a little and press **Send Message** again, or call.
- If you see **Sorry, we could not send your message**, please call (718) 255-6940.
- If Iris says **I couldn't send that just now**, use the contact form or call.

**If it still does not work**

Raise a **General question** request, or call (718) 255-6940.

#### Live check (remove before publishing)

- [x] Owner is happy to list ks@iconht.studio here (confirmed October 7, 2026)
- [ ] Send a test contact form message: **Message Sent!** shows, it reaches the owner's inbox, and replying goes to the address you typed
- [ ] Send a test message through Iris and confirm it arrives. Iris may share one limit of 3 messages an hour across all its users (second code check, item 5); if a second device fails soon after, keep the **I couldn't send that just now** line
- [ ] With typing off, how a customer reaches **Message the salon** (it only appears after Iris cannot help). If it is hard to find, point customers to the contact form instead

---

### KB-10. Internal: adding a service or a promotion

**Who this is for:** the salon owner and support agents. Internal only: do not publish to customers.

**Add a service**

1. Click **Owner Login** at the bottom of the site, or go to iconht.studio/admin/login.
2. Sign in.
3. Open the **Services** tab.
4. Click **Add Service**.
5. Pick the **Category**. It starts on **Threading Services**, so change it for any other kind of service.
6. Enter the **Name**.
7. Fill in **Description (optional)** if you want one.
8. Enter the **Price ($)**. For a range, also fill in **Max Price (optional)**.
9. Enter the **Duration (minutes)**.
10. Click **Save Service**.

**Important: a new service cannot be booked online yet.** It appears on the menu, but admin has no way to link a service to a stylist. Until engineering links it, customers who pick it see **We can't book [service] online right now. Please call us**, and Iris says **[service] isn't bookable through me at the moment.** After saving a new service, send engineering the service name and which stylist offers it.

- A price of 0 with no max price shows as **Price on consultation** on the website, and as **Consultation** in Iris and in the admin list.
- Changes in admin send customers no email.

**Add a promotion**

1. Open the **Promotions** tab.
2. Click **Add Promotion**.
3. Enter the **Title**.
4. Enter the **Offer text — shown to customers exactly as typed** (up to 200 characters).
5. Fill in **Details (optional)** if you want.
6. Set **Starts (optional — defaults to today)**.
7. Set **Ends (optional — blank runs until you hide it)**.
8. Click **Save Promotion**.
9. If the list still shows a **No current offers** placeholder, click **Hide** on it so customers see only the real offer.

**Important: promotions show only in Iris,** under **Current offers**. No website page shows them, even though the Promotions screen says offers appear "on the site". The free eyebrow threading banner on the booking page is fixed in the site's code: ask engineering to change or remove it.

- Adding a promotion in the evening (after 8 PM in summer time, 7 PM in winter)? Pick today's date in **Starts** instead of leaving it blank. A blank start saves as tomorrow at that hour, and the promotion shows **Scheduled** until midnight.

**If it still does not work**

Send support the service or promotion name and what you expected to see.

#### Live check (remove before publishing)

Only with the owner's login, or ask her to do it. Do not add a test service: it appears on the live menu straight away.

- [ ] **Owner Login** in the footer opens iconht.studio/admin/login, and the tabs match
- [ ] The **Add Service** and **Add Promotion** forms show the labels above
- [ ] Whether a **No current offers** placeholder is in the Promotions list today
- [ ] With the owner: add a real promotion, check it appears under **Current offers** in Iris, and check it does not appear on any website page
