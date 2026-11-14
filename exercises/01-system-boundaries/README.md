# E1 — System Boundaries in an Incident-Triage Assistant

**Type:** Mentor-designed practice, not official homework. **State:** Not Started. No implementation or answers have been provided.

## Objective

Understand how control flow, observations, state, and stopping rules distinguish a fixed workflow from a policy-directed agent loop. Test the controller independently of a language model before introducing model variability.

## Scenario

An assistant receives an alert and can search a tiny synthetic runbook collection. It may request a diagnostic observation, then return a recommendation or abstain. It cannot modify infrastructure or contact anyone.

Create three small fictional runbook fixtures and these request categories:

| Case | Request | Environmental condition |
|---|---|---|
| A | Investigate rising checkout latency | Relevant runbook and diagnostic result are available |
| B | Investigate an unfamiliar service error | No runbook supports a recommendation |
| C | Investigate intermittent queue delays | The diagnostic tool raises a simulated timeout |

The exact fixtures and supported conclusions are yours to define. Keep them obviously synthetic.

## Part A — Design First (20–30 minutes)

Write a 200–400 word English note, `design.md`, with two control-flow sketches:

1. A fixed workflow that retrieves once and produces a recommendation or abstains.
2. A loop in which a policy can choose a next tool action after receiving an observation.

Label the policy/model, controller, tools, observations, state, and environment. Explain who makes each decision, which state survives a step, how a failure is represented, and why execution must stop. Choose the simplest useful baseline and propose five tests. Present your design for review before implementing.

This is the **first practical task**. It does not require coding during the opening session.

## Part B — Implement the Controller (60–90 minutes after design review)

### Requirements

- Implement a small Python dispatcher with two local read-only tools, such as runbook lookup and simulated diagnostic lookup.
- Supply a scripted policy test double that produces predetermined actions. Its choices may depend on the current observation; the controller must pass observations back to it.
- Represent a tool action and a final answer/abstention distinctly. Define invalid-action behavior.
- Keep an execution trace with step number, selected action, arguments, result/error, and final status.
- Enforce a maximum of **three tool executions** per request. Define whether attempted failures consume that budget, and test the chosen rule. A policy that keeps requesting tools must terminate with an explicit budget status.
- Separately cap the request at **five policy decisions**, including invalid actions. Repeated invalid actions must not evade termination merely because no tool executes.
- Make invalid tools and tool exceptions produce controlled outcomes. Do not silently treat missing evidence or exceptions as successful recommendations.

### Constraints

Use the Python standard library and `unittest`; no dependency installation, agent framework, LLM, network call, shell execution, real logs, or infrastructure changes. The learner writes `controller.py`, synthetic fixtures, and `test_controller.py`. A scripted policy is a test fixture: passing these tests establishes controller behavior, not agent intelligence or real-world task success.

### Success Criteria

The trace makes each action and stopping reason inspectable. Invalid actions never invoke a tool. Every request finishes within the declared budget, including an endlessly requesting policy. A final recommendation identifies fixture evidence or explicitly abstains. The learner can explain how a real model would later replace the policy double without moving execution authority into model text.

### Tests

Verify at least these independent behaviors:

1. A successful supported recommendation returns expected evidence and final status.
2. A missing-runbook case abstains without inventing evidence.
3. An unknown tool is rejected without invoking any registered tool.
4. A tool timeout has an explicit bounded failure/retry outcome.
5. A policy that never finishes hits the execution limit and terminates.
6. A policy that repeatedly requests an unknown tool hits the decision limit or terminates earlier with an explicit error.

Run from this directory after writing the files:

```bash
python3 -m unittest discover -s . -p 'test_*.py' -v
```

Record the real command/output summary in a learner-authored reflection. Ensure tests were discovered; an empty passing run is not evidence. No tests have been run during setup because no implementation exists.

### Reflection

Which behavior was guaranteed by code, and which came from the policy fixture? What new failure cases appear with a stochastic model? Which application requirements would justify adaptive action selection? What will these tests fail to tell you about a deployed assistant?

## Deliverables and Review

Deliver the design note, controller, fixtures, tests, and a short reflection. Explain one trace from start to finish and adapt your design to an unfamiliar alert. The mentor gives targeted feedback and records actual evidence in `PROGRESS.md`; no completion is inferred from files merely existing.
