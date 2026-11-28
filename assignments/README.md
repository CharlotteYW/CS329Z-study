# Official Assignment Milestones

Both assignments are major learning milestones. Official starters and local environments were prepared on **2026-11-28**. The READMEs, setup-related handout text, and selected setup pages were inspected; complete PDF specifications have **not** been reviewed end to end. Read the current handout before architecture approval or implementation. No learner solution or written homework answer has been supplied.

## Open and start

| Homework | Open in VS Code | Resume instructions |
|---|---|---|
| HW1 | [HW1.code-workspace](HW1.code-workspace) | [HW1 START-HERE](hw1-agent-harness/START-HERE.md) |
| HW2 | [HW2.code-workspace](HW2.code-workspace) | [HW2 START-HERE](hw2-agent-evaluation/START-HERE.md) |

From the study repository root:

```bash
code assignments/HW1.code-workspace
# Or, when starting HW2:
code assignments/HW2.code-workspace
```

Check either or both local environments without making model calls:

```bash
python3 assignments/check_setup.py
python3 assignments/check_setup.py hw1
python3 assignments/check_setup.py hw2
```

Both use the already installed Python 3.12.13 and separate `.venv` directories synchronized from the official lock files. The previously configured OpenRouter key is reused only in ignored local `.env` files. Actual model access, credits, and paid evaluations were not tested. HW1's checksum-verified 26,278-email archive is unpacked locally. HW2's Harbor CLI and Docker connection work; task images and evaluation runs remain for the learner's exercises.

See [setup verification](SETUP.md) for exact commands/outcomes and [upstream provenance](upstream.json) for source revisions. Official files and licenses are preserved. The starter directories are regular files in this main repository, not nested repositories or submodules; their original Git metadata is archived under this repository's local `.git` directory.

The learner explicitly authorized publishing the **official starter and setup snapshot** here. The official HW2 handout asks for a private submission repository. Future learner implementations, answers, and run artifacts are not automatically committed or pushed. Credentials, environments, caches, and the downloaded mail archive remain local. This preparation is administration, not assignment completion.

## HW1 — Build an Agentic Harness

Sources: [official starter](https://github.com/cs329z/assignment1-harness), [handout](https://github.com/cs329z/assignment1-harness/blob/main/cs329z_assignment1_harness.pdf), and [course logistics](https://cs329z.stanford.edu/logistics).

The assignment develops an assistant over an email corpus, progressing through retrieval and pipelines to tools, a terminal, memory, and human involvement. **Agent frameworks are prohibited.** Its README documents Python 3.11+, `uv`, deterministic tests using a scripted model, and separate paid live tests. Follow the official environment when beginning; do not assume an Ollama substitution preserves the grading contract.

Self-paced sequence:

1. **After M3:** Read the handout, inspect starter interfaces/tests, record the upstream revision, and map each requirement to evidence. The learner explains the architecture before implementation.
2. **M3–M4:** Implement incrementally with the learner participating. Discuss output contracts, retrieval quality, and tool failure paths. Run relevant deterministic tests after meaningful changes.
3. **M4–M6:** Add the remaining required harness capabilities and review isolation, persistence, stopping, and human control. Estimate live-test cost before running a small experiment; record any reduced evaluation slice.
4. **Review:** Reproduce required results, inspect failures and limitations, and conduct a short oral defense. Passing scripted tests alone does not establish live model reliability.

**Completion evidence:** handout checklist, explained code, actual deterministic/live results as required by the handout, failure analysis, reproducible setup, and an oral defense. A small live slice is not a full benchmark run.

## HW2 — Evaluate an Agent

Sources: [official starter](https://github.com/cs329z/assignment2-evals) and [handout](https://github.com/cs329z/assignment2-evals/blob/main/cs329z_assignment2_evaluation.pdf).

The starter uses Harbor, Docker, a pinned agent, example tasks, and a submission checker. Its README flags `linux/amd64` configuration for the SWE-bench task on Apple Silicon. Preserve the pinned agent; inspect architecture/emulation needs before downloading images. The public README instructs students to keep the repository private.

Self-paced sequence:

1. **M6:** Read the handout and inspect the supplied agent/environment without changing its evaluation target. Estimate compute, image storage, and model costs before setup.
2. **M7:** Define task requests, environments, stopping rules, and scorers. Identify baselines, data provenance, split discipline, and deterministic checks. Verify all exact task-count and submission requirements against the handout.
3. **M8:** Develop the required model-judge evaluation, calibrate against human judgments, and preserve versions and run metadata. Run experiments, inspect errors, and assess uncertainty.
4. **Review:** Use the supplied checker and actual task runs. Distinguish structural submission completeness from measurement validity. Defend conclusions orally.

**Completion evidence:** justified evaluation design, correct graders, reproducible task artifacts, actual experiments, calibrated judgment where required, error categories, limitations, and an oral defense. No scores or results are inferred from the scaffold.

## Shared Oral Defense

Ask the learner to explain the architecture, alternatives considered, important failure modes, testing strategy, likely scale bottlenecks, and production changes. For HW2, additionally challenge construct validity, leakage, grader errors, and whether the evidence supports each improvement claim. Ask for a new example to check transfer rather than rehearsed explanations.

## Integrity, Timing, and Peer Review

AI-supported explanation, debugging, and understood code are allowed by the course policy; copying others' solutions or bypassing understanding is not. Closed-book quizzes remain individual. Keep homework solutions private; portfolio publication should focus on an original project. Do not commit or push without learner approval.

The original course calendar is reference context only. The learner has no imposed Stanford due dates in this plan. The schedule says HW2 peer review covers three tasks while logistics says two peers per activity; consult the current handout/staff if an official submission is intended. Legitimate self-study peer-review exercises may use permitted public examples or a volunteer's work and must not be represented as completed Stanford peer reviews.
