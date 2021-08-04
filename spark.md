What are the main features of Apache Spark?
Main features of Apache Spark are as follows:
+ Performance: The key feature of Apache Spark is its Performance. With Apache Spark we can run programs up to 100 times faster than Hadoop MapReduce in memory. On disk we can run it 10 times faster than Hadoop.
+ Ease of Use: Spark supports Java, Python, R, Scala etc. languages. So it makes it much easier to develop applications for Apache Spark.
+ Integrated Solution: In Spark we can create an integrated solution that combines the power of SQL, Streaming and data analytics.
R+ un Everywhere: Apache Spark can run on many platforms. It can run on Hadoop, Mesos, in Cloud or standalone. It can also connect to many data sources like HDFS, Cassandra, HBase, S3 etc.
+ Stream Processing: Apache Spark also supports real time stream processing. With real time streaming we can provide real time analytics solutions. This is very useful for real-time data.

What is a Resilient Distribution Dataset in Apache Spark?
Resilient Distribution Dataset (RDD) is an abstraction of data in Apache Spark. It is a distributed and resilient collection of records spread over many partitions. RDD hides the data partitioning and distribution behind the scenes. Main	features of RDD 	are as follows:
+ Distributed: Data in a RDD is distributed across multiple nodes.
+ Resilient: RDD is a fault- tolerant dataset. In case of node failure, Spark can re- compute data.
+ Dataset: It is a collection of data similar to collections in Scala.
+ Immutable: Data in RDD cannot be modified after creation. But we can transform it using a Transformation.

What is a Transformation in Apache Spark?
Transformation in Apache Spark is a function that can be applied to a RDD. Output of a Transformation is another RDD. Transformation in Spark is a lazy operation. It means it is not executed immediately. Once we call an action, transformation is executed. A Transformation does not change the input RDD. We can also create a pipeline of certain Transformations to create a Data flow.

What are security options in Apache Spark?
Apache Spark provides following security options:
Encryption: Apache Spark supports encryption by SSL. We can use HTTPS protocol for secure data transfer. Therefore data is transmitted in encrypted mode. We can use spark.ssl parameters to set the SSL configuration.

Authentication: We can perform authentication by a shared secret in Apache Spark. We can use spark.authenticate	to configure authentication in Spark.
Event Logging: If we use Event Logging, then we can set the permissions on the directory where event logs are	stored.	These permissions can ensure access control for Event log.

How will you monitor Apache Spark?
We can use the Web UI provided by SparkContext to monitor Spark. We can access this Web UI at port 4040 to get the useful information. Some of the information that we can monitor is:
+ Scheduler tasks and stages RDD	Sizes	and	Memory usage Spark	Environment Information
+ Executors Information
+ Spark also provides a Metrics library. This library can be used to send Spark information to HTTP, JMX, CSV files etc.This is another option to collect Spark runtime information for monitoring another dashboard tool.

What are the main libraries of Apache Spark?
Main libraries of Apache Spark are as follows:
+ MLib: This is Spark’s Machine Learning library. We can use it to create scalable machine learning system. We can use various machine learning algorithms as well as features like pipelining etc with this library.
+ GraphX: This library is used for computation of Graphs. It helps in creating a Graph abstraction of data and then use various Graph operators like- SubGraph, joinVertices etc.
+ Structured Streaming: This library is used for handling streams in Spark. It is a fault tolerant system built on top of Spark SQL Engine to process streams.
+ Spark SQL: This is another popular component that is used	for	processing	SQL queries on Spark platform.
+ SparkR: This is a package in Spark to use Spark from R language. We can use R data frames, dplyr etc from this package. We can also start SparkR from RStudio.

What are the main functions of Spark Core in Apache Spark?
Spark Core is the central component of Apache Spark. It serves following functions:
+ Distributed Task Dispatching
+ Job Scheduling
+ I/O Functions

How will you do memory tuning in Spark?
In case of memory tuning we have to take care of these points.
Amount of memory used by objects Cost of accessing objects Overhead	of Garbage Collection
Apache Spark stores objects in memory for caching. So it becomes important to perform memory tuning in a Spark application. First we determine the memory usage by the application. To do this we first create a RDD and put it in cache. Now we can see the size of the RDD in storage page of Web UI. This will tell the amount of memory consumed by RDD. Based on the memory usage, we can estimate the amount of memory needed for our task. In case we need tuning, we can follow these practices to reduce memory usage:
Use data structures like Array of objects or primitives instead of Linked list or HashMap. Fastutil library provides convenient collection classes for primitive types compatible with Java.
We have to reduce the usage of nested data structures with a large number of small objects and pointes. E.g. Linked list has pointers within each node.
It is a good practice to use numeric IDs instead of Strings for keys.
We can also use JVM flag - XX:+UseCompressedOops to	make pointers be four bytes instead of eight.

What are the two ways to create RDD in Spark?
We can create RDD in Spark in following two ways:
+ Internal: We can parallelize an existing collection of data within our Spark Driver program and create a RDD out of it.
+ External: We can also create RDD by referencing a Dataset in an external data source like AWS S3, HDFS, HBASE etc.

111.	What are the main operations that can be done on a RDD in Apache Spark?
        There are two main operations that can be performed on a RDD in Spark:
        Transformation: This is a function that is used to create a new RDD out of an existing RDD.
        Action: This is a function that returns a value to Driver program after running a computation on RDD.

112.	What are the common Transformations in Apache Spark?
        Some of the common transformations in Apache Spark are as follows:
        Map(func): This is a basic transformation that returns a new dataset by passing each element of input dataset through func function.
        Filter(func):	This transformation returns a new dataset of elements that return true for func function. It is used to filter elements in a dataset based on criteria in func function.
        Union(other Dataset): This is used to combine a dataset with another dataset to form a union of two datasets.

Intersection(other Dataset):	This
transformation gives the elements common to two datasets.
Pipe(command, [envVars]): This transformation passes each partition of the dataset through a shell command.

113. What are the common Actions in Apache Spark?
     Some of the commonly used Actions in Apache Spark are as follows:
     Reduce(func): This Action aggregates the elements of a dataset by using func function.
     Count(): This action gives the total number of elements in a Dataset.
     Collect(): This action will return all the elements of a dataset as an Array to the driver program.
     First(): This action gives the first element of a collection.
     Take(n): This action gives the first n elements of dataset.
     Foreach(func): This action runs each element in dataset through a for loop and executes function func on each element.

What is a Shuffle operation in Spark?
Shuffle operation is used in Spark to re-distribute data across multiple partitions. It is a costly and complex operation. In general a single task in Spark operates on elements in one partition. To execute shuffle, we have to run an operation on all elements of all partitions. It is also called all-to-all operation.

What are the operations that can cause a shuffle in Spark?
Some of the common operations that can cause a shuffle internally in Spark are as follows:
Repartition
Coalesce
GroupByKey
ReduceByKey
Cogroup
Join

What is purpose of Spark SQL?
Spark SQL is used for running SQL queries. We can use Spark SQL to interact with SQL as well as Dataset API in Spark. During execution, Spark SQL uses same computation engine for SQL as well as Dataset API. With Spark SQL we can get more information about the structure of data as well as computation being performed. We can also use Spark SQL to read data from an existing Hive installation. Spark SQL can also be accessed by using JDBC/ODBC API as well as command line.
What is a DataFrame in Spark SQL?
A DataFrame in SparkSQL is a Dataset organized into names columns. It is conceptually like a table in SQL.In Java and Scala, a DataFrame is a represented by a DataSet of rows. We can create a DataFrame from an existing RDD, a Hive table or from other Spark data sources.

What is a Parquet file in Spark?
Apache Parquet is a columnar storage format that is available to any project in Hadoop ecosystem. Any data processing framework, data model or programming language can use it. It is a compressed, efficient and encoding format common to Hadoop system projects. Spark SQL supports both reading and writing of parquet files. Parquet files also automatically preserves the schema of the original data. During write operations, by default all columns in a parquet file are converted to nullable column.

What is the difference between Apache Spark and Apache Hadoop MapReduce?
Some of the main differences between Apache Spark and Hadoop MapReduce are follows:
Speed: Apache Spark is 10X to 100X faster than Hadoop due to its usage of in memory processing.
Memory: Apache Spark stores data in memory, whereas	Hadoop MapReduce stores data in hard disk.
RDD: Spark uses Resilient Distributed Dataset (RDD) that guarantee fault tolerance. Where Apache Hadoop uses replication of data in multiple copies to achieve fault tolerance.
Streaming: Apache Spark supports Streaming with very less administration. This makes it much easier to use than Hadoop for real-time stream processing.
API: Spark provides a versatile API that can be used with multiple data sources as well as languages. It is more extensible than the API provided by Apache Hadoop.

120.	What are the main languages supported by Apache Spark?
        Some of the main languages supported by Apache Spark are as follows:
        Java: We can use JavaSparkContext object to work with Java in Spark.
        Scala: To use Scala with Spark, we have to create SparkContext	object	in Scala.
        Python: We also used SparkContext to work with Python in Spark.
        R: We can use SparkR module to work with R language in Spark ecosystem.
        SQL: We can also SparkSQL to work with SQL language in Spark.

121.	What are the file systems supported by Spark?
        Some of the popular file systems supported by Apache Spark are as follows:
        HDFS
        S3
        Local File System
        Cassandra
        OpenStack Swift
        MapR File System

What is a Spark Driver?
Spark Driver is a program that runs on the master node machine. It takes care of declaring any operation- Transformation or Action on a RDD. With Spark Driver was can keep track of all the operations on a Dataset. It can also be used to rebuild a RDD in Spark.

What is an RDD Lineage?
Resilient Distributed Dataset (RDD) Lineage is a graph of all the parent RDD of a RDD. Since Spark does not replicate data, it is possible to lose some data. In case some Dataset is lost, it is possible to use RDD Lineage to recreate the lost Dataset. Therefore RDD Lineage provides solution for better performance of Spark as well as it helps in building a resilient system.

What are the two main types of Vector in Spark?
There are two main types of Vector in Spark:
Dense Vector: A dense vector is backed by an array of double data type. This array contains the values.
E.g. {1.0 , 0.0, 3.0} Sparse Vector: A sparse vector is backed by two parallel arrays. One
array is for indices and the other array is for values. E.g. {3, [0,2], [1.0,3.0]} In this array, the first element is the number of elements in vector. Second element is the array of indices of non-zero values. Third element is the array of non-zero values.

What are the different deployment modes of Apache Spark?
Some of the popular deployment modes of Apache Spark are as follows:
Amazon EC2: We can use AWS cloud product Elastic Compute Cloud (EC2) to deploy and run a Spark cluster.
Mesos: We can deploy a Spark application in a private cluster by using Apache Mesos.
YARN: We can also deploy Spark on Apache YARN (Hadoop NextGen)
Standalone: This is the mode in which we can start Spark by hand. We can launch standalone cluster manually.



What is lazy evaluation in Apache Spark?
Apache Spark uses lazy evaluation as a performance optimization technique. In Laze evaluation as transformation is not applied immediately to a RDD. Spark records the transformations that have to be applied to a RDD. Once an Action is called, Spark executes all the transformations. Since Spark does not perform immediate execution based on transformation, it is	called lazy evaluation.

What are the core components of a distributed application in Apache Spark?
Core components of a distributed application in Apache Spark are as follows:
Cluster Manager: This is the component responsible for launching executors and drivers on multiple nodes. We can use different types of cluster managers based on our requirements. Some of the common types are Standalone, YARN, Mesos etc.
Driver: This is the main program in Spark that runs the main() function of an application. A Driver program creates the SparkConetxt.	Driver program listens and accepts incoming connections from its executors. Driver program can schedule tasks on the cluster. It runs closer to worker nodes.
Executor: This is a process on worker node. It is launched on the node to run an application. It can run tasks and use data in memory or disk storage to perform the task.

What is the difference in cache() and persist() methods in Apache Spark?
Both cache() and persist() functions are used for persisting a RDD in memory across operations. The key difference between persist() and cache() is that in persist() we can specify the Storage level that we select for persisting. Where as in cache(), default strategy is used for persisting. The default storage strategy is MEMORY_ONLY.
How will you remove data from cache in Apache Spark?
In general, Apache Spark automatically removes the unused objects from cache. It uses Least Recently Used (LRU) algorithm to drop old partitions. There are automatic monitoring mechanisms in Spark to monitor cache usage on each node. In case   we   want   to   forcibly remove an object from cache in Apache Spark, we can use RDD.unpersist() method.

What is the use of SparkContext in Apache Spark?
SparkContext is the central object in Spark that coordinates different Spark applications in a cluster. In a cluster we can use SparkContext to connect to multiple Cluster Managers that allocate resources to multiple applications. For any Spark program we first create SparkContext object. We can access a cluster by using this object. To create a SparkContext object, we first create a SparkConf object. This object contains the configuration information of our application. In Spark Shell, by default we get a SparkContext for the shell.

Do we need HDFS for running Spark application?
This is a trick question. Spark supports multiple file-systems. Spark supports HDFS, HBase, local file system, S3, Cassandra etc. So HDFS is not the only file system for running Spark application.

What is Spark Streaming?
Spark Streaming is a very popular feature of Spark for processing live streams with a large amount of data. Spark Streaming uses Spark API to create a highly scalable, high throughput and fault tolerant system to handle live data streams. Spark Streaming supports ingestion of data from popular sources like- Kafka, Kinesis, Flume etc. We can apply popular functions like map, reduce, join etc on data processed through Spark Streams. The processed data can be written to a file system or sent to databases and live dashboards.

How does Spark Streaming work internally?
Spark Streams listen to live data streams from various sources. On receiving data, it is divided into small batches that can be handled by Spark engine. These small batches of data are processed by Spark Engine to generate another output stream of resultant data. Internally, Spark uses an abstraction called DStream or discretized stream. A DStream is a continuous stream of data. We can create DStream from Kafka, Flume, Kinesis etc. A DStream is nothing but a sequence of RDDs in Spark. We can apply transformations and actions on this sequence of RDDs to create further RDDs.

What is a Pipeline in Apache Spark?
Pipeline is a concept from Machine learning. It is a sequence of algorithms that are executed for processing and learning from data. Pipeline is similar to a workflow. There can be one or more stages in a Pipeline.

How does Pipeline work in Apache Spark?
A Pipeline is a sequence of stages. Each stage in Pipeline can be a Transformer or an Estimator. We run these stages in an order. Initially a DataFrame is passed as an input to Pipeline. This DataFrame keeps on transforming with each stage of Pipeline. Most of the time, Runtime checking is done on DataFrame passing through the Pipeline. We can also save a Pipeline to a disk. It can be re-read from disk a later point of time.

What is the difference between Transformer and Estimator in Apache Spark?
A Transformer is an abstraction for feature transformer and learned model. A Transformer implements transform() method. It converts one DataFrame to another DataFrame. It appends one or more columns to a DataFrame. In a feature transformer a DataFrame is the input and the output is a new DataFrame with a new mapped column. An Estimator is an abstraction for a learning algorithm that fits or trains on data. An Estimator implements fit() method. The fit() method takes a DataFrame as input and results in a Model.

What are the different types of Cluster Managers in Apache Spark?
Main types of Cluster Managers for Apache Spark are as follows:
Standalone: It is a simple cluster manager that is included with Spark. We can start Spark manually by hand in this mode.
Spark	on Mesos: In this mode, Mesos master replaces Spark master as the cluster manager. When driver creates a job, Mesos will determine which machine will handle the task.
Hadoop YARN: In this setup, Hadoop YARN is used in cluster. There are two modes in this setup. In cluster mode, Spark driver runs inside a master process managed by YARN on cluster. In client mode, the Spark driver runs in the client process and application master is used for requesting resources from YARN.

138.	How will you minimize data transfer while working with Apache Spark?
        Generally Shuffle operation in Spark leads to a large amount of data transfer. We can configure Spark Shuffle process for optimum data transfer. Some of the main points are as follows:
        spark.shuffle.compress: This configuration can be set to true to compress map output files. This reduces the amount of data transfer due to compression.
        ByKey operations: We can minimize the use of ByKey operations to minimize the shuffle calls.

139. What is the main use of MLib in Apache Spark?
     MLib is a machine-learning library in Apache Spark. Some of the main uses of MLib in Spark are as follows:
     ML Algorithms: It contains Machine Learning algorithms such as classification, regression, clustering, and collaborative filtering. Featurization:
     MLib provides algorithms to work with features. Some of these are	feature	extraction, transformation, dimensionality		reduction, and selection.
     Pipelines: It contains tools for constructing, evaluating, and tuning ML Pipelines.
     Persistence: It also provides methods for saving and load algorithms, models, and Pipelines.
     Utilities: It contains utilities for linear algebra, statistics, data handling, etc.

140. What is the Checkpointing in Apache Spark?
     In Spark Streaming, there is a concept of Checkpointing to add resiliency in the application. In case of a failure, a streaming application needs a checkpoint to recover. Due to this Spark provides Checkpointing. There are two types of Checkpointing:
     Metadata Checkpointing: Metadata is the configuration information and other information that defines a Streaming application. We can create a Metadata checkpoint for a node to recover from the failure while running the driver application.		Metadata includes	configuration, DStream operations and incomplete batches etc.
     Data Checkpointing: In this checkpoint we save RDD to a reliable storage. This is useful	in stateful transformations where generated RDD depends on RDD   of   previous   batch. There can be a long chain of RDDs in some cases. To avoid such a large recovery time, it is easier to create Data Checkpoint with RDDs at intermediate steps.

What is an Accumulator in Apache Spark?
An Accumulator is a variable in Spark that can be added only through an associative and commutative operation. An Accumulator can be supported in parallel. It is generally used to implement a counter or cumulative sum. We can create numeric type Accumulators by default in Spark.An Accumulator variable can be named as well as unnamed.

What is a Broadcast variable in Apache Spark?
As per Spark online documentation, “A Broadcast variable allows a programmer to keep a read-only variable cached on each machine rather than shipping a copy of it with tasks.” Spark can also distribute broadcast variable with an efficient broadcast algorithm to reduce communication cost. In Shuffle operations, there is a need of common data. This common data is broadcast by Spark as a Broadcast variable. The data in these variables is serialized and de-serialized before running a task.
We can	use SparkContext.broadcast(v) to create a broadcast variable. It is recommended that we should use broadcast variable in place of original variable for running a function on cluster.

What is Structured Streaming in Apache Spark?
Structured Streaming is a new feature in Spark 2.1. It is a scalable and fault-tolerant stream- processing engine. It is built on Spark SQL engine. We can use Dataset or DataFrame API to express streaming aggregations, event-time windows etc. The computations are done on the optimized Spark SQL engine.

How will you pass functions to Apache Spark?
In Spark API, we pass functions to driver program so that it can be run on a cluster. Two common ways to pass functions in Spark are as follows:
Anonymous	Function Syntax: This is used for passing short pieces of code in an anonymous function.
Static	Methods in a Singleton object: We can also define static methods in an object with only once instance i.e. Singleton. This object along with its methods can be passed to cluster nodes.

What is a Property Graph?
A Property Graph is a directed multigraph. We can attach an object on each vertex and edge of a Property Graph.In a directed multigraph, we can have multiple parallel edges that share same source and destination vertex. During modeling the data, the option of parallel edges helps in creating multiple relationships between same pair of vertices. E.g. Two persons can have two relationships Boss as well as Mentor.

What is Neighborhood Aggregation in Spark?
Neighborhood Aggregation is a concept in Graph module of Spark. It refers to the task of aggregating information	about	the neighborhood of each vertex. E.g. We want to know the number of books referenced in a book. Or number of times a Tweet is retweeted. This concept is used in iterative graph algorithms. Some of the popular uses of this concept are in Page Rank, Shortest Path etc.

We can use aggregateMessages[] and mergeMsg[] operations in Spark for implementing Neighborhood Aggregation.

What are different Persistence levels in Apache Spark?
Different Persistence levels in Apache Spark are as follows:
MEMORY_ONLY: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be recomputed.
MEMORY_AND_DISK: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
MEMORY_ONLY_SER: In this level, RDD object is stored as a serialized Java object in JVM. It is more efficient than de-serialized object.
MEMORY_AND_DISK_SE In this level, RDD object is stored as a serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
DISK_ONLY: In this level, RDD object is stored only on Disk.

How will you select the storage level in Apache Spark?
We use storage level to maintain balance between CPU efficiency and Memory usage. If our RDD objects fit in memory, we use MEMORY_ONLY option. In this option, the performance is very good due to objects being in Memory only. In case our RDD objects cannot fit in memory, we go for MEMORY_ONLY_SER option and select a serialization library that can provide space savings with serialization. This option is also quite fast in performance. In case our RDD object cannot fit in memory with a big gap in memory vs. total object size, we go for MEMORY_AND_DISK option. In this option some RDD object are stored on Disk. For fast fault recovery we use replication of objects to multiple partitions.

What are the options in Spark to create a Graph?
We can create a Graph in Spark from a collection of vertices and edges. Some of the options in Spark to create a Graph are as follows:
Graph.apply: This is the simplest option to create graph. We use this option to create a graph from RDDs of vertices and edges.
Graph.fromEdges: We can also create a graph from RDD of edges. In this option, vertices are created automatically and a default value is assigned to each vertex.
Graph.fromEdgeTuples: We can also create a graph from only an RDD of tuples.

150.	What are the basic Graph operators in Spark?
        Some of the common Graph operators in Apache Spark are as follows:

numEdges
numVertices
inDegrees
outDegrees
degrees
vertices

edges
persist
cache
unpersistVertices
partitionBy

What is the partitioning approach used in GraphX of Apache Spark?
GraphX uses Vertex-cut approach to distributed graph partitioning. In this approach, a graph is not split along edges. Rather we partition graph along vertices. These vertices can span on multiple machines. This approach reduces communication and storage overheads. Edges are assigned to different partitions based on the partition strategy that we select.


Q2.  What is RDD?



Ans. RDD (Resilient Distribution Datasets) is a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed.


Q3.  Name the different types of RDD



Ans. There are primarily two types of RDD – parallelized collection and Hadoop datasets.


Q4.  What are the methods of creating RDDs in Spark?



Ans. There are two methods –

    By parallelizing a collection in your Driver program.
    By loading an external dataset from external storage like HDFS, HBase, shared file system.


Q5.  What is a Sparse Vector?



Ans. A sparse vector has two parallel arrays –one for indices and the other for values.

