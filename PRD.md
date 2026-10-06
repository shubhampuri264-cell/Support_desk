# Salon Support Desk: Project PRD

**Owner:** Shubham Puri  
**Written:** October 6, 2026  
**Status:** Ready to start  
**Time:** Part 1 is about two weekends. Part 2 is one evening.

This document has two parts:

- **Part 1, Salon Support Desk.** A real help desk for your live Salon Booking Platform, built on Jira Service Management, with a help center, an AI triage helper and a response time dashboard.
- **Part 2, Salon sales demo video.** A 5 minute video that pitches the Salon platform to a business owner the way a solutions engineer would.

---

# Part 1: Salon Support Desk

## 1. Why this project

Your new non SWE resume is strong on customer contact but has one hole. Support, TAM and implementation job postings keep naming a help desk tool (Zendesk, Jira, ServiceNow) plus SQL, APIs and written documentation. Right now you cannot honestly name any help desk tool. This project fixes that with real use, and it reuses the Salon platform you already built, so the story connects:

> "I built the booking platform for a real salon, then set up the help desk behind it, wrote the help articles, built a tool that sorts incoming tickets, and tracked how fast tickets got answered."

That sentence covers the whole support job: intake, triage, answering, documentation, metrics, and feeding problems back to engineering.

## 2. What you will be able to say when it is done

Only claim what you actually finish. Fill every bracket with your real number.

**New skills you can list honestly:** Jira Service Management, ticketing, SLAs, knowledge base, REST APIs, SQL, Streamlit. Add Confluence only if you end up working in Confluence directly.

**Resume entry (Projects section, non SWE base):**

**Salon Support Desk (Help Desk Project)**, right column: `Jira Service Management, Python, SQL, REST API, Claude API`

- Set up the help desk behind a live salon booking app in Jira Service Management, with [N] request types, response time goals, and [N] help articles
- Built a Python triage tool that reads new tickets through the Jira API and tags category and priority with an LLM, matching hand labels on [X] of [40] sample tickets
- Tracked first response and resolution times in SQL and a dashboard, then turned the top repeat issue into a new help article

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

**Out of scope**

- Building your own ticketing system. The point is to use the tool employers use.
- Auto replying to customers with AI. Every customer facing reply is written or approved by you.
- Paid plans or paid add ons.

## 4. The people involved

| Who | Real or sample | What they do |
|---|---|---|
| Salon customers | Sample at first (Phase 2), real after Phase 6 | Ask about booking, rescheduling, cancelling, the chat assistant, confirmation emails and texts |
| You, the support agent | Real | Answer tickets, link articles, escalate bugs |
| The salon owner | Real | Gets escalations about her business. Must approve Phase 6 and anything shown on video |
| Engineering (also you) | Real | Receives bug escalations as GitHub issues in the SalonWebsite repo |

## 5. Tools and cost

All free. Free tiers change, so confirm each one when you sign up.

| Tool | Use | Free tier (checked Oct 2026) |
|---|---|---|
| Jira Service Management Cloud, Free plan | Help desk, portal, queues, request types | Up to 3 agents, unlimited customers, customer portal, email channel, basic automation |
| JSM knowledge base | Help articles | Built in, powered by Confluence. If it asks you to add Confluence, add the **Free** Confluence plan. Never start a paid trial |
| Python 3.11+ | Scripts | Free |
| Claude API (or Gemini API) | Triage labels | Pennies for 40 tickets on a small model such as Claude Haiku 4.5 (`claude-haiku-4-5-20251001`). Gemini has a free tier if you prefer $0 |
| SQLite | Metrics database | Free, no setup |
| Streamlit | Dashboard | Free |

**If the JSM Free plan is gone when you sign up**, use Zammad instead. It is free, open source, runs in Docker, and has a full REST API. Every phase below still applies; only the API calls change.

## 6. Repo layout

The repo already exists at `c:\me files\Coding Projects\salon-support-desk` with this PRD, a README, `.gitignore`, `.env.example` and `requirements.txt`. Build toward this:

```
salon-support-desk/
  PRD.md                 this file
  README.md              what it is, screenshots, how to run, walkthrough video link
  .env.example           names of the secrets (copy to .env, never commit .env)
  requirements.txt
  data/
    tickets_seed.csv     40 sample tickets with your hand labels
  kb/
    articles.md          drafts of every help article before you paste them into JSM
    index.csv            article id, title, url, category (used by triage)
  src/
    jsm.py               small API client (auth, get, post, paginate)
    seed_tickets.py      Phase 2: creates customers and tickets from the CSV
    triage.py            Phase 3: labels new tickets, writes an internal note
    eval_triage.py       Phase 3: compares bot labels with your hand labels
    export.py            Phase 4: pulls tickets, comments, SLAs into SQLite
    dashboard.py         Phase 4: Streamlit dashboard
    weekly_report.py     Phase 5: writes reports/week_YYYY_MM_DD.md
  sql/
    schema.sql
    metrics.sql
  reports/
  screenshots/
```

