# Terminology registry

[registry.yaml](registry.yaml) is the normative starter vocabulary for ICTE-1 version 0.2.

It is not an exhaustive dictionary. It is not a quotation from ASD-STE100. A word list is not an ontology.

The tables in [spec/ICTE-1.md](../spec/ICTE-1.md) sections 4 and 5 must match this file. If a table disagrees with a record, the record wins. Change the table in the same commit. [registry.schema.json](registry.schema.json) is the record schema. `tools/check_alignment.py` checks both.

## Record fields

| Field | Use |
|---|---|
| `id` | Stable identifier, `domain.term`. Do not reuse an id for a different concept. |
| `preferred_term` | The term to use in prose. |
| `part_of_speech` | `noun` or `verb`. |
| `domain` | `infrastructure`, `cloud`, `ai`, `gitops`, `devsecops`, `platform`, or `action`. Verbs use `action`. The noun `action` also uses `action`. |
| `definition` | The controlled meaning. |
| `allowed_aliases` | Empty unless the specification permits an alias. |
| `avoid_as_synonyms` | Words that must not replace this term. |
| `related_terms` | Other preferred terms that the writer should keep distinct. |
| `usage_rule` | An extra restriction. Required when the same preferred term is used in more than one domain. |
| `example` | Optional. Do not invent an operational step. |
| `owner` | Optional. Set only when a maintainer accepts the term. |

There is no `verbs` key. Approved verbs are objects in `terms`.

## Requirement words

`requirement_words` records *must*, *must not*, *should*, *may*, and *can*. Those words are defined in specification section 3.2. They are not RFC 2119, and they are not domain nouns.

`avoid_requirement_words` records *shall* and *will*. Do not use *shall*.

## False equivalences

`non_equivalences` are records with `id`, `relation`, `statement`, and `severity`. `left` is a term id when the claim is about a registered term. Otherwise set `left_text`. Do not store these only as bare sentences.

## Ontology

`proposed_relations.statements` are records with `id`, `left`, `relation`, and `right`. `left` and `right` are term ids. They are not a formal ontology until the types have constraints.