Q6.  What are the languages supported by Apache Spark and which is the most popular one, What is JDBC and why it is popular?

Ans. There are four languages supported by Apache Spark – Scala, Java, Python, and R. Scala is the most popular one.

**Java Database Connectivity (JDBC)** is an application programming interface (API) that defines database connections in Java environments. Spark is written in Scala, which runs on the Java Virtual Machine (JVM). This makes JDBC the preferred method for connecting to data whenever possible. Hadoop, Hive, and MySQL all run on Java and easily interface with Spark clusters.

Databases are advanced technologies that benefit from decades of research and development. To leverage the inherent efficiencies of database engines, Spark uses an optimization called predicate pushdown. Predicate pushdown uses the database itself to handle certain parts of a query (the predicates). In mathematics and functional programming, a predicate is anything that returns a Boolean. In SQL terms, this often refers to the WHERE clause. Since the database is filtering data before it arrives on the Spark cluster, there's less data transfer across the network and fewer records for Spark to process. Spark's Catalyst Optimizer includes predicate pushdown communicated through the JDBC API, making JDBC an ideal data source for Spark workloads.


Q7.  What is Yarn?



Ans. Yarn is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster.



Q8.  Do you need to install Spark on all nodes of Yarn cluster? Why?



Ans. No, because Spark runs on top of Yarn.

Q9.  Is it possible to run Apache Spark on Apache Mesos?



Ans. Yes.



Q10.  What is lineage graph?



Ans. The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph.


Q11.  Define Partitions in Apache Spark



Ans. Partition is a smaller and logical division of data similar to ‘split’ in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process.


Q12.  What is a DStream?



Ans. Discretized Stream (DStream) is a sequence of Resilient Distributed Databases that represent a stream of data.


Q13.  What is a Catalyst framework?



Ans. Catalyst framework is an optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.


Q14.  What are Actions in Spark?



Ans. An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations.

Q15.  What is a Parquet file?



Ans. Parquet is a columnar format file supported by many other data processing systems.

Q16.  What is GraphX?



Ans. Spark uses GraphX for graph processing to build and transform interactive graphs.

Q17.  What file systems does Spark support?



Ans. Hadoop distributed file system (HDFS), local file system, and Amazon S3.

Q18.  What are the different types of transformations on DStreams? Explain.



Ans.

    Stateless Transformations – Processing of the batch does not depend on the output of the previous batch. Examples – map (), reduceByKey (), filter ().
    Stateful Transformations – Processing of the batch depends on the intermediary results of the previous batch. Examples –Transformations that depend on sliding windows.


Q19.  What is the difference between persist () and cache ()?



Ans. Persist () allows the user to specify the storage level whereas cache () uses the default storage level.

Q20.  What do you understand by SchemaRDD?



Ans. SchemaRDD is an RDD that consists of row objects (wrappers around the basic string or integer arrays) with schema information about the type of data in each column.

These are some of the popular questions asked in an Apache Spark interview. Always be prepared to answer all types of questions — technical skills, interpersonal, leadership or methodology. If you are someone who has recently started your career in big data, you can always get certified in Apache Spark to get the techniques and skills required to be an expert in the field.

Q21.What is Apache Spark?

Spark is a fast, easy-to-use and flexible data processing framework. It has an advanced execution engine supporting cyclic data  flow and in-memory computing. Spark can run on Hadoop, standalone or in the cloud and is capable of accessing diverse data sources including HDFS, HBase, Cassandra and others.

Q22. Explain key features of Spark.


    Allows Integration with Hadoop and files included in HDFS.
    Spark has an interactive language shell as it has an independent Scala (the language in which Spark is written) interpreter.
    Spark consists of RDD’s (Resilient Distributed Datasets), which can be cached across computing nodes in a cluster.
    Spark supports multiple analytic tools that are used for interactive query analysis , real-time analysis and graph      processing

Q23. Define RDD?

RDD is the acronym for Resilient Distribution Datasets – a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed. There are primarily two types of RDD:

    Parallelized Collections : The existing RDD’s running parallel with one another.
    Hadoop datasets : perform function on each file record in HDFS or other storage system

Q24. What does a Spark Engine do?

Spark Engine is responsible for scheduling, distributing and monitoring the data application across the cluster.

Q25.Define Partitions?

As the name suggests, partition is a smaller and logical division of data  similar to ‘split’ in MapReduce. Partitioning is the process to derive logical units of data to speed up the processing process. Everything in Spark is a partitioned RDD.

Q26.What operations RDD support?


    Transformations.
    Actions

Q27.What do you understand by Transformations in Spark?

Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filer() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements form current RDD that pass function argument.

Q28.Define Actions.

An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to local node.

Q29.Define functions of SparkCore?

Serving as the base engine, SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems.

Q30.What is RDD Lineage?

Spark does not support data replication in the memory and thus, if any data is lost, it is rebuild using RDD lineage. RDD lineage is a process that reconstructs lost data partitions. The best is that RDD always remembers how to build from other datasets.

Q31.What is Spark Driver?

Spark Driver is the program that runs on the master node of the machine and declares transformations and actions on data RDDs. In simple terms, driver in Spark creates SparkContext, connected to a given Spark Master.
The driver also delivers the RDD graphs to Master, where the standalone cluster manager runs.

Q32.What is Hive on Spark?

Hive contains significant support for Apache Spark, wherein Hive execution is configured to Spark:

hive> set spark.home=/location/to/sparkHome;
hive> set hive.execution.engine=spark;

Q33. Name commonly-used Spark Ecosystems.


    Spark SQL (Shark)- for developers.
    Spark Streaming for processing live data streams.
    GraphX for generating and computing graphs.
    MLlib (Machine Learning Algorithms).
    SparkR to promote R Programming in Spark engine.

Q34. Define Spark Streaming.

Spark supports stream processing – an extension to the Spark API , allowing stream processing of live data streams. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

Q35.What is Spark SQL?

SQL Spark, better known as Shark is a novel module introduced in Spark to work with structured data and perform structured data processing. Through this module, Spark executes relational SQL queries on the data. The core of the component supports an altogether different RDD called SchemaRDD, composed of rows objects and schema objects defining data type of each column in the row. It is similar to a table in relational database.

Q36.List the functions of Spark SQL.?

Spark SQL is capable of:

    Loading data from a variety of structured sources.
    Querying data using SQL statements, both inside a Spark program and from external tools that connect to Spark SQL through standard database connectors (JDBC/ODBC). For instance, using business intelligence tools like Tableau.
    Providing rich integration between SQL and regular Python/Java/Scala code, including the ability to join RDDs and SQL tables, expose custom functions in SQL, and more.


Q37.What are benefits of Spark over MapReduce?


    Due to the availability of in-memory processing, Spark implements the processing around 10-100x faster than Hadoop MapReduce. MapReduce makes use of persistence storage for any of the data processing tasks.
    Unlike Hadoop, Spark provides in-built libraries to perform multiple tasks form the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
    Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
    Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.

Q38. What is Spark Executor?

When SparkContext connect to a cluster manager, it acquires an Executor on nodes in the cluster. Executors are Spark processes that run computations and store the data on the worker node. The final tasks by SparkContext are transferred to executors for their execution.

Q39.Name types of Cluster Managers in Spark.

The Spark framework supports three major types of Cluster Managers:

    Standalone : a basic manager to set up a cluster.
    Apache Mesos : generalized/commonly-used cluster manager, also runs Hadoop MapReduce and other applications.
    Yarn : responsible for resource management in Hadoop

Q40. What do you understand by worker node?

Worker node refers to any node that can run the application code in a cluster.

Q41.Illustrate some demerits of using Spark.

Since Spark utilizes more storage space compared to Hadoop and MapReduce, there may arise certain problems. Developers need to be careful while running their applications in Spark. Instead of running everything on a single node, the work must be distributed over multiple clusters.

Q42.What is the advantage of a Parquet file?

Parquet file is a columnar format file that helps –
Limit I/O operations
Consumes less space
Fetches only required columns.


Q43.What is the difference between persist() and cache()

persist () allows the user to specify the storage level whereas cache () uses the default storage level.

Q44.what are different o/p methods to get result?

collect()
show()
take()
foreach(println)



**Q45:**  What are two ways to attain a schema from data?  
**Ans:**  Allow Spark to infer a schema from your data or provide a user defined schema. Schema inference is the recommended first step; however, you can customize this schema to your use case with a user defined schema.
**Note**

> Providing a schema increases performance two to three times, depending
> on the size of the cluster used. Since Spark doesn't infer the schema,
> it doesn't have to read through all of the data. This is also why
> there are fewer jobs when a schema is provided: Spark doesn't need one
> job for each partition of the data to infer the schema.

**Q46:**  Why should you define your own schema?  
**Ans:**  Benefits of user defined schemas include:

-   Avoiding the extra scan of your data needed to infer the schema
-   Providing alternative data types
-   Parsing only the fields you need

**Q47:**  Why is JSON a common format in big data pipelines?  
**Ans:**  Semi-structured data works well with hierarchical data and where schemas need to evolve over time. It also easily contains composite data types such as arrays and maps.

**Q48:**  By default, how are corrupt records dealt with using  `spark.read.json()`?  
**Ans:**  They appear in a column called  `_corrupt_record`. These are the records that Spark can't read (e.g. when characters are missing from a JSON string).

3. Explain the key features of Apache Spark.
   The following are the key features of Apache Spark:

Polyglot
Speed
Multiple Format Support
Lazy Evaluation
Real Time Computation
Hadoop Integration
Machine Learning
Let us look at these features in detail:

Polyglot: Spark provides high-level APIs in Java, Scala, Python and R. Spark code can be written in any of these four languages. It provides a shell in Scala and Python. The Scala shell can be accessed through ./bin/spark-shell and Python shell through ./bin/pyspark from the installed directory.

Speed: Spark runs upto 100 times faster than Hadoop MapReduce for large-scale data processing. Spark is able to achieve this speed through controlled partitioning. It manages data using partitions that help parallelize distributed data processing with minimal network traffic.

Multiple Formats: Spark supports multiple data sources such as Parquet, JSON, Hive and Cassandra. The Data Sources API provides a pluggable mechanism for accessing structured data though Spark SQL. Data sources can be more than just simple pipes that convert data and pull it into Spark.

Lazy Evaluation: Apache Spark delays its evaluation till it is absolutely necessary. This is one of the key factors contributing to its speed. For transformations, Spark adds them to a DAG of computation and only when the driver requests some data, does this DAG actually gets executed.

Real Time Computation: Spark’s computation is real-time and has less latency because of its in-memory computation. Spark is designed for massive scalability and the Spark team has documented users of the system running production clusters with thousands of nodes and supports several computational models.

Hadoop Integration: Apache Spark provides smooth compatibility with Hadoop. This is a great boon for all the Big Data engineers who started their careers with Hadoop. Spark is a potential replacement for the MapReduce functions of Hadoop, while Spark has the ability to run on top of an existing Hadoop cluster using YARN for resource scheduling.

Machine Learning: Spark’s MLlib is the machine learning component which is handy when it comes to big data processing. It eradicates the need to use multiple tools, one for processing and one for machine learning. Spark provides data engineers and data scientists with a powerful, unified engine that is both fast and easy to use.

4. What are the languages supported by Apache Spark and which is the most popular one?
   Apache Spark supports the following four languages: Scala, Java, Python and R. Among these languages, Scala and Python have interactive shells for Spark. The Scala shell can be accessed through ./bin/spark-shell and the Python shell through ./bin/pyspark. Scala is the most used among them because Spark is written in Scala and it is the most popularly used for Spark.

5. What are benefits of Spark over MapReduce?
   Spark has the following benefits over MapReduce:

Due to the availability of in-memory processing, Spark implements the processing around 10 to 100 times faster than Hadoop MapReduce whereas MapReduce makes use of persistence storage for any of the data processing tasks.
Unlike Hadoop, Spark provides inbuilt libraries to perform multiple tasks from the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.
6. What is YARN?
   Similar to Hadoop, YARN is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster. YARN is a distributed container manager, like Mesos for example, whereas Spark is a data processing tool. Spark can run on YARN, the same way Hadoop Map Reduce can run on YARN. Running Spark on YARN necessitates a binary distribution of Spark as built on YARN support.

7. Do you need to install Spark on all nodes of YARN cluster?
   No, because Spark runs on top of YARN. Spark runs independently from its installation. Spark has some options to use YARN when dispatching jobs to the cluster, rather than its own built-in manager, or Mesos. Further, there are some configurations to run YARN. They include master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

8. Is there any benefit of learning MapReduce if Spark is better than MapReduce?
   Yes, MapReduce is a paradigm used by many big data tools including Spark as well. It is extremely relevant to use MapReduce when the data grows bigger and bigger. Most tools like Pig and Hive convert their queries into MapReduce phases to optimize them better.

9. Explain the concept of Resilient Distributed Dataset (RDD).
   RDD stands for Resilient Distribution Datasets. An RDD is a fault-tolerant collection of operational elements that run in parallel. The partitioned data in RDD is immutable and distributed in nature. There are primarily two types of RDD:

Parallelized Collections: Here, the existing RDDs running parallel with one another.
Hadoop Datasets: They perform functions on each file record in HDFS or other storage systems.
RDDs are basically parts of data that are stored in the memory distributed across many nodes. RDDs are lazily evaluated in Spark. This lazy evaluation is what contributes to Spark’s speed.

10. How do we create RDDs in Spark?
    Spark provides two methods to create RDD:

1. By parallelizing a collection in your Driver program.

2. This makes use of SparkContext’s ‘parallelize’

1
2
3
method val DataArray = Array(2,4,6,8,10)

val DataRDD = sc.parallelize(DataArray)
3. By loading an external dataset from external storage like HDFS, HBase, shared file system.

11. What is Executor Memory in a Spark application?
    Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag. Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

12. Define Partitions in Apache Spark.
    As the name suggests, partition is a smaller and logical division of data similar to ‘split’ in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process. Spark manages data using partitions that help parallelize distributed data processing with minimal network traffic for sending data between executors. By default, Spark tries to read data into an RDD from the nodes that are close to it. Since Spark usually accesses distributed partitioned data, to optimize transformation operations it creates partitions to hold the data chunks. Everything in Spark is a partitioned RDD.

13. What operations does RDD support?
    RDD (Resilient Distributed Dataset) is main logical data unit in Spark. An RDD has distributed a collection of objects. Distributed means, each RDD is divided into multiple partitions. Each of these partitions can reside in memory or stored on the disk of different machines in a cluster. RDDs are immutable (Read Only) data structure. You can’t change original RDD, but you can always transform it into different RDD with all changes you want.

RDDs support two types of operations: transformations and actions.

Transformations: Transformations create new RDD from existing RDD like map, reduceByKey and filter we just saw. Transformations are executed on demand. That means they are computed lazily.

Actions: Actions return final results of RDD computations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.

14. What do you understand by Transformations in Spark?
    Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filter() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements from current RDD that pass function argument.

1
2
3
val rawData=sc.textFile("path to/movies.txt")

val moviesData=rawData.map(x=>x.split("  "))
As we can see here, rawData RDD is transformed into moviesData RDD. Transformations are lazily evaluated.

15. Define Actions in Spark.
    An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.

reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to a local node.

1
moviesData.saveAsTextFile(“MoviesData.txt”)
As we can see here, moviesData RDD is saved into a text file called MoviesData.txt. 

. Define functions of SparkCore.
Spark Core is the base engine for large-scale parallel and distributed data processing. The core is the distributed execution engine and the Java, Scala, and Python APIs offer a platform for distributed ETL application development. SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems. Further, additional libraries, built atop the core allow diverse workloads for streaming, SQL, and machine learning. It is responsible for:

Memory management and fault recovery
Scheduling, distributing and monitoring jobs on a cluster
Interacting with storage systems
17. What do you understand by Pair RDD?
    Apache defines PairRDD functions class as

1
class PairRDDFunctions[K, V] extends Logging with HadoopMapReduceUtil with Serializable
Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey() method that collects data based on each key and a join() method that combines different RDDs together, based on the elements having the same key.

18. Name the components of Spark Ecosystem.
    Spark Core: Base engine for large-scale parallel and distributed data processing
    Spark Streaming: Used for processing real-time streaming data
    Spark SQL: Integrates relational processing with Spark’s functional programming API
    GraphX: Graphs and graph-parallel computation
    MLlib: Performs machine learning in Apache Spark
19. How is Streaming implemented in Spark? Explain with examples.
    Spark Streaming is used for processing real-time streaming data. Thus it is a useful addition to the core Spark API. It enables high-throughput and fault-tolerant stream processing of live data streams. The fundamental stream unit is DStream which is basically a series of RDDs (Resilient Distributed Datasets) to process the real-time data. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

Is there an API for implementing graphs in Spark?
GraphX is the Spark API for graphs and graph-parallel computation. Thus, it extends the Spark RDD with a Resilient Distributed Property Graph.

The property graph is a directed multi-graph which can have multiple edges in parallel. Every edge and vertex have user defined properties associated with it. Here, the parallel edges allow multiple relationships between the same vertices. At a high-level, GraphX extends the Spark RDD abstraction by introducing the Resilient Distributed Property Graph: a directed multigraph with properties attached to each vertex and edge.

To support graph computation, GraphX exposes a set of fundamental operators (e.g., subgraph, joinVertices, and mapReduceTriplets) as well as an optimized variant of the Pregel API. In addition, GraphX includes a growing collection of graph algorithms and builders to simplify graph analytics tasks.

21. What is PageRank in GraphX?
    PageRank measures the importance of each vertex in a graph, assuming an edge from u to v represents an endorsement of v’s importance by u. For example, if a Twitter user is followed by many others, the user will be ranked highly.

GraphX comes with static and dynamic implementations of PageRank as methods on the PageRank Object. Static PageRank runs for a fixed number of iterations, while dynamic PageRank runs until the ranks converge (i.e., stop changing by more than a specified tolerance). GraphOps allows calling these algorithms directly as methods on Graph.

22. How is machine learning implemented in Spark?
    MLlib is scalable machine learning library provided by Spark. It aims at making machine learning easy and scalable with common learning algorithms and use cases like clustering, regression filtering, dimensional reduction, and alike.

. Is there a module to implement SQL in Spark? How does it work?
Spark SQL is a new module in Spark which integrates relational processing with Spark’s functional programming API. It supports querying data either via SQL or via the Hive Query Language. For those of you familiar with RDBMS, Spark SQL will be an easy transition from your earlier tools where you can extend the boundaries of traditional relational data processing.

Spark SQL integrates relational processing with Spark’s functional programming. Further, it provides support for various data sources and makes it possible to weave SQL queries with code transformations thus resulting in a very powerful tool.

The following are the four libraries of Spark SQL.

Data Source API
DataFrame API
Interpreter & Optimizer
SQL Service

List the types of Deploy Modes in Spark.
There are 2 deploy modes in Spark. They are:

Client Mode: The deploy mode is said to be in client mode when the spark driver component runs on the machine node from where the spark job is submitted.
The main disadvantage of this mode is if the machine node fails, then the entire job fails.
This mode supports both interactive shells or the job submission commands.
The performance of this mode is worst and is not preferred in production environments.
Cluster Mode: If the spark job driver component does not run on the machine from which the spark job has been submitted, then the deploy mode is said to be in cluster mode.
The spark job launches the driver component within the cluster as a part of the sub-process of ApplicationMaster.
This mode supports deployment only using the spark-submit command (interactive shell mode is not supported).
Here, since the driver programs are run in ApplicationMaster, in case the program fails, the driver program is re-instantiated.
In this mode, there is a dedicated cluster manager (such as stand-alone, YARN, Apache Mesos, Kubernetes, etc) for allocating the resources required for the job to run as shown in the below architecture.

Apart from the above two modes, if we have to run the application on our local machines for unit testing and development, the deployment mode is called “Local Mode”. Here, the jobs run on a single JVM in a single machine which makes it highly inefficient as at some point or the other there would be a shortage of resources which results in the failure of jobs. It is also not possible to scale up resources in this mode due to the restricted memory and space.

6. What are receivers in Apache Spark Streaming?
   Receivers are those entities that consume data from different data sources and then move them to Spark for processing. They are created by using streaming contexts in the form of long-running tasks that are scheduled for operating in a round-robin fashion. Each receiver is configured to use up only a single core. The receivers are made to run on various executors to accomplish the task of data streaming. There are two types of receivers depending on how the data is sent to Spark:

Reliable receivers: Here, the receiver sends an acknowledegment to the data sources post successful reception of data and its replication on the Spark storage space.
Unreliable receiver: Here, there is no acknowledgement sent to the data sources.
7. What is the difference between repartition and coalesce?
   Repartition 	Coalesce
   Usage repartition can increase/decrease the number of data partitions.	Spark coalesce can only reduce the number of data partitions.
   Repartition creates new data partitions and performs a full shuffle of evenly distributed data.	Coalesce makes use of already existing partitions to reduce the amount of shuffled data unevenly.
   Repartition internally calls coalesce with shuffle parameter thereby making it slower than coalesce.	Coalesce is faster than repartition. However, if there are unequal-sized data partitions, the speed might be slightly slower.
8. What are the data formats supported by Spark?
   Spark supports both the raw files and the structured file formats for efficient reading and processing. File formats like paraquet, JSON, XML, CSV, RC, Avro, TSV, etc are supported by Spark.

9. What do you understand by Shuffling in Spark?
   The process of redistribution of data across different partitions which might or might not cause data movement across the JVM processes or the executors on the separate machines is known as shuffling/repartitioning. Partition is nothing but a smaller logical division of data.


It is to be noted that Spark has no control over what partition the data gets distributed across.

10. What is YARN in Spark?
    YARN is one of the key features provided by Spark that provides a central resource management platform for delivering scalable operations throughout the cluster.
    YARN is a cluster management technology and a Spark is a tool for data processing.


How is Apache Spark different from MapReduce?
MapReduce	                                        Apache Spark
MapReduce does only batch-wise processing of data.	Apache Spark can process the data both in real-time and in batches.
MapReduce does slow processing of large data.	Apache Spark runs approximately 100 times faster than MapReduce for big data processing.
MapReduce stores data in HDFS (Hadoop Distributed File System) which makes it take a long time to get the data.	Spark stores data in memory (RAM) which makes it easier and faster to retrieve data when needed.
MapReduce highly depends on disk which makes it to be a high latency framework.	Spark supports in-memory data storage and caching and makes it a low latency computation framework.
MapReduce requires an external scheduler for jobs.	Spark has its own job scheduler due to the in-memory data computation.
12. Explain the working of Spark with the help of its architecture.
    Spark applications are run in the form of independent processes that are well coordinated by the Driver program by means of a SparkSession object. The cluster manager or the resource manager entity of Spark assigns the tasks of running the Spark jobs to the worker nodes as per one task per partition principle. There are various iterations algorithms that are repeatedly applied to the data to cache the datasets across various iterations. Every task applies its unit of operations to the dataset within its partition and results in the new partitioned dataset. These results are sent back to the main driver application for further processing or to store the data on the disk. The following diagram illustrates this working as described above:


