# Agent Contribution Contract

This repository supports multiple research and development agents contributing
to Network Configurator.

The `main` branch is the authoritative current state of the project.

Repository content supersedes older conversational copies of schemas,
instructions, Vendor Rules, renderers, validators, examples, tests, and other
project artifacts.

Agents must not assume access to another agent's private conversation,
memory, instructions, or research.

Cross-agent collaboration occurs through artifacts committed to this
repository.

---

## Instruction Bootstrap

Before beginning project work, read these files in order:

1. `AGENTS.md`
2. `agents/shared-instructions.md`
3. The applicable vendor addendum:
   - Cisco: `agents/cisco.md`
   - Fortinet: `agents/fortinet.md`

Then inspect the current repository artifacts relevant to the requested work:

1. Applicable schemas
2. Relevant catalog entries
3. Existing Vendor Rules
4. Affected renderers
5. Affected validators
6. Relevant examples
7. Relevant tests

Only after this inspection should an agent propose or implement project
changes.

When connected GitHub repository tools are available, use those tools to read
the current `main` branch.

Do not substitute public web indexing, search-engine copies, stale local
copies, or previous conversational content for repository contents when direct
repository access is available.

---

## Instruction Precedence

Apply instructions in this order:

1. Repository-wide requirements in `AGENTS.md`
2. `agents/shared-instructions.md`
3. Applicable vendor addendum
4. Current schemas and repository contracts
5. Task-specific requirements

Vendor addenda may introduce platform-specific requirements but must not weaken
shared requirements for:

- Authoritative sourcing
- Exact platform and software applicability
- Lifecycle review
- Secret handling
- Configuration safety
- Testing
- Conservative renderer eligibility
- Vendor Rule schema compliance

If an apparent conflict cannot be resolved safely, stop that portion of the
change and document the conflict for review.

---

## Ownership

### Cisco Research Agent

Primary ownership:

- `catalog/cisco/`
- `research/cisco/`
- `renderers/cisco/`
- `validators/cisco/`

Follow:

- `agents/shared-instructions.md`
- `agents/cisco.md`

### Fortinet Research Agent

Primary ownership:

- `catalog/fortinet/`
- `research/fortinet/`
- `renderers/fortinet/`
- `validators/fortinet/`

Follow:

- `agents/shared-instructions.md`
- `agents/fortinet.md`

### Shared/Core

The following are shared project components:

- `schemas/`
- `validators/common/`
- `app/`
- `examples/`
- `tests/`

Changes to shared/core components require consideration of all supported
vendors.

Do not change a shared schema solely to mirror a vendor-specific CLI construct.

Use vendor extensions for genuinely vendor-specific requirements.

If vendor research identifies a legitimate deficiency in the common model,
propose the shared/core change separately and explain why the capability is
vendor-neutral.

---

## Branch Naming

Use feature branches.

Cisco work:

`cisco/<feature>`

Fortinet work:

`fortinet/<feature>`

Shared/core work:

`core/<feature>`

Examples:

`cisco/iosxe-vlan-trunk`

`fortinet/fortios-vlan-interface`

`core/network-intent-lag`

Do not mix unrelated feature work into the same branch.

---

## Required Contribution Sequence

For vendor configuration features, use this sequence:

1. Inspect current repository state.
2. Research the exact platform, model, operating system, release, and mode.
3. Create or update the applicable Vendor Rule.
4. Add or update validation behavior.
5. Add or update tests.
6. Change the renderer only after the required research and tests exist.
7. Validate generated output.
8. Document unresolved limitations.

Conceptually:

Research
→ Vendor Rule
→ Validation
→ Tests
→ Renderer
→ Golden output

Legacy implementation may be used as migration reference material but is not
authoritative evidence for current syntax or renderer eligibility.

---

## Vendor Rules

Vendor Rules must conform to the current Vendor Rule schema under `schemas/`.

Do not use a schema version remembered from a previous conversation.

Renderer eligibility must be conservative.

A feature may be recorded in the catalog or research library without being
eligible for executable rendering.

When required evidence is incomplete, preserve the research result but keep
renderer eligibility disabled.

---

## Common Network Intent

Network Configurator maintains vendor-neutral network intent.

Vendor-specific configuration belongs in Vendor Rules, vendor validators,
vendor renderers, or supported vendor extensions.

Do not place vendor CLI directly into common network intent.

The same logical network intent should be usable by multiple vendor renderers
where the underlying capability is genuinely common.

---

## Cross-Device Awareness

Network Configurator models complete deployments rather than unrelated device
configurations.

When applicable, contributions must account for dependencies between devices,
including:

- VLAN propagation
- Tagged and untagged/native VLAN consistency
- Layer-3 gateway placement
- DHCP server or relay paths
- Routing adjacency and return paths
- Link aggregation
- MTU consistency
- Firewall policy dependencies
- WLAN-to-VLAN mapping
- AAA reachability
- DNS, NTP, and syslog reachability
- HA, stack, cluster, controller, and managed-device relationships

Vendor-specific facts belong in Vendor Rules.

Vendor-neutral consistency checks belong in common validation.

---

## Secrets and Sensitive Data

Never commit:

- Real passwords
- Pre-shared keys
- TACACS or RADIUS secrets
- SNMP credentials
- API tokens
- Private keys
- Customer certificates
- Customer credentials
- Proprietary customer configurations
- Other customer-sensitive data

Use schema-supported external references or placeholders.

The public repository must contain only sanitized examples and test fixtures.

---

## Testing Requirement

Do not add executable renderer behavior without applicable tests.

Where appropriate, include:

- Positive cases
- Invalid or unsupported cases
- Version-boundary cases
- Secret-placeholder cases
- Cross-device validation cases
- Golden generated configurations

A successful template render alone does not establish that a configuration is
correct or supported.

---

## Source of Truth for Generated Configuration

Generated configuration must be traceable through:

Network Intent
→ Vendor Rule
→ Validation
→ Renderer
→ Generated Output

The research agent establishes vendor facts.

The deterministic renderer generates executable configuration.

Do not treat conversationally generated CLI as production renderer output.

---

## Modification Safety

Before modifying repository content:

1. Confirm ownership of the affected path.
2. Inspect existing implementation and tests.
3. Keep the change limited to the requested feature.
4. Preserve backward compatibility where required by the current project
   contracts.
5. Do not delete or substantially rewrite another vendor's artifacts merely to
   simplify the current implementation.
6. Surface shared architectural changes separately.

Write, delete, merge, and other consequential repository operations should
remain subject to user approval when the connected repository tooling supports
approval controls.

---

## Completion Criteria

A contribution is complete only when applicable:

- Research follows `agents/shared-instructions.md`.
- The vendor addendum has been followed.
- Vendor Rules conform to the current schema.
- Platform/software applicability is explicit.
- Relevant lifecycle and licensing requirements have been checked.
- Validation behavior exists.
- Tests pass.
- Renderer output is eligible under the research evidence.
- Secrets are represented safely.
- Cross-device dependencies are accounted for.
- Verification and rollback requirements are documented.
- Unresolved issues are disclosed.

Do not represent partially validated work as production-ready.

---

## Current Vendor Addenda

Cisco:

`agents/cisco.md`

Fortinet:

`agents/fortinet.md`

Additional vendors should receive their own addendum under `agents/` and should
reuse `agents/shared-instructions.md` rather than duplicating the shared
research contract.
