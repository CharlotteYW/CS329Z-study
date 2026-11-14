# Week 1 — Foundations of Agentic Systems

Prepared: **2026-11-13**. Status: **Not Started**. This is the first self-paced study week, not Stanford's calendar week. Choose four sessions over the coming seven days; there is no requirement to finish by Sunday.

## Current Progress

Workspace setup is complete. No lecture, reading, exercise, or comprehension check has been completed. Start at M1/L01. Budget: **5–7 hours**, with a six-hour plan below.

## This Week's Learning Goal

Explain what makes a system agentic, identify the boundary between model decisions and application execution, and build a small controller whose failures and stopping rules can be tested. This is the foundation for diagnosing agent behavior and deciding whether adaptive control is worth its cost.

## Study Materials

Use the [L01 preparation and verified resource links](01-foundations.md): the official lecture slides/video, BAIR's compound-systems article, Weng's overview/component sections, and the abstract/introduction plus one evaluation example from *AI Agents That Matter*. Video playback has not been tested. The public slides/readings are the fallback.

Read the [E1 specification](../exercises/01-system-boundaries/README.md) before coding. E1 is mentor-designed practice, not official homework. No API key, model download, or external dependency is needed.

## Study Plan

| Session | Budget | Concrete actions | Result |
|---|---|---|---|
| 1. Orient and study L01 | 90 min | Spend 10 minutes on the initial diagnostic; study the lecture with slides and record where you stop; write a short own-words summary | Initial answers, lecture coverage, and questions |
| 2. Read and compare | 90 min | Read BAIR; study Weng's overview/components; read the selected *AI Agents That Matter* sections; compare a fixed workflow with an agent loop | Five concise learning points and two unresolved questions |
| 3. Design and start E1 | 90 min | Write the 200–400 word Part A design, present it for review, then begin the controller and fixtures after feedback | Design note and an initial learner-written implementation |
| 4. Test and explain | 90 min | Finish the controller; run the six E1 behavioral checks; explain one failure trace; complete a short knowledge check and reflection | Code, actual test evidence, reflection, and assessment |

If design feedback is pending, use that time to refine fixtures, test cases, or reading notes. Do not treat silence as design feedback. With five hours available, carry unfinished coding or review into the next week. With seven hours, use the extra hour to finish the lecture or address a demonstrated gap. Do not skip the evidence gate to meet a calendar target.

## Expected Deliverables

- Learner-authored notes on L01 and the core readings, with questions clearly distinguished from conclusions.
- `exercises/01-system-boundaries/design.md`: both control-flow sketches, responsibilities, state, limits, and failure behavior.
- A small Python controller, synthetic fixtures, and meaningful `unittest` tests in the E1 directory.
- Actual test results and a short explanation of what the scripted policy does and does not validate.

These files are expected learner outputs; they have not been created as completed work.

## Knowledge Check

1. How can a system use several model calls and still be a fixed workflow?
2. Who selects a tool, who validates the request, and who executes it?
3. Why are separate tool-execution and policy-decision limits useful?
4. What do passing scripted-policy tests fail to establish about a real model?
5. What evidence would justify replacing your fixed baseline with adaptive control?

## Completion Criteria

Explain the central concepts without substantial hints; pass the E1 tests for success, missing evidence, invalid tools, tool failure, execution-budget exhaustion, and decision-budget exhaustion; explain one trace; and apply the distinction to an unfamiliar system. The mentor records demonstrated evidence in `PROGRESS.md` and assigns targeted review where needed. Merely finishing the timetable does not complete M1.

Start now with the [initial diagnostic](../reviews/README.md#initial-diagnostic), then open the L01 slides. Homework and project implementation begin in later modules after their prerequisites and specifications have been reviewed.
