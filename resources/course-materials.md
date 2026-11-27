# Course Materials — Stanford CS329Z, Fall 2026

Verified on **2026-11-13 (America/Los_Angeles)** against the live official site. This is a resource index, not a claim that the learner or mentor has studied every item. The schedule is tentative. Recheck the relevant sources at each module and assignment milestone.

## Source and access conventions

- **Official reading:** listed under the schedule's general Readings label. The site does not label this entire category mandatory. The roadmap identifies the mentor-required study subset and depth.
- **Official additional reading:** listed in the schedule's Additional readings section.
- **Reachable:** endpoint returned HTTP 200 and metadata or a PDF header was checked. This does not establish full content review or video playback.
- **Not linked:** no resource of that type was published in the checked schedule; this is not proof that no recording exists.
- **Restricted/unavailable:** content could not be accessed through this check. Use the explicit alternative; do not bypass access controls.
- L01–L19 are local chronological event IDs, including guest sessions; PDF filenames are preserved from the site rather than inferred.

Raw per-link status, redirects, and titles: [link-checks.json](link-checks.json).

## Official entry points

| Resource | Verified link | Availability |
|---|---|---|
| Syllabus and schedule | [Course](https://cs329z.stanford.edu/) | Public; explicitly Fall 2026 |
| Policies and coursework | [Logistics](https://cs329z.stanford.edu/logistics) | Public |
| Project specification | [Project](https://cs329z.stanford.edu/project.html) | Public |
| HW1 starter | [assignment1-harness](https://github.com/cs329z/assignment1-harness) | Public; README inspected |
| HW1 specification | [Handout](https://github.com/cs329z/assignment1-harness/blob/main/cs329z_assignment1_harness.pdf) | File page reachable; read fully before implementation |
| HW2 starter | [assignment2-evals](https://github.com/cs329z/assignment2-evals) | Public; README inspected |
| HW2 specification | [Handout](https://github.com/cs329z/assignment2-evals/blob/main/cs329z_assignment2_evaluation.pdf) | File page reachable; read fully before implementation |
| Paper presentation | [Handout](https://web.stanford.edu/class/cs329z/assignments/paper_video.pdf) | PDF reachable; review rubric before recording |
| Enrolled-student recordings | [Canvas](https://canvas.stanford.edu/courses/233286) | Restricted; redirects to login |
| Course discussion | [Ed Discussion](https://edstem.org/us/courses/106723/discussion) | App shell reachable; course content not inspected |

Public slides and assigned papers provide a legitimate self-study path where video is missing. For Canvas/Ed material, use authorized enrollment access if available; otherwise proceed with public resources and mentor-designed substitutes.

## Schedule mapping

All dates below are in **2026** and preserve course order; they are not personal deadlines.

| ID | Course week/date | Session | Module | Published resources |
|---|---|---|---|---|
| [L01](#l01) | 1 / Wed Sep 23 | Introduction: What Are Agentic Systems? | M1 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture01.pdf); [Video](https://youtu.be/DGI4vucR71w) |
| [L02](#l02) | 2 / Mon Sep 28 | LLMs for Builders | M2 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf); [Video](https://youtu.be/Vr1NzH8bT44) |
| [L03](#l03) | 2 / Wed Sep 30 | Retrieval-Augmented Generation (RAG) | M2 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf); [Video](https://youtu.be/psLc-46GqY0) |
| [L04](#l04) | 3 / Mon Oct 5 | Tool Use & Function Calling | M3 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf); [Video](https://youtu.be/s0S38lz6O7M) |
| [L05](#l05) | 3 / Wed Oct 7 | Frameworks & Orchestration | M3 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture05.pdf); [Video](https://youtu.be/q0Q-Hy8TTps); [Code](https://github.com/cs329z/lecture5-frameworks) |
| [L06](#l06) | 4 / Mon Oct 12 | Agent Design Patterns & Scaffolds | M4 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf) |
| [L07](#l07) | 4 / Wed Oct 14 | Agent Memory Architectures | M4 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture07.pdf) |
| [L08](#l08) | 5 / Mon Oct 19 | Multi-Agent Systems | M5 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture08.pdf) |
| [L09](#l09) | 5 / Wed Oct 21 | Optimization | M5 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture09.pdf) |
| [L10](#l10) | 6 / Mon Oct 26 | Guest Lecture: Terminal-Bench | M6 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture10.pdf) |
| [L11](#l11) | 6 / Wed Oct 28 | What Data Do Agents Need? | M6 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture11.pdf) |
| [L12](#l12) | 7 / Mon Nov 2 | Data Selection & Quality | M6 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture12.pdf) |
| [L13](#l13) | 7 / Wed Nov 4 | Evaluation Fundamentals & Benchmark Design | M7 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture13.pdf) |
| [L14](#l14) | 8 / Mon Nov 9 | Fireside Chat with Andrew Ng | M8 | No slides/video/code linked |
| [L15](#l15) | 8 / Wed Nov 11 | LLM-as-Judge & Evaluation Infrastructure | M8 | [Slides](https://web.stanford.edu/class/cs329z/slides/lecture15.pdf) |
| [L16](#l16) | 9 / Mon Nov 16 | Guest Lecture: SWE-bench | M8 | No slides/video/code linked |
| [L17](#l17) | 9 / Wed Nov 18 | Agent Safety & Guardrails | M9 | No slides/video/code linked |
| [L18](#l18) | 11 / Mon Nov 30 | Coding & Software Agents | M10 | No slides/video/code linked |
| [L19](#l19) | 11 / Wed Dec 2 | Personal Agents | M10 | No slides/video/code linked |

The schedule has no class on November 23 and 25 (Thanksgiving recess). The final demo event is December 9. These events do not add learning modules.

## Lecture resources and readings

<a id="l01"></a>
### L01 — Introduction: What Are Agentic Systems?

Official placement: week 1, Wed Sep 23, 2026. Roadmap: M1.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture01.pdf) — reachable.
- Video: [Video](https://youtu.be/DGI4vucR71w) — linked; endpoint reachable; playback untested.

**Official readings**

- [The Shift from Models to Compound AI Systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) — reachable.
- [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) — reachable.
- [AI Agents That Matter](https://arxiv.org/abs/2407.01502) — reachable.

<a id="l02"></a>
### L02 — LLMs for Builders

Official placement: week 2, Mon Sep 28, 2026. Roadmap: M2.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf) — reachable.
- Video: [Video](https://youtu.be/Vr1NzH8bT44) — linked; endpoint reachable; playback untested.

**Official readings**

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — reachable.
- [Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention](https://arxiv.org/abs/2006.16236) — reachable.
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — reachable.

<a id="l03"></a>
### L03 — Retrieval-Augmented Generation (RAG)

Official placement: week 2, Wed Sep 30, 2026. Roadmap: M2.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf) — reachable.
- Video: [Video](https://youtu.be/psLc-46GqY0) — linked; endpoint reachable; playback untested.

**Official readings**

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) — reachable.
- [Dense Passage Retrieval for Open-Domain Question Answering](https://arxiv.org/abs/2004.04906) — reachable.
- [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://arxiv.org/abs/2004.12832) — reachable.

<a id="l04"></a>
### L04 — Tool Use & Function Calling

Official placement: week 3, Mon Oct 5, 2026. Roadmap: M3.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf) — reachable.
- Video: [Video](https://youtu.be/s0S38lz6O7M) — linked; endpoint reachable; playback untested.

L04 refresh on November 23: the official schedule still links these resources. Direct checks returned HTTP 200 for both endpoints and a PDF signature for the slides. This refresh confirms links and access only; full slide review and video playback were not performed.

**Official readings**

- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — reachable.
- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) — reachable.
- [Model Context Protocol Specification, revision 2025-06-18. modelcontextprotocol.io (2025)](https://modelcontextprotocol.io/specification/2025-06-18) — reachable.

<a id="l05"></a>
### L05 — Frameworks & Orchestration

Official placement: week 3, Wed Oct 7, 2026. Roadmap: M3.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture05.pdf) — reachable.
- Video: [Video](https://youtu.be/q0Q-Hy8TTps) — linked; endpoint reachable; playback untested.
- Code: [Code](https://github.com/cs329z/lecture5-frameworks) — reachable.

November 25 notebook setup check: the official schedule still links this repository. Its `lecture5.ipynb`, README, setup script, and lockfile were inspected at commit `4e418289b3032cb960984250395525eb91ae25c2`. The demo requires Python 3.12 and OpenRouter, and includes DSPy, LangGraph, Temporal, and tinycal. Local setup/check results are in the [Week 03 setup guide](../lectures/week-03/lecture-05-setup.md). The slide PDF text fetch exceeded the web tool's size limit; no fresh slide review or video playback was performed.

November 26 framework comparison check: the web reader still rejected the 14,413,415-byte slide PDF, but a direct download succeeded. Text was extracted from its 132 pages. Selected relevant text and rendered PDF pages 16 (Framework Landscape), 80 (Agent Harness), and 98 (Temporal Execution Model) were inspected. This resolves access to the relevant slide material; it is not a full-deck review or video-playback check. The original is cached in the ignored lecture working directory. [Reviewed sections and provenance](../lectures/week-03/references.md#lecture-5-framework-landscape-and-agent-harnesses)

**Official readings**

- [DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines](https://arxiv.org/abs/2310.03714) — reachable.
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) — reachable.
- [HarnessTax: How Much Does the Harness Matter for Coding Agents?](https://arena.ai/blog/coding-agents-harness-tax) — reachable.

<a id="l06"></a>
### L06 — Agent Design Patterns & Scaffolds

Official placement: week 4, Mon Oct 12, 2026. Roadmap: M4.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf) — reachable.
- Video: [Video](https://youtu.be/JC_pLC5EX_w) — now linked in the official schedule, rechecked November 26; endpoint and recording title verified, playback untested.

November 26 workflow/agent question: direct download of the 10,861,442-byte official PDF succeeded despite the web reader's size limit. The deck has 86 pages; PDF page 12 (Workflows vs Agents) was extracted, rendered, and visually inspected. This is selected-page source review, not full-deck review or mentor video playback. The learner reports watching L06. [Reviewed definitions and references](../lectures/week-04/references.md#workflow-versus-agent)

November 26 reasoning/acting source check: PDF page 42 is titled CRITIC but its footer cites `2310.01798`, which identifies *Large Language Models Cannot Self-Correct Reasoning Yet*, also used on the preceding limitations slide. The primary CRITIC paper is [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738). Record this source-title mismatch without treating the two papers as interchangeable. [Selected-page checks and method references](../lectures/week-04/references.md#reasoning-acting-patterns-and-trajectory)

November 27 Pi case-study check: the slide-linked `pi.dev/docs/latest/cli` and `/compaction` URLs redirect to `docs.pi.dev/latest/`. Pages 77-83 were rendered and visually inspected. The current project documentation describes project trust before loading project resources, alongside tool execution with process permissions; qualify the slides' "no safeguards" shorthand rather than treating it as an exhaustive, permanent description. The website's GitHub tree links were blocked by the web reader, while the official raw README was accessible. No installation or Pi run was performed. [Pi references](../lectures/week-04/references.md#pi-case-study)

**Official readings**

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) — reachable.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) — reachable.
- [Context Engineering](https://www.langchain.com/blog/context-engineering-for-agents) — reachable.

**Official additional readings**

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) — reachable.
- [Executable Code Actions Elicit Better LLM Agents](https://arxiv.org/abs/2402.01030) — reachable.

<a id="l07"></a>
### L07 — Agent Memory Architectures

Official placement: week 4, Wed Oct 14, 2026. Roadmap: M4.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture07.pdf) — reachable.
- Video: [How AI Agent Memory Works: MemGPT & Memory Types](https://youtu.be/qh5tP6PBZ6U) — now linked in the official schedule, rechecked November 27. The endpoint and title identify CS329Z Lecture 7 with Michael Ryan; playback and full viewing were not performed by the mentor. Learner viewing is Not Started.

**Official readings**

- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) — reachable.
- [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) — reachable.
- [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442) — reachable.

<a id="l08"></a>
### L08 — Multi-Agent Systems

Official placement: week 5, Mon Oct 19, 2026. Roadmap: M5.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture08.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) — reachable.
- [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) — reachable.
- [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) — reachable.

<a id="l09"></a>
### L09 — Optimization

Official placement: week 5, Wed Oct 21, 2026. Roadmap: M5.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture09.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457) — reachable.
- [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs](https://arxiv.org/abs/2406.11695) — reachable.
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) — reachable.

<a id="l10"></a>
### L10 — Guest Lecture: Terminal-Bench

Official placement: week 6, Mon Oct 26, 2026. Roadmap: M6.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture10.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [Terminal-Bench project site (leaderboard, tasks, and harness)](https://www.tbench.ai/) — reachable.
- [Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces](https://arxiv.org/abs/2601.11868) — reachable.

<a id="l11"></a>
### L11 — What Data Do Agents Need?

Official placement: week 6, Wed Oct 28, 2026. Roadmap: M6.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture11.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [Data Flywheels for LLM Applications](https://www.sh-reya.com/blog/ai-engineering-flywheel/) — reachable.

**Official additional readings**

- [Large Language Models for Data Annotation and Synthesis: A Survey](https://aclanthology.org/2024.emnlp-main.54/) — reachable.

<a id="l12"></a>
### L12 — Data Selection & Quality

Official placement: week 7, Mon Nov 2, 2026. Roadmap: M6.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture12.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/abs/2504.21798) — reachable.
- [Who Validates the Validators? Aligning LLM-Assisted Evaluation with Human Preferences](https://arxiv.org/abs/2404.12272) — reachable.

**Official additional readings**

- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206) — reachable.

<a id="l13"></a>
### L13 — Evaluation Fundamentals & Benchmark Design

Official placement: week 7, Wed Nov 4, 2026. Roadmap: M7.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture13.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [Establishing Best Practices for Building Rigorous Agentic Benchmarks](https://arxiv.org/abs/2507.02825) — reachable.

**Official additional readings**

- [How to Build Good Language Modeling Benchmarks](https://ofir.io/How-to-Build-Good-Language-Modeling-Benchmarks/) — reachable.
- [tinyBenchmarks: Evaluating LLMs with Fewer Examples](https://arxiv.org/abs/2402.14992) — reachable.

<a id="l14"></a>
### L14 — Fireside Chat with Andrew Ng

Official placement: week 8, Mon Nov 9, 2026. Roadmap: M8.

- Slides: not linked in the checked schedule.
- Video: not linked in the checked schedule.

No readings assigned in the checked schedule. Self-study substitute: a short reflection connecting earlier system-design tradeoffs; do not invent content for an unavailable talk.

<a id="l15"></a>
### L15 — LLM-as-Judge & Evaluation Infrastructure

Official placement: week 8, Wed Nov 11, 2026. Roadmap: M8.

- Slides: [Slides](https://web.stanford.edu/class/cs329z/slides/lecture15.pdf) — reachable.
- Video: not linked in the checked schedule.

**Official readings**

- [Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — reachable.
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) — reachable.
- [AutoMetrics: Approximate Human Judgements with Automatically Generated Evaluators](https://arxiv.org/abs/2512.17267) — reachable.

**Official additional readings**

- [AutoLibra: Agent Metric Induction from Open-Ended Human Feedback](https://openreview.net/forum?id=4BjGVZ7Bxn) — unavailable to automated reading (browser challenge); [verified author preprint](https://arxiv.org/abs/2505.02820) is an alternative version, not asserted identical to the conference revision.

<a id="l16"></a>
### L16 — Guest Lecture: SWE-bench

Official placement: week 9, Mon Nov 16, 2026. Roadmap: M8.

- Slides: not linked in the checked schedule.
- Video: not linked in the checked schedule.

**Official readings**

- [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) — reachable.

<a id="l17"></a>
### L17 — Agent Safety & Guardrails

Official placement: week 9, Wed Nov 18, 2026. Roadmap: M9.

- Slides: not linked in the checked schedule.
- Video: not linked in the checked schedule.

**Official readings**

- [PrivacyLens: Evaluating Privacy Norm Awareness of LMs in Action](https://arxiv.org/abs/2409.00138) — reachable.
- [Searching for Privacy Risks in LLM Agents via Simulation](https://arxiv.org/abs/2508.10880) — reachable.
- [Agentic LLMs as Powerful Deanonymizers](https://arxiv.org/abs/2601.05918) — reachable.

**Official additional readings**

- [Contextualized Privacy Defense for LLM Agents](https://arxiv.org/abs/2603.02983) — reachable.
- [Understanding Prompt Injections: A Frontier Security Challenge](https://openai.com/index/prompt-injections/) — readable through web browsing; direct HTTP client received 403.
- [Anthropic's Responsible Scaling Policy](https://www.anthropic.com/news/anthropics-responsible-scaling-policy) — reachable.

<a id="l18"></a>
### L18 — Coding & Software Agents

Official placement: week 11, Mon Nov 30, 2026. Roadmap: M10.

- Slides: not linked in the checked schedule.
- Video: not linked in the checked schedule.

**Official readings**

- [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) — reachable.
- [OpenHands: An Open Platform for AI Software Developers](https://arxiv.org/abs/2407.16741) — reachable.

**Official additional readings**

- [Claude Code: Best Practices for Agentic Coding](https://www.anthropic.com/engineering/claude-code-best-practices) — redirects to current Claude Code documentation; historical 2025 article version not preserved by this link.
- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — reachable.

<a id="l19"></a>
### L19 — Personal Agents

Official placement: week 11, Wed Dec 2, 2026. Roadmap: M10.

- Slides: not linked in the checked schedule.
- Video: not linked in the checked schedule.

**Official readings**

- [Creating General User Models from Computer Use](https://arxiv.org/abs/2505.10831) — reachable.

**Official additional readings**

- [Learning Next Action Predictors from Human-Computer Interaction](https://arxiv.org/abs/2603.05923) — reachable.
- [OpenClaw: Open-source proactive AI agent](https://github.com/openclaw/openclaw) — reachable.

## Verification notes and source discrepancies

1. **HW2 repository alias:** the schedule links `assignment2-harness`, which redirects successfully to [assignment2-evals](https://github.com/cs329z/assignment2-evals). Use the destination; this is a working alias, not a missing assignment.
2. **HW2 peer reviews:** the schedule lists three tasks; logistics says two peers per activity. Keep this discrepancy unresolved until the current handout or course staff clarifies it. Self-study practice does not constitute an official submission.
3. **Future lectures:** November 16, November 18, November 30, and December 2 were future sessions on the verification date. Readings were already linked; slides and videos were not. Recheck before studying them. The November 9 fireside chat also has no public slides/video link.
4. **Recordings:** only L01–L05 have public video links in the checked schedule. Other recordings may be available through authorized Canvas access. We did not test playback for the five public links.
5. **Reading versions:** the MCP reading is specifically revision 2025-06-18. Do not silently substitute a newer specification when discussing that lecture. Live framework docs and redirected vendor articles can change.
6. **Publication metadata:** the index preserves course-linked resources. Publication year/venue labels may differ from preprint submission dates; inspect the version actually read before making bibliographic claims.

## Refresh procedure

Open the course, logistics, and project pages; compare schedule rows and assignment links. Check destination content, not just HTTP status. Update this index and the dated verification record together. Preserve restricted/unavailable labels until access is demonstrated. Do not infer missing slide URLs from neighboring filenames. Keep downloaded PDFs, videos, corpora, and login data out of the repository.
