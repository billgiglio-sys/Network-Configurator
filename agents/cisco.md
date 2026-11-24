# Cisco Research Agent Addendum

This file supplements `agents/shared-instructions.md`.

The shared instructions remain authoritative for repository usage, evidence
standards, lifecycle review, validation status, secret handling, testing,
configuration safety, Vendor Rules, and renderer eligibility.

This addendum defines requirements specific to Cisco platforms.

## Scope

Research Cisco products and software families represented by Network
Configurator, including as applicable:

- Cisco IOS
- Cisco IOS-XE
- Cisco NX-OS
- Cisco AireOS
- Cisco Catalyst 9800 wireless
- Cisco ASA
- Cisco Secure Firewall / FTD
- Cisco FMC-managed platforms
- Cisco Meraki when explicitly represented by the project

Never assume that syntax, licensing, capabilities, defaults, or operational
behavior documented for one Cisco operating system or architecture applies
to another.

Treat these as distinct implementation families unless authoritative
documentation establishes otherwise.

## Authoritative Sources

Prioritize applicable official Cisco sources:

- Configuration Guides
- Command References
- Release Notes
- Cisco Feature Navigator
- Compatibility Matrices
- Software Download documentation
- Product Data Sheets
- Licensing Guides
- Cisco Validated Designs
- Field Notices
- Security Advisories
- End-of-Life and End-of-Sale Notices
- API and YANG documentation

Prefer documentation specific to the exact platform and release over a
generic Cisco feature description.

## Platform and Software Applicability

Record applicable:

- Exact PID or supported PID family
- Hardware generation
- Operating-system family
- Software train and release
- Supervisor or stack architecture
- Boot/install mode when relevant
- License level
- Controller dependency
- Managed versus standalone operation

Do not generalize IOS, IOS-XE, NX-OS, AireOS, or Catalyst 9800 behavior.

Do not generalize syntax between Catalyst product generations without
evidence.

## IOS-XE

When researching IOS-XE, check applicable:

- Hardware platform
- IOS-XE release train
- Minimum or excluded releases
- Install versus bundle mode where relevant
- ROMMON or bootloader dependencies
- StackWise requirements
- StackWise Virtual requirements
- ISSU and reload implications
- Network Essentials versus Network Advantage requirements
- Subscription dependencies where documented
- Feature interactions introduced or removed by release

A command appearing in an IOS-XE command reference is not sufficient by
itself to establish support on every IOS-XE platform.

## Switching

For switching features, research applicable:

- Layer-2 versus Layer-3 port mode
- VLAN requirements
- Access/trunk behavior
- Native VLAN behavior
- Allowed VLAN behavior
- EtherChannel/LACP requirements
- Port-channel member restrictions
- Stack behavior
- STP mode and interaction
- PortFast/edge behavior
- Storm-control and security interactions
- SVI requirements
- MTU constraints
- Hardware forwarding limitations

Record cross-device requirements where configuration must agree at both
ends of a link.

## Routing

For routing features, research applicable:

- Required license level
- VRF behavior
- Address-family support
- Routing-process restrictions
- Maximum supported scale when material
- Redistribution behavior
- Administrative-distance defaults when relevant
- Authentication requirements
- Graceful restart or NSF behavior
- Adjacency disruption resulting from changes

Do not assume equivalent behavior across IOS-XE and NX-OS.

## Wireless

Treat AireOS and Catalyst 9800 IOS-XE as separate architectures.

For wireless research, check applicable:

- Controller model
- Controller software release
- AP model
- AP/controller compatibility
- Regulatory domain
- WLAN configuration model
- Policy profile
- Policy tag
- Site tag
- RF tag
- VLAN mapping
- AAA dependencies
- WPA/WPA2/WPA3 mode
- Protected Management Frames requirements
- Cipher requirements
- Client-impacting changes
- AP rejoin requirements

Do not translate AireOS commands or concepts directly into Catalyst 9800
configuration without authoritative evidence.

## Optics and Modules

Where physical interfaces depend on transceivers or modules, check:

- Exact switch/router PID
- Network module
- Transceiver PID
- Supported speed
- Breakout requirements
- DOM support when relevant
- Minimum software release
- Compatibility restrictions

Do not infer optic compatibility merely from matching physical connector
or wavelength.

## Licensing

Establish licensing from official Cisco documentation.

Potential licensing dimensions include:

- Network Essentials
- Network Advantage
- DNA Essentials
- DNA Advantage
- Smart Licensing
- Subscription requirements
- Controller licensing
- Security feature licensing

Do not mark a Cisco subscription or license as required unless official
documentation explicitly establishes the dependency for the researched
feature and scope.

## Lifecycle

Use Cisco End-of-Life and End-of-Sale notices for lifecycle claims.

Record applicable milestones required by the current Vendor Rule schema.

Do not treat a replacement platform as authoritative unless Cisco
identifies it or the recommendation is explicitly marked as engineering
judgment rather than vendor guidance.

## Renderer Guidance

Cisco renderer output must be scoped to the validated operating system,
platform, and software range.

Do not create a generic "Cisco CLI" renderer.

Use distinct renderer families where architecture or syntax materially
differs, for example:

- `iosxe`
- `nxos`
- `aireos`
- `catalyst9800`

Renderer eligibility follows `agents/shared-instructions.md`.

## Final Requirement

For Network Configurator research:

1. Apply `agents/shared-instructions.md`.
2. Apply this Cisco addendum.
3. Read the current Vendor Rule schema from the repository.
4. Research the exact requested Cisco target.
5. Produce or update repository artifacts only within permitted ownership
   boundaries.
6. Keep executable rendering disabled until the shared renderer eligibility
   requirements are satisfied.
