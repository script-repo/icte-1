# Terminology registry

[registry.yaml](registry.yaml) is the machine-readable starter vocabulary for ICTE-1 version 0.1.

It is not an exhaustive dictionary. It is not a quotation from ASD-STE100. A word list is not an ontology.

Canonical prose definitions are in [spec/ICTE-1.md](../spec/ICTE-1.md), section 4 and section 5. If a record disagrees with the specification, the specification wins.

## Record fields

| Field | Use |
|---|---|
| `id` | Stable identifier, `domain.term`. Do not reuse an id for a different concept. |
| `preferred_term` | The term to use in prose. |
| `part_of_speech` | `noun` or `verb` in this draft. |
| `domain` | `infrastructure`, `cloud`, `ai`, `gitops`, `devsecops`, or `platform`. Verbs use `action`. |
| `definition` | The controlled meaning from the specification. |
| `allowed_aliases` | Empty unless the specification permits an alias. |
| `avoid_as_synonyms` | Words that must not replace this term. |
| `related_terms` | Other preferred terms the specification discusses with this one. |
| `usage_rule` | An extra restriction. Omit when the definition already states the whole rule. |
| `example` | Optional. Use a sentence from the specification. Do not invent operational steps. |
| `owner` | Optional. Set only when a maintainer accepts the term. |

The sample record in specification section 9 uses `owner: platform-engineering` to show the field. That value is an illustration, not an assignment. This registry leaves `owner` unset.

## Requirement words

`requirement_words` records *must*, *must not*, *should*, *may*, and *can*. Those words are defined in section 3.2. They are not domain nouns.

## False equivalences

`non_equivalences` records prohibited shortcuts from the specification, such as "model output is not verified fact." Do not encode those as preferred terms.

## Ontology

`proposed_relations` copies the modeling statements from specification section 9.1. They are not a formal ontology until entity types and constraints exist.
