# Learning Progress

Last updated: **2026-11-23**, America/Los_Angeles.

## Learner background

The learner reports **10 years of backend engineering experience** and has built a **mini Claude Code-style coding agent**. Their work includes distributed systems, data infrastructure, and ML infrastructure. Use this experience to choose the level of instruction. Ground examples in course materials and documented open source projects.

## Current position

- Next study focus: **M3 — Tools and orchestration**. M2 remains **In Progress** for later applied retrieval evaluation.
- Next lecture: **L04 — Tool Use & Function Calling**, **Not Started**. The learner reported finishing the L03 video on November 23 and supplied a short reflection. L04 viewing has not yet been reported.
- Learning status: **In Progress**. **0/10 modules** have demonstrated completion.
- Weekly study budget: **3–4 hours**, updated at the learner's request.
- Most recent weekly plan: [Week 1 — Foundations](lectures/week-01-plan.md).
- Week 1 review material: [Questions and answers](lectures/week-01/questions-and-answers.md) and [references](lectures/week-01/references.md).
- Week 2 review material: [Questions and answers](lectures/week-02/questions-and-answers.md) and [references](lectures/week-02/references.md).
- Week 3 entry point: [Lecture 4 resources and viewing prompt](lectures/week-03/references.md).
- Next action: watch L04 and follow the boundary between a model-proposed tool call and the runtime's validation, execution, and returned observation. [Lecture 4 resources](lectures/week-03/references.md)

## Module ledger

| Module | State | Demonstrated evidence | Next gate |
|---|---|---|---|
| M1 Foundations | In Progress | Learner watched L01, summarized its main topics, and identified write access as a risk in delegating decisions | Look for evidence in later course work that the learner can explain when adaptive control earns its cost |
| M2 LLMs and RAG | In Progress | L02 and L03 videos and learner reflections are recorded; prior explanations connect KV reuse, tool errors, the embedding pipeline, and ColBERT's encoder plus MaxSim. See the [L03 reflection](lectures/week-02/questions-and-answers.md#lecture-3-reflection-and-reference-summary) | Apply retrieval metrics to a fixed query set and distinguish retrieval misses from unsupported answers in later course work |
| M3 Tools and frameworks | Not Started | L04 resources are prepared; no viewing or learning evidence yet | Watch L04, write brief notes, and trace model proposals through runtime validation and execution |
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

## Most recent study activity — L03 reflection and L04 preparation

On November 22, the learner requested a detailed explanation of Scoring a Retriever. The mentor verified the lecture's five metrics on PDF pages 45–46 and computed them on a constructed three-query dataset. Local Python arithmetic confirmed the worked scores, using the lecture's linear DCG gain. The rankings are illustrative, with no live retrieval run performed. Understanding of the evaluation metrics remains to be assessed. Continue L03 at the learner's own pace. [Retriever evaluation Q&A](lectures/week-02/questions-and-answers.md#how-does-the-lecture-score-a-retriever)

The learner then asked whether higher metric values are better. The mentor clarified that Hit, MRR, Recall, and nDCG should increase toward 1, while Failed should decrease toward 0, with comparisons holding the evaluation data and cutoff fixed. This clarification is recorded as instruction, without a new comprehension assessment.

