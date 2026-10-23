# ADR 0002: Temporary static hosting on Vercel

Status: accepted, temporary

## Context

infra.vestlux.com was first published as an Azure Static Web App built from this repository with GitHub Actions. In October 2026 the Azure free trial ended and the subscription was disabled, which took the site offline. The site needs to stay reachable because it is linked from my CV and shown to people reviewing my work.

## Decision

Host the site on Vercel (Hobby plan) for now. Vercel builds the same MkDocs project from the same GitHub repository on every push to main. The DNS record for infra.vestlux.com now points to Vercel with a CNAME at the registrar.

## Consequences

- The site is back online at the same address, at no cost.
- Content, build and repository are unchanged. Only the hosting target and the DNS record changed.
- The old Azure Static Web Apps workflow is no longer needed and is being disabled so that it stops failing on every push.
- Moving the site back to Azure later is a hosting and DNS change only. It will be recorded in a new ADR when it happens.
- A DNS record that points to a hosting service nobody controls anymore can be taken over by someone else. Old records pointing to previous hosts are being removed for that reason.
