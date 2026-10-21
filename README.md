# rl-environments

Open RL environments and verifiers.

An environment here is three things:

- a **task** of several steps, not a question
- a **resettable system** the agent acts on
- a **verifier**: code that reads the final state and returns 1 or 0, with no human in the loop

The verifier is the artifact. A weak verifier does not leave a model unchanged — it makes it
worse: it teaches the model to game the check instead of doing the work.

## Layout

    environments/<name>/
      task.md      what the agent is asked to do
      env.py       the resettable state
      verify.py    the verifier
      tests/       cases the verifier must get right, including the cheating ones

## What every verifier here has to answer, in this order

1. **Integrity** — are all the expected objects there, and none invented?
2. **Exactness** — is each value *the* value, computed with exact arithmetic?
3. **Consistency** — do aggregates derive from their parts?
4. **Traceability** — is there a record of how it got there?
5. **Reproducibility** — does it run identically after a reset?

Integrity comes first. Ask about the numbers first and whoever deleted the hard rows passes.

## Status

Work in progress.
