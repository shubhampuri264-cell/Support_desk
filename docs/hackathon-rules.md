# PayPal AI Hackathon: Rules and Requirements

A working summary of the official rules and hackathon pages, read on October 6, 2026. If anything here differs from the official rules, the official rules win. Links are at the bottom.

## Key dates

| Event | Pacific Time | Eastern Time |
|---|---|---|
| Submission period opens | Thu Oct 1, 2026, 9:15 AM | 12:15 PM |
| **Submission deadline** | **Thu Nov 12, 2026, 12:00 PM** | **3:00 PM** |
| Judging | Tue Dec 1, 2:00 PM to Tue Dec 15, 8:00 AM | 5:00 PM to 11:00 AM |
| Winners announced | On or around Mon Dec 21, 2:00 PM | 5:00 PM |

- Our internal target is to submit by **Tuesday November 10**.
- Draft submissions can be saved and edited until the deadline. After it, no changes are allowed, except removals the sponsor permits (infringing material or personal information).

## Organizers

- **Sponsor:** PayPal, Inc.
- **Administrator:** Devpost, Inc.
- Online and open to the public. 8,070 people had registered as of October 6.

## Eligibility

- Individuals who are at least the age of majority where they live, teams of such individuals, and organizations.
- There is no maximum team size. Solo entries are allowed.
- **Excluded:** residents of Brazil, Quebec, Russia, Crimea, Cuba, Iran, North Korea, and any other country comprehensively sanctioned by the U.S. Treasury (OFAC); employees and agents of PayPal and Devpost and their immediate family or household; judges and their employers and families; anyone with a real or apparent conflict of interest.
- A project that received funding, a contract or a commercial license from PayPal or Devpost before the deadline is not eligible.
- An entrant may submit more than one project if each is unique and substantially different.

## Project requirements

Stage one of judging is pass/fail: the project must reasonably fit the theme and reasonably apply the required PayPal APIs or SDKs. A project that fails this stage is not scored.

The project must:

1. **Integrate the PayPal developer platform using the free sandbox.** PayPal must be central to the project, not decorative. Any PayPal technology counts, including the REST APIs, SDKs, Venmo and Braintree.
2. **Meaningfully use AI** (any tool, model or platform) as part of the experience or functionality.
3. **Be new, or significantly updated after October 1, 2026.** An existing project must explain what was added during the hackathon. This repository was created on October 6, so it is a new project.
4. **Be the entrant's original work and solely owned by the entrant.** Open source code may be used if its license is followed and the project builds on top of it. Third-party technical help is allowed as long as the submission remains the entrant's own work product.

## Submission requirements

| Item | Requirement |
|---|---|
| Working demo | Judges must be able to run or interact with a working build, through complete setup instructions in the repository or a hosted demo URL. A mockup, static prototype or non-functional demo does not qualify |
| Code repository | Public on GitHub, GitLab or Bitbucket, containing all source code, assets and instructions needed to run the project |
| License | An open source license file that the host detects and shows at the top of the repository page |
| Text description | Explains the features and functionality |
| Tools list | Which tools were used and how each one was used |
| Video | **Under 3 minutes** (judges are not required to watch past 3:00), public on YouTube, showing the project working on the device it was built for. No copyrighted music or third-party trademarks without permission |
| Testing access | The project must be available to judges **free of charge and without restriction until judging ends on December 15**. If it needs a login, credentials must be provided |
| Language | English, or with English translations |

## Judging

Five criteria, weighted equally:

1. **Technological implementation.** How thoroughly and skillfully the project uses the PayPal developer platform and AI. Genuine effort and a working, non-trivial implementation.
2. **Design.** A complete, coherent product experience, not just a technical proof of concept.
3. **Potential impact.** A credible, specific case for solving a real problem for a real audience, backed by what the demo shows.
4. **Innovation.** How creative and novel the idea is, and how it differs from existing concepts.
5. **Presentation.** The video shows the project working end to end and makes clear what problem it solves, who it is for and why it matters.

Ties are broken by comparing scores on each criterion in the order above.

## Prizes ($67,500+)

