# Shared Network Config Builder Research Instructions

## Purpose
Research and validate vendor-specific platform capabilities, syntax, compatibility, licensing, lifecycle, verification, rollback, and operational risk for Network Configurator.

## Evidence standard
- Use official vendor configuration guides, command references, release notes, compatibility matrices, licensing guides, advisories, field notices, and lifecycle notices first.
- Research the exact product family, model, OS family, release, operating mode, license, feature, and peer dependencies.
- Never infer unsupported syntax from memory.
- Status must be one of: `validated`, `partially_validated`, `unverified`, `unsupported`, `conflicting_documentation`.
- Exact CLI may be marked `validated` only when official documentation establishes syntax and applicability.
- Keep vendor-neutral intent separate from vendor implementation.

## Required research
Document platform applicability, licensing, compatibility, prerequisites, scale limits, configuration sequence, defaults, disruption risk, verification, rollback, and lifecycle.

## Renderer gate
Set `renderer.eligible: true` only when exact syntax, platform/release scope, dependencies, required inputs, secret handling, verification, and rollback are established. Otherwise keep the feature cataloged but renderer-ineligible.

## Secrets
Never place real secrets in research, templates, examples, or tests. Use external references such as `${TACACS_SHARED_SECRET}`.

## Multi-device awareness
Record dependencies across firewalls, routers, switches, controllers, APs, VLAN paths, AAA, DNS, NTP, syslog, routing, MTU, HA, stacking, and link aggregation.

## Required output
1. Concise research summary.
2. One machine-readable YAML Vendor Rule conforming to `schemas/vendor-rule.schema.json`.
3. Genuine unresolved questions.
4. Official source links.

## Quality gate
Before submitting, verify platform, model, OS, release, mode, licensing, lifecycle, syntax, verification, rollback, disruption, dependencies, sources, secret handling, status, and renderer eligibility.
