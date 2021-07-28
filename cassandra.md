Question 1. Explain What Is Cassandra?

Answer :

Cassandra is an open source data storage system developed at Facebook for inbox search and designed for storing and managing large amounts of data across commodity servers. It can server as both Real time data store system for online applications Also as a read intensive database for business intelligence system

Question 2. List The Benefits Of Using Cassandra.?

Answer :

Unlike traditional or any other database, Apache Cassandra delivers near real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.

Instead of master-slave architecture, Cassandra is established on peer-to-peer architecture ensuring no failure.
It also assures phenomenal flexibility as it allows insertion of multiple nodes to any Cassandra cluster in any datacenter. Further, any client can forward its request to any server.
Cassandra facilitates extensible scalability and can be easily scaled up and scaled down as per the requirements. With a high throughput for read and write operations, this NoSQL application need not be restarted while scaling.
Cassandra is also revered for its strong data replication capability as it allows data storage at multiple locations enabling users to retrieve data from another location if one node fails. Users have the option to set up the number of replicas they want to create.
Shows brilliant performance when used for massive datasets and thus, the most preferable NoSQL DB by most organizations.
Operates on column-oriented structure and thus, quickens and simplifies the process of slicing. Even data access and retrieval becomes more efficient with column-based data model.
Further, Apache Cassandra supports schema-free/schema-optional data model, which un-necessitate the purpose of showing all the columns required by your application.
Apache Tapestry Interview Questions
Question 3. What Is The Use Of Cassandra And Why To Use Cassandra?

Answer :

Cassandra was designed to handle big data workloads across multiple nodes without any single point of failure. The various factors responsible for using Cassandra are

It is fault tolerant and consistent
Gigabytes to petabytes scalabilities
It is a column-oriented database
No single point of failure
No need for separate caching layer
Flexible schema design
It has flexible data storage, easy data distribution, and fast writes
It supports ACID (Atomicity, Consistency, Isolation, and Durability)properties
Multi-data center and cloud capable
Data compression
Question 4. Explain The Concept Of Tunable Consistency In Cassandra.?

Answer :

Tunable Consistency is a phenomenal characteristic that makes Cassandra a favored database choice of Developers, Analysts and Big data Architects. Consistency refers to the up-to-date and synchronized data rows on all their replicas. Cassandra’s Tunable Consistency allows users to select the consistency level best suited for their use cases. It supports two consistencies -Eventual and Consistency and Strong Consistency.

The former guarantees consistency when no new updates are made on a given data item, all accesses return the last updated value eventually. Systems with eventual consistency are known to have achieved replica convergence.

For Strong consistency, Cassandra supports the following condition:

R + W > N, where

N – Number of replicas
W – Number of nodes that need to agree for a successful write
R – Number of nodes that need to agree for a successful read
Apache Tapestry Tutorial
Question 5. Explain What Is Composite Type In Cassandra?

Answer :

In Cassandra, composite type allows to define key or a column name with a concatenation of data of different type. You can use two types of Composite Type

Row Key
Column Name
Apache Spark Interview Questions
Question 6. How Does Cassandra Write?

Answer :

Cassandra performs the write function by applying two commits-first it writes to a commit log on disk and then commits to an in-memory structured known as memtable. Once the two commits are successful, the write is achieved. Writes are written in the table structure as SSTable (sorted string table). Cassandra offers speedier write performance.

Question 7. How Cassandra Stores Data?

Answer :

All data stored as bytes
When you specify validator, Cassandra ensures those bytes are encoded as per requirement
Then a comparator orders the column based on the ordering specific to the encoding
While composite are just byte arrays with a specific encoding, for each component it stores a two byte length followed by the byte encoded component followed by a termination bit.
Apache Cassandra Tutorial Apache Solr Interview Questions
Question 8. Define The Management Tools In Cassandra.?

Answer :

DataStaxOpsCenter: internet-based management and monitoring solution for Cassandra cluster and DataStax. It is free to download and includes an additional Edition of OpsCenter

