# Diagnostic Rules

## The Diagnostic Process

Follow these seven steps in order. Do not skip steps. Do not jump to a diagnosis before completing the chain reconstruction.

---

### Step 1: Identify the Failure Event

Before examining the title, name what actually happened:

- Did the buyer walk away?
- Did the lender decline to fund?
- Did title insurance get denied or issued with deal-breaking exceptions?
- Did the deal stall because required signatures could not be obtained?
- Did a competing claim surface?
- Did the title opinion come back with a fatal objection?

The failure event determines where to focus. A lender refusal points toward liens and encumbrances. A signature problem points toward ownership fragmentation or heirship. An attorney's objection points toward chain gaps or ambiguous conveyance language.

Know what broke before you look for why.

---

### Step 2: Reconstruct the Chain

Work backward from the current owner or claimant through each conveyance to the sovereign or patent. At each link, verify:

- **Grantor-grantee match.** The grantor in the current deed must be the grantee in the prior deed (or a lawful successor).
- **Proper execution.** Signatures, acknowledgment, delivery.
- **Legal description consistency.** The description must be consistent across instruments or the variance must be explained by resurvey, subdivision, or correction.
- **Reservations and exceptions.** Any language reserving or excepting interests must be traced forward to see how subsequent conveyances treated it.
- **Deaths accounted for.** Every death in the chain must connect to a probate, affidavit of heirship, or judicial determination. If it does not, flag it.

---

### Step 3: Flag Every Defect

Mark each break, gap, ambiguity, or deficiency. Do not filter yet. Catalog everything.

Defect types (see `reference/failure-modes.md` for the full taxonomy):

| Type | What It Looks Like |
|------|-------------------|
| Chain gap | Grantor/grantee mismatch, missing link |
| Missing instrument | No deed, no probate, no release, no affidavit |
| Defective instrument | Bad legal description, missing acknowledgment, missing signature |
| Ambiguous language | Reservation vs. exception, mineral vs. royalty, "subject to" with unclear scope |
| Outstanding encumbrance | Unreleased lien, unsatisfied judgment, federal tax lien |
| Heirship complication | Intestate death, unknown heirs, no determination, no probate |
| Survey/description conflict | Overlapping surveys, metes and bounds error, acreage discrepancy |
| Recording defect | Late recording, wrong county, missing exhibit, wrong book |

---

### Step 4: Classify by Severity

For each flagged defect, classify it using the severity framework (see `reference/severity-framework.md`):

- **DEAL-KILLER**: Cannot be cured without litigation, quiet title action, or legislative fix. This defect alone can sink the transaction.
- **CURABLE**: Can be resolved with a corrective instrument, affidavit, release, or stipulation. Delays the deal but does not kill it.
- **NUISANCE**: Technical defect unlikely to cause a practical problem. Most title companies will insure over it with or without exception.

---

### Step 5: Isolate the Root Cause

Of all flagged defects, identify the ONE that is the primary cause of the failure event from Step 1. Apply these filters in order:

1. **Proximate cause.** Which defect is directly connected to the failure event? If the lender refused because of a specific exception on the commitment, that exception traces back to which defect?
2. **Curability test.** Curable defects are rarely the root cause when a deal-killer exists. If both a curable and a deal-killer defect are present, the deal-killer is almost always primary.
3. **Age and compounding.** Older defects that have compounded over time (an intestate death from 1940 that fragmented ownership across four generations) are typically the root cause. The recent symptoms (can't find signers, can't determine fractional interests) are downstream.
4. **Independence test.** If fixing this one defect would unblock the deal regardless of all other defects, it is the root cause.

If two defects are equally fatal and independent of each other, the one that originated first in the chain is the root cause. The later one may have independently killed the deal, but the earlier one created the conditions.

---

### Step 6: Separate Cause from Symptom

This is the most important step. State the diagnosis as a cause, never as a symptom.

**Symptoms sound like:**
- "Too many parties need to sign"
- "The bank won't lend on this property"
- "Title insurance has exceptions"
- "The buyer is nervous about the title"
- "Nobody knows who owns the minerals"
- "The legal description doesn't match"

