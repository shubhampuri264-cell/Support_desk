# Salon Support Desk: Project PRD

**Owner:** Shubham Puri  
**Written:** October 6, 2026  
**Status:** Final, ready to build  
**Time:** about 49 hours in total: about 25 hours for the help desk (Phases 0 to 5), about 20 hours for the PayPal refund desk (Phase 3B), and about 4 hours for the hackathon submission (section 12). Phase 3B is your **PayPal AI Hackathon entry, due Thursday November 12, 2026, 3:00 PM New York time**.

A real help desk for your live Salon Booking Platform, built on Jira Service Management, with a help center, an AI triage helper and a response time dashboard. Alongside it, Phase 3B builds an AI refund desk on PayPal for small businesses, shown on a made-up business, as your hackathon entry.

(A sales demo video was planned as Part 2 and dropped on October 6, 2026. The existing YouTube demo of the Salon site already covers it.)

---

## 1. Why this project

Your new non SWE resume is strong on customer contact but has one hole. Support, TAM and implementation job postings keep naming a help desk tool (Zendesk, Jira, ServiceNow) plus SQL, APIs and written documentation. Right now you cannot honestly name any help desk tool. This project fixes that with real use, and it reuses the Salon platform you already built, so the story connects:

> "I built the booking platform for a real salon, then set up the help desk behind it, wrote the help articles, built a tool that sorts incoming tickets, and tracked how fast tickets got answered."

That sentence covers the whole support job: intake, triage, answering, documentation, metrics, and feeding problems back to engineering.

Phase 3B adds payments, but not for the salon: it takes no online payments, and the owner wants to keep it that way. So Phase 3B is a separate AI refund desk for small businesses that take PayPal, shown on a made-up business. When a customer writes "I was charged twice", it finds the payment in PayPal, works out what happened, and drafts the refund for the owner to approve. That is your PayPal AI Hackathon entry, and it ties to real refund handling you did at McDonald's.

## 2. What you will be able to say when it is done

**On the resume right now (added October 6, 2026, before the build started):** "Salon Support Desk" on the non SWE base, with three present tense bullets ("Setting up...", "Building...", "Tracking...") and no numbers. Present tense is what keeps it honest while you build, so do not change it to past tense until a phase is done. If a recruiter asks, describe exactly what is built so far. As each phase finishes, send Claude the result and the bullets move to the finished versions below. ("Jira" is already on the SKILLS line from your Mouse Squad help desk work.)

Only claim what you actually finish. Fill every bracket with your real number.

**New skills you can list honestly once you have used them:** Jira Service Management (the product; plain "Jira" is already on your resume), ticketing, SLAs, knowledge base, REST APIs, SQL, Streamlit. Add Confluence only if you end up working in Confluence directly.

**Resume entry (Projects section, non SWE base):**

**Salon Support Desk (Help Desk Project)**, right column: `Jira Service Management, Python, SQL, REST API, Claude API`

- Set up the help desk behind a live salon booking app in Jira Service Management, with [N] request types, response time goals, and [N] help articles
- Built a Python triage tool that reads new tickets through the Jira API and tags category and priority with an LLM, matching hand labels on [X] of [40] sample tickets
- Tracked first response and resolution times in SQL and a dashboard, then turned the top repeat issue into a new help article

**Hackathons section entry (after you submit):**

**PayPal AI Hackathon**, right column: `November 2026 | Solo`

- Built an AI refund desk for small businesses that take PayPal: it finds the customer's payment, checks it against the refund policy, and drafts the refund for owner approval, matching [X] of [15] sample cases

Write "Winner" or "Finalist" only if it is true. Add "PayPal REST API" and "Postman" to SKILLS once you have used them.

**Honesty rule.** Until Phase 6 (go live) is done, the tickets are sample tickets you wrote. Say "sample tickets" on the resume and in interviews. After Phase 6, real customer questions flow in and you can say so.

## 3. Scope

**In scope**

1. A Jira Service Management (JSM) project for the salon with a customer portal, request types, queues and response time goals.
2. A help center with at least 10 articles about features the Salon app really has.
3. 40 sample tickets, each labeled by you first, loaded through the API.
4. You working those tickets as the agent: replying, linking articles, resolving.
5. A Python triage tool that labels new tickets with an LLM and leaves an internal note. It never replies to a customer on its own.
6. An export script that copies ticket data into SQLite, SQL queries for support metrics, and a small Streamlit dashboard.
7. A weekly support report written from the data.
8. README with screenshots and a 3 minute walkthrough video.
9. Optional Phase 6: send the live Salon contact form into JSM.
10. Phase 3B: an AI refund desk on the PayPal sandbox for a made-up small business, with a customer request form, an owner review page with human approval, a hosted demo judges can open without any keys of their own (plus local setup as a backup), and the hackathon submission.

**Out of scope**

- Building your own ticketing system. The point is to use the tool employers use.
- Auto replying to customers with AI. Every customer facing reply is written or approved by you.
- Paid plans or paid add ons.
- Real money. PayPal work runs only in the sandbox, where money is fake.
- Payments for the real salon. It takes no online payments, and the owner does not want to add them.
- Refunds without a human. The AI proposes, you approve.

## 4. The people involved

| Who | Real or sample | What they do |
|---|---|---|
| Salon customers | Sample at first (Phase 2), real after Phase 6 | Ask about booking, rescheduling, cancelling, the chat assistant and confirmation emails |
| You, the support agent | Real | Answer tickets, link articles, escalate bugs |
| The salon owner | Real | Gets escalations about her business. Must approve Phase 6 and anything shown on video |
| Engineering (also you) | Real | Receives bug escalations as GitHub issues in the SalonWebsite repo |
| Customers of the made-up business (Phase 3B) | Sample only, PayPal sandbox | Complain about double charges, cancellations and wrong amounts |
| Hackathon judges | Real | Open your hosted demo (or run it locally) and watch your video |

## 5. Tools and cost

All free. Free tiers change, so confirm each one when you sign up.

