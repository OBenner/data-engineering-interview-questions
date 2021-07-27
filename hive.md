How will you improve the performance of a program in Hive?
There are many ways to improve the performance of a Hive program. Some of these are as follows:
Data Structure: We have to select the right data structure for our purpose in a Hive program.
Standard	Library: Wherever possible, we should use methods from standard library. Methods implemented in standard library have much better performance than user implementation.
Abstraction: At times, a lot of abstraction and indirection can cause slow performance of a program. We should remove the redundant abstraction in code.
Algorithm: Use of right algorithm can make a big difference in a program. We have to find and select the suitable algorithm to solve our problem with high performance.

Can we use Hive for Online Transaction Processing (OLTP) systems?
No, Hive is not suitable for OLTP systems. It does not support insert and update at each row level. In OLTP systems, we have to update each order or each row.

How will you change the data type of a column in Hive?
We can use Alter statement to change the data type of a column in Hive.
Command will be as follows:
ALTER TABLE tableName REPLACE	COLUMNS
(columnName dataType)

What is Metastore in Hive?
Hive table definitions, mappings and other metadata are stored in Metastore. This can be stored in a RDBMS supported by JPOX. By default only one user can see Metastore at a time. Metastore has two parts.
Metastore Service: This service provides interface between Hive and users/processed.
Metastore Database: This database stores table definitions, data mappings etc.
In default configuration, Hive Metastore is stored in same JVM as Hive driver. This is also known as Embedded Metastore, which is good for Dev and Testing environments. We can also use an external DB like MySQL for storing Metadata. This configuration is called Local Metastore.

What is SerDe in Hive?
SerDe is a short name for Serializer/Deserializer. In Hive, SerDe is used for input/output interface. For any communication we have to Serialize and Deserialize the data.

With SerDe, Hive can read data from a table and write it to HDFS in a custom format. We can also implement custom SerDe to handle our own data formats. During map and reduce, Hive can use serialize methods of LazyBinarySerDe	and BinarySortableSerDe. We can also use ObjectInspector, for a SerDe to serialize an object created by another SerDe.

What are the components in Hive data model?
There are following components in Hive data model:
Tables: These are tables similar to Relation Database (RDBMS). We can create filters on tables. We can run joins and union on tables. Table data is stored in HDFS. Rows in a table are organized like columns in a RDBMS. Each row can have a datatype.
Partitions: In each table in Hive, we can specify partition keys that determine how the data is stored. With partition we can optimize the queries to only looks specific dataset instead of scanning whole table.
Buckets: In each partition, we can divide the data into buckets. Each bucket is based on the hash of a column in a table. There is a separate file in which each bucket of a partition is stored. With buckets it is efficient to evaluate queries based on a sample of data.

57. What are the different modes in which we can run Hive?
    We can run Hive in following modes: Local mode: In Hive local mode, Map Reduce jobs related to Hive run locally on a user machine. This is the default mode in which Hadoop uses local file system.
    Distributed Mode: In this mode, Hive as well as Hadoop is running in a fully distributed	mode. NameNode, DataNode, JobTracker, TaskTracker etc run on different machines in this mode.
    Pseudo-distributed Mode: This is the mode used by developers to test the code before deploying to production. In this mode, all the daemons run on same virtual machine. With this mode, we can quickly write scripts and test on limited data sets.

58. What are the main components of Hive?
    Main components of Hive are as follows:
    Hive Driver: Hive Driver receives queries from users. It handles sessions and provides commands to execute and fetch APIs that are similar to JDBC/ODBC interface.
    Metastore: All the Metadata information about Hive tables and partitions is stored in Metastore. It also maintains information about columns and column types. It knows about the serializers and deserializers that are used in reading and writing data to corresponding HDFS files.
    Hive Compiler: The compiler in Hive parses queries and performs semantic analysis on different query blocks and query expressions. It also generates the execution plan for looking up data from tables and partitions.

    Execution Engine: This is the Hive component that executes the execution plan created by compiler. The Execution engine manages the dependencies between different stages of the execution plan. It executes different stages of Execution plan on the relevant system components.
    User Interface (UI): Hive provides a UI for users to interact with the system. Users can submit queries and execute other operations on the system.

