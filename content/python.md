## [Main title](../README.md)
### [Interview questions](full.md)
#
# Python for Data Engineering
+ [Why is Python widely used in data engineering?](#Why-is-Python-widely-used-in-data-engineering)
+ [How do iterators and generators help with large data processing?](#How-do-iterators-and-generators-help-with-large-data-processing)
+ [What is the difference between threads, multiprocessing, and async IO in Python?](#What-is-the-difference-between-threads-multiprocessing-and-async-IO-in-Python)
+ [What is the GIL and why does it matter?](#What-is-the-GIL-and-why-does-it-matter)
+ [How do you read and write Parquet efficiently in Python?](#How-do-you-read-and-write-Parquet-efficiently-in-Python)
+ [How do you process large CSV files without running out of memory?](#How-do-you-process-large-CSV-files-without-running-out-of-memory)
+ [How do you implement retries with exponential backoff?](#How-do-you-implement-retries-with-exponential-backoff)
+ [What logging practices are important for data pipelines?](#What-logging-practices-are-important-for-data-pipelines)
+ [How do you structure a Python project for data pipelines?](#How-do-you-structure-a-Python-project-for-data-pipelines)
+ [How do you manage dependencies and reproducible environments?](#How-do-you-manage-dependencies-and-reproducible-environments)
+ [How do you test data transformations in Python?](#How-do-you-test-data-transformations-in-Python)
+ [How do you profile and optimize slow Python code?](#How-do-you-profile-and-optimize-slow-Python-code)

## Why is Python widely used in data engineering?
Python is popular because it is productive, readable, and has a strong ecosystem for data processing, orchestration, and integration. It is commonly used for glue code, transformations, APIs, and automation, even when the heavy compute runs on distributed engines.

[Table of Contents](#Python-for-Data-Engineering)

## How do iterators and generators help with large data processing?
Iterators and generators allow streaming data instead of loading everything into memory. They enable processing large datasets row-by-row or batch-by-batch. This reduces memory usage and often improves stability of ETL jobs.

[Table of Contents](#Python-for-Data-Engineering)

## What is the difference between threads, multiprocessing, and async IO in Python?
Threads are useful for IO-bound workloads (network, disk) but limited by the GIL for CPU-bound tasks. Multiprocessing runs multiple processes and can use multiple CPU cores for CPU-bound work. Async IO uses an event loop to handle many concurrent IO operations efficiently when tasks spend time waiting.

[Table of Contents](#Python-for-Data-Engineering)

## What is the GIL and why does it matter?
The Global Interpreter Lock (GIL) allows only one thread to execute Python bytecode at a time in CPython. This limits CPU-bound parallelism with threads. Many data engineering tasks are IO-bound, so threads can still help, but CPU-bound tasks often require multiprocessing or native libraries.

[Table of Contents](#Python-for-Data-Engineering)

## How do you read and write Parquet efficiently in Python?
Using `pyarrow` is common because it supports efficient columnar reads, predicate pushdown (engine-dependent), and schema handling. You should select only needed columns, write reasonably sized row groups/files, and avoid creating many tiny files. For large datasets, integrate with a distributed engine rather than pure local processing.

[Table of Contents](#Python-for-Data-Engineering)

## How do you process large CSV files without running out of memory?
You can stream the file in chunks (for example using chunked readers), process line-by-line, or use a library that supports streaming and type inference control. You also avoid loading wide columns you do not need, and you write results incrementally. For very large data, consider Parquet and/or distributed processing.

[Table of Contents](#Python-for-Data-Engineering)

## How do you implement retries with exponential backoff?
Retries should include exponential backoff and jitter to avoid thundering herds. You should only retry on transient errors (timeouts, rate limits) and limit total retry time. Always make operations idempotent or use deduplication to prevent duplicates on retries.

[Table of Contents](#Python-for-Data-Engineering)

## What logging practices are important for data pipelines?
Logs should include pipeline identifiers, run ids, input/output counts, and key timestamps. Structured logging (JSON) helps search and correlation. You should log errors with context and avoid logging sensitive data.

[Table of Contents](#Python-for-Data-Engineering)

## How do you structure a Python project for data pipelines?
A common structure separates reusable library code from job entrypoints. You keep configuration separate, use dependency injection for external services, and standardize logging and error handling. Small CLI entrypoints improve local runs and CI tests.

[Table of Contents](#Python-for-Data-Engineering)

## How do you manage dependencies and reproducible environments?
Use pinned dependencies and a lockfile (or equivalent) and isolate environments (virtualenv/containers). Reproducibility also requires pinning Python versions and building deterministic images. CI should use the same environment definition as production.

[Table of Contents](#Python-for-Data-Engineering)

## How do you test data transformations in Python?
Use small fixture datasets and assert expected outputs (golden tests). Add property tests for invariants (non-negative amounts, uniqueness). Integration tests validate real connectors and schemas, but they should be isolated and stable.

[Table of Contents](#Python-for-Data-Engineering)

## How do you profile and optimize slow Python code?
Profile first to find hotspots (CPU, IO, memory). Common fixes include vectorizing operations, reducing data copies, using efficient data structures, and offloading heavy compute to native libraries or distributed engines. Optimization should be guided by measurable impact.

[Table of Contents](#Python-for-Data-Engineering)

