# Agent Contribution Contract

All research agents contributing to this repository must follow `agents/shared-instructions.md` and the applicable vendor addendum.

## Ownership

- Cisco Research Agent: `catalog/cisco`, `research/cisco`, `renderers/cisco`, `validators/cisco`
- Fortinet Research Agent: `catalog/fortinet`, `research/fortinet`, `renderers/fortinet`, `validators/fortinet`
- Shared/core changes: `schemas`, `validators/common`, `app`, `examples`, `tests`

## Required workflow

1. Research the exact product, model, operating system, and release using official vendor sources.
2. Add or update a Vendor Rule conforming to `schemas/vendor-rule.schema.json`.
3. Mark renderer eligibility conservatively.
4. Add or update tests before changing a renderer.
5. Never add real secrets, customer configurations, credentials, or proprietary data.
6. Use feature branches: `cisco/<feature>`, `fortinet/<feature>`, or `core/<feature>`.
7. Do not modify the common schema solely to mirror a vendor CLI construct. Use vendor extensions.