| Tool | Use | Free tier (checked Oct 2026) |
|---|---|---|
| Jira Service Management Cloud, Free plan (now sold as part of "Service Collection") | Help desk, portal, queues, request types | Free forever for 3 agents, customer portal, email, chat and widget channels, queues, embedded knowledge base, 1,250 automation steps a month. SLAs on Free are not confirmed; check Project settings |
| JSM knowledge base | Help articles | Built in, powered by Confluence. If it asks you to add Confluence, add the **Free** Confluence plan. Never start a paid trial |
| Python 3.11+ | Scripts | Free |
| Claude API (or Gemini API) | Triage labels and the refund desk | Pennies for 40 tickets on a small model such as Claude Haiku 4.5 (`claude-haiku-4-5-20251001`). Gemini has a free tier if you prefer $0, but Google may use free tier content to improve its products, so send it sample data only, never real customer messages |
| SQLite | Metrics database | Free, no setup |
| Streamlit | Dashboard and the refund desk app | Free |
| PayPal Developer sandbox | Fake payments and refunds (Phase 3B) | Free |
| Postman | Testing API calls before coding them (Phase 3B); hackathon sponsor tool, no prize of its own | Free plan |
| PayPal AI Toolkit (optional) | Ready made PayPal tools for an AI agent through an MCP server: orders, refunds, disputes, transactions (github.com/paypal/AI-Toolkit) | Free, open source |
| AG Grid Community (optional) | Table for the refund review page. Does not target the AG Grid prize, which requires AG Grid Studio (see Phase 3B) | Free, open source |
| Render | Hosting the judges' demo URL (Phase 3B step 11); sponsor prize paid in Render credits | Free tier, plus $50 hackathon credits |

**If the JSM Free plan is gone when you sign up**, use Zammad instead. It is free, open source, runs in Docker, and has a full REST API. Every phase below still applies; only the API calls change.

## 6. Repo layout

The repo already exists at `c:\me files\Coding Projects\salon-support-desk` and is public on GitHub at `github.com/shubhampuri264-cell/Support_desk`, with this PRD, a README, the license, the hackathon rules summary, `.gitignore`, `.env.example` and `requirements.txt`. Build toward this:

```
salon-support-desk/
  PRD.md                 this file
  README.md              what it is, screenshots, how to run, walkthrough video link
  .env.example           names of the secrets (copy to .env, never commit .env)
  requirements.txt
  LICENSE                MIT, added October 6, 2026 (hackathon rule)
  docs/
    hackathon-rules.md   summary of the official hackathon rules and what they mean for this entry
  data/
    tickets_seed.csv     40 sample tickets with your hand labels
    payment_requests.csv 15 sample payment requests with your answer key, keyed by case id (Phase 3B)
    refund_policy.md     the made-up business's refund rules the AI must follow (Phase 3B)
  kb/
    articles.md          drafts of every help article before you paste them into JSM
    index.csv            article id, title, url, category (used by triage)
  src/
    jsm.py               small API client (auth, get, post, paginate)
    seed_tickets.py      Phase 2: creates customers and tickets from a CSV (--csv picks the file)
    triage.py            Phase 3: labels new tickets, writes an internal note
    eval_triage.py       Phase 3: compares bot labels with your hand labels
    paypal.py            Phase 3B: token, look up a payment, refund (sandbox only)
    seed_payments.py     Phase 3B: creates sample bookings, sandbox payments and the sample requests
    refund_helper.py     Phase 3B: reads a request, finds the payment, proposes, refunds after approval
    eval_refunds.py      Phase 3B: compares proposals with your answer key
    review_app.py        Phase 3B: the refund desk app (request form, review page, policy, audit log)
    export.py            Phase 4: pulls tickets, comments, SLAs into SQLite
    dashboard.py         Phase 4: Streamlit dashboard
    weekly_report.py     Phase 5: writes reports/week_YYYY_MM_DD.md
  sql/
    schema.sql
    metrics.sql
  postman/
    paypal_refund_helper.postman_collection.json   no secrets in it
  reports/
  screenshots/
```

## 7. Phases and step by step instructions

Each phase ends with a **Done when** check. Do not move on until it passes.

### Phase 0. Setup (about 2 hours)

1. Go to atlassian.com, choose Jira Service Management, and sign up for the **Free** plan with your own email. Pick a site name such as `spuri-support`. Your site URL becomes `https://spuri-support.atlassian.net`.
2. Create a project from the **General service management** template. Name it `Salon Support`, key `SUP`. Do not use the "Customer service management" template: it now creates a space in Atlassian's separate Customer Service Management app, which has its own API, and the `servicedeskapi` calls in this plan are not confirmed to work there.
3. Set up **request types** (Project settings, Request types). Use these six and give each a one line description customers will see. Delete or hide any default request types the template adds. There is no payment request type, because the salon takes no payments.
   - Booking problem
   - Reschedule or cancel
   - Chat assistant (Iris) question
   - Confirmation email not received (the site sends no text messages)
   - Something is broken (bug report)
   - General question (hours, location, prices and anything else)
4. Set up **queues**: All open, Unassigned, Bugs, Waiting on customer, Breached or close to breaching.
5. Set **response time goals**. Look under Project settings for **SLAs**. If you see it, set:
   - Time to first response: 4 hours
   - Time to resolution: 48 hours  
   If SLAs are not on your plan, skip this. Your Phase 4 script calculates both numbers anyway.
