# Homework Setup Verification

Prepared on **2026-11-28**, America/Los_Angeles, on Apple Silicon macOS.

## Provenance and review scope

- HW1 upstream: `95f4cb7bfe28a27a7cf5bcb1eccb1aaaf1385eb3` from `cs329z/assignment1-harness`.
- HW2 upstream: `3a649d8da0dc6cb0422e6ce7ce7068c3b98be1db` from `cs329z/assignment2-evals`.
- Both handouts identify version 26.1.0. Their full text was extracted locally; setup/constraint-related selections were read. HW1 PDF pages 2-3 and HW2 PDF pages 3-4 were rendered and visually inspected. This is not a full-handout review or evidence that the learner completed the setup exercises.
- All 110 HW1 and 29 HW2 upstream files were compared against their original Git blob hashes: no supplied file changed, including adapters, tests, lock files, pinned agent, example task, and write-up templates.
- Added files are startup instructions, Python selection, editor workspaces, and an external prerequisite checker. The official mail archive remains local; `data/source.json` retains its download URL and checksum.

## Actual checks and outcomes

Commands inside each homework run from that homework's root unless stated otherwise.

| Check | Actual outcome |
|---|---|
| HW1: `uv sync --locked --python 3.12` | Exit 0; installed the locked environment with Python 3.12.13; local environment occupies about 64 MB |
| HW2: `uv sync --locked --python 3.12` | Exit 0; installed the locked environment with Python 3.12.13; local environment occupies about 305 MB |
| Study root: `python3 assignments/check_setup.py` | Exit 0 for both environments; checks local key presence without displaying it or contacting a provider |
| HW1: `uv run --locked --no-sync python data/download.py` | Exit 0; bundled SHA-256 checked and 26,278 records unpacked, about 58.4 MB |
| HW1: `uv run --locked --no-sync pytest --collect-only -m 'not live' -q` | Exit 0; deterministic tests collected successfully |
| HW1: import adapters, OpenAI, NumPy, pytest; call `sandbox.jail()` | Exit 0; imports succeeded and jail reports `sandbox-exec` |
| HW1: `uv run --locked --no-sync pytest tests/test_priority.py -m 'not live' -x -q` | Exit 1 as expected: first test reaches the unchanged adapter and raises `NotImplementedError`; stopped after that failure |
| HW2: `uv run --locked --no-sync harbor --version` | Exit 0; reports 0.18.0 |
| HW2: `uv run --locked --no-sync harbor --help` | Exit 0; CLI starts normally |
| `docker info --format '{{.ServerVersion}} {{.Architecture}}'` | Exit 0; Docker 29.4.0 server reachable on aarch64 |
| HW2: `uv run --locked --no-sync python check_submission.py` | Exit 1 as expected: 6 missing deliverable groups and 2 placeholder warnings in the unimplemented starter |
| Both `.code-workspace` files | Valid JSON; each has three explicit tasks and an existing folder |

Expected assignment failures are distinct from environment failures. No homework implementation tests passed as a result of mentor-written solutions. No oracle attempt, model run, task image download/build, custom evaluation task, or written response was produced. No provider credits were spent by these checks.

## Resume and publication

Open the matching `.code-workspace`, then follow that homework's `START-HERE.md`. Start Docker Desktop when working on HW2. Larger task images are downloaded/built when beginning the relevant exercise; apply the handout's amd64 setting specifically to its SWE-bench run.

The learner approved publication of this starter/setup snapshot, along with the current learning records, on November 28. Keys, `.venv`, downloaded/extracted mail data, and caches are excluded. Future learner homework changes require new explicit commit/push authorization. A local key being present does not establish provider access, model availability, credit balance, or successful live evaluation.