What is the use of Hive in Hadoop eco-system?
Hive provides a SQL like interface to interact with data stored in Hadoop eco-system. We can create tables in Hive and store data into them. Hive is also used for mapping and working with HBase tables. Under the hood, Hive queries are converted into MapReduce jobs. So Hive hides the complexity associated with creating and running of MapReduce jobs.

What Collection/Complex data types are supported by Hive?
Hive supports following Complex/Collection data types:
Map: This is a collection of key value pairs. We can specify [key] to get the value stored at key in the collection.
Array: This is an index based ordered sequence of values in a collection. We can access it with an index like [i] where i is the location of an element.
Struct: This is a record type that has other named fields inside. It is similar to struct in C or object in Java.
Uniontype: This is similar to Union in C. Since support for this data type is not fully available, we should not use it.

What is the use of .hiverc file in Hive?
In Hive, .hiverc is the initialization file. This file is loaded when we start Command Line Interface for Hive. We can set the initial values of parameters in this file.

How will you run Unix commands from Hive?
We can run Unix commands from Hive shell by using ! sign. We have to append ! sign before a unix command. E.g. For using date command we have to run it as !date in Hive shell.

What is the purpose of USE command in Hive?
In Hive we have to call USE command before running and hive queries. USE command sets the current database on which query statements will be executed. We can call USE default to set the database to default database. Or we can call USE database_name to set the database on which we want to run the queries.


What is the precedence order in Hive configuration?
In Hive we can use following precedence order to set the configurable properties.
Hive SET command has the highest priority
-hiveconf option from Hive Command Line
hive-site.xml file
hive-default.xml file
hadoop-site.xml file
hadoop-default.xml file

How will you display header row with the results of a Hive query?
Hive provides a property hive.cli.print.header to set the configuration in which header row is printed. It is as follows:
hive>	set hive.cli.print.header=true;

Can we create multiple tables in Hive for a data file?
Yes, we can create multiple table schemas for a data file. Hive will save schema in Hive Metastore. Data will remain in same file. Based on the schema we can retrieve different results from same Data.

How does CONCAT function work in Hive?
Hive provides CONCAT function to concatenate the input strings. We can specify multiple strings in a comma-separated list. here is another function CONCAT_WS in Hive that can be used to specify the custom delimiter.

How will you change settings of a Hive session?
We can use SET command to change the settings within a Hive Session. We can even change the settings of MapReduce job with SET command. If we just call SET command with a property name, we will get the current value of the property.
With SET -v we get the list of all the properties including Hadoop default in Hive system.

How will you rename a table in Hive without using ALTER command?
We can use IMPORT/EXPORT statements to rename a table in Hive. We first export the original table to a location by EXPORT statement.
hive>	EXPORT	TABLE tableName	TO ’TEMP_LOCATION’
Then we create new table with IMPORT statement.

hive>	IMPORT	TABLE newTableName	FROM ’TEMP_LOCATION’

What is the difference between SORT BY and ORDER BY in Hive?
In Hive we use, SORT BY to sort data in each Reducer. We can use multiple Reducers in SORT BY clause.
We can use ORDER BY to sort all the data that passes through one Reducer. So ORDER BY option can be use only with one Reducer.
ORDER BY guarantees total order in the output. SORT BY guarantees ordering only within the data of one reducer.

What is the use of strict mode in Hive?
We use strict mode in Hive to avoid performing full scan of a table in a query. It is very useful when we have a very large table. We	can	use	‘set hive.mapred.mode=strict’ command to put Hive into strict mode. In this mode, any query that needs full table scan will throw error to user. Strict mode is a useful option in Hive to improve performance and avoid any unexpected delays due to full table scan.

