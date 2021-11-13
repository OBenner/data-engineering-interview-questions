[Interview questions](full.md)
# Hbase
+ [What are the differences between RDBMS and HBase data model?](#What-are-the-differences-between-RDBMS-and-HBase-data-model)
+ [Explain what is Hbase?](#Explain-what-is-Hbase)
+ [Explain why to use Hbase?](#Explain-why-to-use-Hbase)
+ [Mention what are the key components of Hbase?](#Mention-what-are-the-key-components-of-Hbase)
+ [Explain what does Hbase consists of?](#Explain-what-does-Hbase-consists-of)
+ [Mention how many operational commands in Hbase?](#Mention-how-many-operational-commands-in-Hbase)
+ [Explain what is WAL and Hlog in Hbase?](#Explain-what-is-WAL-and-Hlog-in-Hbase)
+ [When you should use Hbase?](#When-you-should-use-Hbase)
+ [In Hbase what is column families?](#In-Hbase-what-is-column-families)
+ [Explain what is the row key?](#Explain-what-is-the-row-key)
+ [Explain deletion in Hbase? Mention what are the three types of tombstone markers in Hbase?](#Explain-deletion-in-Hbase?-Mention-what-are-the-three-types-of-tombstone-markers-in-Hbase)
+ [Explain how does Hbase actually delete a row?](#Explain-how-does-Hbase-actually-delete-a-row)
+ [Explain what happens if you alter the block size of a column family on an already occupied database?](#Explain-what-happens-if-you-alter-the-block-size-of-a-column-family-on-an-already-occupied-database)
+ [Mention the difference between Hbase and Relational Database?](#Mention-the-difference-between-Hbase-and-Relational-Database)
+ [What is HBaseFsck class?](#What-is-HBaseFsck-class)
+ [What are the main key structures of HBase?](#What-are-the-main-key-structures-of-HBase)
+ [Discuss how you can use filters in Apache HBase](#Discuss-how-you-can-use-filters-in-Apache-HBas)
+ [HBase support syntax structure like SQL yes or No?](#HBase-support-syntax-structure-like-SQL-yes-or-No)
+ [What is the meaning of compaction in HBase?](#What-is-the-meaning-of-compaction-in-HBase)
+ [How will you implement joins in HBase?](#How-will-you-implement-joins-in-HBase)
+ [Explain JMX concerning HBSE](#Explain-JMX-concerning-HBS)
+ [What is the use of MasterServer?](#What-is-the-use-of-MasterServer)
+ [Define the Term Thrift.](#Define-the-Term-Thrift)
+ [Why use HColumnDescriptor class?](#Why-use-HColumnDescriptor-class)
+ [What is a cell in HBase?](#What-is-a-cell-in-HBase)
+ [What is a Bloom filter?](#What-is-a-Bloom-filter)
+ [Tell me about the types of HBase Operations?](#Tell-me-about-the-types-of-HBase-Operations)
+ [What is the use of HBase HMaster?](#What-is-the-use-of-HBase-HMaster)
+ [Which technique can you use in HBase to access HFile directly without the help of HBase?](#Which-technique-can-you-use-in-HBase-to-access-HFile-directly-without-the-help-of-HBase)
+ [Can the region server will be located on all DataNodes?](#Can-the-region-server-will-be-located-on-all-DataNodes)
+ [Name the filter which accepts the page size as the parameter in HBase?](#Name-the-filter-which-accepts-the-page-size-as-the-parameter-in-HBase)
+ [When would you use HBase?](#When-would-you-use-HBase)
+ [What is the use of get method?](#What-is-the-use-of-get-method)
+ [Define the difference between Hive and HBase?](#Define-the-difference-between-Hive-and-HBase)
+ [Explain the data model of HBase.](#Explain-the-data-model-of-HBase)
+ [Define column families?](#Define-column-families)
+ [Define standalone mode in HBase?](#Define-standalone-mode-in-HBase)
+ [What is decorating Filters?](#What-is-decorating-Filters)
+ [What is RegionServer?](#What-is-RegionServer)
+ [What are the data manipulation commands of HBase?](#What-are-the-data-manipulation-commands-of-HBase)
+ [What happens when you issue a delete command in HBase?](#What-happens-when-you-issue-a-delete-command-in-HBase)
+ [What are different tombstone markers in HBase?](#What-are-different-tombstone-markers-in-HBase)
+ [HBase blocksize is configured on which level?](#HBase-blocksize-is-configured-on-which-level)
+ [Which command is used to run HBase Shell?](#Which-command-is-used-to-run-HBase-Shell)
+ [Which command is used to show the current HBase user?](#Which-command-is-used-to-show-the-current-HBase-user)
+ [What is the full form of MSLAB?](#What-is-the-full-form-of-MSLAB)
+ [Define LZO?](#Define-LZO)
+ [What is HBase Fsck?](#What-is-HBase-Fsck)
+ [What is REST?](#What-is-REST)
+ [What is Nagios?](#What-is-Nagios)
+ [What is the use of ZooKeeper?](#What-is-the-use-of-ZooKeeper)
+ [Define catalog tables in HBase?](#Define-catalog-tables-in-HBase)
+ [Define compaction in HBase?](#Define-compaction-in-HBase)
+ [Explain what is Hbase?](#Explain-what-is-Hbase)
+ [Explain why to use Hbase?](#Explain-why-to-use-Hbase)
+ [Mention what are Key Components of Hbase?](#Mention-what-are-Key-Components-of-Hbase)
+ [What is the Role of Master Server in Hbase?](#What-is-the-Role-of-Master-Server-in-Hbase)
+ [Explain what does Hbase consists of?](#Explain-what-does-Hbase-consists-of)
+ [What is the Role of Zookeeper in Hbase?](#What-is-the-Role-of-Zookeeper-in-Hbase)
+ [Mention how many operational commands in Hbase?](#Mention-how-many-operational-commands-in-Hbase)
+ [When do we need to disable a table in Hbase?](#When-do-we-need-to-disable-a-table-in-Hbase)
+ [Explain what is Wal and Hlog in Hbase?](#Explain-what-is-Wal-and-Hlog-in-Hbase)
+ [What are the different Types of Filters used in Hbase?](#What-are-the-different-Types-of-Filters-used-in-Hbase)
+ [In Hbase what is Column Families?](#In-Hbase-what-is-Column-Families)
+ [Name three disadvantages Hbase has as compared to Rdbms?](#Name-three-disadvantages-Hbase-has-as-compared-to-Rdbms)
+ [Explain what is the Row Key?](#Explain-what-is-the-Row-Key)
+ [Is Hbase a scale out or scale up process?](#Is-Hbase-a-scale-out-or-scale-up-process)
+ [Explain deletion in Hbase?](#Explain-deletion-in-Hbase)
+ [What are the step in writing something into Hbase by a Client?](#What-are-the-step-in-writing-something-into-Hbase-by-a-Client)
+ [Explain how does Hbase actually delete a Row?](#Explain-how-does-Hbase-actually-delete-a-Row)
+ [What is compaction in Hbase?](#What-is-compaction-in-Hbase)
+ [Explain what happens if you alter the Block Size of a column Family on an already occupied Database?](#Explain-what-happens-if-you-alter-the-Block-Size-of-a-column-Family-on-an-already-occupied-Database)
+ [What are the different compaction types in Hbase?](#What-are-the-different-compaction-types-in-Hbase)
+ [What is a Cell in Hbase?](#What-is-a-Cell-in-Hbase)
+ [What is the Scope of a Rowkey in Hbase?](#What-is-the-Scope-of-a-Rowkey-in-Hbase)
+ [What is the Role of the Class Hcolumndescriptor in Hbase?](#What-is-the-Role-of-the-Class-Hcolumndescriptor-in-Hbase)
+ [What is a Namespace in Hbase?](#What-is-a-Namespace-in-Hbase)
+ [What is the Lower Bound of Versions in Hbase?](#What-is-the-Lower-Bound-of-Versions-in-Hbase)
+ [What is Hotspotting in Hbase?](#What-is-Hotspotting-in-Hbase)
+ [What is Ttl in Hbase?](#What-is-Ttl-in-Hbase)
+ [Why do we Pre create empty Regions?](#Why-do-we-Pre-create-empty-Regions)
+ [Does Hbase support Table Joins?](#Does-Hbase-support-Table-Joins)
+ [Which File in Hbase is designed after Sstable File of Bigtable?](#Which-File-in-Hbase-is-designed-after-Sstable-File-of-Bigtable)
+ [What is a Hbase Store?](#What-is-a-Hbase-Store)
+ [What are the Two Types of Table Design Approach in Hbase?](#What-are-the-Two-Types-of-Table-Design-Approach-in-Hbase)
+ [When do we do Manual Region Splitting?](#When-do-we-do-Manual-Region-Splitting)
+ [In which scenario should we consider creating a short and wide Hbase Table?](#In-which-scenario-should-we-consider-creating-a-short-and-wide-Hbase-Table)
+ [In Hbase what is Log Splitting?](#In-Hbase-what-is-Log-Splitting)
+ [How does Hbase support Bulk Data Loading?](#How-does-Hbase-support-Bulk-Data-Loading)
+ [Why Multiwal is Needed?](#Why-Multiwal-is-Needed)
+ [How does Hbase provide High Availability?](#How-does-Hbase-provide-High-Availability)
+ [How does Wal help when a Regionserver Crashes?](#How-does-Wal-help-when-a-Regionserver-Crashes)
+ [What is Hregionserver in Hbase?](#What-is-Hregionserver-in-Hbase)
+ [What are the different Block Caches in Hbase?](#What-are-the-different-Block-Caches-in-Hbase)

[Table of Contents](#Hbase)


## What are the differences between RDBMS and HBase data model?
The main differences between RDBMS and HBase data model are as follows:
Schema: In RDBMS, there is a schema of tables, columns etc. In HBASE, there is no schema.
Normalization: RDBMS data model is normalized as per the rule of Relation DB normalization.
HBase data model does not require any normalization.
Partition: In RDBMS we can choose to do partitioning. In HBase, partitioning happens automatically.

[Table of Contents](#Hbase)

## Explain what is Hbase?
Hbase is a column-oriented database management system which runs on top of HDFS (Hadoop Distribute File System). Hbase is not a relational data store, and it does not support structured query language like SQL.
In Hbase, a master node regulates the cluster and region servers to store portions of the tables and operates the work on the data.

[Table of Contents](#Hbase)

## Explain why to use Hbase?
High capacity storage system
Distributed design to cater large tables
Column-Oriented Stores
Horizontally Scalable
High performance & Availability
Base goal of Hbase is millions of columns, thousands of versions and billions of rows
Unlike HDFS (Hadoop Distribute File System), it supports random real time CRUD operations

[Table of Contents](#Hbase)

## Mention what are the key components of Hbase?
Zookeeper: It does the co-ordination work between client and Hbase Maser
Hbase Master: Hbase Master monitors the Region Server
RegionServer: RegionServer monitors the Region
Region: It contains in memory data store(MemStore) and Hfile.
Catalog Tables: Catalog tables consist of ROOT and META

[Table of Contents](#Hbase)

## Explain what does Hbase consists of?
Hbase consists of a set of tables
And each table contains rows and columns like traditional database
Each table must contain an element defined as a Primary Key
Hbase column denotes an attribute of an object

[Table of Contents](#Hbase)

## Mention how many operational commands in Hbase?
Operational command in Hbases is about five types
Get
Put
Delete
Scan
Increment

[Table of Contents](#Hbase)

## Explain what is WAL and Hlog in Hbase?
WAL (Write Ahead Log) is similar to MySQL BIN log; it records all the changes occur in data. It is a standard sequence file by Hadoop and it stores HLogkey’s.  These keys consist of a sequential number as well as actual data and are used to replay not yet persisted data after a server crash. So, in cash of server failure WAL work as a life-line and retrieves the lost data’s.

[Table of Contents](#Hbase)

## When you should use Hbase?
Data size is huge: When you have tons and millions of records to operate
Complete Redesign: When you are moving RDBMS to Hbase, you consider it as a complete re-design then mere just changing the ports
SQL-Less commands: You have several features like transactions; inner joins, typed columns, etc.
Infrastructure Investment: You need to have enough cluster for Hbase to be really useful

[Table of Contents](#Hbase)

## In Hbase what is column families?
Column families comprise the basic unit of physical storage in Hbase to which features like compressions are applied.

[Table of Contents](#Hbase)

## Explain what is the row key?
Row key is defined by the application. As the combined key is pre-fixed by the rowkey, it enables the application to define the desired sort order. It also allows logical grouping of cells and make sure that all cells with the same rowkey are co-located on the same server.

[Table of Contents](#Hbase)

## Explain deletion in Hbase? Mention what are the three types of tombstone markers in Hbase?
When you delete the cell in Hbase, the data is not actually deleted but a tombstone marker is set, making the deleted cells invisible.  Hbase deleted are actually removed during compactions.
Three types of tombstone markers are there:
Version delete marker: For deletion, it marks a single version of a column
Column delete marker: For deletion, it marks all the versions of a column
Family delete marker: For deletion, it marks of all column for a column family

[Table of Contents](#Hbase)

## Explain how does Hbase actually delete a row?
In Hbase, whatever you write will be stored from RAM to disk, these disk writes are immutable barring compaction. During deletion process in Hbase, major compaction process delete marker while minor compactions don’t. In normal deletes, it results in a delete tombstone marker- these delete data they represent are removed during compaction.
Also, if you delete data and add more data, but with an earlier timestamp than the tombstone timestamp, further Gets may be masked by the delete/tombstone marker and hence you will not receive the inserted value until after the major compaction.

[Table of Contents](#Hbase)

## Explain what happens if you alter the block size of a column family on an already occupied database?
When you alter the block size of the column family, the new data occupies the new block size while the old data remains within the old block size. During data compaction, old data will take the new block size.  New files as they are flushed, have a new block size whereas existing data will continue to be read correctly. All data should be transformed to the new block size, after the next major compaction.

[Table of Contents](#Hbase)

## Mention the difference between Hbase and Relational Database?
Hbase	Relational Database
It is schema-less
It is a column-oriented data store
It is used to store de-normalized data
It contains sparsely populated tables
Automated partitioning is done in Hbase
It is a schema based database
It is a row-oriented data store
It is used to store normalized data
It contains thin tables
There is no such provision or built-in support for partitioning

[Table of Contents](#Hbase)

## What is HBaseFsck class?
There is a tool name called back is available in HBase, which is implemented by the HBaseFsck class. It offers several command-line switches that influence its behavior.

[Table of Contents](#Hbase)

## What are the main key structures of HBase?
Row key and Column key are the two most important key structures using in HBase

[Table of Contents](#Hbase)

## Discuss how you can use filters in Apache HBase
Filters In HBase Shell. It was introduced in Apache HBase 0.92 which helps you to conduct server-side filtering for accessing HBase over HBase shell or thrift.

[Table of Contents](#Hbase)

## HBase support syntax structure like SQL yes or No?
No, unfortunately, SQL support for HBase is not available currently. However, by using Apache Phoenix, we can retrieve data from HBase through SQL queries.

[Table of Contents](#Hbase)

## What is the meaning of compaction in HBase?
At the time of heavy incoming writes, it is impossible to achieve optimal performance by having one file per store. HBase helps you to combines all these HFiles to reduce the number of disk seeds for every read. This process is known as for as Compaction in HBase.

[Table of Contents](#Hbase)

## How will you implement joins in HBase?
HBase, not support joins directly but uses MapReduce jobs join queries can be implemented by retrieving data with the help of different HBase tables.

[Table of Contents](#Hbase)

## Explain JMX concerning HBSE
Java Management Extensions or JMX is an export status of Java applications is the standard for them.

[Table of Contents](#Hbase)

## What is the use of MasterServer?
Master sever helps you to assign a region to the region server as well. It also helps you to handle the load balancing we use the MasterServer.

[Table of Contents](#Hbase)

## Define the Term Thrift.
Apache Thrift is written in C++. It provides schema compilers for various programming languages like C++, Perl, PHP, Python, Ruby, and more.

[Table of Contents](#Hbase)

## Why use HColumnDescriptor class?
The detail regarding column family such as compression settings, Number of versions, are stored .in HColumnDescriptor.

[Table of Contents](#Hbase)

## What is a cell in HBase?
A cell in HBase is the smallest unit of an Hbase table. It helps you to holds a piece of data in the form of a tuple{row, column, version}

[Table of Contents](#Hbase)

## What is a Bloom filter?
HBase supports Bloom Filter helps you to improve the overall throughput of the cluster. An HBase Bloom Filter is a space-efficient mechanism to test whether a HFile includes certain row or row-col cell.

[Table of Contents](#Hbase)

## Tell me about the types of HBase Operations?
Two types of HBase Operations are:
Read Operation
Write Operation

[Table of Contents](#Hbase)

## What is the use of HBase HMaster?
Main responsibilities of a master are:
Coordinating the region servers
Admin functions

[Table of Contents](#Hbase)

## Which technique can you use in HBase to access HFile directly without the help of HBase?
To access HFile directly without using HBase, we use HFile.main() method.

[Table of Contents](#Hbase)

## Can the region server will be located on all DataNodes?
Yes, Region Servers run on the same servers as a DataNodes

[Table of Contents](#Hbase)

## Name the filter which accepts the page size as the parameter in HBase?
A filter named PageFilter accepts the page size as the parameter.

[Table of Contents](#Hbase)

## When would you use HBase?
HBase is used in cases where we need random read and write operations and it can perform a number of operations per second on a large data sets.
HBase gives strong data consistency.
It can handle very large tables with billions of rows and millions of columns on top of commodity hardware cluster.

[Table of Contents](#Hbase)

## What is the use of get method?
get() method is used to read the data from the table.

[Table of Contents](#Hbase)

## Define the difference between Hive and HBase?
Apache Hive is a data warehousing infrastructure built on top of Hadoop. It helps in querying data stored in HDFS for analysis using Hive Query Language (HQL), which is a SQL-like language, that gets translated into MapReduce jobs. Hive performs batch processing on Hadoop.
Apache HBase is NoSQL key/value store which runs on top of HDFS. Unlike Hive, HBase operations run in real-time on its database rather than MapReduce jobs. HBase partitions the tables, and the tables are further splitted into column families.
Hive and HBase are two different Hadoop based technologies – Hive is an SQL-like engine that runs MapReduce jobs, and HBase is a NoSQL key/value database of Hadoop. We can use them together. Hive can be used for analytical queries while HBase for real-time querying. Data can even be read and written from HBase to Hive and vice-versa.

[Table of Contents](#Hbase)

## Explain the data model of HBase.
HBase comprises of:
Set of tables.
Each table consists of column families and rows.
Row key acts as a Primary key in HBase.
Any access to HBase tables uses this Primary Key.
Each column qualifier present in HBase denotes attributes corresponding to the object which resides in the cell.

[Table of Contents](#Hbase)

## Define column families?
Column Family is a collection of columns, whereas row is a collection of column families.

[Table of Contents](#Hbase)

## Define standalone mode in HBase?
It is a default mode of HBase. In standalone mode, HBase does not use HDFS—it uses the local filesystem instead—and it runs all HBase daemons and a local ZooKeeper in the same JVM process.

[Table of Contents](#Hbase)

## What is decorating Filters?
It is useful to modify, or extend, the behavior of a filter to gain additional control over the returned data. These types of filters are known as decorating filter. It includes SkipFilter and WhileMatchFilter.

[Table of Contents](#Hbase)

## What is RegionServer?
A table can be divided into several regions. A group of regions is served to the clients by a Region Server.

[Table of Contents](#Hbase)

## What are the data manipulation commands of HBase?
Data Manipulation commands of HBase are:
put – Puts a cell value at a specified column in a specified row in a particular table.
get – Fetches the contents of a row or a cell.
delete – Deletes a cell value in a table.
deleteall – Deletes all the cells in a given row.
scan – Scans and returns the table data.
count – Counts and returns the number of rows in a table.
truncate – Disables, drops, and recreates a specified table.

[Table of Contents](#Hbase)

## What happens when you issue a delete command in HBase?
Once you issue a delete command in HBase for cell, column or column family, it is not deleted instantly. A tombstone marker in inserted. Tombstone is a specified data, which is stored along with standard data. This tombstone makes hides all the deleted data.
The actual data is deleted at the time of major compaction. In Major compaction, HBase merges and recommits the smaller HFiles of a region to a new HFile. In this process, the same column families are placed together in the new HFile. It drops deleted and expired cell in this process. All the results from scan and get filters the deleted cells.

[Table of Contents](#Hbase)

## What are different tombstone markers in HBase?
There are three types of tombstone markers in HBase:
Version Marker: Marks only one version of a column for deletion.
Column Marker: Marks the whole column (i.e. all version) for deletion.
Family Marker: Marks the whole column family (i.e. all the columns in the column family) for deletion

[Table of Contents](#Hbase)

## HBase blocksize is configured on which level?
The blocksize is configured per column family and the default value is 64 KB. This value can be changed as per requirements.

[Table of Contents](#Hbase)

## Which command is used to run HBase Shell?
./bin/hbase shell command is used to run the HBase shell. Execute this command in HBase directory.

[Table of Contents](#Hbase)

## Which command is used to show the current HBase user?
whoami command is used to show HBase user.

[Table of Contents](#Hbase)

## What is the full form of MSLAB?
MSLAB stands for Memstore-Local Allocation Buffer. Whenever a request thread needs to insert data into a MemStore, it doesn’t allocates the space for that data from the heap at large, but rather allocates memory arena dedicated to the target region.

[Table of Contents](#Hbase)

## Define LZO?
Lempel-Ziv-Oberhumer (LZO) is a lossless data compression algorithm that focuses on decompression speed.

[Table of Contents](#Hbase)

## What is HBase Fsck?
HBase comes with a tool called hbck which is implemented by the HBaseFsck class. HBaseFsck (hbck) is a tool for checking for region consistency and table integrity problems and repairing a corrupted HBase. It works in two basic modes – a read-only inconsistency identifying mode and a multi-phase read-write repair mode.

[Table of Contents](#Hbase)

## What is REST?
Rest stands for Representational State Transfer which defines the semantics so that the protocol can be used in a generic way to address remote resources. It also provides support for different message formats, offering many choices for a client application to communicate with the server.

[Table of Contents](#Hbase)

## What is Nagios?
Nagios is a very commonly used support tool for gaining qualitative data regarding cluster status. It polls current metrics on a regular basis and compares them with given thresholds.

[Table of Contents](#Hbase)

## What is the use of ZooKeeper?
The ZooKeeper is used to maintain the configuration information and communication between region servers and clients. It also provides distributed synchronization. It helps in maintaining server state inside the cluster by communicating through sessions.
Every Region Server along with HMaster Server sends continuous heartbeat at regular interval to Zookeeper and it checks which server is alive and available. It also provides server failure notifications so that, recovery measures can be executed.

[Table of Contents](#Hbase)

## Define catalog tables in HBase?
Catalog tables are used to maintain the metadata information.

[Table of Contents](#Hbase)

## Define compaction in HBase?
HBase combines HFiles to reduce the storage and reduce the number of disk seeks needed for a read. This process is called compaction. Compaction chooses some HFiles from a region and combines them. There are two types of compactions.

[Table of Contents](#Hbase)

## Explain what is Hbase?
Hbase is a column-oriented database management system which runs on top of HDFS (Hadoop Distribute File System). Hbase is not a relational data store, and it does not support structured query language like SQL.
In Hbase, a master node regulates the cluster and region servers to store portions of the tables and operates the work on the data.

[Table of Contents](#Hbase)

## Explain why to use Hbase?
High capacity storage system
Distributed design to cater large tables
Column-Oriented Stores
Horizontally Scalable
High performance & Availability
Base goal of Hbase is millions of columns, thousands of versions and billions of rows
Unlike HDFS (Hadoop Distribute File System), it supports random real time CRUD operations

[Table of Contents](#Hbase)

## Mention what are Key Components of Hbase?
Zookeeper: It does the co-ordination work between client and Hbase Maser
Hbase Master: Hbase Master monitors the Region Server
RegionServer: RegionServer monitors the Region
Region: It contains in memory data store(MemStore) and Hfile.
Catalog Tables: Catalog tables consist of ROOT and META

[Table of Contents](#Hbase)

## What is the Role of Master Server in Hbase?
The Master server assigns regions to region servers and handles load balancing in the cluster.

[Table of Contents](#Hbase)

## Explain what does Hbase consists of?
Hbase consists of a set of tables
And each table contains rows and columns like traditional database
Each table must contain an element defined as a Primary Key
Hbase column denotes an attribute of an object

[Table of Contents](#Hbase)

## What is the Role of Zookeeper in Hbase?
The zookeeper maintains configuration information, provides distributed synchronization, and also maintains the communication between clients and region servers.

[Table of Contents](#Hbase)

## Mention how many operational commands in Hbase?
Operational command in Hbases is about five types:
+ Get
+ Put
+ Delete
+ Scan
+ Increment

[Table of Contents](#Hbase)

## When do we need to disable a table in Hbase?
In Hbase a table is disabled to allow it to be modified or change its settings. .When a table is disabled it cannot be accessed through the scan command.

[Table of Contents](#Hbase)

## Explain what is Wal and Hlog in Hbase?
WAL (Write Ahead Log) is similar to MySQL BIN log; it records all the changes occur in data. It is a standard sequence file by Hadoop and it stores HLogkey’s. These keys consist of a sequential number as well as actual data and are used to replay not yet persisted data after a server crash. So, in cash of server failure WAL work as a life-line and retrieves the lost data’s.

[Table of Contents](#Hbase)

## What are the different Types of Filters used in Hbase?
Filters are used to get specific data form a Hbase table rather than all the records.
They are of the following types.
Column Value Filter
Column Value comparators
KeyValue Metadata filters.
RowKey filters.

[Table of Contents](#Hbase)

## In Hbase what is Column Families?
Column families comprise the basic unit of physical storage in Hbase to which features like compressions are applied.

[Table of Contents](#Hbase)

## Name three disadvantages Hbase has as compared to Rdbms?
Hbase does not have in-built authentication/permission mechanism
The indexes can be created only on a key column, but in RDBMS it can be done in any column.
With one HMaster node there is a single point of failure.

[Table of Contents](#Hbase)

## Explain what is the Row Key?
Row key is defined by the application. As the combined key is pre-fixed by the rowkey, it enables the application to define the desired sort order. It also allows logical grouping of cells and make sure that all cells with the same rowkey are co-located on the same server.

[Table of Contents](#Hbase)

## Is Hbase a scale out or scale up process?
Hbase runs on top of Hadoop which is a distributed system. Haddop can only scale uo as and when required by adding more machines on the fly. So Hbase is a scale out process.

[Table of Contents](#Hbase)

## Explain deletion in Hbase?
When you delete the cell in Hbase, the data is not actually deleted but a tombstone marker is set, making the deleted cells invisible. Hbase deleted are actually removed during compactions.
Three types of tombstone markers are there:
+ Version delete marker: For deletion, it marks a single version of a column
+ Column delete marker: For deletion, it marks all the versions of a column
+ Family delete marker: For deletion, it marks of all column for a column family

[Table of Contents](#Hbase)

## What are the step in writing something into Hbase by a Client?
In Hbase the client does not write directly into the HFile. The client first writes to WAL(Write Access Log), which then is accessed by Memdtore. The Memstore Flushes the data into permanent memory from time to time.

[Table of Contents](#Hbase)

## Explain how does Hbase actually delete a Row?
In Hbase, whatever you write will be stored from RAM to disk, these disk writes are immutable barring compaction. During deletion process in Hbase, major compaction process delete marker while minor compactions don’t. In normal deletes, it results in a delete tombstone marker- these delete data they represent are removed during compaction.
Also, if you delete data and add more data, but with an earlier timestamp than the tombstone timestamp, further Gets may be masked by the delete/tombstone marker and hence you will not receive the inserted value until after the major compaction.

[Table of Contents](#Hbase)

## What is compaction in Hbase?
As more and more data is written to Hbase, many HFiles get created. Compaction is the process of merging these HFiles to one file and after the merged file is created successfully, discard the old file.

[Table of Contents](#Hbase)

## Explain what happens if you alter the Block Size of a column Family on an already occupied Database?
When you alter the block size of the column family, the new data occupies the new block size while the old data remains within the old block size. During data compaction, old data will take the new block size. New files as they are flushed, have a new block size whereas existing data will continue to be read correctly. All data should be transformed to the new block size, after the next major compaction.

[Table of Contents](#Hbase)

## What are the different compaction types in Hbase?
There are two types of compaction. Major and Minor compaction. In minor compaction, the adjacent small HFiles are merged to create a single HFile without removing the deleted HFiles. Files to be merged are chosen randomly.
In Major compaction, all the HFiles of a column are emerged and a single HFiles is created. The delted HFiles are discarded and it is generally triggered manually.

[Table of Contents](#Hbase)

## What is a Cell in Hbase?
A cell in Hbase is the smallest unit of a Hbase table which holds a piece of data in the form of a tuple{row,column,version}

[Table of Contents](#Hbase)

## What is the Scope of a Rowkey in Hbase?
Rowkeys are scoped to ColumnFamilies. The same rowkey could exist in each ColumnFamily that exists in a table without collision.

[Table of Contents](#Hbase)

## What is the Role of the Class Hcolumndescriptor in Hbase?
This class is used to store information about a column family such as the number of versions, compression settings, etc. It is used as input when creating a table or adding a column.

[Table of Contents](#Hbase)

## What is a Namespace in Hbase?
A Namespace is a logical grouping of tables . It is similar to a database object in a Relational database system.

[Table of Contents](#Hbase)

## What is the Lower Bound of Versions in Hbase?
The lower bound of versions indicates the minimum number of versions to be stored in Hbase for a column. For example If the value is set to 3 then three latest version wil be maintained and the older ones will be removed.

[Table of Contents](#Hbase)

## What is Hotspotting in Hbase?
Hotspotting is a situation when a large amount of client traffic is directed at one node, or only a few nodes, of a cluster. This traffic may represent reads, writes, or other operations. This traffic overwhelms the single machine responsible for hosting that region, causing performance degradation and potentially leading to region unavailability.

[Table of Contents](#Hbase)

## What is Ttl in Hbase?
TTL is a data retention technique using which the version of a cell can be preserved till a specific time period.Once that timestamp is reached the specific version will be removed.

[Table of Contents](#Hbase)

## Why do we Pre create empty Regions?
Tables in HBase are initially created with one region by default. Then for bulk imports, all clients will write to the same region until it is large enough to split and become distributed across the cluster. So empty regions are created to make this process faster.

[Table of Contents](#Hbase)

## Does Hbase support Table Joins?
Hbase does not support table joins. But using a mapreduce job we can specify join queries to retrieve data from multiple Hbase tables.

[Table of Contents](#Hbase)

## Which File in Hbase is designed after Sstable File of Bigtable?
The HFile in Habse which stores the Actual data(not metadata) is designed after the SSTable file of BigTable.

[Table of Contents](#Hbase)

## What is a Hbase Store?
Hbase Store hosts a MemStore and 0 or more StoreFiles (HFiles). A Store corresponds to a column family for a table for a given region.

[Table of Contents](#Hbase)

## What are the Two Types of Table Design Approach in Hbase?
They are:
Short and Wide
Tall and Thin

[Table of Contents](#Hbase)

## When do we do Manual Region Splitting?
The manual region splitting is done we have an unexpected hotspot in your table because of many clients querying the same table.

[Table of Contents](#Hbase)

## In which scenario should we consider creating a short and wide Hbase Table?
The short and wide table design is considered when there is
There is a small number of columns
There is a large number of rows

[Table of Contents](#Hbase)

## In Hbase what is Log Splitting?
When a region is edited, the edits in the WAL file which belong to that region need to be replayed. Therefore, edits in the WAL file must be grouped by region so that particular sets can be replayed to regenerate the data in a particular region. The process of grouping the WAL edits by region is called log splitting.

[Table of Contents](#Hbase)

## How does Hbase support Bulk Data Loading?
There are two main steps to do a data bulk load in Hbase:
Generate Hbase data file(StoreFile) using a custom mapreduce job) from the data source. The StoreFile is created in Hbase internal format which can be efficiently loaded.
The prepared file is imported using another tool like comletebulkload to import data into a running cluster. Each file gets loaded to one specific region.

[Table of Contents](#Hbase)

## Why Multiwal is Needed?
With a single WAL per RegionServer, the RegionServer must write to the WAL serially, because HDFS files must be sequential. This causes the WAL to be a performance bottleneck.

[Table of Contents](#Hbase)

## How does Hbase provide High Availability?
Hbase uses a feature called region replication. In this feature for each region of a table, there will be multiple replicas that are opened in different RegionServers. The Load Balancer ensures that the region replicas are not co-hosted in the same region servers.

[Table of Contents](#Hbase)

## How does Wal help when a Regionserver Crashes?
The Write Ahead Log (WAL) records all changes to data in HBase, to file-based storage. if a RegionServer crashes or becomes unavailable before the MemStore is flushed, the WAL ensures that the changes to the data can be replayed.

[Table of Contents](#Hbase)

## What is Hregionserver in Hbase?
HRegionServer is the RegionServer implementation. It is responsible for serving and managing regions. In a distributed cluster, a RegionServer runs on a DataNode.

[Table of Contents](#Hbase)

## What are the different Block Caches in Hbase?
HBase provides two different BlockCache implementations: the default on-heap LruBlockCache and the BucketCache, which is (usually) off-heap.

[Table of Contents](#Hbase)