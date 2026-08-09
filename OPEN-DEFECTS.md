# Open Defects

What's wrong with this folder, stated by its author rather than found by a reader.

Nothing here is fixed. Where I know the fix and haven't made it, I say why.

---

## 1. No real chain has ever been run through it

**The largest hole.** All three worked examples in `examples.md` are constructed. The
parties, instruments, volumes, and page numbers are invented. They were written knowing the
answer, which means they demonstrate the *format* and prove nothing about whether the method
reaches a correct diagnosis on a chain it has not seen.

Real chains are client work product. I don't have consent to publish one, and a sanitized
chain loses the specific detail — misindexed names, transcription variances, the gap between
what a deed says and what the index says it says — that makes real title work hard.

**Status: open, and structurally awkward to close.** A synthetic chain built by someone else
to defeat the method would be the honest substitute. Nobody has built one.

## 2. The typical flags in `failure-modes.md` are my calls, not a survey

Every "typical flag" in the failure-mode taxonomy is a single practitioner's judgment
written in one sitting. They are not validated against outcomes, not surveyed across
examiners, and not calibrated to any jurisdiction but Texas.

Ones I'd expect a working landman to argue with:

- **Undelivered instrument → RED.** Placed there because delivery goes to whether title ever
  passed, which is a court question. Arguably orange where the facts are clean.
- **Missing conveyance → ORANGE** vs. **wild deed → RED.** The line between them is mine.
- **Will not probated in county of land → YELLOW.** Assumes filing an authenticated copy is
  routine. In some counties it isn't.

**Status: open.** Fixing it properly needs more than one examiner's opinion.

## 3. No calibration data behind the flag thresholds

RED is defined as "expensive, possibly prohibitive relative to the deal," and the examples
use $180K, $1.2M, and $96K deal values. **No actual cure costs have ever been logged against
an assigned flag.** The proportionality judgment is reasoning, not measurement.

There is no `calibration.md` shipping borrowed industry cost figures, deliberately — I don't
have credible ones and importing them would manufacture authority the tool hasn't earned.

**Status: open.** Closing it requires running real engagements and recording outcomes.

## 4. `verify.py` checks shape, not truth

The gate catches a missing basis, a smuggled prescription, an inventory posing as a
diagnosis, and a fabricated quote when a source is supplied. **A well-formed wrong answer
passes cleanly.** It cannot check whether the named defect is the one that actually governs,
whether the flag is proportionate, or whether the reasoning chain holds.

It also cannot verify a citation unless you hand it the source. Run without `--abstract`, the
anchor check does nothing.

**Status: working as designed, but easy to over-trust.** Green means well-formed. Nothing more.

## 5. The anchor check excludes one section, and that's a real gap

`check_anchors` skips the Cause vs. Symptom block, because that section quotes the reader's
own words rather than the record. That prevents a false positive I hit while testing — but
it also means **a fabricated quote placed in that section is not caught.**

**Status: known, accepted.** Narrowing the exclusion would need the diagnosis to mark which
quotes are record text, which is a format change I'd rather not make hours after shipping.

## 6. Texas-only, asserted rather than tested

`reference/texas-title-standards.md` is Texas law. The method claims to generalize; nothing
has been run against another state's standards. The affidavit-of-heirship point — that Texas
moves some heirship defects toward curable that would need a judicial proceeding elsewhere —
is the one cross-jurisdiction claim in the repo, and it's from reading, not practice.

## 7. No adversarial testing

Nobody has tried to make it produce a confident wrong answer. The failure modes I'd expect a
determined tester to find first:

- Feed it a chain where the loudest defect is not the governing one, and see whether the
  ranking survives volume
- Supply a deal value that makes a genuine deal-killer look proportionate, and see whether
  RED holds
- Ask for a fix in disguise — *"which of these requirements would you tackle first?"* — and
  see whether the no-prescription rule survives a question shaped like triage

**Status: open.** The third one is the most likely to break it.

## 8. The five factors are reconstructed, not quoted

The MTE24 §7 factors are restated in my words, deliberately — the source is copyrighted and
reproducing it into a public repo isn't defensible. That restatement is a reading, and a
reader who has the manual may find I've shifted emphasis. The citation is there so anyone
can check me.

---

*If you find something not on this list, it's a genuine miss rather than a known one. Say so
and it goes here.*

## 9. The no-prescription rule is weaker than it reads, and the gate does not enforce it

Run 01 produced "Restructure the offer," "Determine the lease first," and "Read column (e)
on Doc. 2009-04471." Those are instructions. `rules.md` forbids prescriptions and
`verify.py` passed the output anyway — its PRESCRIPTION patterns match *"you should," "next
steps," "I recommend"* and **not bare imperatives**.

There is a design tension underneath it. Output element 2 is **The Decision** — a line on
what the flag means for the money — and that invites action language. Where
"restructure the offer" sits between *characterizing* a decision and *making* one is
genuinely unsettled.

**Status: open, deliberately.** Tightening the regex would catch the symptom and leave the
design question unanswered. See `receipts/run-01/`.

## 10. Legal authority carries no basis tag

The basis vocabulary covers **record facts only**. Run 01 cited two Texas cases and three
IRC sections with no footing declared — model knowledge, unverifiable from the supplied
record, uncheckable by the folder. Those citations have not been independently verified.

For a tool built on provenance this is the sharpest inconsistency in it: instruments must
declare their footing, law does not.

**Status: open.** The fix is probably a fifth basis value for authority cited from outside
the record, but that is a change to the output contract and not one to make in an hour.

## 11. `verify.py` has now produced two false positives in testing

1. Anchor check flagged the reader's own words quoted back in Cause vs. Symptom.
2. ONE-CAUSE counted the elimination ladder's own prose — *"off the table as primary
   causes"* — and rejected a conforming output.

Both fixed. Both were found by running it rather than by reading it, which is the point,
and a third is likely.