What is the use of IF EXISTS clause in Hive statements?
We use IF EXISTS clause in DROP TABLE statement. When we drop a table, there can be a case that table does not exist. In such a case DROP statement will give error. In case we are not sure if the table exists or not in Hive, we use DROP TABLE IF EXISTS tableName statement to drop a table. This statement will not give error in case table does not exist.

What is the use of PURGE in DROP statement of Hive?
We use PURGE option when we are absolutely sure to delete the data of a table. With DROP TABLE tableName PURGE statement, table data will not go to trash folder. So it cannot be retrieved in case of an accidental DROP statement.

What are the main limitations of Apache Hive?
Apache Hive is a popular tool in Hadoop eco-system. Some of the limitations of Hive are as follows:
OLTP: Hive cannot be used for OLTP applications, since it does not support record level update, insert statements.
Data Warehouse: Hive is more suitable for data warehouse	applications	on Big Data.
Latency: Hive queries have higher latency than SQL due to time overhead during start-up.
Batch Oriented: Hive is mostly used in Batch- oriented use cases.
OLAP: For Online Analytic Processing (OLAP) we can use Hive. We can use HBase also for OLAP processing.


What is the difference between HBase and Hive?
HBase is a NoSQL database. It supports update, insert and delete statements at record level. HBase does not support a query language like SQL. But we can use Hive with HBase for querying purpose. Hive runs on MapReduce. HBase runs on HDFS. Apache Hive is a data warehousing and data analytics framework that is used for data warehouse applications. HBase is a NoSQL database on top of HDFS.

What is ObjectInspector in Hive?
ObjectInspector is used in Hive to look into the internal structure of a complex object. It is an interface that is implemented by classes like StandardListObjectInspector, StandardMapObjectInspector, StandardSetObjectInspector etc. Main use of ObjectInspector is in SerDe package for Serialization and Deserialization. We have to make sure that hashCode() and equals() methods of Object class work for ObjectInspector as well.

What are the main components of Query Processor in Apache Hive?
The main components of Apache Hive Query Processor are as follows:
Parse and SemanticAnalysis (ql/parse)
Optimizer (ql/optimizer) Plan Components (ql/plan) MetaData	Layer (ql/metadata)
Map/Reduce	Execution Engine (ql/exec)
Sessions (ql/session)
Type interfaces (ql/typeinfo) Hive	Function	Framework (ql/udf)
Tools (ql/tools)

How will you resolve an out of memory error while running a JOIN query?
In case of JOIN query with large tables, we have a lot of data in memory. This can cause out of memory error.One simple solution for handling this error is to change the RIGHT OUTER JOIN to LEFT OUTER
JOIN. We should try to put the table with a large number of rows on the rightmost side in a JOIN query.

What are the different SerDe implementations in Hive?
There are many implementations of SerDe in Hive. We can also write our own custom SerDe implementation. Some of the popular implementations are as follows:
ByteStreamTypedSerDe RegexSerDe OpenCSVSerde DelimitedJSONSerDe

What is the use of HCatalog?
Hadoop provides a table and storage management layer called HCatalog. With HCatalog users in Hive can use different data processing tools like- Pig, MapReduce, Hive, Streaming etc to read and write data on the grid. With HCatalog we can read and write files in any format for which SerDe is available. Default options supported by HCatalog are: RCFile, CSV, JSON and SequenceFile. In HCatalog we can see the data in a relational view.

What is the Data Model of HCatalog?
HCatalog has same datatypes as Hive. We can create tables in HCatalog to store data. These tables can be placed in a Database. We can also partition HCatalog tables based on a Hash. There are multiple dimensions in a HCatalog partition. There are records in a partition. Once a partition is created, we cannot add or remove records into it. Records are divided into columns. Each column has a name and a datatype. Overall, HCatalog data model is similar to Relational Data Model.

