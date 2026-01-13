## [Main title](../README.md)
### [Interview questions](full.md)
#
# Data Modeling
+ [What is data modeling in analytics and why does it matter?](#What-is-data-modeling-in-analytics-and-why-does-it-matter)
+ [What is grain and why is it the first question to answer?](#What-is-grain-and-why-is-it-the-first-question-to-answer)
+ [What is the difference between fact and dimension tables?](#What-is-the-difference-between-fact-and-dimension-tables)
+ [What is a star schema and what are its benefits?](#What-is-a-star-schema-and-what-are-its-benefits)
+ [Star schema vs snowflake schema: what are the trade-offs?](#Star-schema-vs-snowflake-schema:-what-are-the-trade-offs)
+ [What are the main types of fact tables?](#What-are-the-main-types-of-fact-tables)
+ [What is a surrogate key and when should you use it?](#What-is-a-surrogate-key-and-when-should-you-use-it)
+ [What is a conformed dimension?](#What-is-a-conformed-dimension)
+ [What is SCD (Slowly Changing Dimension)?](#What-is-SCD-(Slowly-Changing-Dimension))
+ [How do you implement SCD Type 2?](#How-do-you-implement-SCD-Type-2)
+ [What is a factless fact table?](#What-is-a-factless-fact-table)
+ [What is a bridge table and when do you need it?](#What-is-a-bridge-table-and-when-do-you-need-it)
+ [What are degenerate dimensions?](#What-are-degenerate-dimensions)
+ [How do you prevent double counting in analytical models?](#How-do-you-prevent-double-counting-in-analytical-models)
+ [How do you validate a data model after changes?](#How-do-you-validate-a-data-model-after-changes)

## What is data modeling in analytics and why does it matter?
Data modeling in analytics is the process of structuring data so it can be queried reliably and efficiently for business questions. A good model makes metrics consistent, reduces complexity for consumers, and improves performance by aligning storage with query patterns. A bad model leads to inconsistent KPIs, confusing joins, and expensive queries.

[Table of Contents](#Data-Modeling)

## What is grain and why is it the first question to answer?
Grain is the level of detail of a table, for example “one row per order line” or “one row per user per day”. It determines which metrics are additive, how joins behave, and what can be uniquely identified. If grain is unclear, you will get duplicates, incorrect aggregations, and ambiguous keys.

[Table of Contents](#Data-Modeling)

## What is the difference between fact and dimension tables?
Facts store measurable events (orders, payments, clicks) and typically contain foreign keys to dimensions. Dimensions store descriptive attributes (user, product, date) that provide context for slicing and filtering. Facts answer “what happened”, dimensions answer “who/what/where/when”.

[Table of Contents](#Data-Modeling)

## What is a star schema and what are its benefits?
A star schema has a central fact table connected to multiple dimension tables. Benefits include simpler queries, clear join paths, and good performance because joins are typically fact-to-dimension (many-to-one). It also encourages consistent definitions of metrics and attributes.

[Table of Contents](#Data-Modeling)

## Star schema vs snowflake schema: what are the trade-offs?
Snowflake schema normalizes dimensions into multiple related tables. It can reduce redundancy and improve dimension maintainability, but it increases join complexity and can hurt performance. Star schemas are usually preferred for BI and ad-hoc analytics because they are easier for users and tools.

[Table of Contents](#Data-Modeling)

## What are the main types of fact tables?
Common types are:
+ transactional: one row per business event (order, payment)
+ periodic snapshot: one row per entity per period (daily account balance)
+ accumulating snapshot: one row that is updated as a process progresses (order lifecycle)
Choosing the right type depends on the questions you need to answer.

[Table of Contents](#Data-Modeling)

## What is a surrogate key and when should you use it?
A surrogate key is a synthetic identifier used instead of a natural key. It is useful when natural keys are not stable, when you need SCD history, or when integrating multiple sources with different key systems. Surrogate keys also allow consistent joins even if source keys change.

[Table of Contents](#Data-Modeling)

## What is a conformed dimension?
A conformed dimension is a dimension shared consistently across multiple fact tables or data marts. For example, the same “customer” dimension used for orders and support tickets. Conformed dimensions enable consistent reporting and cross-domain analysis.

[Table of Contents](#Data-Modeling)

## What is SCD (Slowly Changing Dimension)?
SCD describes how you handle changes in dimension attributes over time (for example a user changing address). Type 1 overwrites history, Type 2 tracks history with multiple rows and effective dates, and Type 3 keeps limited history in additional columns. The choice depends on whether “as-of” reporting is required.

[Table of Contents](#Data-Modeling)

## How do you implement SCD Type 2?
SCD2 typically stores:
+ a surrogate key
+ the natural/business key
+ effective_start and effective_end timestamps (or end_date)
+ a current_flag
On change, you “close” the previous record and insert a new version. You must define how to detect changes and handle late arriving updates.

[Table of Contents](#Data-Modeling)

## What is a factless fact table?
A factless fact table records events that do not have numeric measures, for example “student attended class” or “user is eligible for campaign”. The fact itself can be counted, and the table is useful for coverage, eligibility, and relationship tracking.

[Table of Contents](#Data-Modeling)

## What is a bridge table and when do you need it?
A bridge table resolves many-to-many relationships, for example products belonging to multiple categories or users having multiple roles. It can also store weights for allocation (for example revenue split). Without a bridge table, joins can explode row counts and break aggregations.

[Table of Contents](#Data-Modeling)

## What are degenerate dimensions?
Degenerate dimensions are identifiers stored in the fact table without a separate dimension table, such as order_id or invoice_number. They are useful for drill-through and filtering while avoiding unnecessary dimension tables.

[Table of Contents](#Data-Modeling)

## How do you prevent double counting in analytical models?
You prevent double counting by enforcing correct grain, using proper join keys (many-to-one), and avoiding many-to-many joins without a bridge table. You also define metric rules (sum vs distinct count vs last value) and test them with reconciliation queries.

[Table of Contents](#Data-Modeling)

## How do you validate a data model after changes?
Typical validation includes:
+ row count and key uniqueness checks at each layer
+ reconciliation of totals against source systems
+ sampling and drill-through checks on known entities
+ regression tests for key business metrics
This catches subtle issues like join duplication or missing late data.

[Table of Contents](#Data-Modeling)

