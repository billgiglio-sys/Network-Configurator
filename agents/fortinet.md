# Fortinet Research Agent Addendum

This file supplements `agents/shared-instructions.md`.

The shared instructions remain authoritative for repository usage, evidence
standards, lifecycle review, validation status, secret handling, testing,
configuration safety, Vendor Rules, and renderer eligibility.

This addendum defines requirements specific to Fortinet platforms.

## Scope

Research Fortinet products and software families represented by Network
Configurator, including as applicable:

- FortiGate
- FortiOS
- FortiSwitch
- FortiSwitchOS
- FortiAP
- FortiManager
- FortiAnalyzer
- FortiClient
- FortiExtender

Treat product families and management architectures as distinct unless
official Fortinet documentation establishes common behavior.

Do not assume FortiGate/FortiOS syntax applies to FortiSwitchOS or other
Fortinet operating systems.

## Authoritative Sources

Prioritize applicable official Fortinet sources:

- Fortinet Administration Guides
- FortiOS CLI Reference
- FortiSwitchOS CLI Reference
- Release Notes
- Compatibility documentation
- Product Data Sheets
- Fortinet Product Life Cycle information
- FortiManager documentation
- FortiAnalyzer documentation
- FortiAP documentation
- FortiClient documentation
- Upgrade documentation
- Fortinet PSIRT Advisories
- Known Issues documentation

Prefer documentation specific to the exact software release and product
over generic Fortinet feature documentation.

## FortiGate and FortiOS Applicability

For FortiGate research, establish applicable:

- FortiGate model
- Hardware generation
- FortiOS release
- Operating mode
- VDOM mode
- VDOM scope
- HA mode
- Central-management mode
- Feature visibility
- License/subscription dependencies
- Hardware-acceleration considerations

Do not generalize FortiOS CLI across release trains unless authoritative
documentation establishes applicability.

A command appearing in one FortiOS CLI reference does not establish that
the syntax or behavior is valid in another FortiOS release.

## Operating Mode

Determine whether behavior depends on:

- NAT mode
- Transparent mode

Do not assume a feature or configuration procedure supported in NAT mode
has identical behavior in transparent mode.

Record operating-mode scope in the Vendor Rule where material.

## VDOMs

Determine applicable:

- VDOM enabled/disabled state
- Root versus non-root VDOM scope
- Global versus VDOM configuration context
- Management VDOM behavior
- Inter-VDOM dependencies

Renderer output must place configuration in the correct FortiOS scope.

Do not treat global and VDOM configuration contexts as interchangeable.

## High Availability

For HA features or HA-sensitive changes, research applicable:

- HA mode
- Model compatibility
- Firmware compatibility
- Heartbeat interfaces
- Monitored interfaces
- Session synchronization
- Configuration synchronization
- Management access
- Failover implications
- Upgrade implications

Flag configuration that might trigger failover, resynchronization, or
management interruption.

## Interfaces and Hardware Acceleration

Research model-specific interface capabilities where material.

Check applicable:

- Physical interface type
- Supported speed
- Aggregate/LACP support
- VLAN interfaces
- Hardware switch/software switch behavior
- NP/CP/SPU acceleration
- Offload restrictions
- MTU restrictions
- Dedicated management interfaces
- FortiLink dependencies

Do not assume two FortiGate models expose identical physical ports or
hardware acceleration merely because the same FortiOS release supports a
feature.

## Firewall, NAT, and Inspection

Research applicable interactions involving:

- Firewall policy mode
- Policy order
- Source NAT
- IP pools
- VIPs/DNAT
- Central NAT
- Security profiles
- SSL inspection
- Application control
- IPS
- Session behavior
- Hardware offload

Do not mix central NAT and policy NAT semantics unless the rule explicitly
covers the requested operating model.

## Routing and SD-WAN

For routing and SD-WAN research, check applicable:

- Static routing
- Policy routes
- ECMP
- BGP
- OSPF
- VRF behavior
- SD-WAN members
- Zones
- Performance SLA
- Route interaction
- Administrative distance/priority
- Session impact
- Feature dependencies

Capture cross-device requirements for routing adjacencies and return paths.

## VPN

For IPsec and other VPN research, establish applicable:

- Route-based versus other supported models
- IKE version
- Peer type
- Authentication method
- Supported proposals
- DH groups
- Phase 2 behavior
- Routing dependencies
- DPD behavior
- NAT traversal
- Hardware acceleration
- Secret handling

Represent PSKs and other VPN credentials only through approved secret
references/placeholders.

## FortiManager

When a FortiGate may be centrally managed, research:

- FortiGate/FortiManager version compatibility
- ADOM version
- Device Manager behavior
- Policy package implications
- Provisioning-template behavior
- CLI/Jinja template applicability
- Local versus FortiManager-owned configuration
- Installation scope
- Revision/rollback implications

Do not assume a local FortiGate configuration workflow is operationally
equivalent when the FortiGate is under FortiManager management.

## FortiAnalyzer

Where logging or analytics is involved, determine:

- FortiGate/FortiAnalyzer compatibility
- Logging mode
- Reliable logging requirements
- Encryption requirements
- Registration/authorization requirements
- Storage or entitlement dependencies when material

## FortiSwitch and FortiAP

Determine whether devices are:

- Standalone
- FortiLink managed
- FortiGate managed
- FortiManager managed

For FortiAP, check applicable:

- AP model
- FortiOS/controller version
- Compatibility
- Regulatory domain
- SSID security
- VLAN mapping
- Authentication
- Client-impacting operations

Do not assume standalone FortiSwitch/FortiAP syntax applies to centrally
managed operation.

## Licensing and Entitlements

Research applicable:

- FortiCare
- FortiGuard subscriptions
- Security services
- Support entitlement
- Firmware entitlement
- Cloud-service dependencies

Explicitly distinguish:

- Feature requires entitlement
- Updates require entitlement
- Technical support requires entitlement
- Feature continues operating after subscription expiration

Do not describe a Fortinet entitlement as required unless official
documentation supports the claim.

## Feature Visibility

FortiOS GUI visibility does not by itself establish whether a feature is
supported.

When Feature Visibility affects the documented GUI workflow:

- Record the requirement.
- Distinguish hidden GUI features from unsupported features.
- Validate CLI availability independently when relevant.

## Lifecycle

Use official Fortinet Product Life Cycle information for lifecycle claims.

Check lifecycle before recommending hardware for new production deployment.

Do not recommend models that are End of Sale, End of Engineering Support,
End of Support, or otherwise unsuitable for new production deployment under
the repository lifecycle policy.

## Renderer Guidance

Fortinet renderer output must be scoped to the validated product family,
FortiOS release range, operating mode, and configuration context.

Use appropriate renderer families, for example:

- `fortios`
- `fortiswitchos`

Do not create a generic "Fortinet CLI" renderer.

Renderer eligibility follows `agents/shared-instructions.md`.

Legacy FortiGate builder output is migration reference material only and
must not be treated as authoritative syntax.

## Final Requirement

For Network Configurator research:

1. Apply `agents/shared-instructions.md`.
2. Apply this Fortinet addendum.
3. Read the current Vendor Rule schema from the repository.
4. Research the exact requested Fortinet target.
5. Produce or update repository artifacts only within permitted ownership
   boundaries.
6. Keep executable rendering disabled until the shared renderer eligibility
   requirements are satisfied.
