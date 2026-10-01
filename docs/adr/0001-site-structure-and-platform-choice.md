# ADR 0001: Site Structure and Platform Choice

**Date:** September 30, 2026
**Status:** Accepted

## Context

Project Polaris needs two public things before the technical work begins. First, a short professional summary that represents me as a candidate. Second, a technical documentation platform that records the roadmap as it is built, week by week, with every decision and procedure written down.

## Decision

**1. Two separate sites.** vestlux.com is the 30-second summary for recruiters. infra.vestlux.com is the detailed technical build log, sourced from the `Philkaran/polaris` GitHub repository. Combining them would weaken both, because a summary should stay short and a build log should stay detailed.

**2. MkDocs Material for infra.vestlux.com, not Docusaurus.** Reasons: content is written in plain Markdown, the dependency footprint is lighter, and the dark slate theme with a configurable accent colour matches the visual style of vestlux.com and the printed roadmap.

**3. Azure Static Web App for infra.vestlux.com, not Vercel.** Reasons: a site that documents Azure skills should itself run on Azure, and the Free tier includes GitHub Actions deployment at no extra cost.

**4. Deployment region: West US 2, not West Europe.** West Europe is restricted for new Azure customers (Microsoft capacity policy, confirmed by the error `RequestDisallowedByAzure: locationineligible`). Static Web Apps serve content through a global CDN regardless of the configured region, so this has no material effect on performance for European visitors.

## Consequences

- Two repositories (`Philkaran/vestlux` and `Philkaran/polaris`) must be kept in sync conceptually, although they serve different audiences and update at different rates.
- The Azure region for infra.vestlux.com (West US 2) is far from most European visitors. The CDN reduces the impact.
