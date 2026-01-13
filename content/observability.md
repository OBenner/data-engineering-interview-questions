## [Main title](../README.md)
### [Interview questions](full.md)
#
# Data Observability
+ [What is data observability?](#What-is-data-observability)
+ [How is data observability different from application observability?](#How-is-data-observability-different-from-application-observability)
+ [What are the key signals you monitor for data pipelines?](#What-are-the-key-signals-you-monitor-for-data-pipelines)
+ [How do you define and measure an end-to-end SLA for data?](#How-do-you-define-and-measure-an-end-to-end-SLA-for-data)
+ [What should you log for each pipeline run?](#What-should-you-log-for-each-pipeline-run)
+ [How do you detect silent failures?](#How-do-you-detect-silent-failures)
+ [What is lineage and how does it help during incidents?](#What-is-lineage-and-how-does-it-help-during-incidents)
+ [How do you monitor and debug a broken metric in BI?](#How-do-you-monitor-and-debug-a-broken-metric-in-BI)
+ [How do you design alerts to avoid alert fatigue?](#How-do-you-design-alerts-to-avoid-alert-fatigue)
+ [How do you approach backfills safely?](#How-do-you-approach-backfills-safely)
+ [What is a runbook and what should it contain?](#What-is-a-runbook-and-what-should-it-contain)
+ [What are common incident patterns in data platforms?](#What-are-common-incident-patterns-in-data-platforms)

## What is data observability?
Data observability is the practice of monitoring, alerting, and diagnosing the health of data and data pipelines. It focuses on whether datasets are arriving on time, with correct volume and values, and whether downstream consumers can rely on them. The goal is to reduce “data downtime” and speed up root-cause analysis.

[Table of Contents](#Data-Observability)

## How is data observability different from application observability?
Application observability focuses on service health (latency, error rates, traces) for request/response systems. Data observability focuses on dataset health and pipeline behavior over time (freshness, completeness, distribution shifts). Data issues can be silent, delayed, and cumulative, so you need different signals and baselines.

[Table of Contents](#Data-Observability)

## What are the key signals you monitor for data pipelines?
Common signals include:
+ freshness (max event/ingestion time)
+ volume (row counts, bytes, partitions)
+ schema changes (added/removed/typed columns)
+ quality checks (null rates, uniqueness, referential integrity)
+ pipeline run status and duration
+ cost signals (query time, bytes scanned, cluster utilization)

[Table of Contents](#Data-Observability)

## How do you define and measure an end-to-end SLA for data?
You define the SLA from source event time to availability in the final dataset or BI metric. Measure it with timestamps at each stage (ingest, transform, publish) and compute percentiles (p50/p95) as well as breach counts. SLAs should reflect consumer needs and include ownership and escalation paths.

[Table of Contents](#Data-Observability)

## What should you log for each pipeline run?
At minimum:
+ inputs (source tables/partitions, offsets, watermarks)
+ outputs (target tables/partitions, row counts written)
+ runtime and resource usage
+ warnings/errors and retry attempts
+ data quality results summary
This makes runs reproducible and speeds up debugging.

[Table of Contents](#Data-Observability)

## How do you detect silent failures?
Silent failures happen when the job succeeds but data is wrong (missing subset, wrong join, truncation). Detect them with dataset-level checks: freshness, volume bounds, distribution checks, and reconciliations against sources. Monitoring key business KPIs for unexpected changes is also effective.

[Table of Contents](#Data-Observability)

## What is lineage and how does it help during incidents?
Lineage describes upstream/downstream dependencies between datasets, jobs, and dashboards. During incidents, lineage helps you assess blast radius (which reports are impacted) and prioritize fixes. It also helps prevent regressions by making dependencies explicit.

[Table of Contents](#Data-Observability)

## How do you monitor and debug a broken metric in BI?
You start from the metric definition and trace dependencies to the underlying tables. Then check data freshness and recent changes (deploys, schema changes, upstream outages). Use reconciliation queries and sampling to locate where the metric diverged, then confirm whether it is a data issue or a definition change.

[Table of Contents](#Data-Observability)

## How do you design alerts to avoid alert fatigue?
Alerts should be actionable, scoped, and owned. Use severity levels, suppression windows, and baselines that account for seasonality. Prefer multi-signal alerts (freshness + volume) over single noisy checks, and include runbooks with clear next steps.

[Table of Contents](#Data-Observability)

## How do you approach backfills safely?
Backfills can be expensive and risky because they rewrite history and can change metrics. A safe approach includes running in smaller batches, validating each batch, and separating “raw” from “published” layers so you can rebuild derived tables without re-ingesting sources. You also communicate expected metric changes and schedule around peak usage.

[Table of Contents](#Data-Observability)

## What is a runbook and what should it contain?
A runbook is a step-by-step guide for responding to an alert or incident. It should include impact assessment, common root causes, validation queries, mitigation steps, rollback/backfill steps, and escalation contacts. Good runbooks reduce time-to-recovery for on-call engineers.

[Table of Contents](#Data-Observability)

## What are common incident patterns in data platforms?
Common patterns include:
+ upstream outages and late data
+ schema changes breaking transforms
+ duplicates from retries/reprocessing
+ incorrect joins causing metric inflation
+ partition boundary/timezone bugs
+ cost spikes due to inefficient queries

[Table of Contents](#Data-Observability)

