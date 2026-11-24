# Network Configurator Agent Instructions

This directory contains the instruction hierarchy for research agents that
contribute vendor knowledge, validation rules, and renderer support to
Network Configurator.

The goal is to give every vendor agent the same research, evidence, safety,
testing, and contribution standards while preserving vendor-specific
technical expertise.

---

## Instruction Structure

Agent instructions are intentionally layered:

```text
Repository root
│
├── AGENTS.md
│     Repository governance, ownership, branching,
│     contribution sequence, and bootstrap rules
│
└── agents/
      │
      ├── README.md
      │     This file
      │
      ├── shared-instructions.md
      │     Common research, evidence, validation,
      │     safety, testing, and renderer requirements
      │
      ├── cisco.md
      │     Cisco-specific research requirements
      │
      └── fortinet.md
            Fortinet-specific research requirements
