# Title Chain Diagnostician

**Is the juice worth the squeeze?**

You're holding a title with problems in it and deciding whether to put more money in. This
tells you which single defect decides that, what clearing it costs, and how it knows.

Drop the folder into a Claude project. Built for land and mineral title, Texas-calibrated.

---

## Two defects, identical on paper, opposite answers

> **"Mary Elizabeth Smith" vs. "Mary E. Smith."** One affidavit, one known party. A phone
> call and a notary.
>
> **Forty-seven heirs across six states.** All identified. All locatable. All willing.
> Running them costs more than the mineral interest is worth.

**Both code `CURABLE`.** Every severity scale in this business calls them the same thing —
and sends a landman into six months of signature-chasing on the second one.

The severity says *by what mechanism it resolves.* It does not say *what resolving it
costs*, and those are different questions with opposite answers. This folder asks the second
one.

Same again with an unreleased lien: identical defect, and whether the bank's successor is
traceable is the difference between an afternoon and a suit to quiet title against an
unlocatable lienholder. **Nobody has looked it up, so nobody knows which deal they're in.**

---

## The money hasn't been spent yet

Most diagnosis works a corpse — the lost deal, the rejected filing, the dead transaction.
This works the live one.

*"Should we keep spending on this"* is asked while the cheque is still in your hand. The
title opinion is on the desk, the requirements are open, the seller is getting impatient,
and every day of landman hours is money going out on a deal you may not do. **The failure
this prevents hasn't happened yet.**

It works on a dead deal too — *why it died* and *which defect was never going to clear* are
the same question at different times. But the expensive moment is the live one.

---

## The Problem

A title examiner answers: *is title good, and what's required to make it good?*

**Nobody answers: are those requirements achievable?**

An opinion says "obtain affidavit of heirship from the heirs of Harold Mitchell." Correct
and complete as a requirement. It does not say there are forty-odd heirs across three
generations in six states, four are unlocatable, and **that affidavit is never getting
signed.**

The examiner isn't paid to know that. The landman finds out over six months, then walks.

So a requirements list arrives flat — twelve items that look equally weighty on the page.
One is a phone call and a notary. One is a two-year quiet title against defendants nobody
can find. **Deciding "the extra work isn't worth it" without knowing which is which is how
good deals get abandoned and dead ones get funded.**

---

## What It Does

Ranks the defects to **one**, and flags what resolving it costs.

| Flag | Means | Next move |
|---|---|---|
| 🟡 **YELLOW** | Known, cheap. Parties identified and available. | Speed bump. Proceed. |
| 🟠 **ORANGE** | Path known, **cost not determinable** without scoped work. | Decide how much to spend finding out. |
| 🔴 **RED** | Expensive, possibly prohibitive relative to the deal. | Price it in, or walk. |

Behind the flag sits the severity — deal-killer, curable, nuisance — which explains *why*.

**They don't map onto each other** — see the top of this file. `CURABLE` spans all three
flags, and that gap is why the flag exists.

**RED is relative to the deal.** A $40,000 cure is orange on a $2M tract and red on a
$60,000 one. Give it the deal value, or it'll tell you what threshold it assumed.

---

## Who It's For

- **Brokers** deciding whether to tell a client to keep spending or walk
- **Landmen** holding a requirements list and needing to know which requirement is the deal
- **Mineral buyers** deciding whether to commission an opinion at all
- **Attorneys and examiners** wanting a second read on which defect actually governs
- **Anyone who got a "no"** and needs to know whether it was the right call


---

## How to Use It

**Setup.** Add this folder to a Claude project as project knowledge.

**Input.** A title abstract, runsheet, commitment, requirements list, chain summary, or a
narrative of what happened. **Include the deal value** — a flag is a judgment about
proportion and it's meaningless without one.

**Ask:**

- *"Should we keep spending on this?"*
- *"Which of these requirements is going to kill us?"*
- *"Is it worth commissioning an opinion here?"*
- *"The buyer walked. Were they right to?"*

**Output — seven things:**

1. **Flag** — 🟡 / 🟠 / 🔴 with the severity behind it
2. **The Decision** — one sentence on what it means for the money
3. **Primary Cause** — the defect that decides it, with instrument citation
4. **Basis** — what the finding rests on, and what would refute it
5. **Reasoning Chain** — how it traced from the decision back to the defect
6. **Cause vs. Symptom** — why what you're seeing is downstream
7. **Secondary Defects** — flag and severity each, noted if they stack

---

## Provenance Is the Product

Anyone can name a defect. What makes a call worth acting on is that you can **check it
without redoing the examination.**

| Basis | Means |
|---|---|
| `instrument-decided` | Visible on the face of an instrument that was read |
| `record-searched` | The defect is an *absence* — only as good as the search behind it |
| `inferred` | Follows from what's in hand, decisive instrument unread |
| `pull required` | Can't be settled without an instrument nobody has yet |

Then it names **what would refute it** — or says plainly that nothing would, because some
defects are settled by a court, not a deeper search.

That isn't hedging. Hedging weakens a conclusion; declaring the basis makes it falsifiable,
which is what makes it strong.

---

## What a Call Looks Like

