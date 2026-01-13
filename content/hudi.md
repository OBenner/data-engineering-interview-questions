## [Main title](../README.md)
### [Interview questions](full.md)
#
# Apache Hudi
+ [What is Apache Hudi?](#What-is-Apache-Hudi)
+ [What problems does Hudi solve in a data lake?](#What-problems-does-Hudi-solve-in-a-data-lake)
+ [What is the difference between Copy-on-Write (COW) and Merge-on-Read (MOR)?](#What-is-the-difference-between-Copy-on-Write-(COW)-and-Merge-on-Read-(MOR))
+ [How do you choose between COW and MOR?](#How-do-you-choose-between-COW-and-MOR)
+ [What is a record key, partition path, and precombine field?](#What-is-a-record-key-partition-path-and-precombine-field)
+ [How does Hudi support upserts?](#How-does-Hudi-support-upserts)
+ [What is compaction in Hudi?](#What-is-compaction-in-Hudi)
+ [What is clustering in Hudi and when do you need it?](#What-is-clustering-in-Hudi-and-when-do-you-need-it)
+ [Why does the small files problem happen and how do you mitigate it in Hudi?](#Why-does-the-small-files-problem-happen-and-how-do-you-mitigate-it-in-Hudi)
+ [How do you handle CDC with Hudi?](#How-do-you-handle-CDC-with-Hudi)
+ [What are common operational metrics for Hudi tables?](#What-are-common-operational-metrics-for-Hudi-tables)
+ [When would you choose Hudi vs Iceberg vs Delta?](#When-would-you-choose-Hudi-vs-Iceberg-vs-Delta)

## What is Apache Hudi?
Apache Hudi is an open-source data lakehouse framework that brings database-like capabilities (upserts, deletes, incremental pulls) to data lakes on object storage. It manages table metadata and timelines so batch and streaming engines can write and read consistently.

[Table of Contents](#Apache-Hudi)

## What problems does Hudi solve in a data lake?
Hudi enables efficient updates and deletes without rewriting entire datasets, supports incremental processing (read only changes), and helps manage small files and write amplification. It is commonly used for near-real-time ingestion and CDC-style workloads where tables must be kept up-to-date.

[Table of Contents](#Apache-Hudi)

## What is the difference between Copy-on-Write (COW) and Merge-on-Read (MOR)?
COW stores data in columnar files and rewrites them on updates, optimizing read performance at the cost of write amplification. MOR stores base files plus delta log files and merges them at read time (or during compaction), optimizing write performance at the cost of more complex reads.

[Table of Contents](#Apache-Hudi)

## How do you choose between COW and MOR?
Choose COW when read latency and query simplicity are most important and updates are moderate. Choose MOR when write throughput and near-real-time updates are critical, and you can manage compaction and read-time merges. The choice also depends on engine support and operational constraints.

[Table of Contents](#Apache-Hudi)

## What is a record key, partition path, and precombine field?
Record key identifies a row uniquely (like a primary key). Partition path controls how data is grouped for storage and pruning. Precombine field is used to resolve multiple records for the same key in a batch (for example choose the latest by `updated_at`) to ensure deterministic upserts.

[Table of Contents](#Apache-Hudi)

## How does Hudi support upserts?
Hudi indexes records by key and can locate existing records to update them. On upsert, it writes new versions and updates the timeline/metadata so readers see a consistent view. Correctness depends on stable keys and proper handling of late and duplicate events.

[Table of Contents](#Apache-Hudi)

## What is compaction in Hudi?
Compaction merges delta log files into base columnar files (mostly relevant for MOR tables). It improves read performance and reduces the overhead of reading many log files. Compaction must be scheduled and monitored to avoid backlog.

[Table of Contents](#Apache-Hudi)

## What is clustering in Hudi and when do you need it?
Clustering reorganizes data files to improve layout (file sizes, sorting, locality) and query performance. You use clustering to combat small files, improve pruning, or optimize for common access patterns (for example sorting by event time).

[Table of Contents](#Apache-Hudi)

## Why does the small files problem happen and how do you mitigate it in Hudi?
It happens when writers commit frequently with small batches or when partitions are highly granular. Mitigations include tuning write parallelism and file sizing, using clustering/compaction, and adjusting partitioning strategy to reduce tiny partitions.

[Table of Contents](#Apache-Hudi)

## How do you handle CDC with Hudi?
Hudi can ingest CDC events and apply them as upserts/deletes to maintain a current-state table. You typically standardize event ordering and deduplication (record key + precombine field) and monitor lag/compaction. Some setups also keep an append-only log for auditing alongside the current-state table.

[Table of Contents](#Apache-Hudi)

## What are common operational metrics for Hudi tables?
Common metrics include commit/compaction backlog, file counts per partition, average file size, write latency, failed commits, and query scan metrics. Operational alerts often focus on increasing small files and compaction lag.

[Table of Contents](#Apache-Hudi)

## When would you choose Hudi vs Iceberg vs Delta?
Hudi is often chosen for CDC-heavy and upsert/delete workloads with near-real-time ingestion requirements. Iceberg is often chosen for engine-agnostic open tables with strong metadata and evolution features. Delta is often chosen when you are aligned with the Delta ecosystem and its tooling. The best choice depends on engines, governance, and operational capabilities.

[Table of Contents](#Apache-Hudi)

