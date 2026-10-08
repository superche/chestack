# Measurement checklist

Answer these questions from actual runs before reporting a number:

1. What metric and unit are measured, and what user or system outcome does it represent?
2. What limits the result: CPU, I/O, memory, queueing, network, concurrency, or a fixed wait?
3. What workload and completed work count demonstrate that the intended work happened?
4. What errors, retries, dropped work, cache effects, or warm-up conditions could distort it?
5. Are baseline and candidate equivalent in environment, input, configuration, and observation boundary?
6. How many samples exist, how were runs interleaved, and how large is the noise?
7. What correctness/regression gates passed at the measured revisions?

Preserve raw samples and the command. Explain uncertainty and avoid ratios between unlike scenarios. A single observation can establish a failure exists; it rarely establishes a stable speedup. Evaluation results also need denominators, task distribution, grader rules, and failed or excluded trials.
