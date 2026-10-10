# Acceptance and limitations

Extract of ICTE-1 sections 11 and 12. Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md). If this file disagrees with the specification, the specification wins.

A review records three results. One result does not imply another.

## Language result

The language result passes when all of the following are true:

- Terms match the approved meanings in the registry.
- Actions identify their targets and the actors that matter.
- Requirement words match section 3.2.
- Every required rule that the document breaks has a recorded exception.
- Unknown information remains visibly unknown.
- The document does not assert a prohibited equivalence from section 4.3.

Advisory rules, including L04, are reported. An advisory miss does not fail the language result. Record the miss when the writer kept the longer sentence in order to keep the meaning.

## Operational completeness

Operational completeness passes when both of the following are true:

- Each item in the section 6 checklist for that document type is stated, or marked not applicable.
- Each field in the matching section 7 pattern is filled, or marked not applicable.

## Technical review

Technical review passes only when a named owner of the technical content has reviewed correctness. This profile cannot record that result by itself. A language result is not a technical review. Operational completeness is not a technical review.

## Normative sources

| Subject | Normative source |
|---|---|
| Writing rules | [spec/ICTE-1.md](../spec/ICTE-1.md) section 3 |
| Domain checklists | [spec/ICTE-1.md](../spec/ICTE-1.md) section 6 |
| Term records | [vocabulary/registry.yaml](../vocabulary/registry.yaml) |
| Assistant instructions | [spec/ICTE-1.md](../spec/ICTE-1.md) section 10 |
| Document patterns | [spec/ICTE-1.md](../spec/ICTE-1.md) section 7 |

`tools/check_alignment.py` must pass before a change is complete. The checker is a language-alignment check. It is not proof of technical correctness, and it is not a language result for an arbitrary document.

## Next test

The in-repo sample [examples/sample-runbook.md](../examples/sample-runbook.md) has a section 11 score. Language passes with the recorded `upgrade` exception. Operational completeness passes because missing facts are `TBD` or not applicable. Technical review does not pass: no named owner has reviewed it.

A document from outside this repository has not been scored. Score one real architecture document and one real AI tool specification the same way. Use the mismatches to refine the vocabulary. Do not expand the dictionary first.

## Limitations

- ICTE-1 is a proposed writing profile, not a published industry standard.
- The vocabulary is a starter set, not a complete replacement for the ASD-STE100 dictionary.
- The domain definitions are local usage conventions, not universal definitions across every vendor or standard.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- A language result does not establish operational completeness or technical review.
- Examples are illustrative and require technical validation before operational use.
- A prompt alone cannot establish compliance with either ICTE-1 or ASD-STE100.
- Automated alignment checks are not proof that a document is correct.
