## [Main title](../README.md)
### [Interview questions](full.md)
#
# Change Data Capture (CDC)
+ [What is CDC (Change Data Capture)?](#What-is-CDC-(Change-Data-Capture))
+ [When would you choose CDC over batch ingestion?](#When-would-you-choose-CDC-over-batch-ingestion)
+ [What are common CDC sources (WAL/binlog/triggers) and trade-offs?](#What-are-common-CDC-sources-(WAL/binlog/triggers)-and-trade-offs)
+ [What is the difference between snapshot and incremental CDC?](#What-is-the-difference-between-snapshot-and-incremental-CDC)
+ [What delivery semantics exist (at-most-once/at-least-once/exactly-once)?](#What-delivery-semantics-exist-(at-most-once/at-least-once/exactly-once))
+ [How do you make CDC ingestion idempotent?](#How-do-you-make-CDC-ingestion-idempotent)
+ [How do you handle deletes in CDC pipelines?](#How-do-you-handle-deletes-in-CDC-pipelines)
+ [How do you handle updates when the source does not provide full row images?](#How-do-you-handle-updates-when-the-source-does-not-provide-full-row-images)
+ [What is ordering and why is it hard in CDC?](#What-is-ordering-and-why-is-it-hard-in-CDC)
+ [What is a watermark/offset and where should it be stored?](#What-is-a-watermark/offset-and-where-should-it-be-stored)
+ [How do you handle schema evolution with CDC?](#How-do-you-handle-schema-evolution-with-CDC)
+ [What is the outbox pattern and why is it useful?](#What-is-the-outbox-pattern-and-why-is-it-useful)
+ [How do you monitor CDC lag and where can lag come from?](#How-do-you-monitor-CDC-lag-and-where-can-lag-come-from)
+ [How do you design a safe backfill/reprocessing strategy for CDC?](#How-do-you-design-a-safe-backfill/reprocessing-strategy-for-CDC)
+ [What are the most common failure modes in CDC pipelines?](#What-are-the-most-common-failure-modes-in-CDC-pipelines)

## What is CDC (Change Data Capture)?
CDC is a technique to capture row-level changes (inserts, updates, deletes) from a source system and stream them downstream. In databases, CDC is commonly log-based (reading WAL/binlog) so it can capture changes without repeatedly scanning full tables. CDC pipelines often feed event logs (append-only) and/or materialized current-state tables.

[Table of Contents](#Change-Data-Capture-(CDC))

## When would you choose CDC over batch ingestion?
Choose CDC when you need low-latency updates, continuous incremental processing, or a reliable change history. CDC is also useful when full-table scans are too expensive because the source is large or changes frequently. Batch ingestion is often simpler when latency requirements are relaxed and operational complexity should be minimized.

[Table of Contents](#Change-Data-Capture-(CDC))

## What are common CDC sources (WAL/binlog/triggers) and trade-offs?
Common sources are:
+ database logs (WAL/binlog): low overhead and high fidelity, but requires privileges and careful offset handling
+ triggers: can work without log access, but adds write overhead and is easy to break
+ timestamp-based queries: simple but can miss updates or create duplicates if clocks/transactions behave unexpectedly
Log-based CDC is usually preferred for production at scale.

[Table of Contents](#Change-Data-Capture-(CDC))

## What is the difference between snapshot and incremental CDC?
A snapshot reads an initial consistent baseline of existing rows. Incremental CDC then streams changes after that baseline using a log position/offset. Many systems require both: snapshot for bootstrap, incremental for ongoing updates.

[Table of Contents](#Change-Data-Capture-(CDC))

## What delivery semantics exist (at-most-once/at-least-once/exactly-once)?
At-most-once can lose messages but avoids duplicates. At-least-once avoids loss but can produce duplicates on retries. Exactly-once is hard end-to-end; many systems implement “effectively once” by combining at-least-once delivery with idempotent writes and deterministic merge logic.

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you make CDC ingestion idempotent?
You make downstream writes idempotent by using stable keys (primary key + source LSN/transaction id) and applying deterministic upsert/merge logic. A common pattern is to load changes into an append-only raw log, then build current-state tables using “latest per key” logic. Idempotency must hold across retries and replays.

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you handle deletes in CDC pipelines?
Deletes may appear as explicit delete events, tombstones, or a “before image” without an “after image”. Downstream you can:
+ apply hard deletes (remove row)
+ apply soft deletes (is_deleted flag with deleted_at)
+ keep full history (append-only) and compute current state with delete logic
The choice depends on compliance, analytics needs, and downstream consumers.

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you handle updates when the source does not provide full row images?
If updates are partial (only changed columns), you often need to reconstruct the full row by joining against previous state. Some CDC tools can be configured to emit before/after images; if not, current-state reconstruction becomes part of your pipeline. You must also handle out-of-order updates carefully.

[Table of Contents](#Change-Data-Capture-(CDC))

## What is ordering and why is it hard in CDC?
Ordering means applying changes in the same order they happened in the source. It is hard because events can be partitioned (multiple tables/partitions), delivered out of order, or retried. Correctness often requires per-key ordering (or per-partition ordering) using source transaction metadata.

[Table of Contents](#Change-Data-Capture-(CDC))

## What is a watermark/offset and where should it be stored?
An offset (watermark) is the position in the source log (or stream) up to which changes have been processed. It should be stored durably in the ingestion system (connector state store) and, for reliability, often also in your platform (for example a control table) so you can audit and recover. Offsets must be updated atomically with downstream writes to avoid gaps/duplicates.

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you handle schema evolution with CDC?
You need a strategy for compatible changes (additive columns) and breaking changes (renames, type changes). Common tools include schema registries and compatibility policies, plus strict validation in CI. Downstream tables should tolerate additive fields, and pipelines should alert on breaking changes before production data is corrupted.

[Table of Contents](#Change-Data-Capture-(CDC))

## What is the outbox pattern and why is it useful?
The outbox pattern writes business events into an “outbox” table in the same transaction as the application write. CDC then captures the outbox changes and publishes them reliably. This avoids dual-write problems where the database update succeeds but the event publish fails (or vice versa).

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you monitor CDC lag and where can lag come from?
Lag can come from:
+ source: heavy write load, log retention limits
+ connector: slow polling, backpressure, failures
+ broker/stream: throughput limits, partition hotspots
+ downstream: slow merges/compaction, expensive transformations
You monitor lag using source LSN vs processed LSN, consumer offsets, and end-to-end freshness in target tables.

[Table of Contents](#Change-Data-Capture-(CDC))

## How do you design a safe backfill/reprocessing strategy for CDC?
A safe strategy usually separates raw change storage from derived tables. You keep the raw CDC log (immutable) and rebuild derived current-state/marts from it when needed. For backfills, you often run in a separate environment or commit to new snapshots/versions, then switch consumers after validation.

[Table of Contents](#Change-Data-Capture-(CDC))

## What are the most common failure modes in CDC pipelines?
Common issues include:
+ duplicates due to retries/rebalances
+ missed events due to offset mismanagement or log retention
+ schema drift/breaking changes
+ incorrect delete handling
+ out-of-order application of updates
Good pipelines treat CDC as “production software” with strong observability and tests.

[Table of Contents](#Change-Data-Capture-(CDC))

