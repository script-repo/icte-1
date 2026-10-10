# Acceptance and limitations

Extract of ICTE-1 sections 11 and 12. Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md).

## A document passes this draft when

- Terms match the approved domain meanings.
- Actions identify their targets and relevant actors.
- Preconditions and success criteria are explicit.
- Destructive effects and recovery limits are stated.
- Product-specific claims identify applicable versions.
- Performance claims include measurement conditions.
- Unknown information remains visibly unknown.
- A technical owner has reviewed correctness.
- Exceptions to the writing rules are recorded.

## Version-controlled assets

Keep these three assets under version control:

1. The writing rules, in [rules/](.).
2. The terminology registry, in [vocabulary/registry.yaml](../vocabulary/registry.yaml).
3. The example documents, in [examples/](../examples/).

[spec/ICTE-1.md](../spec/ICTE-1.md) remains the canonical text. Separate maintenance is useful only while each companion stays aligned with that text. See [CONTRIBUTING.md](../CONTRIBUTING.md).

Treat automated linting as a language check, not proof of technical correctness.

## Next test

Test this draft against one architecture document, one operational runbook, and one AI tool specification. Use the review results to refine the vocabulary before expanding it into a larger dictionary.

## Limitations

- ICTE-1 is a proposed writing profile, not a published industry standard.
- The vocabulary is a starter set, not a complete replacement for the ASD-STE100 dictionary.
- The domain definitions are local usage conventions, not universal definitions across every vendor or standard.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- Examples are illustrative and require technical validation before operational use.
- A prompt alone cannot establish compliance with either ICTE-1 or ASD-STE100.
