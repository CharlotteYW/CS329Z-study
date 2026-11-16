# Week 1 Questions and Answers

Review notes from the study conversation. See the [weekly plan](../week-01-plan.md) and [references](references.md).

## What does LLM reasoning mean? Is it a property of the model?

Reasoning describes the model's ability to connect evidence and draw conclusions that require multiple steps. Training shapes that ability. The prompt and inference settings can affect how the model uses it on a given request. At the implementation level, an autoregressive model repeatedly predicts the next token from its context. Generated intermediate steps can become part of that context. Text that explains an answer can omit factors that influenced it. [Reasoning and faithfulness sources](references.md#reasoning-and-faithfulness)

## What is chain of thought, and is chain-of-thought prompting a prompting technique?

**Chain of thought (CoT)** is the sequence of intermediate reasoning steps a model generates. **CoT prompting** is a technique for eliciting those steps. You can ask the model to break a problem down before answering or give it a worked example to follow. Some models can generate intermediate steps automatically. Some also offer a dedicated thinking mode that changes how much inference computation they can spend on a request. [CoT and thinking sources](references.md#chain-of-thought)

## What is ReAct, and how does it relate to CoT?

**Preview of Lecture 6.** ReAct interleaves reasoning with actions and observations. In the authors' HotpotQA example, the model decides what information to look up, issues a Wikipedia search, and uses the search result to decide what to do next. CoT refers to the intermediate reasoning steps. ReAct places reasoning in a loop where an action can bring in new information. In a system that implements the pattern, the harness runs the tool and passes the observation back to the model. [ReAct paper and example](references.md#react)

## When is it worth letting the model decide the next action after a tool result?

Use model-directed branching when the meaning of the observation determines which next action is useful and a fixed rule would handle that choice poorly. In the ReAct paper's HotpotQA example, a Wikipedia result supplies information needed to formulate the next lookup. An explicit timeout with a known retry policy is a good fit for application code.

Permissions are a separate decision. Read-only tools limit the effects of a mistaken action. The harness can enforce a scoped tool set and a call budget, and require approval for a proposed write. To judge the value of adaptation, compare correctness and cost against a simpler baseline. [ReAct example](references.md#react) · [Evaluation example](references.md#optional-reading-and-comparison)

## What should I understand at a high level after Lecture 1?

- **Control flow.** In a fixed workflow, application code determines the steps and branches. An agent can let the model choose an action in response to observations. A system can combine both approaches.
- **System boundaries.** Trace one cycle from goal and state to action, observation, and the next decision. Identify which decisions the model makes and which permissions, budgets, and stop conditions the harness enforces.
- **Evaluation.** Start with a simple baseline. Compare task correctness and API cost to judge whether a more involved design adds value. Give one concrete example of how it might fail.

Recognizing the history and names of patterns is sufficient at this stage. Later lectures revisit their details. [Lecture 1 materials](../../resources/course-materials.md#l01) · [Optional reading and comparison](references.md#optional-reading-and-comparison)

## What does AI Agents That Matter show about Retry and Reflexion?

The paper argues that agent evaluations should account for cost alongside accuracy, use appropriate held-out tasks, and report enough details for others to reproduce the comparison. On the 164 HumanEval problems used in the study, the authors report 92.0% accuracy and $2.51 in total API cost for GPT-4 Retry, compared with 87.8% and $3.90 for GPT-4 Reflexion. These are per-run averages over five runs at the study's prices.

**Reference answer.** For similar coding tasks with fast tests, I would start with a retry baseline that has a fixed attempt limit. In this experiment, it solved more tasks at lower API cost. For a different task, I would reevaluate both methods on the same tasks and under a comparable budget before choosing an architecture. [Figure 1 and Table A1](references.md#optional-reading-and-comparison)

## What types of memory does an agent use, and how are they classified?

**Preview of Lecture 7.** CoALA distinguishes active working memory from three forms of long-term memory. The table adapts the paper's retail assistant example to a returns conversation.

| Type | What it helps the agent answer | Example |
|---|---|---|
| Working | What is happening in the current task? | The current order ID, conversation, and latest order lookup result |
| Episodic | What happened on a specific past occasion? | The steps and outcome of this customer's previous return |
| Semantic | What facts can I use across tasks? | Product attributes, the return window, or a customer's language preference |
| Procedural | How do I carry out this task? | A return workflow that verifies the order, checks eligibility, and requests approval for an exception |

Classify information by how the agent uses it. A past return is an episode. Once the agent retrieves it for the current case, the relevant details are also part of working memory. Storage is a separate design choice. LangGraph can persist thread state in a database checkpoint, so working memory can survive a process restart while staying scoped to that thread. [Agent memory sources](references.md#agent-memory)

## What do insincere flattery and sycophancy mean?

**Insincere flattery** is praise the speaker does not genuinely mean. **Sycophancy** in everyday English is excessive flattery or deference to win favor. In LLM research, it describes a response that follows the user's stated view or preference at the expense of accuracy or independent judgment. Praise is one form. Agreeing with an unsupported claim can also qualify. In Sharma et al.'s feedback experiment, the same argument received more positive feedback when the user said they liked it. [Definitions and study](references.md#sycophancy)

## What is multi-agent collusion?

Multi-agent collusion occurs when agents coordinate in a way that benefits the participating agents or their principals while undermining an intended constraint, such as fair competition or independent oversight. Coordination can be explicit through messages or tacit through repeated responses to observable behavior. In a simulated market studied by Fish et al., separate LLM pricing agents reached prices above the competitive benchmark while observing each other's prices without direct messaging. Ordinary teamwork follows the intended system design, such as an agent gathering evidence for a reviewer to check independently. Matching outputs alone are weak evidence of collusion because agents can face the same inputs and incentives. [Pricing study](references.md#multi-agent-collusion)

## Will we build an agent, and where will the model run?

HW1 builds a terminal assistant that retrieves from an email and document archive, uses tools, and adds memory and human approval. The harness runs locally. Default tests replay scripted model replies and require no network model call. Live tests use the course's hosted model configuration through OpenRouter. HW2 builds an evaluation for a supplied agent. A self-study project can use a local model or a hosted API. [Course and assignment sources](references.md#course-and-tooling)

## What is OpenRouter? Do I need an account now?

OpenRouter is a hosted gateway that provides one API for models from multiple providers. Registration and API key creation are free. Models marked `:free` have usage limits, and paid models charge by usage. The initial lectures and HW1's default tests can be done without an account. For the official HW1 live tests, set up an OpenRouter API key and budget for model calls. [OpenRouter and HW1 sources](references.md#course-and-tooling)
