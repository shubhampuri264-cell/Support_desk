# Help center articles

Drafts of every help article before it goes into the JSM knowledge base. Articles describe only features confirmed on the live site.

## Feature check (issue #5)

Checked against the Salon website code on October 6, 2026. Every item still needs a check on the live site, because the deployed version or the owner's settings in the admin page can differ from the code.

### What the site does

| Feature | How it works |
|---|---|
| Booking | Four steps: service, stylist, date and time, your details. The stylist step is skipped when only one stylist offers the service. There is no "anyone available" option. Guests can book; signed-in customers have the booking linked to their account |
| Required details | Full name, email, phone (digits, spaces, `-`, `+`, `()`), and a ticked cancellation policy box. Notes and the marketing opt-in are optional |
| Availability | Start times every 30 minutes from opening. The whole service must end by closing time. Bookable up to 180 days ahead, with no minimum notice. A time is taken only if it overlaps another booking or a slot the owner blocked |
| Confirmation | The page shows "Booking Confirmed!" with the date, time and an 8 character booking reference. A confirmation email follows. Bookings are confirmed immediately |
| Cancelling | The cancel link in the confirmation email (with a "Confirm Cancellation" click), the profile page for signed-in customers, or Iris. No cutoff is enforced. The booking form says cancelling under 24 hours ahead "may be subject to a late cancellation fee", but nothing charges it |
| Rescheduling | Signed-in customers: through Iris, to a new date and time with the same service and stylist. Guests: through the link in the confirmation email. In the code, that link is "Cancel appointment", and the cancellation email then offers "Book a new appointment", so a guest moves a booking in two steps. The live-site check confirms whether the deployed site does it in one step. The profile page has no reschedule button |
| Iris chat assistant | Books, shows "My appointments", cancels, reschedules, and shows prices, service details, offers, hours and location. It can also pass a message to the salon. Bookings and changes only happen when the customer taps a confirm button, and a confirm card expires after 10 minutes |
| Iris buttons | Book an appointment, My appointments, Prices, Current offers, Hours & location, Start over, and a Call button. When typed messages are unavailable, the message box reads "Typed messages are unavailable right now, the buttons above still work" |
| Emails | Booking confirmation, cancellation, "Your Appointment Has Moved" after a reschedule, a reminder the day before, a review request the day after (only if the owner set a review link), contact form copies and password resets |
| Text messages | **None.** The code has unused settings for a text provider, but sends no texts |
| Customer accounts | Sign up, sign in, password reset, and a profile page listing appointments with Cancel and "Resend Email" (once per 5 minutes per appointment) |
| Contact form | Name, email and a message of 10 to 1,000 characters. It goes to the owner's inbox with reply-to set to the customer. Limited to 3 messages an hour per visitor. On failure it asks the customer to call |
| Hours | Monday to Saturday 10:00 AM to 7:30 PM, Sunday 10:00 AM to 6:00 PM, open every day |
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

### Article list after the check

1. How do I book an appointment?
2. How do I choose a service and stylist?
3. How do I reschedule my appointment? (signed in: Iris; guest: the link in the confirmation email)
4. How do I cancel my appointment? (email link, profile, Iris; the 24 hour note)
5. Using the chat assistant (Iris)
6. Iris says typed messages are unavailable (use the buttons)
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
6. A visitor in a time zone ahead of New York gets an appointment on the wrong day.
7. Iris says there are no offers while the booking page shows the threading offer.
8. A long "Message the salon" sent through Iris fails.
9. The Iris confirm card expired ("That confirmation has expired").
10. A page left open shows times for a retired service, then fails with "Something went wrong".
11. A customer asks why they did not get a text.

## Articles

Drafts go here (issue #6).
