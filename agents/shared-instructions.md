# Network Configurator Shared Research Instructions

## Purpose

Research and document vendor-specific capabilities, syntax, compatibility, licensing, lifecycle, verification, rollback, and deployment requirements for Network Configurator.

Network Configurator maintains vendor-neutral network intent and uses evidence-backed Vendor Rules, validators, and vendor-specific renderers to generate device configurations.

Research agents provide authoritative knowledge for:

- Platform and software catalogs
- Feature and capability rules
- Compatibility constraints
- Licensing and entitlement requirements
- Lifecycle warnings
- Validators
- Renderer implementation
- Cross-device validation
- Verification and rollback procedures

Research agents do not own the vendor-neutral application architecture.

---

## 1. Repository Authority

The `main` branch is the authoritative current state of Network Configurator.

Repository content supersedes previous conversations, copied schemas, old examples, and agent memory.

Before project work:

1. Read `AGENTS.md`.
2. Read this file.
3. Read the applicable vendor addendum under `agents/`.
4. Inspect applicable schemas.
5. Inspect relevant catalog entries and existing Vendor Rules.
6. Inspect affected renderers and validators.
7. Inspect relevant examples and tests.
8. Only then propose or implement changes.

Use the connected repository source when available. Do not substitute web-indexed copies or conversational copies for repository contents.

Do not assume access to another agent's conversation or private context.

**Agents collaborate through repository artifacts.**

---

## 2. Ownership and Changes

Follow ownership boundaries defined by `AGENTS.md`.

Vendor-specific changes belong under that vendor's catalog, research, renderer, and validator paths.

Treat shared areas such as schemas, common validators, application code, examples, and shared tests as core components.

Do not modify the common model merely to mirror vendor CLI. Use vendor extensions for genuinely vendor-specific constructs.

If research reveals a legitimate deficiency in a shared contract, document it and propose a separate core change.

Use feature branches:

- `cisco/<feature>`
- `fortinet/<feature>`
- `core/<feature>`

Keep changes scoped to the assigned feature.

---

## 3. Research the Exact Target

Identify applicable:

- Vendor
- Product family
- Model or supported model set
- Hardware revision when relevant
- Operating-system family
- Software release or bounded release family
- Operating mode
- HA, stack, chassis, or clustering mode
- Virtualization or tenancy mode
- License/subscription/support entitlement
- Management method
- Feature
- Relevant peers and dependencies

Do not silently substitute or generalize across platforms, operating systems, releases, or modes.

Ask for clarification only when missing information materially changes syntax, compatibility, licensing, security, operational risk, or renderer output.

Where research can safely cover a documented release family, state the assumption explicitly.

---

## 4. Evidence Standard

Use official vendor sources first:

- Administration/configuration guides
- CLI command references
- API or YANG references
- Release notes
- Feature/compatibility matrices
- Data sheets
- Licensing guides
- Upgrade/downgrade guides
- Validated designs
- Security advisories
- Field notices
- Lifecycle/EOS/EOL notices

Unofficial sources may help identify issues but must not be the sole evidence for a validated rule.

Preserve source provenance required by the current Vendor Rule schema.

Do not invent URLs, section names, publication dates, applicability, or other source metadata.

When official sources conflict:

1. Prefer documentation specific to the exact platform and release.
2. Prefer applicable release notes for release-specific behavior.
3. Record the conflict.
4. Reduce validation status when unresolved.
5. Make the renderer ineligible if the conflict affects generated configuration.
6. Recommend lab validation or vendor confirmation when necessary.

---

## 5. Validation Status

Use only statuses defined by the current Vendor Rule schema, including:

- `validated`
- `partially_validated`
- `unverified`
- `unsupported`
- `conflicting_documentation`

A rule is `validated` only when authoritative evidence establishes required platform/software applicability, prerequisites, behavior, and any executable syntax supplied.

Never produce plausible-looking executable syntax from memory and mark it validated.

If exact syntax or its applicability cannot be established, reduce the status and make executable rendering ineligible.

---

## 6. Intent vs. Implementation

Keep vendor-neutral intent separate from vendor implementation.

Intent describes **what the network must accomplish**.

Vendor Rules and renderers describe **how a specific platform implements that intent**.

Do not place vendor CLI in vendor-neutral intent.

Do not change common intent solely because one vendor implements a feature differently.

---

## 7. Required Research Scope

Research applicable dimensions for every feature.

### Platform

- Supported families/models
- Hardware restrictions
- Supported software releases
- Operating-mode restrictions
- Scale limits
- Unsupported combinations

### Licensing and Entitlement

- Required license/tier
- Subscription requirements
- Support entitlement
- Feature entitlement
- Expiration behavior
- Whether existing configuration continues operating after expiration

Do not claim a licensing requirement without authoritative evidence.

### Compatibility

Evaluate relevant:

- Controllers and managed devices
- HA/stack/cluster peers
- AP/controller relationships
- Optics/modules
- Firmware/bootloader
- Management platforms
- AAA systems
- API versions
- Cryptographic requirements
- Neighboring devices
- Feature interoperability

### Configuration

Research:

- Prerequisites
- Sequence
- Exact CLI
- Official GUI procedure when available
- API/YANG models when relevant
- Defaults
- Version differences
- Disruptive actions
- Reload/reboot requirements

### Verification

Provide applicable:

- Pre-change checks
- Post-change commands
- Expected successful results
- Status/counter/log checks
- Failure indicators
- Troubleshooting commands

### Rollback

Document applicable:

- Removal/reversal commands
- Backup/checkpoint requirements
- Restoration procedure
- Reload implications
- HA/stack implications
- Management-access risks

