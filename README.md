# Network Configurator

A local-first, multi-device network design, validation, and configuration compiler for Cisco and Fortinet platforms.

## Goals

- Define network intent once across an entire customer deployment.
- Validate addressing, topology, lifecycle, compatibility, licensing, and cross-device dependencies.
- Render platform/version-specific configurations through vendor plugins.
- Produce per-device configuration files and a complete delivery bundle.
- Preserve authoritative vendor-source provenance for every renderer rule.

## Initial platform scope

### Cisco
- Catalyst 3850 on IOS-XE Gibraltar 16.12.x
- Catalyst 9300/9300L on IOS-XE 17.x
- Catalyst 8300 on IOS-XE 17.x
- Cisco 3504 Wireless Controller on AireOS 8.10.196.0
- Catalyst 9130AX access points
- Catalyst 9800 wireless controllers

### Fortinet
- The original FortiGate Config Builder is preserved under `legacy/fortigate-builder/`.
- FortiOS renderer migration begins with FortiOS 7.4.

## Repository structure

- `agents/`: shared and vendor-specific research-agent instructions
- `schemas/`: JSON Schemas for projects and evidence-backed Vendor Rules
- `catalog/`: platform, release, capability, compatibility, and lifecycle data
- `research/`: reviewed Vendor Rule YAML files with official-source provenance
- `renderers/`: Jinja configuration renderers
- `validators/`: common and vendor-specific validators
- `app/`: FastAPI backend and web frontend
- `examples/`: example multi-device projects
- `tests/`: schema, catalog, renderer, and validator tests
- `legacy/`: preserved working prototypes used during migration

## Quick start

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.backend.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Development rule

No vendor-specific configuration syntax is renderer-eligible until the applicable platform, software release, prerequisites, verification, rollback, and official sources are represented in a reviewed Vendor Rule.
