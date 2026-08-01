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

You'll get four things:

1. **Primary Cause** — One sentence naming the root defect and where in the chain it originates
2. **Reasoning Chain** — How the diagnostician traced from the failure event back to the cause
3. **Cause vs. Symptom** — Why the thing you're seeing is downstream of the real problem
4. **Secondary Defects** — Brief classification of anything else found (deal-killer, curable, or nuisance)

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