SPM primarily administers Cassandra metrics and various OS and JVM metrics. Besides Cassandra, SPM also monitors Hadoop, Spark, Solr, Storm, zookeeper and other Big Data platforms. The main features of SPM include correlation of events and metrics, distributed transaction tracing, creating real-time graphs with zooming, anomaly detection and heartbeat alerting.

Question 9. Mention What Are The Main Components Of Cassandra Data Model?

Answer :

The main components of Cassandra Data Model are

Cluster
Keyspace
Column
Column & Family
Apache Storm Interview Questions
Question 10. Define Memtable.?

Answer :

Similar to table, memtable is in-memory/write-back cache space consisting of content in key and column format. The data in memtable is sorted by key, and each ColumnFamily consist of a distinct memtable that retrieves column data via key. It stores the writes until it is full, and then flushed out.

Apache Solr Tutorial
Question 11. Explain What Is A Column Family In Cassandra?

Answer :

Column family in Cassandra is referred for a collection of Rows.

Apache Hive Interview Questions
Question 12. What Is Sstable? How Is It Different From Other Relational Tables?

Answer :

SSTable expands to ‘Sorted String Table,’ which refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table. Exhibiting immutability, SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

Apache Tapestry Interview Questions
Question 13. Explain What Is A Cluster In Cassandra?

Answer :

A cluster is a container for keyspaces. Cassandra database is segmented over several machines that operate together. The cluster is the outermost container which arranges the nodes in a ring format and assigns data to them. These nodes have a replica which takes charge in case of data handling failure.

Apache Storm Tutorial
Question 14. Explain The Concept Of Bloom Filter.?

Answer :

Associated with SSTable, Bloom filter is an off-heap (off the Java heap to native memory) data structure to check whether there is any data available in the SSTable before performing any I/O disk operation.

Question 15. List Out The Other Components Of Cassandra?

Answer :

The other components of Cassandra are

Node
Data Center
Cluster
Commit log
Mem-table
SSTable
Bloom Filter
Apache Pig Interview Questions
Question 16. Explain Cap Theorem?

Answer :

With a strong requirement to scale systems when additional resources are needed, CAP Theorem plays a major role in maintaining the scaling strategy. It is an efficient way to handle scaling in distributed systems. Consistency Availability and Partition tolerance (CAP) theorem states that in distributed systems like Cassandra, users can enjoy only two out of these three characteristics.

One of them needs to be sacrificed. Consistency guarantees the return of most recent write for the client, Availability returns a rational response within minimum time and in Partition Tolerance, the system will continue its operations when network partitions occur. The two options available are AP and CP.

Apache Hive Tutorial
Question 17. Explain What Is A Keyspace In Cassandra?

Answer :

In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster consist of one keyspace per node.

Apache Flume Interview Questions
Question 18. State The Differences Between A Node, A Cluster And Datacenter In Cassandra.?

Answer :

While a node is a single machine running Cassandra, cluster is a collection of nodes that have similar type of data grouped together. DataCentersare useful components when serving customers in different geographical areas. You can group different nodes of a cluster into different data centers.

Apache Spark Interview Questions
Question 19. Mention What Are The Values Stored In The Cassandra Column?

Answer :

In Cassandra Column, basically there are three values

Column Name
Value
Time Stamp
Apache Pig Tutorial
Question 20. How To Write A Query In Cassandra?

Answer :

Using CQL (Cassandra Query Language).Cqlsh is used for interacting with database.

Apache Kafka Interview Questions
Question 21. Mention When You Can Use Alter Keyspace?

Answer :

ALTER KEYSPACE can be used to change properties such as the number of replicas and the durable_write of a keyspace.

Question 22. What Os Cassandra Supports?

Answer :

Windows and Linux.

Apache Flume Tutorial
Question 23. Explain What Is Cassandra-cqlsh?

Answer :

Cassandra-Cqlsh is a query language that enables users to communicate with its database. By using Cassandra cqlsh, you can do following things