## 7. Phases and step by step instructions

Each phase ends with a **Done when** check. Do not move on until it passes.

### Phase 0. Setup (about 2 hours)

1. Go to atlassian.com, choose Jira Service Management, and sign up for the **Free** plan with your own email. Pick a site name such as `spuri-support`. Your site URL becomes `https://spuri-support.atlassian.net`.
2. Create a project from the **Customer service** template (not IT service management). Name it `Salon Support`, key `SUP`.
3. Set up **request types** (Project settings, Request types). Use these five and give each a one line description customers will see:
   - Booking problem
   - Reschedule or cancel
   - Chat assistant (Iris) question
   - Confirmation email or text not received
   - Something is broken (bug report)
4. Set up **queues**: All open, Unassigned, Bugs, Waiting on customer, Breached or close to breaching.
5. Set **response time goals**. Look under Project settings for **SLAs**. If you see it, set:
   - Time to first response: 4 hours
   - Time to resolution: 48 hours  
   If SLAs are not on your plan, skip this. Your Phase 4 script calculates both numbers anyway.
6. **Turn off customer notifications** before seeding (Project settings, Customer notifications), so 40 sample tickets do not send 40 emails. Turn them back on before Phase 6.
7. Create an **API token**: id.atlassian.com, Security, API tokens, Create. Save it once; you cannot view it again.
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

**Done when:** `python src/jsm.py` prints your service desk, and you have the five request type ids in `.env` or a config file.

### Phase 1. Help center articles (about 4 hours)

1. **Open the live Salon site and check every feature before you write about it.** Only write about what really exists. From the project facts, the app has: booking, choosing a service and stylist, checking availability, rescheduling and cancelling, the Iris chat assistant (books, reschedules, cancels, answers questions about services and hours, with a tap through menu that works even when the AI is off), confirmation emails, text messages, a contact form, and an admin side for the owner (appointments, services, promotions).
2. Draft 10 articles in `kb/articles.md` with this shape:
   - **Title** as the customer would search it ("How do I reschedule my appointment?")
   - **Who this is for**
   - **Steps** (numbered, one action each)
   - **If it still does not work** (what to send support, which request type to use)
3. Suggested 10 (adjust to what you confirm in step 1):
   1. How to book an appointment
   2. How to choose a stylist and service
   3. How to reschedule an appointment
   4. How to cancel an appointment
   5. Using the chat assistant (Iris)
   6. The chat assistant did not understand me (use the tap through menu)
   7. I did not get a confirmation email or text
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
   - **Fill `expected_category` and `expected_priority` yourself before you build the triage tool.** These are your answer key for Phase 3.
2. Write `src/seed_tickets.py`:
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
   - Load in 4 batches of 10 on different days, so your response times look like real work instead of 40 tickets created in the same minute.
3. **Work every ticket as the agent in the JSM web UI.** Reply publicly, ask a follow up where the ticket is vague, link the right article, and resolve. For bug tickets, open a GitHub issue in the SalonWebsite repo and link it in an internal note. This is the actual support work and where your interview stories come from.
4. Keep a short log in `reports/agent_notes.md` of anything surprising, such as a missing article or a confusing feature.

**Done when:** all 40 tickets are resolved, at least 20 replies link an article, and every bug ticket links a GitHub issue.

### Phase 3. AI triage helper (about 6 hours)

Goal: when a ticket arrives, the tool suggests a category and priority, spots an upset customer, suggests the best help article, and writes all of that as an **internal note**. It never sends anything to the customer.