13. What is the working of DAG in Spark?
    DAG stands for Direct Acyclic Graph which has a set of finite vertices and edges. The vertices represent RDDs and the edges represent the operations to be performed on RDDs sequentially. The DAG created is submitted to the DAG Scheduler which splits the graphs into stages of tasks based on the transformations applied to the data. The stage view has the details of the RDDs of that stage.

The working of DAG in spark is defined as per the workflow diagram below:


The first task is to interpret the code with the help of an interpreter. If you use the Scala code, then the Scala interpreter interprets the code.
Spark then creates an operator graph when the code is entered in the Spark console.
When the action is called on Spark RDD, the operator graph is submitted to the DAG Scheduler.
The operators are divided into stages of task by the DAG Scheduler. The stage consists of detailed step-by-step operation on the input data. The operators are then pipelined together.
The stages are then passed to the Task Scheduler which launches the task via the cluster manager to work on independently without the dependencies between the stages.
The worker nodes then execute the task.
Each RDD keeps track of the pointer to one/more parent RDD along with its relationship with the parent. For example, consider the operation val childB=parentA.map() on RDD, then we have the RDD childB that keeps track of its parentA which is called RDD lineage.

14. Under what scenarios do you use Client and Cluster modes for deployment?
    In case the client machines are not close to the cluster, then the Cluster mode should be used for deployment. This is done to avoid the network latency caused while communication between the executors which would occur in the Client mode. Also, in Client mode, the entire process is lost if the machine goes offline.
    If we have the client machine inside the cluster, then the Client mode can be used for deployment. Since the machine is inside the cluster, there won’t be issues of network latency and since the maintenance of the cluster is already handled, there is no cause of worry in cases of failure.
15. What is Spark Streaming and how is it implemented in Spark?
    Spark Streaming is one of the most important features provided by Spark. It is nothing but a Spark API extension for supporting stream processing of data from different sources.

Data from sources like Kafka, Kinesis, Flume, etc are processed and pushed to various destinations like databases, dashboards, machine learning APIs, or as simple as file systems. The data is divided into various streams (similar to batches) and is processed accordingly.
Spark streaming supports highly scalable, fault-tolerant continuous stream processing which is mostly used in cases like fraud detection, website monitoring, website click baits, IoT (Internet of Things) sensors, etc.
Spark Streaming first divides the data from the data stream into batches of X seconds which are called Dstreams or Discretized Streams. They are internally nothing but a sequence of multiple RDDs. The Spark application does the task of processing these RDDs using various Spark APIs and the results of this processing are again returned as batches. The following diagram explains the workflow of the spark streaming process.



Write a spark program to check if a given keyword exists in a huge text file or not?
def keywordExists(line):
if (line.find(“my_keyword”) > -1):
return 1
return 0
lines = sparkContext.textFile(“test_file.txt”);
isExist = lines.map(keywordExists);
sum = isExist.reduce(sum);
print(“Found” if sum>0 else “Not Found”)
17. What can you say about Spark Datasets?
    Spark Datasets are those data structures of SparkSQL that provide JVM objects with all the benefits (such as data manipulation using lambda functions) of RDDs alongside Spark SQL-optimised execution engine. This was introduced as part of Spark since version 1.6.

Spark datasets are strongly typed structures that represent the structured queries along with their encoders.
They provide type safety to the data and also give an object-oriented programming interface.
The datasets are more structured and have the lazy query expression which helps in triggering the action. Datasets have the combined powers of both RDD and Dataframes. Internally, each dataset symbolizes a logical plan which informs the computational query about the need for data production. Once the logical plan is analyzed and resolved, then the physical query plan is formed that does the actual query execution.
Datasets have the following features:

Optimized Query feature: Spark datasets provide optimized queries using Tungsten and Catalyst Query Optimizer frameworks. The Catalyst Query Optimizer represents and manipulates a data flow graph (graph of expressions and relational operators). The Tungsten improves and optimizes the speed of execution of Spark job by emphasizing the hardware architecture of the Spark execution platform.
Compile-Time Analysis: Datasets have the flexibility of analyzing and checking the syntaxes at the compile-time which is not technically possible in RDDs or Dataframes or the regular SQL queries.
Interconvertible: The type-safe feature of datasets can be converted to “untyped” Dataframes by making use of the following methods provided by the Datasetholder:
toDS():Dataset[T]
toDF():DataFrame
toDF(columName:String*):DataFrame
Faster Computation: Datasets implementation are much faster than those of the RDDs which helps in increasing the system performance.
Persistent storage qualified: Since the datasets are both queryable and serializable, they can be easily stored in any persistent storages.
Less Memory Consumed: Spark uses the feature of caching to create a more optimal data layout. Hence, less memory is consumed.
Single Interface Multiple Languages: Single API is provided for both Java and Scala languages. These are widely used languages for using Apache Spark. This results in a lesser burden of using libraries for different types of inputs.
18. Define Spark DataFrames.
    Spark Dataframes are the distributed collection of datasets organized into columns similar to SQL. It is equivalent to a table in the relational database and is mainly optimized for big data operations.
    Dataframes can be created from an array of data from different data sources such as external databases, existing RDDs, Hive Tables, etc. Following are the features of Spark Dataframes:

Spark Dataframes have the ability of processing data in sizes ranging from Kilobytes to Petabytes on a single node to large clusters.
They support different data formats like CSV, Avro, elastic search, etc, and various storage systems like HDFS, Cassandra, MySQL, etc.
By making use of SparkSQL catalyst optimizer, state of art optimization is achieved.
It is possible to easily integrate Spark Dataframes with major Big Data tools using SparkCore.
19. Define Executor Memory in Spark
    The applications developed in Spark have the same fixed cores count and fixed heap size defined for spark executors. The heap size refers to the memory of the Spark executor that is controlled by making use of the property spark.executor.memory that belongs to the -executor-memory flag. Every Spark applications have one allocated executor on each worker node it runs. The executor memory is a measure of the memory consumed by the worker node that the application utilizes.

20. What are the functions of SparkCore?
    SparkCore is the main engine that is meant for large-scale distributed and parallel data processing. The Spark core consists of the distributed execution engine that offers various APIs in Java, Python, and Scala for developing distributed ETL applications.
    Spark Core does important functions such as memory management, job monitoring, fault-tolerance, storage system interactions, job scheduling, and providing support for all the basic I/O functionalities. There are various additional libraries built on top of Spark Core which allows diverse workloads for SQL, streaming, and machine learning. They are responsible for:

Fault recovery
Memory management and Storage system interactions
Job monitoring, scheduling, and distribution
Basic I/O functions
21. What do you understand by worker node?
    Worker nodes are those nodes that run the Spark application in a cluster. The Spark driver program listens for the incoming connections and accepts them from the executors addresses them to the worker nodes for execution. A worker node is like a slave node where it gets the work from its master node and actually executes them. The worker nodes do data processing and report the resources used to the master. The master decides what amount of resources needs to be allocated and then based on their availability, the tasks are scheduled for the worker nodes by the master.

What are some of the demerits of using Spark in applications?
Despite Spark being the powerful data processing engine, there are certain demerits to using Apache Spark in applications. Some of them are:

Spark makes use of more storage space when compared to MapReduce or Hadoop which may lead to certain memory-based problems.
Care must be taken by the developers while running the applications. The work should be distributed across multiple clusters instead of running everything on a single node.
Since Spark makes use of “in-memory” computations, they can be a bottleneck to cost-efficient big data processing.
While using files present on the path of the local filesystem, the files must be accessible at the same location on all the worker nodes when working on cluster mode as the task execution shuffles between various worker nodes based on the resource availabilities. The files need to be copied on all worker nodes or a separate network-mounted file-sharing system needs to be in place.
One of the biggest problems while using Spark is when using a large number of small files. When Spark is used with Hadoop, we know that HDFS gives a limited number of large files instead of a large number of small files. When there is a large number of small gzipped files, Spark needs to uncompress these files by keeping them on its memory and network. So large amount of time is spent in burning core capacities for unzipping the files in sequence and performing partitions of the resulting RDDs to get data in a manageable format which would require extensive shuffling overall. This impacts the performance of Spark as much time is spent preparing the data instead of processing them.
Spark doesn’t work well in multi-user environments as it is not capable of handling many users concurrently.
23. How can the data transfers be minimized while working with Spark?
    Data transfers correspond to the process of shuffling. Minimizing these transfers results in faster and reliable running Spark applications. There are various ways in which these can be minimized. They are:

Usage of Broadcast Variables: Broadcast variables increases the efficiency of the join between large and small RDDs.
Usage of Accumulators: These help to update the variable values parallelly during execution.
Another common way is to avoid the operations which trigger these reshuffles.
24. What is SchemaRDD in Spark RDD?
    SchemaRDD is an RDD consisting of row objects that are wrappers around integer arrays or strings that has schema information regarding the data type of each column. They were designed to ease the lives of developers while debugging the code and while running unit test cases on the SparkSQL modules. They represent the description of the RDD which is similar to the schema of relational databases. SchemaRDD also provides the basic functionalities of the common RDDs along with some relational query interfaces of SparkSQL.

Consider an example. If you have an RDD named Person that represents a person’s data. Then SchemaRDD represents what data each row of Person RDD represents. If the Person has attributes like name and age, then they are represented in SchemaRDD.


25. What module is used for implementing SQL in Apache Spark?
    Spark provides a powerful module called SparkSQL which performs relational data processing combined with the power of the functional programming feature of Spark. This module also supports either by means of SQL or Hive Query Language. It also provides support for different data sources and helps developers write powerful SQL queries using code transformations.
    The four major libraries of SparkSQL are:

Data Source API
DataFrame API
Interpreter & Catalyst Optimizer
SQL Services
Spark SQL supports the usage of structured and semi-structured data in the following ways:

Spark supports DataFrame abstraction in various languages like Python, Scala, and Java along with providing good optimization techniques.
SparkSQL supports data read and writes operations in various structured formats like JSON, Hive, Parquet, etc.
SparkSQL allows data querying inside the Spark program and via external tools that do the JDBC/ODBC connections.
It is recommended to use SparkSQL inside the Spark applications as it empowers the developers to load the data, query the data from databases and write the results to the destination.

26. What are the different persistence levels in Apache Spark?
    Spark persists intermediary data from different shuffle operations automatically. But it is recommended to call the persist() method on the RDD. There are different persistence levels for storing the RDDs on memory or disk or both with different levels of replication. The persistence levels available in Spark are:

MEMORY_ONLY: This is the default persistence level and is used for storing the RDDs as the deserialized version of Java objects on the JVM. In case the RDDs are huge and do not fit in the memory, then the partitions are not cached and they will be recomputed as and when needed.
MEMORY_AND_DISK: The RDDs are stored again as deserialized Java objects on JVM. In case the memory is insufficient, then partitions not fitting on the memory will be stored on disk and the data will be read from the disk as and when needed.
MEMORY_ONLY_SER: The RDD is stored as serialized Java Objects as One Byte per partition.
MEMORY_AND_DISK_SER: This level is similar to MEMORY_ONLY_SER but the difference is that the partitions not fitting in the memory are saved on the disk to avoid recomputations on the fly.
DISK_ONLY: The RDD partitions are stored only on the disk.
OFF_HEAP: This level is the same as the MEMORY_ONLY_SER but here the data is stored in the off-heap memory.
The syntax for using persistence levels in the persist() method is:

df.persist(StorageLevel.<level_value>)
The following table summarizes the details of persistence levels:

Persistence Level 	Space Consumed 	CPU time	In-memory?	On-disk?
MEMORY_ONLY	High	Low	Yes	No
MEMORY_ONLY_SER	Low	High	Yes	No
MEMORY_AND_DISK	High	Medium	Some	Some
MEMORY_AND_DISK_SER	Low	High	Some	Some
DISK_ONLY	Low	High	No	Yes
OFF_HEAP	Low	High	Yes (but off-heap)	No
27. What are the steps to calculate the executor memory?
    Consider you have the below details regarding the cluster:

Number of nodes = 10
Number of cores in each node = 15 cores
RAM of each node = 61GB
To identify the number of cores, we follow the approach:

Number of Cores = number of concurrent tasks that can be run parallelly by the executor. The optimal value as part of a general rule of thumb is 5.
Hence to calculate the number of executors, we follow the below approach:

Number of executors = Number of cores/Concurrent Task
= 15/5
= 3
Number of executors = Number of nodes * Number of executor in each node
= 10 * 3
= 30 executors per Spark job
28. Why do we need broadcast variables in Spark?
    Broadcast variables let the developers maintain read-only variables cached on each machine instead of shipping a copy of it with tasks. They are used to give every node copy of a large input dataset efficiently. These variables are broadcasted to the nodes using different algorithms to reduce the cost of communication.


Differentiate between Spark Datasets, Dataframes and RDDs.
Criteria	Spark Datasets	Spark Dataframes	Spark RDDs
Representation of Data	Spark Datasets is a combination of Dataframes and RDDs with features like static type safety and object-oriented interfaces.	Spark Dataframe is a distributed collection of data that is organized into named columns.	Spark RDDs are a distributed collection of data without schema.
Optimization	Datasets make use of catalyst optimizers for optimization.	Dataframes also makes use of catalyst optimizer for optimization.	There is no built-in optimization engine.
Schema Projection	Datasets find out schema automatically using SQL Engine.	Dataframes also find the schema automatically.	Schema needs to be defined manually in RDDs.
Aggregation Speed	Dataset aggregation is faster than RDD but slower than Dataframes.	Aggregations are faster in Dataframes due to the provision of easy and powerful APIs.	RDDs are slower than both the Dataframes and the Datasets while performing even simple operations like data grouping.
30. Can Apache Spark be used along with Hadoop? If yes, then how?
    Yes! The main feature of Spark is its compatibility with Hadoop. This makes it a powerful framework as using the combination of these two helps to leverage the processing capacity of Spark by making use of the best of Hadoop’s YARN and HDFS features.


Hadoop can be integrated with Spark in the following ways:

HDFS: Spark can be configured to run atop HDFS to leverage the feature of distributed replicated storage.
MapReduce: Spark can also be configured to run alongside the MapReduce in the same or different processing framework or Hadoop cluster. Spark and MapReduce can be used together to perform real-time and batch processing respectively.
YARN: Spark applications can be configured to run on YARN which acts as the cluster management framework.
31. What are Sparse Vectors? How are they different from dense vectors?
    Sparse vectors consist of two parallel arrays where one array is for storing indices and the other for storing values. These vectors are used to store non-zero values for saving space.

val sparseVec: Vector = Vectors.sparse(5, Array(0, 4), Array(1.0, 2.0))
In the above example, we have the vector of size 5, but the non-zero values are there only at indices 0 and 4.
Sparse vectors are particularly useful when there are very few non-zero values. If there are cases that have only a few zero values, then it is recommended to use dense vectors as usage of sparse vectors would introduce the overhead of indices which could impact the performance.
Dense vectors can be defines as follows:
val denseVec = Vectors.dense(4405d,260100d,400d,5.0,4.0,198.0,9070d,1.0,1.0,2.0,0.0)
Usage of sparse or dense vectors does not impact the results of calculations but when used inappropriately, they impact the memory consumed and the speed of calculation.
32. How are automatic clean-ups triggered in Spark for handling the accumulated metadata?
    The clean-up tasks can be triggered automatically either by setting spark.cleaner.ttl parameter or by doing the batch-wise division of the long-running jobs and then writing the intermediary results on the disk.

33. How is Caching relevant in Spark Streaming?
    Spark Streaming involves the division of data stream’s data into batches of X seconds called DStreams. These DStreams let the developers cache the data into the memory which can be very useful in case the data of DStream is used for multiple computations. The caching of data can be done using the cache() method or using persist() method by using appropriate persistence levels. The default persistence level value for input streams receiving data over the networks such as Kafka, Flume, etc is set to achieve data replication on 2 nodes to accomplish fault tolerance.

Caching using cache method:
val cacheDf = dframe.cache()
Caching using persist method:
val persistDf = dframe.persist(StorageLevel.MEMORY_ONLY)
The main advantages of caching are:

Cost efficiency: Since Spark computations are expensive, caching helps to achieve reusing of data and this leads to reuse computations which can save the cost of operations.
Time-efficient: The computation reusage leads to saving a lot of time.
More Jobs Achieved: By saving time of computation execution, the worker nodes can perform/execute more jobs.

34. Define Piping in Spark.
    Apache Spark provides the pipe() method on RDDs which gives the opportunity to compose different parts of occupations that can utilize any language as needed as per the UNIX Standard Streams. Using the pipe() method, the RDD transformation can be written which can be used for reading each element of the RDD as String. These can be manipulated as required and the results can be displayed as String.

35. What API is used for Graph Implementation in Spark?
    Spark provides a powerful API called GraphX that extends Spark RDD for supporting graphs and graph-based computations. The extended property of Spark RDD is called as Resilient Distributed Property Graph which is a directed multi-graph that has multiple parallel edges. Each edge and the vertex has associated user-defined properties. The presence of parallel edges indicates multiple relationships between the same set of vertices. GraphX has a set of operators such as subgraph, mapReduceTriplets, joinVertices, etc that can support graph computation. It also includes a large collection of graph builders and algorithms for simplifying tasks related to graph analytics.

36. How can you achieve machine learning in Spark?
    Spark provides a very robust, scalable machine learning-based library called MLlib. This library aims at implementing easy and scalable common ML-based algorithms and has the features like classification, clustering, dimensional reduction, regression filtering, etc. More information about this library can be obtained in detail from Spark’s official documentation site here: https://spark.apache.org/docs/latest/ml-guide.html


4. EXPLAIN THE CONCEPT OF SPARSE VECTOR.
   A vector is a one-dimensional array of elements. However, in many applications, the vector elements have mostly zero values that are said to be sparse.

5. WHAT IS THE METHOD FOR CREATING A DATA FRAME?
   A data frame can be generated using the Hive and Structured Data Tables.

6. EXPLAIN WHAT SCHEMARDD IS.
   A SchemaRDD is similar to a table in a traditional relational database. A SchemaRDD can be created from an existing RDD, Parquet file, a JSON dataset, or by running HiveQL against data stored in Apache Hive.

7. EXPLAIN WHAT ACCUMULATORS ARE.
   Accumulators are variables used to aggregate information across the executors.

8. EXPLAIN WHAT THE CORE OF SPARK IS.
   Spark Core is a basic execution engine on the Spark platform.

9. EXPLAIN HOW DATA IS INTERPRETED IN SPARK?
   Data can be interpreted in Apache Spark in three ways: RDD, DataFrame, and DataSet.

NOTE: These are some of the most frequently asked spark interview questions.

10. HOW MANY FORMS OF TRANSFORMATIONS ARE THERE?
    There are two forms of transformation: narrow transformations and broad transformations.

11. WHAT’S PAIRED RDD?
    Paired RDD is a key-value pair of RDDs.

12. WHAT IS IMPLIED BY THE TREATMENT OF MEMORY IN SPARK?
    In memory computing, we retain data in sloppy access memory instead of specific slow disc drives.

NOTE: It is important to know more about this concept as it is commonly asked in Spark Interview Questions.

13. EXPLAIN THE DIRECTED ACYCLIC GRAPH.
    Directed Acyclic Graph is a finite collateral graphic with no alternating disc.

14. EXPLAIN THE LINEAGE CHART.
    Lineage map reports to the graph for the RDD parent as a whole.

15. EXPLAIN THE IDLE ASSESSMENT IN SPARK.
    The idle assessment, known as call by use, is a strategy that defers compliance until one needs a benefit.

16. EXPLAIN THE ADVANTAGE OF A LAZY EVALUATION.
    To expand the program’s manageability and features.

17. EXPLAIN THE CONCEPT OF “PERSISTENCE”.
    RDD persistence is an ideal technique that saves the results of the RDD assessment.

18. WHAT IS THE MAP-REDUCE LEARNING FUNCTION?
    Map Reduce is a model used for a vast amount of data design.

19. WHEN PROCESSING INFORMATION FROM HDFS, IS THE CODE PERFORMED NEAR THE DATA?
    Yes, in most situations, it is. It creates executors that are close to paths that contain data.

20. DOES SPARK ALSO CONTAIN THE STORAGE LAYER?
    No, it doesn’t have a disc layer, but it lets you use many data sources.

These 20 Spark coding interview questions are some of the most important ones! Make sure you revise them before your interview!

21. WHERE DOES THE SPARK DRIVER OPERATE ON YARN?
    The Spark driver operates on the client computer.

22. HOW IS MACHINE LEARNING CARRIED OUT IN SPARK?
    Machine learning is carried out in Spark with the help of MLlib. It’s a scalable machine learning library provided by Spark.

23. EXPLAIN WHAT A PARQUET FILE IS.
    Parquet is a column structure file that is supported by many other data processing classes.

24. EXPLAIN THE LINEAGE OF THE RDD.
    The lineage of RDD is that it does not allow memory duplication of records.

25. EXPLAIN THE SPARK EXECUTOR.
    Executors are worker nodes’ processes in charge of running individual tasks in a given Spark job.

26. EXPLAIN THE MEANING OF A WORKER’S NODE OR ROUTE.
    A worker node or path corresponds to any node that can stick the application symbol in many nodes.

27. EXPLAIN THE SPARSE VECTOR.
    A sparse vector has two parallel formats, one for indices and the other for values.

28. IS IT POSSIBLE TO STICK WITH THE APACHE SPARK ON APACHE MESOS?
    Yes, you should adhere to the clusters of resources that have Mesos.

29. EXPLAIN THE APACHE SPARK ACCUMULATORS.
    Accumulators are predictions that are taken away only by a non-linear method of thinking and alternate processes.

30. WHY IS THERE A NEED FOR TRANSMITTING VARIABLES WHILE USING APACHE SPARK?
    Because it reads, except for variables, the relevant in-memory array on each machine tool.

