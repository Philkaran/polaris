# Decision Log

Format: date — what I chose, what I rejected, why.

---

## 2026-07-16 — Codespaces over local VM
Chose: GitHub Codespaces for all lab work.
Rejected: Local VirtualBox/VMware VMs.
Why: Laptop hardware can't handle heavy local VMs. Codespaces runs in-browser, free tier covers early phases, and keeps environment consistent across sessions.

## 2026-07-17 — Default file permissions
Chose: 644 (owner read/write, group/others read-only) as the baseline for tracked files.
Rejected: leaving Codespaces' default 666 (world-writable) permissions as-is.
Why: 666 is a Codespaces convenience default, not a security posture. Getting into the habit of tightening permissions now — even on throwaway lab files — builds the instinct that matters later for Phase 2 hardening (CIS Benchmarks, least-privilege).

## 2026-07-18 — Treat environment variables as sensitive by default
Observed: GITHUB_CODESPACE_TOKEN and other auth-relevant values are injected automatically into every Codespace via `env`.
Decision: never echo, log, or dump full environment output in any script going forward — treat env vars as secrets-adjacent even in throwaway labs.
Why: builds the habit now, before Vault/secrets-management work in Phase 12, instead of learning it the hard way via a leaked token in a log.