| Group | Prize | Amount |
|---|---|---|
| Grand | 1st / 2nd / 3rd place | $12,000 / $8,000 / $5,000 |
| Honorable Mention | Most Creative | $5,000 |
| Honorable Mention | Most Impactful | $5,000 |
| Honorable Mention | Best Demo Delivery | $5,000 |
| Honorable Mention | Best Use of PayPal + AI | $5,000 |
| Honorable Mention | Best Use of Agentic Commerce | $5,000 |
| Sponsor | AG Grid | $5,000 / $2,000 / three at $1,000 |
| Sponsor | APIMatic | Three at $1,000 plus a 6 month subscription |
| Sponsor | Bryntum | Three at $1,000 |
| Sponsor | Channel3 | $1,500 |
| Sponsor | Render | Credits only: $1,000 / $750 / $500 |

**Stacking limit:** a project can win at most one Grand Prize and one Sponsor Prize, or one Honorable Mention and one Sponsor Prize.

Prize payment requires a winner affidavit (due within 10 business days), tax forms (W-9 for U.S. residents), and verification of the winner's identity and role in creating the submission. Winners pay their own taxes.

## Use of AI

**In the project.** Any AI tool, model or platform is allowed. There is no upper limit; the requirement is that both PayPal and AI are central to the project.

**While building the project.** The rules do not mention AI coding assistants. The relevant rules are that the submission must be the entrant's original work, solely owned by the entrant, and that prizes are subject to verification of the winner's role in creating it. PayPal's own AI Toolkit ships plugins for Claude Code, Codex and Cursor, so AI-assisted development is clearly expected. PayPal's October 7 sponsor webinar went further: it demonstrated building with the APIMatic Context Plugin inside Claude Code, and the APIMatic prize requires building the integration with that plugin. Our approach:

- Make the design decisions ourselves and be able to explain every part of the code.
- List every tool honestly in the submission, including AI coding assistants.
- For a written confirmation, ask in the hackathon Discord. A member's reply is not an official answer (see the Discord rules below), so count it only if it comes from PayPal or Devpost staff; otherwise ask the Devpost help desk.

## PayPal AI tooling

- **PayPal AI Toolkit** (github.com/paypal/AI-Toolkit): an MCP server with plugins for Claude Code, Codex and Cursor. Covers orders, captures, refunds, invoices, subscriptions, disputes, catalog, shipments and transaction reporting. Sandbox only.
- **Disputes API:** list and respond to buyer disputes. Not in our current scope, but it fits a refund helper and could strengthen the innovation score.
- **Sandbox getting-started guide** (github.com/paypaldev/getting-started-with-paypal-sandbox): accounts, credentials, a first test payment and negative testing. The repository has no license, so link to it rather than copying from it. Points we will use:
  - developer.paypal.com takes the real PayPal login; www.sandbox.paypal.com takes only generated sandbox account logins. The API base is `https://api-m.sandbox.paypal.com`.
  - A personal (buyer) sandbox account needs a balance to pay with PayPal funds. Balances are set under Testing Tools, Sandbox Accounts, View/Edit Account.
  - To force an error on a sandbox call, add the header `PayPal-Mock-Response: {"mock_application_codes": "<CODE>"}`. Each API has its own codes, listed in the Orders v2 and Payments v2 error references. This lets us test refund failure handling without a real failure.
  - Branch error handling on `details[0].issue` and log `debug_id`, which PayPal asks for in support requests.
  - Account-level Negative Testing (View/Edit Account, Settings) makes every transaction on that account fail. Turn it off afterwards.
- Other resources: REST API docs, JavaScript SDK v6, webhooks, payouts and invoicing.

## Sponsor tools

Sponsor tools are optional. Any AI tool works as long as PayPal is central.