31. EXPLAIN THE IMPORT OF SLIDING WINDOW PERFORMANCE.
    Sliding Window withholds transmission of numerical information packets between different data networks on machines.

32. EXPLAIN THE DISCRETIZED STREAM OF APACHE SPARK.
    Discretized Stream is a fundamental abstraction acceptable to Spark Streaming.

Make sure you revise these Spark streaming interview questions before moving onto the next set of questions.

33. STATE THE DISTINCTION BETWEEN SQL AND HQL.
    SparkSQL is a critical component of the Spark Core engine, whereas HQL is a combination of OOPS with the Relational database concept.

NOTE: This is one of the most widely asked Spark SQL interview questions.

34. EXPLAIN THE USE OF BLINK DB.
    Blink DB is a query machine tool that helps you to run SQL queries.

35. EXPLAIN THE NODE OF THE APACHE SPARK WORKER.
    The node of a worker is any path that can run the application code in a cluster.

NOTE: This is one of the most crucial Spark interview questions for experienced candidates.

36. EXPLAIN THE FRAMEWORK OF THE CATALYST.
    The Catalyst Concept is a modern optimization framework in Spark SQL.

37. DOES SPARK USE HADOOP?
    Spark has its own cluster administration list and only uses Hadoop for collection.

38. WHY DOES SPARK USE AKKA?
    Spark simply uses Akka for scheduling.

39. EXPLAIN THE WORKER NODE OR PATHWAY.
    A node or route that can run the Spark program code in a cluster can be called a worker or porter node.

40. EXPLAIN WHAT YOU UNDERSTAND ABOUT THE RDD SCHEMA?
    Schema RDD consists of a row factor with schema data in both directions with details in each column.

41. WHAT IS THE FUNCTION OF SPARK ENGINE?
    Spark Engine schedules for distribution and monitoring.

42. WHICH IS THE APACHE SPARK DEFAULT LEVEL?
    The cache() method is used for the default storage level, which is StorageLevel.

43. CAN YOU USE SPARK TO PERFORM THE ETL PROCESS?
    Yes, Spark may be used for the ETL operation as Spark supports Java, Scala, R, and Python.

44. WHICH IS THE NECESSARY DATA STRUCTURE OF SPARK?
    The Data Framework is essential for the fundamental development of Spark data.

45. CAN YOU FLEE APACHE SPARK ON APACHE MESOS?
    Yes, it can flee Apache Spark on the hardware clusters that Mesos charges.

46. EXPLAIN THE SPARK MLLIB.
    MLlib is the acronym of Spark’s scalable machine learning library.

47. EXPLAIN DSTREAM.
    D Stream is a high-level concentration described by Spark Streaming.

48. WHAT IS ONE ADVANTAGE OF PARQUET FILES?
    Parquet files are adequate for large-scale queries.

49. EXPLAIN THE FRAMEWORK OF THE CATALYST.
    The Catalyst is a structure that represents and manipulates a data frame graph.

50. EXPLAIN THE SET OF DATA.
    Spark Datasets is an extension of the Data Frame API.

51. WHAT ARE DATAFRAMES?
    They are a list of data that is arranged in the named columns.

52. EXPLAIN THE CONCEPT OF THE DDR (RESILIENT DISTRIBUTED DATASET). ALSO, HOW CAN YOU BUILD RDDS IN APACHE SPARK?
    The RDD or Resilient Distribution Dataset is a fault-tolerant array of operating elements capable of running parallel. Any partitioned data in the RDD can be distributed. There are two kinds of RDDs:

Hadoop Datasets – Perform functions for each file record in HDFS (Hadoop Distributed File System) or other forms of storage structures.
Parallelized  Collections – Extensive RDDs running parallel to each other
There are two ways to build an RDD in Apache Spark:

By paralleling the array in the Driver program. It uses the parallelize() function of SparkContext.
Through accessing an arbitrary dataset from any external storage, including HBase, HDFS, and a shared file system.
53. DEFINE SPARK.
    Spark is a parallel system for data analysis. It allows a quick, streamlined big data framework to integrate batch, streaming, and immersive analytics.

54. WHY USE SPARK?
    Spark is a 3rd gen distributed data processing platform. It’s a centralized big data approach for big data processing challenges such as batch, interactive or streaming processing. It can ease a lot of big data issues.

55. WHAT IS RDD?
    The primary central abstraction of Spark is called Resilient Distributed Datasets. Resilient Distributed Datasets are a set of partitioned data that fulfills these characteristics. The popular RDD properties are immutable, distributed, lazily evaluated, and catchable.

56. THROW SOME LIGHT ON WHAT IS IMMUTABLE.
    If a value has been generated and assigned, it cannot be changed. This attribute is called immutability. Spark is immutable by nature. It does not accept upgrades or alterations. Please notice that data storage is not immutable, but the data content is immutable.

57. HOW CAN RDD SPREAD DATA?
    RDD can dynamically spread data through various parallel computing nodes.

58. WHAT ARE THE DIFFERENT ECOSYSTEMS OF SPARK?
    Some typical Spark ecosystems are:

Spark SQL for developers of SQL
Spark Streaming for data streaming
MLLib for algorithms of machine learning
GraphX for computing of graph
SparkR to work on the Spark engine
BlinkDB, which enables dynamic queries of large data
GraphX, SparkR, and BlinkDB are in their incubation phase.

59. WHAT ARE PARTITIONS?
    Partition is a logical partition of records, an idea taken from Map-reduce (split) in which logical data is directly obtained to process data. Small bits of data can also help in scalability and fasten the operation. Input data, output data & intermediate data are all partitioned RDDs.

60. HOW DOES SPARK PARTITION DATA?
    Spark uses the map-reduce API for the data partition. One may construct several partitions in the input format. HDFS block size is partition size (for optimum performance), but it’s possible to adjust partition sizes like Split.

61. HOW DOES SPARK STORE DATA?
    Spark is a computing machine without a storage engine in place. It can recover data from any storage engine, such as HDFS, S3, and other data services.

62. IS IT OBLIGATORY TO LAUNCH THE HADOOP PROGRAM TO RUN A SPARK?
    It is not obligatory, but there is no special storage in Spark. Thus you must use the local file system to store the files. You may load and process data from a local device. Hadoop or HDFS is not needed to run a Spark program.

63. WHAT’S SPARKCONTEXT?
    When the programmer generates RDDs, SparkContext connects to the Spark cluster to develop a new SparkContext object. SparkContext tells Spark to navigate the cluster. SparkConf is the central element for creating an application for the programmer.

64. HOW IS SPARKSQL DIFFERENT FROM HQL AND SQL?
    SparkSQL is a special part of the SparkCore engine that supports SQL and HiveQueryLanguage without modifying syntax. You will enter the SQL table and the HQL table.

65. WHEN IS SPARK STREAMING USED?
    It is an API used for streaming data and processing it in real-time. Spark streaming collects streaming data from various services, such as web server log files, data from social media, stock exchange data, or Hadoop ecosystems such as Kafka or Flume.

66. HOW DOES THE SPARK STREAMING API WORK?
    The programmer needs to set a specific time in the setup, during which the data that goes into the Spark is separated into batches. The input stream (DStream) goes into the Spark stream.

The framework splits into little pieces called batches, then feeds into the Spark engine for processing. The Spark Streaming API sends the batches to the central engine. Core engines can produce final results in the form of streaming batches. Production is in the form of batches, too. It allows the streaming of data and batch data for processing.

67. WHAT IS GRAPHX?
    GraphX is a Spark API for editing graphics and arrays. It unifies ETL, analysis, and iterative graph computing. Its fastest graphics system offers error tolerance and easy use without the need for special expertise.

68. WHAT IS FILE SYSTEM API?
    The File System API can read data from various storage devices, such as HDFS, S3, or Local FileSystem. Spark utilizes the FS API to read data from multiple storage engines.

69. WHY ARE PARTITIONS IMMUTABLE?
    Each transformation creates a new partition. Partitions use the HDFS API such that the partition is immutable, distributed, and error-tolerant. Partitions are, therefore, conscious of the location of the results.

70. DISCUSS WHAT IS FLATMAP AND MAP IN SPARK.
    A map is a simple line or row to process the data. Each input object can be mapped to various output items in FlatMap (so the function should return a Seq rather than a unitary item). So most often, it is used to return the Array components.

71. DEFINE BROADCAST VARIABLES.
    Broadcast variables allow the programmer to have a read-only variable cached on each computer instead of sending a copy of it with tasks. Spark embraces two kinds of mutual variables: broadcast variables and accumulators. Broadcast variables are stored as Array Buffers, which deliver read-only values to the working nodes.

72. WHAT ARE SPARK ACCUMULATORS IN CONTEXT TO HADOOP?
    Off-line Spark debuggers are called accumulators. Spark accumulators are equivalent to Hadoop counters and can count the number of activities. Only the driver program can read the value of the accumulator, not the tasks.

73. WHEN CAN APACHE SPARK BE USED? WHAT ARE THE ADVANTAGES OF SPARK OVER MAPREDUCE?
    Spark is quite fast. Programs run up to 100x faster than Hadoop MapReduce in memory. It appropriately uses RAM to achieve quicker performance.

In Map Reduce Paradigm, you write many Map-reduce tasks and then link these tasks together using the Oozie/shell script. This process is time-intensive, and the role of map-reducing has a high latency.

Frequently, converting production from one MR job to another MR job can entail writing another code since Oozie might not be enough.

In Spark, you can do anything using a single application/console and get the output instantly. Switching between ‘Running something on a cluster’ and ‘doing something locally’ is pretty simple and straightforward. All this leads to a lower background transition for the creator and increased efficiency.

Spark sort of equals MapReduce and Oozie when put in conjunction.

The above-mentioned Spark Scala interview questions are pretty popular and are a compulsory read before you go for an interview.

74. IS THERE A POINT OF MAPREDUCE LEARNING?
    Yes. It serves the following purposes:

MapReduce is a paradigm put to use by several big data tools, including Spark. So learning the MapReduce model and transforming a problem into a sequence of MR tasks is critical.
When data expands beyond what can fit into the cluster memory, the Hadoop Map-Reduce model becomes very important.
Almost every other tool, such as Hive or Pig, transforms the query to MapReduce phases. If you grasp the Mapreduce, you would be better able to refine your queries.
75. WHAT ARE THE DRAWBACKS OF SPARK?
    Spark uses memory. The developer needs to be cautious about this. Casual developers can make the following mistakes:

It might end up running everything on the local node instead of spreading work to the cluster.
It could reach some web services too many times by using multiple clusters.
The first dilemma is well addressed by the Hadoop Map reduce model.
A second error is also possible in Map-Reduce. When writing Map-Reduce, the user can touch the service from the inside of the map() or reduce() too often. This server overload is also likely when using Spark.

Q.4 What are the limitations of Spark?

Does not have its file management system. Thus, it needs to integrate with Hadoop or other cloud-based data platforms.
In-memory capability can become a bottleneck. Especially when it comes to cost-efficient processing of Bigdata.
Memory consumption is very high. And the issues for the same are not handled in a user-friendly manner. d. It requires large data.
MLlib lack in some available algorithms, for example, Tanimoto distance.
Read more Apache Spark Limitations in detail.

Q.5 List the languages supported by Apache Spark.

Apache Spark Supports the following Languages: Scala, Java, R, Python.

Q.6 What are the cases where Apache Spark surpasses Hadoop?

The data processing speed increases in the Apache Spark. This is because of the support of in-memory computation by the system. Thus, the performance of the system increase by 10x-1000x times. Apache Spark uses various languages for distributed application development.
On the top of spark core, various libraries are present. These libraries enable workload that uses streaming, SQL, graph and machine learning. Some of these workloads are also supported by Hadoop. Spark facilitates the development by joining them into the same application. Apache Spark adopts micro-batching. Which is essentially used for handling near real time processing data model.

Q.7 Compare Hadoop and Spark.

Cost Efficient – In Hadoop, during replication, a large number of servers, huge amount of storage, and the large data center is required. Thus, installing and using Apache Hadoop is expensive. While using Apache Spark is a cost effective solution for big data environment.
Performance – The basic idea behind Spark was to improve the performance of data processing. And Spark did this to 10x-100x times. And all the credit of faster processing in Spark goes to in-memory processing of data. In Hadoop, the data processing takes place in disc while in Spark the data processing takes place in memory. It moves to the disc only when needed. The Spark in-memory computation is beneficial for iterative algorithms. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow while the processing speed of Apache is faster as it supports micro-batching.
Ease of development – The core in Spark is the distributed execution engine. Various languages are supported by Apache Spark for distributed application development. For example, Java, Scala, Python, and R. On the top of spark core, various libraries are built that enables workload. they make use of streaming, SQL, graph and machine learning. Hadoop also supports some of these workloads but Spark eases the development by combining all into the same application. d. Failure recovery: The method of Fault
Failure recovery – The method of Fault Recovery is different in both Apache Hadoop and Apache Spark. In Hadoop after every operation data is written to disk. The data objects are stored in Spark in RDD distributed across data cluster. The RDDs are either in memory or on disk and provides full recovery from faults or failure.
File Management System – Hadoop has its own File Management System called HDFS (Hadoop Distributed File System). While Apache Spark an integration with one, it may be even HDFS. Thus, Hadoop can run over Apache Spark.
Computation model – Apache Hadoop uses batch processing model i.e. it takes a large amount of data and processes it. But Apache Spark adopts micro-batching. Must for handling near real time processing data model. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow. The processing speed of Apache is faster as it supports micro-batching.
Lines of code – Apache Hadoop has near about 23, 00,000 lines of code while Apache Spark has 20,000 lines of code.
Caching – By caching partial result in memory of distributed workers Spark ensures low latency computations. While MapReduce is completely disk oriented, there is no provision of caching.
Scheduler – Because of in-memory computation in Spark, it acts as its own flow scheduler. While with Hadoop MapReduce we need an extra job scheduler like Azkaban or Oozie so that we can schedule complex flows.
Spark API – Because of very Strict API in Hadoop MapReduce, it is not versatile. But since Spark discards many low-level details it is more productive.
Window criteria – Apache Spark has time-based window criteria. But Apache Hadoop does not have window criteria since it does not support streaming.
Faster – Apache Hadoop executes job 10 to 100 times faster than Apache Hadoop MapReduce.
License – Both Apache Hadoop and Apache MapReduce has a License Version 2.0.
DAG() – In Apache Spark, there is cyclic data flow in machine learning algorithm, which is a direct acyclic graph. While in Hadoop MapReduce data flow does not have any loops, rather it is a chain of the image.
Memory Management – Apache Spark has automatic memory management system. While Memory Management in Apache Hadoop can be either statistic or dynamic.
Iterative Processing – In Apache Spark, the data iterates in batches. Here processing and scheduling of each iteration are separate. While in Apache Hadoop there is no provision for iterative processing.
Latency – The time taken for processing by Apache Spark is less as compared to Hadoop since it caches its data on memory by means of RDD, thus the latency of Apache Spark is less as compared to Hadoop.
Spark Interview Questions and Answers
Spark Interview Questions and Answers – Spark Ecosystem

Read Hadoop vs Spark in detail.

Q.8 What are the components of Spark Ecosystem?

The various components of Apache Spark are:

Spark Core – Spark Core is the foundation of the whole project. All the functionality that is in Spark, is present on the top of Spark Core.
Spark Streaming – It allows fault-tolerant streaming of live data streams. It is an add-on to core Spark API. Here it makes use of micro-batching for real-time streaming. Thus it packages live data into small batches and delivers to the batch system for processing.
Spark SQL – Spark SQL component is distributed framework for structured data processing. Using Spark SQL Spark gets more information about the structure of data and the computation being performed. As a result, by using this information Spark can perform extra optimization.
Spark MLlib – MLlib is a scalable learning library that discusses both: High-quality algorithm, High speed. The motive behind MLlib creation is to make machine learning scalable and easy. Thus. it contains machine learning libraries that have an implementation of various machine learning algorithms.
Spark GraphX – GraphX is API for graphs and graph parallel execution. In order to support graph computation, graphX contains set of fundamental operators like sub graph, joinvertices and an optimized variant of Pregel API. Also, clustering, classification, traversal, searching, and pathfinding is possible in graphX.
SparkR – SparkR is Apache Spark 1.4 release. The key component of SparkR is SparkR DataFrame. Data frames are a fundamental data structure for data processing in R and the concept of data frames extends to other languages with libraries like Pandas etc.
Read Apache Spark Ecosystem Components in detail.

Q.9 What is Spark Core?

Spark Core is a common execution engine for Spark platform. It provides parallel and distributed processing for large data sets. All the components on the top of it. Spark core provides speed through in-memory computation. And for ease of development, it also supports Java, Scala and Python APIs.
RDD is the basic data structure of Spark Core. RDDs are immutable, a partitioned collection of record that can operate in parallel. We can create RDDs by transformation on existing RDDs. Also by loading an external dataset from stable storage like HDFS or HBase, we can form RDD.

Q.10 How is data represented in Spark?
The data can be represented in three ways in Apache Spark: RDD, DataFrame, DataSet.

RDD: RDD stands for Resilient Distributed Datasets. It is also a Read-only partition collection of records. RDD is the fundamental data structure of Spark. Hence, RDDs can only be created through deterministic operation on either:

Data in stable storage.
Parallelizing already existing collection in driver program.
Other RDDs. RDD allows programmer perform in-memory computations on large clusters in a fault-tolerant manner. Thus, speed up the task.
DataFrame: Unlike an RDD, the data organizes into named columns, like a table in a relational database. It is also an immutable distributed collection of data. DataFrame allows developers to impose a structure onto a distributed collection of data, therefore, allowing higher-level abstraction.

DataSet: Dataset is an extension of DataFrame API which provides type-safe, object-oriented programming interface. DataSet also takes advantage of Spark’s Catalyst optimizer by exposing expressions and data fields to a query planner.

Q.11 What are the abstractions of Apache Spark?

The main abstraction provided by Apache Spark is Resilient Distributed Dataset. RDDs are fault tolerant in nature. We cannot improve the changes made in RDD. RDDs creation starts with the file in a file system like Hadoop file system and then transforming it. The shared variable is the second abstraction provided by Apache Spark. We can use this in parallel operations.
Read about Apache Spark RDD in detail.

Q.12 Explain the operations of Apache Spark RDD.

Apache Spark RDD supports two types of operations: Transformations and Actions-

Transformations are lazy operations on an RDD that create one or many new RDDs. For example Map, filter, reduceByKey etc creates new RDD. RDD create a new dataset from an existing one. That executes on demand. That means they compute lazily. Whenever we perform any transformation on RDD, it creates a new RDD each time.
Action returns final result of RDD computations. It triggers execution using lineage graph to load the data into original RDD. After application of all the intermediate transformation, it gives the final result to driver program or writes it out to file system. Upon applying Actions on an RDD non-RDD values gets generate.
Read about RDD transformations and Actions in detail.
Q.13 How many types of Transformation are there?

There are two types of transformation namely narrow transformation and wide transformation.

Narrow Transformation is the result of map, filter and such that the data is from a single partition only. As a result, the data is self-sustained. The RDD that we get as an output has a partition with records that originate from a single partition in the parent RDD.
Wide transformations are the result of groupByKey and reduceByKey. The data that we will need to compute the records in a single partition is kept at many partitions of the parent RDD.
Apache Spark Narrow and Wide Transformations
Apache Spark Narrow and Wide Transformations

Q.14 In how many ways RDDs can be created? Explain.

There are three ways to create an RDD:

Parallelized collection – In the initial stages, the RDD is generally created by parallelized collection. In this method, we take the existing collection in the program and pass it to parallelize() method of SparkContext. The thing that should be noticed in the parallelized collection is the number of partition the dataset is cut into. For each partition of the cluster, Spark will run one task. Spark set a number of partition based on our cluster. But the number of partitions can also be set manually. Pass the number of partition as the second parameter for manual partition. e.g. sc.parallelize(data, 20), here we have manually given a number of partition as 20.
External Datasets (Referencing a dataset) – In Spark one can create distributed dataset from any data source supported by Hadoop. For example the local file system, HDFS, Cassandra, HBase etc. In this, the data is loaded from the external dataset. To create text file RDD we can use SparkContext textFile method. It takes URL of the file and read it as a collection of line. URL can be a local path on the machine or a hdfs://, s3n://, etc.
Creating RDD from existing RDD – Transformation converts one RDD into another RDD. By using transformation we can create an RDD from existing RDD. Transformation acts as a function that intakes an RDD and produces one.
Read the ways to create RDD in Spark in detail.
Q.15 What are Paired RDD?

Paired RDDs are the RDD-containing key-value pair. A key-value pair (KYP) contains two linked data item. Here Key is the identifier and Value are the data corresponding to the key value.

Q.16 What is meant by in-memory processing in Spark?

In in-memory computation, we keep data in random access memory in place of some slow disk drives. The processing of data is in parallel. Using this we can also identify the pattern, analyze large data Spark offers in in-memory capabilities. As a result, this increases the processing speed because it retrieves the data from memory in place of the disk. Also, the execution time of the process decreases. Keeping the data in-memory improves the performance by the order of magnitudes.
The main abstraction of Spark is its RDDs. Also, we can cache RDD using the cache() or persist() method. In cache() method all the RDD are in-memory. The dissimilarity between cache() and persist() is the default storage level. For cache() it is MEMORY_ONLY. While in persist() there are various storage levels like:

MEMORY_ONLY,
MEMORY_AND_DISK,
MEMORY_ONLY_SER
MEMORY_AND_DISK_SER
DISK_ONLY
Read Spark in-memory processing in detail.

Q.17 How is fault tolerance achieved in Apache Spark?

The basic fault-tolerant semantic of Spark are:

Since all RDD is an immutable data set. Each RDD keeps track of the lineage of the deterministic operation that employee on fault-tolerant input dataset to create it.
If any partition of an RDD is lost due to a worker node failure, then that partition can be re-computed from the original fault-tolerant dataset using the lineage of operations.
Assuming that all of the RDD transformations are deterministic, the data in the final transformed RDD will always be the same irrespective of failures in the Spark cluster.
To achieve fault tolerance for all the generated RDDs, the achieved data replicates among multiple Spark executors in worker node in the cluster. This result in two types of data that should recover in the event of failure:

Data received and replicated – In this, the data replicates on one of the other nodes. Thus we can retrieve data when a failure occurs.
Data received but buffered for replication – the data does not replicate. Thus the only way to recover fault is by retrieving it again from the source.
Failure can also occur in worker and driver nodes.