Define a schema
Insert a data and
Execute a query
Apache Ant Interview Questions
Question 24. What Is Cassandra Data Model?

Answer :

Cassandra Data Model consists of four main components:

Cluster: Made up of multiple nodes and keyspaces
Keyspace: a namespace to group multiple column families, especially one per partition
Column: consists of a column name, value and timestamp
ColumnFamily: multiple columns with row key reference.
Apache Solr Interview Questions
Question 25. Mention What Does The Shell Commands “capture” And “consistency” Determines?

Answer :

There are various Cqlsh shell commands in Cassandra. Command “Capture”, captures the output of a command and adds it to a file while, command “Consistency” display the current consistency level or set a new consistency level.

Apache Kafka Tutorial
Question 26. What Is Cql?

Answer :

CQL is Cassandra Query language to access and query the Apache distributed database. It consists of a CQL parser that incites all the implementation details to the server. The syntax of CQL is similar to SQL but it does not alter the Cassandra data model.

Apache Camel Interview Questions
Question 27. What Is Mandatory While Creating A Table In Cassandra?

Answer :

While creating a table primary key is mandatory, it is made up of one or more columns of a table.

Apache Storm Interview Questions
Question 28. Explain The Concept Of Compaction In Cassandra.?

Answer :

Compaction refers to a maintenance process in Cassandra , in which, the SSTables are reorganized for data optimization of data structure son the disk. The compaction process is useful during interactive with memtable. There are two type sof compaction in Cassandra:

Minor compaction: started automatically when a new sstable is created. Here, Cassandra condenses all the equally sized sstables into one.
Major compaction : is triggered manually using nodetool. Compacts all sstables of a ColumnFamily into one.
Apache Ant Tutorial
Question 29. Mention What Needs To Be Taken Care While Adding A Column?

Answer :

While adding a column you need to take care that the

Column name is not conflicting with the existing column names
Table is not defined with compact storage option
Apache Tajo Interview Questions
Question 30. Does Cassandra Support Acid Transactions?

Answer :

Unlike relational databases, Cassandra does not support ACID transactions.

Question 31. Explain How Cassandra Writes Data?

Answer :

Cassandra writes data in three components

Commitlog write
Memtable write
SStable write
Apache Tajo Tutorial
Question 32. What Is Supercolumn In Cassandra?

Answer :

Cassandra Super Column is a unique element consisting of similar collections of data. They are actually key-value pairs with values as columns. It is a sorted array of columns, and they follow a hierarchy when in action: keystore> column family> super column> column data structure in JSON.

Similar to row keys, super column data entries contains no independent values but are used to collect other columns. It is interesting to note that super column keys appearing in different rows do not necessarily match and will not ever.

Apache Impala Interview Questions
Question 33. Explain What Is Memtable In Cassandra?

Answer :

Cassandra writes the data to a in memory structure known as Memtable
It is an in-memory cache with content stored as key/column
By key Memtable data are sorted
There is a separate Memtable for each ColumnFamily, and it retrieves column data from the key
Apache Hive Interview Questions
Question 34. Define The Consistency Levels For Read Operations In Cassandra.?

Answer :

ALL: Highly consistent. A write must be written to commitlog and memtable on all replica nodes in the cluster
EACH_QUORUM: A write must be written to commitlog and memtable on quorum of replica nodes in all data centers.
LOCAL_QUORUM:A write must be written to commitlog and memtable on quorum of replica nodes in the same center.
ONE: A write must be written to commitlog and memtableof at least one replica node.
TWO, Three: Same as One but at least two and three replica nodes, respectively
LOCAL_ONE: A write must be written for at least one replica node in the local data center ANY
SERIAL: Linearizable Consistency to prevent unconditional updates
LOCAL_SERIAL: Same as Serial but restricted to local data center
Question 35. Explain How Cassandra Writes Changed Data Into Commitlog?

Answer :

Cassandra concatenate changed data to commitlog