| Tool | What is offered | Prize | Our plan |
|---|---|---|---|
| Render | $50 hackathon credits; Render Workflows for agent orchestration | Credits | **Use.** Host the judges' demo URL, which also enters us for this prize. The credit code sits behind the "Start building with $50" link on the Render details page, which does not look like a link |
| Postman | Free platform, PayPal API collection | None | Use for testing and documenting API calls |
| AG Grid | AG Grid Studio, a React boilerplate, a free 45-day trial license | Cash | **Skip.** Judges want custom widgets, theming and the Studio Agent Framework, which is a separate project. The license is not the blocker: AG Grid's DevRel lead said in Discord that every product works without a license for the hackathon, showing a watermark and a console error that judging does not penalize |
| APIMatic | Context Plugin: skills that teach a coding agent the APIMatic-generated PayPal Server SDK (details below) | Cash and subscription | **Decide before #17.** It covers the Orders and Payments calls `src/paypal.py` needs |
| Bryntum | Calendar, scheduler and grid components | Cash | Not planned |
| Zapier | Zapier MCP: AI agent actions across 9,000+ apps, including PayPal invoices, orders and refund triggers | None | **Skip.** PayPal is a premium Zapier app, so it needs the 14-day Professional trial, which would end long before judging ends on December 15 and break the hosted demo. Each successful MCP call also uses 2 plan tasks |
| Channel3, Elastic, KERNEL, Astropods | Product data, vector search, agent browsing, agent infrastructure | Channel3 only | Not planned |

### APIMatic Context Plugin

From the October 7 webinar (PayPal and APIMatic) and the plugin's README.

- **What it is.** A Claude Code, Cursor, Codex or VS Code plugin whose skills teach the agent the PayPal Server SDK from the SDK's own source and docs. Languages: TypeScript, Python, Java, Ruby, PHP and C#. APIs: Orders, Payments, Vault, Subscriptions and Transaction search.
- **Install.** `npx context-plugins install https://github.com/paypaldev/server-sdk-context-plugin-preview`
- **Status.** A preview made for the hackathon. The README says it "is not an official long term supported PayPal product and may be removed at any time."
- **Prize ("Best Use of APIMatic").** The top 3 win $1,000 each plus six months of APIMatic Business. Every submission that uses the plugin gets one month of APIMatic Basic. To qualify, build the PayPal integration with the plugin and answer the plugin question on the submission form.
- **What it changes for us.** `src/paypal.py` would call the PayPal Server SDK for Python instead of plain `requests`. The sandbox-only check, the `PayPal-Request-Id` on refunds and the guardrails stay ours either way.
- The webinar's claims (86% fewer errors, 50 times cheaper) are APIMatic's own benchmark, not independent results.

## Events and support

| Date | Time | Session |
|---|---|---|
| Oct 7 | 9:00 AM PT (12:00 PM ET) | Power Your PayPal Hackathon Project with APIMatic Context Plugins (held; slides in the Discord, summary under Sponsor tools) |
| Oct 12 | 7:00 AM PT (10:00 AM ET) | Build a payments dashboard without building a dashboard |
| Oct 13 | 1:00 AM PT (4:00 AM ET) | Start building with PayPal (repeat of the Oct 6 session) |

Support is available in the PayPal Discord (discord.gg/sJ2G6DyvSK) and through the Devpost help desk.

## PayPal developer Discord rules

From the server's welcome message, read on October 7, 2026. The server is a community space, not an official PayPal support channel. A member's reply is not PayPal advice or an official statement, and PayPal's official terms and developer documentation win over anything said there. Discord's Community Guidelines and Terms of Service also apply. Breaking the rules can lead to removed posts, warnings, restrictions or a ban.

What applies to us:

- **Never post secrets or payment data, even from the sandbox.** No API keys, client secrets, access tokens, webhook secrets, transaction or capture ids, card data, PayPal account details, or screenshots that show any of them. The server enforces this automatically. When asking about an API error, post the endpoint, the status code and the error name, with every id and token removed.
- **No personal data.** Our sample customers are made up, but real salon customers and the owner's details must never appear.
- **No proprietary or third-party content.** Do not paste SalonWebsite code or the owner's business information. The public Support_desk repo is fine to link.
- **Technical questions only.** No requests for financial, legal, tax, regulatory or compliance advice. Ask how the refunds endpoint behaves, not whether our refund policy is compliant.
- **Account matters go to official PayPal support,** not the server: account issues, disputes, holds, limitations, fraud and security incidents.
- **Use channels, not DMs.** PayPal staff never ask for passwords, 2FA codes, API secrets or account details by DM. Report any DM that does.
- **Sharing the project is fine; promotion is not.** Post the repo or demo link in an on-topic channel, without repeating it across channels.
- **Technical questions go in the dev-questions channel.** Staff redirect questions asked elsewhere, or by DM, to it. Webinar recordings and slides are pinned in the hackathon channel.

