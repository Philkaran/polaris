# Day 0: Site Build and Infrastructure Platform

**Date:** September 30, 2026
**Status:** Phase 1 has not started yet. This is Day 0, the setup before the roadmap begins.

## What I did today

Before starting the 8-week Microsoft Hybrid Cloud roadmap, I built my public presence: a personal site (vestlux.com) and this documentation platform (infra.vestlux.com). The goal was to have an honest, working foundation in place before the technical work begins, so every step of the roadmap is documented as it happens and not reconstructed afterwards.

## Why two sites

Two audiences, two jobs. vestlux.com is the short summary a recruiter reads in 30 seconds. infra.vestlux.com is the detailed technical record behind it: decisions, procedures and weekly progress. Keeping them separate keeps each one clear.

## What vestlux.com is

Seven pages: Home, About, Project, Certifications, Roadmap, CV and Contact. Dark background with cyan and blue accents, matching this documentation site and my printed roadmap, so everything reads as one coherent whole.

The principle behind every page: nothing claims a skill I don't have yet. The Certifications page shows AZ-104 as in progress and the rest as planned. The CV only lists what is true today. Ambition lives on the Roadmap page, clearly labelled as a plan.

## What infra.vestlux.com is

This site. A public technical build log, built with MkDocs Material from the `Philkaran/polaris` GitHub repository. Architecture decisions (`docs/adr/`), runbooks (`docs/runbooks/`) and weekly entries like this one are published automatically each time I push a commit to the repository.

## How it is hosted

An Azure Static Web App on the Free tier, connected to the GitHub repository. Every push to `main` triggers a GitHub Actions workflow that builds the site and publishes it. The platform that documents my Azure skills runs on Azure itself.

## Infrastructure issues and fixes

1. **Region restriction.** Azure refused to create the Static Web App in West Europe for this new subscription (error `RequestDisallowedByAzure: locationineligible`, a Microsoft capacity policy for new customers). I deployed in West US 2 instead. Static Web Apps serve content through a global CDN, so this does not noticeably affect speed for European visitors.

2. **Wrong build in the deployment workflow.** The workflow Azure generated assumes a Node.js project and failed on the first deployment. I rewrote it to install Python and run `mkdocs build`, and set `skip_app_build: true` so Azure publishes the finished output without building it again. The second run succeeded.

3. **Custom domain.** I added a CNAME record at the domain registrar (Porkbun) pointing `infra.vestlux.com` to the Azure-generated hostname. Before relying on Azure's validation, I confirmed the record had propagated with `getent hosts`, then completed the validation.

## Outcome

Both sites are live and fully committed to GitHub:

- [vestlux.com](https://vestlux.com)
- [infra.vestlux.com](https://infra.vestlux.com)
- [github.com/Philkaran/vestlux](https://github.com/Philkaran/vestlux): personal site source
- [github.com/Philkaran/polaris](https://github.com/Philkaran/polaris): this documentation platform

## Next

Week 1, Day 1 of the roadmap: Azure fundamentals, covering subscriptions, resource groups, the portal and the Azure CLI.