Commitlog acts as a crash recovery log for data
Until the changed data is concatenated to commitlog write operation will be never considered successful
Data will not be lost once commitlog is flushed out to file.

Question 36. What Is Difference Between Column And Super Column?

Answer :

Both elements work on the principle of tuple having name and value. However, the former‘s value is a string while the value in latter is a Map of Columns with different data types.

Unlike Columns, Super Columns do not contain the third component of timestamp.

Apache Pig Interview Questions
Question 37. What Is Columnfamily?

Answer :

As the name suggests, ColumnFamily refers to a structure having infinite number of rows. That are referred by a key-value pair, where key is the name of the column and value represents the column data. It is much similar to a hashmap in java or dictionary in Python. Rememeber, the rows are not limited to a predefined list of Columns here. Also, the ColumnFamily is absolutely flexible with one row having 100 Columns while the other only 2 columns.

Question 38. Explain How Cassandra Delete Data?

Answer :

SSTables are immutable and cannot remove a row from SSTables. When a row needs to be deleted, Cassandra assigns the column value with a special value called Tombstone. When the data is read, the Tombstone value is considered as deleted.

Question 39. Define The Use Of Source Command In Cassandra.?

Answer :

Source command is used to execute a file consisting of CQL statements.

Question 40. What Is Thrift?

Answer :

Thrift is a legacy RPC protocol or API unified with a code generation tool for CQL. The purpose of using Thrift in Cassandra is to facilitate access to the DB across the programming language.

Apache Flume Interview Questions
Question 41. Explain Tombstone In Cassandra.?

Answer :

Tombstone is row marker indicating a column deletion. These marked columns are deleted during compaction. Tombstones are of great significance as Cassnadra supports eventual consistency, where the data must respond before any successful operation.

Question 42. What Platforms Cassandra Runs On?

Answer :

Since Cassandra is a Java application, it can successfully run on any Java-driven platform or Java Runtime Environment (JRE) or Java Virtual Machine (JVM). Cassandra also runs on RedHat, CentOS, Debian and Ubuntu Linux platforms.

Apache Kafka Interview Questions
Question 43. Name The Ports Cassandra Uses.?

Answer :

The default settings state that Cassandra uses 7000 ports for Cluster Management, 9160 for Thrift Clients, 8080 for JMX. These are all TCP ports and can be edited in the configuration file: bin/Cassandra.in.sh

Question 44. Can You Add Or Remove Column Families In A Working Cluster?

Answer :

Yes, but keeping in mind the following processes.

Do not forget to clear the commitlog with ‘nodetool drain’
Turn off Cassandra to check that there is no data left in commitlog
Delete the sstable files for the removed CFs
Question 45. What Is Replication Factor In Cassandra?

Answer :

Replication Factor is the measure of number of data copies existing. It is important to increase the replication factor to log into the cluster.

Question 46. Can We Change Replication Factor On A Live Cluster?

Answer :

Yes, but it will require running repair to alter the replica count of existing data.

Question 47. How To Iterate All Rows In Columnfamily?

Answer :

Using get_range_slices. You can start iteration with the empty string and after each iteration, the last key read serves as the start key for next iteration.



xplain Cassandra.
Cassandra is a popular NOSQL database management system used to handle large amount of data. It is free and open source distributed database that provides high availability without any failure.

2) In which language Cassandra is written?
   Cassandra is written in Java. It is originally designed by Facebook consisting of flexible schemas. It is highly scalable for big data.

3) Who was the original author of Cassandra?
   The original authors of Cassandra are Avinash Lakshman and Prashant Malik. It was initially developed at Facebook to power the Facebook inbox search feature.

4) Which query language is used in Cassandra database?
   Cassandra introduced its own Cassandra Query Language (CQL). CQL is a simple interface for accessing Cassandra, as an alternative to the traditional Structured Query Language (SQL).

