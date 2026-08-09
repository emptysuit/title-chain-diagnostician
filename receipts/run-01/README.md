# Run 01 — Sec 88, Blk 4, T&P Ry Co Survey, A-1204

**Date:** 2026-08-08
**Model:** Opus 5, high reasoning
**Session:** fresh claude.ai Project, no prior context
**Project knowledge:** the six operating files only — `identity.md`, `rules.md`,
`examples.md`, and the three under `reference/`. Not `verify.py`, not `tests/`, not
`OPEN-DEFECTS.md`.
**Files:** `input.md` (verbatim, as pasted) · `output.md` (verbatim, unedited)

## Method, stated before the run

The case was **constructed by a session that did not run it.** The author of the case knew
the intended answer; the session that produced the diagnosis had never seen the case, and
the case is not among the three worked examples in `examples.md`.

That is a real separation and it is **not fully blind.** Nobody outside this project has
run it. Stated here rather than left to be discovered.

The case was built with a **decoy**: the requirement the fictional attorney "flagged
hardest" (a federal tax lien) is not the one that governs. Five open requirements, real
volume to rank against.

## Result

**It rejected the decoy.** Named the 1961 double-fraction royalty reservation as the
deciding defect; filed the tax lien as an orange likely resolving to yellow.

`verify.py` — **conforms** (after a false-positive fix, below).

### What it did that the folder did not supply

- **Ran the elimination ladder unprompted.** Placed the engagement at rung 4 of 5 and wrote:
  *"Diagnosis is complete; 'the search missed something' and 'nobody found the problem' are
  off the table as primary causes."* That is Step 1's ladder applied correctly to a case it
  had never seen.
- **Brought outside law.** *Hysaw v. Dawkins* (Tex. 2016) and *Van Dyke v. Navigator Group*
  (Tex. 2023) on double-fraction 1/8 reservations and the estate-misconception presumption.
  Neither is in `reference/`.
- **Caught a scope error in the case.** "No production on our tract" is the wrong search
  when the 1981 lease has no Pugh clause — production anywhere on the ~2,880 leased acres
  holds all of it. That correction was not solicited.
- **IRC § 6325(a) self-releasing lien.** Form 668(Y)(c) carries a column (e) date; absent
  refiling, the notice becomes its own release. *"'No release of record' is exactly what a
  self-released lien looks like."* Not in `reference/`, and it inverts the requirement.
- **Coupled two defects economically.** Both constructions of the reservation yield 1/16
  under a 1/8 royalty and diverge only at modern royalties — so what the reservation costs
  depends on whether the 1981 lease is still alive. Shipped with a table. That is reasoning
  from the framework, not recitation of it.

### Defects this run exposed

**1. It prescribed, and the gate did not catch it.**

"Restructure the offer." "Determine the lease first." "Read column (e) on Doc. 2009-04471."
Those are instructions. `rules.md` forbids prescriptions.

`verify.py` passed it because the PRESCRIPTION patterns look for *"you should," "next
steps," "I recommend"* — **not bare imperatives.** Both the rule and the gate are weaker
than they read.

There is also genuine tension in the design: output element 2 is **The Decision**, a line on
what the flag means for the money. That invites action language. Where "restructure the
offer" sits between characterizing a decision and making one is unresolved, and it is a
design question, not a bug to quietly patch.

**2. Legal authority carries no basis tag.**

The basis vocabulary — `instrument-decided`, `record-searched`, `inferred`, `pull required` —
covers **record facts only.** The run cited two Texas cases and three IRC sections with no
footing declared. Those came from model knowledge, are unverifiable from the supplied
record, and neither the folder nor the reader can check them from what's in the file.

For a tool whose whole claim is provenance, that is a real hole. **The citations were not
independently verified before this receipt was written.**

**3. `verify.py` false positive, found by this run and fixed.**

The ONE-CAUSE check counted every case-insensitive occurrence of "primary cause," including
the ladder's own eliminative prose — *"off the table as primary causes"* — and rejected a
conforming output. Now counts only the labelled form (heading or bold label). Fixture suite
re-run: 5/5.

This is the **second** false positive testing has found in this verifier. The first was the
anchor check flagging the reader's own words quoted back in Cause vs. Symptom.

## Not done

- No refusal test. The disguised fix request — *"which of these would you tackle first?"* —
  was not run.
- One run, one case, one model. No replication, no second model, no adversarial attempt.
