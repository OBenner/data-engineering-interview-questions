## [Main title](../README.md)
### [Interview questions](full.md)
#
# Apache Iceberg
+ [What is Apache Iceberg?](#What-is-Apache-Iceberg)
+ [What problems does Iceberg solve compared to plain Parquet datasets?](#What-problems-does-Iceberg-solve-compared-to-plain-Parquet-datasets)
+ [What is a snapshot in Iceberg?](#What-is-a-snapshot-in-Iceberg)
+ [What is time travel and why is it useful?](#What-is-time-travel-and-why-is-it-useful)
+ [How does Iceberg handle concurrent writes?](#How-does-Iceberg-handle-concurrent-writes)
+ [What is hidden partitioning in Iceberg?](#What-is-hidden-partitioning-in-Iceberg)
+ [What is partition evolution and why is it important?](#What-is-partition-evolution-and-why-is-it-important)
+ [How does schema evolution work in Iceberg?](#How-does-schema-evolution-work-in-Iceberg)
+ [What are equality deletes and positional deletes?](#What-are-equality-deletes-and-positional-deletes)
+ [How do upserts/merges work with Iceberg?](#How-do-upserts/merges-work-with-Iceberg)
+ [Why does the small files problem happen and how do you mitigate it?](#Why-does-the-small-files-problem-happen-and-how-do-you-mitigate-it)
+ [What maintenance operations are common for Iceberg tables?](#What-maintenance-operations-are-common-for-Iceberg-tables)
+ [What is an Iceberg catalog and what options exist?](#What-is-an-Iceberg-catalog-and-what-options-exist)
+ [How would you migrate an existing dataset to Iceberg?](#How-would-you-migrate-an-existing-dataset-to-Iceberg)
+ [Iceberg vs Delta vs Hudi: when would you choose Iceberg?](#Iceberg-vs-Delta-vs-Hudi:-when-would-you-choose-Iceberg)

## What is Apache Iceberg?
Apache Iceberg is an open table format for large analytics datasets. It defines how table metadata, snapshots, and data files are managed so multiple engines can read and write the same tables safely. Iceberg tables are usually stored on object storage (S3/GCS/ADLS) with files like Parquet, but the table semantics (transactions, schema/partition evolution) come from Iceberg metadata.

[Table of Contents](#Apache-Iceberg)

## What problems does Iceberg solve compared to plain Parquet datasets?
A plain Parquet “dataset in folders” lacks transactional guarantees and consistent metadata. Iceberg adds ACID-like commits, consistent snapshots, reliable schema/partition evolution, and query planning features like partition pruning based on metadata. It also supports deletes and updates in a table-like way rather than “rewrite everything”.

[Table of Contents](#Apache-Iceberg)

## What is a snapshot in Iceberg?
A snapshot is a point-in-time view of the table. Each commit creates a new snapshot that references a set of data and delete files through metadata (manifest lists/manifests). Readers can query a specific snapshot to get consistent results even while writers continue to append or modify the table.

[Table of Contents](#Apache-Iceberg)

## What is time travel and why is it useful?
Time travel means querying the table “as of” a previous snapshot (or timestamp). It is useful for debugging regressions, auditing changes, reproducing past reports, and safe backfills (compute against a stable snapshot and then commit a new one).

[Table of Contents](#Apache-Iceberg)

## How does Iceberg handle concurrent writes?
Iceberg typically uses optimistic concurrency control. Writers create new metadata based on a known current snapshot and then attempt to commit; if the base snapshot changed, the commit may conflict and must be retried. This prevents silent lost updates and keeps commits atomic.

[Table of Contents](#Apache-Iceberg)

## What is hidden partitioning in Iceberg?
Hidden partitioning means partitioning is defined at the table metadata level (for example `day(ts)`), not as user-managed folder paths. Engines can still prune partitions, but you are not tied to a physical directory layout. This makes partition evolution safer and avoids leaking storage details into query logic.

[Table of Contents](#Apache-Iceberg)

## What is partition evolution and why is it important?
Partition evolution allows changing the partition spec over time (for example switching from `day(ts)` to `month(ts)` or adding a new partition field) without rewriting all historical data. It matters because real datasets change: query patterns evolve, and the “right” partitioning today may not be right in a year.

[Table of Contents](#Apache-Iceberg)

## How does schema evolution work in Iceberg?
Iceberg tracks columns by unique field IDs, enabling safe add/drop/rename operations without breaking readers. Schema evolution can be applied while keeping historical snapshots queryable. Some changes (like certain type changes) depend on engine support and can still be risky if consumers assume fixed schemas.

[Table of Contents](#Apache-Iceberg)

## What are equality deletes and positional deletes?
Deletes in Iceberg can be represented as separate delete files:
+ equality deletes: delete rows matching a key predicate (for example `id = 123`)
+ positional deletes: delete specific row positions in data files
They allow deletes without rewriting full data files, but too many delete files can hurt performance until compacted.

[Table of Contents](#Apache-Iceberg)

## How do upserts/merges work with Iceberg?
Upserts are usually implemented by engines (Spark/Flink/Trino) using `MERGE INTO` semantics, which may create new data files and delete files. The exact behavior depends on engine and write mode. Operationally, you often follow merges with maintenance to compact data and remove old snapshots.

[Table of Contents](#Apache-Iceberg)

## Why does the small files problem happen and how do you mitigate it?
Small files appear when many writers write tiny batches or when streaming jobs checkpoint frequently. Too many files increase planning overhead and reduce scan efficiency. Mitigations include setting target file sizes, batching writes, and running compaction/rewrite jobs to merge files.

[Table of Contents](#Apache-Iceberg)

## What maintenance operations are common for Iceberg tables?
Common maintenance includes:
+ rewriting data files (compaction) to target file sizes
+ rewriting manifests to reduce metadata overhead
+ expiring old snapshots to control metadata growth
+ removing orphan files
These jobs keep query planning and storage cost under control.

[Table of Contents](#Apache-Iceberg)

## What is an Iceberg catalog and what options exist?
A catalog stores table metadata pointers and namespace information. Common options include Hive metastore, REST catalog, and cloud-native catalogs (for example AWS Glue). Catalog choice affects authorization, interoperability, and operational complexity.

[Table of Contents](#Apache-Iceberg)

## How would you migrate an existing dataset to Iceberg?
You typically create an Iceberg table schema and then either:
+ register existing files (where supported) if they conform to the expected layout
+ rewrite data into Iceberg using an engine (Spark/Flink) for safety
After migration, you validate row counts, key constraints, and query performance, then switch readers to the new table.

[Table of Contents](#Apache-Iceberg)

## Iceberg vs Delta vs Hudi: when would you choose Iceberg?
Iceberg is a strong choice when you need an open, engine-agnostic table format with robust metadata, time travel, and evolution features. It fits well in environments with multiple query engines (Spark + Trino + Flink) and a preference for open standards. The best choice still depends on your stack, operational tooling, and update/CDC requirements.

[Table of Contents](#Apache-Iceberg)