5) What are the benefits/advantages of Cassandra?
   Cassandra delivers real-time performance simplifying the work of Developers, Administrators, Data Analysts and Software Engineers.
   It provides extensible scalability and can be easily scaled up and scaled down as per the requirements.
   Data can be replicated to several nodes for fault-tolerance.
   Being a distributed management system, there is no single point of failure.
   Every node in a cluster contains different data and able to serve any request.
6) Where Cassandra stores its data?
   Cassandra stores its data in the data dictionary.

7) What was the design goal of Cassandra?
   The main design goal of Cassandra was to handle big data workloads across multiple nodes without a single point of failure.

8) How many types of NoSQL databases? Give some examples.
   There are mainly 4 types of NoSQL databases:

Document store types ( MongoDB and CouchDB)
Key-Value store types ( Redis and Volgemort)
Column store types ( Cassandra)
Graph store types ( Neo4j and Giraph)
9) Mention some important components of Cassandra data models?
   These are some key components of Cassandra data model: -

Table( collection of columns)
Node
Cluster
Keyspace
10) What are the other components of Cassandra?
    Some other components of Cassandra are:

Node
Data Center
Commit log
Mem-table
SSTable
Bloom Filter
11) What is keyspace in Cassandra?
    In Cassandra, a keyspace is a namespace that determines data replication on nodes. A cluster contains of one keyspace per node.

12) What are the different composite keys in Cassandra?
    In Cassandra, composite keys are used to define key or a column name with a concatenation of data of different type. There are two types of Composite key in Cassandra:

Row Key
Column Name
13) What is data replication in Cassandra?
    Data replication is an electronic copying of data from a database in one computer or server to a database in another so that all users can share the same level of information. Cassandra stores replicas on multiple nodes to ensure reliability and fault tolerance. The replication strategy decides the nodes where replicas are placed.

14) What is node in Cassandra?
    In Cassandra, node is a place where data is stored.

15) 15) What do you mean by data center in Cassandra?
        Data center is a complete data of clusters.

16) What do you mean by commit log in Cassandra?
    In Cassandra, commit log is a crash-recovery mechanism. Every write operation is written to the commit log.

17) 17) What do you mean by column family in Cassandra?
        Column family is a table in RDMS that contains an ordered collection of rows.

18) What do you mean by consistency in Cassandra?
    Consistency in Cassandra specifies how to synchronize and up to date a row of Cassandra data and its replicas.

19) How many types of tunable consistency are supported in Cassandra?
    It supports two consistencies: Eventual Consistency and Strong Consistency.

The eventual consistency is used when no new updates are made on a given data item, all accesses return the last updated value eventually. Systems with eventual consistency are known to have achieved replica convergence.

Cassandra supports the following conditions for strong consistency:

R + W > N

Here

N: Number of replicas

W: Number of nodes that need to agree for a successful write

R: Number of nodes that need to agree for a successful read

20) What is tunable consistency in Cassandra?
    Tunable Consistency is a phenomenal characteristic of Cassandra which makes it a popular choice. Consistency refers to the up-to-date and synchronized data rows on all their replicas. Cassandra's Tunable Consistency facilitates users to select the consistency level best suited for their use cases.

21) What is the syntax to create keyspace in Cassandra?
    CREATE KEYSPACE <identifier> WITH <properties>
22) What is a column family in Cassandra?
    In Cassandra, a collection of rows is referred as "column family".

23) How does Cassandra perform write function?
    Cassandra performs the write function by applying two commits:

First commit is applied on disk and then second commit to an in-memory structure known as memtable.
When the both commits are applied successfully, the write is achieved.
Writes are written in the table structure as SSTable (sorted string table).
24) What is memtable?
    Memtable is in-memory/write-back cache space containing content in key and column format. In memtable, data is sorted by key, and each ColumnFamily has a distinct memtable that retrieves column data via key. It stores the writes until it is full, and then flushed out.

25) What is SSTable?
    SSTable is a short form of 'Sorted String Table'. It refers to an important data file in Cassandra and accepts regular written memtables. They are stored on disk and exist for each Cassandra table.