What is RLIKE operator in Hive?
RLIKE is an operator similar to LIKE in SQL. We use LIKE to search for string with similar text.
E.g. user_name LIKE ‘%Smith’
Hive provides RLIKE operator that can be used for searching advanced Regular Expressions in Java.
E.g.	user_name	RLIKE	‘.* (Smith|Sam).*’  This will return user_name that has Smith or Sam in it.

Can we use same name for a TABLE and VIEW in Hive?
No, we cannot use same name for a table and view in Hive. So we have to select a unique name for a view in Hive.

How will you load data into a VIEW in Hive?
This is a trick question. We cannot use VIEW in Hive INSERT or LOAD statement. We can only load data into a Hive table.

What is Bucketing in Hive?
With Bucketing in Hive, we can divide datasets into manageable parts. It is similar to hashing. Even if the size of data set varies, we can still have fixed number of buckets. Also with bucketing we can do map-side joins in Hive. E.g. Let say we have a table with date as a first level partition and user_id as second level partition. The date may have smaller number of partitions. But user_id may have a large number of partitions. If we have millions of users, there will be millions of second level partitions and files. To avoid creating so many partitions, we can do bucketing instead of partitioning on user_id. With bucketing, we can use HASH function to put different user_ids in different buckets. We can create a manageable number of buckets for user_id values.

What are the pros and cons of archiving a partition in Hive?
We can archive some less used partitions in Hive. The main advantage of archiving is that it will decrease the number of files to be stored in NameNode. We can even query an archived partition in Hive. The main disadvantage of archiving is that queries become slower and less efficient in Hive.
What are the table generating functions in Hive?
Table generating functions in Hive are user-defined functions like CONCAT that take a single row and give an output of multiple rows.Some of the Table generating functions are:
EXPLODE(array) EXPLODE(map) STACK() JSON_TUPLE()

How can we specify in Hive to load an HDFS file in LOAD DATA?
We have to remove the LOCAL clause from LOAD DATA statement to avoid loading the local file. Once LOCAL clause is removed, we can load HDFS file.

What is a Skewed table in Hive?
A Skewed tables is a special type of table in which some values in a column appear more often. Due to this the distribution in skewed. In Hive, when we specify a table as SKEWED during creation, then skewed values are written into separate files and remaining values go to another file.
E.g. CREATE TABLE tableName (column1 STRING, column2 STRING)  SKEWED  BY (column1) on (‘value1’)
During queries, we get better performance in Hive with SKEWED tables.

What is the use of CLUSTERED BY clause during table creation in Hive?
CLUSTERED BY in Hive is same as DISTRIBUTE BY and SORT BY. When we specify CLUSTERED BY, it will first distribute the data into different reducers by using a Hash. Once data is distributed, it will sort the data.
We have to specify CLUSTERED BY clause during table creation. But it is useful in querying of data in Hive.

What is a Managed table in Hive?
Managed tables are the tables in which files, metadata and statistics etc are managed by internal Hive processes. Hive creates Managed tables by default. When we drop a managed table or partition, then all the metadata and data associated with the table is also deleted. We use Managed tables, when we want Hive to manage the lifecycle of a table. Even for temporary tables, we use managed tables in Hive.
When we run DESCRIBE FORMATTED	tableName statement, it displays whether a table is MANAGED_TABLE or EXTERNAL_TABLE.

How will you prevent data to be dropped or queried from a partition in Hive?
We can use ALTER TABLE table_name ENABLE NO_DROP to prevent a table partition from being dropped. We can use ALTER TABLE table_name ENABLE OFFLINE to prevent a table partition frombeing queried. In offline mode, we can still access metadata of a table partition.



What is the use of TOUCH in ALTER statement?
In Hive, TOUCH clause in ALTER statement is used to read the metadata and write it back. This operation will modify the last accessed time of a partition in Hive. With TOUCH statement we can also execute the POST and PRE hooks on a table partition. This statement cannot be used for creating a table or partition if it does not exist yet.