## Answers from the Discord

Read on October 7, 2026. Only answers from PayPal or sponsor staff count as guidance; tips from other entrants are marked as such and need checking.

- **Plain REST is enough.** The JavaScript SDK v6 is not required; calling the PayPal API directly also counts (PayPal developer advocate).
- **Mixing is fine.** Calling the REST API directly for anything the PayPal MCP server does not cover, and using the AI Toolkit for the rest, is allowed. PayPal asks to hear which features the MCP server is missing (PayPal developer advocate).
- **Disputes in the sandbox** need dispute creation enabled in the sandbox account settings. Creating one through the API as the buyer needs the `PayPal-Auth-Assertion` header, and one entrant got `No permissions to set target_client_id` (a missing `GRANT_PROXY_CLIENT` permission), which PayPal is looking into. An entrant's workaround: a second sandbox Business account acts as the buyer with its own REST app, pays the merchant account, then opens the dispute. This matters only if we add the Disputes API.
- **Sandbox accounts (entrant tip).** Card payments through `payment_source.card` work in only 37 sandbox countries. Create the sandbox accounts as US accounts.
- **Region sign-up problems** (Bangladesh, Pakistan, India, Türkiye and others) are still being looked into by PayPal. They do not affect us.

## What this means for our entry

1. **Hosted demo on Render.** Judges cannot be required to bring their own paid AI keys, so the review page runs on Render with our sandbox and model keys, and stays live until December 15. The local "run it in 5 minutes" setup remains as a backup.
2. **Prize targets.** One Honorable Mention (Best Use of PayPal + AI, or Best Demo Delivery) plus one sponsor prize. A Grand Prize is the stretch goal. Only one sponsor prize can be won, so if `src/paypal.py` is built with the APIMatic Context Plugin, APIMatic ($1,000 cash) becomes the sponsor target and Render (credits) the fallback; Render still hosts the demo either way.
3. **Skip the AG Grid prize.** It needs AG Grid Studio and a polished React dashboard, which is outside our time budget.
4. **Keep the video on our own screens.** Show our refund desk app and the PayPal sandbox only.
5. **License.** The MIT license was added on October 6. Confirm that GitHub still shows it at the top of the repository page before submitting.
6. **State the timeline in the submission.** The repository started on October 6, after the submission period opened.
7. **Use a made-up business.** The salon takes no online payments and the owner does not want to add them (October 7), so the refund desk is shown on a made-up business. That keeps the salon's name out of the demo and the video, and the submission says plainly that the business and its customers are sample data.

## Sources

- [Official Rules](https://paypalaihackathon.devpost.com/rules)
- [Hackathon overview](https://paypalaihackathon.devpost.com/)
- [Resources](https://paypalaihackathon.devpost.com/resources)
- [FAQs](https://paypalaihackathon.devpost.com/details/faqs)
- [AG Grid details](https://paypalaihackathon.devpost.com/details/aggrid)
- [Render details](https://paypalaihackathon.devpost.com/details/render)
- [Postman details](https://paypalaihackathon.devpost.com/details/postman)
- [PayPal Community Blog announcement](https://developer.paypal.com/community/blog/PayPal_AI_Hackathon/)
- [PayPal AI Toolkit](https://github.com/paypal/AI-Toolkit)
- [PayPal AI tools, getting started](https://developer.paypal.com/ai-tools/get-started)
- [PayPal Developer Docs](https://developer.paypal.com/)
- [PayPal Sandbox](https://sandbox.paypal.com/)
- [Getting started with the PayPal sandbox](https://github.com/paypaldev/getting-started-with-paypal-sandbox)
- [PayPal Postman collection](https://postman.com/paypal)
- [PayPal docs example code](https://github.com/paypal-examples/docs-examples)
- [PayPal Server SDK Context Plugin (preview)](https://github.com/paypaldev/server-sdk-context-plugin-preview)
- [Sandbox dispute setup](https://developer.paypal.com/disputes/set-up)