Failure of worker node – The node which runs the application code on the cluster is worker node. These are the slave nodes. Any of the worker nodes running executor can fail, thus resulting in loss of in-memory data. If any receivers were running on failed nodes, then their buffer data will vanish.
Failure of driver node – If the driver node running the Spark Streaming application fails, then there is the loss of SparkContent. All executors along with their in-memory data vanishes.
Spark Interview Questions and Answers - Lazy Evaluation Feature
Spark Interview Questions and Answers – Lazy Evaluation Feature

Read about Spark Fault tolerance in detail.
Q.18 What is Directed Acyclic Graph(DAG)?

RDDs are formed after every transformation. At high level when we apply action on these RDD, Spark creates a DAG. DAG is a finite directed graph with no directed cycles.

There are so many vertices and edges, where each edge is directed from one vertex to another. It contains a sequence of vertices such that every edge is directed from earlier to later in the sequence. It is a strict generalization of MapReduce model. DAG lets you get into the stage and expand in detail on any stage.

In the stage view, the details of all RDDs that belong to that stage are expanded.
Read DAG in Apache Spark in detail.
Q.19 What is lineage graph?

Lineage graph refers to the graph that has all the parent RDDs of an RDD. It is the result of all the transformation on the RDD. It creates a logical execution plan.

A logical execution plan is a plan that starts with the very first RDD. Also, it does not have any dependency on any RDD. It then ends at the RDD which produces the result of an action that has been called to execute.

Q.20 What is lazy evaluation in Spark?

The lazy evaluation known as call-by-need is a strategy that delays the execution until one requires a value. The transformation in Spark is lazy in nature. Spark evaluate them lazily. When we call some operation in RDD it does not execute immediately; Spark maintains the graph of which operation it demands. We can execute the operation at any instance by calling the action on the data. The data does not loads until it is necessary.

Read about Spark Lazy Evaluation in detail.

Q.21 What are the benefits of lazy evaluation?

Using lazy evaluation we can:

Increase the manageability of the program.
Saves computation overhead and increases the speed of the system.
Reduces the time and space complexity.
provides the optimization by reducing the number of queries.
Q.22 What do you mean by Persistence?

RDD persistence is an optimization technique which saves the result of RDD evaluation. Using this we save the intermediate result for further use. It reduces the computation overhead. We can make persisted RDD through cache() and persist() methods. It is a key tool for the interactive algorithm. Because, when RDD is persisted each node stores any partition of it that it computes in memory. Thus makes it reusable for future use. This process speeds up the further computation ten times.
Read about RDD Persistence and Caching Mechanism in detail.

Q.23 Explain various level of persistence in Apache Spark.

The persist method allows seven storage level:

MEMORY_ONLY – Store RDD as deserialized Java objects. If the RDD does not fit in memory, then some partitions will not be cached and will recompute on the fly each time needed. This is the default level.
MEMORY_AND_DISK – Store RDD as deserialized Java objects. If the RDD does not fit in memory, store the partitions that don’t fit on the disk, and read them from there when they’re needed.
MEMORY_ONLY_SER (Java and Scala) – Store RDD as serialized Java objects. This is more space-efficient than deserialized objects. especially when using a fast serializer. but it is hard for CPU to read.
MEMORY_AND_DISK_SER(Java and Scala) – Like MEMORY_ONLY_SER, but spills partitions that don’t fit in memory to disk.
DISK_ONLY – It stores the RDD partitions only on disk.
MEMORY_ONLY_2, MEMORY_AND_DISK_2 – It replicates each partition on two cluster nodes.
OFF_HEAP – Like MEMORY_ONLY_SER, but store the data in off-heap memory. This requires enabling of off-heap memory.
Q.24 Explain the run-time architecture of Spark?

The components of the run-time architecture of Spark are as follows:
a. The driver
b. Cluster manager
c. Executors

The Driver – The main() method of the program runs in the driver. The process that runs the user code which creates RDDs performs transformation and action, and also creates SparkContext is called diver. When the Spark Shell is launched, this signifies that we have created a driver program. The application finishes, as the driver terminates. Finally, driver program splits the Spark application into the task and schedules them to run on the executor.

Cluster Manager –  Spark depends on cluster manager to launch executors. In some cases, even the drivers are launched by cluster manager. It is a pluggable component in Spark. On the cluster manager, the Spark scheduler schedules the jobs and action within a spark application in FIFO fashion. Alternatively, the scheduling can also be done in Round Robin fashion. The resources used by a Spark application can also be dynamically adjusted based on the workload. Thus, the application can free unused resources and request them again when there is a demand. This is available on all coarse-grained cluster managers, i.e. standalone mode, YARN mode, and Mesos coarse-grained mode.

The Executors –  Each task in the Spark job runs in the Spark executors. thus, Executors are launched once in the beginning of Spark Application and then they run for the entire lifetime of an application. Even after the failure of Spark executor, the Spark application can continue with ease.
There are two main roles of the executors:

Runs the task that makes up the application and returns the result to the driver.
Provide in-memory storage for RDDs that the user program cache.
Q.25 Explain various cluster manager in Apache Spark?

The various cluster manages supported by Apache Spark are Standalone, Hadoop YARN, Apache Mesos.

Standalone Cluster Manager – Standalone is a simple cluster manager of Spark that makes it easy to setup a cluster. In many cases, it is the simplest way to run Spark application in a clustered environment. It has masters and number of workers with the configured amount of memory and CPU cores. In standalone cluster mode, Spark allocates resources based on the core. It has the constraints that only one executor can be allocated on each worker per application.
Hadoop YARN – YARN became the sub-project of Hadoop in the year 2012. The key idea behind YARN is to bifurcate the functionality of resource manager and job scheduling into different daemons. The plan is to have a Global Resource Manager (RM) and per-application Application Master (AM). An application is either a DAG of graphs or an individual job. The data computation framework is a combination of the ResourceManager and the NodeManager.
Apache Mesos – Apache Mesos handles the workload in a distributed environment.It is healthful for deployment and management of applications in large-scale cluster environments. Mesos clubs together the existing resource of the machines/nodes into a cluster, as a result from this a variety of workloads may utilize. This is known as node abstraction, thus it decreases an overhead of allocating a specific machine for different workloads. It is resource management platform for Hadoop and Big Data cluster. In some way, Apache Mesos is the reverse of virtualization. Because in virtualization one physical resource divides into multiple virtual resources, while in Mesos multiple physical resources groups into a single virtual resource.
Spark Interview Questions and Answers - Hadoop Compatibility
Spark Interview Questions and Answers – Hadoop Compatibility

Read about Spark Cluster Managers in detail.

Q.26 In how many ways can we use Spark over Hadoop?

In three ways we can run Spark over Hadoop: Standalone, YARN, SIMR

Standalone – In this, we can either divide resource on all machines or subset of machines in Hadoop cluster.
YARN – We can run Spark on YARN without any pre-requisites. Thus, we can integrate Spark in Hadoop stack and take an advantage of facilities of Spark.
SIMR (Spark in MapReduce) – Another way to do this is by launching Spark job inside Map reduce. With SIMR we can use Spark shell in few minutes after downloading it. This reduces the overhead of deployment, and we can play with Spark.
Read about Spark Hadoop Compatibility in detail.

Q.27 What is YARN?

YARN became the sub-project of Hadoop in the year 2012. It is also known as MapReduce 2.0. The key idea behind YARN is to bifurcate the functionality of resource manager and job scheduling into different daemons. The plan is to have a Global Resource Manager(RM) and per-application Application Master (AM). An application is either a DAG of graphs or an individual job.
The data computation framework is a combination of the ResourceManager and the NodeManager.

The Resource Manager manages resource among all the applications in the system. The Resource Manager has scheduled and Application Manager. The Scheduler allocates resource to the various running application. The Scheduler is pure Scheduler if it performs no monitoring or tracking of the status of the application. The Application Manager manages applications across all the nodes. NodeManager contains ApplicationMaster and container. A container is a place where a unit of work happens. Each task of MapReduce runs in one container. The per-application ApplicationMaster is a framework specific library. It negotiates resources from the ResourceManager and continues with NodeManager(s) to execute and watch the tasks. Application or job requires one or more containers. NodeManager looks after containers, resource usage (CPU, memory, disk, and network) and reporting this to the ResourceManager.

Read about YARN in detail.

Q.28 How can we launch Spark application on YARN?

There are two deployment modes to launch Spark application on YARN: the cluster mode and the client mode.

In cluster mode, the Spark driver runs inside Application Master Process and this is managed by YARN on the cluster.
In client mode, the driver runs in the client process. The Application Master requests a resource from YARN. And it provides it to the driver program.
Q.29 Define Partition in Apache Spark.

Partition refers to, a logical block of large distributed Dataset. Logically partitioning the data and distributing it over the cluster provides parallelism. It also minimizes network traffic for sending data between executors. It determines how to access the entire hardware resources during job execution. RDD is automatically partitioned in Spark. We can change the size and number of the partition.

Read Spark Catalyst Optimizer in detail.

Q.30 What are shared variables?
Shared variables are one of the abstractions of Apache Spark. Shared variables can be used in parallel operations.

Whenever Spark runs a function in parallel as a set of tasks on different nodes, each variable that is used in function are circulated to each task. Sometimes there is a need to share the variables across the tasks or between the task and the driver program.

Apache Spark supports two types of shared variables namely broadcast variable and accumulator.
Using broadcast variables we cache a value in memory on all nodes while we add accumulators to, such as counters and sums.

Q.31 What is Accumulator?

The accumulator is the type of Shared variable that is only added through associative and commutative operations. Using accumulator we can update the value of the variable while executing. We can also implement counters (as in MapReduce) or sums using an accumulator. Users can create named or unnamed accumulator. We can create numeric accumulator by calling SparkContext.longAccumulator() or SparkContext.doubleAccumulator() for Long or Double.

Q.32 What is the difference between DSM and RDD?

a) READ

RDD: In RDD the read operation is coarse grained or fine grained. In coarse-grained we can transform the whole dataset but not an individual element. While in fine-grained we do the transformation of an individual element on a dataset.
Distributed Shared Memory: The read operation in Distributed shared memory is fine-grained.
b) Write:

RDD: The write operation is coarse-grained in RDD.
Distributed Shared Memory: In distributed shared system the write operation is fine grained.
c) Consistency:

RDD: The consistency of RDD is trivial meaning it is immutable in nature. Any changes made to an RDD cannot roll back, it is permanent. So the level of consistency is high.
Distributed Shared Memory: The system guarantees that if the programmer follows the rules, the memory will be consistent. It also guarantees that the results of memory operations will be predictable.
d) Fault-recovery mechanism:

RDD: Using lineage graph at any point in time we can easily find the lost data in an RDD.
Distributed Shared Memory: Fault tolerance is achieved by a checkpointing technique. It allows applications to roll back to a recent checkpoint rather than restarting.
e) Straggler mitigation: Stragglers, in general, are those tasks that take more time to complete than their peers.

RDD: in RDD it is possible to mitigate stragglers using backup task.
Distributed Shared Memory: It is quite difficult to achieve straggler mitigation.
f) Behavior if not enough RAM:

RDD: If there is not enough space to store RDD in RAM then the RDDs are shifted to disk.
Distributed Shared Memory: In this type of system the performance decreases if the RAM runs out of storage.
Q.33 How can data transfer be minimized when working with Apache Spark?

By minimizing data transfer and avoiding shuffling of data we can increase the performance. In Apache Spark, we can minimize the data transfer in three ways:

By using a broadcast variable – Since broadcast variable increases the efficiency of joins between small and large RDDs. the broadcast variable allows keeping a read-only variable cached on every machine in place of shipping a copy of it with tasks. We create broadcast variable v by calling SparlContext.broadcast(v) and we can access its value by calling the value method.
Using Accumulator – Using accumulator we can update the value of a variable in parallel while executing. Accumulators can only be added through the associative and commutative operation. We can also implement counters (as in MapReduce) or sums using an accumulator. Users can create named or unnamed accumulator. We can create numeric accumulator by calling SparkContext.longAccumulator() or SparkContext.doubleAccumulator() for Long or Double respectively.
By avoiding operations like ByKey, repartition or any other operation that trigger shuffle. we can minimize the data transfer.
Q.34 How does Apache Spark handles accumulated Metadata?

By triggering automatic cleanup Spark handles the automatic Metadata. We can trigger cleanup by setting the parameter “spark.cleaner.ttl“. the default value for this is infinite. It tells for how much duration Spark will remember the metadata. It is periodic cleaner. And also ensure that metadata older than the set duration will vanish. Thus, with its help, we can run Spark for many hours.

Q.35 What are the common faults of the developer while using Apache Spark?

The common mistake by developers are:

Customer hit web-service several time by using multiple clusters.
Customer runs everything on local node instead of distributing it.
Q.36 Which among the two is preferable for the project- Hadoop MapReduce or Apache Spark?

The answer to this question depends on the type of project one has. As we all know Spark makes use of a large amount of RAM and also needs a dedicated machine to provide an effective result. Thus the answer depends on the project and the budget of the organization.

Q.37 List the popular use cases of Apache Spark.

The most popular use-cases of Apache Spark are:
1. Streaming
2. Machine Learning
3. interactive Analysis
4. fog computing
5. Using Spark in the real world

Q.38 What is Spark.executor.memory in a Spark Application?

The default value for this is 1 GB. It refers to the amount of memory that will be used per executor process.
We have categorized the above Spark Interview Questions and Answers for Freshers and Experienced-

Spark Interview Questions and Answers for Fresher – Q.No.1-8, 37
Spark Interview Questions and Answers for Experienced – Q.No. 9-36, 38
Follow this link to read more Spark Basic interview Questions with Answers.

b. Spark SQL Interview Questions and Answers
In this section, we will discuss some basic Spark SQL Interview Questions and Answers.

Q.39 What is DataFrames?

It is a collection of data which organize in named columns. It is theoretically equivalent to a table in relational database. But it is more optimized. Just like RDD, DataFrames evaluates lazily. Using lazy evaluation we can optimize the execution. It optimizes by applying the techniques such as bytecode generation and predicate push-downs.

Read about Spark DataFrame in detail.

Q.40 What are the advantages of DataFrame?

It makes large data set processing even easier. Data Frame also allows developers to impose a structure onto a distributed collection of data. As a result, it allows higher-level abstraction.
Data frame is both space and performance efficient.
It can deal with both structured and unstructured data formats, for example, Avro, CSV etc . And also storage systems like HDFS, HIVE tables, MySQL, etc.
The DataFrame API’s are available in various programming languages. For example Java, Scala, Python, and R.
It provides Hive compatibility. As a result, we can run unmodified Hive queries on existing Hive warehouse.
Catalyst tree transformation uses DataFrame in four phases: a) Analyze logical plan to solve references. b) Logical plan optimization c) Physical planning d) Code generation to compile part of the query to Java bytecode.
It can scale from kilobytes of data on the single laptop to petabytes of data on the large cluster.
Q.41 What is DataSet?

Spark Datasets are the extension of Dataframe API. It creates object-oriented programming interface and type-safety. Dataset is Spark 1.6 release. It makes use of Spark’s catalyst optimizer. It reveals expressions and data fields to a query optimizer. Dataset also influences fast in-memory encoding. It also provides provision for compile time type-safety. We can check for errors in an application when they run.

Q.42 What are the advantages of DataSets?

It provides run-time type safety.
Influences fast in-memory encoding.
It provides a custom view of structured and semi-structured data.
It owns rich semantics and an easy set of domain-specific operations, as a result, it facilitates the use of structured data.
Dataset API decreases the use of memory. As Spark knows the structure of data in the dataset, thus it creates an optimal layout in memory while caching.
Q.43 Explain Catalyst framework.

The Catalyst is a framework which represents and manipulate a DataFrame graph. Data flow graph is a tree of relational operator and expressions. The three main features of catalyst are:

It has a TreeNode library for transforming tree. They are expressed as Scala case classes.
A logical plan representation for relational operator.
Expression library.
The TreeNode builds a query optimizer. It contains a number of the query optimizer. Catalyst Optimizer supports both rule-based and cost-based optimization. In rule-based optimization the optimizer use set of rule to determine how to execute the query. While the cost based optimization finds the most suitable way to carry out SQL statement. In cost-based optimization, many plans are generates using rules. And after this, it computes their cost. Catalyst optimizer makes use of standard features of Scala programming like pattern matching.

Q.44 List the advantage of Parquet files.

It is efficient for large scale queries.
It supports various efficient compression and encoding Scheme.
It consumes less space.
We have categorized the above frequently asked Spark Interview Questions and Answers for Freshers and Experienced-

Spark Interview Questions and Answers for Fresher – Q.No. 39-42
Spark Interview Questions and Answers for Experienced – Q.No. 43, 44
Follow this link to read more basic Spark interview Questions with Answers.

c. Spark Streaming Interview Questions and Answers
In this section, we will discuss some basic Spark Interview Questions and Answers based on Spark Streaming.

Q.45 What is Spark Streaming?

Through Spark streaming, we achieve fault tolerant processing of live data stream. The input data can be from any source. For example, like Kafka, Flume, kinesis, twitter or HDFS/S3. It gives the data to filesystems, databases, and live dashboards after processing. The working of Spark Streaming is as under:

Spark Streaming takes in the live data.
The input data stream is divided into batches of input data.
The Spark engine processes the batches of input data. The final result is also in batches.
Q.46 What is DStream?

DStream is the high-level abstraction provided by Spark Streaming. It represents a continuous stream of data. Thus, DStream is internally a sequence of RDDs. There are two ways to create DStream:

by using data from different sources such as Kafka, Flume, and Kinesis.
by applying high-level operations on other DStreams.
Q.47 Explain different transformation on DStream.

DStream is a basic abstraction of Spark Streaming. It is a continuous sequence of RDD which represents a continuous stream of data. Like RDD, DStream also supports many transformations which are available on normal Spark RDD. For example, map(func), flatMap(func), filter(func) etc.

Q.48 Does Apache Spark provide checkpointing?

Yes, Apache Spark provides checkpointing. Apache supports two types of checkpointing:

Reliable Checkpointing: It refers to that checkpointing in which the actual RDD is saved in the reliable distributed file system, e.g. HDFS. To set the checkpoint directory call: SparkContext.setCheckpointDir(directory: String). When running on the cluster the directory must be an HDFS path since the driver tries to recover the checkpointed RDD from a local file. While the checkpoint files are actually on the executor’s machines.
Local Checkpointing: In this checkpointing, in Spark Streaming or GraphX we truncate the RDD lineage graph in Spark. In this, the RDD is persisted to local storage in the executor.
Q.49 What is write ahead log(journaling)?

The write-ahead log is a technique that provides durability in a database system. It works in the way that all the operation that applies on data, we write it to write-ahead log. The logs are durable in nature. Thus, when the failure occurs we can easily recover the data from these logs. When we enable the write-ahead log Spark stores the data in fault-tolerant file system.

Q.50 What is a reliable and unreliable receiver in Spark?

Reliable Receiver – A reliable receiver acknowledges to the source on receiving data and stores it. Implementing this receiver involves examining of the semantics of source acknowledgments.
Unreliable Receiver – An unreliable receiver does not send an acknowledgment to a source. It is for sources that do not bear an acknowledgment. It is also for reliable sources when one does not want to enter the complexity of acknowledgment.
We have categorized the above Spark Interview Questions and Answers for Freshers and Experienced-

Spark Interview Questions and Answers for Fresher – Q.No. 45-47
Spark Interview Questions and Answers for Experienced – Q.No. 48-50
d. Spark MLlib Interview Questions and Answers
Here are some Spark Interview Questions and Answers for freshers and experienced based on MLlib.

Q.51 What is Spark MLlib?

MLlib is the name of Spark’s machine learning library. The various tools provided by MLlib are:

ML Algorithms: It contains common learning algorithms such as classification, regression, etc.
Featurization: it has tools for feature extraction, dimensionality reduction, and selection. It also has tools for constructing, evaluating and tuning ML Pipelines.

4) List down the languages supported by Apache Spark.

Ans. Apache Spark supports Scala, Python, Java, and R.
Apache Spark is written in Scala. Many people use Scala for the purpose of development. But it also has API in Java, Python, and R.

5) What are the components of Apache Spark Eco-system?

Ans. Spark Core

Spark Core is the base of Spark for parallel and distributed processing of huge datasets. It is in charge of all the essential I/O functionalities, programming, and observance the roles on spark clusters. It is also responsible for task dispatching, and networking with different storage systems, fault tolerance, and economical memory management. Core uses special collection referred to as RDD (Resilient Distributed Datasets).

Spark SQL
SparkSQL is module/component in Apache Spark that is employed to access structured and semi-structured information. It is a distributed framework that is tightly integrated with varied spark programming like Scala, Python, and Java. Spark SQL supports relative process in Spark programs via RDD further as on external data source. It is used for manipulating and taking information in varied formats. The means through that {we can|we will|we square measure able to} act with Spark SQL are SQL/HQL, DataFrame API, and Datasets API.

The main abstraction in SparkSQL is information sets that act on structured data. It translates ancient SQL and HiveQL queries into Spark jobs creating Spark accessible wide. It supports real-time data analytics, data streaming SQL.SparkSQL defines 3 varieties of function:

Built-in perform or user-defined function: Object comes with some functions for column manipulation. Using Scala we are able to outlined user outlined perform.
Aggregate Function: Operates on the cluster of rows and calculates one come back price per cluster.
Window Aggregate: Operates on the cluster of rows and calculates one come back price every row in an exceeding cluster.
Different type of APIs for accessing SparkSQL:

SQL: Executing SQL queries or Hive queries, the result is going to become in the variety of DataFrame.

DataFrame: It is similar to the relative table in SparkSQL and distributed the assortment of tabular information having rows and named column. It will perform filter, intersect, join, sort mixture and much more. DataFrames powerfully trusts options of RDD. As it trusts RDD, it is lazy evaluated and immutable in nature.
DataFrameAPI is offered in Scala, Java, and Python.
Datasets API: Dataset is new API to supply benefit of RDD because it is robust written and declarative in nature. Dataset is the assortment of object or records with the familiar schema. It should model in some data structure. DataSets API offers improvement of DataFrames and static kind safety of Scala. We can convert information set to Data Frame.
Spark Streaming
Spark Streaming is a light-weight API that permits developers to perform execution and streaming of information application. Discretized Streams kind the bottom abstraction in Spark Streaming. It makes use of an endless stream of {input information|input file|computer file} to method data in the time period. It leverages the quick programming capability of Apache Spark core to perform streaming analytics by ingesting information in mini-batches. Information in Spark Streaming accepts from varied information sources and live streams like Twitter, Apache Kafka, IoT Sensors, Amazon response, Apache Flume, etc. in an event-driven, fault-tolerant, and type-safe applications.

