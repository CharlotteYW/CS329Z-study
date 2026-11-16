# Week 1 References

Use these sources to revisit the [week's questions and answers](questions-and-answers.md).

## Optional reading and comparison

- **Read when time permits.** The introduction and Figure 1 cover the main comparison. Appendix A, Table A1 gives the exact HumanEval accuracy and API cost for each method. [AI Agents That Matter](https://arxiv.org/html/2407.01502)
- **Optional comparison.** Compare the GPT-4 Retry baseline with Reflexion using accuracy and total API cost. For a worked answer, see the [paper summary and reference answer](questions-and-answers.md#what-does-ai-agents-that-matter-show-about-retry-and-reflexion).

## Chain of thought

- Wei et al. show how worked examples with intermediate reasoning steps can improve performance on multi-step tasks. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
- Kojima et al. test a short step-by-step instruction with no worked example. [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- Anthropic documents model-specific thinking modes, effort settings, and what the API may return to the caller. [Claude Thinking documentation](https://platform.claude.com/docs/en/build-with-claude/thinking)

## Reasoning and faithfulness

- Guo et al. describe post-training methods for improving reasoning performance. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- Turpin et al. find that generated CoT explanations can omit factors that influenced an answer. [Unfaithful Explanations in Chain-of-Thought Prompting](https://arxiv.org/abs/2305.04388)

## ReAct

- Yao et al. interleave reasoning and actions across interactive tasks and question answering. The authors' project page links to the code and shows a HotpotQA example. This is preview material for Lecture 6. [ReAct paper](https://arxiv.org/abs/2210.03629) · [Project page and code](https://react-lm.github.io/)

## Agent memory

- Lecture 7 introduces the four memory types and compares agent memory architectures. [L07 course materials and slides](../../resources/course-materials.md#l07)
- Sumers et al. describe working, episodic, semantic, and procedural memory in Section 4.1. The paper uses a retail assistant as a design example in Section 6. [Cognitive Architectures for Language Agents](https://arxiv.org/html/2309.02427)
- LangChain's memory guide shows how LangGraph handles thread-scoped state with checkpoints and uses stores for recall across threads. [Memory overview](https://docs.langchain.com/oss/python/concepts/memory)

## Sycophancy

- Merriam-Webster gives the everyday meaning of sycophancy as excessive, deferential flattery. [Sycophancy definition](https://www.merriam-webster.com/dictionary/sycophancy)
- Sharma et al. measure how a user's stated position can shift model feedback and answers. Figure 1 compares feedback on the same argument with and without a stated preference. [Towards Understanding Sycophancy in Language Models](https://arxiv.org/html/2310.13548)

## Multi-agent collusion

- Fish, Gonczarowski, and Shorrer report prices above a competitive benchmark in a simulated market with separate LLM pricing agents. Sections 2 and 3 describe what the agents could observe and what the experiment found. [Algorithmic Collusion by Large Language Models](https://arxiv.org/html/2404.00806)

## Course and tooling

- Stanford describes the course and its two applied assignments. [Course schedule](https://cs329z.stanford.edu/) · [Coursework](https://cs329z.stanford.edu/logistics#coursework)
- HW1 documents scripted and live tests. HW2 provides the evaluation starter. [HW1 starter](https://github.com/cs329z/assignment1-harness#tests) · [HW2 starter](https://github.com/cs329z/assignment2-evals)
- OpenRouter documents API key setup, free model limits, and paid usage. Check current terms when setting up live tests. [Developer documentation](https://openrouter.ai/developers) · [Free models](https://openrouter.ai/collections/free-models) · [Pricing](https://openrouter.ai/pricing)
