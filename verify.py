#!/usr/bin/env python3
"""
verify.py — gate a diagnosis against the output contract.

The folder's rules are prose. A model reads them and complies, or doesn't. This
checks whether it did.

    python verify.py diagnosis.txt
    python verify.py diagnosis.txt --abstract chain.txt   # also anchor-check citations
    cat output | python verify.py -

Exit 0 if the diagnosis conforms. Exit 1 with named failures if not.
Standard library only. Offline. No key.

WHAT IT CANNOT DO: it cannot tell you the diagnosis is *correct*. It checks shape,
not truth — that one cause was named rather than a list, that the flag and basis are
present and legal, that no fix was smuggled in, and that quoted citations actually
appear in the source you supplied. A well-formed wrong answer passes. Judgment stays
yours; this only catches the failures that are mechanical.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FLAGS = ("YELLOW", "ORANGE", "RED")
SEVERITIES = ("DEAL-KILLER", "CURABLE", "NUISANCE")
BASES = ("instrument-decided", "record-searched", "inferred", "pull required")

# Language that means the tool stopped diagnosing and started advising.
PRESCRIPTION = [
    (r"\byou should\b", "you should"),
    (r"\bI recommend\b", "I recommend"),
    (r"\bwe recommend\b", "we recommend"),
    (r"\bmy recommendation\b", "my recommendation"),
    (r"\byou'll want to\b", "you'll want to"),
    (r"\bthe fix is\b", "the fix is"),
    (r"\bto cure this,? (you|simply|just)\b", "to cure this, you…"),
    (r"\bnext steps?:", "next steps:"),
    (r"\bhere'?s how to (fix|cure|resolve)\b", "here's how to fix"),
    (r"\bI'?d suggest\b", "I'd suggest"),
]

# "Consider" is prescriptive as an imperative, fine as a verb elsewhere.
CONSIDER = re.compile(r"(^|[.!?]\s+|\n\s*[-*]?\s*)consider\b", re.I | re.M)


class Result:
    def __init__(self) -> None:
        self.fails: list[tuple[str, str]] = []
        self.warns: list[tuple[str, str]] = []
        self.notes: list[str] = []

    def fail(self, check: str, detail: str) -> None:
        self.fails.append((check, detail))

    def warn(self, check: str, detail: str) -> None:
        self.warns.append((check, detail))


def norm(s: str) -> str:
    """Collapse whitespace so a quote spanning a line break still matches."""
    return re.sub(r"\s+", " ", s).strip()


# ── checks ──────────────────────────────────────────────────────────────────────


def check_flag(t: str, r: Result) -> str | None:
    found = [f for f in FLAGS if re.search(rf"\b{f}\b", t)]
    if not found:
        r.fail("FLAG", "no flag. Every diagnosis leads with YELLOW, ORANGE, or RED.")
        return None
    # The headline flag is whichever appears first.
    first = min(found, key=lambda f: t.find(f))
    if len(found) > 1:
        r.notes.append(f"headline flag read as {first} (others appear later: {', '.join(x for x in found if x != first)})")
    return first


def check_severity(t: str, r: Result) -> None:
    if not any(re.search(rf"\b{s}\b", t, re.I) for s in SEVERITIES):
        r.fail(
            "SEVERITY",
            "no severity behind the flag. The flag says what it costs; the severity says why.",
        )


def check_basis(t: str, r: Result) -> None:
    hits = [b for b in BASES if re.search(re.escape(b), t, re.I)]
    if not hits:
        r.fail(
            "BASIS",
            "no evidentiary basis. Must declare one of: " + ", ".join(BASES) + ".",
        )
        return
    if not re.search(r"refut|would change (my|its) mind|overturn|settle", t, re.I):
        r.fail(
            "REFUTATION",
            "basis declared but nothing says what would refute it. A finding nobody can "
            "check is an assertion.",
        )
    if "pull required" in [h.lower() for h in hits]:
        if not re.search(r"\b(instrument|cause no\.?|doc(ument)? no\.?|vol\.?|volume|probate|file)\b", t, re.I):
            r.warn(
                "PULL-NAMED",
                "basis is 'pull required' but no specific instrument is named. Say which one.",
            )


def check_one_cause(t: str, r: Result) -> None:
    """A diagnosis names one cause. An inventory names several.

    Count only the LABELLED form — a heading or a bold label. Prose mentions don't
    count, and must not: the elimination ladder legitimately writes sentences like
    "X and Y are off the table as primary causes," which names none.
    """
    labels = re.findall(r"(?:^#{1,6}\s*Primary Cause|\*\*Primary Cause)", t, re.I | re.M)
    n = len(labels)
    if n == 0:
        r.fail("ONE-CAUSE", "no 'Primary Cause' section found (expect a heading or **bold label**).")
    elif n > 1:
        r.fail(
            "ONE-CAUSE",
            f"'Primary Cause' is labelled {n} times. Name one. Ties break by Step 6.",
        )

    # An enumerated list before the Secondary Defects section reads as an inventory.
    head = re.split(r"secondary defects", t, flags=re.I)[0]
    enumerated = re.findall(r"^\s*(\d+)[.)]\s+\S", head, re.M)
    if len(enumerated) >= 5:
        r.warn(
            "INVENTORY",
            f"{len(enumerated)} enumerated items before Secondary Defects. If that's a "
            "defect list, this is an audit, not a diagnosis.",
        )


def check_no_prescription(t: str, r: Result) -> None:
    for pat, label in PRESCRIPTION:
        m = re.search(pat, t, re.I)
        if m:
            line = t[: m.start()].count("\n") + 1
            r.fail("PRESCRIPTION", f"line {line}: \"{label}\" — that's a consultant, not a diagnostician.")
    m = CONSIDER.search(t)
    if m:
        line = t[: m.start()].count("\n") + 1
        r.fail("PRESCRIPTION", f"line {line}: sentence-initial \"Consider…\" reads as advice.")


def check_cause_vs_symptom(t: str, r: Result) -> None:
    if not re.search(r"symptom", t, re.I):
        r.fail(
            "CAUSE-VS-SYMPTOM",
            "the presenting symptom is never named. Say what the reader thought was wrong "
            "and why the cause sits upstream of it.",
        )


def check_red_route(t: str, flag: str | None, r: Result) -> None:
    """RED has two roads and they have different escape routes."""
    if flag != "RED":
        return
    if not re.search(r"mechanism|economics|court|judicial|no instrument|cost (to|of)|exceeds", t, re.I):
        r.warn(
            "RED-ROUTE",
            "RED without saying whether it's mechanism-red (a court decides) or "
            "economics-red (curable and not worth it). Different escape routes.",
        )


def check_decision(t: str, r: Result) -> None:
    if not re.search(r"the decision|worth|spend|proportion|walk|price it in", t, re.I):
        r.warn(
            "DECISION",
            "no line on what this means for the money. The flag is the headline; the "
            "decision sentence is what makes it actionable.",
        )


def check_anchors(t: str, abstract: str, r: Result) -> None:
    """Every quoted excerpt of the RECORD must actually appear in the source.

    The Cause vs. Symptom section quotes the user's own words back at them — the
    presenting complaint — which is not record text and has no business being
    anchor-checked. Strip that section before extracting quotes.
    """
    src = norm(abstract)

    # Drop the Cause vs. Symptom block: it quotes the reader, not the record.
    scannable = re.sub(
        r"\*\*Cause vs\.?\s*Symptom:?\*\*.*?(?=\n\s*\*\*[A-Z]|\Z)",
        "",
        t,
        flags=re.S | re.I,
    )

    quotes = re.findall(r'"([^"\n]{25,})"', scannable)
    if not quotes:
        r.notes.append("no record quotes to anchor-check")
        return
    bad = [q for q in quotes if norm(q) not in src]
    for q in bad:
        short = q if len(q) <= 70 else q[:67] + "…"
        r.fail("ANCHOR", f'quoted record text not found in the supplied source: "{short}"')
    r.notes.append(
        f"anchor-checked {len(quotes)} record quote(s), {len(quotes) - len(bad)} verified "
        "(Cause vs. Symptom excluded — it quotes the reader, not the record)"
    )


# ── driver ──────────────────────────────────────────────────────────────────────


def verify(text: str, abstract: str | None) -> Result:
    r = Result()
    if not text.strip():
        r.fail("EMPTY", "nothing to verify.")
        return r

    # An INSUFFICIENT EVIDENCE return is a complete answer with a different shape.
    # It carries no flag by design, so the diagnosis checks don't apply — but it must
    # still name the one observation that would settle it, or it's just a shrug.
    if re.search(r"\bINSUFFICIENT EVIDENCE\b", text, re.I):
        r.notes.append("INSUFFICIENT EVIDENCE return — checked against that contract, not the diagnosis one")
        if not re.search(r"would settle|settle it|single observation|one thing that would", text, re.I):
            r.fail(
                "SETTLE",
                "declines to call it but never names the observation that would settle it. "
                "That's a shrug, not an answer.",
            )
        check_no_prescription(text, r)
        return r

    flag = check_flag(text, r)
    check_severity(text, r)
    check_basis(text, r)
    check_one_cause(text, r)
    check_no_prescription(text, r)
    check_cause_vs_symptom(text, r)
    check_red_route(text, flag, r)
    check_decision(text, r)
    if abstract:
        check_anchors(text, abstract, r)
    return r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Gate a diagnosis against the output contract.")
    ap.add_argument("diagnosis", help="file containing the diagnosis, or - for stdin")
    ap.add_argument("--abstract", help="the source the diagnosis was run against; enables anchor-checking")
    ap.add_argument("--quiet", action="store_true", help="failures only")
    a = ap.parse_args(argv)

    text = sys.stdin.read() if a.diagnosis == "-" else Path(a.diagnosis).read_text(encoding="utf-8-sig")
    abstract = Path(a.abstract).read_text(encoding="utf-8-sig") if a.abstract else None

    r = verify(text, abstract)

    if r.notes and not a.quiet:
        for n in r.notes:
            print(f"  note: {n}")
    for check, detail in r.warns:
        print(f"  WARN  [{check}] {detail}")
    for check, detail in r.fails:
        print(f"  FAIL  [{check}] {detail}")

    if r.fails:
        print(f"\nREJECTED — {len(r.fails)} contract violation(s).")
        return 1
    print(f"\nOK — conforms to the output contract"
          + (f" ({len(r.warns)} warning(s))" if r.warns else "")
          + ".\n  This checks shape, not truth. A well-formed wrong answer passes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
