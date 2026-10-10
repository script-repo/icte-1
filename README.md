# ICTE-1

**Infrastructure and Cloud Technical English**

Version 0.2 · Proposed independent specification · 2026-10-10

ICTE-1 is a writing profile for technical content about IT infrastructure, cloud, AI, GitOps, DevSecOps, and platform engineering. It combines controlled terminology, sentence-construction rules, and operational documentation requirements.

Write for a technical reader who can execute the procedure or review it, including a reader who does not already know the product.

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

## Three review results

A review records three results. One does not imply another. See [spec/ICTE-1.md](spec/ICTE-1.md) section 11.

| Result | What passes |
|---|---|
| Language | Terms, actors, requirement words, and required rules. Advisory misses, including the sentence-length target, do not fail this result. |
| Operational completeness | Each checklist item and pattern field is stated, or marked not applicable. |
| Technical review | A named owner of the content has reviewed correctness. The profile cannot record this by itself. |

## Repository layout

| Path | Role |
|---|---|
| [spec/ICTE-1.md](spec/ICTE-1.md) | Normative prose: rules, checklists, patterns, prompts, and limitations. |
| [vocabulary/registry.yaml](vocabulary/registry.yaml) | Normative term records. Sections 4 and 5 of the spec must match it. Schema: [registry.schema.json](vocabulary/registry.schema.json). |
| [rules/](rules/) | Copies of the writing rules, domain checks, and acceptance criteria. |
| [examples/](examples/) | Before-and-after wording and worked samples. Illustrative only. Not executable procedures. |
| [templates/](templates/) | Runbook, architecture, AI tool, and model-serving patterns. |
| [prompts/](prompts/) | Copies of the section 10 instructions. |
| [tools/check_alignment.py](tools/check_alignment.py) | Fails when a copy drifts from its normative source. |

If a prose copy disagrees with the specification, the specification wins. If a term table disagrees with the registry, the registry wins for that record. Change both in the same commit. Do not delete technical meaning to silence the checker.

## Requirement words

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Do not use *shall*. Do not use *will* to imply a guarantee unless the behavior is established and its conditions are stated. These words are not RFC 2119.

## Check

```bash
pip install pyyaml jsonschema
python tools/check_alignment.py
```

The checker is an alignment check. It is not a language result for an arbitrary document, and it is not proof of technical correctness.

## Scope

Apply ICTE-1 to architecture descriptions, deployment guides, runbooks, infrastructure-as-code documentation, GitOps workflows, security controls, AI model-serving and agent workflows, platform service definitions, and technical proposals.

Do not apply prose restrictions to commands, source code, API identifiers, configuration keys, logs, or quoted source material.

## Status

This is a draft profile, not a published industry standard.

- The vocabulary is a starter set, not a replacement for the ASD-STE100 dictionary.
- Domain definitions are local usage conventions, not universal vendor definitions.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- A prompt alone cannot establish compliance with ICTE-1 or with ASD-STE100.
- A language result does not establish operational completeness or technical review.

## License

The text in this repository is licensed under [CC BY 4.0](LICENSE). ASD-STE100 and other third-party standards remain the property of their owners. This repository does not grant rights to them.
