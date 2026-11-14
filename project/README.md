# Final Project Planning and Milestones

**State: Not Started. No project selected.** The learner chooses the direction after comparing alternatives. This document is planning guidance, not a course project report or an approved proposal.

## Candidate Discussion

These are mentor-proposed directions tailored to backend, inference, and evaluation interests. They are not selected projects or claims of research novelty. Feasibility assumes a narrow scope and synthetic/permitted data; confirm it through a baseline experiment.

| Direction | Learning value | Complexity | Originality opportunity | Feasibility | Evaluation approach | Portfolio value |
|---|---|---|---|---|---|---|
| Agent evaluation and trace-debugging tool | Graders, observability, reproducibility | Moderate | Useful failure taxonomy or debugging workflow | Strong for a scoped local tool | Known seeded failures, grader agreement, debugging tasks | Demonstrates systems and evaluation depth |
| Read-only incident/runbook assistant | Retrieval, tools, memory, permissions | Moderate | Domain-specific failure recovery and evidence quality | Strong with synthetic incidents | Grounded answers, tool correctness, abstention, latency | Connects backend expertise to agents |
| Small repository maintenance agent | Tool interfaces, code repair, sandboxing | Higher | Narrow maintenance task with rigorous baselines | Moderate; limit repository and task families | Hidden tests, patch review, budget and failure analysis | Familiar developer-facing use case |
| Reproducible technical research assistant | Retrieval, provenance, long task state | Moderate to higher | Source verification or citation-quality method | Moderate; bound sources and queries | Evidence support, coverage, citation errors, cost | Clear demo if claims are objectively tested |

Compare learning value, engineering effort, originality, feasibility, evaluation quality, and portfolio relevance before choosing. A two-role or multi-agent design must earn its complexity against a simpler baseline.

## Official Course Milestones

The [project page](https://cs329z.stanford.edu/project.html) specifies a proposal (1–2 pages), midway report (3–4 pages) with recorded prototype demo, and final report (8 pages) with final demo. Reports use ICLR format; references are excluded from these page limits. A code repository and runnable README accompany the midpoint and final stages. AI-use disclosure is required at every report stage; the final report also requires safety/ethics and authorship statements. Recheck the current specification before submission.

The [logistics policy](https://cs329z.stanford.edu/logistics) prohibits AI-written project reports. The learner writes submission prose. The mentor may help brainstorm, pose outline questions, critique drafts, and rehearse a defense. Record AI contributions accurately; disclosure does not waive the writing restriction.

Course dates are reference context. This self-study project advances by the evidence gates below.

## Self-Study Milestones and Gates

| ID | Stage | Evidence required to advance |
|---|---|---|
| P0 | Problem selection, M2–M3 | Compare at least two candidates; state intended user, concrete task, scope, constraints, and why a simpler solution may suffice |
| P1 | Evaluation-first proposal, M3 | Define representative tasks, data provenance, success/failure criteria, metric, simple baseline, budget, and a learner-authored proposal outline |
| P2 | Baseline, M4–M5 | Runnable simple implementation, meaningful tests, trace contract, and baseline measurements on development tasks |
| P3 | Midpoint, M6–M7 | Working prototype, defined dataset/splits, repeatable experiment configuration, preliminary comparison, failure examples, and a demo; learner writes the midway report |
| P4 | Evidence and hardening, M8–M9 | Frozen held-out evaluation, calibrated graders where needed, repeated trials/uncertainty, an ablation, failure taxonomy, and permission/privacy tests |
| P5 | Final integration, M10 | Clean setup reproduction, one-command small evaluation, full results with limitations, final demo, learner-authored final report/disclosures, and oral defense |

Track each milestone separately in `PROGRESS.md`. A lecture's completion never automatically completes a project milestone. If the idea changes, revise the problem and evaluation before expanding implementation.

## Definition of a Portfolio-Ready Result

The finished original project should have a clear problem and architecture rationale; a working implementation; automated tests; permitted evaluation tasks/data; appropriate baselines; quantitative and qualitative findings; failure analysis; reproducible installation/configuration/run/evaluation instructions; limitations; and justified future work. Include actual software/model/data/scorer versions and budget information.

Test the README from a clean environment and run one documented evaluation case. Distinguish that quick-start check from reproducing every reported result. Explain data/model access limitations and provide synthetic fixtures when private data cannot be distributed. Remove credentials and raw private traces from publishable artifacts.

An honest negative result can be valuable. A polished demo with no evidence of reliability is insufficient. Do not claim originality until related work has been examined, and do not choose a project merely because its framework is fashionable.

## Questions for the Learner-Authored Proposal

Who experiences the problem? What is one concrete task? What is the smallest useful baseline? Which uncertain step requires an LLM or adaptive control? How will the environment be reset? What counts as success and what can a scorer miss? What data is permitted? What can fit within the weekly budget? What result would make you abandon or simplify the idea?

Future AI-use records should identify the date, tool, specific assistance, learner verification, and affected artifact. Initialization assistance has so far created planning documents only; no project code, experiments, results, or report text has been produced.