> **Input:** *"Buying a 640-acre ranch, cash, ~$1.2M. Commitment came back and the buyer's
> attorney flagged an old deed of trust on Schedule B. Seller swears he paid it off twenty
> years ago. Do we keep going?"*

**🟠 ORANGE — curable. Resolves to 🟡 YELLOW on one check:** is First National Bank of Quanah
still in existence, and if not, is its successor by merger or FDIC receivership identifiable
and willing to release? That's a phone call and a charter search. If the institution failed
and the note went into a pool that can't be traced, it escalates toward red — a suit to
quiet title against an unlocatable lienholder.

**The Decision:** Don't price this in yet and don't walk. Spend the afternoon on the
successor search — it's cheap and it settles which deal you're in.

**Primary Cause:** A Deed of Trust dated March 15, 1983, from Robert and Linda Dawson to
First National Bank of Quanah, recorded at Volume 287, Page 142, securing a note of
$85,000, has never been released of record.

**Basis:** `instrument-decided` as to the lien — read at Volume 287, Page 142.
`record-searched` as to the absence of release — county records searched from March 15,
1983 to present; no release appears. *Refuted by:* a recorded release, or a satisfaction
filed in the wrong county or misindexed. **The seller's recollection of payoff is not
refutation** — satisfaction of the debt and release of the lien are separate events, and
only the second one clears title.

**Cause vs. Symptom:** "The buyer is threatening to walk" is the symptom. The unreleased
1983 deed of trust is the cause.

Then it stops. It does not tell you to go get a release. That's your attorney's call.

Two more worked calls — unresolved heirship, and royalty-vs-mineral ambiguity — are in
[`examples.md`](examples.md).

---

## Where It Stops

**Whether to pursue curative action remains the client's business decision, informed by the
degree of title risk the client is willing to accept.**

That's how the profession draws the line and this tool respects it. FNREL's materials treat
the curative decision as the client's, influenced by the risk they'll assume (MTE24 §7).

What the profession has never supplied is a *scale* for making it. Risk assessment is a
named step in the standard workflow with no instrument for carrying it out. **The flag is
that instrument. It informs the decision. It doesn't make it.**

| Won't do this | That's the job of |
|---|---|
| Prescribe a fix | Your title attorney |
| Audit the full title | A title examination company |
| Draft curative instruments | A title company or law firm |
| Assess insurability | A title insurer |
| Give legal advice | A licensed attorney |

---

## What's in the Folder

```
title-chain-diagnostician/
|-- identity.md                        # Who it is, the question it answers, where it stops
|-- rules.md                           # The nine-step process and the hard rules
|-- examples.md                        # Three worked calls
|-- reference/
|   |-- failure-modes.md               # Taxonomy of title defects by type
|   |-- severity-framework.md          # The flag and severity scales, and how they interact
|   +-- texas-title-standards.md       # Key Texas title examination standards
+-- README.md                          # This file
```

---

## Verify the Output

The rules are prose. A model reads them and complies, or doesn't. **`verify.py` checks
whether it did.**

```bash
python verify.py diagnosis.txt
```

```bash
python verify.py diagnosis.txt --abstract chain.txt    # also anchor-check citations
```

Exit `0` if it conforms, `1` with named failures if not. Standard library, offline, no key.

| Check | Rejects |
|---|---|
| `ONE-CAUSE` | More than one primary cause, or an enumerated inventory posing as a diagnosis |
| `FLAG` / `SEVERITY` | Missing or invalid flag, or a flag with no severity behind it |
| `BASIS` / `REFUTATION` | No evidentiary basis, or a basis with nothing that would refute it |
| `PRESCRIPTION` | "You should," "next steps," "here's how to fix" — a consultant, not a diagnostician |
| `CAUSE-VS-SYMPTOM` | Never naming the presenting symptom |
| `ANCHOR` | A quoted excerpt that does not appear in the source you supplied |

Fixtures in `tests/` — one that conforms, four that fail on a named check.

### What it can't do

**It checks shape, not truth.** A well-formed wrong answer passes cleanly. It cannot tell
you the named defect is the one that actually governs, that the flag is proportionate, or
that the reasoning holds. Green means well-formed and nothing more.

The judgment stays yours. The gate only catches what's mechanical — and the point of making
the diagnosis declare its footing is that the rest is auditable by hand.

**A real run is in [receipts/run-01/](receipts/run-01/)** — fresh session, Opus 5 high,
verbatim in and out, including the two defects it exposed and the verifier false positive it
caught. **Known holes are in [OPEN-DEFECTS.md](OPEN-DEFECTS.md)**, including the largest:
no real chain of title has been run through this, only constructed cases.

---

## Limitations

- **Texas-calibrated.** Statutory presumptions, caselaw, and curative procedures in the
  reference material are Texas-specific. The method applies broadly; the legal details are
  jurisdiction-dependent.
- **Needs a deal value.** Without one, flags are guesses at proportion. It'll say what it
  assumed, but that's a weaker answer.
- **Garbage in, garbage out.** A full abstract with instrument references produces a
  precise call. "There's something wrong with the title" produces a request for more.
- **Not a legal opinion.** A diagnostic aid. It does not replace a licensed examiner's work
  or an attorney's title opinion.