Spark element MLlib
MLlib in Spark stands for machine learning (ML) library. Its goal is to form sensible machine learning effective, ascendible and straightforward. It consists of some learning algorithms and utilities, as well as classification, regression, clustering, collaborative filtering, spatial property reduction, further as lower-level improvement primitives and higher-level pipeline genus Apis.
GraphX
GraphX, a distributed graph process framework on prime of Apache Spark. because it predicate on RDDs, that square measure immutable, graphs square measure immutable and so GraphX is unsuitable for graphs that require being updated, in addition to in an exceedingly transactional manner sort of a graph info.
For more details, please read Apache Spark Eco-system.

6) Is it possible to run Apache Spark without Hadoop?

Ans.  Yes, Apache Spark can run without Hadoop, standalone, or in the cloud. Spark doesn’t need a Hadoop cluster to work. It can read and then process data from other file systems as well. HDFS is just one of the file systems that Spark supports.

Spark does not have any storage layer, so it relies on one of the distributed storage systems for distributed computing like HDFS, Cassandra etc.

However, there are a lot of advantages to running Spark on top of Hadoop (HDFS (for storage) + YARN (resource manager)), but it’s not the mandatory requirement. It meant for distributed computing. In this case, the data distribute across the computers and Hadoop’s distributed file system HDFS is used to store data that does not fit in memory.

One more reason for using Hadoop with Spark is they both are open source and both can integrate with each other rather easily as compared to other data storage system.

For more details, please refer: Apache Spark Compatibility with Hadoop

7) What is RDD in Apache Spark? How are they computed in Spark? what are the various ways in which it can create?

Ans. RDD in Apache Spark is the representation of a set of records, it is the immutable collection of objects with distributed computing. RDD is the large collection of data or an array of reference of partitioned objects. Each and every dataset in RDD is logically partitioned across many servers so that they can compute on different nodes of the cluster. RDDs are fault tolerant i.e. self-recovered / recomputed in the case of failure. The dataset could data load externally by the users which can be in the form of JSON file, CSV file, text file or database via JDBC with no specific data structure.

RDD is Lazily Evaluated i.e. it is memorized or called when required or needed, which saves lots of time. RDD is a read-only, partitioned collection of data. RDDs can creates through deterministic operations or on stable storage or from other RDDs. It can also generates by parallelizing an existing collection in your application or referring a dataset in an external storage system. It is cacheable. As it operates on data over multiple jobs in computations such as logistic regression, k-means clustering, PageRank algorithms, which makes it reuse or share data among multiple jobs.

To learn more about the RDD follow: RDD Tutorial

3. Apache Spark Interview Questions For Beginners
8) What are the features of RDD, that makes RDD an important abstraction of Spark?

Ans.  RDD (Resilient Distributed Dataset) is a basic abstraction in Apache Spark. Spark RDD is an immutable, partitioned collection of elements on the cluster which can operates in parallel.

Each RDD is characterized by five main properties :

Below operations are lineage operations.

List or Set of partitions.
List of dependencies on other (parent) RDD
A function to compute each partition
Below operations are used for optimization during execution.

Optional preferred location [i.e. block location of an HDFS file] [it’s about data locality]
Optional partitioned info [i.e. Hash-Partition for Key/Value pair –> When data shuffled how data will travel]
Examples :

# HadoopRDD: HadoopRDD provides core functionality for reading data stored in Hadoop (HDFS, HBase, Amazon S3..) using the older MapReduce API (org.apache.hadoop.mapred)

Properties of HadoopRDD :

List or Set of partitions: One per HDFS block.
List of dependencies on parent RDD: None.
A function to compute each partition: read respective HDFS block
Optional Preferred location: HDFS block location
Optional partitioned info: None
#FilteredRDD : Properties of FilteredRDD:

List or Set of partitions: No. of partitions same as parent RDD\
List of dependencies on parent RDD: ‘one-to-one’ as the parent (same as parent)
A function to compute each partition: compute parent and then filter it
Optional Preferred location: None (Ask Parent)
Optional partitioned info: None
Find features of RDD in RDD Features in Spark

9) List out the ways of creating RDD in Apache Spark.

Ans. There are three ways to create RDD

(1) By Parallelizing collections in the driver program

(2) By loading an external dataset

(3) Creating RDD from already existing RDDs.

Create RDD By Parallelizing collections :

Parallelized collections are created by calling parallelize() method on an existing collection in driver program.

val rdd1 = Array(1,2,3,4,5)
val rdd2 = sc.parallelize(rdd1)
OR

val myList = sc.parallelize(List(1 to 1000), 5) where 5 is the number of partitions
[If we do not specify then default partition is 1
Create by loading an external Dataset

In Spark, the distributed dataset can form from any data source supported by Hadoop, including the local file system, HDFS, Cassandra, HBase etc. In this, the data is loaded from the external dataset. To create text file RDD, we can use SparkContext’s textFile method. It takes URL of the file and read it as a collection of line. URL can be a local path on the machine or a hdfs://, s3n://, etc. Use SparkSession.read to access an instance of DataFrameReader. DataFrameReader supports many file formats-

i) csv (String path)

import org.apache.spark.sql.SparkSession
def main(args: Array[String]):Unit = {
object DataFormat {
val spark =  SparkSession.builder.appName("AvgAnsTime").master("local").getOrCreate()
val dataRDD = spark.read.csv("path/of/csv/file").rdd
ii) json (String path)

val dataRDD = spark.read.json("path/of/json/file").rdd
iii) textFile (String path)

val dataRDD = spark.read.textFile("path/of/text/file").rdd
Creating RDD from existing RDD:

Transformation mutates one RDD into another RDD, thus transformation is the way to create an RDD from already existing RDD.

val words=spark.sparkContext.parallelize(Seq("the", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
"dog"))
val wordPair = words.map(w => (w.charAt(0), w))
wordPair.foreach(println)
For a detailed description on creating RDD read How to create RDD in Apache Spark

10) Explain Transformation in RDD. How is lazy evaluation helpful in reducing the complexity of the System?

Ans. Transformations are lazy evaluated operations on RDD that create one or many new RDDs, e.g. map, filter, reduceByKey, join, cogroup, randomSplit. Transformations are functions which take an RDD as the input and produces one or many RDDs as output. They don’t change the input RDD as RDDs are immutable and hence cannot change or modify but always produces new RDD by applying the computations operations on them. By applying transformations you incrementally build an RDD lineage with all the ancestor RDDs of the final RDD(s).

Transformations are lazy, i.e. are not executed immediately. Transformations can execute only when actions are called. After executing a transformation, the result RDD(s) will always be different from their ancestors RDD and can be smaller (e.g. filter, distinct, sample), bigger (e.g. flatMap, union, cartesian) or the same size (e.g. map) or it can vary in size.

RDD allows you to create dependencies b/w RDDs. Dependencies are the steps for producing results in a program. Each RDD in lineage chain, string of dependencies has a function for operating its data and has a pointer dependency to its ancestor RDD. Spark will divide RDD dependencies into stages and tasks and then send those to workers for execution.

Follow this link to read more

11) What are the types of Transformation in Spark RDD Operations?

Ans. There are two kinds of transformations:

Narrow transformations:

Narrow transformations are the result of map, filter and in which data to transform id from a single partition only, i.e. it is self-sustained.
An output RDD has partitions with records that originate from a single partition in the parent RDD.

Wide Transformations

Wide transformations are the result of groupByKey and reduceByKey. The data required to compute the records in a single partition may
reside in many partitions of the parent RDD.

Wide transformations are also called shuffle transformations as they may or may not depend on a shuffle. All of the tuples with the same key must end up in the same partition, processed by the same task. To satisfy these operations, Spark must execute RDD shuffle, which transfers data across the cluster and results in a new stage with a new set of partitions.

12) What is the reason behind Transformation being a lazy operation in Apache Spark RDD? How is it useful?

Ans. Whenever a transformation operation is performed in Apache Spark, it is lazily evaluated. It won’t execute until an action is performed. Apache Spark just adds an entry of the transformation operation to the DAG (Directed Acyclic Graph) of computation, which is a directed finite graph with no cycles. In this DAG, all the operations are classified into different stages, with no shuffling of data in a single stage.

By this way, Spark can optimize the execution by looking at the DAG at its entirety, and return the appropriate result to the driver program.

For example, consider a 1TB of a log file in HDFS containing errors, warnings, and other information. Below are the operations being performed in the driver program:

Create an RDD of this log file
It perform a flatmap() operation on this RDD to split the data in the log file based on tab delimiter.
Perform a filter() operation to extract data containing only error messages
Perform first() operation to fetch only the first error message.
If all the transformations in the above driver program are eagerly evaluated, then the whole log file will load into memory, all of the data within the file will split base on the tab, now either it needs to write the output of FlatMap somewhere or keep it in the memory. Spark needs to wait until the next operation is performed with the resource blocked for the upcoming operation. Apart from this for each and every operation spark need to scan all the records, like for FlatMap process all the records then again process them in filter operation.

On the other hand, if all the transformations are lazily evaluated, Spark will look at the DAG on the whole and prepare the execution plan for the application, now this plan will optimize the operation will combine/merge into stages then the execution will start. The optimized plan created by Spark improves job’s efficiency and overall throughput.

By this lazy evaluation in Spark, the number of switches between driver program and cluster is also reduced thereby saving time and resources in memory, and also there is an increase in the speed of computation.

13) What is RDD lineage graph? How is it useful in achieving Fault Tolerance?

Ans. The RDD Lineage Graph or RDD operator graph could be a graph of the entire parent RDDs of an RDD. It’s engineered as a result of materializing transformations to the RDD and then creating a logical execution set up.

The RDDs in Apache Spark rely on one or a lot of alternative RDDs. The illustration of dependencies in between RDDs is understood because of the lineage graph. Lineage graph info is employed to cypher every RDD on demand, so whenever a district of persistent RDD is lost, {the data | the info | the info} that’s lost will recover using the lineage graph information.

For details on RDD DAG refer to Directed Acyclic Graph

14) Explain the various Transformation on Apache Spark RDD like distinct(), union(), intersection(), and subtract().

Ans.  distnct() transformation –  If one wants only unique elements in a RDD, in that case, one can use d1.distnct() where d1 is RDD

Example

val d1 = sc.parallelize(List("c","c","p","m","t"))
val result = d1.distnct()
result.foreach{println}
OutPut:
p
t
m
c

union() transformation – Its simplest set operation. rdd1.union(rdd2) which outputs RDD which contains the data from both sources. If the duplicates are present in the input RDD, an output of union() transformation will contain duplicate also which can fix using distinct().
Example

val u1 = sc.parallelize(List("c","c","p","m","t"))
val u2 = sc.parallelize(List("c","m","k"))
val result = u1.union(u2)
result.foreach{println}
Output:
c
c
p
m
t
c
m
k

intersection() transformation – It returns the elements which are present in both the RDDs and remove all the duplicate including duplicated in single RDD
val is1 = sc.parallelize(List("c","c","p","m","t"))
val is2 = sc.parallelize(List("c","m","k"))
val result = is1.union(is2)
result.foreach{println}
Output :
m
c

subtract() transformation – Subtract(anotherrdd), returns an RDD that has an only value present in the first RDD and not in second RDD.
Example

val s1 = sc.parallelize(List("c","c","p","m","t"))
val s2 = sc.parallelize(List("c","m","k"))
val result = s1.subtract(s2)
result.foreach{println}
Output:
t
p

For more transformation in Apache Spark refer to Transformation and Action

15) What is the FlatMap Transformation in Apache Spark RDD?

Ans. FlatMap is a transformation operation in Apache Spark to create an RDD from existing RDD. It takes one element from an RDD and can produce 0, 1 or many outputs based on business logic. It is similar to Map operation, but Map produces one to one output. If we perform Map operation on an RDD of length N, output RDD will also be of length N. But for FlatMap operation output RDD can be of different length based on business logic

X——A x———–a
Y——B y———–b,c
Z——C z———–d,e,f

Map Operation FlatMap Operation

We can also say as flatMap transforms an RDD of length N into a collection of N collection, then flattens into a single RDD of results.

If we observe the below example data1 RDD which is the output of Map operation has same no of element as of data RDD,
But data2 RDD does not have the same number of elements. We can also observe here as data2 RDD is a flattened output of data1 RDD

pranshu@pranshu-virtual-machine:~$ cat pk.txt

1 2 3 4

5 6 7 8 9

10 11 12

13 14 15 16 17

18 19 20

scala> val data = sc.textFile(“/home/pranshu/pk.txt”)
17/05/17 07:08:20 WARN SizeEstimator: Failed to check whether UseCompressedOops is set; assuming yes

data: org.apache.spark.rdd.RDD[String] = /home/pranshu/pk.txt MapPartitionsRDD[1] at textFile at <console>:24

scala> data.collect
res0: Array[String] = Array(1 2 3 4, 5 6 7 8 9, 10 11 12, 13 14 15 16 17, 18 19 20)

scala>
scala> val data1 = data.map(line => line.split(” “))
data1: org.apache.spark.rdd.RDD[Array[String]] = MapPartitionsRDD[2] at map at <console>:26

scala>
scala> val data2 = data.flatMap(line => line.split(” “))
data2: org.apache.spark.rdd.RDD[String] = MapPartitionsRDD[3] at flatMap at <console>:26

scala>
scala> data1.collect
res1: Array[Array[String]] = Array(Array(1, 2, 3, 4), Array(5, 6, 7, 8, 9), Array(10, 11, 12), Array(13, 14, 15, 16, 17), Array(18, 19, 20))

scala>
scala> data2.collect
res2: Array[String] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

For more details, refer: Map Vs Flatmap Operations

16) Explain first() operation in Apache Spark RDD.

Ans.  It is an action and returns the first element of the RDD.

Example :

val rdd1 = sc.textFile("/home/hdadmin/wc-data.txt")
rdd1.count
rdd1.first
Output :

Long: 20

String: DataFlair is the leading technology training provider

4. Apache Spark Interview Questions For Intermediate
17) Describe join() operation. How is outer join supported?

Ans. join() is transformation and is in package org.apache.spark.rdd.pairRDDFunction

def join[W](other: RDD[(K, W)]): RDD[(K, (V, W))]Permalink

Return an RDD containing all pairs of elements with matching keys in this and other.

Each pair of elements will returns as a (k, (v1, v2)) tuple, where (k, v1) is in this and (k, v2) is in other. Performs a hash join across the cluster.

It is joining two datasets. When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.

Example 1:

val rdd1 = sc.parallelize(Seq(("m",55),("m",56),("e",57),("e",58),("s",59),("s",54)))
val rdd2 = sc.parallelize(Seq(("m",60),("m",65),("s",61),("s",62),("h",63),("h",64)))
val joinrdd = rdd1.join(rdd2)
joinrdd.collect
Output:

Array[(String, (Int, Int))] = Array((m,(55,60)), (m,(55,65)), (m,(56,60)), (m,(56,65)), (s,(59,61)), (s,(59,62)), (s,(54,61)), (s,(54,62)))

Example 2:

val myrdd1 = sc.parallelize(Seq((1,2),(3,4),(3,6)))
val myrdd2 = sc.parallelize(Seq((3,9)))
val myjoinedrdd = myrdd1.join(myrdd2)
myjoinedrdd.collect
Output:

Array[(Int, (Int, Int))] = Array((3,(4,9)), (3,(6,9)))

18) Describe coalesce() operation. When can you coalesce to a larger number of partitions? Explain.

Ans. It is a transformation and it’s in a package org.apache.spark.rdd.ShuffledRDD

def coalesce(numPartitions: Int, shuffle: Boolean = false, partitionCoalescer: Option[PartitionCoalescer] = Option.empty)(implicit ord: Ordering[(K, C)] = null): RDD[(K, C)]

Return a new RDD that is reduced into numPartitions partitions.

This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead, each of the 100 new partitions will claim 10 of the current partitions.

However, if you’re doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step but means the current upstream partitions will execut in parallel (per whatever the current partitioning is).

Note: With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner.

Coalesce() operation changes a number of the partition where data is stored. It combines original partitions to a new number of partitions, so it reduces the number of partitions. Coalesce() operation is an optimized version of repartition that allows data movement, but only if you are decreasing the number of RDD partitions. It runs operations more efficiently after filtering large datasets.

Example :

val myrdd1 = sc.parallelize(1 to 1000, 15)
myrdd1.partitions.length
val myrdd2 = myrdd1.coalesce(5,false)
myrdd2.partitions.length
Int = 5
Output :

Int = 15

Int = 5

19) Explain pipe() operation. How it writes the result to the standard output?

Ans. It is a transformation.

def pipe(command: String): RDD[String]

Return an RDD created by piping elements to a forked external process.

In general, Spark is using Scala, Java, and Python to write the program. However, if that is not enough, and one want to pipe (inject) the data which written in other languages like ‘R’, Spark provides the general mechanism in the form of pipe() method.
Spark provides the pipe() method on RDDs.
With Spark’s pipe() method, one can write a transformation of an RDD that can read each element in the RDD from standard input as String.
It can write the results as String to the standard output.
For more transformation on RDDs see: Apache Spark Operations

20) What is the key difference between textFile and wholeTextFile method?

Ans. Both are the method of org.apache.spark.SparkContext.

textFile() :

def textFile(path: String, minPartitions: Int = defaultMinPartitions): RDD[String]
Read a text file from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI, and return it as an RDD of Strings
For example sc.textFile(“/home/hdadmin/wc-data.txt”) so it will create RDD in which each individual line an element.
Everyone knows the use of textFile.
wholeTextFiles() :

def wholeTextFiles(path: String, minPartitions: Int = defaultMinPartitions): RDD[(String, String)]
Read a directory of text files from HDFS, a local file system (available on all nodes), or any Hadoop-supported file system URI.
Rather than create basic RDD, the wholeTextFile() returns pairRDD.
For example, you have few files in a directory so by using wholeTextFile() method,
it creates pair RDD with a filename with a path as key,
and value is the whole file as a string
val myfilerdd = sc.wholeTextFiles("/home/hdadmin/MyFiles")
val keyrdd = myfilerdd.keys
keyrdd.collect
val filerdd = myfilerdd.values
filerdd.collect
Output :

Array[String] = Array(
file:/home/hdadmin/MyFiles/JavaSparkPi.java,
file:/home/hdadmin/MyFiles/sumnumber.txt,
file:/home/hdadmin/MyFiles/JavaHdfsLR.java,
file:/home/hdadmin/MyFiles/JavaPageRank.java,
file:/home/hdadmin/MyFiles/JavaLogQuery.java,
file:/home/hdadmin/MyFiles/wc-data.txt,
file:/home/hdadmin/MyFiles/nosum.txt)

Array[String] =

