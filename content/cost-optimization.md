## [Main title](../README.md)
### [Interview questions](full.md)
#
# Cost Optimization
+ [Why is cost optimization a core data engineering skill?](#Why-is-cost-optimization-a-core-data-engineering-skill)
+ [What are the main cost drivers in data platforms?](#What-are-the-main-cost-drivers-in-data-platforms)
+ [How does partitioning affect cost and performance?](#How-does-partitioning-affect-cost-and-performance)
+ [What is the small files problem and why does it increase cost?](#What-is-the-small-files-problem-and-why-does-it-increase-cost)
+ [How do you choose a target file size for Parquet tables?](#How-do-you-choose-a-target-file-size-for-Parquet-tables)
+ [How do you detect and fix data skew in distributed processing?](#How-do-you-detect-and-fix-data-skew-in-distributed-processing)
+ [What is shuffle and how do you reduce it in Spark?](#What-is-shuffle-and-how-do-you-reduce-it-in-Spark)
+ [When should you pre-aggregate or materialize tables?](#When-should-you-pre-aggregate-or-materialize-tables)
+ [How do you prevent runaway queries and protect shared clusters?](#How-do-you-prevent-runaway-queries-and-protect-shared-clusters)
+ [How do you optimize joins in large-scale analytics?](#How-do-you-optimize-joins-in-large-scale-analytics)
+ [How do you plan and estimate the cost of a backfill?](#How-do-you-plan-and-estimate-the-cost-of-a-backfill)
+ [What metrics would you track for FinOps in data engineering?](#What-metrics-would-you-track-for-FinOps-in-data-engineering)

## Why is cost optimization a core data engineering skill?
Data platforms can scale costs linearly or worse with data volume and usage. Cost optimization ensures the platform remains sustainable while meeting SLAs. It requires understanding storage layout, compute behavior, query patterns, and operational practices like backfills and compaction.

[Table of Contents](#Cost-Optimization)

## What are the main cost drivers in data platforms?
Typical drivers include:
+ compute time (clusters, warehouses, serverless slots)
+ bytes scanned and shuffles
+ storage growth (raw + derived + duplicates)
+ data movement (egress, cross-region transfers)
+ operational overhead (frequent backfills, retries)

[Table of Contents](#Cost-Optimization)

## How does partitioning affect cost and performance?
Good partitioning reduces scanned data by enabling partition pruning. Bad partitioning creates too many small partitions, increasing metadata overhead and small files. Partitioning should match common query filters and data distribution, and be reevaluated as workloads evolve.

[Table of Contents](#Cost-Optimization)

## What is the small files problem and why does it increase cost?
Small files increase scheduling and metadata overhead and reduce scan efficiency. Engines spend more time opening and planning files than processing data. Small files often appear from streaming writes or overly granular partitions and typically require compaction or clustering to fix.

[Table of Contents](#Cost-Optimization)

## How do you choose a target file size for Parquet tables?
You choose a size that balances parallelism and overhead. Too small increases file count and planning cost; too large reduces parallelism and can slow selective queries. Many teams target hundreds of MB per file, but the correct value depends on the engine, storage, and query patterns.

[Table of Contents](#Cost-Optimization)

## How do you detect and fix data skew in distributed processing?
Skew happens when some partitions have much more data than others, causing straggler tasks. Detect it via task duration distributions and partition size metrics. Fixes include salting keys, using skew-aware joins, repartitioning, or changing the join strategy (broadcast when possible).

[Table of Contents](#Cost-Optimization)

## What is shuffle and how do you reduce it in Spark?
Shuffle is data redistribution across executors (for joins, group by, distinct). It is expensive due to network IO and disk spills. You reduce shuffle by using proper partitioning, avoiding wide transformations, filtering early, broadcasting small tables, and tuning shuffle partitions.

[Table of Contents](#Cost-Optimization)

## When should you pre-aggregate or materialize tables?
Materialize when many downstream queries reuse expensive computations or when interactive BI requires low latency. Avoid over-materialization because it increases storage and refresh complexity. A good approach is to materialize stable, high-value marts and keep exploratory logic as views.

[Table of Contents](#Cost-Optimization)

## How do you prevent runaway queries and protect shared clusters?
Use workload management: query timeouts, concurrency limits, resource quotas, and separate compute for heavy workloads. Enforce best practices with guardrails (linting, cost alerts) and educate users with profiling tools. Multi-tenant platforms typically need isolation to prevent one team from impacting others.

[Table of Contents](#Cost-Optimization)

## How do you optimize joins in large-scale analytics?
You optimize joins by ensuring join keys are clean and well-distributed, filtering before joins, and choosing appropriate join strategies (broadcast vs shuffle). You also reduce the size of join inputs (select only needed columns) and consider pre-joining into curated marts when joins are repeated.

[Table of Contents](#Cost-Optimization)

## How do you plan and estimate the cost of a backfill?
Estimate based on data volume, compute requirements, and expected scan/shuffle behavior. Run on a small sample window to measure throughput and extrapolate. Backfills should be staged, monitored, and preferably run in off-peak windows, with a clear rollback plan.

[Table of Contents](#Cost-Optimization)

## What metrics would you track for FinOps in data engineering?
Common metrics include cost by team/project, cost per pipeline, bytes scanned per query, cluster utilization, storage growth by layer, and top expensive datasets/queries. You also track trend changes (week-over-week) and tie cost to value (usage, criticality).

[Table of Contents](#Cost-Optimization)

