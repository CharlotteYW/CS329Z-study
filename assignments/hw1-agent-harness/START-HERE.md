# HW1: Resume Here

Local setup was prepared on November 28, 2026. This is an unimplemented official starter.

1. Open `../HW1.code-workspace` in VS Code, or run `code ../HW1.code-workspace` from this directory.
2. Run `python3 ../check_setup.py hw1`. This checks the environment, local key presence, and email data without calling a model.
3. Read Sections 1-2 and the first problem in [the handout](cs329z_assignment1_harness.pdf), then explain the intended data flow before implementation.
4. Start with the matching adapter in `cs329z_hw1/adapters.py` and its provided test file. The functions still raise `NotImplementedError`.

```bash
uv run --locked pytest --collect-only
uv run --locked pytest tests/test_priority.py
```

Both commands use the default non-live selection. Starter tests failing with `NotImplementedError` are expected. A passing local setup check is not a passing assignment.

Python 3.12 is selected in `.python-version`; `.venv` follows the original `uv.lock`. The local `.env` reuses the previously configured OpenRouter key. Credentials, extracted email data, model cache, and runs remain ignored. Key presence is checked; model access/credits have not been tested.

For a fresh checkout, run `uv sync --locked` and `uv run python data/download.py`. The latter verifies and unpacks the official archive, downloading it from the URL in `data/source.json` if needed. The compressed archive and its extracted contents are intentionally local.

Preserve provided code/tests and the dependency list. The handout prohibits agent/LLM frameworks and additional dependencies. Paid live tests are a later, explicit step after implementation and a budget/model check. No solution code or write-up has been supplied by the setup work.