Array(“/*

Licensed to the Apache Software Foundation (ASF) under one or more
Contributor license agreements. See the NOTICE file distributed with
This work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
The “License”; you may not use this file except in compliance with
The License. You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
Distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
21) What is Action, how it process data in Apache Spark?

Ans. Actions return final result of RDD computations/operation. It triggers execution using lineage graph to load the data into original RDD, and carries out all intermediate transformations and returns final result to Driver program or write it out to file system.

For example: First, take, reduce, collect, count, aggregate are some of the actions in spark.

Action produces a value back to the Apache Spark driver program. It may trigger a previously constructed, lazy RDD to evaluate. It is an RDD operations that produce non-RDD values. Action function materializes a value in a Spark program. So basically an action is RDD operation that returns a value of any type but RDD[T] is an action. Actions are one of two ways to send data from executors to the driver (the other being accumulators).

For detail study of Action refer Transformation and Action in Apache Spark.

22) How is Transformation on RDD different from Action?

Ans. Transformations create new RDD from existing RDD
Transformations are executed on demand.(Lazy computation)
Ex: filter(), union()

An Action will return a non-RDD type (your stored value types usually)
Actions trigger execution using lineage graph to load the data into original RDD
Ex: count(), first()

23) What are the ways in which one can know that the given operation is Transformation or Action?

Ans. In order to identify the operation, one needs to look at the return type of an operation.

If the operation returns a new RDD, in that case, an operation is ‘Transformation’
If the operation returns any other type than RDD, in that case, an operation is ‘Action’
Hence, Transformation constructs a new RDD from an existing one (previous one) while Action computes the result based on applied transformation and returns the result to either driver program or save it to the external storage.

Also, refer to operations of RDD in Apache Spark and its Operations

24) Describe Partition and Partitioner in Apache Spark.

Ans. Partition in Spark is similar to split in HDFS. A partition in Spark is a logical division of data stored on a node in the cluster. They are the basic units of parallelism in Apache Spark. RDDs are a collection of partitions. When some actions are executed, a task is launched per partition.

By default, partitions are automatically created by the framework. However, the number of partitions in Spark are configurable to suit the needs. For the number of partitions, if spark.default.parallelism is set, then we should use the value from SparkContext defaultParallelism, othewrwise we should use the max number of upstream partitions. Unless spark.default.parallelism is set, the number of partitions will be the same as that of the largest upstream RDD, as this would least likely cause out-of-memory errors.

A partitioner is an object that defines how the elements in a key-value pair RDD are partitioned by key, maps each key to a partition ID from 0 to numPartitions – 1. It captures the data distribution at the output. With the help of partitioner, the scheduler can optimize the future operations. The contract of partitioner ensures that records for a given key have to reside on a single partition.

We should choose a partitioner to use for a cogroup-like operations. If any of the RDDs already has a partitioner, we should choose that one. Otherwise, we use a default HashPartitioner.

There are three types of partitioners in Spark :

Hash Partitioner
Range Partitioner
Custom Partitioner
Hash – Partitioner: Hash- partitioning attempts to spread the data evenly across various partitions based on the key.

Range – Partitioner: In Range- Partitioning method, tuples having keys with same range will appear on the same machine.

RDDs can create with specific partitioning in two ways :

i) Providing explicit partitioner by calling partitionBy method on an RDD

ii) Applying transformations that return RDDs with specific partitioners.

5. Apache Spark Interview Questions For Experience
25) How can you manually partition the RDD?

Ans. When we create the RDD from a file stored in HDFS.

data = context.textFile("/user/dataflair/file-name")
By default one partition is created for one block. ie. if we have a file of size 1280 MB (with 128 MB block size) there will be 10 HDFS blocks, hence the similar number of partitions (10) will create.

If you want to create more partitions than the number of blocks, you can specify the same while RDD creation:

data = context.textFile("/user/dataflair/file-name", 20)
It will create 20 partitions for the file. ie for each block 2 partitions will create.

NOTE: It is often recommended to have more no of partitions than no of the block, it improves the performance

26) Name the two types of shared variable available in Apache Spark.

Ans. There are two types of shared variables available in Apache Spark:

Accumulators: used to Aggregate the Information.
Broadcast variable: to efficiently distribute large values.
When we pass the function to Spark, say filter(), this function can use the variable which defined outside of the function but within the Driver program but when we submit the task to Cluster, each worker node gets a new copy of variables and update from these variables not propagated back to Driver program.

Accumulators and Broadcast variable are used to remove above drawback ( i.e. we can get the updated values back to our Driver program)

27) What are accumulators in Apache Spark?

Ans. This discussion is in continuation with a question, Name the two types of shared variable available in Apache Spark.

Introduction of Accumulator :

An accumulator is a shared variable in Apache Spark, used to aggregating information across the cluster.
In other words, aggregating information/values from worker nodes back to the driver program. ( How we will see in below session)
Why Accumulator :

When we use a function inside the operation like map(), filter() etc these functions can use the variables which defined outside these function scope in the driver program.
When we submit the task to cluster, each task running on the cluster gets a new copy of these variables and updates from these variable do not propagate back to the driver program.
Accumulator lowers this restriction.
Use Cases :

One of the most common uses of accumulator counts the events that occur during job execution for debugging purpose.
Meaning count the no. of blank lines from the input file, no. of bad packets from a network during a session, during Olympic data analysis we have to find age where we said (age != ‘NA’) in SQL query in short finding bad/corrupted records.
Examples :

scala> val record = spark.read.textFile("/home/hdadmin/wc-data-blanklines.txt")
record: org.apache.spark.sql.Dataset[String] = [value: string]

scala> val emptylines = sc.accumulator(0) warning: there were two deprecation
warnings; re-run with -deprecation for details e

mptylines: org.apache.spark.Accumulator[Int] = 0

scala> val processdata = record.flatMap(x =>
{
if(x == "")
emptylines += 1
x.split(" ")
})
processdata: org.apache.spark.sql.Dataset[String] = [value: string]

scala> processdata.collect
16/12/02 20:55:15 WARN SizeEstimator: Failed to check whether UseCompressedOops is set; assuming yes

Output :

res0: Array[String] = Array(DataFlair, provides, training, on, cutting, edge, technologies., “”, DataFlair, is, the, leading, training, provider,, we, have, trained, 1000s, of, candidates., Training, focues, on, practical, aspects, which, industy, needs, rather, than, theoretical, knowledge., “”, DataFlair, helps, the, organizations, to, solve, BigData, Problems., “”, Javadoc, is, a, tool, for, generating, API, documentation, in, HTML, format, from, doc, comments, in, source, code., It, can, be, downloaded, only, as, part, of, the, Java, 2, SDK., To, see, documentation, generated, by, the, Javadoc, tool,, go, to, J2SE, 1.5.0, API, Documentation., “”, Javadoc, FAQ, -, This, FAQ, covers, where, to, download, the, Javadoc, tool,, how, to, find, a, list, of, known, bugs, and, feature, reque…

scala> println(“No. of Empty Lines : ” + emptylines.value)

No. of Empty Lines: 10

28) Explain SparkContext in Apache Spark.

Ans. A SparkContext is a client of Spark’s execution environment and it acts as the master of the Spark application. SparkContext sets up internal services and establishes a connection to a Spark execution environment. You can create RDDs, accumulators and broadcast variables, access Spark services and run jobs (until SparkContext stops) after the creation of SparkContext. Only one SparkContext may be active per JVM. You must stop() the active SparkContext before creating a new one.

In Spark shell, a special interpreter-aware SparkContext is already created for the user, in the variable called sc.

The first step of any Spark driver application is to create a SparkContext. The SparkContext allows the Spark driver application to access the cluster through a resource manager. The resource manager can be YARN, or Spark’s Cluster Manager.

Few functionalities which SparkContext offers are:

We can get the current status of a Spark application like configuration, app name.
We can set Configuration like master URL, default logging level.
One can create Distributed Entities like RDDs.
29) Discuss the role of Spark driver in Spark application.

Ans. The spark driver is that the program that defines the transformations and actions on RDDs of knowledge and submits a request to the master. Spark driver is a program that runs on the master node of the machine which declares transformations and actions on knowledge RDDs.

In easy terms, the driver in Spark creates SparkContext, connected to a given Spark Master. It conjointly delivers the RDD graphs to Master, wherever the standalone cluster manager runs.

Also, see How Spark works

30) What role does worker node play in Apache Spark Cluster? And what is the need to register a worker node with the driver program?

Ans. Apache Spark follows a master/slave architecture, with one master or driver process and more than one slave or worker processes

The master is the driver that runs the main() program where the spark context is created. It then interacts with the cluster manager to schedule the job execution and perform the tasks.
The worker consists of processes that can run in parallel to perform the tasks scheduled by the driver program. These processes are called executors.
Whenever a client runs the application code, the driver programs instantiates Spark Context, converts the transformations and actions into logical DAG of execution. This logical DAG is then converted into a physical execution plan, which is then broken down into smaller physical execution units. The driver then interacts with the cluster manager to negotiate the resources required to perform the tasks of the application code. The cluster manager then interacts with each of the worker nodes to understand the number of executors running in each of them.

The role of worker nodes/executors:

Perform the data processing for the application code
Read from and write the data to the external sources
Store the computation results in memory, or disk.
The executors run throughout the lifetime of the Spark application. This is a static allocation of executors. The user can also decide how many numbers of executors are required to run the tasks, depending on the workload. This is a dynamic allocation of executors.

Before the execution of tasks, the executors are registered with the driver program through the cluster manager, so that the driver knows how many numbers of executors are running to perform the scheduled tasks. The executors then start executing the tasks scheduled by the worker nodes through the cluster manager.

Whenever any of the worker nodes fail, the tasks that are required to perform will automatically allocates to any other worker nodes

For information on how Spark works Spark-How it works

31) Discuss the various running mode of Apache Spark.

Ans. We can launch spark application in four modes:

1) Local Mode (local[*],local,local[2]…etc)

-> When you launch spark-shell without control/configuration argument, It will launch in local mode

spark-shell –master local[1]

-> spark-submit –class com.df.SparkWordCount SparkWC.jar local[1]

2) Spark Standalone cluster manger:

-> spark-shell –master spark://hduser:7077

-> spark-submit –class com.df.SparkWordCount SparkWC.jar spark://hduser:7077

3) Yarn mode (Client/Cluster mode):

-> spark-shell –master yarn or

(or)

->spark-shell –master yarn –deploy-mode client

Above both commands are same.

To launch spark application in cluster mode, we have to use a spark-submit command. We cannot run yarn-cluster mode via spark-shell because when we run spark application, driver program will be running as part application master container/process. So it is not possible to run cluster mode via spark-shell.

-> spark-submit –class com.df.SparkWordCount SparkWC.jar yarn-client

-> spark-submit –class com.df.SparkWordCount SparkWC.jar yarn-cluster

4) Mesos mode:

-> spark-shell –master mesos://HOST:5050

32) Describe the run-time architecture of Spark.

Ans. There are 3 important components of Runtime architecture of Apache Spark as described below.

Client process
Driver
Executor
Responsibilities of the client process component

The client process starts the driver program.

For example, the client process can be a spark-submit script for running applications, a spark-shell script, or a custom application using Spark API. The client process prepares the classpath and all configuration options for the Spark application.

It also passes application arguments, if any, to the application running on the driver.

Responsibilities of the driver component

The driver orchestrates and monitors the execution of a Spark application. There’s always one driver per Spark application.

The driver is like a wrapper around the application. The driver and its subcomponents (the Spark context and scheduler ) are responsible for:

requesting memory and CPU resources from cluster managers
breaking application logic into stages and tasks
sending tasks to executors
collecting the results
Responsibilities of the executors

The executors, which is a JVM processes, accept tasks from the driver, execute those tasks, and return the results to the driver. Each executor has several task slots (or CPU cores) for running tasks in parallel.

6. Best Apache Spark Interview Questions and Answers
33) What is the command to start and stop the Spark in an interactive shell?

Ans. Command to start the interactive shell in Scala:

>>>bin/spark-shell
First, go the spark directory i.e.

hdadmin@ubuntu:~$ cd spark-1.6.1-bin-hadoop2.6/
hdadmin@ubuntu:~/spark-1.6.1-bin-hadoop2.6$ bin/spark-shell
——————————————————————————————————————————
Command to stop the interactive shell in Scala:

scala>Press (Ctrl+D)
One can see the following message

scala> Stopping spark context.
34) Describe Spark SQL.

Ans. Spark SQL is a Spark interface to work with Structured and Semi-Structured data (data that as defined fields i.e. tables). It provides abstraction layer called DataFrame and DataSet through with we can work with data easily. One can say that DataFrame is like a table in a relational database. Spark SQL can read and write data in a variety of Structured and Semi-Structured formats like Parquets, JSON, Hive. Using SparkSQL inside Spark application is the best way to use it. This empowers us to load data and query it with SQL. we can also combine it with “regular” program code in Python, Java or Scala.

For a detailed study on SparkSQL, Refer link: Spark SQL

35) What is SparkSession in Apache Spark? Why is it needed?

Ans. Starting from Apache Spark 2.0, Spark Session is the new entry point for Spark applications.

Prior to 2.0, SparkContext was the entry point for spark jobs. RDD was one of the main APIs then, and it was created and manipulated using Spark Context. Every other APIs, different contexts were required – For SQL, SQL Context was required; For Streaming, Streaming Context was required; For Hive, Hive Context was required.

But from 2.0, RDD along with DataSet and its subset DataFrame APIs are becoming the standard APIs and are a basic unit of data abstraction in Spark. All of the user-defined code will be written and evaluated against the DataSet and DataFrame APIs as well as RDD.

So, there is a need for a new entry point build for handling these new APIs, which is why Spark Session has been introduced. Spark Session also includes all the APIs available in different contexts – Spark Context, SQL Context, Streaming Context, Hive Context.

36) Explain API create Or Replace TempView().

Ans. It’s basic Dataset function and under org.apache.spark.sql

def createOrReplaceTempView(viewName: String): Unit
Creates a temporary view using the given name.
The lifetime of this temporary view is tied to the SparkSession that was used to create this Dataset.
scala> val df = spark.read.csv("/home/hdadmin/titanic_data.txt")
df: org.apache.spark.sql.DataFrame = [_c0: string, _c1: string … 9 more fields]

scala> df.printSchema
root

|– _c0: string (nullable = true)

|– _c1: string (nullable = true)

|– _c2: string (nullable = true)

|– _c3: string (nullable = true)

|– _c4: string (nullable = true)

|– _c5: string (nullable = true)

|– _c6: string (nullable = true)

|– _c7: string (nullable = true)

|– _c8: string (nullable = true)

|– _c9: string (nullable = true)

|– _c10: string (nullable = true)

scala> df.show
+—+—+—+——————–+——-+———–+——————–+——-+—————–+—–+——+

|_c0|_c1|_c2| _c3| _c4| _c5| _c6| _c7| _c8| _c9| _c10|

+—+—+—+——————–+——-+———–+——————–+——-+—————–+—–+——+

| 1|1st| 1|Allen, Miss Elisa…|29.0000|Southampton| St Louis, MO| B-5| 24160 L221| 2|female|

| 2|1st| 0|Allison, Miss Hel…| 2.0000|Southampton|Montreal, PQ / Ch…| C26| null| null|female|

| 3|1st| 0|Allison, Mr Hudso…|30.0000|Southampton|Montreal, PQ / Ch…| C26| null|(135)| male|

| 4|1st| 0|Allison, Mrs Huds…|25.0000|Southampton|Montreal, PQ / Ch…| C26| null| null|female|

| 5|1st| 1|Allison, Master H…| 0.9167|Southampton|Montreal, PQ / Ch…| C22| null| 11| male|

| 6|1st| 1| Anderson, Mr Harry|47.0000|Southampton| New York, NY| E-12| null| 3| male|

| 7|1st| 1|Andrews, Miss Kor…|63.0000|Southampton| Hudson, NY| D-7| 13502 L77| 10|female|

| 8|1st| 0|Andrews, Mr Thoma…|39.0000|Southampton| Belfast, NI| A-36| null| null| male|

| 9|1st| 1|Appleton, Mrs Edw…|58.0000|Southampton| Bayside, Queens, NY| C-101| null| 2|female|

| 10|1st| 0|Artagaveytia, Mr …|71.0000| Cherbourg| Montevideo, Uruguay| null| null| (22)| male|

| 11|1st| 0|Astor, Colonel Jo…|47.0000| Cherbourg| New York, NY| null|17754 L224 10s 6d|(124)| male|

| 12|1st| 1|Astor, Mrs John J…|19.0000| Cherbourg| New York, NY| null|17754 L224 10s 6d| 4|female|

| 13|1st| 1|Aubert, Mrs Leont…| NA| Cherbourg| Paris, France| B-35| 17477 L69 6s| 9|female|

| 14|1st| 1|Barkworth, Mr Alg…| NA|Southampton| Hessle, Yorks| A-23| null| B| male|

| 15|1st| 0| Baumann, Mr John D.| NA|Southampton| New York, NY| null| null| null| male|

| 16|1st| 1|Baxter, Mrs James…|50.0000| Cherbourg| Montreal, PQ|B-58/60| null| 6|female|

| 17|1st| 0|Baxter, Mr Quigg …|24.0000| Cherbourg| Montreal, PQ|B-58/60| null| null| male|

| 18|1st| 0| Beattie, Mr Thomson|36.0000| Cherbourg| Winnipeg, MN| C-6| null| null| male|

| 19|1st| 1|Beckwith, Mr Rich…|37.0000|Southampton| New York, NY| D-35| null| 5| male|

| 20|1st| 1|Beckwith, Mrs Ric…|47.0000|Southampton| New York, NY| D-35| null| 5|female|

+—+—+—+——————–+——-+———–+——————–+——-+—————–+—–+——+

only showing top 20 rows

scala> df.createOrReplaceTempView("titanicdata")
37) What are the various advantages of DataFrame over RDD in Apache Spark?

Ans. DataFrames are the distributed collection of data. In DataFrame, data is organized into named columns. It is conceptually similar to a table in a relational database.
we can construct DataFrames from a wide array of sources. Such as structured data files, tables in Hive, external databases, or existing RDDs.

As same as RDDs, DataFrames are evaluated lazily(Lazy Evaluation). In other words, computation only happens when an action (e.g. display result, save output) is required.

Out of the box, DataFrame supports reading data from the most popular formats, including JSON files, Parquet files, Hive tables. Also, can read from distributed file systems (HDFS), local file systems, cloud storage (S3), and external relational database systems through JDBC. In addition, through Spark SQL’s external data sources API, DataFrames can extend to support any third-party data formats or sources. Existing third-party extensions already include Avro, CSV, ElasticSearch, and Cassandra.

There is much more to know about DataFrames. Refer link: Spark SQL DataFrame

38) What is a DataSet? What are its advantages over DataFrame and RDD?

Ans. In Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.

In SparkSQL, Dataset is a data structure which is strongly typed and is a map to a relational schema. Also, represents structured queries with encoders. DataSet has been released in Spark 1.6.

In serialization and deserialization (SerDe) framework, encoder turns out as a primary concept in Spark SQL. Encoders handle all translation process between JVM objects and Spark’s internal binary format. In Spark, we have built-in encoders those are very advanced. Even they generate bytecode to interact with off-heap data.

On-demand access to individual attributes without having to de-serialize an entire object is provided by an encoder. Spark SQL uses a SerDe framework, to make input-output time and space efficient. Due to encoder knows the schema of record, it became possible to achieve serialization as well as deserialization.

Spark Dataset is structured and lazy query expression(lazy Evolution) that triggers the action. Internally dataset represents a logical plan. The logical plan tells the computational query that we need to produce the data. the logical plan is a base catalyst query plan for the logical operator to form a logical query plan. When we analyze this and resolve we can form a physical query plan.

As Dataset introduced after RDD and DataFrame, it clubs the features of both. It offers the following similar features:

1. The convenience of RDD.
2. Performance optimization of DataFrame.
3. Static type-safety of Scala.

Hence, we have observed that Datasets provides a more functional programming interface to work with structured data.

To know more detailed information about DataSets, refer link: Spark Dataset

39) On what all basis can you differentiate RDD, DataFrame, and DataSet?

Ans. DataFrame: A Data Frame is used for storing data into tables. It is equivalent to a table in a relational database but with richer optimization. Spark DataFrame is a data abstraction and domain-specific language (DSL) applicable on a structure and semi-structured data. It is distributed the collection of data in the form of named column and row. It has a matrix-like structure whose column may be different types (numeric, logical, factor, or character ). We can say data frame has the two-dimensional array like structure where each column contains the value of one variable and row contains one set of values for each column and combines feature of list and matrices.

For more details about DataFrame, please refer: DataFrame in Spark

RDD is the representation of a set of records, immutable collection of objects with distributed computing. RDD is a large collection of data or RDD is an array of reference of partitioned objects. Each and every dataset in RDD is logically partitioned across many servers so that they can compute on different nodes of the cluster. RDDs are fault tolerant i.e. self-recovered/recomputed in the case of failure. The dataset can load externally by the users which can be in the form of JSON file, CSV file, text file or database via JDBC with no specific data structure.

DataSet in Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.

For more details about RDD, please refer: RDD in Spark

For the detailed comparison between RDD vs DataFrame, follow: RDD vs DataFrame vs DataSet

40) What is Apache Spark Streaming? How is the processing of streaming data achieved in Apache Spark? Explain.

Ans. Data arriving continuously, in an unbounded sequence is a data stream. Continuously flowing input data is divided into discrete units with the help of streaming for further processing. Through Stream processing analyzing of streaming data is possible. Also, it is a low latency processing.

In the year 2103 Spark Streaming was introduced to Apache Spark. It is an extension of the core Spark API. Streaming offers scalable, high-throughput and fault-tolerant stream processing of live data streams. It is possible to do Data ingestion from many sources. For Example Apache Flume, Kafka, Amazon Kinesis or TCP sockets. And, By using complex algorithms that are expressed with high-level functions processing can do. For example reduce, map, join and window. Afterwards, processed data can push out to live dashboards, filesystems and databases.

Streaming’s Key abstraction is Discretized Stream. It is also known as Spark DStream. A stream of data divided into small batches is represented by it. DStreams are built on Spark’s core data abstraction”RDDs“. Streaming allows integration with any other Apache Spark components like Spark SQL and Spark MLlib.

To know more about Spark Streaming, follow the link: Spark Streaming Tutorial for Beginners

7. Latest Apache Spark Interview Questions
41) What is the abstraction of Spark Streaming?

Ans. A Discretized Stream (DStream), the basic abstraction in Spark Streaming, is a continuous sequence of RDDsrepresenting a continuous stream of data. DStreams can either create from live data (such as, data from HDFS, Kafka or Flume) or it can generate by transformation existing DStreams using operations such as map, window and reduceByKeyAndWindow.

Internally, there are few basic properties by which DStreams is characterized:

1. DStream depends on the list of other DStreams.
2. A time interval at which the DStream generates an RDD
3. A function that is used to generate an RDD after each time interval

for complete introduction, refer link: Apache Spark DStream (Discretized Streams)

42) Explain what are the various types of Transformation on DStream?

Ans. There are two types of transformation on DStream.

Stateless transformation: In stateless transformation, the processing of each batch does not depend on the data of its previous batches.
Stateful transformation: Stateful transformation use data or intermediate results from previous batches to compute the result of the current batch.
Also, refer to Transformation operation in Spark Streaming.

43) Explain the level of parallelism in Spark Streaming. Also, describe its need.

Ans. In order to reduce the processing time, one need to increase the parallelism. In Spark Streaming, there are three ways to increase the parallelism:

Increase the number of receivers : If there are too many records for single receiver (single machine) to read in and distribute so that is bottleneck. So we can increase the no. of receiver depends on scenario.
Re-partition the receive data : If one is not in a position to increase the no. of receivers in that case redistribute the data by re-partitioning.
Increase parallelism in aggregation :
for complete guide on Spark Streaming you may refer to Apache Spark-Streaming guide

44) Discuss writeahead logging in Apache Spark Streaming.

Ans. There are two types of failures in any Apache Spark job – Either the driver failure or the worker failure.

When any worker node fails, the executor processes running in that worker node will kill, and the tasks which were scheduled on that worker node will be automatically moved to any of the other running worker nodes, and the tasks will accomplish.

When the driver or master node fails, all of the associated worker nodes running the executors will kill, along with the data in each of the executors’ memory. In the case of files being read from reliable and fault tolerant file systems like HDFS, zero data loss is always guaranteed, as the data is ready to be read anytime from the file system. Checkpointing also ensures fault tolerance in Spark by periodically saving the application data in specific intervals.

In the case of Spark Streaming application, zero data loss is not always guaranteed, as the data will buffer in the executors’ memory until they get processed. If the driver fails, all of the executors will kill, with the data in their memory, and the data cannot recover.

To overcome this data loss scenario, Write Ahead Logging (WAL) has been introduced in Apache Spark 1.2. With WAL enabled, the intention of the operation is first noted down in a log file, such that if the driver fails and is restarted, the noted operations in that log file can apply to the data. For sources that read streaming data, like Kafka or Flume, receivers will be receiving the data, and those will store in the executor’s memory. With WAL enabled, these received data will also store in the log files.

WAL can enable by performing the below:

1. Setting the checkpoint directory, by using streamingContext.checkpoint(path)

2. Enabling the WAL logging, by setting spark.stream.receiver.WriteAheadLog.enable to True.

45) What are the roles of the file system in any framework?

Ans. In order to manage data on computer, one has to interact with the File System directly or indirectly. When we install Hadoop on our computer, actually there are two file system exists on machine

(1) Local File System ,
(2) HDFS (Hadoop Distributed File System)

HDFS is sits top on of Local File System.

Following are the genera functions of File System (be it Local or HDFS)

Control the data access mechanism (i.e how data stored and retrived)
Manages the metadata about the Files / Folders (i.e. created date, size etc)
Grants the access permission and manage the securities
Efficiently manage the storage space
For more details, please follow: HDFS

46) What do you mean by Speculative execution in Apache Spark?

Ans. The Speculative task in Apache Spark is task that runs slower than the rest of the task in the job.It is health check process that verifies the task is speculated, meaning the task that runs slower than the median of successfully completed task in the task sheet. Such tasks are submitted to another worker. It runs the new copy in parallel rather than shutting down the slow task.

In the cluster deployment mode, the thread starts as TaskSchedulerImp1with spark.speculation enabled. It executes periodically every spark.speculation.interval after the initial spark.speculation.interval passes.

8. Apache Spark Interview Questions for Practice
47) How do you parse data in XML? Which kind of class do you use with java to pass data?

Ans. One way to parse the XML data in Java is to use the JDOM library. One can download it and import the JDOM library in your project. You can get help from Google. If still, required help post your problem in the forum. I will try to give you the solution. For Scala, Scala has the inbuilt library for XML parsing. Scala-xml_2.11-1.0.2 jar (please check them for new version if available).

48) Explain Machine Learning library in Spark.

Ans. It is a scalable machine learning library. It delivers both blazing speed (up to 100x faster than MapReduce) and high-quality algorithms (e.g., multiple iterations to increase accuracy). We can use this library in Java, Scala, and Python as part of Spark applications so that you can include it incomplete workflows. There are many tools, which are provided by MLlib. Such as-

ML Algorithms: Common learning algorithms such as classification, regression, clustering, and collaborative filtering.
Featurization: Feature extraction, transformation, dimensionality reduction, and selection.
Pipelines: Tools for constructing, evaluating, and tuning ML Pipelines.
Persistence: Saving and load algorithms, models, and Pipelines.
Utilities: Linear algebra, statistics, data handling, etc.
For detailed insights, follow link: Apache Spark MLlib (Machine Learning Library)

49) List various commonly used Machine Learning Algorithm.

Ans. Basically, there are three types of Machine Learning Algorithms :

(1) Supervised Learning Algorithm

(2) Unsupervised Learning Algorithm

(3) Reinforcement Learning Algorithm

Most commonly used Machine Learning Algorithm is as follows :

Linear Regression
Logistic Regression
Decision Tree
K-Means
KNN
SVM
Random Forest
Naïve Bayes
Dimensionality Reduction Algorithm
Gradient Boost and Adaboost
For what is MLlib see Apache Spark Ecosystem

50) Explain the Parquet File format in Apache Spark. When is it the best to choose this?

Ans. Parquet is the columnar information illustration that is that the best choice for storing long run massive information for analytics functions. It will perform each scan and write operations with Parquet file. It could be a columnar information storage format.



rm Tutorial
Question 14. What Is Lineage Graph?

Answer :

The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph. Lineage graph information is used to compute each RDD on demand, so that whenever a part of persistent RDD is lost, the data that is lost can be recovered using the lineage graph information.

Question 15. How Can You Trigger Automatic Clean-ups In Spark To Handle Accumulated Metadata?

Answer :

You can trigger the clean-ups by setting the parameter ‘spark.cleaner.ttl’ or by dividing the long running jobs into different batches and writing the intermediary results to the disk.

Apache Pig Interview Questions
Question 16. Explain About The Major Libraries That Constitute The Spark Ecosystem?

Answer :

Spark MLib- Machine learning library in Spark for commonly used learning algorithms like clustering, regression, classification, etc.

Spark Streaming – This library is used to process real time streaming data.

Spark GraphX – Spark API for graph parallel computations with basic operators like joinVertices, subgraph, aggregateMessages, etc.

Spark SQL – Helps execute SQL like queries on Spark data using standard visualization or BI tools.

Apache Hive Tutorial
Question 17. What Are The Benefits Of Using Spark With Apache Mesos?

Answer :

It renders scalable partitioning among various Spark instances and dynamic partitioning between Spark and other big data frameworks.

Apache Flume Interview Questions
Question 18. What Is The Significance Of Sliding Window Operation?

Answer :

Sliding Window controls transmission of data packets between various computer networks. Spark Streaming library provides windowed computations where the transformations on RDDs are applied over a sliding window of data. Whenever the window slides, the RDDs that fall within the particular window are combined and operated upon to produce new RDDs of the windowed DStream.

Apache Cassandra Interview Questions
Question 19. What Is A Dstream?

Answer :

Discretized Stream is a sequence of Resilient Distributed Databases that represent a stream of data. DStreams can be created from various sources like Apache Kafka, HDFS, and Apache Flume.

DStreams have two operations: –

Transformations that produce a new DStream.
Output operations that write data to an external system.
Apache Pig Tutorial
Question 20. When Running Spark Applications, Is It Necessary To Install Spark On All The Nodes Of Yarn Cluster?

Answer :

Spark need not be installed when running a job under YARN or Mesos because Spark can execute on top of YARN or Mesos clusters without affecting any change to the cluster.

Apache Kafka Interview Questions
Question 21. What Is Catalyst Framework?

Answer :

Catalyst framework is a new optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.

Question 22. Name A Few Companies That Use Apache Spark In Production.?

Answer :

Pinterest, Conviva, Shopify, Open Table

Apache Flume Tutorial
Question 23. Which Spark Library Allows Reliable File Sharing At Memory Speed Across Different Cluster Frameworks?

Answer :

Tachyon

Apache Ant Interview Questions
Question 24. Why Is Blinkdb Used?

Answer :

BlinkDB is a query engine for executing interactive SQL queries on huge volumes of data and renders query results marked with meaningful error bars. BlinkDB helps users balance ‘query accuracy’ with response time.

Apache Solr Interview Questions
Question 25. How Can You Compare Hadoop And Spark In Terms Of Ease Of Use?

Answer :

Hadoop MapReduce requires programming in Java which is difficult, though Pig and Hive make it considerably easier. Learning Pig and Hive syntax takes time. Spark has interactive APIs for different languages like Java, Python or Scala and also includes Shark i.e. Spark SQL for SQL lovers - making it comparatively easier to use than Hadoop.

Apache Kafka Tutorial
Question 26. What Are The Common Mistakes Developers Make When Running Spark Applications?

Answer :

Developers often make the mistake of:-

Hitting the web service several times by using multiple clusters.
Run everything on the local node instead of distributing it.
Developers need to be careful with this, as Spark makes use of memory for processing.
Apache Camel Interview Questions
Question 27. What Is The Advantage Of A Parquet File?

Answer :

Parquet file is a columnar format file that helps:

Limit I/O operations
Consumes less space
Fetches only required columns.
Apache Storm Interview Questions
Question 28. What Are The Various Data Sources Available In Sparksql?

Answer :

Parquet file
JSON Datasets
Hive tables
Apache Ant Tutorial
Question 29. What Are The Key Features Of Apache Spark That You Like?

Answer :

Spark provides advanced analytic options like graph algorithms, machine learning, streaming data, etc
It has built-in APIs in multiple languages like Java, Scala, Python and R
It has good performance gains, as it helps run an application in the Hadoop cluster ten times faster on disk and 100 times faster in memory.
Apache Tajo Interview Questions
Question 30. What Do You Understand By Pair Rdd?

Answer :

Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey () method that collects data based on each key and a join () method that combines different RDDs together, based on the elements having the same key.

Question 31. Explain About The Different Types Of Transformations On Dstreams?

Answer :

Stateless Transformations:- Processing of the batch does not depend on the output of the previous batch.

Examples: map (), reduceByKey (), filter ().

Stateful Transformations:- Processing of the batch depends on the intermediary results of the previous batch.

Examples: Transformations that depend on sliding windows.

Apache Tajo Tutorial
Question 32. Explain About The Popular Use Cases Of Apache Spark?

Answer :

Apache Spark is mainly used for:

Iterative machine learning.
Interactive data analytics and processing.
Stream processing
Sensor data processing
Apache Impala Interview Questions
Question 33. Is Apache Spark A Good Fit For Reinforcement Learning?

Answer :

No. Apache Spark works well only for simple machine learning algorithms like clustering, regression, classification.

Apache Hive Interview Questions
Question 34. What Is Spark Core?

Answer :

It has all the basic functionalities of Spark, like - memory management, fault recovery, interacting with storage systems, scheduling tasks, etc.

Question 35. How Can You Remove The Elements With A Key Present In Any Other Rdd?

Answer :

Use the subtractByKey () function.

Question 36. What Is The Difference Between Persist() And Cache()?

Answer :

persist () allows the user to specify the storage level where as cache () uses the default storage level.

Apache Pig Interview Questions
Question 37. What Are The Various Levels Of Persistence In Apache Spark?

Answer :

Apache Spark automatically persists the intermediary data from various shuffle operations, however it is often suggested that users call persist () method on the RDD in case they plan to reuse it. Spark has various persistence levels to store the RDDs on disk or in memory or as a combination of both with different replication levels.

The various storage/persistence levels in Spark are:

MEMORY_ONLY
MEMORY_ONLY_SER
MEMORY_AND_DISK
MEMORY_AND_DISK_SER, DISK_ONLY
OFF_HEAP

Question 38. How Spark Handles Monitoring And Logging In Standalone Mode?

Answer :

Spark has a web based user interface for monitoring the cluster in standalone mode that shows the cluster and job statistics. The log output for each job is written to the work directory of the slave nodes.

Question 39. Does Apache Spark Provide Check Pointing?

Answer :

Lineage graphs are always useful to recover RDDs from a failure but this is generally time consuming if the RDDs have long lineage chains. Spark has an API for check pointing i.e. a REPLICATE flag to persist. However, the decision on which data to checkpoint - is decided by the user. Checkpoints are useful when the lineage graphs are long and have wide dependencies.

Question 40. How Can You Launch Spark Jobs Inside Hadoop Mapreduce?

Answer :

Using SIMR (Spark in MapReduce) users can run any spark job inside MapReduce without requiring any admin rights.

Apache Flume Interview Questions
Question 41. How Spark Uses Akka?

Answer :

Spark uses Akka basically for scheduling. All the workers request for a task to master after registering. The master just assigns the task. Here Spark uses Akka for messaging between the workers and masters.

Question 42. How Can You Achieve High Availability In Apache Spark?

Answer :

Implementing single node recovery with local file system
Using StandBy Masters with Apache ZooKeeper.
Apache Kafka Interview Questions
Question 43. Hadoop Uses Replication To Achieve Fault Tolerance. How Is This Achieved In Apache Spark?

Answer :

Data storage model in Apache Spark is based on RDDs. RDDs help achieve fault tolerance through lineage. RDD always has the information on how to build from other datasets. If any partition of a RDD is lost due to failure, lineage helps build only that particular lost partition.

Question 44. Explain About The Core Components Of A Distributed Spark Application.?

Answer :

Driver: The process that runs the main () method of the program to create RDDs and perform transformations and actions on them.

Executor: The worker processes that run the individual tasks of a Spark job.

Cluster Manager: A pluggable component in Spark, to launch Executors and Drivers. The cluster manager allows Spark to run on top of other external managers like Apache Mesos or YARN.

Question 45. What Do You Understand By Lazy Evaluation?

Answer :

Spark is intellectual in the manner in which it operates on data. When you tell Spark to operate on a given dataset, it heeds the instructions and makes a note of it, so that it does not forget - but it does nothing, unless asked for the final result.

When a transformation like map () is called on a RDD-the operation is not performed immediately. Transformations in Spark are not evaluated till you perform an action. This helps optimize the overall data processing workflow.

Question 46. Define A Worker Node.?

Answer :

A node that can run the Spark application code in a cluster can be called as a worker node. A worker node can have more than one worker which is configured by setting the SPARK_ WORKER_INSTANCES property in the spark-env.sh file. Only one worker is started if the SPARK_ WORKER_INSTANCES property is not defined.

Question 47. What Do You Understand By Schemardd?

Answer :

An RDD that consists of row objects (wrappers around basic string or integer arrays) with schema information about the type of data in each column.

Question 48. What Are The Disadvantages Of Using Apache Spark Over Hadoop Mapreduce?

Answer :

Apache spark does not scale well for compute intensive jobs and consumes large number of system resources. Apache Spark’s in-memory capability at times comes a major roadblock for cost efficient processing of big data. Also, Spark does have its own file management system and hence needs to be integrated with other cloud based data platforms or apache hadoop.

Question 49. Is It Necessary To Install Spark On All The Nodes Of A Yarn Cluster While Running Apache Spark On Yarn ?

Answer :

No , it is not necessary because Apache Spark runs on top of YARN.

Question 50. What Do You Understand By Executor Memory In A Spark Application?

Answer :

Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag.

Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

Question 51. What Does The Spark Engine Do?

Answer :

Spark engine schedules, distributes and monitors the data application across the spark cluster.

Question 52. What Makes Apache Spark Good At Low-latency Workloads Like Graph Processing And Machine Learning?

Answer :

Apache Spark stores data in-memory for faster model building and training. Machine learning algorithms require multiple iterations to generate a resulting optimal model and similarly graph algorithms traverse all the nodes and edges.

These low latency workloads that need multiple iterations can lead to increased performance. Less disk access and  controlled network traffic make a huge difference when there is lots of data to be processed.



15) What is Dstream in Apache Spark?
    Dstream stands for Discretized Stream. It is a sequence of Resilient Distributed Database (RDD) representing a continuous stream of data. There are several ways to create Dstream from various sources like HDFS, Apache Flume, Apache Kafka, etc.

16) What do you understand by YARN?
    Just like in Hadoop, YARN is one of the key features in Apache Spark, which is used to provide a central and resource management platform to deliver scalable operations across the cluster. Spark can run on YARN, as the same way Hadoop Map Reduce can run on YARN.

17) Is it necessary to install Spark on all nodes of the YARN cluster?
    No. It doesn't seem necessary to install Spark on all YARN cluster nodes because Spark runs on top of the YARN. Apache Spark runs independently from its installation. Spark provides some options to use YARN when dispatching jobs to the cluster, rather than its built-in manager or Mesos. Besides this, there are also some configurations to run YARN, such as master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

18) What are the different data sources available in SparkSQL?
    There are the following three data sources available in SparkSQL:

JSON Datasets
Hive tables
Parquet file
19) Which are some important internal daemons used in Apache Spark?
    Following are the important internal daemons used in Spark:

Blockmanager
Memestore
DAGscheduler
Driver
Worker
Executor
Tasks etc.
20) What is the method to create a Data frame in Apache Spark?
    In Apache Spark, we can create a data frame using Tables in Hive and Structured data files.

21) What do you understand by accumulators in Apache Spark?
    Accumulators are the write-only variables that are initialized once and sent to the workers. Then, these workers update based on the logic written, which will send back to the driver.

22) What is the default level of parallelism in Apache Spark?
    If it is not specified, then the number of partitions is called the default level of parallelism in Apache Spark.

23) Which companies are using Spark streaming services?
    The three most famous companies using Spark Streaming services are:

Uber
Netflix
Pinterest
24) Is it possible to use Spark to access and analyze data stored in Cassandra databases?
    Yes, it is possible to use Spark to access and analyze Cassandra databases' data by using Cassandra Connector.

25) Can we run Apache Spark on Apache Mesos?
    Yes, we can run Apache Spark on the hardware clusters managed by Mesos.

26) What do you understand by Spark SQL?
    Spark SQL is a module for structured data processing, which provides the advantage of SQL queries running on that database.

27) How can you connect Spark to Apache Mesos?
    Follow the steps given below to connect Spark to Apache Mesos:

Configure the spark driver program to connect to Mesos.
Set a path location for the Spark binary package that it can be accessible by Mesos.
Install Apache Spark in the same location as that of Apache Mesos and configure the property 'spark.mesos.executor.home' to point to the location where it is installed.
28) What is the best way to minimize data transfers when working with Spark?
    To write a fast and reliable Spark program, we have to minimize data transfers and avoid shuffling. There are various ways to minimize data transfers while working with Apache Spark. These are:

Using Broadcast Variable- Broadcast variables enhance the efficiency of joins between small and large RDDs.

Using Accumulators- Accumulators are used to updating the values of variables in parallel while executing.

29) What do you understand by lazy evaluation in Apache Spark?
    As the name specifies, lazy evaluation in Apache Spark means that the execution will not start until an action is triggered. In Spark, the lazy evaluation comes into action when Spark transformations occur. Transformations are lazy. When a transformation such as a map() is called on an RDD, it is not performed instantly. Transformations in Spark are not evaluated until you perform an action, which aids in optimizing the overall data processing workflow, known as lazy evaluation. So we can say that in lazy evaluation, data is not loaded until it is necessary.

30) What do you understand by Spark Driver?
    Spark Driver is the program that runs on the master node of the machine and is used to declare transformations and actions on data RDDs.

31) What is the Parquet file in Apache Spark?
    Parquet is a column format file supported by many data processing systems. Spark SQL facilitates us to perform both read and write operations with the Parquet file.

32) What is the way to store the data in Apache Spark?
    Apache Spark is an open-source analytics and processing engine for large-scale data processing, but it does not have any storage engine. It can retrieve data from another storage engine like HDFS, S3.

33) How is it possible to implement machine learning in Apache Spark?
    Apache Spark itself provides a versatile machine learning library called MLif. By using this library, we can implement machine learning in Spark.

34) What are some disadvantages or demerits of using Apache Spark?
    Following is the list of some disadvantages or demerits of using Apache Spark:

Apache Spark requires more storage space than Hadoop and MapReduce, so that it may create some problems.
Apache Spark consumes a huge amount of data as compared to Hadoop.
Apache Spark requires more attentiveness because developers need to be careful while running their applications in Spark.
Spark runs on multiple clusters on different nodes instead of running everything on a single node. So, the work is distributed over multiple clusters.
The "in-memory" capability of Apache Spark makes it a more costly way for processing big data.
35) What is the use of File system API in Apache Spark?
    File system API is used to read data from various storage devices such as HDFS, S3 or Local Files.

36) What are the tasks of a Spark Engine?
    The main task of a Spark Engine is handling the process of scheduling, distributing and monitoring the data application across the clusters.

37) What is the use of Apache SparkContext?
    The SparkContent is the entry point to Apache Spark. SparkContext facilitates users to create RDDs, which provide various ways of churning data.

38) Is it possible to do real-time processing with SparkSQL?
    In SparkSQL, real-time data processing is not possible directly. We can register the existing RDD as a SQL table and trigger the SQL queries on priority.

39) What is the use of Akka in Apache Spark?
    Akka is used for scheduling in Apache Spark. Spark also uses Akka for messaging between the workers and masters.

40) What do you understand by Spark map() Transformation?
    Spark map() is a transformation operation used to apply the Transformation on every element of RDD, DataFrame, and Dataset and finally returns a new RDD/Dataset, respectively.

41) What is the advantage of using the Parquet file?
    In Apache Spark, the Parquet file is used to perform both read and write operations. Following is the list of some advantages of having a Parquet file:

Parquet file facilitates users to fetch specific columns for access.
It consumes less space.
It follows the type-specific encoding.
It supports limited I/O operations.
42) What is the difference between persist() and cache() functions in Apache Spark?
    In Apache Spark, the persist() function is used to allow the user to specify the storage level, whereas the cache() function uses the default storage level.

43) Which Spark libraries allow reliable file sharing at memory speed across different cluster frameworks?
    Tachyon is the Apache Spark library's name, which is used for reliable file sharing at memory speed across various cluster frameworks.

44) What is shuffling in Apache Spark? When does it occur?
    In Apache Spark, shuffling is the process of redistributing data across partitions that may lead to data movement across the executors. The implementation of shuffle operation is entirely different in Spark as compared to Hadoop.

Shuffling has two important compression parameters:

shuffle.compress: It is used to check whether the engine would compress shuffle outputs or not.
shuffle.spill.compress: It is used to decide whether to compress intermediate shuffle spill files or not.
Shuffling comes in the scene when we join two tables or perform byKey operations such as GroupByKey or ReduceByKey.

45) What are the file formats supported by Apache Spark?
    Apache Spark supports the file format such as json, tsv, snappy, orc, rc, etc.

46) What are Actions in Apache Spark?
    In Apache Spark, the action is used to bring back the RDD data to the local machine. Its execution is the result of all previously created transformations.

47) What is Yarn in Apache Spark?
    Yarn is one of the most important features of Apache Spark. Apache Spark is an in-memory distributed data processing engine, and YARN is a cluster management technology that is used to run Spark. Yarn makes you able to dynamically share and centrally configure the same pool of cluster resources between all frameworks that run on Yarn. When Spark runs on Yarn, it makes the binary distribution as it is built on Yarn support.

48) In which type of machine learning techniques, Apache Spark is the best fit?
    Apache Spark is the best fit for simple machine learning algorithms like clustering, regression, and classification, etc.

49) What is the use of checkpoints in Apache Spark?
    In Apache Spark, checkpoints are used to allow the program to run all around the clock. It also helps to make it resilient towards failure irrespective of application logic.

50) What is the lineage in Spark?
    In Apache Spark, when a transformation (map or filter etc.) is called, it is not executed by Spark immediately; instead, a lineage is created for each transformation. This lineage is used to keep track of what all transformations have to be applied on that RDD. It also traces the location from where it has to read the data.

51) What do you understand by a lineage graph in Spark?
    In Apache Spark, the lineage graph is a dependencies graph between existing RDD and new RDD. It specifies that all the dependencies between the RDD are recorded in a graph rather than the original data.

52) How can you trigger automatic clean-ups in Spark to handle accumulated metadata?
    You can trigger the clean-ups by setting the parameter ' Spark.cleaner.ttl' or dividing the long-running jobs into different batches and writing the intermediary results to the disk.

53) Is it possible to launch Spark jobs inside Hadoop MapReduce?
    Yes, you can run all kinds of spark jobs inside MapReduce without the need to obtain the admin rights of that application.

54) What is the use of BlinkDB in Spark?
    BlinkDB is a query engine tool used to execute SQL queries on massive volumes of data and renders query results in the meaningful error bars.

55) Can Spark handle monitoring and logging in Standalone mode?
    Yes. Because of having a web-based user interface, Spark can handle monitoring and logging in standalone mode.

56) How SparkSQL is different from SQL and HQL?
    SparkSQL is a unique component on the Apache Spark core engine that supports SQL and HQL without changing any syntax. HQL stands for Hive Query Language. You can also join the SQL table and HQL table.