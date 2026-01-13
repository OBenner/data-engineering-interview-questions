## [Main title](../README.md)
### [Interview questions](full.md)
#
# Data Quality
+ [What does data quality mean in data engineering?](#What-does-data-quality-mean-in-data-engineering)
+ [What are common dimensions of data quality?](#What-are-common-dimensions-of-data-quality)
+ [What is data freshness and how do you measure it?](#What-is-data-freshness-and-how-do-you-measure-it)
+ [What is the difference between data validation and data reconciliation?](#What-is-the-difference-between-data-validation-and-data-reconciliation)
+ [What are row-level checks and aggregate checks?](#What-are-row-level-checks-and-aggregate-checks)
+ [How do you design quality checks for incremental pipelines?](#How-do-you-design-quality-checks-for-incremental-pipelines)
+ [How do you handle late arriving data from a quality perspective?](#How-do-you-handle-late-arriving-data-from-a-quality-perspective)
+ [How do you detect schema drift and breaking changes?](#How-do-you-detect-schema-drift-and-breaking-changes)
+ [What are data contracts?](#What-are-data-contracts)
+ [How do you avoid noisy alerts (false positives) in data quality monitoring?](#How-do-you-avoid-noisy-alerts-(false-positives)-in-data-quality-monitoring)
+ [What is anomaly detection for metrics and when is it useful?](#What-is-anomaly-detection-for-metrics-and-when-is-it-useful)
+ [How do you quarantine bad data without blocking the entire pipeline?](#How-do-you-quarantine-bad-data-without-blocking-the-entire-pipeline)
+ [How do you test data transformations?](#How-do-you-test-data-transformations)
+ [What is the minimum set of checks you would add to every table?](#What-is-the-minimum-set-of-checks-you-would-add-to-every-table)
+ [What are common data quality failure modes?](#What-are-common-data-quality-failure-modes)

## What does data quality mean in data engineering?
Data quality means the data is fit for its intended use. In practice, it means data is correct, complete, consistent, timely, and well-defined so downstream consumers can trust metrics. Data quality is both a technical problem (pipelines) and a product problem (definitions and contracts).

[Table of Contents](#Data-Quality)

## What are common dimensions of data quality?
Common dimensions include:
+ completeness (missing rows/fields)
+ validity (values in allowed ranges/domains)
+ accuracy (matches real-world or source truth)
+ consistency (no contradictions across tables)
+ timeliness/freshness (arrives within SLA)
+ uniqueness (no duplicates where keys should be unique)

[Table of Contents](#Data-Quality)

## What is data freshness and how do you measure it?
Freshness is how recently data was updated relative to expected cadence. You can measure it by comparing the maximum event/ingestion timestamp in a table to current time, and alert when it exceeds an SLA threshold. Freshness should be defined per dataset because “daily” and “real-time” pipelines differ.

[Table of Contents](#Data-Quality)

## What is the difference between data validation and data reconciliation?
Validation checks whether a dataset satisfies rules (types, constraints, ranges). Reconciliation compares datasets to ensure they match expected totals or invariants (for example source row count vs target row count, or sum(amount) in source vs warehouse). Reconciliation is important when multiple systems can drift.

[Table of Contents](#Data-Quality)

## What are row-level checks and aggregate checks?
Row-level checks validate each record (for example `not_null`, regex, range constraints). Aggregate checks validate the dataset as a whole (row counts, distinct counts, distribution checks, totals). Aggregate checks often catch issues that row-level rules miss, like missing partitions.

[Table of Contents](#Data-Quality)

## How do you design quality checks for incremental pipelines?
Checks should be scoped to the incremental window and also protect the full table invariants. For example, validate uniqueness on the keys in the new batch, validate that the batch size is within expected bounds, and validate that total counts change consistently. You also need idempotency checks to detect duplicates on retries.

[Table of Contents](#Data-Quality)

## How do you handle late arriving data from a quality perspective?
You define allowed lateness (for example 7 days), track completeness by event time, and implement backfills to “close” historical partitions. Quality checks should consider both ingestion time and event time so you can detect gaps in past periods.

[Table of Contents](#Data-Quality)

## How do you detect schema drift and breaking changes?
You compare incoming schemas to an expected contract (column names, types, nullability) and alert on changes. Additive changes can be allowed with policy, but breaking changes (rename/type change) should fail fast. Many teams use CI checks and schema registries to enforce compatibility.

[Table of Contents](#Data-Quality)

## What are data contracts?
Data contracts are explicit agreements between producers and consumers about schema, semantics, SLAs, and ownership. Contracts reduce surprises by defining what can change and what cannot, and they enable automated validation. A contract can live as code (YAML/JSON) and be enforced in CI/CD.

[Table of Contents](#Data-Quality)

## How do you avoid noisy alerts (false positives) in data quality monitoring?
Use dynamic thresholds, seasonality-aware baselines, and multi-signal alerts (freshness + volume + error rate). Also route alerts by severity and dataset criticality, and suppress alerts during known maintenance windows. Good alerting includes a runbook and clear ownership.

[Table of Contents](#Data-Quality)

## What is anomaly detection for metrics and when is it useful?
Anomaly detection flags unusual changes in metrics (spikes/drops) that may indicate pipeline issues or business events. It is useful for detecting silent failures where data still arrives but is wrong. It should be combined with context (releases, campaigns) to avoid alert fatigue.

[Table of Contents](#Data-Quality)

## How do you quarantine bad data without blocking the entire pipeline?
A common pattern is to split data into “good” and “quarantine” outputs based on validation rules. You can store bad rows with error reasons for debugging while allowing the pipeline to continue for valid data. For critical datasets, you may still block publishing to marts while keeping raw ingestion running.

[Table of Contents](#Data-Quality)

## How do you test data transformations?
You can test transformations by:
+ unit-like tests on small fixtures (golden datasets)
+ property tests (invariants like non-negative totals)
+ reconciliation tests against known sources
+ regression tests on key metrics
In dbt-style workflows, tests often run in the warehouse as SQL assertions.

[Table of Contents](#Data-Quality)

## What is the minimum set of checks you would add to every table?
Minimum checks often include:
+ freshness (max timestamp within SLA)
+ row count / volume sanity check
+ primary key uniqueness (if applicable)
+ not_null checks on critical columns
+ referential integrity for key joins (where applicable)

[Table of Contents](#Data-Quality)

## What are common data quality failure modes?
Common failures include:
+ missing partitions or partial loads
+ duplicates due to retries/reprocessing
+ schema drift and type coercion issues
+ timezone and date boundary bugs
+ silent truncation or rounding changes
+ incorrect joins causing duplication

[Table of Contents](#Data-Quality)