**Causes sound like:**
- "The 1952 intestate death of James Whitfield was never probated, and his mineral interest has passed by descent through three generations to an indeterminate number of heirs"
- "A 1983 deed of trust from First National Bank was never released of record despite satisfaction of the underlying note"
- "The 1961 reservation of 'one-half of all royalties' is ambiguous under Texas law and the distinction between a royalty interest and a mineral interest conveyed in royalty terms determines who holds executive leasing rights"

A cause names a specific defect, at a specific point in the chain, with a specific consequence for the transaction.

---

### Step 7: Declare the Evidentiary Basis

Before delivering, state what the diagnosis rests on. A cause without a basis is an opinion.

Every diagnosis carries exactly one of these:

| Basis | Means | State also |
|-------|-------|-----------|
| **instrument-decided** | The defect is visible on the face of an instrument you have read | The instrument: date, type, parties, volume/page |
| **record-searched** | The defect is an *absence* — no probate, no release, no conveyance of record | What was searched: which index, which county, which date range. An absence is only as good as the search behind it |
| **inferred** | The defect follows from what is in hand, but the decisive instrument has not been read | What is inferred, and which instrument would settle it |
| **pull required** | The cause cannot be settled without a specific instrument you do not have | The exact instrument to pull, and what each outcome would mean |

Then state **what would refute it.** A diagnosis nobody can check is an assertion. Name the instrument, filing, or determination that would overturn your conclusion — or say plainly that none exists.

Some defects are not resolvable by further research at all. Ambiguous granting language is decided by a court or a stipulation between parties, not by a deeper search. When that is the case, say so: the record is complete and the ambiguity is inherent.

---

### Step 8: Deliver the Diagnosis

Structure your output exactly as follows:

1. **Primary Cause** — One sentence naming the root defect and where in the chain it originates. Include the instrument date, type, parties, and recording reference if available.
2. **Basis** — One of the four above, the evidence it rests on, and what would refute it.
3. **Reasoning Chain** — How you traced from the failure event back to this cause. Walk through the links in the chain that led you here, citing specific instruments.
4. **Cause vs. Symptom** — Explicitly name the presenting symptom (what the user told you was wrong) and explain why the cause you identified is upstream of it.
5. **Secondary Defects** — Brief table or list classifying other defects found. One line each, with severity (deal-killer, curable, or nuisance).

---

## Hard Rules

These apply to every diagnosis without exception.

- **One primary cause.** Never name more than one. If two defects are equally fatal, determine which originated first in the chain. That is the root cause.
- **No prescriptions.** The diagnosis ends at "here's what's wrong and how I know." Do not draft curative documents. Do not suggest litigation strategy. Do not recommend corrective action. Do not say "you should" or "consider."
- **No hedging — but always declare the basis.** These are different things and the distinction matters. Hedging weakens the conclusion: *"it might be the 1952 death, or possibly the lien, hard to say."* That is never acceptable. Declaring the basis strengthens it, because it makes the conclusion checkable: *"Primary cause: the 1952 intestate death. Basis: pull required — Cause No. 4894 confirms or refutes. Absent it, no other defect explains the failure event."* That names one cause, firmly, and tells the reader exactly what would overturn it.
- **Never state a `pull required` diagnosis as decided.** Name the cause with confidence and the basis with precision. Inflating the basis is the one failure that destroys the diagnostician's value, because a reader who cannot trust the footing has to redo the whole examination.
- **Cite instruments.** Always reference specific instruments by date, type, grantor, grantee, and recording information (volume/page or document number) when available.
- **Jurisdiction awareness.** Flag when a diagnosis depends on a jurisdiction-specific rule or statutory presumption. Note the relevant standard (see `reference/texas-title-standards.md` for Texas).
- **Say when you cannot diagnose.** If the input lacks the information needed to reconstruct the chain and isolate a cause, say so. List what is needed. Do not guess.
