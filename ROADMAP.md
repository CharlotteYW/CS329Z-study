# CS329Z Learning Roadmap

Aligned with the [official Fall 2026 schedule](https://cs329z.stanford.edu/), checked **2026-11-13**. The [resource index](resources/course-materials.md) supplies verified links and availability for every scheduled instructional event. This roadmap adds mentor-designed exercises and mastery gates; these are not Stanford grading requirements.

## Pace, sequence, and learning strategy

The confirmed budget is **5–7 hours per week**. A typical week allocates about two hours to lectures/readings, two or three to implementation, one to explanation and review, and an optional hour to catch-up. Stop a session at a useful boundary rather than rushing a whole lecture or paper.

Ten modules organize the actual curriculum; a module can occupy several study weeks. The module estimates total **77–99 hours** for focused study, exercises, and assessments. Separately budget HW1 **18–26 hours**, HW2 **14–22 hours**, the project **30–45 hours**, and paper presentation/review **4–6 hours**: roughly **143–198 hours overall**, or **21–40 study weeks** at the chosen pace. These are mentor estimates, not course expectations or deadlines. Refine them after M1 and the HW1 specification review. Reuse demonstrated work where it meets a gate instead of duplicating exercises and homework.

Use a repeated cycle: predict behavior, study a primary source, build the smallest useful component, test failures, explain the tradeoff, and transfer the idea to a new problem. Preserve a simple baseline. Diagnose failures before adding frameworks, agents, or model calls.

**Reading labels:** "Required" below means required for this self-study plan, at the stated depth. The course labels most entries simply "Readings" and some "Additional readings"; do not turn that into an unsupported official mandate. All other course-listed readings remain available as optional deeper study. A first pass should identify the mechanism, a key experiment, and a limitation; derivations or full replication are only needed when relevant to an exercise. No optional reading blocks progress.

| Module | Official events, in order | Course week | Study effort |
|---|---|---|---|
| M1 Foundations | L01 | 1 | 5–7 h |
| M2 LLMs and RAG | L02–L03 | 2 | 10–14 h |
| M3 Tools and frameworks | L04–L05 | 3 | 8–10 h |
| M4 Patterns and memory | L06–L07 | 4 | 10–12 h |
| M5 Multi-agent systems and optimization | L08–L09 | 5 | 8–10 h |
| M6 Data, with Terminal-Bench introduction | L10–L12 | 6–7 | 6–8 h |
| M7 Evaluation | L13 | 7 | 8–10 h |
| M8 Judges and infrastructure, with guest sessions | L14–L16 | 8–9 | 8–10 h |
| M9 Safety and reliability | L17 | 9 | 6–8 h |
| M10 Coding/personal agents and integration | L18–L19 | 11 | 8–10 h |

The Terminal-Bench guest session stays before the data lectures. The Andrew Ng fireside chat stays before the judge lecture, and the SWE-bench guest session stays before safety. Their concepts are revisited later without changing the initial study order. The Thanksgiving break adds no module. Unavailable talks receive explicit self-study substitutes, never invented summaries.

## Shared completion standard

A module is **Completed** only when the learner can explain its central concepts, produce its deliverables, verify its practical behavior, and handle one unfamiliar transfer case. Use the [diagnostic rubric](reviews/README.md): generally at least 3/4 on each assessable dimension, with no unresolved essential correctness or safety failure. A dimension without evidence remains unassessed; an average cannot hide it. These thresholds are mentor-defined and adjustable based on evidence.

Record actual artifacts, test commands/results, answers, and feedback in `PROGRESS.md`. Completion of a source-reading activity is distinct from mastery. A properly measured negative experimental result can satisfy a gate; a claimed improvement without evidence cannot.

## M1 — Foundations of Agentic Systems

**Why and objectives:** Understand where model behavior ends and system behavior begins. Distinguish compound systems, fixed workflows, and model-directed control. Identify the policy/model, tools, state, environment, observations, and stopping rules. Explain why adding autonomy changes failure handling and operational cost.

**Prerequisites:** Existing backend engineering experience. Basic familiarity with LLM input/output; deeper knowledge is assessed rather than assumed.

**Official lecture:** [L01 — Introduction: What Are Agentic Systems?](resources/course-materials.md#l01).

**Required readings:** BAIR's compound-systems article; Weng's agent overview and component sections; *AI Agents That Matter* abstract, introduction, and one evaluation example. Explain each reading's main claim in your own words.

**Optional readings:** Weng's case studies and the remaining methods/results of *AI Agents That Matter*. All links are in L01; do not treat old example frameworks as installation recommendations.

**Practical exercise E1:** [System boundaries](exercises/01-system-boundaries/README.md).

- **Objective:** Make control flow and stopping behavior explicit.
- **Requirements:** Compare a fixed incident-triage workflow with a policy-directed loop; implement the controller using a scripted policy and local fixtures.
- **Constraints:** Python standard library, no model, no framework, no real incident actions. Learner writes the solution.
- **Success criteria:** Trace who chose each action, terminate within a budget, and explain why a scripted test double does not demonstrate LLM competence.
- **Tests:** Normal answer, missing evidence, invalid tool, simulated tool failure, repeated-action budget exhaustion.
- **Reflection:** When does adaptive control justify its extra complexity?

**Expected deliverables:** A one-page architecture comparison, a small controller and tests, and a short own-words lecture summary.

**Assessment:** Is every RAG system an agent? Who selects a tool versus executes it? How can accurate model outputs still yield a failed task? What would you measure besides success rate?

**Completion criteria:** Correctly classify three unfamiliar systems with reasons; defend a baseline; pass the E1 behavioral tests; explain one failure trace without hints. **Effort:** 5–7 hours. Start with the [75-minute session](lectures/01-foundations.md).

## M2 — LLMs for Builders and RAG

**Why and objectives:** Learn which inference and retrieval decisions control answer quality, latency, and cost. Explain decoding, attention/context limits, structured outputs, and the role of pretraining versus post-training at a builder's level. Trace indexing, BM25, embeddings, hybrid retrieval, reranking, and answer generation; separate retrieval failures from synthesis failures.

**Prerequisites:** M1 control-flow and baseline reasoning; basic vector similarity and precision/recall, with a short refresh if needed.

**Official lectures:** [L02 — LLMs for Builders](resources/course-materials.md#l02), then [L03 — RAG](resources/course-materials.md#l03).

**Required readings:** *Attention Is All You Need* architecture and attention sections; *Effective Context Engineering for AI Agents*; the RAG paper's architecture and one experiment; DPR and ColBERT abstracts/mechanisms as a retrieval comparison.

**Optional readings:** Linear-attention paper; deeper DPR/ColBERT experiments and indexing details. Distinguish approximate-nearest-neighbor indexing from the retrieval model itself.

**Practical exercise E2:** Build a tiny evidence-grounded runbook assistant.

- **Objective:** Localize errors across the retrieval/generation boundary.
- **Requirements:** Use 15–30 synthetic documents and at least 10 labeled questions; build a lexical baseline, then compare one embedding or hybrid variant. Validate structured answers and source IDs; support abstention.
- **Constraints:** Start with a plain Python pipeline. Use a small local model or a bounded hosted run only after discussing resources; use scripted responses for deterministic tests. A simple lexical baseline is not to be mislabeled BM25.
- **Success criteria:** Report retrieval recall@k separately from supported-answer quality, with latency and actual model-call counts. Compare on the same held-out queries.
- **Tests:** Empty retrieval, exact identifiers, paraphrases, contradictory documents, invalid JSON, valid JSON with unsupported facts, and oversized context.
- **Reflection:** Which bottleneck would a larger model fail to fix?

**Expected deliverables:** Dataset and provenance, pipeline code, tests, comparison table, and categorized failures. Begin project problem discovery without choosing for the learner.

**Assessment:** Why can constrained decoding produce a valid but wrong answer? When does BM25 beat embeddings? What can reranking repair? Why is a longer context not equivalent to reliable recall?

**Completion criteria:** Trace a failed answer to a component; justify retrieval/latency choices; reproduce the comparison; explain attention/context implications without needing to train a model. **Effort:** 10–14 hours.

## M3 — Tool Use and Agent Frameworks

**Why and objectives:** Separate tool descriptions, action selection, argument validation, execution, and observations. Implement a bounded loop and explain the responsibilities that remain outside the model. Relate REST/function calling/MCP interfaces to orchestration. Map plain Python behavior to LangGraph and DSPy abstractions.

**Prerequisites:** M1–M2, structured outputs, exceptions, and basic service retry semantics.

**Official lectures:** [L04 — Tool Use & Function Calling](resources/course-materials.md#l04), then [L05 — Frameworks & Orchestration](resources/course-materials.md#l05). L05 includes an official code repository.

**Required readings:** Toolformer mechanism and evaluation; MCP **2025-06-18** architecture/tool concepts; DSPy signatures/modules and optimization motivation; LangGraph overview.

**Optional readings:** Gorilla; HarnessTax; remaining official framework-demo code. Current APIs must be checked before implementation.

**Practical exercise E3:** Add a validated dispatcher to the runbook assistant.

- **Objective:** Make tool boundaries testable independently of a model.
- **Requirements:** Register two read-only tools; validate calls; return structured success/error observations; enforce time/step budgets; record action IDs and outcomes.
- **Constraints:** Implement the first version without an agent framework. Then make a small separate framework comparison; never import it into HW1.
- **Success criteria:** No unknown tool or malformed call reaches execution; retries have explicit limits; explain state/node/edge and signature/module mappings.
- **Tests:** Wrong argument types, nonexistent tool, timeout, exception, repeated call, and stop request. Discuss a hypothetical non-idempotent tool before deciding whether retry is safe.
- **Reflection:** Which failures belong to the model, harness, interface, or external service?

**Expected deliverables:** Dispatcher, test traces, abstraction comparison, and a learner-authored HW1 architecture sketch after reading its handout. Project P0/P1: choose a problem and define initial evaluation tasks.

**Assessment:** Does MCP make a tool safe or select it? Where should permissions live? What survives a process restart? When is a framework worth adopting?

**Completion criteria:** Pass the failure tests; explain the loop unaided; justify a framework decision against the plain implementation; review HW1 constraints before starting it. **Effort:** 8–10 hours, excluding official homework.

## M4 — Agent Design Patterns and Memory

**Why and objectives:** Choose a workflow or agent pattern based on task uncertainty. Understand ReAct and alternatives such as Reflexion, CodeAct, and ReWOO without treating a pattern name as a guarantee. Distinguish working, episodic, semantic, and procedural memory; manage context, persistence, retention, and invalidation.

**Prerequisites:** M3 loop, tool observations, and state transitions; backend persistence concepts.

**Official lectures:** [L06 — Agent Design Patterns & Scaffolds](resources/course-materials.md#l06), then [L07 — Agent Memory Architectures](resources/course-materials.md#l07).

**Required readings:** ReAct; *Building Effective AI Agents*; *Cognitive Architectures for Language Agents* taxonomy; MemGPT's memory mechanism. Study one relevant experiment from each research paper rather than only its abstract.

**Optional readings:** Context Engineering, Reflexion, CodeAct, and Generative Agents from the course list.

**Practical exercise E4:** Add budgeted context and scoped memory.

- **Objective:** Test when remembered information helps or harms task completion.
- **Requirements:** Store provenance and timestamps; distinguish durable records from current context; support correction and deletion; compare full history with a bounded context strategy.
- **Constraints:** Start with local JSON/SQLite. Keep user/task scopes separate. Log actions and concise observable decisions; do not assume a model exposes faithful hidden reasoning.
- **Success criteria:** Demonstrate persistence, correction, isolation, deletion, and explicit behavior when a needed fact is dropped. Compare to a stateless baseline.
- **Tests:** Restart, stale/conflicting records, token-budget pressure, deletion, and cross-user lookup denial.
- **Reflection:** Is retrieved history knowledge, evidence, instruction, or untrusted data in this case?

**Expected deliverables:** Memory contract, tests, context comparison, and failure analysis. Continue HW1 incrementally; shortlist a research paper. Project P2 begins with a simple baseline.

**Assessment:** Does reflection update model weights? When should an observation be masked instead of summarized? What distinguishes semantic memory from a chat log? How can compaction change correctness?

**Completion criteria:** Defend a pattern choice for a new task; explain all four memory types; pass isolation/deletion and budget tests; analyze a case where memory reduces quality. **Effort:** 10–12 hours, excluding HW1.

## M5 — Multi-Agent Systems and Optimization

**Why and objectives:** Decide whether specialization or parallelism justifies coordination overhead. Explain handoffs, shared state, isolated workspaces, task ownership, and failure propagation. Compare prompt/context optimization with weight optimization; understand SFT/RL at the architectural level without requiring large training runs.

**Prerequisites:** M3–M4 and a working single-controller baseline; held-out evaluation concepts from M2.

**Official lectures:** [L08 — Multi-Agent Systems](resources/course-materials.md#l08), then [L09 — Optimization](resources/course-materials.md#l09).

**Required readings:** AutoGen architecture; *Why Do Multi-Agent LLM Systems Fail?* failure taxonomy; GEPA's optimization loop and a controlled result; MIPRO's instruction/demonstration search mechanism.

**Optional readings:** *Towards a Science of Scaling Agent Systems*; DeepSeekMath for the GRPO motivation and limits. Large-scale weight training is not required self-study work.

**Practical exercise E5:** Compare one controller with a two-role design.

- **Objective:** Identify where a measured gain comes from.
- **Requirements:** Evaluate both on the same tasks and a comparable total-call/token budget; add an explicit handoff protocol. Tune one prompt using development data only, then freeze it before held-out evaluation.
- **Constraints:** Use existing components; a deterministic two-worker simulation is acceptable preparation, but cannot establish model-quality gains. No automatic implementation by the mentor.
- **Success criteria:** Report quality, cost, latency, coordination failures, and uncertainty; include a matched-budget baseline and an ablation.
- **Tests:** Duplicate work, missing handoff, conflicting answers, stalled worker, exhausted budget, and train/test overlap.
- **Reflection:** Would a single agent with extra calls obtain the same gain?

**Expected deliverables:** Experiment configuration, result table, trace examples, and a decision to keep or reject added complexity. Continue project P2.

**Assessment:** When is more parallelism slower? Who owns shared state? How does optimizer overfitting arise? When is prompt optimization preferable to fine-tuning?

**Completion criteria:** Reproduce the comparison and defend its fairness; localize a coordination failure; explain why an inconclusive or negative result does not justify claiming improvement. Include one M1–M4 transfer question. **Effort:** 8–10 hours.

## M6 — Data for Agentic Systems

**Why and objectives:** Treat traces and feedback as datasets with provenance and failure modes. Separate demonstrations, synthetic examples, optimization data, and evaluation data. Reason about selection quality, coverage, annotation disagreement, and feedback loops. Introduce realistic terminal tasks before formal evaluation design in M7.

**Prerequisites:** Observable tool runs and M5 development/test separation.

**Official events:** [L10 — Terminal-Bench guest lecture](resources/course-materials.md#l10), [L11 — What Data Do Agents Need?](resources/course-materials.md#l11), then [L12 — Data Selection & Quality](resources/course-materials.md#l12).

**Required readings:** Terminal-Bench project/task overview and paper evaluation setup; Data Flywheels; SWE-smith's generation/validation mechanism; *Who Validates the Validators?* study design and findings.

**Optional readings:** Data Annotation and Synthesis survey; LIMA. Do not equate a small pedagogical dataset with evidence about population performance.

**Practical exercise E6:** Build a small trace-derived dataset.

- **Objective:** Produce inspectable data for improvement and evaluation.
- **Requirements:** Curate at least 20 small traces; label tool/retrieval/control/answer failures; record provenance, task family, label rationale, and split. Identify simulated versus model-generated records.
- **Constraints:** Synthetic or permitted non-sensitive data only. Split by task family/source as appropriate, not blindly by row; keep final test data out of optimization.
- **Success criteria:** Reconstruct each example's origin; explain inclusion/exclusion decisions; double-label five cases and inspect disagreement without claiming population-level annotation reliability.
- **Tests:** Missing provenance, duplicates across splits, missing labels, sensitive fields, and near-duplicate task templates.
- **Reflection:** What important failure would the sampling procedure systematically miss?

**Expected deliverables:** Versioned small dataset, dataset card, validator, and label audit. Complete HW1 review/defense if its evidence is ready; orient to HW2's handout. Project P3 begins.

**Assessment:** Why can synthetic data reinforce errors? How can traces leak answers into test sets? Which examples are useful for optimization but misleading for evaluation?

**Completion criteria:** Pass schema/leakage checks; defend the split and selection; explain a disputed label and one coverage gap. **Effort:** 6–8 hours, excluding homework/project work.

## M7 — Agent Evaluation

**Why and objectives:** Turn a vague claim of capability into an executable experiment. Specify request, environment, stopping criteria, and scorer. Distinguish task outcome from process quality, benchmark difficulty from realism, and sampling variation from genuine improvement.

**Prerequisites:** M6 dataset provenance, M3 budgets, basic success-rate arithmetic; refresh uncertainty estimates as needed.

**Official lecture:** [L13 — Evaluation Fundamentals & Benchmark Design](resources/course-materials.md#l13).

**Required reading:** *Establishing Best Practices for Building Rigorous Agentic Benchmarks*, focusing on task construction, validity, and reproducibility. Revisit the critique in *AI Agents That Matter* from M1.

**Optional readings:** *How to Build Good Language Modeling Benchmarks* and tinyBenchmarks.

**Practical exercise E7:** Specify and run a small task suite.

- **Objective:** Make success independently measurable.
- **Requirements:** Define at least 10 varied tasks with all four components; implement deterministic graders for objective outcomes; reset the environment between runs; include a simple baseline and several repeated trials.
- **Constraints:** Use mock/local tasks initially. Pin model/configuration/data versions when real calls are introduced. Choose a feasible repeat count before observing results; report small-sample limits.
- **Success criteria:** Another person can rerun one task; reports include denominators, retries, timeouts, tool/model budgets, and failure categories.
- **Tests:** Known correct/incorrect outputs, a superficial answer that games a naive scorer, environment contamination, timeout, and grader exceptions.
- **Reflection:** Does the score measure the user's goal or an easily optimized proxy?

**Expected deliverables:** Task specifications, graders, run manifest, uncertainty discussion, and an error-analysis table. Develop HW2 evaluation design and project P3 evaluation tasks.

**Assessment:** Can an improved success rate be caused only by a larger retry budget? Is a timeout an agent or harness failure? What changes when the deployment environment differs from the benchmark?

**Completion criteria:** Defend all four components for two unfamiliar tasks; reproduce one run; catch a scorer-gaming case; state exactly what the results do and do not support. **Effort:** 8–10 hours.

## M8 — LLM-as-Judge and Evaluation Infrastructure

**Why and objectives:** Decide when deterministic, human, or model grading fits the construct being measured. Calibrate judges against labeled examples, identify bias, and build a harness that records failures instead of hiding them. Distinguish pass@k from pass^k and per-attempt success.

**Prerequisites:** M7 benchmark design, repeated trials, and independent test data.

**Official events:** [L14 — Andrew Ng fireside chat](resources/course-materials.md#l14), [L15 — LLM-as-Judge & Evaluation Infrastructure](resources/course-materials.md#l15), then [L16 — SWE-bench guest lecture](resources/course-materials.md#l16). L14 has no public resources: substitute a reflection on prior material and record the talk as unavailable, not watched. Until L16 materials are released, its linked paper supplies a legitimate reading-based substitute.

**Required readings:** *Demystifying Evals for AI Agents*; MT-Bench/Chatbot Arena judge calibration and bias experiments; AutoMetrics mechanism; SWE-bench task/environment/scoring design.

**Optional reading:** AutoLibra, using the verified preprint if OpenReview remains inaccessible.

**Practical exercise E8:** Calibrate a judge and harden the evaluation runner.

- **Objective:** Measure the evaluator's errors and run integrity.
- **Requirements:** Label at least 20 varied outputs; separate rubric-development examples from a small held-out audit; compare human labels with a model judge; include pairwise order swaps and verbosity controls. Log run/task/trial/model/prompt/scorer versions.
- **Constraints:** Use deterministic graders where possible. Judge candidates are untrusted inputs. A small audit is instructional and does not prove deployment readiness.
- **Success criteria:** Report disagreement cases, uncertainty, order sensitivity, and malformed outputs; treat failed grading explicitly. Show pass@k and pass^k on a transparent repeated-trial example without conflating them.
- **Tests:** Judge prompt injection, malformed scores, timeouts, duplicate/resumed runs, position bias probes, and changed scorer versions.
- **Reflection:** What evidence would make you stop trusting this judge?

**Expected deliverables:** Rubric, labeled audit set, calibration results, harness tests, HW2 analysis/defense when ready, and a paper-presentation rehearsal. Project P4 begins.

**Assessment:** Does high average judge agreement hide rare severe failures? Why can larger k raise pass@k while lowering pass^k? How do you compare runs when models or graders change?

**Completion criteria:** Explain disagreement sources; reproduce the audit; distinguish scorer error from agent error; defend repeat-run semantics. Include a cumulative retrieval/tool-use debugging case. **Effort:** 8–10 hours.

## M9 — Agent Safety and Reliability

**Why and objectives:** Model the boundary between authorized instructions and untrusted content. Understand direct/indirect prompt injection, privacy leakage, tool permissions, sandboxing, guardrails, and human review. Enforce consequential-action policy outside model text and measure residual risk.

**Prerequisites:** M3 tool dispatcher, M4 state isolation, and M7–M8 adversarial evaluation.

**Official lecture:** [L17 — Agent Safety & Guardrails](resources/course-materials.md#l17). Slides/video were not linked on the verification date; recheck, then use the assigned readings if still unavailable.

**Required readings:** PrivacyLens; privacy-risk simulation paper; the deanonymization paper's threat model and evaluation limitations. Discuss these analytically using synthetic data only.

**Optional readings:** Contextualized Privacy Defense, OpenAI's prompt-injection article, and the course-linked Responsible Scaling Policy article. Separate an organizational scaling policy from controls in a local application.

**Practical exercise E9:** Threat-model and test the existing assistant.

- **Objective:** Reduce unsafe behavior without hiding task failures.
- **Requirements:** Identify assets, actors, trust boundaries, and permitted actions; add a tool allowlist, scoped data access, and an approval state for a simulated consequential action.
- **Constraints:** Synthetic canary secrets and isolated fixtures only; never run attacks against third parties or real private data. Approval applies to a concrete action and arguments.
- **Success criteria:** Code denies prohibited actions even if a model requests them; approval cannot silently authorize changed arguments. Report unsafe-action rate and benign-task success separately.
- **Tests:** Malicious retrieved instructions, forged approval, altered arguments, cross-user memory access, secret exfiltration attempts, and legitimate requests.
- **Reflection:** Which protections are deterministic, which are probabilistic, and what remains untested?

**Expected deliverables:** Threat model, enforced controls, adversarial regression suite, and residual-risk analysis for project P4.

**Assessment:** Can a stronger system prompt replace permissions? What does a sandbox fail to prevent? How can a seemingly helpful proactive action violate privacy expectations?

**Completion criteria:** Demonstrate enforced boundaries in tests; explain one failed defense and its fix; assess the cost to legitimate use; avoid claiming complete prompt-injection immunity. **Effort:** 6–8 hours.

## M10 — Coding Agents, Proactive Agents, and Final Project

**Why and objectives:** Integrate agent-computer interfaces, repository exploration, code edits, tests, stopping conditions, and evaluation. Explain when a personal agent should initiate, ask, or wait. Deliver an original project with evidence strong enough for another engineer to critique and reproduce.

**Prerequisites:** M1–M9, project baseline and evaluation plan. Revisit L16's SWE-bench discussion rather than moving it out of course order.

**Official lectures:** [L18 — Coding & Software Agents](resources/course-materials.md#l18), then [L19 — Personal Agents](resources/course-materials.md#l19). Use linked papers if lecture media remain unavailable.

**Required readings:** SWE-agent's interface design and ablations; OpenHands architecture; GUM's user-model construction and evaluation. Consult the official project specification before milestone review.

**Optional readings:** Course-linked Claude Code practices, long-running harness article, next-action prediction paper, and OpenClaw repository inspection. No broad desktop permissions or installation are needed merely to study these architectures.

**Practical exercise E10:** Compare agent interfaces in a small disposable repository, then design a proactive policy.

- **Objective:** Connect interface choices to measurable coding and user-impact outcomes.
- **Requirements:** Define at least three small repair tasks with tests; isolate workspaces; record patches, tool failures, budgets, and final test outcomes. Draft a policy for five synthetic events deciding whether to initiate, ask, or wait.
- **Constraints:** Use small local fixtures and no external side effects. Keep hidden evaluation tests separate from agent-visible feedback. A tiny coding suite is not a SWE-bench leaderboard result.
- **Success criteria:** Compare to a simple baseline; reproduce one repair; explain false successes, changed tests, interruption, and unnecessary proactive actions.
- **Tests:** Passing tests with an incorrect patch, modification of evaluation files, timeout, restart, canceled intent, and an event requiring confirmation.
- **Reflection:** Which interfaces improve capability, and which merely expose more authority?

**Expected deliverables:** Coding-task comparison, proactive-action policy, final project P5 artifacts, reproducibility evidence, and learner-authored report. The mentor supplies outline guidance and feedback only.

**Assessment:** Why can an agent pass visible tests yet fail the task? What makes a coding-agent baseline fair? How do you evaluate unnecessary interventions? Which project conclusion is most vulnerable to confounding?

**Completion criteria:** Pass the cumulative oral defense; satisfy the [project gates](project/README.md); reproduce a clean setup and one evaluation case; defend baselines, uncertainty, failures, limitations, and next improvements. If project evidence is incomplete, retain **In Progress** even if both lectures are understood. **Effort:** 8–10 hours plus remaining project work.

## Parallel milestones and review rhythm

The [assignment guide](assignments/README.md) specifies how HW1 and HW2 enter this plan. Their original Stanford dates do not determine personal completion. Read their full current handouts before implementation, including framework, environment, privacy, and submission restrictions.

Project selection starts in M2–M3; evaluation design starts before the full implementation. See [project milestones](project/README.md). Research-paper selection starts after M4, with explanation/rehearsal through M8; use the [paper-reading protocol](readings/README.md).

At every module boundary, assess concepts, architecture, code reasoning, debugging, and transfer. At M3, M5, M8, and M10 include earlier material. Write one targeted remediation task for each demonstrated gap and recheck it in the next session. Keep mastered material moving forward.
