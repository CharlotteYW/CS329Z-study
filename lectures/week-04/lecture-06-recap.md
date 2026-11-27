# Lecture 6: Instructor Section Recaps

Official lecture material, summarized in English from the [L06 slides](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf). These are faithful paraphrases of the instructor's recap slides, not a transcript or the mentor's independent reference summary. PDF page numbers refer to the 86-page deck reviewed on November 27.

## Workflow recap: PDF page 30

- Workflows generally make reproduction and debugging more straightforward than adaptive agents.
- The five reusable patterns are prompt chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer.
- Practical workflows combine these components into larger systems.

[Source slide](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=30) · [Detailed pattern notes](questions-and-answers.md#what-are-the-five-workflow-design-patterns-in-lecture-6)

## Reasoning and acting recap: PDF page 54

- **ReAct:** reasoning can help select actions before execution.
- **Reflexion:** the lecturer connects the self-reflection idea with reasoning behavior in contemporary models.
- **CodeAct:** executable code is a useful representation for actions.
- **ReWOO / LLMCompiler:** the lecturer relates compiled tool workflows to parallel calls in contemporary systems while retaining the importance of planning.
- Predefined workflows can also coordinate subagents.

[Source slide](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=54) · [Method comparison](questions-and-answers.md#how-do-the-lectures-reasoning-and-acting-methods-compare)

**Mentor clarification:** the slide's comments about contemporary practice are the lecturer's synthesis, not universal benchmark findings. Reasoning-model reflection does not automatically implement the original Reflexion memory/trial algorithm. Original ReWOO and LLMCompiler also have distinct planning, scheduling, and replanning designs, explained in the method notes.

## Context-management recap: PDF pages 73-75

- Event logs, memory offloading, compaction, observation masking, and context isolation provide reusable context-management patterns.
- Real systems combine these policies.
- Preserve two priorities: keep inputs relevant and maintain task continuity.
- The closing taxonomy groups operations into **write, select, compress, and isolate**. The highlighted later topics are persistent memory and multi-agent context partitioning.

[Taxonomy](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=73) · [Recap](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=75) · [Context notes](questions-and-answers.md#what-should-i-understand-before-watching-the-context-management-section)

**Mentor clarification:** storing complete event history and choosing the current model input are separate operations. Summaries, masking, isolated workers, and progressively loaded Skills can be used together; their usefulness depends on preserving needed goals, constraints, and evidence.

## Pi recap: PDF page 83

- Pi keeps its harness core small and supports community extensions.
- The default tool set highlighted in the lecture is read, bash, edit, and write.
- Its action/observation cycle follows a ReAct-style design.
- Event history, progressive disclosure, and compaction manage context.
- The lecturer emphasizes that the core does not supply the execution safeguards of a more restrictive environment.

[Source slide](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=83) · [Pi notes and current documentation](questions-and-answers.md#what-is-pi-and-how-does-the-lectures-case-study-connect-the-design-patterns)

**Mentor clarification:** the safety shorthand refers to the lecture's core configuration. Tools use the process's operating-system permissions, while current documentation also describes project-resource trust. Extensions and deployment boundaries can change behavior; avoid treating the recap as a permanent claim about every release.

## Whole-lecture summary: PDF page 85

The final slide connects five topics: workflow/agent control, workflow composition, agent reasoning/actions, agent context management, and the Pi implementation case study.

[Source slide](https://web.stanford.edu/class/cs329z/slides/lecture06.pdf#page=85) · [Learner reflection and AI reference summary](questions-and-answers.md#lecture-6-reflection-and-reference-summary)

Use these instructor recaps for a quick review, then consult the linked Q&A for mechanisms and examples. The next lecture, L07, develops agent memory architectures; its viewing is not yet reported. Source review covers the recap pages and relevant earlier section pages, not full mentor video playback. No implementation or benchmark is claimed.