6. **Turn off customer notifications** before seeding (Project settings, Customer notifications), so 40 sample tickets do not send 40 emails. Turn them back on before Phase 6.
7. Create an **API token**: id.atlassian.com, Security, API tokens, Create. Save it once; you cannot view it again. Create it on your own account, which must be the site admin and one of the 3 agents: creating customers needs Jira admin rights, adding them to the desk needs service desk admin rights, and raising tickets on a customer's behalf or reading SLAs needs an agent.
8. In the repo:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   copy .env.example .env
   ```
   Fill `.env` with your site URL, email, API token and LLM key.
9. Write `src/jsm.py` with one function that calls the API with basic auth (email plus token), and test it:
   ```python
   import os, requests
   from dotenv import load_dotenv
   load_dotenv()
   BASE = os.environ["JSM_SITE"]                      # https://spuri-support.atlassian.net
   AUTH = (os.environ["JSM_EMAIL"], os.environ["JSM_API_TOKEN"])

   def get(path, **params):
       r = requests.get(BASE + path, auth=AUTH, params=params,
                        headers={"Accept": "application/json"}, timeout=30)
       r.raise_for_status()
       return r.json()

   if __name__ == "__main__":
       print(get("/rest/servicedeskapi/servicedesk"))  # shows your service desk id
   ```
10. Write down your `serviceDeskId` and each `requestTypeId`:  
    `GET /rest/servicedeskapi/servicedesk/{serviceDeskId}/requesttype`  
    Also write down your own `accountId` from `GET /rest/api/3/myself`. Phase 4 uses it to tell your agent replies apart from customer comments.

**Done when:** `python src/jsm.py` prints your service desk, and you have all six request type ids in `.env` or a config file.

### Phase 1. Help center articles (about 4 hours)

1. **Open the live Salon site and check every feature before you write about it.** Only write about what really exists. The code check on October 6, 2026 (issue #5, written up at the top of `kb/articles.md`) found:
   - booking as a guest or with an account, including choosing a service and stylist and checking availability;
   - cancelling through the email link, the profile page or Iris;
   - rescheduling: signed-in customers through Iris, guests through the link in their confirmation email;
   - the Iris chat assistant: it books, reschedules, cancels, and answers questions about services and hours, with a tap-through menu that works even when the AI is off;
   - confirmation, reminder and cancellation emails;
   - customer accounts and a contact form;
   - an admin side for the owner (appointments, services, promotions, blocked slots).

   The site sends **no text messages** and takes **no payments**.
2. Draft 10 articles in `kb/articles.md` with this shape:
   - **Title** as the customer would search it ("How do I reschedule my appointment?")
   - **Who this is for**
   - **Steps** (numbered, one action each)
   - **If it still does not work** (what to send support, which request type to use)
3. Suggested 10 (adjust to what you confirm in step 1):
   1. How to book an appointment
   2. How to choose a stylist and service
   3. How to reschedule an appointment (signed in: through Iris; guests: the link in the confirmation email)
   4. How to cancel an appointment
   5. Using the chat assistant (Iris)
   6. The chat assistant did not understand me (use the tap through menu)
   7. I did not get a confirmation email
   8. Finding the salon's hours and location
   9. How to contact the salon
   10. Internal, owner only: adding a service or a promotion in the admin page
4. Paste them into the JSM knowledge base (Project, Knowledge base, Create article). If it asks you to add Confluence, choose the Free plan.
5. Fill `kb/index.csv`: `article_id,title,url,category`.

**Done when:** a customer can search "reschedule" in your portal and find the right article.

### Phase 2. Sample tickets and working them as the agent (about 4 hours, spread over a few days)

1. Write 40 realistic tickets in `data/tickets_seed.csv`:
   ```
   id,customer_name,customer_email,request_type,summary,description,expected_category,expected_priority
   1,Maria Lopez,maria.lopez@example.com,Reschedule or cancel,Need to move Saturday appointment,"I booked a haircut for Saturday at 2 but something came up. Can I move it to Sunday?",reschedule,low
   ```
   - Use `@example.com` addresses. That domain is reserved for testing, so no real person gets mail.
   - Mix it like real life: about 12 reschedule or cancel, 8 booking problems, 6 Iris questions, 6 missing confirmations, 4 bugs, 4 general questions. Make some angry, some vague, and some that need a follow up question.
   - `request_type` must match one of the six request type names in JSM exactly. File 3 or 4 tickets under the wrong request type on purpose, as real customers do; `expected_category` still records the true category.
   - **Fill `expected_category` and `expected_priority` yourself before you build the triage tool.** These are your answer key for Phase 3.
2. Write `src/seed_tickets.py`:
   - Take the CSV path as an argument (`--csv`, default `data/tickets_seed.csv`) and read only the columns it needs (`customer_name`, `customer_email`, `request_type`, `summary`, `description`).
   - Create each customer: `POST /rest/servicedeskapi/customer` with `{"email": ..., "displayName": ...}`. It returns an `accountId`.
   - If the next step says the customer has no access, add them to the desk: `POST /rest/servicedeskapi/servicedesk/{id}/customer` with `{"accountIds": [...]}`.
   - Create the ticket as that customer:
     ```json
     POST /rest/servicedeskapi/request
     {
       "serviceDeskId": "1",
       "requestTypeId": "10",
       "requestFieldValues": {"summary": "...", "description": "..."},
       "raiseOnBehalfOf": "<customer accountId>"
     }
     ```
   - Save the returned issue key (for example `SUP-12`) next to the CSV id.
   - Load in 4 batches of 10 on different days, so the response times measure how you actually worked through them, instead of 40 tickets created in the same minute.
3. **Work every ticket as the agent in the JSM web UI.** Reply publicly, ask a follow up where the ticket is vague, link the right article, and resolve. For bug tickets, open a GitHub issue in the SalonWebsite repo and link it in an internal note. This is the actual support work and where your interview stories come from.
4. Keep a short log in `reports/agent_notes.md` of anything surprising, such as a missing article or a confusing feature.

**Done when:** all 40 tickets are resolved, at least 20 replies link an article, and every bug ticket links a GitHub issue.

### Phase 3. AI triage helper (about 6 hours)

Goal: when a ticket arrives, the tool suggests a category and priority, spots an upset customer, suggests the best help article, and writes all of that as an **internal note**. It never sends anything to the customer.

1. **Find new tickets** with the Jira search API. The old `/rest/api/3/search` endpoint is removed; use the new one, which pages with a token:
   ```
   GET /rest/api/3/search/jql?jql=project = SUP AND labels is EMPTY AND statusCategory != Done ORDER BY created ASC
       &fields=summary,description,created,priority,labels&maxResults=50
   ```
   Repeat with `nextPageToken` until the response says `isLast: true`. The `statusCategory != Done` part keeps the tool off the Phase 2 tickets you already resolved by hand, so it only touches tickets that are still open, as it would in real life.
   - Always pass `fields`: without it, this endpoint returns only issue ids.
   - Always keep `project = SUP` in the JQL: the endpoint rejects searches that are not limited to a project or similar.
   - A ticket created a few seconds ago may not show up yet. That is normal; the next run picks it up.
2. **Ask the LLM for JSON only**, with a fixed list of allowed values:
   ```
   category: booking | reschedule | iris | confirmation | bug | general
   priority: low | medium | high
   sentiment: calm | frustrated | angry
   article_id: one id from kb/index.csv, or "none"
   confidence: 0 to 1
   ```
   Put the article list (id plus title) in the prompt so the model can only pick a real one.
3. **Validate before writing anything.** Check the reply against the allowed values (pydantic works). If it is invalid, or confidence is below 0.6, label the ticket `needs-human` and stop. This is the same idea as the zod check in your Salon assistant.
4. **Write the result back:**
   - Labels: `PUT /rest/api/3/issue/{key}` with `{"update": {"labels": [{"add": "cat-reschedule"}, {"add": "triaged"}]}}`
   - Priority: same call with `{"fields": {"priority": {"name": "High"}}}` (match your site's priority names). If Jira replies that the field cannot be set, add Priority to the project's issue screen in Project settings and try again.
   - Internal note: `POST /rest/servicedeskapi/request/{key}/comment` with `{"body": "...", "public": false}`. `public: false` is what keeps it internal. **Test this on one ticket and confirm in the UI that the customer cannot see it before running it on more.**
5. **Run it on a schedule** with polling: Windows Task Scheduler every 10 minutes, or just run it by hand. Webhooks need a public URL, so skip them for now.
6. **Measure it honestly** with `src/eval_triage.py`: run the classifier on the 40 seed tickets without writing to JSM, compare with your hand labels, and print category accuracy, priority accuracy, and a confusion table. **This gives you the "[X] of 40" number for the resume.** Never tune the prompt on a ticket and then count that ticket in the score. If you tune, hold out 10 tickets you never look at and report the score on those too.

**Done when:** a new ticket gets labels plus an internal note within one run, invalid model output is caught, and `eval_triage.py` prints a real accuracy number.

### Phase 3B. AI refund desk on PayPal, your PayPal AI Hackathon entry (about 20 hours, Oct 19 to Nov 8)

**Hackathon facts (official page and rules, read October 6, 2026).** The full breakdown, with sources, is in `docs/hackathon-rules.md`.

- **Deadline:** Thursday November 12, 2026, 3:00 PM New York time (12:00 PM Pacific). Submit by November 10. Drafts can be edited until the deadline; nothing can change after it.
- **Solo is fine.** Existing projects count if you make meaningful progress during the hackathon (October 1 to November 12). This repo started October 6, so all of it counts. Say so in the submission.
- **Must use:** at least one PayPal API or product in the free sandbox, plus any AI tool or model. PayPal has to be central, not decoration. Stage one of judging is pass/fail on exactly this.
- **Must submit:** a text description, a working demo judges can run themselves (setup instructions in the repo or a hosted URL; mockups do not count), a list of the tools used and how, a public open source repo with the license detected and shown at the top of the repo page, and a public YouTube video **under 3 minutes** with no copyrighted music or third-party trademarks.
- **Free testing access until December 15.** The project must be available to judges "free of charge and without any restriction" until judging ends. Judges therefore cannot be required to bring their own paid AI key, which is why step 11 hosts the demo with our own keys.
- **Judging, equally weighted:** technological implementation, design (a complete product experience, not just a proof of concept), potential impact (a real problem for a real audience), innovation, and presentation (the video: problem, who it is for, why it matters).
- **Prize groups:** Grand ($12,000 / $8,000 / $5,000), Honorable Mention ($5,000 each: Most Creative, Most Impactful, Best Demo Delivery, Best Use of PayPal + AI, Best Use of Agentic Commerce), and Sponsor prizes. **A project can win at most one Grand Prize and one Sponsor Prize, or one Honorable Mention and one Sponsor Prize.**
- **Our prize targets:** one Honorable Mention (Best Use of PayPal + AI, or Best Demo Delivery) plus the Render sponsor prize, which our hosted demo enters at no extra cost. A Grand Prize is the stretch goal.
- **Skip the AG Grid prize.** It is judged on AG Grid Studio (a React boilerplate with a 45 day trial license and the Studio Agent Framework), and judges want custom widgets and theming, "not just AG Grid or AG Charts on their own." That is a separate project. The Render prize is paid in credits only ($1,000 / $750 / $500). Postman has no prize.
- **AI coding assistants:** the rules do not mention them. The submission must be your original work, and prizes are paid only after PayPal verifies your role in building it. Make the design decisions yourself, be able to explain every part, and list every tool honestly in the submission.
- **8,070 people had registered** by October 6. The page does not say how many submitted, and registrations usually far outnumber finished entries.

**Plan B: a made-up business, not the salon (decided October 7, 2026).** The salon takes no online payments, and the owner does not want to add them. So Phase 3B is its own small product, an AI refund desk for small businesses that take PayPal, shown on a made-up appointment business (for example a day spa) with sample customers and sandbox payments.

- The salon's name, staff, prices and help desk never appear in the demo, the video or the sample data. That also keeps the video clear of third-party trademarks.
- Say plainly in the app, the README and the video that the business and its customers are sample data.
- Pick a name for the business that no real business uses (search it first).
- Phase 3B does not use Jira. Requests arrive through the app, and the owner works them on the app's review page. The help desk work from Phases 0 to 3 is the background story, not part of the demo.

**What it does, in one sentence for the judges.** When a customer of a small business writes in about a payment ("I was charged twice", "I cancelled, where is my refund?"), the refund desk finds the payment in PayPal, checks what happened against the business's refund policy, and drafts the exact refund and reply for the owner, who approves it with one click. No money moves without a human.

**Why the pitch works.** Small service businesses handle payment complaints by hand. It is slow, a wrong refund costs money, and a slow one costs the customer. The audience is real and specific: small appointment businesses that take PayPal, and the person at the front desk handling refunds, a job you have done.

**How a request flows.**

1. A customer submits a request on the app's form, or it is one of the 15 sample requests.
2. AI step 1 reads the claim.
3. Code finds the customer's bookings and payments, and confirms each payment live in PayPal.
4. AI step 2 proposes an action, an amount and a draft reply.
5. Code guardrails check the proposal. A failed check blocks it and records which check failed.
6. The owner sees the proposal on the review page and clicks Approve or Reject.
7. On Approve, the guardrails run again and the refund is issued in the PayPal sandbox. The page shows the refund id and the draft reply for the owner to send.
8. Every step is written to an audit log.

#### Steps

1. **PayPal developer setup (30 minutes).**
   - Go to developer.paypal.com and log in or sign up. Open **Apps & Credentials**, keep the toggle on **Sandbox**, and click **Create App**.
   - Copy the Client ID and Secret into `.env` as `PAYPAL_CLIENT_ID` and `PAYPAL_CLIENT_SECRET`, and set `PAYPAL_BASE=https://api-m.sandbox.paypal.com`.
   - Under **Sandbox accounts** you get a test business account (the made-up business) and a test personal account (a customer). Sandbox money is fake.
   - Walkthrough with screenshots: PayPal's [getting started with the sandbox](https://github.com/paypaldev/getting-started-with-paypal-sandbox) guide. Two sites, two logins: developer.paypal.com takes your real PayPal login, and www.sandbox.paypal.com takes only the generated sandbox account logins (needed for the approve-link fallback in step 4).
   - Check that both sandbox accounts are US accounts (Testing Tools, Sandbox Accounts). If not, create new ones with country United States: one-step card payments (step 4, easy path) work in only 37 sandbox countries, according to another entrant in the hackathon Discord.
