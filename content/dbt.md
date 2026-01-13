## [Main title](../README.md)
### [Interview questions](full.md)
#
# dbt
+ [What is dbt?](#What-is-dbt)
+ [How is dbt different from Airflow?](#How-is-dbt-different-from-Airflow)
+ [What is a dbt model?](#What-is-a-dbt-model)
+ [What does ref() do and why is it important?](#What-does-ref()-do-and-why-is-it-important)
+ [What are typical layers in a dbt project (staging/intermediate/marts)?](#What-are-typical-layers-in-a-dbt-project-(staging/intermediate/marts))
+ [What is a materialization in dbt?](#What-is-a-materialization-in-dbt)
+ [When would you use view vs table materializations?](#When-would-you-use-view-vs-table-materializations)
+ [What is an incremental model and what problems does it solve?](#What-is-an-incremental-model-and-what-problems-does-it-solve)
+ [How do you design a reliable unique_key for incremental models?](#How-do-you-design-a-reliable-unique_key-for-incremental-models)
+ [What are dbt tests and what types exist?](#What-are-dbt-tests-and-what-types-exist)
+ [What are sources in dbt and how do you test them?](#What-are-sources-in-dbt-and-how-do-you-test-them)
+ [What are snapshots in dbt and when would you use them?](#What-are-snapshots-in-dbt-and-when-would-you-use-them)
+ [What are macros in dbt and when should you use them?](#What-are-macros-in-dbt-and-when-should-you-use-them)
+ [What is dbt state selection (slim CI) and why is it useful?](#What-is-dbt-state-selection-(slim-CI)-and-why-is-it-useful)
+ [How do you approach CI/CD for dbt projects?](#How-do-you-approach-CI/CD-for-dbt-projects)

## What is dbt?
dbt (data build tool) is a transformation framework where you write transformations as SQL (and Jinja-templated SQL), and dbt builds a DAG of models and runs them in the right order. It is commonly used to transform raw data into cleaned, documented, tested analytics tables in a warehouse/lakehouse.

[Table of Contents](#dbt)

## How is dbt different from Airflow?
Airflow is an orchestration system that schedules and coordinates tasks of any kind. dbt focuses specifically on SQL-based transformations and their dependency graph, plus testing and documentation. In practice, Airflow often runs dbt as one step of a larger pipeline (ingestion → transform → publish).

[Table of Contents](#dbt)

## What is a dbt model?
A dbt model is a select query stored as a `.sql` file in the `models/` directory. dbt materializes the model into a relation in your warehouse (view/table/incremental) and manages dependencies between models.

[Table of Contents](#dbt)

## What does ref() do and why is it important?
`ref('model_name')` declares a dependency on another dbt model. dbt uses it to build the DAG, order execution, and resolve the correct schema/database per environment. It also enables features like automated lineage in dbt docs.

[Table of Contents](#dbt)

## What are typical layers in a dbt project (staging/intermediate/marts)?
A common pattern is:
+ staging: light cleaning and renaming, close to sources
+ intermediate: reusable transformations and joins
+ marts: business-facing fact/dimension tables and metrics-ready datasets
This makes models easier to test, reuse, and maintain.

[Table of Contents](#dbt)

## What is a materialization in dbt?
A materialization defines how dbt builds a model in the warehouse (for example as a view, table, or incremental table). It controls the build strategy and how changes are applied over time.

[Table of Contents](#dbt)

## When would you use view vs table materializations?
Views are useful for fast iteration and when compute cost per query is acceptable. Tables are useful when queries are expensive or many downstream queries reuse the same result. The trade-off is storage cost and the need to keep tables updated.

[Table of Contents](#dbt)

## What is an incremental model and what problems does it solve?
An incremental model only processes new or changed data instead of rebuilding the entire table each run. It reduces runtime and cost for large datasets. It requires correct keys and logic to avoid duplicates and missed updates.

[Table of Contents](#dbt)

## How do you design a reliable unique_key for incremental models?
The `unique_key` should uniquely identify a record in the target table, usually a stable business key or a surrogate key derived from stable columns. If the source can update records, you also need a deterministic “latest record” rule (for example using an `updated_at` column) so merges are correct.

[Table of Contents](#dbt)

## What are dbt tests and what types exist?
dbt supports:
+ generic tests (built-in or custom): `unique`, `not_null`, `accepted_values`, `relationships`
+ singular tests: custom SQL queries that should return zero failing rows
Tests run as queries in the warehouse and fail the run if assertions are violated.

[Table of Contents](#dbt)

## What are sources in dbt and how do you test them?
Sources declare upstream tables and their metadata in `sources.yml`. You can test sources with freshness checks and column-level tests (like `not_null`) to detect broken ingestion or schema drift early.

[Table of Contents](#dbt)

## What are snapshots in dbt and when would you use them?
Snapshots capture slowly changing dimension history by tracking changes in source records over time. They are useful when you need point-in-time analysis or to implement SCD2-style history from mutable source tables.

[Table of Contents](#dbt)

## What are macros in dbt and when should you use them?
Macros are Jinja functions that generate SQL. Use them to avoid repetition (standardized column selection, reusable filters, dynamic SQL) and to keep business logic consistent across models. Overusing macros for complex logic can hurt readability and debugging.

[Table of Contents](#dbt)

## What is dbt state selection (slim CI) and why is it useful?
State selection runs only models that changed (and their dependents) compared to a previous artifact state. In CI, this reduces runtime by avoiding full rebuilds, while still validating that changes compile, run, and pass tests for affected parts of the DAG.

[Table of Contents](#dbt)

## How do you approach CI/CD for dbt projects?
A common approach is:
+ in CI: `dbt deps`, `dbt compile`, run selected models/tests (state-based or tags)
+ in CD: deploy artifacts and run scheduled jobs in production
You usually also enforce code review, documentation, and data tests for critical marts.

[Table of Contents](#dbt)

