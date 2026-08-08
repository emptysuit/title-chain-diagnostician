# Title Chain Diagnostician

**Diagnoses why land and mineral deals die due to title defects.**

Built for Texas land and mineral title examination. Drop the folder into a Claude project, feed it a busted chain of title, and it tells you the one thing that killed your deal.

---

## What This Does

You had a deal. It died. Something in the title chain killed it. This diagnostician works backward from the failure to identify the primary defect — the root cause, not the symptom list.

It does not tell you how to fix it. It does not audit the full title. It does not rewrite your documents. It names what went wrong, shows how it got there, and stops.

---

## Who It's For

- **Land brokers** trying to figure out why a deal fell apart
- **Landmen** running title and hitting a wall they can't explain
- **Real estate attorneys** reviewing a chain that doesn't add up
- **Title examiners** wanting a second set of eyes on a complex chain
- **Mineral buyers** who got a "no" and need to understand why

---

## How to Use It

### Setup

Add this folder to a Claude project as project knowledge.

### Input

Paste one of the following into the conversation:

- A **title abstract** or **runsheet**
- A **title commitment** (Schedule B exceptions are especially useful)
- A **chain of title summary** with instrument references
- A **narrative description**: what the deal was, who the parties were, and what happened when it fell apart

The more specific your input, the more precise the diagnosis. Include dates, recording references, party names, and legal descriptions when you have them.

### Prompt

Ask a question like:

- *"Why did this deal die?"*
- *"What killed this transaction?"*
- *"The buyer walked — what's the title problem?"*
- *"Our landman can't get this lease done. Diagnose the title chain."*

### Output

You'll get five things:

1. **Primary Cause** — One sentence naming the root defect and where in the chain it originates
2. **Basis** — What the diagnosis rests on, and what would refute it
3. **Reasoning Chain** — How the diagnostician traced from the failure event back to the cause
4. **Cause vs. Symptom** — Why the thing you're seeing is downstream of the real problem
5. **Secondary Defects** — Brief classification of anything else found (deal-killer, curable, or nuisance)

---

## Provenance Is the Product

Anyone can name a defect. What makes a diagnosis worth acting on is that you can **check
it without redoing the examination.**

So every diagnosis declares its footing:

| Basis | Means |
|---|---|
| `instrument-decided` | The defect is visible on the face of an instrument that was read |
| `record-searched` | The defect is an *absence* — and an absence is only as good as the search behind it |
| `inferred` | It follows from what's in hand, but the decisive instrument hasn't been read |
| `pull required` | It can't be settled without a specific instrument nobody has yet |

Then it names **what would refute it** — or says plainly that nothing would, because some
defects (ambiguous granting language, for one) are settled by a court, not by a deeper
search.

This isn't hedging. Hedging weakens a conclusion; declaring the basis makes it
falsifiable, which is what makes it strong.

---

## What a Diagnosis Looks Like

> **Input:** *"My client is buying a 640-acre ranch. Cash buyer. Title company ran the
> commitment and everything looked fine until the buyer's attorney flagged an old deed of
> trust on Schedule B. Now the buyer is threatening to walk. The seller swears he paid
> that loan off twenty years ago."*

**Primary Cause:** A Deed of Trust dated March 15, 1983, from Robert and Linda Dawson to
First National Bank of Quanah, recorded at Volume 287, Page 142, securing a note of
$85,000, has never been released of record.

**Basis:** `instrument-decided` as to the lien — read on its face at Volume 287, Page 142.
`record-searched` as to the absence of release — county Deed of Trust and Official Public
Records searched from March 15, 1983 to present; no release or satisfaction appears.

*Refuted by:* a recorded release, or a satisfaction filed in the wrong county or
misindexed under a variant name. **The seller's recollection of payoff is not
refutation** — satisfaction of the debt and release of the lien are separate events, and
only the second one clears title.

**Cause vs. Symptom:** "The buyer is threatening to walk" is the symptom. The unreleased
1983 deed of trust is the cause. The seller's representation may well be true, but the
lien of record survives until a release is filed.

**Secondary Defects:** 1971 utilities easement across the north boundary — NUISANCE.

Then it stops. It does not tell you to go get a release. That's your attorney's call.

Two more worked diagnoses — one on unresolved heirship, one on royalty-vs-mineral
ambiguity — are in [`examples.md`](examples.md).

---

## What It Will NOT Do

| Won't do this | That's the job of |
|---|---|
| Prescribe a fix | Your title attorney |
| Audit the full title | A title examination company |
| Draft curative instruments | A title company or law firm |
| Assess insurability | A title insurer |
| Give legal advice | A licensed attorney |

This is a diagnostic tool. It finds the cause. What you do about it is your call.

---

## What's in the Folder

```
title-chain-diagnostician/
|-- identity.md                        # Who the diagnostician is and its scope
|-- rules.md                           # Step-by-step diagnostic methodology
|-- examples.md                        # Three worked diagnoses showing reasoning
|-- reference/
|   |-- failure-modes.md               # Taxonomy of title defects by type
|   |-- severity-framework.md          # Deal-killer vs. curable vs. nuisance
|   +-- texas-title-standards.md       # Key Texas title examination standards
+-- README.md                          # This file
```

---

## Limitations

- **Texas-calibrated.** Statutory presumptions, case law references, and curative procedures in the reference materials are Texas-specific. The diagnostic methodology applies broadly, but the legal details are jurisdiction-dependent.
- **Garbage in, garbage out.** A full abstract with instrument references produces a precise diagnosis. A vague narrative ("there's something wrong with the title") produces a request for more information.
- **Not a legal opinion.** This is a diagnostic aid. It does not replace a licensed title examiner's examination or an attorney's title opinion.
