# Day 0 — Site Rebuild & Infrastructure Platform

**Date:** September 30, 2026
**Status:** Phase 1 has not started yet — this is Day 0, pre-roadmap setup.

## What I did today

Before starting the actual 8-week Microsoft Hybrid Cloud roadmap, I rebuilt my entire public
presence from scratch: my personal site (vestlux.com) and this documentation platform
(infra.vestlux.com). The goal was to have an honest, working foundation in place *before* the
real technical work begins — not scrambling to build a portfolio after the fact.

## Why a full rebuild, not an edit

vestlux.com already existed, but as a course-selling platform ("VestLux Academy") — 24 course
listings, a waitlist, Stripe payment integration, none of it relevant to a job search. Rather
than awkwardly bolt a CV page onto a product site, I archived the old code on a separate git
branch (`archive/vestlux-v1`) and rebuilt the live site from zero as what it actually needs to
be: a professional landing page.

## What vestlux.com is now

Seven pages: Home, About, Project, Certifications, Roadmap, CV, Contact. Dark background with
cyan/blue accents — deliberately matching the same visual language as this documentation site
and my printed roadmap, so everything I show a recruiter feels like one coherent thing, not
three disconnected pieces.

**The one principle that shaped every page:** nothing claims a skill I don't have yet. The
certifications page shows AZ-104 as "in progress" and the rest as "planned" — not vague, not
inflated. The CV is a single, always-current document, not a "future" version padded with
skills I'm aiming for. Ambition lives on the **Roadmap** page instead, clearly labeled as a
plan — that page is honest precisely because it doesn't pretend to be anything else.

## What infra.vestlux.com is

This site. A public technical build log, rendered from this same GitHub repository
(`Philkaran/polaris`) using MkDocs Material. Every architecture decision (`docs/adr/`), every
operational procedure I write down (`docs/runbooks/`), and every weekly entry like this one
gets published here automatically the moment I push a commit — nothing is polished after the
fact.

## How it's actually hosted

infra.vestlux.com runs on an **Azure Static Web App** — deliberately, not Vercel. The site
proving my Azure skills is itself hosted on Azure. It's connected directly to this GitHub repo,
so every `git push` to `main` triggers an automatic rebuild and redeploy via GitHub Actions —
no manual upload step, ever.

## Real problems I hit today, and how I solved them

This part matters as much as the result — this is the actual skill being demonstrated, not
just the finished sites:

- **A garbled terminal paste** during a large file write initially looked like file corruption.
  Rather than assume the worst, I verified with `cat` before redoing any work — it was a cosmetic
  terminal-echo issue, the file was intact both times it happened.
- **A missing component file** broke the homepage build (`Module not found`). Diagnosed by
  listing the actual directory contents rather than assuming the file existed, found it was
  never created, recreated it, verified before restarting.
- **A dependency version mismatch** — the installed `lucide-react` version didn't export the
  icon names I'd used. Fixed by writing the two icons as plain inline SVG instead, removing the
  dependency risk entirely rather than chasing an exact version pin.
- **A file upload that silently failed twice** (drag-and-drop, then the Codespaces upload
  dialog) before succeeding on a third method via GitHub's own web upload. Diagnosed by checking
  actual file size/existence at each step instead of trusting the UI's apparent success.
- **A broken `mailto:` link** on Contact and in the footer — traced to the visitor's browser
  having no default mail client configured (very common), not a code bug. Replaced with a
  click-to-copy button as a more reliable pattern.
- **Three "zombie" dev server processes** ended up simultaneously squatting on ports 3000, 3001,
  and 3002 after repeated restarts, causing me to load stale/dead browser tabs and see
  misleading errors. Found via the Ports tab, killed by exact process ID, confirmed clean with
  `lsof` before restarting once, cleanly.
- **Azure blocked West Europe** for this brand-new subscription ("region currently not accepting
  new customers") — a real, documented Microsoft capacity restriction, not a mistake on my end.
  Solved by switching to West US 2; since Static Web Apps serve content from a global CDN
  regardless of this setting, it has no real impact on site speed for visitors.
- **Azure's auto-generated GitHub Actions workflow** assumed a Node.js project and failed on
  first deploy. Rewrote it to install Python and run `mkdocs build` instead, with
  `skip_app_build: true` telling Azure to just publish the already-built output.
- **DNS for the custom domain** — added a CNAME record in Porkbun pointing `infra.vestlux.com`
  to the Azure-generated hostname, verified propagation myself with `getent hosts` before
  trusting Azure's validation step, rather than just clicking retry blindly.

## Outcome

Both sites are live, honest, and fully committed to git:

- **[vestlux.com](https://vestlux.com)**
- **[infra.vestlux.com](https://infra.vestlux.com)**
- **[github.com/Philkaran/vestlux](https://github.com/Philkaran/vestlux)** — personal site source
- **[github.com/Philkaran/polaris](https://github.com/Philkaran/polaris)** — this documentation platform

## Next

Week 1, Day 1 of the actual roadmap: Azure fundamentals — subscriptions, resource groups, the
Portal, Azure CLI.