1. **Find new tickets** with the Jira search API. The old `/rest/api/3/search` endpoint is removed; use the new one, which pages with a token:
   ```
   GET /rest/api/3/search/jql?jql=project = SUP AND labels is EMPTY ORDER BY created ASC
       &fields=summary,description,created,priority,labels&maxResults=50
   ```
   Repeat with `nextPageToken` until the response says `isLast: true`.
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
   - Priority: same call with `{"fields": {"priority": {"name": "High"}}}` (match your site's priority names)
   - Internal note: `POST /rest/servicedeskapi/request/{key}/comment` with `{"body": "...", "public": false}`. `public: false` is what keeps it internal. **Test this on one ticket and confirm in the UI that the customer cannot see it before running it on more.**
5. **Run it on a schedule** with polling: Windows Task Scheduler every 10 minutes, or just run it by hand. Webhooks need a public URL, so skip them for now.
6. **Measure it honestly** with `src/eval_triage.py`: run the classifier on the 40 seed tickets without writing to JSM, compare with your hand labels, and print category accuracy, priority accuracy, and a confusion table. **This gives you the "[X] of 40" number for the resume.** Never tune the prompt on a ticket and then count that ticket in the score. If you tune, hold out 10 tickets you never look at and report the score on those too.

**Done when:** a new ticket gets labels plus an internal note within one run, invalid model output is caught, and `eval_triage.py` prints a real accuracy number.

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
   - Tickets: the search API from Phase 3 (also ask for the `resolutiondate` and `status` fields).
   - Comments: `GET /rest/servicedeskapi/request/{key}/comment` (each comment says whether it is public and who wrote it).
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
4. Record a 3 minute walkthrough (see Part 2 for recording tips) and link it in the README.
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
- **AI never talks to customers.** It only writes internal notes and labels.
- **Real numbers only.** Every number on the resume comes from your own export or eval run.
- **Commit small and often,** one commit per working step, with a clear message.

## 9. Timeline

| When | Phases |
|---|---|
| Weekend 1, day 1 | Phase 0 and Phase 1 |
| Weekend 1, day 2 | Phase 2 seeding, start working tickets (finish over the week, about 10 a day) |
| Weekend 2, day 1 | Phase 3 |
| Weekend 2, day 2 | Phase 4 and Phase 5 |
| Later | Phase 6, after talking to the owner |

## 10. Risks and fallbacks

| Risk | What to do |
|---|---|
| JSM Free plan missing or changed | Use Zammad in Docker. Same phases, different API calls |
| Knowledge base pushes a paid Confluence trial | Decline. Keep articles in `kb/articles.md` and publish them in the README until you find the free path |
| SLAs not on the Free plan | Skip step 0.5. Your SQL calculates response and resolution times anyway |
| `raiseOnBehalfOf` errors | Add the customer to the service desk first (Phase 2, step 2) |
| Triage accuracy is low | Report it honestly. Then improve the article list and category descriptions, and score again on held out tickets |
| API search returns nothing | Check that the JQL works in the Jira search bar first, then copy it exactly |

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
| Search tickets | `GET /rest/api/3/search/jql` (pages with `nextPageToken`) |
| Edit labels, priority | `PUT /rest/api/3/issue/{key}` |
| Search help articles | `GET /rest/servicedeskapi/knowledgebase/article?query=...` (if it errors, match against `kb/index.csv` instead) |

Official docs: developer.atlassian.com, then Jira Service Management Cloud REST API, and Jira Cloud platform REST API v3.

---

# Part 2: Salon sales demo video

**Goal:** a 5 minute video where you pitch the Salon platform to a small business owner the way a solutions engineer runs a demo. Solutions engineer hiring managers ask for demos, and a recorded one is proof you can explain technology to a non technical buyer.

**This is not a build walkthrough.** If your current Salon demo shows code or how you built it, keep that one for the SWE resume. This one never shows code.

## Before you record (about 1 hour)

1. **Ask the salon owner** whether you may show the live site and admin page. If not, use a test booking and blur anything real.
2. **Hide real customer data.** Make 2 or 3 test bookings under fake names and only show those.
3. Use OBS Studio (free, no time limit), or Loom's free plan (it caps recordings at 5 minutes, which suits this). Trim with Clipchamp, which comes with Windows 11.
4. Use a real microphone or earbuds, close other tabs, and turn off notifications.
5. Practice the script out loud twice. Say it in your own words; do not read it.

## Script (about 5 minutes)

**1. Opening, 20 seconds.** "Hi, I'm Shubham. This is the booking platform I built for a neighborhood salon. I'll show you how it takes bookings when nobody is at the front desk."

**2. The customer's problem, 45 seconds.** Tell the discovery story in plain words. The owner ran every booking on pen and paper, had no way to take bookings online, and people could not find the salon online. You sat down with her and worked out what she actually needed. Then say what she cared about: bookings coming in without her answering the phone, and being findable.

**3. Live demo, 2 minutes 30 seconds.** Follow the customer, not the code.
   - On a phone screen: find the salon on Google Maps, open the site, pick a service and stylist, and book.
   - Open the chat assistant and ask it to reschedule. Point out that it answers questions about services and hours at 11pm, when the salon is closed.
   - Show the tap through menu: if a customer does not want to type, or the AI is off, they can still book.
   - Owner side: show the booking arriving (the email notification and the admin view).

**4. Two objections, 1 minute.** Ask each question out loud, then answer it.
   - "My customers aren't techy." The tap through menu works without typing, and the chat answers in plain language.
   - "What if the AI books something wrong?" Every action the assistant proposes is checked before anything is saved, and the assistant cannot make up prices or times. The owner sees every booking.

**5. Close, 20 seconds.** What it changed: the salon is on Google Maps with a real website, bringing in bookings and walk ins from people who could not find it before. End with a next step: "If you run a small business that still books by phone, I'd set up the same thing for you."

## Do not say

- Any booking count, launch date or revenue number. None are confirmed.
- "Cut booking from 7 steps to 3" or anything implying an older system existed. It was built from scratch.
- Any price for the service.

## After recording

1. Upload it to YouTube as **Unlisted**, titled "Salon Booking Platform, customer demo".
2. Send Claude the link. On the **non SWE base resume**, the Salon "Demo" link switches to this video. The SWE resume keeps the current one.
3. Optional: post it on LinkedIn with 3 lines about the problem, the fix and what changed for the owner.

**Done when:** the video is under 5 minutes, shows no code and no real customer data, and the link is on the non SWE resume.
