# Learning Progress

Last updated: **2026-11-15**, America/Los_Angeles.

## Learner background

The learner reports **10 years of backend engineering experience** and has built a **mini Claude Code-style coding agent**. Their work includes distributed systems, data infrastructure, and ML infrastructure. Use this experience to choose the level of instruction. Ground examples in course materials and documented open source projects.

## Current position

- Next module: **M2 — Models and retrieval**.
- Next lecture: **L02 — LLMs for Builders**, **Not Started**.
- Learning status: **In Progress**. **0/10 modules** have demonstrated completion.
- Weekly study budget: **3–4 hours**, updated at the learner's request.
- Most recent weekly plan: [Week 1 — Foundations](lectures/week-01-plan.md).
- Week 1 review material: [Questions and answers](lectures/week-01/questions-and-answers.md) and [references](lectures/week-01/references.md).
- Next action: start the L02 lecture. [Course materials](resources/course-materials.md#l02)

## Module ledger

| Module | State | Demonstrated evidence | Next gate |
|---|---|---|---|
| M1 Foundations | In Progress | Learner watched L01, summarized its main topics, and identified write access as a risk in delegating decisions | Look for evidence in later course work that the learner can explain when adaptive control earns its cost |
| M2 LLMs and RAG | Not Started | None yet | Structured I/O and retrieval error analysis |
| M3 Tools and frameworks | Not Started | None yet | Bounded tool dispatcher and framework mapping |
| M4 Patterns and memory | Not Started | None yet | Explain and test context and memory behavior |
| M5 Multi-agent systems and optimization | Not Started | None yet | Controlled comparison with a simpler baseline |
| M6 Agent data | Not Started | None yet | Trace dataset, provenance, and leakage checks |
| M7 Evaluation | Not Started | None yet | Reproducible task specifications and scorers |
| M8 Judges and infrastructure | Not Started | None yet | Calibrated judge and robust evaluation harness |
| M9 Safety and reliability | Not Started | None yet | Adversarial tests and enforced permissions |
| M10 Coding/personal agents and integration | Not Started | None yet | Cumulative assessment and project defense |

## Activities and exercises

**Completed administration:** initialized the study workspace, verified the Fall 2026 resources, and published the initial version at `6b1f9e6`. Recorded the learner's experience and revised the plan to center course material, official assignments, and a project.

**Course evidence:** the learner reported finishing L01 and reflected on agent history, components, CoT, ReAct, reflection, multiple roles, interactions with external systems, and challenges. They correctly identified chain-of-thought prompting as a prompting technique. When asked when a model should choose the next action, they proposed read-only operations as a lower-risk starting point and expressed uncertainty about the broader criterion.

**Deferred at the learner's request:** independent reading and comparison of accuracy and API cost. The mentor supplied a summary and reference answer. [Optional paper review](lectures/week-01/references.md#optional-reading-and-comparison)

## Assignment and presentation milestones

| Milestone | State | Evidence / next action |
|---|---|---|
| HW1 specification and architecture | Not Started | Read current handout during M3; learner proposes architecture |
| HW1 implementation and tests | Not Started | Complete incrementally through M4–M6 |
| HW1 oral defense | Not Started | Explain implementation, failures, and tradeoffs |
| HW2 specification and evaluation design | Not Started | Orient during M6; design through M7–M8 |
| HW2 experiments and error analysis | Not Started | Preserve task/model/scorer versions and actual run evidence |
| HW2 oral defense | Not Started | Defend measurement validity and conclusions |
| Paper selection and presentation | Not Started | Shortlist after M4; explain evidence before recording |
| Peer-review practice | Not Started | Use legitimate materials; track separately from Stanford submissions |

## Project milestones — tracked independently

No project has been selected. All milestones are **Not Started**.

| ID | Milestone | Target learning stage |
|---|---|---|
| P0 | Compare candidate problems and choose one | M2–M3 |
| P1 | Define scope, evaluation tasks, baseline, and proposal outline | M3 |
| P2 | Reproducible baseline, trace format, and initial tests | M4–M5 |
| P3 | Prototype, evaluation data, and midpoint demo | M6–M7 |
| P4 | Held-out evaluation, grader calibration, ablations, safety checks | M8–M9 |
| P5 | Final demo, reproducibility audit, learner-authored report, defense | M10 |

## Knowledge gaps and review queue

Review two questions separately. Does interpreting the observation help the system choose a better next step? What actions may the system actually execute? Revisit these decisions when they come up in course work. [Review note](lectures/week-01/questions-and-answers.md#when-is-it-worth-letting-the-model-decide-the-next-action-after-a-tool-result)

Project choice and model budget remain open for later milestones.

## Most recent study activity — L01 reflection

The learner summarized L01 and identified read-only operations as candidates for safe delegation. The mentor explained when interpreting a tool result can make model-directed branching useful. The learner chose to defer the paper reading and comparison, and the mentor supplied a worked answer. The next lecture is L02.

## Recording future evidence

Use **Not Started**, **In Progress**, **Needs Review**, or **Completed**. Add dated links to learner answers, artifacts, actual test commands/results, rubric scores where assessable, remaining gaps, and the next action. Mark a lecture complete only after a comprehension check; mark a module complete only after its application and transfer gates. Record watched/read activities without treating them as mastery.
