# Proof of work

This runnable audit turns paired simulated and real rollout outcomes into a ranked sim-to-real gap report. It focuses on a narrow eval-layer question: which subtasks look successful in simulation but fail on hardware, especially around contact.

Verified locally with `python -m unittest -v` and `python audit.py sample_rollouts.csv --output report.json`.

All inputs are synthetic; no private company data is included.
