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

**While building the project.** The rules do not mention AI coding assistants. The relevant rules are that the submission must be the entrant's original work, solely owned by the entrant, and that prizes are subject to verification of the winner's role in creating it. PayPal's own AI Toolkit ships plugins for Claude Code, Codex and Cursor, so AI-assisted development is clearly expected. Our approach:

- Make the design decisions ourselves and be able to explain every part of the code.
- List every tool honestly in the submission, including AI coding assistants.
- For a written confirmation, ask in the hackathon Discord.

## PayPal AI tooling

- **PayPal AI Toolkit** (github.com/paypal/AI-Toolkit): an MCP server with plugins for Claude Code, Codex and Cursor. Covers orders, captures, refunds, invoices, subscriptions, disputes, catalog, shipments and transaction reporting. Sandbox only.
- **Disputes API:** list and respond to buyer disputes. Not in our current scope, but it fits a refund helper and could strengthen the innovation score.
- Other resources: REST API docs, JavaScript SDK v6, webhooks, payouts, invoicing, and a sandbox getting-started repository.

## Sponsor tools

Sponsor tools are optional. Any AI tool works as long as PayPal is central.

| Tool | What is offered | Prize | Our plan |
|---|---|---|---|
| Render | $50 hackathon credits; Render Workflows for agent orchestration | Credits | **Use.** Host the judges' demo URL, which also enters us for this prize |
| Postman | Free platform, PayPal API collection | None | Use for testing and documenting API calls |
| AG Grid | AG Grid Studio, a React boilerplate, a free 45-day trial license | Cash | **Skip.** Judges want custom widgets, theming and the Studio Agent Framework, which is a separate project |
| APIMatic | Context plugins for AI agents | Cash and subscription | Not planned |
| Bryntum | Calendar, scheduler and grid components | Cash | Not planned |
| Channel3, Elastic, KERNEL, Astropods, Zapier | Product data, vector search, agent browsing, agent infrastructure, automation | Channel3 only | Not planned |

## Events and support

| Date | Time | Session |
|---|---|---|
| Oct 7 | 9:00 AM PT (12:00 PM ET) | Power Your PayPal Hackathon Project with APIMatic Context Plugins |
| Oct 12 | 7:00 AM PT (10:00 AM ET) | Build a payments dashboard without building a dashboard |
| Oct 13 | 1:00 AM PT (4:00 AM ET) | Start building with PayPal (repeat of the Oct 6 session) |

Support is available in the PayPal Discord (discord.gg/sJ2G6DyvSK) and through the Devpost help desk.

## What this means for our entry

1. **Hosted demo on Render.** Judges cannot be required to bring their own paid AI keys, so the review page runs on Render with our sandbox and model keys, and stays live until December 15. The local "run it in 5 minutes" setup remains as a backup.
2. **Prize targets.** One Honorable Mention (Best Use of PayPal + AI, or Best Demo Delivery) plus the Render sponsor prize. A Grand Prize is the stretch goal.
3. **Skip the AG Grid prize.** It needs AG Grid Studio and a polished React dashboard, which is outside our time budget.
4. **Keep the video on our own screens.** Show the review page and the PayPal sandbox, and keep third-party product screens such as Jira to a minimum.
5. **Add the license now.** The repository is already public, and the license must be visible before submission.
6. **State the timeline in the submission.** The repository started on October 6, after the submission period opened.

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
