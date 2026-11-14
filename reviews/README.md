# Assessments and Learning Evidence

This is a **self-study diagnostic**, not Stanford's official grading scheme. No answers, scores, or knowledge gaps have been inferred during setup.

<a id="initial-diagnostic"></a>
## Initial Diagnostic

Answer briefly without looking anything up. A concrete example is more useful than terminology. "I am unsure" is informative, not a failure.

1. **Control flow:** A service always retrieves documents and calls an LLM to answer. A second service lets the LLM decide whether to search again, use a tool, or finish. What architectural difference matters, and when would you prefer the first design?
2. **Tool execution:** A model requests `create_ticket`, the request times out, and the system retries. What could go wrong, and where would you put the control that prevents it?
3. **Retrieval:** A RAG assistant gives a wrong answer. How would you determine whether the cause was retrieval, context construction, or answer generation?
4. **Evaluation:** An agent succeeds on 8 of 10 tasks. What additional information would you need before claiming that it is reliable or better than a baseline?
5. **Trust boundaries:** A retrieved document tells an assistant to send private logs to an external URL. Which component should prevent that action, and why is prompt wording alone insufficient evidence of protection?

Also mention one agent/RAG system you have personally built, if any, and which component you implemented yourself. This is optional background context, not an additional test.

The mentor should identify demonstrated strengths, one or two priority gaps, and the next task. Do not reveal a full answer key before the learner attempts the questions. Do not infer implementation ability solely from fluent verbal answers.

## Module Review Rubric

| Dimension | Weight | Typical evidence |
|---|---|---|
| Conceptual understanding | 25% | Accurate own-words explanation and a counterexample |
| Implementation ability | 25% | Explained code plus meaningful executed tests |
| Architecture and tradeoff reasoning | 20% | Choice versus a simpler baseline under stated constraints |
| Evaluation and debugging ability | 20% | Failure attribution, scorer critique, reproducible evidence |
| Communication and explanation | 10% | Clear assumptions, limitations, and concise technical reasoning |

Score demonstrated performance on a 0–4 scale: **0** cannot explain or perform the attempted task; **1** major gaps and substantial guidance; **2** partially correct with targeted help; **3** independently correct on the core task; **4** correct transfer with well-supported tradeoffs. Mark untested dimensions **unassessed**, never zero. Compute a weighted total only once all dimensions have evidence; do not fabricate precision from incomplete observations.

The default module gate is at least 3/4 per dimension plus its explicit deliverables and transfer check. Essential correctness, privacy, or permission failures require review even if a numerical average is high. Use scores to target learning, not rank the learner.

## Review Format

Use a 15–25 minute module review with a conceptual question, architecture choice, code-reasoning or debugging case, evaluation critique, and a transfer problem. Add a prior-module question at M3, M5, M8, and M10. Reveal hints progressively and note how much assistance was needed.

Create a dated English review record containing the questions actually asked, learner responses or faithful summaries, evidence links, observed misconceptions, rubric results, feedback, and a specific remediation task. Reassess only the unresolved skill, unless new evidence shows a broader gap. Keep `PROGRESS.md` synchronized with the review.

After an assignment, conduct an oral defense of the real implementation. After a paper, separate author claims from experimental support. After the project, ask for a clean reproduction and a defense of the strongest and weakest conclusions.