2. **Try every call in Postman before coding it (1 hour).** Postman is a hackathon sponsor tool (it has no prize of its own) and fills a gap on your resume.
   - Create a Postman environment with `client_id`, `client_secret` and `base_url` as variables, so no secret ever sits inside the collection.
   - Build five requests: get a token (`POST /v1/oauth2/token`, basic auth with id and secret, body `grant_type=client_credentials`), create an order, capture it, look up the capture, and refund it.
   - Export the collection to `postman/paypal_refund_helper.postman_collection.json` and commit it.
3. **Write `src/paypal.py` (1 hour).** Functions: `token()`, `create_and_capture(...)`, `get_capture(capture_id)`, `refund(capture_id, amount=None, request_id=...)`. At the top, **refuse to run unless `PAYPAL_BASE` contains `sandbox`.** Cache the token until it expires.
4. **Seed sample bookings and payments (2 hours), `src/seed_payments.py`.**
   - Make about 15 sample customers with `@example.com` addresses, each with a booking and a payment for one of the made-up business's services, at made-up prices.
   - **Easy path:** create each order with intent `CAPTURE` and a card `payment_source`, using a test card number from PayPal's card testing page (developer.paypal.com, Sandbox, Card testing). It completes in one step with no clicks: the response has `status: COMPLETED` and the capture id is in `purchase_units[0].payments.captures[0]`. This needs card payments enabled on the sandbox app (Apps & Credentials, your app, Features, Accept payments; usually on by default), and PayPal rejects this one-step call if the `PayPal-Request-Id` header is missing.
   - **Fallback**, if your sandbox app will not take cards: create the order, open its `approve` link, log in with the sandbox personal account, approve, then call `POST /v2/checkout/orders/{id}/capture`.
   - Build these 15 cases on purpose, each with a fixed `case_id`:

     | Case ids | Count | What happened | Expected action |
     |---|---|---|---|
     | `dup-1` to `dup-4` | 4 | Duplicate charge: same customer, same amount, minutes apart | `refund_full` of the second charge |
     | `cancel-1` to `cancel-3` | 3 | Cancelled 24 or more hours before the appointment | `refund_full` |
     | `wrong-1` to `wrong-3` | 3 | Charged for a longer service than was booked | `refund_partial`, the difference |
     | `refunded-1`, `refunded-2` | 2 | Already refunded (the script refunds them) | `no_refund` |
     | `noshow-1` | 1 | No-show, outside the policy | `no_refund` |
     | `other-1` | 1 | Asks for a refund of a payment made under a different email | `no_refund` |
     | `vague-1` | 1 | Customer with several payments says "I think I was overcharged", with no date or amount | `ask_customer` |

   - Save everything in SQLite. These tables stand in for the business's own booking system, which would store the PayPal ids:
     ```
     bookings(booking_id, case_id, customer_email, service, booked_price, appointment_at, status, cancelled_at)
     payments(case_id, booking_id, customer_email, order_id, capture_id, amount, created_at, is_refund_target)
     ```
     `status` is one of `booked`, `completed`, `cancelled`, `no_show`. `is_refund_target` marks the one capture the answer key expects to be refunded (for a duplicate, the second charge). Because every sandbox creates different capture ids, the answer key points at cases, not capture ids.
   - Send a `PayPal-Request-Id` on every create call, built as `seed-<run_id>-<case_id>-<n>`. `run_id` is saved in the database when a seeding run starts, so rerunning a crashed run reuses the same ids and can never charge twice. `n` numbers the charges inside a case, so both charges of a duplicate case go through. The Reset demo button (step 11) starts a new run, which creates fresh payments instead of returning the old, already refunded ones. PayPal remembers order request ids for 6 hours, so a rerun protects you within that window. Keep every request id under 38 characters.
   - The same script loads the 15 sample requests from step 6 into the app's database.
