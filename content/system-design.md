## [Main title](../README.md)
### [Interview questions](full.md)
#
# Data System Design
+ [How would you design an end-to-end batch analytics pipeline?](#How-would-you-design-an-end-to-end-batch-analytics-pipeline)
+ [How would you design a near-real-time ingestion pipeline?](#How-would-you-design-a-near-real-time-ingestion-pipeline)
+ [How do you ensure idempotency in data pipelines?](#How-do-you-ensure-idempotency-in-data-pipelines)
+ [How do you handle late arriving events and backfills?](#How-do-you-handle-late-arriving-events-and-backfills)
+ [How do you choose between batch and streaming?](#How-do-you-choose-between-batch-and-streaming)
+ [How do you model raw/silver/gold layers (bronze/silver/gold)?](#How-do-you-model-raw/silver/gold-layers-(bronze/silver/gold))
+ [How do you design a data platform for multiple teams (multi-tenancy)?](#How-do-you-design-a-data-platform-for-multiple-teams-(multi-tenancy))
+ [How do you design for schema evolution?](#How-do-you-design-for-schema-evolution)
+ [What are the main reliability patterns for pipelines?](#What-are-the-main-reliability-patterns-for-pipelines)
+ [How do you design observability for a data platform?](#How-do-you-design-observability-for-a-data-platform)
+ [How do you manage cost while meeting SLAs?](#How-do-you-manage-cost-while-meeting-SLAs)

## How would you design an end-to-end batch analytics pipeline?
A typical design is ingestion into a raw layer (immutable), transformation into curated datasets (cleaned and modeled), and publishing into marts/BI-serving datasets. You define SLAs, data quality checks, and ownership for each dataset. Batch pipelines are often scheduled daily/hourly and optimized for correctness and cost.

[Table of Contents](#Data-System-Design)

## How would you design a near-real-time ingestion pipeline?
You typically use an event log or CDC stream (Kafka/PubSub/Kinesis) and write to a raw append-only store with durable offsets. Downstream, you materialize current-state tables and metrics with windowing and deduplication. You must design for replays, ordering, and late events.

[Table of Contents](#Data-System-Design)

## How do you ensure idempotency in data pipelines?
Idempotency means retries do not change the final result. Common strategies include writing with deterministic keys (upserts/merges), using exactly-once features where available, and keeping raw data immutable while rebuilding derived layers. You also store checkpoints/watermarks consistently with writes.

[Table of Contents](#Data-System-Design)

## How do you handle late arriving events and backfills?
You define allowed lateness and design tables by event time, not just ingestion time. For late events, you reprocess affected windows/partitions and update derived outputs deterministically. Backfills should be incremental, validated, and isolated so they do not corrupt current reporting.

[Table of Contents](#Data-System-Design)

## How do you choose between batch and streaming?
Streaming is chosen for low latency and continuous updates, but it adds complexity (state, ordering, exactly-once). Batch is simpler and often cheaper for many analytics use cases. Many real systems are hybrid: streaming ingestion into raw, batch modeling into marts.

[Table of Contents](#Data-System-Design)

## How do you model raw/silver/gold layers (bronze/silver/gold)?
Bronze/raw is immutable ingestion with minimal transformation. Silver is cleaned, standardized, and deduplicated data with consistent schemas. Gold is business-ready marts and aggregates designed for BI and applications. This layering helps with reprocessing, governance, and clear contracts.

[Table of Contents](#Data-System-Design)

## How do you design a data platform for multiple teams (multi-tenancy)?
You need isolation (separate compute or quotas), clear ownership, and strong governance. Provide shared standards for naming, testing, and documentation, and a catalog for discovery. Multi-tenancy also requires controlling cost and preventing one team’s workloads from impacting others.

[Table of Contents](#Data-System-Design)

## How do you design for schema evolution?
You define compatibility rules, version schemas/contracts, and enforce them in CI and ingestion. Downstream transforms should tolerate additive fields but fail fast on breaking changes. You also maintain backward-compatible outputs where multiple consumers depend on stable schemas.

[Table of Contents](#Data-System-Design)

## What are the main reliability patterns for pipelines?
Common patterns include idempotent writes, retries with backoff, dead-letter queues, exactly-once or effectively-once processing, and separation of raw from derived layers. You also use checkpointing and consistent watermark management to avoid gaps and duplicates.

[Table of Contents](#Data-System-Design)

## How do you design observability for a data platform?
You monitor freshness, volume, quality, and lineage, plus pipeline runtime and failure rates. Alerts should be actionable with runbooks. Observability should be end-to-end: from source to final BI datasets and critical metrics.

[Table of Contents](#Data-System-Design)

## How do you manage cost while meeting SLAs?
You optimize storage layout (partitioning, file sizes), avoid unnecessary recomputation, and use selective materialization. You also schedule heavy jobs off-peak, enforce resource quotas, and track cost per dataset/pipeline. Cost is part of design, not just an afterthought.

[Table of Contents](#Data-System-Design)