How does OVERWRITE clause work in CREATE TABLE statement in Hive?
We use OVERWRITE clause in CREATE TABLE statement to delete the existing data and write new data in a Hive table. Essentially, as the name suggests, OVERWRITE helps in overwriting existing data in a Hive table.

What are the options to connect an application to a Hive server?
We can use following options to connect an application a Hive server:
JDBC Driver: We can use JDBC Driver with embedded as well as remote access to connect to HiveServer. This is for Java based connectivity.
Python Client: For Python language application there is Python client that can connect to Hive server.
Ruby Client: With Ruby client driver also we can connect to Hive server.
Thrift Client: We can use Beeline command line shell to connect to Hive server over Thrift. For production mode, this is one of the very good options. It is a secure option for production use. Also we do not need to grant HDFS access to users for using Thrift client.

How TRIM and RPAD functions work in Hive?
TRIM and RPAD functions are for processing String data type in Hive. With TRIM function we can delete the spaces before and after a String. It is very useful for formatting user input in which user may have entered extra spaces. The other variations of TRIM function are LTRIM and RTRIM that remove spaces from left and right side of the string respectively. E.g. TRIM(‘ Smith ’) Smith RPAD function is used to add padding (extra spaces) in a String on the right hand side. So that String reaches a specified length. LPAD function is same as RPAD but it pads on the left hand side of String.
E.g. Let say we have a String “Hello”.LPAD(‘Hello’,8,’ ')
Hello
We can also specify our optional padding character in RPAD and LPAD functions. These functions are similar to the ones in SQL.

How will you recursively access sub-directories in Hive?
We can use following commands in Hive to recursively access sub- directories:
hive>	Set mapred.input.dir.recursive=true;
hive>	Set hive.mapred.supports.subdirectories=true
Once above options are set to true, Hive will recursively access sub- directories of a directory in MapReduce.

What is the optimization that can be done in SELECT * query in Hive?
We can convert some of the SELECT queries in Hive into single FETCH task. With this optimization, latency of SELECT query is decreased. To use this we have to set the value of	hive.fetch.task.conversion parameter. The permissible values are:
0: It means FETCH is disabled.
1: It is minimal mode. SELECT *, FILTER on
partition columns (WHERE and HAVING clauses), LIMIT only
2: It is more mode: SELECT, FILTER,      LIMIT      only
(including virtual columns) "more"	can	even	take	UDF expressions in the SELECT clause.

What is the use of ORC format tables in Hive?
We use Optimized Row Columnar (ORC) file format to store data efficiently in Hive. It is used for performance improvement in reading, writing and processing of data. In ORC format, we can overcome the limitations of other Hive file formats. Some of the advantages of ORC format are: There is single file as the output of each task. This reduces load on NameNode.
It supports date time, decimal, struct, map etc complex types. It stores light-weight indexes within the file. We can bound the memory used in read/write of data. It stores metadata with Protocol Buffers that supports add/remove of fields.

What are the main use cases for using Hive?
Hive is mainly used for Datawarehouse applications. Hive used Hadoop and MapReduce that put some restrictions on use cases for Hive. Some of the  main use cases for Hive are:
Analysis of static Big data Applications in which less responsive time is acceptable Analysis of data that does not hange rapidly
What is STREAMTABLE in Hive?
In Hive, we can optimize a query by using STREAMTABLE hint. We can specify it in SELECT query with JOIN. During the map/reduce stage of JOIN, a table data can be streamed by using this hint.
E.g. SELECT	/*+ STREAMTABLE(table1)	*/ table1.val, table2.val FROM table1	JOIN table2	ON (table1.key = table2.key1)
In above query we are using table1 as a stream. If we do not use STREAMTABLE hint then Hive will stream the right most table in the JOIN query.
 
