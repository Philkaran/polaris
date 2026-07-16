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