5. **Write the refund policy (30 minutes), `data/refund_policy.md`.** A short sample policy for the made-up business: duplicate charge, full refund; cancelled 24 or more hours ahead, full refund; wrong amount, refund the difference; no-show, no refund. Show it in the app on its own tab. Then write the same rules as one function in code, `policy_allows(claim, booking, payment)`, so the guardrail in step 7 checks the policy against the booking record and never relies on the model.
6. **Write 15 sample requests with your answer key (1 hour), `data/payment_requests.csv`.**
   ```
   id,case_id,customer_name,customer_email,summary,description,expected_action,expected_amount
   ```
   - One request per case from step 4. `case_id` links the request to its seeded booking and payments; the expected capture is that case's payment with `is_refund_target = 1`.
   - `expected_action` is one of `refund_full`, `refund_partial`, `no_refund`, `ask_customer`. `expected_amount` is empty for `no_refund` and `ask_customer`.
   - Write them the way real customers write: some angry, some vague, some with the wrong date.
   - **Fill the answer key yourself before you build step 7.**
7. **Build `src/refund_helper.py`, the core (5 to 6 hours).**
   1. **Pick up** new requests from the database.
   2. **AI step 1, understand the claim.** Ask for JSON only: claim type (duplicate, cancelled, wrong_amount, other), the date and the amount the customer mentions. Validate it with pydantic, same as Phase 3.
   3. **Find the money.** Look up the customer's bookings and payments by email, then confirm each payment live with `GET /v2/payments/captures/{capture_id}` (status, amount, any refunds already made).
   4. **AI step 2, propose.** Give the model the claim, the bookings, the verified payments and the refund policy. JSON only: action, capture id, amount, a one line reason, and a draft reply to the customer.
   5. **Guardrails in code, never skipped:** the capture exists and is `COMPLETED`; it belongs to the request's customer; the amount is no more than what is still refundable; it was not already refunded; `policy_allows` approves the action against the booking record (status, cancellation time, booked price); the base URL is the sandbox. Any failure marks the request `blocked` and records which check failed.
   6. **Propose.** Save the proposal with status `proposed`: the payment found, the amount, the reason and the draft reply.
   7. **Wait for the owner.** The owner clicks Approve or Reject on the review page (step 10).
   8. **Refund only after approval.** Run the guardrails again, call `POST /v2/payments/captures/{capture_id}/refund` with `PayPal-Request-Id` set to `refund-<request id>-<capture id>` (so a retry can never refund twice), and save the refund id and status. The owner sends the customer the draft reply; the app never emails anyone.
   9. **Audit log.** Write every proposal, block, approval, rejection and refund to an `audit` table with a timestamp.
   - **Optional, for "Best Use of Agentic Commerce":** PayPal's AI Toolkit (github.com/paypal/AI-Toolkit) gives an AI agent ready made tools through an MCP server, such as get order, create refund and list transactions. You can use it for the lookup and refund calls, but keep your own guardrail checks around it, because the toolkit's refund tool refunds whatever it is told to.
