[Interview questions](full.md)
# Apache Cassandra
+ [Explain what is Cassandra?](#Explain-what-is-Cassandra)
+ [List the benefits of using Cassandra?](#List-the-benefits-of-using-Cassandra)
+ [What is the use of Cassandra and why to use Cassandra?](#What-is-the-use-of-Cassandra-and-why-to-use-Cassandra)
+ [Explain the concept of tunable consistency in Cassandra?](#Explain-the-concept-of-tunable-consistency-in-Cassandra)
+ [Explain what is composite type in Cassandra?](#Explain-what-is-composite-type-in-Cassandra)
+ [How does Cassandra write?](#How-does-Cassandra-write)
+ [How Cassandra stores data?](#How-Cassandra-stores-data)
+ [Define the management tools in Cassandra?](#Define-the-management-tools-in-Cassandra)
+ [Mention what are the main components of Cassandra data model?](#Mention-what-are-the-main-components-of-Cassandra-data-model)
+ [Define Memtable?](#Define-Memtable?)
+ [Explain what is a Column Family in Cassandra?](#Explain-what-is-a-Column-Family-in-Cassandra)
+ [What is SStable and how is it different from other relational tables?](#What-is-SStable-and-how-is-it-different-from-other-relational-tables)
+ [Explain what is a Cluster in Cassandra?](#Explain-what-is-a-Cluster-in-Cassandra)
+ [Explain the concept of Bloom Filter?](#Explain-the-concept-of-Bloom-Filter)
+ [List out the other components of Cassandra?](#List-out-the-other-components-of-Cassandra)
+ [Explain Cap Theorem?](#Explain-Cap-Theorem)
+ [Explain what is a Keyspace in Cassandra?](#Explain-what-is-a-Keyspace-in-Cassandra)
+ [State the differences between  Node and Cluster And DataCenter in Cassandra?](#State-the-differences-between-Node-and-Cluster-And-DataCenter-in-Cassandra)
+ [Mention what are the values stored in the Cassandra Column?](#Mention-what-are-the-values-stored-in-the-Cassandra-Column)
+ [How to write a Query in Cassandra?](#How-to-write-a-Query-in-Cassandra)
+ [Mention when you can use Alter Keyspace?](#Mention-when-you-can-use-Alter-Keyspace)
+ [What os Cassandra supports?](#What-os-Cassandra-supports)
+ [Explain what is Cassandra cqlsh?](#Explain-what-is-Cassandra-cqlsh)
+ [What is Cassandra Data Model?](#What-is-Cassandra-Data-Model)
+ [Mention what does the Shell Commands capture And consistency determines?](#Mention-what-does-the-Shell-Commands-capture-And-consistency-determines)
+ [What is Cql?](#What-is-Cql)
+ [What is mandatory while creating a table in Cassandra?](#What-is-mandatory-while-creating-a-table-in-Cassandra)
+ [Explain the concept of compaction in Cassandra?](#Explain-the-concept-of-compaction-in-Cassandra)
+ [Mention what needs to be taken care while adding a Column?](#Mention-what-needs-to-be-taken-care-while-adding-a-Column)
+ [Does Cassandra support ACID transactions?](#Does-Cassandra-support-ACID-transactions)
+ [Explain how Cassandra writes data?](#Explain-how-Cassandra-writes-data)
+ [What is SuperColumn in Cassandra?](#What-is-SuperColumn-in-Cassandra)
+ [Explain what is Memtable in Cassandra?](#Explain-what-is-Memtable-in-Cassandra)
+ [Define the Consistency Levels for Read Operations in Cassandra?](#Define-the-Consistency-Levels-for-Read-Operations-in-Cassandra)
+ [Explain how Cassandra writes changed data into Commitlog?](#Explain-how-Cassandra-writes-changed-data-into-Commitlog)
+ [What is difference between Column and Super Column?](#What-is-difference-between-Column-and-Super-Column)
+ [What is ColumnFamily?](#What-is-ColumnFamily)
+ [Explain how Cassandra delete data?](#Explain-how-Cassandra-delete-data)
+ [Define the use of Source Command in Cassandra?](#Define-the-use-of-Source-Command-in-Cassandra)
+ [What is Thrift?](#What-is-Thrift)
+ [Explain Tombstone in Cassandra?](#Explain-Tombstone-in-Cassandra)
+ [What Platforms Cassandra runs on?](#What-Platforms-Cassandra-runs-on)
+ [Name the ports Cassandra uses?](#Name-the-ports-Cassandra-uses)
+ [Can you Add Or Remove column families in a working cluster?](#Can-you-Add-Or-Remove-column-families-in-a-working-cluster)
+ [What is Replication Factor in Cassandra?](#What-is-Replication-Factor-in-Cassandra)
+ [Can we change Replication Factor on a Live Cluster?](#Can-we-change-Replication-Factor-on-a-Live-Cluster)
+ [How to Iterate all rows in ColumnFamily?](#How-to-Iterate-all-rows-in-ColumnFamily)
+ [Explain Cassandra.](#Explain-Cassandra)
+ [In which language Cassandra is written?](#In-which-language-Cassandra-is-written)
+ [Which query language is used in Cassandra database?](#Which-query-language-is-used-in-Cassandra-database)
+ [What are the benefits and advantages of Cassandra?](#What-are-the-benefits-and-advantages-of-Cassandra)
+ [Where Cassandra stores its data?](#Where-Cassandra-stores-its-data)
+ [What was the design goal of Cassandra?](#What-was-the-design-goal-of-Cassandra)
+ [How many types of NoSQL databases and give some examples.](#How-many-types-of-NoSQL-databases-and-give-some-examples)
+ [What is keyspace in Cassandra?](#What-is-keyspace-in-Cassandra)
+ [What are the different composite keys in Cassandra?](#What-are-the-different-composite-keys-in-Cassandra)
+ [What is data replication in Cassandra?](#What-is-data-replication-in-Cassandra)
+ [What is node in Cassandra?](#What-is-node-in-Cassandra)
+ [What do you mean by data center in Cassandra?](#What-do-you-mean-by-data-center-in-Cassandra)
+ [What do you mean by commit log in Cassandra?](#What-do-you-mean-by-commit-log-in-Cassandra)
+ [What do you mean by column family in Cassandra?](#What-do-you-mean-by-column-family-in-Cassandra)
+ [What do you mean by consistency in Cassandra?](#What-do-you-mean-by-consistency-in-Cassandra)
+ [How does Cassandra perform write function?](#How-does-Cassandra-perform-write-function)
+ [What is SSTable?](#What-is-SSTable)
+ [How the SSTable is different from other relational tables?](#How-the-SSTable-is-different-from-other-relational-tables)
+ [What is the role of ALTER KEYSPACE?](#What-is-the-role-of-ALTER-KEYSPACE)
+ [What are the differences between node and cluster and datacenter in Cassandra?](#What-are-the-differences-between-node-and-cluster-and-datacenter-in-Cassandra)
+ [What is the use of Cassandra CQL collection?](#What-is-the-use-of-Cassandra-CQL-collection)
+ [What is the use of Bloom Filter in Cassandra?](#What-is-the-use-of-Bloom-Filter-in-Cassandra)
+ [How does Cassandra delete data?](#How-does-Cassandra-delete-data)
+ [What is SuperColumn in Cassandra?](#What-is-SuperColumn-in-Cassandra)
+ [What are the Hadoop and HBase and Hive and Cassandra?](#What-are-the-Hadoop-and-HBase-and-Hive-and-Cassandra)
+ [What is the usage of void close() method?](#What-is-the-usage-of-void-close-method)
+ [Which command is used to start the cqlsh prompt?](#Which-command-is-used-to-start-the-cqlsh-prompt)
+ [What is the usage of cqlsh-version command?](#What-is-the-usage-of-cqlsh-version-command)
+ [Does Cassandra work on Windows?](#Does-Cassandra-work-on-Windows)
+ [What is Kundera in Cassandra?](#What-is-Kundera-in-Cassandra)
+ [What do you mean by Thrift in Cassandra?](#What-do-you-mean-by-Thrift-in-Cassandra)
+ [What is Hector in Cassandra?](#What-is-Hector-in-Cassandra)

## Explain what is Cassandra?
Cassandra is an open source data storage system developed at Facebook for inbox search and designed for storing and managing large amounts of data across commodity servers. It can server as both Real time data store system for online applications Also as a read intensive database for business intelligence system

[Table of Contents](#Apache-Cassandra)

## List the benefits of using Cassandra?
Unlike traditional or any other database, Apache Cassandra delivers near real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.
Instead of master-slave architecture, Cassandra is established on peer-to-peer architecture ensuring no failure.
It also assures phenomenal flexibility as it allows insertion of multiple nodes to any Cassandra cluster in any datacenter. Further, any client can forward its request to any server.
Cassandra facilitates extensible scalability and can be easily scaled up and scaled down as per the requirements. With a high throughput for read and write operations, this NoSQL application need not be restarted while scaling.
Cassandra is also revered for its strong data replication capability as it allows data storage at multiple locations enabling users to retrieve data from another location if one node fails. Users have the option to set up the number of replicas they want to create.
Shows brilliant performance when used for massive datasets and thus, the most preferable NoSQL DB by most organizations.
Operates on column-oriented structure and thus, quickens and simplifies the process of slicing. Even data access and retrieval becomes more efficient with column-based data model.
Further, Apache Cassandra supports schema-free/schema-optional data model, which un-necessitate the purpose of showing all the columns required by your application.

[Table of Contents](#Apache-Cassandra)

## What is the use of Cassandra and why to use Cassandra?
Cassandra was designed to handle big data workloads across multiple nodes without any single point of failure. The various factors responsible for using Cassandra are
+ It is fault tolerant and consistent
+ Gigabytes to petabytes scalabilities
+ It is a column-oriented database
+ No single point of failure
+ No need for separate caching layer
+ Flexible schema design
+ It has flexible data storage, easy data distribution, and fast writes
+ It supports ACID (Atomicity, Consistency, Isolation, and Durability)properties
+ Multi-data center and cloud capable
+ Data compression

[Table of Contents](#Apache-Cassandra)

## Explain the concept of tunable consistency in Cassandra?
Tunable Consistency is a phenomenal characteristic that makes Cassandra a favored database choice of Developers, Analysts and Big data Architects. Consistency refers to the up-to-date and synchronized data rows on all their replicas. Cassandra’s Tunable Consistency allows users to select the consistency level best suited for their use cases. It supports two consistencies -Eventual and Consistency and Strong Consistency.
The former guarantees consistency when no new updates are made on a given data item, all accesses return the last updated value eventually. Systems with eventual consistency are known to have achieved replica convergence.
For Strong consistency, Cassandra supports the following condition:
R + W > N, where
N – Number of replicas
W – Number of nodes that need to agree for a successful write
R – Number of nodes that need to agree for a successful read

[Table of Contents](#Apache-Cassandra)

## Explain what is composite type in Cassandra?
In Cassandra, composite type allows to defined key or a column name with a concatenation of data of different type. You can use two types of Composite Type
Row Key
Column Name

[Table of Contents](#Apache-Cassandra)

## How does Cassandra write?
Cassandra performs the write function by applying two commits-first it writes to a commit log on disk and then commits to an in-memory structured known as memtable. Once the two commits are successful, the write is achieved. Writes are written in the table structure as SSTable (sorted string table). Cassandra offers speedier write performance.

[Table of Contents](#Apache-Cassandra)

## How Cassandra stores data?
All data stored as bytes
When you specify validator, Cassandra ensures those bytes are encoded as per requirement
Then a comparator orders the column based on the ordering specific to the encoding
While composite are just byte arrays with a specific encoding, for each component it stores a two byte length followed by the byte encoded component followed by a termination bit.

[Table of Contents](#Apache-Cassandra)

## Define the management tools in Cassandra?
DataStaxOpsCenter: internet-based management and monitoring solution for Cassandra cluster and DataStax. It is free to download and includes an additional Edition of OpsCenter
SPM primarily administers Cassandra metrics and various OS and JVM metrics. Besides Cassandra, SPM also monitors Hadoop, Spark, Solr, Storm, zookeeper and other Big Data platforms. The main features of SPM include correlation of events and metrics, distributed transaction tracing, creating real-time graphs with zooming, anomaly detection and heartbeat alerting.

[Table of Contents](#Apache-Cassandra)

## Mention what are the main components of Cassandra data model?
The main components of Cassandra Data Model are
+ Cluster
+ Keyspace
+ Column
+ Column & Family

[Table of Contents](#Apache-Cassandra)

## Define Memtable?
Similar to table, memtable is in-memory/write-back cache space consisting of content in key and column format. The data in memtable is sorted by key, and each ColumnFamily consist of a distinct memtable that retrieves column data via key. It stores the writes until it is full, and then flushed out.

[Table of Contents](#Apache-Cassandra)

## Explain what is a Column Family in Cassandra?
Column family in Cassandra is referred for a collection of Rows.

[Table of Contents](#Apache-Cassandra)

## What is SStable and how is it different from other relational tables?
SSTable expands to ‘Sorted String Table,’ which refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table. Exhibiting immutability, SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

[Table of Contents](#Apache-Cassandra)

## Explain what is a Cluster in Cassandra?
A cluster is a container for keyspaces. Cassandra database is segmented over several machines that operate together. The cluster is the outermost container which arranges the nodes in a ring format and assigns data to them. These nodes have a replica which takes charge in case of data handling failure.

[Table of Contents](#Apache-Cassandra)

## Explain the concept of Bloom Filter?
Associated with SSTable, Bloom filter is an off-heap (off the Java heap to native memory) data structure to check whether there is any data available in the SSTable before performing any I/O disk operation.

[Table of Contents](#Apache-Cassandra)

## List out the other components of Cassandra?
The other components of Cassandra are
+ Node
+ Data Center
+ Cluster
+ Commit log
+ Mem-table
+ SSTable
+ Bloom Filter

[Table of Contents](#Apache-Cassandra)

## Explain Cap Theorem?
With a strong requirement to scale systems when additional resources are needed, CAP Theorem plays a major role in maintaining the scaling strategy. It is an efficient way to handle scaling in distributed systems. Consistency Availability and Partition tolerance (CAP) theorem states that in distributed systems like Cassandra, users can enjoy only two out of these three characteristics.
One of them needs to be sacrificed. Consistency guarantees the return of most recent write for the client, Availability returns a rational response within minimum time and in Partition Tolerance, the system will continue its operations when network partitions occur. The two options available are AP and CP.

[Table of Contents](#Apache-Cassandra)

## Explain what is a Keyspace in Cassandra?
In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster consist of one keyspace per node.

[Table of Contents](#Apache-Cassandra)

## State the differences between Node and Cluster And DataCenter in Cassandra?
While a node is a single machine running Cassandra, cluster is a collection of nodes that have similar type of data grouped together. DataCentersare useful components when serving customers in different geographical areas. You can group different nodes of a cluster into different data centers.

[Table of Contents](#Apache-Cassandra)

## Mention what are the values stored in the Cassandra Column?
In Cassandra Column, basically there are three values
+ Column Name
+ Value
+ Time Stamp

[Table of Contents](#Apache-Cassandra)

## How to write a Query in Cassandra?
Using CQL (Cassandra Query Language).Cqlsh is used for interacting with database.

[Table of Contents](#Apache-Cassandra)

## Mention when you can use Alter Keyspace?
ALTER KEYSPACE can be used to change properties such as the number of replicas and the durable_write of a keyspace.

[Table of Contents](#Apache-Cassandra)

## What os Cassandra supports?
Windows and Linux.

[Table of Contents](#Apache-Cassandra)

## Explain what is Cassandra cqlsh?
Cassandra-Cqlsh is a query language that enables users to communicate with its database. By using Cassandra cqlsh, you can do following things
+ Define a schema
+ Insert a data and
+ Execute a query

[Table of Contents](#Apache-Cassandra)

## What is Cassandra Data Model?
Cassandra Data Model consists of four main components:
+ Cluster: Made up of multiple nodes and keyspaces
+ Keyspace: a namespace to group multiple column families, especially one per partition
+ Column: consists of a column name, value and timestamp
+ ColumnFamily: multiple columns with row key reference.

[Table of Contents](#Apache-Cassandra)

## Mention what does the Shell Commands capture And consistency determines?
There are various Cqlsh shell commands in Cassandra. Command “Capture”, captures the output of a command and adds it to a file while, command “Consistency” display the current consistency level or set a new consistency level.

[Table of Contents](#Apache-Cassandra)

## What is Cql?
CQL is Cassandra Query language to access and query the Apache distributed database. It consists of a CQL parser that incites all the implementation details to the server. The syntax of CQL is similar to SQL but it does not alter the Cassandra data model.

[Table of Contents](#Apache-Cassandra)

## What is mandatory while creating a table in Cassandra?
While creating a table primary key is mandatory, it is made up of one or more columns of a table.

[Table of Contents](#Apache-Cassandra)

## Explain the concept of compaction in Cassandra?
Compaction refers to a maintenance process in Cassandra , in which, the SSTables are reorganized for data optimization of data structure son the disk. The compaction process is useful during interactive with memtable. There are two type sof compaction in Cassandra:
+ Minor compaction: started automatically when a new sstable is created. Here, Cassandra condenses all the equally sized sstables into one.
+ Major compaction : is triggered manually using nodetool. Compacts all sstables of a ColumnFamily into one.

[Table of Contents](#Apache-Cassandra)

## Mention what needs to be taken care while adding a Column?
+ While adding a column you need to take care that the Column name is not conflicting with the existing column names 
+ Table is not defined with compact storage option

[Table of Contents](#Apache-Cassandra)

## Does Cassandra support ACID transactions?
Unlike relational databases, Cassandra does not support ACID transactions.

[Table of Contents](#Apache-Cassandra)

## Explain how Cassandra writes data?
Cassandra writes data in three components
+ Commitlog write
+ Memtable write
+ SStable write

[Table of Contents](#Apache-Cassandra)

## Explain what is Memtable in Cassandra?
Cassandra writes the data to a in memory structure known as Memtable.
It is an in-memory cache with content stored as key/column.
By key Memtable data are sorted.
There is a separate Memtable for each ColumnFamily, and it retrieves column data from the key.

[Table of Contents](#Apache-Cassandra)

## Define the Consistency Levels for Read Operations in Cassandra?
+ ALL: Highly consistent. A write must be written to commitlog and memtable on all replica nodes in the cluster
+ EACH_QUORUM: A write must be written to commitlog and memtable on quorum of replica nodes in all data centers.
+ LOCAL_QUORUM:A write must be written to commitlog and memtable on quorum of replica nodes in the same center.
+ ONE: A write must be written to commitlog and memtableof at least one replica node.
+ TWO, Three: Same as One but at least two and three replica nodes, respectively
+ LOCAL_ONE: A write must be written for at least one replica node in the local data center ANY
+ SERIAL: Linearizable Consistency to prevent unconditional updates
+ LOCAL_SERIAL: Same as Serial but restricted to local data center

[Table of Contents](#Apache-Cassandra)

## Explain how Cassandra writes changed data into Commitlog?
Cassandra concatenate changed data to commitlog
Commitlog acts as a crash recovery log for data
Until the changed data is concatenated to commitlog write operation will be never considered successful
Data will not be lost once commitlog is flushed out to file.

[Table of Contents](#Apache-Cassandra)

## What is difference between Column and Super Column?
Both elements work on the principle of tuple having name and value. However, the former‘s value is a string while the value in latter is a Map of Columns with different data types.
Unlike Columns, Super Columns do not contain the third component of timestamp.

[Table of Contents](#Apache-Cassandra)

## What is ColumnFamily?
As the name suggests, ColumnFamily refers to a structure having infinite number of rows. That are referred by a key-value pair, where key is the name of the column and value represents the column data. It is much similar to a hashmap in java or dictionary in Python. Rememeber, the rows are not limited to a predefined list of Columns here. Also, the ColumnFamily is absolutely flexible with one row having 100 Columns while the other only 2 columns.

[Table of Contents](#Apache-Cassandra)

## Explain how Cassandra delete data?
SSTables are immutable and cannot remove a row from SSTables. When a row needs to be deleted, Cassandra assigns the column value with a special value called Tombstone. When the data is read, the Tombstone value is considered as deleted.

[Table of Contents](#Apache-Cassandra)

## Define the use of Source Command in Cassandra?
Source command is used to execute a file consisting of CQL statements.

[Table of Contents](#Apache-Cassandra)

## What is Thrift?
Thrift is a legacy RPC protocol or API unified with a code generation tool for CQL. The purpose of using Thrift in Cassandra is to facilitate access to the DB across the programming language.

[Table of Contents](#Apache-Cassandra)

## Explain Tombstone in Cassandra?
Tombstone is row marker indicating a column deletion. These marked columns are deleted during compaction. Tombstones are of great significance as Cassnadra supports eventual consistency, where the data must respond before any successful operation.

[Table of Contents](#Apache-Cassandra)

## What Platforms Cassandra runs on?
Since Cassandra is a Java application, it can successfully run on any Java-driven platform or Java Runtime Environment (JRE) or Java Virtual Machine (JVM). Cassandra also runs on RedHat, CentOS, Debian and Ubuntu Linux platforms.

[Table of Contents](#Apache-Cassandra)

## Name the ports Cassandra uses?
The default settings state that Cassandra uses 7000 ports for Cluster Management, 9160 for Thrift Clients, 8080 for JMX. These are all TCP ports and can be edited in the configuration file: bin/Cassandra.in.sh

[Table of Contents](#Apache-Cassandra)

## Can you Add Or Remove column families in a working cluster?
Yes, but keeping in mind the following processes.
Do not forget to clear the commitlog with ‘nodetool drain’
Turn off Cassandra to check that there is no data left in commitlog
Delete the sstable files for the removed CFs

[Table of Contents](#Apache-Cassandra)

## What is Replication Factor in Cassandra?
Replication Factor is the measure of number of data copies existing. It is important to increase the replication factor to log into the cluster.

[Table of Contents](#Apache-Cassandra)

## Can we change Replication Factor on a Live Cluster?
Yes, but it will require running repair to alter the replica count of existing data.

[Table of Contents](#Apache-Cassandra)

## How to Iterate all rows in ColumnFamily?
Using get_range_slices. You can start iteration with the empty string and after each iteration, the last key read serves as the start key for next iteration.

[Table of Contents](#Apache-Cassandra)

## Explain Cassandra.
Cassandra is a popular NOSQL database management system used to handle large amount of data. It is free and open source distributed database that provides high availability without any failure.

[Table of Contents](#Apache-Cassandra)

## In which language Cassandra is written?
Cassandra is written in Java. It is originally designed by Facebook consisting of flexible schemas. It is highly scalable for big data.

[Table of Contents](#Apache-Cassandra)

## Which query language is used in Cassandra database?
Cassandra introduced its own Cassandra Query Language (CQL). CQL is a simple interface for accessing Cassandra, as an alternative to the traditional Structured Query Language (SQL).

[Table of Contents](#Apache-Cassandra)

## What are the benefits and advantages of Cassandra?
Cassandra delivers real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.
It provides extensible scalability and can be easily scaled up and scaled down as per the requirements.
Data can be replicated to several nodes for fault-tolerance.
Being a distributed management system, there is no single point of failure.
Every node in a cluster contains different data and able to serve any request.

[Table of Contents](#Apache-Cassandra)

## Where Cassandra stores its data?
Cassandra stores its data in the data dictionary.

[Table of Contents](#Apache-Cassandra)

## What was the design goal of Cassandra?
The main design goal of Cassandra was to handle big data workloads across multiple nodes without a single point of failure.

[Table of Contents](#Apache-Cassandra)

## How many types of NoSQL databases and give some examples.
There are mainly 4 types of NoSQL databases:
+ Document store types ( MongoDB and CouchDB)
+ Key-Value store types ( Redis and Voldemort)
+ Column store types ( Cassandra)
+ Graph store types ( Neo4j and Giraph)

[Table of Contents](#Apache-Cassandra)

## What is keyspace in Cassandra?
In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster contains of one keyspace per node.

[Table of Contents](#Apache-Cassandra)

## What are the different composite keys in Cassandra?
In Cassandra, composite keys are used to define key or a column name with a concatenation of data of different type. There are two types of Composite key in Cassandra:
+ Row Key
+ Column Name

[Table of Contents](#Apache-Cassandra)

## What is data replication in Cassandra?
Data replication is an electronic copying of data from a database in one computer or server to a database in another so that all users can share the same level of information. Cassandra stores replicas on multiple nodes to ensure reliability and fault tolerance. The replication strategy decides the nodes where replicas are placed.

[Table of Contents](#Apache-Cassandra)

## What is node in Cassandra?
In Cassandra, node is a place where data is stored.

[Table of Contents](#Apache-Cassandra)

## What do you mean by data center in Cassandra?
Data center is a complete data of clusters.

[Table of Contents](#Apache-Cassandra)

## What do you mean by commit log in Cassandra?
In Cassandra, commit log is a crash-recovery mechanism. Every write operation is written to the commit log.

[Table of Contents](#Apache-Cassandra)

## What do you mean by column family in Cassandra?
Column family is a table in RDMS that contains an ordered collection of rows.

[Table of Contents](#Apache-Cassandra)

## What do you mean by consistency in Cassandra?
Consistency in Cassandra specifies how to synchronize and up to date a row of Cassandra data and its replicas.

[Table of Contents](#Apache-Cassandra)

## How does Cassandra perform write function?
Cassandra performs the write function by applying two commits:
First commit is applied on disk and then second commit to an in-memory structure known as memtable.
When the both commits are applied successfully, to write is achieved.
Writes are written in the table structure as SSTable (sorted string table).

[Table of Contents](#Apache-Cassandra)

## What is SSTable?
SSTable is a short form of 'Sorted String Table'. It refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table.

[Table of Contents](#Apache-Cassandra)

## How the SSTable is different from other relational tables?
SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

[Table of Contents](#Apache-Cassandra)

## What is the role of ALTER KEYSPACE?
ALTER KEYSPACE is used to change the value of DURABLE_WRITES with its related properties.

[Table of Contents](#Apache-Cassandra)

## What are the differences between node and cluster and datacenter in Cassandra?
+ Node: A node is a single machine running Cassandra.
+ Cluster: A cluster is a collection of nodes that contains similar types of data together.
+ Datacenter: A datacenter is a useful component when serving customers in different geographical areas. Different nodes of a cluster can be grouped into different data centers.

[Table of Contents](#Apache-Cassandra)

## What is the use of Cassandra CQL collection?
Cassandra CQL collection is used to collect the data and store it in a column where each collection represents the same type of data. CQL consist of three types of types:
+ SET: It is a collection of unordered list of unique elements.
+ List: It is a collection of elements arranged in an order and can contain duplicate values.
+ MAP: It is a collection of unique elements in a form of key-value pair.

[Table of Contents](#Apache-Cassandra)

## What is the use of Bloom Filter in Cassandra?
On a request of a data, before doing any disk I/O Bloom filter checks whether the requested data exist in the row of SSTable.

[Table of Contents](#Apache-Cassandra)

## How does Cassandra delete data?
In Cassandra, to delete a row, it is required to associate the value of column to Tombstone (where Tombstone is a special value).

[Table of Contents](#Apache-Cassandra)

## What is SuperColumn in Cassandra?
In Cassandra, SuperColumn is a unique element containing similar collection of data. They are actually key-value pairs with values as columns.

[Table of Contents](#Apache-Cassandra)

## What are the Hadoop and HBase and Hive and Cassandra?
Hadoop, HBase, Hive and Cassandra all are Apache products.
Apache Hadoop supports file storage, grid compute processing via Map reduce. Apache Hive is a SQL like interface on the top of Hadoop. 
Apache HBase follows column family storage built like Big Table. 
Apache Cassandra also follows column family storage built like Big Table with Dynamo topology and consistency.

[Table of Contents](#Apache-Cassandra)

## What is the usage of void close method?
In Cassandra, the void close() method is used to close the current session instance.

[Table of Contents](#Apache-Cassandra)

## Which command is used to start the cqlsh prompt?
The cqlsh command is used to start the cqlsh prompt.

[Table of Contents](#Apache-Cassandra)

## What is the usage of cqlsh version command?
The "cqlsh-version" command is used to provide the version of the cqlsh you are using.

[Table of Contents](#Apache-Cassandra)

## Does Cassandra work on Windows?
Yes. Cassandra is compatible on Windows and works pretty well. Now its Linux and Window compatible version are available.

[Table of Contents](#Apache-Cassandra)

## What is Kundera in Cassandra?
In Cassandra, Kundera is an object-relational mapping (ORM) implementation which is written using Java annotations.

[Table of Contents](#Apache-Cassandra)

## What do you mean by Thrift in Cassandra?
Thrift is the name of RPC client which is used to communicate with the Cassandra Server.

[Table of Contents](#Apache-Cassandra)

## What is Hector in Cassandra?
Hector was one of the early Cassandra clients. It is an open source project written in Java using the MIT license.

[Table of Contents](#Apache-Cassandra)