The learner also asked whether BM25, DPR, and ANN methods are parallel alternatives. The mentor explained the roles of lexical scoring, learned dense representations, vector search indexes, and compression, with example compositions such as DPR with HNSW or IVF-PQ. These relationships have been explained; independent application remains unassessed. [Retrieval method relationships](lectures/week-02/questions-and-answers.md#are-bm25-dpr-and-ann-methods-alternatives-at-the-same-level)

The learner then asked whether another encoder can replace DPR and requested examples. The mentor checked primary documentation for BGE-M3, multilingual E5, Qwen3-Embedding, and OpenAI embedding models, and explained compatible query/passage spaces, input conventions, and re-indexing after a model change. No model was downloaded and no inference or retrieval experiment was run. The learner's understanding of embedding compatibility remains unassessed. [Embedding model alternatives](lectures/week-02/questions-and-answers.md#which-embedding-models-can-replace-dpr-upstream-of-vector-search)

The learner correctly proposed BGE-M3 with HNSW or IVF and attempted to separate lexical from dense retrieval. They still grouped ANN with embedding generation and described BM25 as only term frequency. The mentor clarified the encoder/search distinction and BM25's IDF and length normalization, and added a relationship diagram. These specific corrections have been explained, with no follow-up learner explanation yet. [Retrieval relationship diagram](lectures/week-02/questions-and-answers.md#how-do-bm25-embedding-encoders-and-vector-search-connect)

The learner moved on to ask about bi-encoders and cross-encoders. The mentor checked Lecture 3 PDF page 50, Sentence Transformers documentation, and the BGE reranker model card. The explanation covers separate and joint encoding, precomputation, pair scores, query-dependent cost, and retrieval followed by reranking. The diagrams and candidate counts are instructional, with no inference or measured quality improvement. Understanding of the new distinction remains unassessed. [Bi-encoder and cross-encoder Q&A](lectures/week-02/questions-and-answers.md#what-are-bi-encoders-and-cross-encoders-and-how-do-they-support-retrieval-and-reranking)

The learner next requested a detailed explanation of late interaction. The mentor verified the course slides, the original ColBERT architecture and MaxSim formula, and the authors' implementation. A constructed normalized-vector example gives scores 2.75 and 1.30; local Python checked the dot products, row maxima, unit norms, and illustrative raw storage arithmetic. No model inference, retrieval benchmark, or index construction was performed. The explanation distinguishes contextual token vectors, late interaction, single-vector retrieval, cross-encoding, and late chunking. Understanding of the new mechanism remains unassessed. [Late interaction Q&A](lectures/week-02/questions-and-answers.md#what-is-late-interaction-and-how-does-colbert-use-maxsim)

The learner then asked what ColBERT ultimately produces and whether training creates a retriever that can answer questions well. The mentor distinguished trained weights, token embedding matrices, pair scores, ranked evidence, and downstream answer generation. The explanation also covers positive/negative ranking supervision and using an existing checkpoint with a new corpus. These distinctions have been explained, without a new learner demonstration or model execution. [ColBERT outputs Q&A](lectures/week-02/questions-and-answers.md#what-does-colbert-produce-after-training-and-when-answering-a-search-query)

The learner first identified the encoding model as an output of ColBERT training. After clarification, they explained that a retrieval-oriented encoder plus MaxSim supports ranking and retrieval, and correctly classified ColBERT as a vector retrieval approach when comparing it with BM25. This is evidence of high-level conceptual understanding. The mentor emphasized the multi-vector representation; detailed MaxSim application and engineering tradeoffs remain unassessed. No completion state changed. [ColBERT outputs Q&A](lectures/week-02/questions-and-answers.md#what-does-colbert-produce-after-training-and-when-answering-a-search-query)

At the learner's request, the mentor added the lecture's "Fast vs Slow Retrievers" summary from PDF page 54 to the Week 02 notes. The comparison records offline representations, slide-reported latency, strengths, and limitations, with the cited experiments' different hardware and workloads made explicit. This was note maintenance; no retrieval benchmark or new comprehension assessment occurred. [Retriever comparison note](lectures/week-02/questions-and-answers.md#how-does-the-lecture-summarize-fast-and-slow-retrievers)

The learner moved into Agentic RAG and requested a step-by-step Self-RAG explanation with an example. The mentor checked the course slides, the paper's reflection categories and training/inference sections, and the authors' project and repository. The example distinguishes retrieval decisions, passage relevance, generated-claim support, usefulness, candidate selection, and repeated retrieval during segment generation. The API rules and model judgments are constructed; no model or retriever was run. The learner's understanding of Self-RAG remains unassessed. [Self-RAG Q&A](lectures/week-02/questions-and-answers.md#how-does-self-rag-combine-retrieval-generation-and-self-critique-step-by-step)

The learner requested a summary of CRAG and the remaining agentic retrieval methods. The mentor checked the official CRAG/Search-R1 sequence, the original papers' routing and learning mechanisms, Search-R1's implementation, and a ReAct review connection. The comparison distinguishes a retrieval evaluator with predefined corrective routes, supervised reflection tokens, and an RL-trained search policy. The API and dependency examples are constructed, with no model execution or measured result. These methods have been explained; learner understanding remains unassessed. [Agentic retrieval comparison](lectures/week-02/questions-and-answers.md#how-do-crag-search-r1-and-other-agentic-retrieval-patterns-differ)

On November 23, the learner reported finishing the L03 video and summarized learning what RAG is, retrieval's technical details, and generation. The mentor recorded that reflection and then added an AI reference summary. Earlier discussions demonstrate selected conceptual distinctions, while applied retrieval evaluation and independent explanation of the agentic methods remain open. M2 stays In Progress. The learner chose to continue with L04 without treating pending application work as completed. [L03 reflection](lectures/week-02/questions-and-answers.md#lecture-3-reflection-and-reference-summary)

The official schedule's L04 video and slides links were rechecked on November 23. Direct requests returned HTTP 200, and the slide response had a PDF signature. Video playback was not tested. The mentor prepared a concise viewing prompt and Week 03 resource entry; L04 learning remains Not Started until viewing or another study activity is reported. The learner explicitly authorized committing and pushing the current notes. [L04 entry point](lectures/week-03/references.md)

## Recording future evidence

Use **Not Started**, **In Progress**, **Needs Review**, or **Completed**. Add dated links to learner answers, artifacts, actual test commands/results, rubric scores where assessable, remaining gaps, and the next action. Mark a lecture complete only after a comprehension check; mark a module complete only after its application and transfer gates. Record watched/read activities without treating them as mastery.
