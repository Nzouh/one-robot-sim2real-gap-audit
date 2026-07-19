# One Robot sim-to-real gap audit

A dependency-free rollout audit that pairs simulated and real results by task/subtask, ranks success-rate gaps, and carries contact-error counts into an inspectable JSON report.

```bash
python audit.py sample_rollouts.csv --output report.json
python -m unittest -v
```

The sample is synthetic. This does not reproduce One Robot's world models or use company data; it is a complementary release-checking wedge. Next steps could include confidence intervals and trajectory-boundary localization.
