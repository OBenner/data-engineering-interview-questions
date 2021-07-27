What are the main features of Apache Spark?
Main features of Apache Spark are as follows:
Performance: The key feature of Apache Spark is its Performance. With Apache Spark we can run programs up to 100 times faster than Hadoop MapReduce in memory. On disk we can run it 10 times faster than Hadoop.
Ease of Use: Spark supports Java, Python, R, Scala etc. languages. So it makes it much easier to develop applications for Apache Spark.
Integrated Solution: In Spark we can create an integrated solution that combines the power of SQL, Streaming and data analytics.
Run Everywhere: Apache Spark can run on many platforms. It can run on Hadoop, Mesos, in Cloud or standalone. It can also connect to many data sources like HDFS, Cassandra, HBase, S3 etc.
Stream Processing: Apache Spark also supports real time stream processing. With real time streaming we can provide real time analytics solutions. This is very useful for real-time data.

103.	What is a Resilient Distribution Dataset in Apache Spark?
        Resilient Distribution Dataset (RDD) is an abstraction of data in Apache Spark. It is a distributed and resilient collection of records spread over many partitions. RDD hides the data partitioning and distribution behind the scenes. Main	features of RDD 	are as follows:
        Distributed: Data in a RDD is distributed across multiple nodes.
        Resilient: RDD is a fault- tolerant dataset. In case of node failure, Spark can re- compute data.
        Dataset: It is a collection of data similar to collections in Scala.
        Immutable: Data in RDD cannot be modified after creation. But we can transform it using a Transformation.

What is a Transformation in Apache Spark?
Transformation in Apache Spark is a function that can be applied to a RDD. Output of a Transformation is another RDD. Transformation in Spark is a lazy operation. It means it is not executed immediately. Once we call an action, transformation is executed. A Transformation does not change the input RDD. We can also create a pipeline of certain Transformations to create a Data flow.

What are security options in Apache Spark?
Apache Spark provides following security options:
Encryption: Apache Spark supports encryption by SSL. We can use HTTPS protocol for secure data transfer. Therefore data is transmitted in encrypted mode. We can use spark.ssl parameters to set the SSL configuration.

Authentication: We can perform authentication by a shared secret in Apache Spark. We can use spark.authenticate	to configure authentication in Spark.
Event Logging: If we use Event Logging, then we can set the permissions on the directory where event logs are	stored.	These permissions can ensure access control for Event log.

106.	How will you monitor Apache Spark?
        We can use the Web UI provided by SparkContext to monitor Spark. We can access this Web UI at port 4040 to get the useful information. Some of the information that we can monitor is:
        Scheduler tasks and stages RDD	Sizes	and	Memory usage Spark	Environment Information
        Executors Information
        Spark also provides a Metrics library. This library can be used to send Spark information to HTTP, JMX, CSV files etc.This is another option to collect Spark runtime information for monitoring another dashboard tool.

107.	What are the main libraries of Apache Spark?
        Some	of the main libraries of Apache Spark are as follows:
        MLib: This is Spark’s Machine Learning library. We can use it to create scalable machine learning system. We can use various machine learning algorithms as well as features like pipelining etc with this library.
        GraphX: This library is used for computation of Graphs. It helps in creating a Graph abstraction of data and then use various Graph operators like- SubGraph, joinVertices etc.
        Structured Streaming: This library is used for handling streams in Spark. It is a fault tolerant system built on top of Spark SQL Engine to process streams.
        Spark SQL: This is another popular component that is used	for	processing	SQL queries on Spark platform.
        SparkR: This is a package in Spark to use Spark from R language. We can use R data frames, dplyr etc from this package. We can also start SparkR from RStudio.

108.	What are the main functions of Spark Core in Apache Spark?
        Spark Core is the central component of Apache Spark. It serves following functions:
        Distributed Task Dispatching
        Job Scheduling
        I/O Functions

109.	How will you do memory tuning in Spark?
        In case of memory tuning we have to take care of these points.

Amount of memory used by objects Cost of accessing objects Overhead	of Garbage Collection
Apache Spark stores objects in memory for caching. So it becomes important to perform memory tuning in a Spark application. First we determine the memory usage by the application. To do this we first create a RDD and put it in cache. Now we can see the size of the RDD in storage page of Web UI. This will tell the amount of memory consumed by RDD. Based on the memory usage, we can estimate the amount of memory needed for our task. In case we need tuning, we can follow these practices to reduce memory usage:
Use data structures like Array of objects or primitives instead of Linked list or HashMap. Fastutil library provides convenient collection classes for primitive types compatible with Java.
We have to reduce the usage of nested data structures with a large number of small objects and pointes. E.g. Linked list has pointers within each node.
It is a good practice to use numeric IDs instead of Strings for keys.
We can also use JVM flag - XX:+UseCompressedOops to	make	pointers	be	four bytes instead of eight.

110.	What are the two ways to create RDD in Spark?
        We can create RDD in Spark in following two ways:
        Internal: We can parallelize an existing collection of data within our Spark Driver program and create a RDD out of it.
        External: We can also create RDD by referencing a Dataset in an external data source like AWS S3, HDFS, HBASE etc.

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