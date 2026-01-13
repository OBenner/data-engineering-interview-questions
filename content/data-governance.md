## [Main title](../README.md)
### [Interview questions](full.md)
#
# Data Governance
+ [What is data governance and why does it matter?](#What-is-data-governance-and-why-does-it-matter)
+ [What is the difference between governance and security?](#What-is-the-difference-between-governance-and-security)
+ [What are common roles in data governance (owner/steward/custodian)?](#What-are-common-roles-in-data-governance-(owner/steward/custodian))
+ [What is a data catalog and what should it contain?](#What-is-a-data-catalog-and-what-should-it-contain)
+ [What is business glossary vs technical metadata?](#What-is-business-glossary-vs-technical-metadata)
+ [RBAC vs ABAC: what is the difference?](#RBAC-vs-ABAC:-what-is-the-difference)
+ [What is row-level and column-level security?](#What-is-row-level-and-column-level-security)
+ [How do you handle PII/PHI data in analytics platforms?](#How-do-you-handle-PII/PHI-data-in-analytics-platforms)
+ [What is data masking and tokenization?](#What-is-data-masking-and-tokenization)
+ [How do you implement auditability for data access?](#How-do-you-implement-auditability-for-data-access)
+ [How do you handle GDPR “right to be forgotten” in a lakehouse/warehouse?](#How-do-you-handle-GDPR-“right-to-be-forgotten”-in-a-lakehouse/warehouse)
+ [What are data retention policies and how do you enforce them?](#What-are-data-retention-policies-and-how-do-you-enforce-them)

## What is data governance and why does it matter?
Data governance is the set of processes, policies, and responsibilities that ensure data is discoverable, trusted, secure, and used correctly. It matters because data platforms scale to many teams; without governance, definitions diverge, access becomes risky, and compliance issues appear. Good governance enables faster, safer self-service analytics.

[Table of Contents](#Data-Governance)

## What is the difference between governance and security?
Security focuses on preventing unauthorized access and ensuring confidentiality/integrity (access controls, encryption). Governance includes security but also covers ownership, definitions, quality, lifecycle, and change management. Governance answers “who owns this data and what does it mean”, not just “who can access it”.

[Table of Contents](#Data-Governance)

## What are common roles in data governance (owner/steward/custodian)?
Common roles are:
+ data owner: accountable for the dataset and its business definition
+ data steward: maintains quality, metadata, and processes
+ data custodian: operates the technical platform (storage, access, backups)
Clear roles prevent “nobody owns it” incidents.

[Table of Contents](#Data-Governance)

## What is a data catalog and what should it contain?
A data catalog is an inventory of datasets with searchable metadata. It typically contains dataset descriptions, owners, lineage, classifications, freshness/SLA, schema, and links to dashboards. A good catalog reduces time to discovery and improves trust and reuse.

[Table of Contents](#Data-Governance)

## What is business glossary vs technical metadata?
A business glossary defines business terms (for example “active user”, “net revenue”) and their approved definitions. Technical metadata describes datasets and fields (schemas, types, partitions, lineage). Both are needed: glossary aligns meaning, technical metadata enables implementation and discovery.

[Table of Contents](#Data-Governance)

## RBAC vs ABAC: what is the difference?
RBAC (Role-Based Access Control) grants permissions to roles (analyst, engineer) and assigns users to roles. ABAC (Attribute-Based Access Control) uses attributes (department, region, sensitivity) to evaluate policies dynamically. ABAC is more flexible but can be harder to manage without good tooling.

[Table of Contents](#Data-Governance)

## What is row-level and column-level security?
Row-level security restricts which rows a user can see (for example only their region). Column-level security restricts which columns are visible (for example hide salary or PII). These controls are important for multi-tenant analytics and compliance.

[Table of Contents](#Data-Governance)

## How do you handle PII/PHI data in analytics platforms?
You classify sensitive fields, minimize exposure, and enforce least privilege. Common controls include encryption, masking/tokenization, column-level access, and auditing. You also ensure downstream marts only include necessary fields and implement secure sharing patterns.

[Table of Contents](#Data-Governance)

## What is data masking and tokenization?
Masking hides sensitive values (for example showing only last 4 digits) while keeping the dataset usable. Tokenization replaces sensitive values with tokens that can be detokenized only with access to a secure mapping. Tokenization is useful when analytics needs stable identifiers without exposing raw PII.

[Table of Contents](#Data-Governance)

## How do you implement auditability for data access?
You log access events (who queried what, when, from where) and retain logs per policy. You also track permission changes and administrative actions. Audit logs should be queryable for investigations and compliance reporting.

[Table of Contents](#Data-Governance)

## How do you handle GDPR “right to be forgotten” in a lakehouse/warehouse?
You need a process to delete or anonymize personal data across raw, derived, and serving layers. This can involve targeted deletes (where supported), reprocessing from raw logs without the user, or storing personal data separately to allow deletion without rewriting large datasets. You also document what is feasible given retention and legal constraints.

[Table of Contents](#Data-Governance)

## What are data retention policies and how do you enforce them?
Retention policies define how long data is kept and when it must be deleted or archived. Enforcement can be implemented with partition expiry jobs, lifecycle rules on object storage, snapshot expiration, and access reviews. Retention must align with legal requirements and business needs.

[Table of Contents](#Data-Governance)