8. **Measure it honestly (1 hour), `src/eval_refunds.py`.** Run steps 2 to 5 on the 15 sample requests without writing anything. Compare with your answer key and print matched actions, matched amounts, matched captures (the case's `is_refund_target` payment), and how many bad cases the guardrails stopped. This is the "[X] of 15" number. It runs the same way in any sandbox, because the answer key points at cases, not capture ids. Same rule as Phase 3: never score a request you tuned the prompt on.
9. **Add the customer request form (1 hour).** A "Get help with a payment" page in the app: name, email and a message. A new request goes through the same flow, so a judge can type their own complaint as one of the sample customers and watch it work. Limit the message length and the number of requests per session and per day, so the model bill stays capped.
10. **Design the review page (3 hours), `src/review_app.py`.** "Design" is a judging criterion, so give the owner a real screen: a queue of requests (customer, what they claim, payment found, proposed amount, reason, status) with Approve and Reject buttons and the draft reply underneath, blocked requests marked with the check that stopped them, and the refund policy and audit log on their own tabs. Streamlit is enough. AG Grid's free Community edition can be used for the table, but it does not compete for the AG Grid prize, which is judged on AG Grid Studio.
11. **Host it for the judges (3 hours).** Judges cannot be asked to bring their own paid AI key, because the project must be available to them free of charge and without restriction.
   - **Hosted demo on Render.** Deploy the app as a Render web service with the start command `streamlit run src/review_app.py --server.address 0.0.0.0 --server.port $PORT`, and set your own sandbox and model keys as Render environment variables (never in the repo). Claim the $50 hackathon credits. Set a monthly spend limit on the model API key.
   - Add a "Reset demo" button that starts a new seeding run, so every judge starts from the same state. Render's free tier wipes the local disk on every restart, so the app also reseeds at startup whenever the database is empty. The free tier sleeps when idle and takes about a minute to wake, so either say so on the page or use the credits for an always-on instance.
   - **Keep it live until judging ends on December 15**, and check it once a week until then.
   - **Backup: run it locally.** Add a "Run it in 5 minutes" section to the README: clone, add your own keys, `python src/seed_payments.py`, `streamlit run src/review_app.py`. Name a free model option (for example the Gemini free tier) so a local run can also cost nothing.

**Done when:** a "charged twice" request goes from submission, to a proposal, to the owner's approval, to a real sandbox refund with its refund id on the page; the guardrails stop both "must not refund" cases (`noshow-1` and `other-1`); a request typed into the form goes through the same flow; the hosted demo URL works end to end in a logged-out browser window; a fresh clone runs locally; and `eval_refunds.py` prints a real score.

### Phase 4. Metrics in SQL and a dashboard (about 6 hours)

1. `sql/schema.sql`:
   ```sql
   CREATE TABLE tickets (
     key TEXT PRIMARY KEY, request_type TEXT, category TEXT, priority TEXT,
     sentiment TEXT, status TEXT, created_at TEXT, resolved_at TEXT
   );
   CREATE TABLE comments (
     ticket_key TEXT, author TEXT, is_public INTEGER, is_agent INTEGER, created_at TEXT
   );
   CREATE TABLE sla (
     ticket_key TEXT, name TEXT, breached INTEGER, elapsed_minutes INTEGER
   );
   ```
2. `src/export.py` fills it:
   - Tickets: the search API from Phase 3, without the `labels is EMPTY` and `statusCategory` filters, and also asking for the `resolutiondate`, `status` and Request Type fields (Request Type is a custom field; find its id with `GET /rest/api/3/field`).
   - Category and sentiment: take them from the triage labels when a ticket has them. The 40 Phase 2 tickets were resolved before triage existed, so for those, take the category from your hand labels in `data/tickets_seed.csv` (matched through the issue keys saved in Phase 2) and leave sentiment empty.
   - Comments: `GET /rest/servicedeskapi/request/{key}/comment` (each comment says whether it is public and who wrote it). The API does not say whether the author is an agent, so set `is_agent` by comparing the author's `accountId` with your own (Phase 0 step 10). Internal notes from the triage helper are posted with your token too; they are not public, so the first response metric skips them.
   - SLAs, if your plan has them: `GET /rest/servicedeskapi/request/{key}/sla`.
   - Dates come back in several formats. Use the ISO 8601 one and store UTC.
3. `sql/metrics.sql`, one query each:
   - **First response time:** minutes from `created_at` to the first public comment written by an agent. Report the median, not the average, because one slow ticket skews an average.
   - **Share answered within 4 hours.**
   - **Resolution time** (median hours).
   - **Tickets by category per week.**
   - **Article use:** share of resolved tickets whose reply linked an article.
   - **Top repeat issue without an article.** This is the gap you fill in Phase 5.
4. `src/dashboard.py`, Streamlit with 4 charts: tickets per week by category, median first response, share within goal, top repeat issues. Run it with `streamlit run src/dashboard.py`.

**Done when:** the dashboard shows the numbers from your 40 worked tickets, and you can explain how each one is calculated.

### Phase 5. Close the loop, write it up (about 3 hours)

1. Take the top repeat issue from the metrics, write the missing help article, and note in the README which ticket data led to it. This is the "turned the top repeat issue into a new help article" bullet.
2. `src/weekly_report.py` writes `reports/week_YYYY_MM_DD.md` in plain language: what came in, how fast it was answered, what keeps repeating, and what to fix in the product. This is the kind of note a TAM or customer success person sends every week.
3. README: one paragraph on what it is, an architecture sketch (JSM → triage script → JSM; JSM → export → SQLite → dashboard), 4 screenshots (portal, queue, internal note, dashboard), how to run it, and the results table with your real numbers.
4. Record a 3 minute walkthrough (OBS Studio is free, or Loom's free plan, which caps recordings at 5 minutes) and link it in the README. Show only sample data, never a token. This video covers the whole help desk; the hackathon video (section 12) covers only the refund desk. Reuse your OBS scene setup from the hackathon recording.
5. Tell Claude your final numbers, and the project goes onto the non SWE base resume.

**Done when:** the README alone explains the project to a hiring manager in 2 minutes.

### Phase 6 (optional, highest value). Go live with the real salon

Only with the salon owner's OK.

1. The Salon app already has a `contact` API. When a customer submits the contact form, also create a JSM request with `POST /rest/servicedeskapi/request` (keep sending the owner her email exactly as today).
2. Turn customer notifications back on, so real customers get a ticket confirmation.
3. Store the JSM token as a Vercel environment variable. Never put it in client code.
4. Let real tickets flow for a few weeks. Your triage tool and dashboard now run on real data.
5. Never show real customer names or messages in screenshots, the README or videos.

After this you can honestly say "real customer tickets" and "support for a live business".

## 8. Rules that apply the whole time

- **Secrets:** `.env` stays out of git (it is already in `.gitignore`). Never paste a token into code, a screenshot or a video.
- **Privacy:** sample data uses `@example.com`. Real customer data from Phase 6 never leaves JSM.
- **AI never talks to customers and never moves money.** It only writes internal notes, labels and drafts. Every refund needs your approval.
- **Sandbox only.** `src/paypal.py` refuses to run unless the base URL contains `sandbox`.
- **Real numbers only.** Every number on the resume comes from your own export or eval run.
- **Commit small and often,** one commit per working step, with a clear message.

## 9. Timeline

The hackathon deadline sets the order: Phases 0 to 3B come first, and Phases 4 and 5 move to after you submit.

| When | Work |
|---|---|
| Oct 7, 12:00 PM ET (optional) | Hackathon webinar: APIMatic context plugins |
| Weekend Oct 10 to 11 | Phase 0 and Phase 1 |
| Oct 11 to 18 | Phase 2: seed tickets, work about 10 a day |
| Oct 12, 10:00 AM ET (optional) | Hackathon webinar: "Build a payments dashboard without building a dashboard" |
| Weekend Oct 17 to 18 | Phase 3 |
| Oct 19 to 25 | Phase 3B steps 1 to 6: PayPal setup, Postman, sample payments, policy, sample requests |
| Oct 26 to Nov 1 | Phase 3B steps 7 and 8: refund desk core and its score |
| Nov 2 to 8 | Phase 3B steps 9 to 11: request form, review page, and the hosted demo on Render |
| **Nov 9 to 10** | **Hackathon submission (section 12). Submit by Nov 10** |
| **Nov 12, 3:00 PM ET** | **Hard deadline. Nothing is accepted after it** |
| Nov 13 to 22 | Phase 4 and Phase 5 |
| Nov 12 to Dec 15 | Keep the hosted demo live and funded; check it weekly. Judging runs Dec 1 to 15 |
| Around Dec 21 | Winners announced |
| Later | Phase 6, after talking to the owner |

## 10. Risks and fallbacks

| Risk | What to do |
|---|---|
| JSM Free plan missing or changed | Use Zammad in Docker. Same phases, different API calls |
| An API call fails with a permission error | Make sure the token's account is the site admin and one of the 3 agents (Phase 0 step 7) |
| Setting priority through the API fails | Add Priority to the project's issue screen (Phase 3 step 4) |
| Knowledge base pushes a paid Confluence trial | Decline. Keep articles in `kb/articles.md` and publish them in the README until you find the free path |
| SLAs not on the Free plan | Skip Phase 0 step 5. Your SQL calculates response and resolution times anyway |
| `raiseOnBehalfOf` errors | Add the customer to the service desk first (Phase 2, step 2) |
| Triage accuracy is low | Report it honestly. Then improve the article list and category descriptions, and score again on held out tickets |
| API search returns nothing | Check that the JQL works in the Jira search bar first, then copy it exactly |
| Sandbox card payments are not enabled on your app | Use the approve link fallback in Phase 3B step 4 (about 20 minutes of clicks for 15 payments) |
| A seed script reruns and charges twice | Every create and refund call sends a `PayPal-Request-Id`; a retry reuses the same id |
| The AI proposes a wrong refund | The code guardrails block it first, and the review page shows which check failed |
| Falling behind before Nov 12 | Cut in this order: review page polish (keep a plain Streamlit table with Approve and Reject), the Reset demo button, the Postman collection, the request form. Never cut the hosted demo, the README or the video |
| Hosted demo goes down or runs out of model credit during judging | Spend limit and weekly checks from Phase 3B step 11; the README's local setup is the backup |

## 11. API cheat sheet

All calls use basic auth with your email and API token. Base URL is your site.

| Purpose | Call |
|---|---|
| List service desks | `GET /rest/servicedeskapi/servicedesk` |
| List request types | `GET /rest/servicedeskapi/servicedesk/{id}/requesttype` |
| Create customer | `POST /rest/servicedeskapi/customer` |
| Add customer to desk | `POST /rest/servicedeskapi/servicedesk/{id}/customer` |
| Create ticket | `POST /rest/servicedeskapi/request` |
| Read or add comments | `GET` or `POST /rest/servicedeskapi/request/{key}/comment` |
| SLA info | `GET /rest/servicedeskapi/request/{key}/sla` |
| Search tickets | `GET /rest/api/3/search/jql` (pages with `nextPageToken`; always pass `fields` and keep `project = SUP` in the JQL) |
| Edit labels, priority | `PUT /rest/api/3/issue/{key}` |
| Your own account id | `GET /rest/api/3/myself` |
| List fields (find the Request Type field id) | `GET /rest/api/3/field` |
| Search help articles | `GET /rest/servicedeskapi/knowledgebase/article?query=...&highlight=false` (`highlight` is required; if the call errors, match against `kb/index.csv` instead) |

**PayPal, sandbox base URL `https://api-m.sandbox.paypal.com`:**

| Purpose | Call |
|---|---|
| Get an access token | `POST /v1/oauth2/token`, basic auth with client id and secret, body `grant_type=client_credentials` |
| Create an order | `POST /v2/checkout/orders` (intent `CAPTURE`; with a card `payment_source` it completes in one step, and then the `PayPal-Request-Id` header is required) |
| Capture an approved order | `POST /v2/checkout/orders/{order_id}/capture` |
| Look up a payment | `GET /v2/payments/captures/{capture_id}` |
| Refund (full: empty body; partial: send `amount`) | `POST /v2/payments/captures/{capture_id}/refund` with header `PayPal-Request-Id` |
| Look up a refund | `GET /v2/payments/refunds/{refund_id}` |

PayPal docs: developer.paypal.com (Orders v2, Payments v2, Sandbox testing guide). Sandbox walkthrough: github.com/paypaldev/getting-started-with-paypal-sandbox. AI Toolkit: github.com/paypal/AI-Toolkit.

Atlassian docs: developer.atlassian.com, then Jira Service Management Cloud REST API, and Jira Cloud platform REST API v3.

## 12. Hackathon submission checklist (November 9 to 10)

**Due Thursday November 12, 2026, 3:00 PM New York time. Aim to submit by November 10.**

1. **Secret check.** The repo is already public, so run this before every push that adds code, and once more before submitting.
   - Scan the whole history with gitleaks (free, open source, from its GitHub releases page): `gitleaks git .` must report no leaks. A plain text search such as `findstr` also matches every harmless `token()` call, so it is too noisy to trust.
   - Confirm `.env` was never committed: `git log --all -- .env` must print nothing.
   - If a key ever appeared in a commit, revoke it and make a new one. Deleting the line is not enough, because history keeps it.
2. **Check the license.** The MIT `LICENSE` file was added on October 6. Confirm it is still in the repo root and that GitHub shows "MIT license" in the About box on the right. That is a hackathon rule.
3. **Push the final state.** The public repo already exists (`github.com/shubhampuri264-cell/Support_desk`). Claude pushes only after you approve each push.
4. **README for judges:**
   - the problem and who it is for (small service businesses and the person handling refunds), and a note that the demo business and its customers are made up;
   - how it works, with a diagram (ticket, then AI claim reading, then PayPal lookup, then guardrails, then proposal, then human approval, then refund);
   - which PayPal APIs are used and why, and which AI model and why;
   - the guardrails;
   - your eval results;
   - the hosted demo URL at the top, then "Run it in 5 minutes" as the backup;
   - the tools list, including Postman, Render and any AI coding assistant you used, and how each one was used.
5. **Demo video, under 3 minutes**, public on YouTube, no copyrighted music, showing it working end to end:
   - 0:00 to 0:20, the problem: a small salon handles payment complaints by hand.
   - 0:20 to 2:10, the demo: a "charged twice" request arrives; the refund desk finds the payment in PayPal; the proposal and reason appear; you approve as the owner; the refund shows up in the PayPal sandbox; the drafted reply is ready to send. Then show one blocked case, such as a payment that belongs to someone else.
   - 2:10 to 2:45, the guardrails and your eval numbers.
   - 2:45 to 2:55, who it is for and what comes next.
   - Keep the video on your own app and the PayPal sandbox, because the rules bar third-party trademarks without permission. Say once that the business and its customers are sample data.
   - Record with OBS Studio (free). Practice twice and speak in your own words.
6. **Devpost form:** text description, the tools and how each one was used, the repo link, the video link, the hosted demo URL, and the local setup instructions. State that the repo was started on October 6, 2026, after the submission period opened.
7. **Before you press submit:** open the hosted demo in a logged-out browser window and run one full case, and check that GitHub shows the license at the top of the repo page.
8. **After submitting:** send Claude the Devpost link, your eval score and the video link. The Hackathons section and the project bullets get updated with your real numbers. Keep the hosted demo live until December 15.