---

## 8. Lifecycle

Check lifecycle status when applicable.

Research relevant milestones such as:

- End of Sale
- End of Software Maintenance
- End of Security/Vulnerability Support
- Last Date of Support

Apply lifecycle policy defined by the repository.

Do not recommend an obsolete platform for a new production deployment unless explicitly required and the risk is clearly identified.

Obsolete platforms may still be researched for existing deployments, migration, recovery, development, or lab use.

---

## 9. Multi-Device Awareness

Network Configurator models complete deployments, not isolated devices.

Record cross-device dependencies such as:

- VLAN consistency across trunks and gateways
- Native/untagged VLAN consistency
- DHCP relay/server reachability
- Routing adjacency and return paths
- Link-aggregation compatibility
- MTU consistency
- Firewall policy dependencies
- AAA/DNS/NTP/syslog reachability
- AP/controller compatibility
- WLAN-to-VLAN mapping
- HA/stack requirements

Express dependencies as Vendor Rule compatibility requirements and validation rules where safe.

---

## 10. Validation Rules

Use only operators and structures supported by the current Vendor Rule schema.

Do not invent new machine operators for conditions the validator cannot safely express.

If a condition cannot be safely encoded, identify it as a manual-review requirement.

A manual check is preferable to an incorrect automated rule.

---

## 11. Renderer Eligibility

Be conservative.

Set renderer eligibility true only when the current repository contract is satisfied, including applicable:

- Exact syntax validation
- Platform scope
- Software scope
- Operating mode
- Required inputs
- Dependencies
- Secret handling
- Verification
- Rollback
- Absence of unresolved conflicts affecting generated commands

A supported capability is not automatically renderer-eligible.

When required evidence is incomplete, record the research but keep executable rendering disabled.

---

## 12. Testing Before Rendering

Do not change a renderer before adding or updating applicable tests.

Preferred sequence:

1. Vendor research
2. Vendor Rule
3. Validation behavior
4. Test fixture/expected behavior
5. Renderer implementation
6. Golden-output validation

Where applicable include:

- Positive tests
- Negative/unsupported tests
- Version-boundary tests
- Secret-placeholder tests
- Golden configurations

Legacy configurations may inform research but are not authoritative evidence.

---

## 13. Secrets and Customer Data

Never commit real:

- Passwords
- PSKs
- TACACS/RADIUS secrets
- SNMP credentials
- API tokens
- Private keys
- Customer certificates
- Customer credentials
- Proprietary customer configurations

Use external references or placeholders supported by the current schema, such as:

`${IPSEC_PSK}`

`${TACACS_SHARED_SECRET}`

`${SNMPV3_AUTH_PASSWORD}`

Never use production/customer secrets as research examples or test fixtures.

---

## 14. Configuration Safety

Identify actions that may:

- Interrupt management access
- Restart services/processes
- Reload/reboot devices
- Trigger HA/stack elections
- Cause AP rejoins
- Disconnect clients
- Flush sessions
- Replace running configuration
- Modify boot behavior
- Change addressing
- Reset routing adjacencies
- Affect STP
- Alter firewall-policy evaluation
- Disable security controls

For disruptive changes document applicable:

- Expected impact
- Maintenance-window recommendation
- Backup/checkpoint
- Out-of-band access recommendation
- Verification checkpoint
- Rollback trigger
- Rollback procedure

---

## 15. Research Deliverable

For Network Configurator research return:

### Research Result

- Feature
- Vendor
- Target platform/model
- Software scope
- Operating mode
- Validation status
- Confidence
- License/entitlement requirements
- Operational risk
- Renderer eligibility

### Important Findings

Summarize material:

- Version behavior
- Platform limitations
- Compatibility constraints
- Lifecycle concerns
- Disruption
- Manual-review requirements

### Vendor Rule

Produce a machine-readable Vendor Rule conforming to the **current schema in the repository**.

Never rely on a schema version remembered from conversation.

### Unresolved Items

List only genuine gaps affecting validation, compatibility, renderer eligibility, or safe deployment.

### Official Sources

Provide authoritative sources supporting material claims.

---

## 16. Quality Gate

Before submitting research or enabling a renderer, verify:

- [ ] Vendor and product family are correct.
- [ ] Models are explicit.
- [ ] OS/software scope is explicit.
- [ ] Operating mode is explicit where relevant.
- [ ] Licensing claims have authoritative support.
- [ ] Lifecycle has been checked.
- [ ] Executable syntax is officially supported for the stated scope.
- [ ] GUI steps are included only when documented.
- [ ] Verification is documented.
- [ ] Rollback is documented.
- [ ] Disruption risks are identified.
- [ ] Cross-device dependencies are recorded.
- [ ] Secrets use references/placeholders.
- [ ] Material claims map to authoritative sources.
- [ ] Unverified syntax is not marked validated.
- [ ] Renderer eligibility is conservative.
- [ ] Unresolved gaps are disclosed.
- [ ] Applicable tests exist or are proposed.
- [ ] Output conforms to the repository's current Vendor Rule schema.

If a required item cannot be established, reduce validation status, renderer eligibility, or both.

---

## 17. Vendor Addenda

After these shared instructions, follow the applicable vendor-specific addendum under `agents/`.

Vendor addenda may define additional platform-specific research requirements, but must not weaken:

- Repository authority
- Official-source requirements
- Exact version/platform applicability
- Lifecycle review
- Secret handling
- Safety requirements
- Testing requirements
- Conservative renderer eligibility
- Vendor Rule schema compliance

When shared and vendor-specific instructions genuinely conflict because of a platform-specific requirement, document the issue rather than silently weakening the shared contract.
