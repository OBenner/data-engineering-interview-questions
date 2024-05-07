## [Main title](../README.md)
### [Interview questions](full.md)

# MongoDB
## Table of Contents

+ [What is MongoDB?](#What-is-MongoDB)
+ [Why use MongoDB?](#Why-use-MongoDB)
+ [What are the Advantages of MongoDB?](#What-are-the-Advantages-of-MongoDB)
+ [When Should You Use MongoDB?](#When-Should-You-Use-MongoDB)
+ [How does MongoDB exactly store the data?](#How-does-MongoDB-exactly-stores-the-data)
+ [MongoDB vs. RDBMS: What are the differences?](#MongoDB-vs-RDBMS-What-are-the-differences)
+ [How does MongoDB scale?](#How-does-mongodb-scale)
+ [How does MongoDB scale horizontally?](#How-does-mongodb-scale-horizontally)
+ [What are the advantages of sharding?](#What-are-the-advantages-of-sharding)
+ [What methods can we use for sharding in MongoDB?](#What-methods-can-we-use-for-sharding-in-mongodb)
+ [How does atomicity and transaction work in MongoDB?](#How-does-atomicity-and-transaction-word-in-mongodb)
+ [What is an Aggregation Pipeline in MongoDB?](#What-is-an-Aggregation-Pipeline-in-mongodb)
+ [Where should I use an index in MongoDB?](#Where-should-I-use-an-index-in-mongodb)
+ [How would you choose an indexing strategy in MongoDB and what are some common considerations we need to care about?](#How-would-you-choose-a-indexing-strategy-in-mongo-and-what-are-some-common-considerations-we-need-to-care-about)



## What is MongoDB?
MongoDB is a document database built on a horizontal scale-out architecture that uses a flexible schema for storing data. Founded in 2007, MongoDB has a worldwide following in the developer community.

[Table of Contents](#mongo)

## Why use MongoDB?
As a document database, MongoDB makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents. This format directly maps to native objects in most modern programming languages, making it a natural choice for developers, as they don’t need to think about normalizing data. MongoDB can also handle high volume and can scale both vertically or horizontally to accommodate large data loads.

[Table of Contents](#mongo)

## What are the Advantages of MongoDB?
- A Powerful Document-Oriented Database
- Developer User Experience
- Scalability and Transactionality
- Platform and Ecosystem Maturity

[Table of Contents](#mongo)

## When Should You Use MongoDB?
- Integrating large amounts of diverse data
- Describing complex data structures that evolve
- Delivering data in high-performance applications
- Supporting hybrid and multi-cloud applications
- Supporting agile development and collaboration

[Table of Contents](#mongo)

## How does MongoDB exactly stores the data?

In MongoDB, records are stored as documents in compressed [BSON]([url](https://www.mongodb.com/json-and-bson)) files. The documents can be retrieved directly in JSON format, which has many benefits:

- It is a natural form to store data.
- It is human-readable.
- Structured and unstructured information can be stored in the same document.
- You can nest JSON to store complex data objects.
- JSON has a flexible and dynamic schema, so adding fields or leaving a field out is not a problem.
- Documents map to objects in most popular programming languages.

Most developers find it easy to work with JSON because it is a simple and powerful way to describe and store data. 

[Table of Contents](#mongo)


## MongoDB vs. RDBMS: What are the differences?

One of the main differences between MongoDB and RDBMS is that RDBMS is a relational database while MongoDB is nonrelational. Likewise, while most RDBMS systems use SQL to manage stored data, MongoDB uses BSON for data storage.

While RDBMS uses tables and rows, MongoDB uses documents and collections. In RDBMS a table -- the equivalent to a MongoDB collection -- stores data as columns and rows. Likewise, a row in RDBMS is the equivalent of a MongoDB document but stores data as structured data items in a table. A column denotes sets of data values, which is the equivalent to a field in MongoDB.

[Table of Contents](#mongo)



## How does mongodb scale?

mongo scales the same way as any distributed application would scale, throw more resources at it(`Vertical Scaling`) or distribute the data on multiple physical servers or nodes (`Horizontal Scaling` ) .

or in other words: 

*Vertical Scaling* involves increasing the capacity of a single server, such as using a more powerful CPU, adding more RAM, or increasing the amount of storage space.

*Horizontal Scaling* involves dividing the system dataset and load over multiple servers, adding additional servers to increase capacity as required.

While the overall speed or capacity of a single machine may not be high, each machine handles a subset of the overall workload, potentially providing better efficiency than a single high-speed high-capacity server.

[Table of Contents](#mongo)

## How does mongodb scale horizontally?

MongoDB supports *horizontal scaling* through [sharding.](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-sharding)

Sharding is a method for distributing data across multiple machines. MongoDB uses sharding to support deployments with very large data sets and high throughput operations.

A MongoDB [sharded cluster](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-sharded-cluster) consists of the following components:

- [shard](https://www.mongodb.com/docs/manual/core/sharded-cluster-shards/#std-label-shards-concepts): Each shard contains a subset of the sharded data. Each shard must be deployed as a [replica set.](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-replica-set)
- [mongos](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/): The `mongos` acts as a query router, providing an interface between client applications and the sharded cluster. [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos) can support [hedged reads](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-mongos-hedged-reads) to minimize latencies.
- [config servers](https://www.mongodb.com/docs/manual/core/sharded-cluster-config-servers/#std-label-sharding-config-server): Config servers store metadata and configuration settings for the cluster. As of MongoDB 3.4, config servers must be deployed as a replica set (CSRS).

The following graphic describes the interaction of components within a sharded cluster:

![Diagram of a sample sharded cluster for production purposes.  Contains exactly 3 config servers, 2 or more ``mongos`` query routers, and at least 2 shards. The shards are replica sets.](https://www.mongodb.com/docs/manual/images/sharded-cluster-production-architecture.bakedsvg.svg)

MongoDB shards data at the [collection](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-collection) level, distributing the collection data across the shards in the cluster.	

[Table of Contents](#mongo)



## What are the advantages of sharding?

##### Reads / Writes[![img](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/sharding/#reads---writes)

MongoDB distributes the read and write workload across the [shards](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard) in the [sharded cluster](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-sharded-cluster), allowing each shard to process a subset of cluster operations. Both read and write workloads can be scaled horizontally across the cluster by adding more shards.

For queries that include the shard key or the prefix of a [compound](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-compound-index) shard key, [`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos) can target the query at a specific shard or set of shards. These [targeted operations](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-sharding-mongos-targeted) are generally more efficient than [broadcasting](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-sharding-mongos-broadcast) to every shard in the cluster.

[`mongos`](https://www.mongodb.com/docs/manual/reference/program/mongos/#mongodb-binary-bin.mongos) can support [hedged reads](https://www.mongodb.com/docs/manual/core/sharded-cluster-query-router/#std-label-mongos-hedged-reads) to minimize latencies.

##### Storage Capacity[![img](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/sharding/#storage-capacity)

[Sharding](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-sharding) distributes data across the [shards](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-shard) in the cluster, allowing each shard to contain a subset of the total cluster data. As the data set grows, additional shards increase the storage capacity of the cluster.



##### High Availability[![img](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/sharding/#high-availability)

The deployment of config servers and shards as replica sets provide increased availability.

Even if one or more shard replica sets become completely unavailable, the sharded cluster can continue to perform partial reads and writes. That is, while data on the unavailable shard(s) cannot be accessed, reads or writes directed at the available shards can still succeed.

## What methods can we use for sharding in mongodb?

MongoDB supports two sharding strategies for distributing data across [sharded clusters.](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-sharded-cluster)

##### Hashed Sharding[![img](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/sharding/#hashed-sharding)

Hashed Sharding involves computing a hash of the shard key field's value. Each [chunk](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-chunk) is then assigned a range based on the hashed shard key values.

##### Ranged Sharding[![img](https://www.mongodb.com/docs/manual/assets/link.svg)](https://www.mongodb.com/docs/manual/sharding/#ranged-sharding)

Ranged sharding involves dividing data into ranges based on the shard key values. Each [chunk](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-chunk) is then assigned a range based on the shard key values.

[Table of Contents](#mongo)

## How does atomicity and transaction word in mongodb?

In MongoDB, a write operation is [atomic](https://www.mongodb.com/docs/manual/reference/glossary/#std-term-atomic-operation) on the level of a single document, even if the operation modifies multiple embedded documents *within* a single document.

When a single write operation (e.g. [`db.collection.updateMany()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/#mongodb-method-db.collection.updateMany)) modifies multiple documents, the modification of each document is atomic, but the operation as a whole is not atomic.

For situations that require atomicity of reads and writes to multiple documents (in a single or multiple collections), MongoDB supports distributed transactions, including transactions on replica sets and sharded clusters.

[Table of Contents](#mongo)



## What is an Aggregation Pipeline in mongodb?

An aggregation pipeline consists of one or more [stages](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/#std-label-aggregation-pipeline-operator-reference) that process documents:

- Each stage performs an operation on the input documents. For example, a stage can filter documents, group documents, and calculate values.
- The documents that are output from a stage are passed to the next stage.
- An aggregation pipeline can return results for groups of documents. For example, return the total, average, maximum, and minimum values.

[Table of Contents](#mongo)

## Where should I use an index in mongodb? 

If your application is repeatedly running queries on the same fields, you can create an index on those fields to improve performance.

Although indexes improve query performance, adding an index has negative performance impact for write operations. For collections with a high write-to-read ratio, indexes are expensive because each insert must also update any indexes.

[Table of Contents](#mongo)

## How would you choose a indexing strategy in mongo and what are some common considerations we need to care about?

The best indexes for your application must take a number of factors into account, including the kinds of queries you expect, the ratio of reads to writes, and the amount of free memory on your system. 

The best overall strategy for designing indexes is to profile a variety of index configurations with data sets similar to the ones you'll be running in production to see which configurations perform best. Inspect the current indexes created for your collections to ensure they are supporting your current and planned queries. If an index is no longer used, drop the index.

These are some considerations you need to take for your indexing strategy:

- [Use the ESR (Equality, Sort, Range) Rule](https://www.mongodb.com/docs/manual/tutorial/equality-sort-range-rule/#std-label-esr-indexing-rule)

  The ESR (Equality, Sort, Range) Rule is a guide to creating indexes that support your queries efficiently.

- [Create Indexes to Support Your Queries](https://www.mongodb.com/docs/manual/tutorial/create-indexes-to-support-queries/#std-label-create-indexes-to-support-queries)

  An index supports a query when the index contains all the fields scanned by the query. Creating indexes that support queries results in greatly increased query performance.

- [Use Indexes to Sort Query Results](https://www.mongodb.com/docs/manual/tutorial/sort-results-with-indexes/#std-label-sorting-with-indexes)

  To support efficient queries, use the strategies here when you specify the sequential order and sort order of index fields.

- [Ensure Indexes Fit in RAM](https://www.mongodb.com/docs/manual/tutorial/ensure-indexes-fit-ram/#std-label-indexes-ensure-indexes-fit-ram)

  When your index fits in RAM, the system can avoid reading the index from disk and you get the fastest processing.

- [Create Indexes to Ensure Query Selectivity](https://www.mongodb.com/docs/manual/tutorial/create-queries-that-ensure-selectivity/#std-label-index-selectivity)

  Selectivity is the ability of a query to narrow results using the index. Selectivity allows MongoDB to use the index for a larger portion of the work associated with fulfilling the query.

[Table of Contents](#mongo)