26) How the SSTable is different from other relational tables?
    SStables do not allow any further addition and removal of data items once written. For each SSTable, Cassandra creates three separate files like partition index, partition summary and a bloom filter.

27) What are the management tools in Cassandra?
    DataStaxOpsCenter: It is an internet-based management and monitoring solution for Cassandra cluster and DataStax. It is free to download and includes an additional Edition of OpsCenter.

SPM: SPM primarily administers Cassandra metrics and various OS and JVM metrics. It also monitors Hadoop, Spark, Solr, Storm, zookeeper and other Big Data platforms besides Cassandra.

28) Mention some important features of SPM in Cassandra?
    The main features of SPM are:

Correlation of events and metrics
Distributed transaction tracing
Creating real-time graphs with zooming
Detection and heartbeat alerting
29) What is cluster in Cassandra?
    In Cassandra, the cluster is an outermost container for keyspaces that arranges the nodes in a ring format and assigns data to them. These nodes have a replica which takes charge in case of data handling failure.

30) What is the role of ALTER KEYSPACE?
    ALTER KEYSPACE is used to change the value of DURABLE_WRITES with its related properties.

31) What do you mean by Cassandra-Cqlsh?
    Cqlsh is a Cassandra query language shell used to execute the commands of CQL (Cassandra query language).

32) What are the differences between a node, a cluster, and datacenter in Cassandra?
    Node: A node is a single machine running Cassandra.

Cluster: A cluster is a collection of nodes that contains similar types of data together.

Datacenter: A datacenter is a useful component when serving customers in different geographical areas. Different nodes of a cluster can be grouped into different data centers.

33) What is the use of Cassandra CQL collection?
    Cassandra CQL collection is used to collect the data and store it in a column where each collection represents the same type of data. CQL consist of three types of types:

SET: It is a collection of unordered list of unique elements.
List: It is a collection of elements arranged in an order and can contain duplicate values.
MAP: It is a collection of unique elements in a form of key-value pair.
34) What is the use of Bloom Filter in Cassandra?
    On a request of a data, before doing any disk I/O Bloom filter checks whether the requested data exist in the row of SSTable.

35) How does Cassandra delete data?
    In Cassandra, to delete a row, it is required to associate the value of column to Tombstone (where Tombstone is a special value).

36) What is SuperColumn in Cassandra?
    In Cassandra, SuperColumn is a unique element containing similar collection of data. They are actually key-value pairs with values as columns.

37) What is the difference between Column and SuperColumn?
    Difference between Column and SuperColumn:

The values in columns are string while the values in SuperColumn are Map of Columns with different data types.
Unlike Columns, Super Columns do not contain the third component of timestamp.
38) What is Hadoop, HBase, Hive and Cassandra? Specify similarities and differences among them.
    Hadoop, HBase, Hive and Cassandra all are Apache products.

Apache Hadoop supports file storage, grid compute processing via Map reduce. Apache Hive is a SQL like interface on the top of Haddop. Apache HBase follows column family storage built like Big Table. Apache Cassandra also follows column family storage built like Big Table with Dynamo topology and consistency.

39) What is the usage of "void close()" method?
    In Cassandra, the void close() method is used to close the current session instance.

40) Which command is used to start the cqlsh prompt?
    The cqlsh command is used to start the cqlsh prompt.

41) What is the usage of "cqlsh-version" command?
    The "cqlsh-version" command is used to provide the version of the cqlsh you are using.

42) Does Cassandra work on Windows?
    Yes. Cassandra is compatible on Windows and works pretty well. Now its Linux and Window compatible version are available.

43) What is Kundera in Cassandra?
    In Cassandra, Kundera is an object-relational mapping (ORM) implementation which is written using Java annotations.

44) What do you mean by Thrift in Cassandra?
    Thrift is the name of RPC client which is used to communicate with the Cassandra Server.

45) What is Hector in Cassandra?
    Hector was one of the early Cassandra clients. It is an open source project written in Java using the MIT license.