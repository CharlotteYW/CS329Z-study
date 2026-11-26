# Week 3 References

## Current study action

L04's discussion and learner reflection are recorded. On November 24, the learner identified why tools are needed, how to call them, and how to evaluate calls; the AI reference summary followed that reflection. Detailed applied evidence remains for later course work. Keep the 3–4 hour weekly budget, with no extra reading or coding exercise assigned for this wrap-up. [Reflection and reference summary](questions-and-answers.md#lecture-4-reflection-and-reference-summary)

On November 25, follow-up discussion compares the actual integration work of direct function calling, MCP, and an existing tool gateway. This is an explanation and reference update, not an installation task. [MCP scenario comparison](questions-and-answers.md#when-does-mcp-actually-save-work)

Next: **L05 — Frameworks & Orchestration**, **Not Started**. [Official video](https://youtu.be/q0Q-Hy8TTps) · [Verified course entry](../../resources/course-materials.md#l05). Viewing question: which control-flow, state, and error-handling responsibilities does a framework take over, and which remain with the application?

- [Official lecture video](https://youtu.be/s0S38lz6O7M)
- [Official slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf)
- [Course resource index](../../resources/course-materials.md#l04)

**Viewing prompt used for L04:** when the model proposes a tool call, which validation, execution, and error-reporting responsibilities belong to the runtime?

The L04 reflection is now recorded. No new L05 viewing, reading, code execution, or source recheck is claimed by this entry; the linked resource verification is documented in the course index.

## Official readings for reference

The official schedule lists these readings for L04. They are indexed here for later questions, not a checklist for this study session.

- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) — learning when and how to invoke tools.
- [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334) — connecting model outputs with API usage.
- [Model Context Protocol specification, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18) — the revision linked by the course; use it when discussing the lecture rather than silently substituting a newer revision.

## Access record

On November 23, the [official Fall 2026 schedule](https://cs329z.stanford.edu/) was inspected and confirmed L04's title, resource links, and reading list. Direct requests returned HTTP 200 for the video page and slides, and the slide response had a PDF signature. Video playback and full slide or reading review were not performed. This entry prepares the next session and does not establish lecture completion.

## Toolformer candidate generation and filtering

These sources were inspected on November 24 for the current question. They are references for review, with no additional reading assignment.

- Lecture 4 PDF pages 24–28 describe constructing augmented data, sampling call positions and arguments, executing calls, and filtering by weighted cross-entropy improvement. The filter slide is PDF page 27, labeled 28 on the slide. [Toolformer method slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=24)
- Section 2 and Figures 2–3 of the original paper specify the annotation prompt, call-start probabilities, sampling threshold, three scoring conditions, minimum-baseline comparison, and filtering threshold. The filtering footnote explains prepending candidate API information during scoring; the fine-tuning paragraph explains interleaving retained calls into the original text. The inference paragraph specifies execution and resumption at deployment. These sections were inspected, without claiming a full-paper review. [Toolformer original method](https://arxiv.org/html/2302.04761)

## Toolformer and current tool-use practice

These primary sources were checked on November 24 to distinguish current application interfaces from model training. They are references for the learner's question, not new reading assignments. The comparison is based on public evidence and does not establish the prevalence of undisclosed training recipes.

- OpenAI documents runtime tool definitions, structured calls, application-side execution, returned observations, and schema constraints. [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- Claude documents tool descriptions and input schemas, model-emitted `tool_use` blocks, application-returned `tool_result` blocks, and the distinction between client and server tools. [Tool-use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Olmo 3 Section 5.2.1 describes function-calling SFT data from real MCP environments and simulated interactions, along with a unified tool format. This is an open training example previously introduced during L02. [Olmo 3 technical report](https://arxiv.org/html/2512.13961)
- Qwen3-Coder-Next Sections 4.1 and 4.2.4 describe execution-verified agent trajectories for supervised fine-tuning and multi-turn RL with task rewards and format penalties. This is a 2026 public example; the relevant sections were inspected, without a full-report review. [Qwen3-Coder-Next technical report](https://arxiv.org/html/2603.00729)
- MCP's course-linked revision defines discovery and invocation of tools; it is an interface protocol, not a model training method. [MCP tools, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

## ToolLLM and ToolBench

These lecture-mentioned sources were checked on November 24 for the learner's comparison question. They are review references, not an additional reading assignment.

- Lecture 4 PDF pages 37–38 introduce ToolLLM and its neural API retriever. PDF page 45 contrasts tool-learning methods, and pages 61–62 return to ToolBench evaluation. [ToolLLM slides](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=37) · [Method comparison](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=45)
- The original paper distinguishes the ToolLLM framework, ToolBench data/evaluation resource, and ToolLLaMA model. Sections 2 and 3.1 describe API collection, generated instructions, executed trajectories, depth-first-search-based annotation, and API-document retrieval. The curated collection contains 3,451 tools and 16,464 APIs; these are different counting units. Relevant sections were inspected, without a full-paper review. [ToolLLM original paper](https://arxiv.org/html/2307.16789)
- The authors' repository identifies the ICLR 2024 work and provides dataset, model, retriever, and evaluation resources. This is a historical implementation reference, not a recommendation to reproduce its environment or a claim that its APIs remain available. [Official ToolBench repository](https://github.com/OpenBMB/ToolBench)

## Gorilla API generation and retrieval

Checked on November 24 for the learner's question. These are review references, not additional reading assignments.

- Lecture 4 PDF pages 39–45 connect API hallucination, Gorilla's data, retrieval-aware training, AST matching, and the comparison with Toolformer and ToolLLM. PDF page 42 emphasizes relevant and irrelevant retrieval context; this is not a guarantee of robustness. [Gorilla lecture segment](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=39)
- The original arXiv v1 Sections 3.1–3.3 and 4.1 describe APIBench, GPT-4 instruction generation, LLaMA-7B fine-tuning, document-conditioned training/inference, AST subtree matching, and sensitivity to retrieval quality. The inspected training experiment uses oracle API documents, so the slide's correct/incorrect-context statement is not treated as a verified v1 sampling recipe. Relevant sections were inspected, without a full-paper review. [Gorilla original paper](https://arxiv.org/html/2305.15334)
- The authors' project site distinguishes the original Gorilla research from later OpenFunctions models and the BFCL evaluation effort. No later model was benchmarked or installed. [Gorilla project](https://gorilla.cs.berkeley.edu/)
- For the follow-up walkthrough, Sections 3.1–3.2 were rechecked for API record fields, ten generated instruction/API pairs per API, standard instruction fine-tuning, the documentation-conditioned input, and BM25/GPT-Index inference. GPT-4's data-generation role is separate from deployment. The authors' README links the original inference, evaluation, and APIBench resources; the README was inspected without running code or inspecting individual dataset rows. [Original method](https://arxiv.org/html/2305.15334#S3) · [Authors' implementation overview](https://github.com/ShishirPatil/gorilla#about)

## Lecture 4 concept map

Checked on November 24 to answer the learner's synthesis question. These sources support review, not additional reading work. Interface and evaluation material was first introduced as a preview and was subsequently discussed in the later Q&A.

- The lecture's stated objectives are why tools are needed, how models learn to call them, how tools are exposed, and how tool use is evaluated. PDF page 45 compares training approaches, pages 47–56 introduce interfaces and runtime responsibilities, and pages 58–68 discuss evaluations and failure modes. The concept map is the mentor's synthesis of these stated objectives. [Learning objectives](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=3) · [Approach comparison](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=45) · [Interface preview](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=47) · [Evaluation preview](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=58)
- The original papers clarify the naming levels: Toolformer describes a training approach and resulting models; ToolLLM describes an overall framework and names its trained model ToolLLaMA; Gorilla describes API-call training and a trained model. Relevant descriptions were rechecked, without a full-paper review. [Toolformer](https://arxiv.org/html/2302.04761) · [ToolLLM](https://arxiv.org/html/2307.16789) · [Gorilla](https://arxiv.org/html/2305.15334)
- The current OpenAI and Claude interface documentation linked under [current tool-use practice](#toolformer-and-current-tool-use-practice) was rechecked: general models can emit tool requests directly, while client or provider infrastructure executes them. A separate specialist model is not required by these interfaces. This says nothing about undisclosed training recipes or correctness on arbitrary tasks.

## Learning-to-use-tools comparison

Added on November 24 at the learner's request. These are references for the saved comparison, with no new reading task.

- The learner supplied a screenshot of "Learning to Use Tools: Summary". Its six comparison rows were transcribed into the Week 03 Q&A, with explanatory notes separated from the table. The screenshot's subtitles and player interface were not included. [Official comparison slide, PDF page 45](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=45)
- ToolkenGPT's abstract, introduction, and Figure 1 explain the frozen base LM, learned tool-token embeddings, tool selection, and in-context argument completion. These descriptions clarify the slide's abbreviated "one new token" and "in-context" entries. Relevant parts were inspected, without a full-paper review. [ToolkenGPT original paper](https://arxiv.org/html/2305.11554)
- For the other methods' mechanisms, use the existing [Toolformer filtering](#toolformer-candidate-generation-and-filtering), [ToolLLM](#toolllm-and-toolbench), and [Gorilla](#gorilla-api-generation-and-retrieval) references above. The table's scale row is historical context, not a comparative performance result.

## New tools, retraining, and standard interfaces

Checked on November 24 for the learner's transition question; references for review, not extra reading tasks.

- The previously inspected "Why Standard Interfaces?" slide contrasts adapting models to tools with runtime tool descriptions. The learner subsequently quoted its exact every-new-API training statement, which lists Toolformer, ToolkenGPT, and Gorilla, excluding ToolLLM. The transition interpretation is accurate; the primary papers below qualify a universal reading of the wording. Follow-up PDF refetches timed out; the quotation is learner-supplied, and no fresh slide inspection or playback is claimed. [Interface transition, PDF page 47](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=47)
- ToolLLM discusses generalization to unseen APIs and Section 3.3 evaluates out-of-distribution APIBench tasks. These results qualify the idea that every newly supplied API requires another model training run. They do not prove universal generalization. [ToolLLM paper](https://arxiv.org/html/2307.16789)
- Gorilla Section 4.2 tests changed API documentation at inference. Documentation changes and arbitrary new-tool generalization should not be conflated. [Gorilla paper](https://arxiv.org/html/2305.15334)
- ToolkenGPT describes training embeddings for new tool tokens while freezing the base LM; this is distinct from full-model retraining. [ToolkenGPT paper](https://arxiv.org/html/2305.11554)
- Current Claude documentation describes runtime definitions, model-generated requests, and external execution. The course-pinned MCP tools specification defines schemas, discovery, and invocation. Both were rechecked; neither interface eliminates the need for model capability or task evaluation. [Tool-use interface](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) · [MCP tools, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)

## MCP schema validation and function calling

Checked on November 24 for the learner's schema-guarantee question. These are targeted references for review, not extra study assignments.

- The course-pinned tools specification defines `tools/list`, `tools/call`, `inputSchema`, optional `outputSchema`, tool results, and error reporting. Its security considerations require servers to validate all tool inputs. This requirement does not prove that any particular SDK or deployment implements validation correctly. [MCP tools, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- The base specification defines JSON-RPC messages and lifecycle/capability concerns. Message-envelope validation and tool-specific argument validation are separate checks. [MCP base protocol, revision 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18/basic)
- Claude documents `strict: true` as grammar-constrained sampling against a supported JSON Schema subset. This is a model-provider generation feature, not an automatic consequence of exposing an MCP tool. The relevant descriptions were inspected without invoking a model. [Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)
- OpenAI documents JSON Schema function parameters and strict tool definitions. The provider-facing format differs from MCP's wire format; schema mapping must respect provider constraints. [Function calling](https://developers.openai.com/api/docs/guides/function-calling)
- For the follow-up integration example, the MCP tools specification, OpenAI's function definitions, and Claude's `input_schema` field were rechecked. The notes compare the same input contract in different wrappers and explain service reuse with a constructed order/inventory integration. Automatic schema discovery is distinct from provider-schema compatibility or a guarantee of backward-compatible API changes. [OpenAI function definitions](https://developers.openai.com/api/docs/guides/function-calling.md) · [Claude tool definitions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)
- The pinned architecture places model coordination in hosts and tool capabilities in servers. Current provider documentation describes OpenAI remote MCP tools and Claude's MCP connector, which can manage discovery and invocation on the provider side. These are implementation examples, not a change to the course's protocol revision or a claim that provider request formats are identical. Relevant descriptions were inspected; no connection was configured. [MCP architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture) · [OpenAI MCP integration](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) · [Claude MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)

## Tool-calling benchmarks

Checked on November 24 for the requested L04 benchmark summary. These are review references, not new reading assignments or current leaderboard recommendations.

- The official lecture identifies BFCL, ToolBench, and tau-bench as its evaluation topics. PDF pages 58–64 cover their comparison and pass-at-k versus pass-hat-k; subsequent slides discuss evolution and failure modes. The PDF opened this turn, but targeted follow-up page fetches timed out. The original sources below support the mechanism details; no leaderboard chart or video playback was verified. [Lecture evaluation section](https://web.stanford.edu/class/cs329z/slides/lecture04.pdf#page=58)
- The original BFCL authors' overview describes function selection, parallel calls, relevance detection, AST evaluation, and execution evaluation. The V3 article documents multi-turn/multi-step tasks and per-turn state/response checks. These versions provide the scope distinctions used in the notes; they are not claims about the newest leaderboard. [BFCL overview](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html) · [BFCL V3](https://gorilla.cs.berkeley.edu/blogs/13_bfcl_v3_multi_turn.html)
- ToolLLM Section 3.1 and Appendix A.5 explain ChatGPT-based ToolEval, pass rate under a budget, win rate, and how solvable/unsolvable tasks affect judgments. Relevant parts were inspected without a full-paper review. [ToolBench and ToolEval](https://arxiv.org/html/2307.16789)
- Original tau-bench Section 3 defines the simulated user, policies, task outcome, database and response reward checks, and pass^k versus pass@k. The paper notes that its reward can miss some policy violations. Relevant parts were inspected without a full-paper review; the notes do not substitute later tau-bench variants for the original setup. [Tau-bench original paper](https://arxiv.org/html/2406.12045)

## When MCP reduces integration work

Checked on November 25 for the learner's request for a concrete benefit comparison. These sources are references for review, not an instruction to install integrations.

- The pinned MCP architecture separates host coordination, client sessions, and server capabilities; servers can be local processes or remote services. The tools specification supplies discovery and invocation. These support the mechanism explanation, not a quantified claim that MCP is always simpler. [Architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture) · [Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- OpenAI's function-calling guide describes application-provided definitions and tool execution. Its MCP integration guide describes a provider-managed connection to remote servers. Both approaches still require implemented tool capabilities. Relevant descriptions were rechecked without running an API request. [Function calling](https://developers.openai.com/api/docs/guides/function-calling.md) · [MCP integration](https://developers.openai.com/api/docs/guides/tools-connectors-mcp.md)
- GitHub's official server README documents its hosted endpoint, a VS Code connection example, other MCP hosts including Claude applications, and varying authentication/configuration support. This is the concrete interoperability example used in the notes, rather than an invented claim of universal plug-and-play support. [GitHub MCP server](https://github.com/github/github-mcp-server)
- VS Code documents adding and using MCP servers through its host integration. Configuration destinations and supported authentication depend on the host/version; no local setup was performed or verified. [VS Code MCP documentation](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- The MCP architecture/tools specifications and function-calling guide were rechecked for the November 25 interview reference answer. The answer's selection criteria are mentor engineering judgments grounded in those interface responsibilities; no claim of universal superiority or quantified productivity gain is made.
