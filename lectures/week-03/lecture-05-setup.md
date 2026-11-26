# Lecture 5 Notebook Setup

Official lecture demo, prepared on November 25, 2026. This environment is separate from official homework implementations.

## Source and working copy

- Official repository: [cs329z/lecture5-frameworks](https://github.com/cs329z/lecture5-frameworks).
- Checked-out commit: `4e418289b3032cb960984250395525eb91ae25c2`.
- Local working directory, relative to the study repository: `notebooks/lecture-05/`.
- Notebook: `notebooks/lecture-05/lecture5.ipynb`.
- The working copy has its own Git history and is ignored by the study repository, including credentials, notebook outputs, environments, and calendar state.
- During initial setup, all notebook cell sources were preserved. Only kernel display/name metadata and Python version metadata were adjusted for the local environment.

At initial setup, the official schedule's code link and the repository's README, setup script, dependency file, lockfile, and notebook were inspected. The slide PDF text fetch exceeded the web tool's size limit then. Selected slide pages were subsequently downloaded and inspected on November 26, as recorded in the [references](references.md#lecture-5-framework-landscape-and-agent-harnesses); video playback by the mentor is not claimed.

## Environment

The existing Apple Silicon Python 3.12 installation was reused. `uv sync --locked` installed the course's locked dependencies in the working copy's `.venv`; no local LLM weights were downloaded.

| Component | Installed version |
|---|---|
| Python | 3.12.13 |
| DSPy | 3.4.0 |
| LangGraph | 1.2.12 |
| LangChain OpenAI | 1.6.7 |
| Temporal Python SDK | 1.34.0 |
| IPython kernel | 7.4.0 |
| JupyterLab | 4.6.4 |
| Deno | 2.9.7, native Apple Silicon |

The registered kernel is **CS329Z Lecture 5 (Python 3.12)**, with kernel name `cs329z-lecture05`. Project-local VS Code settings point to `.venv/bin/python` and use the lecture directory as the notebook working directory. Python and Jupyter extensions were already installed.

## Open and follow along

From the study repository:

```bash
code notebooks/lecture-05 notebooks/lecture-05/lecture5.ipynb
```

Select **CS329Z Lecture 5 (Python 3.12)** in the notebook's kernel picker if it is not selected automatically. The project `.venv` Python 3.12 interpreter is the equivalent choice.

Run cells in lecture order. Parts 2 and 3 reuse definitions from Part 1. Begin with the setup cells and the first DSPy signature example; leave evaluation and GEPA optimization until the instructor reaches them.

### OpenRouter credentials

The notebook reads `OPENROUTER_API_KEY` from the working copy's `.env`. Enter the value locally, never in chat, code, notebook outputs, or command-line arguments. The file has permissions `0600` and is ignored by both repositories.

Use a regular model-inference key from the [OpenRouter API Keys page](https://openrouter.ai/settings/keys). A Management API Key can administer keys but cannot call completion endpoints. Both types can have an OpenRouter-looking prefix, so the prefix alone does not establish suitability. [Management key restrictions](https://openrouter.ai/blog/tutorials/team-spend-controls-setup/)

The first supplied key was identified by OpenRouter as a management key: metadata authentication returned HTTP 200, while inference returned HTTP 401, `User not found`. The learner replaced it locally with a regular inference key. **Both DSPy and LangChain/OpenRouter then returned successful responses to minimal connectivity prompts.** No credential value or account usage data is recorded here.

If the key changes after a notebook kernel has loaded it, restart the kernel and rerun the setup cells. The notebook uses `load_dotenv()` without overriding an already populated process environment.

The notebook uses the hosted models `openai/gpt-5.4-nano` and `google/gemma-3-12b-it`; both were present in the public model catalog when checked. The README estimates roughly one cent for a full notebook run. This is the author's estimate, not a spending guarantee; actual charges depend on model responses, retries, evaluation, and optimization calls.

### Local calendar

The setup started tinycal as a background process at **http://127.0.0.1:8765**. Its log and process ID are under the ignored working copy's `.runtime/` directory. Its HTTP endpoint was checked without adding, clearing, or changing events.

If the calendar is not already running, start it in a separate terminal:

```bash
cd notebooks/lecture-05
uv run python -m tinycal
```

The notebook can reuse that process. Its own setup cell intentionally clears this local demo calendar and adds the lecture's sample events. These are local tinycal events, not an external personal calendar.

The instructor's examples use October 5–9, 2026. Navigate to those dates in the calendar when following the demo, even if the calendar initially opens on today's date.

### Temporal and notebook ordering

The notebook's Temporal setup cell starts a local development server and its UI on port 8233. A separate startup/health smoke test downloaded the needed binary, passed, and shut down its server afterward. The notebook can therefore start its own instance. If an old notebook kernel later holds that port, restart that kernel as directed by the upstream README.

The LangGraph diagram rendering path was checked with a tiny synthetic graph. Deno's Python sandbox was checked with arithmetic only. Neither check ran the lecture's LLM exercises.

## Verification evidence

| Command or check | Observed result |
|---|---|
| `uv sync --locked` | Resolved the official lockfile and installed 170 packages |
| `uv pip check` | All installed packages compatible |
| Framework and course-helper imports | Passed |
| `nbformat.validate` and compilation with top-level-await support | Notebook valid; all 51 code cells compiled |
| Registered-kernel startup via `jupyter_client` | Python 3.12 and course imports passed; test kernel stopped |
| `dspy.PythonInterpreter` arithmetic | Deno-backed execution completed; interpreter closed |
| Synthetic `StateGraph` invocation and `draw_mermaid_png` | Passed; PNG signature checked |
| `WorkflowEnvironment.start_local` and service health | Healthy; smoke-test server stopped |
| tinycal `GET /api/today` | Passed; service left available for the learner |
| Original notebook's DSPy model constructor | Initializes successfully |
| OpenRouter inference | Regular key authenticated; two minimal requests passed through DSPy and LangChain using the notebook's main model |
| Git exclusion and credential file permissions | Working copy excluded; `.env` mode `0600` |
| VS Code opening and kernel configuration | Notebook opened through the CLI; kernel registered and metadata pinned. GUI selection was not visually verified, so check the kernel picker before running cells |

Two successful minimal model invocations were used for environment verification. No full notebook run, learner exercise solution, GEPA optimization, benchmark, or Gemma extraction run is claimed. The local environment setup is administration, not evidence of mastering DSPy, LangGraph, or Temporal.

## November 26 session shutdown

The learner reported finishing the L05 video and requested closing the notebook. The active course kernel was identified by its working directory and shut down through the Jupyter control channel; `shutdown_reply` was received. The Temporal development server was a child of that kernel and exited. The separately started tinycal process was sent SIGTERM. The saved notebook remains local and ignored; its cell count differs from the earlier setup snapshot, so the earlier 51-cell validation is historical environment evidence, not verification of subsequent learner edits.

Native desktop control timed out, and macOS denied assistive access to the UI fallback. The mentor therefore could not save unsaved editor buffers or close the VS Code tab. Save any pending changes and close the tab manually. No unrelated editor windows or application processes were closed. The environment, credentials, and notebook were retained for later reuse.

## Sources

- [Official lecture repository and run instructions](https://github.com/cs329z/lecture5-frameworks)
- [Official course schedule](https://cs329z.stanford.edu/)
- [OpenRouter current-key metadata](https://openrouter.ai/docs/api/api-reference/api-keys/get-current-key)
- [OpenRouter management versus inference keys](https://openrouter.ai/blog/tutorials/team-spend-controls-setup/)
