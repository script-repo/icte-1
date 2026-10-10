#!/usr/bin/env python3
"""Check ICTE-1 companions against the normative sources.

The specification is normative for prose rules, checklists, patterns,
and prompts. vocabulary/registry.yaml is normative for term records.
This script fails if a copy drifts. It does not judge an arbitrary
document, and it does not prove technical correctness.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "spec" / "ICTE-1.md"
REG_PATH = ROOT / "vocabulary" / "registry.yaml"

DOMAINS = {
    "infrastructure",
    "cloud",
    "ai",
    "gitops",
    "devsecops",
    "platform",
    "action",
}
ID_RE = re.compile(r"^[a-z0-9]+(?:\.[a-z0-9_]+)+$")
SAMPLES = [
    "examples/sample-runbook.md",
    "examples/sample-architecture.md",
    "examples/sample-ai-tool.md",
    "examples/sample-model-serving.md",
]
TEMPLATES = {
    "7.1": "templates/runbook.md",
    "7.2": "templates/architecture.md",
    "7.3": "templates/ai-tool.md",
    "7.4": "templates/model-serving.md",
}


def norm(text: str) -> str:
    return " ".join(str(text).split())


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def tables(md: str) -> list[tuple[list[str], list[list[str]]]]:
    lines = md.splitlines()
    found = []
    i = 0
    while i < len(lines):
        if (
            lines[i].startswith("|")
            and i + 1 < len(lines)
            and re.match(r"^\|[\s:|-]+\|$", lines[i + 1])
        ):
            header = split_row(lines[i])
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            found.append((header, rows))
        else:
            i += 1
    return found


def between(md: str, start: str, end: str) -> str:
    if start not in md or end not in md:
        raise CheckError(f"missing section bounds {start!r} .. {end!r}")
    return md.split(start, 1)[1].split(end, 1)[0]


def fenced_text(block: str) -> list[str]:
    fences = []
    current = []
    inside = False
    for line in block.splitlines():
        if line.startswith("```"):
            if inside:
                fences.append("\n".join(current))
                current = []
            inside = not inside
            continue
        if inside:
            current.append(line)
    if inside:
        raise CheckError("unclosed fence")
    return fences


def prompt_body(md: str, label: str) -> str:
    start = f"<!-- prompt:{label} -->"
    end = f"<!-- /prompt:{label} -->"
    body = between(md, start, end)
    chunks = fenced_text(body)
    if len(chunks) != 1:
        raise CheckError(f"prompt {label} has {len(chunks)} fences")
    return chunks[0].strip() + "\n"


class CheckError(Exception):
    pass


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def fail(self, message: str) -> None:
        self.errors.append(message)

    def ok(self) -> bool:
        return not self.errors


def check_registry(reg: dict, report: Report) -> dict[str, dict]:
    if "verbs" in reg:
        report.fail("registry has a verbs key; verbs belong in terms")
    if str(reg.get("version")) != "0.2":
        report.fail(f"registry version is {reg.get('version')!r}, expected 0.2")
    terms = reg.get("terms")
    if not isinstance(terms, list) or not terms:
        report.fail("registry terms must be a non-empty list")
        return {}
    by_id: dict[str, dict] = {}
    by_term: dict[str, list[dict]] = {}
    for term in terms:
        tid = term.get("id")
        if not isinstance(tid, str) or not ID_RE.match(tid):
            report.fail(f"bad term id: {tid!r}")
            continue
        if tid in by_id:
            report.fail(f"duplicate term id: {tid}")
        by_id[tid] = term
        for field in ("preferred_term", "part_of_speech", "domain", "definition"):
            if not str(term.get(field, "")).strip():
                report.fail(f"{tid} missing {field}")
        if term.get("part_of_speech") not in {"noun", "verb"}:
            report.fail(f"{tid} bad part_of_speech")
        if term.get("domain") not in DOMAINS:
            report.fail(f"{tid} bad domain {term.get('domain')!r}")
        if term.get("part_of_speech") == "verb" and term.get("domain") != "action":
            report.fail(f"{tid} verb must use domain action")
        if term.get("domain") == "action" and term.get("part_of_speech") == "noun":
            if tid != "action.named_action":
                report.fail(f"{tid} is an unexpected noun in domain action")
        for list_field in ("allowed_aliases", "avoid_as_synonyms", "related_terms"):
            if list_field in term and not isinstance(term[list_field], list):
                report.fail(f"{tid} {list_field} must be a list")
        by_term.setdefault(term["preferred_term"], []).append(term)
    for preferred, group in by_term.items():
        if len(group) > 1:
            for term in group:
                if not str(term.get("usage_rule", "")).strip():
                    report.fail(
                        f"{term['id']} repeats {preferred!r} and has no usage_rule"
                    )
    return by_id


def check_relations(reg: dict, by_id: dict[str, dict], spec: str, report: Report) -> None:
    rows = reg.get("non_equivalences")
    if not isinstance(rows, list) or len(rows) < 6:
        report.fail("non_equivalences must be a list of records")
        return
    for row in rows:
        rid = row.get("id")
        if not isinstance(rid, str) or not ID_RE.match(rid):
            report.fail(f"bad non_equivalence id {rid!r}")
            continue
        for field in ("relation", "statement", "severity"):
            if not str(row.get(field, "")).strip():
                report.fail(f"{rid} missing {field}")
        if row.get("severity") not in {"required", "advisory"}:
            report.fail(f"{rid} bad severity")
        if "left" in row and row["left"] not in by_id:
            report.fail(f"{rid} left is not a term id")
        if "left" not in row and not str(row.get("left_text", "")).strip():
            report.fail(f"{rid} needs left or left_text")
        statement = row.get("statement", "")
        if statement and statement not in spec:
            report.fail(f"{rid} statement is not in the specification")
    relations = reg.get("proposed_relations", {})
    statements = relations.get("statements") if isinstance(relations, dict) else None
    if not isinstance(statements, list) or len(statements) < 5:
        report.fail("proposed_relations.statements must be records")
        return
    expected = {
        "rel.gitops.reconciles": ("gitops.controller", "gitops.managed_resource"),
        "rel.ai.serves": ("ai.inference_server", "ai.model_version"),
        "rel.ai.invokes": ("ai.agent", "ai.tool"),
        "rel.devsecops.constrains": ("devsecops.policy", "action.named_action"),
        "rel.platform.has_owner": ("platform.platform_service", "platform.service_owner"),
    }
    seen = {}
    for row in statements:
        rid = row.get("id")
        left, right = row.get("left"), row.get("right")
        if left not in by_id or right not in by_id:
            report.fail(f"{rid} endpoints are not term ids: {left} -> {right}")
        if not str(row.get("relation", "")).strip():
            report.fail(f"{rid} missing relation")
        seen[rid] = (left, right)
    for rid, pair in expected.items():
        if seen.get(rid) != pair:
            report.fail(f"missing or changed relation {rid}")


def check_terms_match_spec(reg: dict, spec: str, report: Report) -> None:
    spec_nouns = {}
    spec_verbs = {}
    for header, rows in tables(spec):
        if header[:3] == ["Preferred term", "Definition", "Usage rule"]:
            for row in rows:
                if len(row) != 3:
                    report.fail(f"term row has {len(row)} cells: {row}")
                    continue
                spec_nouns[row[0]] = (norm(row[1]), row[2])
        elif header[:3] == ["Verb", "Definition", "Usage rule"]:
            for row in rows:
                if len(row) != 3:
                    report.fail(f"verb row has {len(row)} cells: {row}")
                    continue
                spec_verbs[row[0]] = (norm(row[1]), row[2])
    for term in reg["terms"]:
        preferred = term["preferred_term"]
        definition = norm(term["definition"])
        usage = norm(term["usage_rule"]) if term.get("usage_rule") else "—"
        target = spec_verbs if term["part_of_speech"] == "verb" else spec_nouns
        other = spec_nouns if term["part_of_speech"] == "verb" else spec_verbs
        if preferred in other:
            report.fail(f"{preferred!r} is in the wrong spec table")
        if preferred not in target:
            report.fail(f"registry term {preferred!r} is missing from the spec tables")
            continue
        spec_def, spec_usage = target[preferred]
        if spec_def != definition:
            report.fail(f"definition mismatch for {preferred!r}")
        if norm(spec_usage) != usage:
            report.fail(f"usage_rule mismatch for {preferred!r}")
        del target[preferred]
    for leftover in spec_nouns:
        report.fail(f"spec noun {leftover!r} is not in the registry")
    for leftover in spec_verbs:
        report.fail(f"spec verb {leftover!r} is not in the registry")


def rule_map(md: str) -> dict[str, tuple[str, str, str | None]]:
    found = {}
    for header, rows in tables(md):
        if header[:3] != ["ID", "Severity", "Proposed rule"]:
            continue
        has_example = len(header) > 3 and header[3] == "Example"
        for row in rows:
            if len(row) < 3:
                continue
            example = row[3] if has_example and len(row) > 3 else None
            found[row[0]] = (row[1], norm(row[2]), norm(example) if example else None)
    return found


def check_rules(spec: str, report: Report) -> None:
    spec_rules = rule_map(spec)
    copy = (ROOT / "rules" / "writing-rules.md").read_text()
    copy_rules = rule_map(copy)
    if spec_rules.keys() != copy_rules.keys():
        report.fail(
            "writing-rules.md rule ids differ: "
            f"spec={sorted(spec_rules)} copy={sorted(copy_rules)}"
        )
    for rid, triple in spec_rules.items():
        if copy_rules.get(rid) != triple:
            report.fail(f"writing rule {rid} differs from the specification")
        if triple[0] not in {"required", "advisory"}:
            report.fail(f"{rid} has severity {triple[0]!r}")
    for rid, severity in {"L04": "advisory", "L10": "required", "L12": "required", "L13": "required"}.items():
        if spec_rules.get(rid, ("",))[0] != severity:
            report.fail(f"{rid} must be {severity}")
    if "Do not use shall." not in spec or "Do not use shall." not in copy:
        report.fail("shall prohibition missing")
    words = {}
    for header, rows in tables(spec):
        if header[:2] == ["Word", "Meaning in ICTE-1"]:
            for row in rows:
                words[row[0]] = norm(row[1])
    copy_words = {}
    for header, rows in tables(copy):
        if header[:2] == ["Word", "Meaning in ICTE-1"]:
            for row in rows:
                copy_words[row[0]] = norm(row[1])
    if words != copy_words:
        report.fail("requirement-word table differs from the specification")
    reg = yaml.safe_load(REG_PATH.read_text())
    reg_words = {row["word"]: norm(row["meaning"]) for row in reg["requirement_words"]}
    if reg_words != words:
        report.fail("registry requirement_words differ from the specification")
    reasons = {row["word"]: norm(row["reason"]) for row in reg["avoid_requirement_words"]}
    if reasons.get("shall") != "Do not use shall.":
        report.fail("registry shall reason drifted")
    will = "Do not use will to imply a guarantee unless the behavior is established and its conditions are stated."
    if reasons.get("will") != will or will not in spec:
        report.fail("will prohibition drifted")


def check_section_6(spec: str, report: Report) -> None:
    block = between(spec, "## 6. Domain-specific precision rules", "## 7. Required document patterns")
    bullets = [
        line[2:].strip()
        for line in block.splitlines()
        if line.startswith("- ")
    ]
    copy = (ROOT / "rules" / "domain-precision.md").read_text()
    if "or mark the item not applicable" not in block or "or mark the item not applicable" not in copy:
        report.fail("not-applicable checklist sentence missing")
    for bullet in bullets:
        if bullet not in copy:
            report.fail(f"domain-precision.md missing bullet: {bullet}")
    for sentence in (
        "Put the warning immediately before a destructive action.",
        "Model output is not verified fact.",
        "Do not imply that reverting a commit restores application data or reverses external side effects.",
    ):
        if sentence not in copy or sentence not in spec:
            report.fail(f"missing shared sentence: {sentence}")


def check_patterns(spec: str, report: Report) -> None:
    block = between(spec, "## 7. Required document patterns", "## 8. Before-and-after examples")
    # Split on ### 7.n headings.
    parts = re.split(r"(?=### 7\.[1-4] )", block)
    found = {}
    for part in parts:
        match = re.match(r"### (7\.[1-4]) ", part)
        if not match:
            continue
        fences = fenced_text(part)
        if len(fences) != 1:
            report.fail(f"{match.group(1)} should contain one pattern fence")
            continue
        labels = []
        for line in fences[0].splitlines():
            stripped = line.strip()
            if stripped.endswith(":"):
                label = re.sub(r"^\d+\.\s*", "", stripped)[:-1].strip()
                labels.append(label)
        found[match.group(1)] = labels
    for number, path in TEMPLATES.items():
        text = (ROOT / path).read_text()
        for label in found.get(number, []):
            if label not in text:
                report.fail(f"{path} missing field {label!r}")
        if "TBD" not in text or "not applicable" not in text:
            report.fail(f"{path} must tell the writer to use TBD and not applicable")


def check_prompts(spec: str, report: Report) -> None:
    for label, path in (
        ("icte-1", "prompts/icte-1.txt"),
        ("ste-inspired", "prompts/ste-inspired.txt"),
    ):
        expected = prompt_body(spec, label)
        actual = (ROOT / path).read_text()
        if actual.strip() + "\n" != expected:
            report.fail(f"{path} does not match the specification prompt")
    if "This instruction is not the ICTE-1 profile." not in spec:
        report.fail("STE prompt is not distinguished from ICTE-1")


def check_examples(spec: str, report: Report) -> None:
    sentence = "The operator verifies that every workload has migrated off the target host."
    procedure = (ROOT / "examples" / "infrastructure-procedure.md").read_text()
    if sentence not in spec or sentence not in procedure:
        report.fail("section 8.1 procedure sentence is missing from the extract")
    if "Move all workloads from the target host." in procedure:
        report.fail("section 8.1 extract still changes the procedure order")
    spec_rows = domain_rows(spec)
    copy_rows = domain_rows((ROOT / "examples" / "before-after.md").read_text())
    if not spec_rows or spec_rows != copy_rows:
        report.fail("examples/before-after.md does not match section 8")
    for path in SAMPLES:
        text = (ROOT / path).read_text()
        if "TBD" not in text:
            report.fail(f"{path} does not keep unknowns visible")
        if "Rules:" not in text:
            report.fail(f"{path} does not annotate rules")
    acceptance = (ROOT / "rules" / "acceptance.md").read_text()
    for phrase in ("Language result", "Operational completeness", "Technical review"):
        if phrase not in spec or phrase not in acceptance:
            report.fail(f"acceptance copy missing {phrase}")


def domain_rows(md: str) -> list[tuple[str, str, str]] | None:
    for header, rows in tables(md):
        if header[:3] == ["Domain", "Ambiguous wording", "ICTE-1 wording"]:
            return [tuple(row[:3]) for row in rows]  # type: ignore[misc]
    return None


def check_schema_file(reg: dict, report: Report) -> None:
    path = ROOT / "vocabulary" / "registry.schema.json"
    text = path.read_text()
    for token in ("preferred_term", "non_equivalences", "proposed_relations", "usage_rule"):
        if token not in text:
            report.fail(f"schema is missing {token}")
    schema = json.loads(text)
    errors = sorted(
        Draft202012Validator(schema).iter_errors(reg),
        key=lambda err: list(err.absolute_path),
    )
    for err in errors:
        where = "/".join(str(part) for part in err.absolute_path) or "<root>"
        report.fail(f"schema: {where}: {err.message}")


def check_reader(spec: str, report: Report) -> None:
    if "### 2.3 Reader" not in spec:
        report.fail("reader section missing")
    if "https://opengitops.dev/" not in spec:
        report.fail("OpenGitOps citation missing")
    if not spec.startswith("# ICTE-1:") or "Version: 0.2" not in spec.split("## 1.", 1)[0]:
        report.fail("spec version line is not 0.2")


def main() -> int:
    report = Report()
    spec = SPEC_PATH.read_text()
    reg = yaml.safe_load(REG_PATH.read_text())
    try:
        by_id = check_registry(reg, report)
        check_relations(reg, by_id, spec, report)
        check_terms_match_spec(reg, spec, report)
        check_rules(spec, report)
        check_section_6(spec, report)
        check_patterns(spec, report)
        check_prompts(spec, report)
        check_examples(spec, report)
        check_schema_file(reg, report)
        check_reader(spec, report)
    except CheckError as exc:
        report.fail(str(exc))
    if report.errors:
        print(f"{len(report.errors)} alignment error(s):", file=sys.stderr)
        for error in report.errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"ICTE-1 alignment ok ({len(reg['terms'])} terms)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
