# ADR 0001 — Full Site Rebuild & Documentation Platform Choice

**Date:** September 30, 2026
**Status:** Accepted

## Context

An existing personal site (vestlux.com) was live but built for a different purpose — an online
course platform ("VestLux Academy") with a full course catalog, waitlist, and Stripe payment
integration. This did not represent me as a job candidate, and nothing about the current
Microsoft Hybrid Cloud roadmap or Project Polaris existed anywhere publicly. A separate need
also existed: a public, technical documentation platform to track the roadmap itself as it's
built, week by week.

## Decision

**1. Rebuild vestlux.com from scratch rather than adapt the existing code**, after archiving the
original on a separate branch (`archive/vestlux-v1`) rather than deleting it outright — the
CV-builder/Stripe code has potential future value and cost real effort to build.

**2. Build a separate site, infra.vestlux.com, as the technical build log**, sourced from the
`Philkaran/polaris` GitHub repository, rather than combining it into vestlux.com. Reasoning:
vestlux.com is a 30-second recruiter-facing summary; infra.vestlux.com is the detailed,
technical "show your work" layer. Conflating the two would weaken both.

**3. Use MkDocs Material for infra.vestlux.com**, not Docusaurus. Reasoning: pure Markdown
source, lighter dependency footprint, and a design system (dark slate + configurable accent
color) that maps cleanly onto the same visual language already established for the printed
roadmap and vestlux.com.

**4. Host infra.vestlux.com on an Azure Static Web App, not Vercel.** Reasoning: the site
demonstrating Azure capability should itself run on Azure — a small but deliberate signal, and
free-tier hosting with built-in GitHub Actions CI/CD costs nothing extra to set up.

**5. Deploy region: West US 2, not West Europe.** West Europe is currently restricted for new
Azure tenants (Microsoft capacity policy, confirmed via the Azure error `RequestDisallowedByAzure:
locationineligible`). Static Web Apps serve content via global CDN regardless of the configured
backend region, so this has no material effect on site performance for European visitors.

**6. Click-to-copy instead of `mailto:` links for contact information.** `mailto:` links
silently fail for any visitor without a configured default mail client — a common situation,
especially for anyone primarily using webmail. A copy-to-clipboard button works universally.

## Consequences

- Two separate repositories now need to stay conceptually in sync (`Philkaran/vestlux` and
  `Philkaran/polaris`), though they serve deliberately different audiences and update cadences.
- The backend region for infra.vestlux.com (West US 2) is geographically distant from primary
  European traffic, though this is mitigated by CDN-based content delivery.
- The archived `vestlux.com` v1 code (CV builder, Stripe, Supabase) remains available on the
  `archive/vestlux-v1` branch if revisited for VestLux Academy once course content exists.
