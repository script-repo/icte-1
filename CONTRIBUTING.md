# Contributing

ICTE-1 is a proposed profile. Changes should make a document easier to execute or review without deleting technical meaning.

## Normative sources

| Subject | Normative source | Also update |
|---|---|---|
| Writing rule, requirement word, or claim pattern | [spec/ICTE-1.md](spec/ICTE-1.md) section 3 | [rules/writing-rules.md](rules/writing-rules.md) |
| Domain checklist | [spec/ICTE-1.md](spec/ICTE-1.md) section 6 | [rules/domain-precision.md](rules/domain-precision.md) |
| Acceptance criterion or limitation | [spec/ICTE-1.md](spec/ICTE-1.md) sections 11 and 12 | [rules/acceptance.md](rules/acceptance.md) |
| Term, verb, false equivalence, or relation | [vocabulary/registry.yaml](vocabulary/registry.yaml) | Sections 4, 5, and 9 of the specification |
| Document pattern | [spec/ICTE-1.md](spec/ICTE-1.md) section 7 | [templates/](templates/) |
| Assistant instruction | [spec/ICTE-1.md](spec/ICTE-1.md) section 10 | [prompts/](prompts/) |
| Wording example | [spec/ICTE-1.md](spec/ICTE-1.md) section 8 | [examples/](examples/) |

If a prose copy disagrees with the specification, the specification wins. If a term table disagrees with the registry, the registry wins for that record. Update the other file in the same commit.

Run this before you finish:

```bash
pip install pyyaml jsonschema
python tools/check_alignment.py
```

## Term records

Add a term only when documents would otherwise use competing words for one concept, or when a word has a dangerous nearby meaning.

Put every term, including verbs, in `terms`. A verb uses `part_of_speech: verb` and `domain: action`. Do not add a `verbs` key.

Use the record shape in [vocabulary/README.md](vocabulary/README.md) and [vocabulary/registry.schema.json](vocabulary/registry.schema.json). A proposed relation must point `left` and `right` at term ids.

Leave `owner` unset until a maintainer accepts accountability for that term.

## Do not

- Copy the ASD-STE100 dictionary, rule text, or issue PDF into this repository.
- Claim formal ASD-STE100 compliance, or claim that a prompt establishes compliance.
- Treat model output, a scan result, or a private deployment as proof of fact, security, or compliance.
- Invent prerequisites, timeouts, capacities, or expected results in examples. Mark missing information as `TBD` or `not applicable`.
- Let a writing rule override an approval, security, or change-management requirement.
- Change a procedure's order or actor in order to make a sentence shorter.

## Review

A documentation change is ready when the checker passes and:

- Terms match the approved meanings.
- Actions identify their targets and the actors that matter.
- Unknown information remains visibly unknown.
- A person who owns the technical content has reviewed correctness, when the change states operational facts.

The in-repo sample runbook has a section 11 score. A document from outside this repository has not been scored. The next useful test is one real architecture document and one real AI tool specification. Use the mismatches to refine the vocabulary before expanding it.
