# ICTE-1

**Infrastructure and Cloud Technical English**

Version 0.1 · Proposed independent specification · 2026-10-10

ICTE-1 is a writing profile for technical content about IT infrastructure, cloud, AI, GitOps, DevSecOps, and platform engineering. It combines controlled terminology, sentence-construction rules, and operational documentation requirements.

ICTE-1 is inspired by the aims of Simplified Technical English. It is **not** an official version of [ASD-STE100](https://www.asd-ste100.org/), it does **not** include the ASD-STE100 dictionary, and it does **not** establish ASD-STE100 compliance.

Simplify the language. Do not remove the architecture.

## What a reader must be able to identify

1. Which component performs an action.
2. Which resource the action affects.
3. Where the action occurs.
4. Which conditions must be true.
5. What result to expect.
6. How to detect failure.
7. How to recover.

## Repository layout

The canonical text is [spec/ICTE-1.md](spec/ICTE-1.md). The other paths are the three version-controlled assets named in that specification, plus paste-ready prompts and document patterns.

| Path | Role |
|---|---|
| [spec/ICTE-1.md](spec/ICTE-1.md) | Canonical specification. If a companion file disagrees with it, the specification wins. |
| [rules/](rules/) | Writing rules, domain precision checks, and acceptance criteria. |
| [vocabulary/registry.yaml](vocabulary/registry.yaml) | Machine-readable starter terminology. |
| [examples/](examples/) | Before-and-after wording. Illustrative only. Not executable procedures. |
| [templates/](templates/) | Runbook, architecture, and AI tool description patterns. |
| [prompts/](prompts/) | Copy-ready instructions for a writing assistant. |

## Requirement words

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Do not use *shall*. Do not use *will* to imply a guarantee unless the behavior is established and its conditions are stated.

## Scope

Apply ICTE-1 to architecture descriptions, deployment guides, runbooks, infrastructure-as-code documentation, GitOps workflows, security controls, AI model-serving and agent workflows, platform service definitions, and technical proposals.

Do not apply prose restrictions to commands, source code, API identifiers, configuration keys, logs, or quoted source material.

## Status

This is a draft profile, not a published industry standard.

- The vocabulary is a starter set, not a replacement for the ASD-STE100 dictionary.
- Domain definitions are local usage conventions, not universal vendor definitions.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- A prompt alone cannot establish compliance with ICTE-1 or with ASD-STE100.
- Automated language checks are not proof of technical correctness.

## License

The text in this repository is licensed under [CC BY 4.0](LICENSE). ASD-STE100 and other third-party standards remain the property of their owners. This repository does not grant rights to them.
