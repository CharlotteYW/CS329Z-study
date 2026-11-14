# First Session — System Boundaries and Agent Control

Status: **Not Started**. This is session preparation, not learner-authored notes or evidence of completion.

## Current Progress

The workspace is initialized. No agent-engineering knowledge has been assessed. The current module is M1; the weekly budget is 5–7 hours.

## Today's Learning Goal

Distinguish an LLM call, a compound workflow, and a model-directed agent loop. Identify who selects actions, who executes them, where state lives, and what stops the system. These distinctions determine which component to debug and where to enforce reliability controls.

## Study Materials

First official lecture: **Introduction — What Are Agentic Systems?**, September 23, 2026.

- [Official slides](https://web.stanford.edu/class/cs329z/slides/lecture01.pdf): reachable PDF.
- [Officially linked video](https://youtu.be/DGI4vucR71w): endpoint reachable; playback not tested.
- [The Shift from Models to Compound AI Systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/): first reading for this session.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/): overview/components during M1; save detailed case studies for later.
- [AI Agents That Matter](https://arxiv.org/abs/2407.01502): abstract/introduction and one evaluation example during M1.

All three readings are on the official L01 list. The order and selected reading depth above are mentor recommendations. If video playback is unavailable, use the public slides and readings; do not record the video as watched.

## Before the Lecture

Prerequisites: backend request handling, state, APIs, and failure handling. No ML training background is needed for this session. Ask for a short LLM-input/output explanation if needed.

Focus on the boundary between the model and the application, the source of control flow, and how observations can change a next action. For each architectural component, ask what can fail and what evidence would reveal the failure. Avoid classifying an application only by how many model calls it makes.

Questions to answer after studying the lecture:

1. Can a system use an LLM, retrieval, and tools while still following a fixed workflow? Explain using its control flow.
2. What extra uncertainty does letting a model choose the next action introduce?
3. Which parts of task state belong in model context, persistent storage, and the environment?
4. Who should enforce stopping, permissions, and execution validity?
5. What evidence would justify choosing an agent over a simpler pipeline?

## Study Plan

This **75-minute opening session** deliberately covers only a first pass; it is not the entire lecture or module.

| Time | Activity |
|---|---|
| 0–10 min | Answer the [initial diagnostic](../reviews/README.md#initial-diagnostic) without looking up answers; uncertainty is useful information |
| 10–25 min | Read the BAIR article; identify one engineering reason to improve the system around a model |
| 25–45 min | Inspect the opening lecture slides or begin the linked recording; stop at a coherent topic boundary and note the exact page/time reached |
| 45–65 min | Complete [E1 Part A](../exercises/01-system-boundaries/README.md): compare two incident-triage designs |
| 65–75 min | Explain the chosen boundaries and answer two questions above; record gaps and the next step |

Use the remaining M1 sessions to finish the lecture and core readings, implement E1 Part B, run its tests, and complete the module assessment. Do not record a 20-minute preview as a completed lecture.

## Expected Deliverables

- Diagnostic answers in conversation or a learner-authored review file.
- A short English design note in the E1 folder, containing both control-flow sketches, the chosen baseline, stopping rules, and test cases.
- A brief own-words explanation and a precise record of the source material actually covered.

The mentor should review the design before giving implementation hints. No solution code is prefilled.

## Knowledge Check

Explain how your design changes if the first retrieved runbook is irrelevant. Identify the exact component that decides what happens next. Then explain what happens if the tool times out twice. A plausible answer must specify observable behavior, not only say that the agent will reason or try again.

## Completion Criteria

This session is successful when the learner can distinguish the two designs, identify model versus harness responsibilities, and describe a bounded failure path. The mentor records observed gaps and a next action. The lecture and module remain incomplete until their remaining comprehension and implementation gates are met.

## During and After the Lecture

Use questions to connect the lecture to concrete backend systems. After the full lecture, explain its key ideas in your own words, identify an architectural pattern, relate it to E1, and answer the questions above. Save learner conclusions separately from this preparation document and link assessment evidence from `PROGRESS.md`.
