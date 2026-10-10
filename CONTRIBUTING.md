# Contributing

ICTE-1 is a proposed profile. Changes should make a document easier to execute or review without deleting technical meaning.

## What to change together

[spec/ICTE-1.md](spec/ICTE-1.md) is canonical. When a rule, term, or example changes, update the specification and the companion file in the same commit:

| Change | Companion file |
|---|---|
| Writing rule, requirement word, or claim pattern | [rules/writing-rules.md](rules/writing-rules.md) |
| Domain checklist | [rules/domain-precision.md](rules/domain-precision.md) |
| Acceptance criterion or limitation | [rules/acceptance.md](rules/acceptance.md) |
| Term, verb, or false equivalence | [vocabulary/registry.yaml](vocabulary/registry.yaml) |
| Wording example | [examples/](examples/) |
| Assistant instruction | [prompts/](prompts/) |

## Term records

Add a term only when documents would otherwise use competing words for one concept, or when a word has a dangerous nearby meaning.

Use the record shape in [vocabulary/README.md](vocabulary/README.md). Do not add a meaning that the specification does not state. If the specification needs a new meaning, change the specification in the same commit.

Leave `owner` unset until a maintainer accepts accountability for that term.

## Do not

- Copy the ASD-STE100 dictionary, rule text, or issue PDF into this repository.
- Claim formal ASD-STE100 compliance, or claim that a prompt establishes compliance.
- Treat model output, a scan result, or a private deployment as proof of fact, security, or compliance.
- Invent prerequisites, timeouts, capacities, or expected results in examples. Mark missing information as `TBD` or unspecified.
- Let a writing rule override an approval, security, or change-management requirement.

## Review

A documentation change is ready when:

- Terms match the approved domain meanings.
- Actions identify their targets and relevant actors.
- Unknown information remains visibly unknown.
- A person who owns the technical content has reviewed correctness.

The next useful test of this draft is one architecture document, one operational runbook, and one AI tool specification. Use the mismatches to refine the vocabulary before expanding it.
