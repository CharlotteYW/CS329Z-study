# Assessments and Learning Evidence

This is a **self-study diagnostic**, not Stanford's official grading scheme. No answers, scores, or knowledge gaps have been inferred during setup.

## Lecture Follow-Up

Start from the learner's note and ask one question about an assumption, a design tradeoff, or the evidence behind a claim. If the learner is stuck, give one hint and let them try before explaining. When a transfer check adds value, draw the example from a lecture, reading, or documented open source implementation.

## Module Review Rubric

| Dimension | Weight | Typical evidence |
|---|---|---|
| Conceptual understanding | 25% | Accurate own-words explanation and a counterexample |
| Implementation ability | 25% | Explained code plus meaningful executed tests |
| Architecture and tradeoff reasoning | 20% | Choice versus a simpler baseline under stated constraints |
| Evaluation and debugging ability | 20% | Failure attribution, scorer critique, reproducible evidence |
| Communication and explanation | 10% | Clear assumptions, limitations, and concise technical reasoning |

Score demonstrated performance on a 0–4 scale: **0** cannot explain or perform the attempted task; **1** major gaps and substantial guidance; **2** partially correct with targeted help; **3** independently correct on the core task; **4** correct transfer with well-supported tradeoffs. Mark untested dimensions **unassessed**, never zero. Compute a weighted total only once all dimensions have evidence; do not fabricate precision from incomplete observations.

For formal reviews, the default gate is at least 3/4 on each assessable dimension plus the relevant application and transfer check. Essential correctness, privacy, or permission failures require review even if a numerical average is high. Use this rubric at meaningful milestones; a routine lecture note does not need a scorecard.

## Review Format

For a formal review, select questions that fit the material: conceptual explanation, architecture choice, debugging, evaluation, or transfer. Use actual homework and project decisions as evidence wherever possible. Reveal hints progressively and note how much assistance was needed.

Create a dated English review record containing the questions actually asked, learner responses or faithful summaries, evidence links, observed misconceptions, rubric results, feedback, and a specific remediation task. Reassess only the unresolved skill, unless new evidence shows a broader gap. Keep `PROGRESS.md` synchronized with the review.

After an assignment, conduct an oral defense of the real implementation. After a paper, separate author claims from experimental support. After the project, ask for a clean reproduction and a defense of the strongest and weakest conclusions.
