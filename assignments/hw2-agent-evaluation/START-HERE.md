# HW2: Resume Here

Local setup was prepared on November 28, 2026. The official task example, pinned agent, and write-up placeholders are unchanged.

1. Start Docker Desktop if it is not running.
2. Open `../HW2.code-workspace` in VS Code, or run `code ../HW2.code-workspace` from this directory.
3. Run `python3 ../check_setup.py hw2`, then `uv run --locked harbor --version`.
4. Read Section 2 of [the handout](cs329z_assignment2_evaluation.pdf). Begin the Docker/Harbor exercises yourself and record your own observations in the supplied response files.

```bash
uv run --locked harbor --help
uv run --locked python check_submission.py
```

The submission checker reports unfinished answers, tasks, figures, and run artifacts. These are expected for an untouched starter and are separate from environment setup.

Python 3.12 is selected in `.python-version`; `.venv` follows the official `uv.lock`, including Harbor 0.18.0. The local `.env` reuses the previously configured OpenRouter key. It is ignored, and its value is never shown by the setup checker. Actual provider/model access remains untested.

No task images, oracle runs, agent attempts, new evaluation tasks, or written answers were produced during setup. Docker images download/build when you begin the relevant exercises; model attempts can incur charges. For the SWE-bench exercise specifically, the handout requires `DOCKER_DEFAULT_PLATFORM=linux/amd64` on Apple Silicon. Apply that setting to that exercise, rather than globally forcing every task to use emulation.

Keep `pinned_agent.py` and the course versions intact. The checked handout's clone command names `assignment2-harness`; this workspace uses the public `cs329z/assignment2-evals` starter identified in the course resource index. Upstream revision and setup provenance are in `../upstream.json`.

Publication scope: the learner authorized publishing the official starter and setup in the study repository. The official handout requests a private repository for completed submissions. Future learner solutions and results are not automatically committed or pushed.
