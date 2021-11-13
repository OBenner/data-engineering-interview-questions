[Interview questions](full.md)
# Apache Spark
+ [What are the main features of Apache Spark?](#What-are-the-main-features-of-Apache-Spark)
+ [What is a Resilient Distribution Dataset in Apache Spark?](#What-is-a-Resilient-Distribution-Dataset-in-Apache-Spark)
+ [What is a Transformation in Apache Spark?](#What-is-a-Transformation-in-Apache-Spark)
+ [What are security options in Apache Spark?](#What-are-security-options-in-Apache-Spark)
+ [How will you monitor Apache Spark?](#How-will-you-monitor-Apache-Spark)
+ [What are the main libraries of Apache Spark?](#What-are-the-main-libraries-of-Apache-Spark)
+ [What are the main functions of Spark Core in Apache Spark?](#What-are-the-main-functions-of-Spark-Core-in-Apache-Spark)
+ [How will you do memory tuning in Spark?](#How-will-you-do-memory-tuning-in-Spark)
+ [What are the two ways to create RDD in Spark?](#What-are-the-two-ways-to-create-RDD-in-Spark)
+ [What are the main operations that can be done on a RDD in Apache Spark?](#What-are-the-main-operations-that-can-be-done-on-a-RDD-in-Apache-Spark)
+ [What are the common Transformations in Apache Spark?](#What-are-the-common-Transformations-in-Apache-Spark)
+ [What are the common Actions in Apache Spark?](#What-are-the-common-Actions-in-Apache-Spark)
+ [What is a Shuffle operation in Spark?](#What-is-a-Shuffle-operation-in-Spark)
+ [What are the operations that can cause a shuffle in Spark?](#What-are-the-operations-that-can-cause-a-shuffle-in-Spark)
+ [What is purpose of Spark SQL?](#What-is-purpose-of-Spark-SQL)
+ [What is a DataFrame in Spark SQL?](#What-is-a-DataFrame-in-Spark-SQL)
+ [What is a Parquet file in Spark?](#What-is-a-Parquet-file-in-Spark)
+ [What is the difference between Apache Spark and Apache Hadoop MapReduce?](#What-is-the-difference-between-Apache-Spark-and-Apache-Hadoop-MapReduce)
+ [What are the main languages supported by Apache Spark?](#What-are-the-main-languages-supported-by-Apache-Spark)
+ [What are the file systems supported by Spark?](#What-are-the-file-systems-supported-by-Spark)
+ [What is a Spark Driver?](#What-is-a-Spark-Driver)
+ [What is an RDD Lineage?](#What-is-an-RDD-Lineage)
+ [What are the two main types of Vector in Spark?](#What-are-the-two-main-types-of-Vector-in-Spark)
+ [What are the different deployment modes of Apache Spark?](#What-are-the-different-deployment-modes-of-Apache-Spark)
+ [What is lazy evaluation in Apache Spark?](#What-is-lazy-evaluation-in-Apache-Spark)
+ [What are the core components of a distributed application in Apache Spark?](#What-are-the-core-components-of-a-distributed-application-in-Apache-Spark)
+ [What is the difference in cache() and persist() methods in Apache Spark?](#What-is-the-difference-in-cache()-and-persist()-methods-in-Apache-Spark)
+ [How will you remove data from cache in Apache Spark?](#How-will-you-remove-data-from-cache-in-Apache-Spark)
+ [What is the use of SparkContext in Apache Spark?](#What-is-the-use-of-SparkContext-in-Apache-Spark)
+ [Do we need HDFS for running Spark application?](#Do-we-need-HDFS-for-running-Spark-application)
+ [What is Spark Streaming?](#What-is-Spark-Streaming)
+ [How does Spark Streaming work internally?](#How-does-Spark-Streaming-work-internally)
+ [What is a Pipeline in Apache Spark?](#What-is-a-Pipeline-in-Apache-Spark)
+ [How does Pipeline work in Apache Spark?](#How-does-Pipeline-work-in-Apache-Spark)
+ [What is the difference between Transformer and Estimator in Apache Spark?](#What-is-the-difference-between-Transformer-and-Estimator-in-Apache-Spark)
+ [What are the different types of Cluster Managers in Apache Spark?](#What-are-the-different-types-of-Cluster-Managers-in-Apache-Spark)
+ [How will you minimize data transfer while working with Apache Spark?](#How-will-you-minimize-data-transfer-while-working-with-Apache-Spark)
+ [What is the main use of MLib in Apache Spark?](#What-is-the-main-use-of-MLib-in-Apache-Spark)
+ [What is the Checkpointing in Apache Spark?](#What-is-the-Checkpointing-in-Apache-Spark)
+ [What is an Accumulator in Apache Spark?](#What-is-an-Accumulator-in-Apache-Spark)
+ [What is a Broadcast variable in Apache Spark?](#What-is-a-Broadcast-variable-in-Apache-Spark)
+ [What is Structured Streaming in Apache Spark?](#What-is-Structured-Streaming-in-Apache-Spark)
+ [How will you pass functions to Apache Spark?](#How-will-you-pass-functions-to-Apache-Spark)
+ [What is a Property Graph?](#What-is-a-Property-Graph)
+ [What is Neighborhood Aggregation in Spark?](#What-is-Neighborhood-Aggregation-in-Spark)
+ [What are different Persistence levels in Apache Spark?](#What-are-different-Persistence-levels-in-Apache-Spark)
+ [How will you select the storage level in Apache Spark?](#How-will-you-select-the-storage-level-in-Apache-Spark)
+ [What are the options in Spark to create a Graph?](#What-are-the-options-in-Spark-to-create-a-Graph)
+ [What are the basic Graph operators in Spark?](#What-are-the-basic-Graph-operators-in-Spark)
+ [What is the partitioning approach used in GraphX of Apache Spark?](#What-is-the-partitioning-approach-used-in-GraphX-of-Apache-Spark)
+ [What is RDD?](#What-is-RDD)
+ [Name the different types of RDD](#Name-the-different-types-of-RD)
+ [What are the methods of creating RDDs in Spark?](#What-are-the-methods-of-creating-RDDs-in-Spark)
+ [What is a Sparse Vector?](#What-is-a-Sparse-Vector)
+ [What are the languages supported by Apache Spark and which is the most popular one, What is JDBC and why it is popular?](#What-are-the-languages-supported-by-Apache-Spark-and-which-is-the-most-popular-one,-What-is-JDBC-and-why-it-is-popular)
+ [What is Yarn?](#What-is-Yarn)
+ [Do you need to install Spark on all nodes of Yarn cluster? Why?](#Do-you-need-to-install-Spark-on-all-nodes-of-Yarn-cluster?-Why)
+ [Is it possible to run Apache Spark on Apache Mesos?](#Is-it-possible-to-run-Apache-Spark-on-Apache-Mesos)
+ [What is lineage graph?](#What-is-lineage-graph)
+ [Define Partitions in Apache Spark](#Define-Partitions-in-Apache-Spar)
+ [What is a DStream?](#What-is-a-DStream)
+ [What is a Catalyst framework?](#What-is-a-Catalyst-framework)
+ [What are Actions in Spark?](#What-are-Actions-in-Spark)
+ [What is a Parquet file?](#What-is-a-Parquet-file)
+ [What is GraphX?](#What-is-GraphX)
+ [What file systems does Spark support?](#What-file-systems-does-Spark-support)
+ [What are the different types of transformations on DStreams? Explain.](#What-are-the-different-types-of-transformations-on-DStreams?-Explain)
+ [What is the difference between persist () and cache ()?](#What-is-the-difference-between-persist-()-and-cache-())
+ [What do you understand by SchemaRDD?](#What-do-you-understand-by-SchemaRDD)
+ [What is Apache Spark?](#What-is-Apache-Spark)
+ [Explain key features of Spark.](#Explain-key-features-of-Spark)
+ [Define RDD?](#Define-RDD)
+ [What does a Spark Engine do?](#What-does-a-Spark-Engine-do)
+ [Define Partitions?](#Define-Partitions)
+ [What do you understand by Transformations in Spark?](#What-do-you-understand-by-Transformations-in-Spark)
+ [Define Actions.](#Define-Actions)
+ [Define functions of SparkCore?](#Define-functions-of-SparkCore)
+ [What is RDD Lineage?](#What-is-RDD-Lineage)
+ [What is Spark Driver?](#What-is-Spark-Driver)
+ [What is Hive on Spark?](#What-is-Hive-on-Spark)
+ [Define Spark Streaming.](#Define-Spark-Streaming)
+ [What is Spark SQL?](#What-is-Spark-SQL)
+ [List the functions of Spark SQL?](#List-the-functions-of-Spark-SQL)
+ [What are benefits of Spark over MapReduce?](#What-are-benefits-of-Spark-over-MapReduce)
+ [What is Spark Executor?](#What-is-Spark-Executor)
+ [What do you understand by worker node?](#What-do-you-understand-by-worker-node)
+ [Illustrate some demerits of using Spark.](#Illustrate-some-demerits-of-using-Spark)
+ [What is the advantage of a Parquet file?](#What-is-the-advantage-of-a-Parquet-file)
+ [What are different o/p methods to get result?](#What-are-different-o/p-methods-to-get-result)
+ [What are two ways to attain a schema from data?](#What-are-two-ways-to-attain-a-schema-from-data)
+ [Why should you define your own schema?](#Why-should-you-define-your-own-schema)
+ [Why is JSON a common format in big data pipelines?](#Why-is-JSON-a-common-format-in-big-data-pipelines)
+ [By default, how are corrupt records dealt with using  spark.read.json()?](#By-default,-how-are-corrupt-records-dealt-with-using-spark.read.json())
+ [Explain the key features of Apache Spark.](#Explain-the-key-features-of-Apache-Spark)
+ [What are benefits of Spark over MapReduce?](#What-are-benefits-of-Spark-over-MapReduce)
+ [What is YARN?](#What-is-YARN)
+ [Do you need to install Spark on all nodes of YARN cluster?](#Do-you-need-to-install-Spark-on-all-nodes-of-YARN-cluster)
+ [Is there any benefit of learning MapReduce if Spark is better than MapReduce?](#Is-there-any-benefit-of-learning-MapReduce-if-Spark-is-better-than-MapReduce)
+ [Explain the concept of Resilient Distributed Dataset (RDD).](#Explain-the-concept-of-Resilient-Distributed-Dataset-(RDD))
+ [How do we create RDDs in Spark?](#How-do-we-create-RDDs-in-Spark)
+ [What is Executor Memory in a Spark application?](#What-is-Executor-Memory-in-a-Spark-application)
+ [Define Partitions in Apache Spark.](#Define-Partitions-in-Apache-Spark)
+ [What operations does RDD support?](#What-operations-does-RDD-support)
+ [What do you understand by Transformations in Spark?](#What-do-you-understand-by-Transformations-in-Spark)
+ [Define Actions in Spark.](#Define-Actions-in-Spark)
+ [Define functions of SparkCore.](#Define-functions-of-SparkCore)
+ [Memory management and fault recovery](#Memory-management-and-fault-recover)
+ [What do you understand by Pair RDD?](#What-do-you-understand-by-Pair-RDD)
+ [How is Streaming implemented in Spark? Explain with examples.](#How-is-Streaming-implemented-in-Spark?-Explain-with-examples)
+ [Is there an API for implementing graphs in Spark?](#Is-there-an-API-for-implementing-graphs-in-Spark)
+ [What is PageRank in GraphX?](#What-is-PageRank-in-GraphX)
+ [How is machine learning implemented in Spark?](#How-is-machine-learning-implemented-in-Spark)
+ [Is there a module to implement SQL in Spark? How does it work?](#Is-there-a-module-to-implement-SQL-in-Spark?-How-does-it-work)
+ [What are receivers in Apache Spark Streaming?](#What-are-receivers-in-Apache-Spark-Streaming)
+ [What do you understand by Shuffling in Spark?](#What-do-you-understand-by-Shuffling-in-Spark)
+ [How is Apache Spark different from MapReduce?](#How-is-Apache-Spark-different-from-MapReduce)
+ [Explain the working of Spark with the help of its architecture.](#Explain-the-working-of-Spark-with-the-help-of-its-architecture)
+ [What is the working of DAG in Spark?](#What-is-the-working-of-DAG-in-Spark)
+ [Under what scenarios do you use Client and Cluster modes for deployment?](#Under-what-scenarios-do-you-use-Client-and-Cluster-modes-for-deployment)
+ [What is Spark Streaming and how is it implemented in Spark?](#What-is-Spark-Streaming-and-how-is-it-implemented-in-Spark)
+ [What can you say about Spark Datasets?](#What-can-you-say-about-Spark-Datasets)
+ [Define Spark DataFrames.](#Define-Spark-DataFrames)
+ [Define Executor Memory in Spark](#Define-Executor-Memory-in-Spar)
+ [What are the functions of SparkCore?](#What-are-the-functions-of-SparkCore)
+ [What do you understand by worker node?](#What-do-you-understand-by-worker-node)
+ [What are some demerits of using Spark in applications?](#What-are-some-demerits-of-using-Spark-in-applications)
+ [How can the data transfers be minimized while working with Spark?](#How-can-the-data-transfers-be-minimized-while-working-with-Spark)
+ [What is SchemaRDD in Spark RDD?](#What-is-SchemaRDD-in-Spark-RDD)
+ [What module is used for implementing SQL in Apache Spark?](#What-module-is-used-for-implementing-SQL-in-Apache-Spark)
+ [What are the steps to calculate the executor memory?](#What-are-the-steps-to-calculate-the-executor-memory)
+ [Why do we need broadcast variables in Spark?](#Why-do-we-need-broadcast-variables-in-Spark)
+ [Can Apache Spark be used along with Hadoop? If yes, then how?](#Can-Apache-Spark-be-used-along-with-Hadoop?-If-yes,-then-how)
+ [What are Sparse Vectors? How are they different from dense vectors?](#What-are-Sparse-Vectors?-How-are-they-different-from-dense-vectors)
+ [How are automatic clean-ups triggered in Spark for handling the accumulated metadata?](#How-are-automatic-clean-ups-triggered-in-Spark-for-handling-the-accumulated-metadata)
+ [How is Caching relevant in Spark Streaming?](#How-is-Caching-relevant-in-Spark-Streaming)
+ [Define Piping in Spark.](#Define-Piping-in-Spark)
+ [What API is used for Graph Implementation in Spark?](#What-API-is-used-for-Graph-Implementation-in-Spark)
+ [How can you achieve machine learning in Spark?](#How-can-you-achieve-machine-learning-in-Spark)
+ [What are the limitations of Spark?](#What-are-the-limitations-of-Spark)
+ [Compare Hadoop and Spark.](#Compare-Hadoop-and-Spark)
+ [What is lazy evaluation in Spark?](#What-is-lazy-evaluation-in-Spark)
+ [What are the benefits of lazy evaluation?](#What-are-the-benefits-of-lazy-evaluation)
+ [What do you mean by Persistence?](#What-do-you-mean-by-Persistence)
+ [Explain the run time architecture of Spark?](#Explain-the-run-time-architecture-of-Spark)
+ [What is the difference between DSM and RDD?](#What-is-the-difference-between-DSM-and-RDD)
+ [How can data transfer be minimized when working with Apache Spark?](#How-can-data-transfer-be-minimized-when-working-with-Apache-Spark)
+ [How does Apache Spark handles accumulated Metadata?](#How-does-Apache-Spark-handles-accumulated-Metadata)
+ [What are the common faults of the developer while using Apache Spark?](#What-are-the-common-faults-of-the-developer-while-using-Apache-Spark)
+ [Which among the two is preferable for the project- Hadoop MapReduce or Apache Spark?](#Which-among-the-two-is-preferable-for-the-project--Hadoop-MapReduce-or-Apache-Spark)
+ [List the popular use cases of Apache Spark.](#List-the-popular-use-cases-of-Apache-Spark)
+ [What is Spark.executor.memory in a Spark Application?](#What-is-Spark.executor.memory-in-a-Spark-Application)
+ [What is DataFrames?](#What-is-DataFrames)
+ [What are the advantages of DataFrame?](#What-are-the-advantages-of-DataFrame)
+ [What is DataSet?](#What-is-DataSet)
+ [What are the advantages of DataSets?](#What-are-the-advantages-of-DataSets)
+ [Explain Catalyst framework.](#Explain-Catalyst-framework)
+ [What is DStream?](#What-is-DStream)
+ [Explain different transformation on DStream.](#Explain-different-transformation-on-DStream)
+ [What is written ahead log or journaling?](#What-is-written-ahead-log-or-journaling)
+ [Explain first operation in Apache Spark RDD.](#Explain-first-operation-in-Apache-Spark-RDD)
+ [Describe join operation. How is outer join supported?](#Describe-join-operation.-How-is-outer-join-supported)
+ [Describe coalesce operation. When can you coalesce to a larger number of partitions? Explain.](#Describe-coalesce-operation.-When-can-you-coalesce-to-a-larger-number-of-partitions?-Explain)
+ [Describe Partition and Partitioner in Apache Spark.](#Describe-Partition-and-Partitioner-in-Apache-Spark)
+ [How can you manually partition the RDD?](#How-can-you-manually-partition-the-RDD)
+ [Explain API create Or Replace TempView.](#Explain-API-create-Or-Replace-TempView)
+ [What are the various advantages of DataFrame over RDD in Apache Spark?](#What-are-the-various-advantages-of-DataFrame-over-RDD-in-Apache-Spark)
+ [What is a DataSet and what are its advantages over DataFrame and RDD?](#What-is-a-DataSet-and-what-are-its-advantages-over-DataFrame-and-RDD)
+ [On what all basis can you differentiate RDD and DataFrame and DataSet?](#On-what-all-basis-can-you-differentiate-RDD-and-DataFrame-and-DataSet)
+ [Explain the level of parallelism in Spark Streaming.](#Explain-the-level-of-parallelism-in-Spark-Streaming)
+ [Discuss writeahead logging in Apache Spark Streaming.](#Discuss-writeahead-logging-in-Apache-Spark-Streaming)
+ [What do you mean by Speculative execution in Apache Spark?](#What-do-you-mean-by-Speculative-execution-in-Apache-Spark)
+ [How do you parse data in XML? Which kind of class do you use with java to pass data?](#How-do-you-parse-data-in-XML?-Which-kind-of-class-do-you-use-with-java-to-pass-data)
+ [Explain Machine Learning library in Spark.](#Explain-Machine-Learning-library-in-Spark)
+ [List various commonly used Machine Learning Algorithm.](#List-various-commonly-used-Machine-Learning-Algorithm)
+ [Explain the Parquet File format in Apache Spark. When is it the best to choose this?](#Explain-the-Parquet-File-format-in-Apache-Spark.-When-is-it-the-best-to-choose-this)
+ [What is Lineage Graph?](#What-is-Lineage-Graph)
+ [How can you Trigger Automatic Cleanups in Spark to Handle Accumulated Metadata?](#How-can-you-Trigger-Automatic-Cleanups-in-Spark-to-Handle-Accumulated-Metadata)
+ [What are the benefits of using Spark With Apache Mesos?](#What-are-the-benefits-of-using-Spark-With-Apache-Mesos)
+ [What is the Significance of Sliding Window Operation?](#What-is-the-Significance-of-Sliding-Window-Operation)
+ [When running Spark Applications is it necessary to install Spark on all Nodes of Yarn Cluster?](#When-running-Spark-Applications-is-it-necessary-to-install-Spark-on-all-Nodes-of-Yarn-Cluster)
+ [What is Catalyst Framework?](#What-is-Catalyst-Framework)
+ [Which Spark Library allows reliable File Sharing at Memory Speed across different cluster frameworks?](#Which-Spark-Library-allows-reliable-File-Sharing-at-Memory-Speed-across-different-cluster-frameworks)
+ [Why is Blinkdb used?](#Why-is-Blinkdb-used)
+ [How can you compare Hadoop and Spark in terms of ease of use?](#How-can-you-compare-Hadoop-and-Spark-in-terms-of-ease-of-use)
+ [What are the common mistakes developers make when running Spark Applications?](#What-are-the-common-mistakes-developers-make-when-running-Spark-Applications)
+ [What is the Advantage of a Parquet File?](#What-is-the-Advantage-of-a-Parquet-File)
+ [What are the various Data Sources available in Sparksql?](#What-are-the-various-Data-Sources-available-in-Sparksql)
+ [What are the Key Features of Apache Spark that you like?](#What-are-the-Key-Features-of-Apache-Spark-that-you-like)
+ [What do you understand by Pair Rdd?](#What-do-you-understand-by-Pair-Rdd)
+ [Explain about different Types of Transformations on Dstreams?](#Explain-about-different-Types-of-Transformations-on-Dstreams)
+ [Explain about popular use cases of Apache Spark?](#Explain-about-popular-use-cases-of-Apache-Spark)
+ [Is Apache Spark a good fit for reinforcement Learning?](#Is-Apache-Spark-a-good-fit-for-reinforcement-Learning)
+ [What is Spark Core?](#What-is-Spark-Core)
+ [How can you remove the elements with a Key present in any other Rdd?](#How-can-you-remove-the-elements-with-a-Key-present-in-any-other-Rdd)
+ [What is the difference between Persist and Cache?](#What-is-the-difference-between-Persist-and-Cache)
+ [How Spark handles Monitoring and Logging in Standalone Mode?](#How-Spark-handles-Monitoring-and-Logging-in-Standalone-Mode)
+ [Does Apache Spark provide check pointing?](#Does-Apache-Spark-provide-check-pointing)
+ [How can you launch Spark Jobs inside Hadoop Mapreduce?](#How-can-you-launch-Spark-Jobs-inside-Hadoop-Mapreduce)
+ [How can you achieve High Availability in Apache Spark?](#How-can-you-achieve-High-Availability-in-Apache-Spark)
+ [Hadoop uses Replication to achieve Fault Tolerance and how is this achieved in Apache Spark?](#Hadoop-uses-Replication-to-achieve-Fault-Tolerance-and-how-is-this-achieved-in-Apache-Spark)
+ [Explain about Core Components of a distributed Spark Application?](#Explain-about-Core-Components-of-a-distributed-Spark-Application)
+ [What do you understand by Lazy Evaluation?](#What-do-you-understand-by-Lazy-Evaluation)
+ [Define a Worker Node?](#Define-a-Worker-Node)
+ [What do you understand by Schemardd?](#What-do-you-understand-by-Schemardd)
+ [What are the disadvantages of using Apache Spark over Hadoop Mapreduce?](#What-are-the-disadvantages-of-using-Apache-Spark-over-Hadoop-Mapreduce)
+ [Is it necessary to install Spark on all Nodes of Yarn Cluster while running Apache Spark on Yarn?](#Is-it-necessary-to-install-Spark-on-all-Nodes-of-Yarn-Cluster-while-running-Apache-Spark-on-Yarn)
+ [What do you understand by Executor Memory in Spark Application?](#What-do-you-understand-by-Executor-Memory-in-Spark-Application)
+ [What does the Spark Engine do?](#What-does-the-Spark-Engine-do)
+ [What makes Apache Spark good at Low latency Workloads like Graph Processing and Machine Learning?](#What-makes-Apache-Spark-good-at-Low-latency-Workloads-like-Graph-Processing-and-Machine-Learning)
+ [What is Dstream in Apache Spark?](#What-is-Dstream-in-Apache-Spark)
+ [What do you understand by YARN?](#What-do-you-understand-by-YARN)
+ [Is it necessary to install Spark on all nodes of the YARN cluster?](#Is-it-necessary-to-install-Spark-on-all-nodes-of-the-YARN-cluster)
+ [What are the different data sources available in SparkSQL?](#What-are-the-different-data-sources-available-in-SparkSQL)
+ [Which are some important internal daemons used in Apache Spark?](#Which-are-some-important-internal-daemons-used-in-Apache-Spark)
+ [What is the method to create a Data frame in Apache Spark?](#What-is-the-method-to-create-a-Data-frame-in-Apache-Spark)
+ [What do you understand by accumulators in Apache Spark?](#What-do-you-understand-by-accumulators-in-Apache-Spark)
+ [What is the default level of parallelism in Apache Spark?](#What-is-the-default-level-of-parallelism-in-Apache-Spark)
+ [Which companies are using Spark streaming services?](#Which-companies-are-using-Spark-streaming-services)
+ [Is it possible to use Spark to access and analyze data stored in Cassandra databases?](#Is-it-possible-to-use-Spark-to-access-and-analyze-data-stored-in-Cassandra-databases)
+ [Can we run Apache Spark on Apache Mesos?](#Can-we-run-Apache-Spark-on-Apache-Mesos)
+ [What do you understand by Spark SQL?](#What-do-you-understand-by-Spark-SQL)
+ [How can you connect Spark to Apache Mesos?](#How-can-you-connect-Spark-to-Apache-Mesos)
+ [What is the best way to minimize data transfers when working with Spark?](#What-is-the-best-way-to-minimize-data-transfers-when-working-with-Spark)
+ [What do you understand by lazy evaluation in Apache Spark?](#What-do-you-understand-by-lazy-evaluation-in-Apache-Spark)
+ [What do you understand by Spark Driver?](#What-do-you-understand-by-Spark-Driver)
+ [What is the Parquet file in Apache Spark?](#What-is-the-Parquet-file-in-Apache-Spark)
+ [What is the way to store the data in Apache Spark?](#What-is-the-way-to-store-the-data-in-Apache-Spark)
+ [How is it possible to implement machine learning in Apache Spark?](#How-is-it-possible-to-implement-machine-learning-in-Apache-Spark)
+ [What are some disadvantages or demerits of using Apache Spark?](#What-are-some-disadvantages-or-demerits-of-using-Apache-Spark)
+ [What is the use of File system API in Apache Spark?](#What-is-the-use-of-File-system-API-in-Apache-Spark)
+ [What are the tasks of a Spark Engine?](#What-are-the-tasks-of-a-Spark-Engine)
+ [What is the use of Apache SparkContext?](#What-is-the-use-of-Apache-SparkContext)
+ [Is it possible to do real-time processing with SparkSQL?](#Is-it-possible-to-do-real-time-processing-with-SparkSQL)
+ [What is the use of Akka in Apache Spark?](#What-is-the-use-of-Akka-in-Apache-Spark)
+ [What do you understand by Spark map() Transformation?](#What-do-you-understand-by-Spark-map()-Transformation)
+ [What is the advantage of using the Parquet file?](#What-is-the-advantage-of-using-the-Parquet-file)
+ [What is the difference between persist() and cache() functions in Apache Spark?](#What-is-the-difference-between-persist()-and-cache()-functions-in-Apache-Spark)
+ [Which Spark libraries allow reliable file sharing at memory speed across different cluster frameworks?](#Which-Spark-libraries-allow-reliable-file-sharing-at-memory-speed-across-different-cluster-frameworks)
+ [What is shuffling in Apache Spark? When does it occur?](#What-is-shuffling-in-Apache-Spark?-When-does-it-occur)
+ [What is the lineage in Spark?](#What-is-the-lineage-in-Spark)
+ [How can you trigger automatic clean-ups in Spark to handle accumulated metadata?](#How-can-you-trigger-automatic-clean-ups-in-Spark-to-handle-accumulated-metadata)
+ [Is it possible to launch Spark jobs inside Hadoop MapReduce?](#Is-it-possible-to-launch-Spark-jobs-inside-Hadoop-MapReduce)
+ [What is the use of BlinkDB in Spark?](#What-is-the-use-of-BlinkDB-in-Spark)

[Table of Contents](#Apache-Spark)

## What are the main features of Apache Spark?
Main features of Apache Spark are as follows:
+ Performance: The key feature of Apache Spark is its Performance. With Apache Spark we can run programs up to 100 times faster than Hadoop MapReduce in memory. On disk we can run it 10 times faster than Hadoop.
+ Ease of Use: Spark supports Java, Python, R, Scala etc. languages. So it makes it much easier to develop applications for Apache Spark.
+ Integrated Solution: In Spark we can create an integrated solution that combines the power of SQL, Streaming and data analytics.
  R+ un Everywhere: Apache Spark can run on many platforms. It can run on Hadoop, Mesos, in Cloud or standalone. It can also connect to many data sources like HDFS, Cassandra, HBase, S3 etc.
+ Stream Processing: Apache Spark also supports real time stream processing. With real time streaming we can provide real time analytics solutions. This is very useful for real-time data.

[Table of Contents](#Apache-Spark)

## What is a Resilient Distribution Dataset in Apache Spark?
Resilient Distribution Dataset (RDD) is an abstraction of data in Apache Spark. It is a distributed and resilient collection of records spread over many partitions. RDD hides the data partitioning and distribution behind the scenes. Main	features of RDD 	are as follows:
+ Distributed: Data in a RDD is distributed across multiple nodes.
+ Resilient: RDD is a fault- tolerant dataset. In case of node failure, Spark can re- compute data.
+ Dataset: It is a collection of data similar to collections in Scala.
+ Immutable: Data in RDD cannot be modified after creation. But we can transform it using a Transformation.

[Table of Contents](#Apache-Spark)

## What is a Transformation in Apache Spark?
Transformation in Apache Spark is a function that can be applied to a RDD. Output of a Transformation is another RDD. Transformation in Spark is a lazy operation. It means it is not executed immediately. Once we call an action, transformation is executed. A Transformation does not change the input RDD. We can also create a pipeline of certain Transformations to create a Data flow.

[Table of Contents](#Apache-Spark)

## What are security options in Apache Spark?
Apache Spark provides following security options:
Encryption: Apache Spark supports encryption by SSL. We can use HTTPS protocol for secure data transfer. Therefore data is transmitted in encrypted mode. We can use spark.ssl parameters to set the SSL configuration.

Authentication: We can perform authentication by a shared secret in Apache Spark. We can use spark.authenticate	to configure authentication in Spark.
Event Logging: If we use Event Logging, then we can set the permissions on the directory where event logs are	stored.	These permissions can ensure access control for Event log.

[Table of Contents](#Apache-Spark)

## How will you monitor Apache Spark?
We can use the Web UI provided by SparkContext to monitor Spark. We can access this Web UI at port 4040 to get the useful information. Some of the information that we can monitor is:
+ Scheduler tasks and stages RDD	Sizes	and	Memory usage Spark	Environment Information
+ Executors Information
+ Spark also provides a Metrics library. This library can be used to send Spark information to HTTP, JMX, CSV files etc.This is another option to collect Spark runtime information for monitoring another dashboard tool.

[Table of Contents](#Apache-Spark)

## What are the main libraries of Apache Spark?
Main libraries of Apache Spark are as follows:
+ MLib: This is Spark’s Machine Learning library. We can use it to create scalable machine learning system. We can use various machine learning algorithms as well as features like pipelining etc with this library.
+ GraphX: This library is used for computation of Graphs. It helps in creating a Graph abstraction of data and then use various Graph operators like- SubGraph, joinVertices etc.
+ Structured Streaming: This library is used for handling streams in Spark. It is a fault tolerant system built on top of Spark SQL Engine to process streams.
+ Spark SQL: This is another popular component that is used	for	processing	SQL queries on Spark platform.
+ SparkR: This is a package in Spark to use Spark from R language. We can use R data frames, dplyr etc from this package. We can also start SparkR from RStudio.

[Table of Contents](#Apache-Spark)

## What are the main functions of Spark Core in Apache Spark?
Spark Core is the central component of Apache Spark. It serves following functions:
+ Distributed Task Dispatching
+ Job Scheduling
+ I/O Functions

[Table of Contents](#Apache-Spark)

## How will you do memory tuning in Spark?
In case of memory tuning we have to take care of these points.
Amount of memory used by objects Cost of accessing objects Overhead	of Garbage Collection
Apache Spark stores objects in memory for caching. So it becomes important to perform memory tuning in a Spark application. First we determine the memory usage by the application. To do this we first create a RDD and put it in cache. Now we can see the size of the RDD in storage page of Web UI. This will tell the amount of memory consumed by RDD. Based on the memory usage, we can estimate the amount of memory needed for our task. In case we need tuning, we can follow these practices to reduce memory usage:
Use data structures like Array of objects or primitives instead of Linked list or HashMap. Fastutil library provides convenient collection classes for primitive types compatible with Java.
We have to reduce the usage of nested data structures with a large number of small objects and pointes. E.g. Linked list has pointers within each node.
It is a good practice to use numeric IDs instead of Strings for keys.
We can also use JVM flag - XX:+UseCompressedOops to	make pointers be four bytes instead of eight.

[Table of Contents](#Apache-Spark)

## What are the two ways to create RDD in Spark?
We can create RDD in Spark in following two ways:
+ Internal: We can parallelize an existing collection of data within our Spark Driver program and create a RDD out of it.
+ External: We can also create RDD by referencing a Dataset in an external data source like AWS S3, HDFS, HBASE etc.

[Table of Contents](#Apache-Spark)

## What are the main operations that can be done on a RDD in Apache Spark?
There are two main operations that can be performed on a RDD in Spark:
+ Transformation: This is a function that is used to create a new RDD out of an existing RDD.
+ Action: This is a function that returns a value to Driver program after running a computation on RDD.

[Table of Contents](#Apache-Spark)

## What are the common Transformations in Apache Spark?
Some common transformations in Apache Spark are as follows:
+ Map(func): This is a basic transformation that returns a new dataset by passing each element of input dataset through func function.
+ Filter(func):	This transformation returns a new dataset of elements that return true for func function. It is used to filter elements in a dataset based on criteria in func function.
+ Union(other Dataset): This is used to combine a dataset with another dataset to form a union of two datasets.
+ Intersection(other Dataset):	This transformation gives the elements common to two datasets.
+ Pipe(command, [envVars]): This transformation passes each partition of the dataset through a shell command.

[Table of Contents](#Apache-Spark)

## What are the common Actions in Apache Spark?
Some commonly used Actions in Apache Spark are as follows:
+ Reduce(func): This Action aggregates the elements of a dataset by using func function.
+ Count(): This action gives the total number of elements in a Dataset.
+ Collect(): This action will return all the elements of a dataset as an Array to the driver program.
+ First(): This action gives the first element of a collection.
+ Take(n): This action gives the first n elements of dataset.
+ Foreach(func): This action runs each element in dataset through a for loop and executes function func on each element.

[Table of Contents](#Apache-Spark)

## What is a Shuffle operation in Spark?
Shuffle operation is used in Spark to re-distribute data across multiple partitions. It is a costly and complex operation. In general a single task in Spark operates on elements in one partition. To execute shuffle, we have to run an operation on all elements of all partitions. It is also called all-to-all operation.

[Table of Contents](#Apache-Spark)

## What are the operations that can cause a shuffle in Spark?
Some of the common operations that can cause a shuffle internally in Spark are as follows:
+ Repartition
+ Coalesce
+ GroupByKey
+ ReduceByKey
+ Cogroup
+ Join

[Table of Contents](#Apache-Spark)

## What is purpose of Spark SQL?
Spark SQL is used for running SQL queries. We can use Spark SQL to interact with SQL as well as Dataset API in Spark. During execution, Spark SQL uses same computation engine for SQL as well as Dataset API. With Spark SQL we can get more information about the structure of data as well as computation being performed. We can also use Spark SQL to read data from an existing Hive installation. Spark SQL can also be accessed by using JDBC/ODBC API as well as command line.

[Table of Contents](#Apache-Spark)

## What is a DataFrame in Spark SQL?
A DataFrame in SparkSQL is a Dataset organized into names columns. It is conceptually like a table in SQL.In Java and Scala, a DataFrame is a represented by a DataSet of rows. We can create a DataFrame from an existing RDD, a Hive table or from other Spark data sources.

[Table of Contents](#Apache-Spark)

## What is a Parquet file in Spark?
Apache Parquet is a columnar storage format that is available to any project in Hadoop ecosystem. Any data processing framework, data model or programming language can use it. It is a compressed, efficient and encoding format common to Hadoop system projects. Spark SQL supports both reading and writing of parquet files. Parquet files also automatically preserves the schema of the original data. During write operations, by default all columns in a parquet file are converted to nullable column.

[Table of Contents](#Apache-Spark)

## What is the difference between Apache Spark and Apache Hadoop MapReduce?
Some of the main differences between Apache Spark and Hadoop MapReduce are follows:
+ Speed: Apache Spark is 10X to 100X faster than Hadoop due to its usage of in memory processing.
+ Memory: Apache Spark stores data in memory, whereas	Hadoop MapReduce stores data in hard disk.
+ RDD: Spark uses Resilient Distributed Dataset (RDD) that guarantee fault tolerance. Where Apache Hadoop uses replication of data in multiple copies to achieve fault tolerance.
+ Streaming: Apache Spark supports Streaming with very less administration. This makes it much easier to use than Hadoop for real-time stream processing.
+ API: Spark provides a versatile API that can be used with multiple data sources as well as languages. It is more extensible than the API provided by Apache Hadoop.

[Table of Contents](#Apache-Spark)

## What are the main languages supported by Apache Spark?
Some of the main languages supported by Apache Spark are as follows:
+ Java: We can use JavaSparkContext object to work with Java in Spark.
+ Scala: To use Scala with Spark, we have to create SparkContext	object	in Scala.
+ Python: We also used SparkContext to work with Python in Spark.
+ R: We can use SparkR module to work with R language in Spark ecosystem.
+ SQL: We can also SparkSQL to work with SQL language in Spark.

[Table of Contents](#Apache-Spark)

## What are the file systems supported by Spark?
Some of the popular file systems supported by Apache Spark are as follows:
+ HDFS
+ S3
+ Local File System
+ Cassandra
+ OpenStack Swift
+ MapR File System

[Table of Contents](#Apache-Spark)

## What is a Spark Driver?
Spark Driver is a program that runs on the master node machine. It takes care of declaring any operation- Transformation or Action on a RDD. With Spark Driver was can keep track of all the operations on a Dataset. It can also be used to rebuild a RDD in Spark.

[Table of Contents](#Apache-Spark)

## What is an RDD Lineage?
Resilient Distributed Dataset (RDD) Lineage is a graph of all the parent RDD of a RDD. Since Spark does not replicate data, it is possible to lose some data. In case some Dataset is lost, it is possible to use RDD Lineage to recreate the lost Dataset. Therefore RDD Lineage provides solution for better performance of Spark as well as it helps in building a resilient system.

[Table of Contents](#Apache-Spark)

## What are the two main types of Vector in Spark?
There are two main types of Vector in Spark:
Dense Vector: A dense vector is backed by an array of double data type. This array contains the values.
E.g. {1.0 , 0.0, 3.0} Sparse Vector: A sparse vector is backed by two parallel arrays. One array is for indices and the other array is for values. E.g. {3, [0,2], [1.0,3.0]} In this array, the first element is the number of elements in vector. Second element is the array of indices of non-zero values. Third element is the array of non-zero values.

[Table of Contents](#Apache-Spark)

## What are the different deployment modes of Apache Spark?
Some popular deployment modes of Apache Spark are as follows:
+ Amazon EC2: We can use AWS cloud product Elastic Compute Cloud (EC2) to deploy and run a Spark cluster.
+ Mesos: We can deploy a Spark application in a private cluster by using Apache Mesos.
+ YARN: We can also deploy Spark on Apache YARN (Hadoop NextGen)
+ Standalone: This is the mode in which we can start Spark by hand. We can launch standalone cluster manually.

[Table of Contents](#Apache-Spark)

## What is lazy evaluation in Apache Spark?
Apache Spark uses lazy evaluation as a performance optimization technique. In Laze evaluation as transformation is not applied immediately to a RDD. Spark records the transformations that have to be applied to a RDD. Once an Action is called, Spark executes all the transformations. Since Spark does not perform immediate execution based on transformation, it is	called lazy evaluation.

## What are the core components of a distributed application in Apache Spark?
Core components of a distributed application in Apache Spark are as follows:
+ Cluster Manager: This is the component responsible for launching executors and drivers on multiple nodes. We can use different types of cluster managers based on our requirements. Some of the common types are Standalone, YARN, Mesos etc.
+ Driver: This is the main program in Spark that runs the main() function of an application. A Driver program creates the SparkConetxt.	Driver program listens and accepts incoming connections from its executors. Driver program can schedule tasks on the cluster. It runs closer to worker nodes.
+ Executor: This is a process on worker node. It is launched on the node to run an application. It can run tasks and use data in memory or disk storage to perform the task.

[Table of Contents](#Apache-Spark)

## What is the difference in cache() and persist() methods in Apache Spark?
Both cache() and persist() functions are used for persisting a RDD in memory across operations. The key difference between persist() and cache() is that in persist() we can specify the Storage level that we select for persisting. Where as in cache(), default strategy is used for persisting. The default storage strategy is MEMORY_ONLY.

[Table of Contents](#Apache-Spark)

## How will you remove data from cache in Apache Spark?
In general, Apache Spark automatically removes the unused objects from cache. It uses Least Recently Used (LRU) algorithm to drop old partitions. There are automatic monitoring mechanisms in Spark to monitor cache usage on each node. In case   we   want   to   forcibly remove an object from cache in Apache Spark, we can use RDD.unpersist() method.

[Table of Contents](#Apache-Spark)

## What is the use of SparkContext in Apache Spark?
SparkContext is the central object in Spark that coordinates different Spark applications in a cluster. In a cluster we can use SparkContext to connect to multiple Cluster Managers that allocate resources to multiple applications. For any Spark program we first create SparkContext object. We can access a cluster by using this object. To create a SparkContext object, we first create a SparkConf object. This object contains the configuration information of our application. In Spark Shell, by default we get a SparkContext for the shell.

[Table of Contents](#Apache-Spark)

## Do we need HDFS for running Spark application?
This is a trick question. Spark supports multiple file-systems. Spark supports HDFS, HBase, local file system, S3, Cassandra etc. So HDFS is not the only file system for running Spark application.

[Table of Contents](#Apache-Spark)

## What is Spark Streaming?
Spark Streaming is a very popular feature of Spark for processing live streams with a large amount of data. Spark Streaming uses Spark API to create a highly scalable, high throughput and fault tolerant system to handle live data streams. Spark Streaming supports ingestion of data from popular sources like- Kafka, Kinesis, Flume etc. We can apply popular functions like map, reduce, join etc on data processed through Spark Streams. The processed data can be written to a file system or sent to databases and live dashboards.

[Table of Contents](#Apache-Spark)

## How does Spark Streaming work internally?
Spark Streams listen to live data streams from various sources. On receiving data, it is divided into small batches that can be handled by Spark engine. These small batches of data are processed by Spark Engine to generate another output stream of resultant data. Internally, Spark uses an abstraction called DStream or discretized stream. A DStream is a continuous stream of data. We can create DStream from Kafka, Flume, Kinesis etc. A DStream is nothing but a sequence of RDDs in Spark. We can apply transformations and actions on this sequence of RDDs to create further RDDs.

[Table of Contents](#Apache-Spark)

## What is a Pipeline in Apache Spark?
Pipeline is a concept from Machine learning. It is a sequence of algorithms that are executed for processing and learning from data. Pipeline is similar to a workflow. There can be one or more stages in a Pipeline.

[Table of Contents](#Apache-Spark)

## How does Pipeline work in Apache Spark?
A Pipeline is a sequence of stages. Each stage in Pipeline can be a Transformer or an Estimator. We run these stages in an order. Initially a DataFrame is passed as an input to Pipeline. This DataFrame keeps on transforming with each stage of Pipeline. Most of the time, Runtime checking is done on DataFrame passing through the Pipeline. We can also save a Pipeline to a disk. It can be re-read from disk a later point of time.

[Table of Contents](#Apache-Spark)

## What is the difference between Transformer and Estimator in Apache Spark?
A Transformer is an abstraction for feature transformer and learned model. A Transformer implements transform() method. It converts one DataFrame to another DataFrame. It appends one or more columns to a DataFrame. In a feature transformer a DataFrame is the input and the output is a new DataFrame with a new mapped column. An Estimator is an abstraction for a learning algorithm that fits or trains on data. An Estimator implements fit() method. The fit() method takes a DataFrame as input and results in a Model.

[Table of Contents](#Apache-Spark)

## What are the different types of Cluster Managers in Apache Spark?
Main types of Cluster Managers for Apache Spark are as follows:
+ Standalone: It is a simple cluster manager that is included with Spark. We can start Spark manually by hand in this mode.
+ Spark	on Mesos: In this mode, Mesos master replaces Spark master as the cluster manager. When driver creates a job, Mesos will determine which machine will handle the task.
+ Hadoop YARN: In this setup, Hadoop YARN is used in cluster. There are two modes in this setup. In cluster mode, Spark driver runs inside a master process managed by YARN on cluster. In client mode, the Spark driver runs in the client process and application master is used for requesting resources from YARN.

[Table of Contents](#Apache-Spark)

## How will you minimize data transfer while working with Apache Spark?
Generally Shuffle operation in Spark leads to a large amount of data transfer. We can configure Spark Shuffle process for optimum data transfer. Some of the main points are as follows:
+ spark.shuffle.compress: This configuration can be set to true to compress map output files. This reduces the amount of data transfer due to compression.
+ ByKey operations: We can minimize the use of ByKey operations to minimize the shuffle calls.

[Table of Contents](#Apache-Spark)

## What is the main use of MLib in Apache Spark?
MLib is a machine-learning library in Apache Spark. Some of the main uses of MLib in Spark are as follows:
+ ML Algorithms: It contains Machine Learning algorithms such as classification, regression, clustering, and collaborative filtering. Featurization:
+ MLib provides algorithms to work with features. Some of these are	feature	extraction, transformation, dimensionality		reduction, and selection.
+ Pipelines: It contains tools for constructing, evaluating, and tuning ML Pipelines.
+ Persistence: It also provides methods for saving and load algorithms, models, and Pipelines.
+ Utilities: It contains utilities for linear algebra, statistics, data handling, etc.

[Table of Contents](#Apache-Spark)

## What is the Checkpointing in Apache Spark?
In Spark Streaming, there is a concept of Checkpointing to add resiliency in the application. In case of a failure, a streaming application needs a checkpoint to recover. Due to this Spark provides Checkpointing. There are two types of Checkpointing:
+ Metadata Checkpointing: Metadata is the configuration information and other information that defines a Streaming application. We can create a Metadata checkpoint for a node to recover from the failure while running the driver application.		Metadata includes	configuration, DStream operations and incomplete batches etc.
+ Data Checkpointing: In this checkpoint we save RDD to a reliable storage. This is useful	in stateful transformations where generated RDD depends on RDD   of   previous   batch. There can be a long chain of RDDs in some cases. To avoid such a large recovery time, it is easier to create Data Checkpoint with RDDs at intermediate steps.

[Table of Contents](#Apache-Spark)

## What is an Accumulator in Apache Spark?
An Accumulator is a variable in Spark that can be added only through an associative and commutative operation. An Accumulator can be supported in parallel. It is generally used to implement a counter or cumulative sum. We can create numeric type Accumulators by default in Spark.An Accumulator variable can be named as well as unnamed.

[Table of Contents](#Apache-Spark)

## What is a Broadcast variable in Apache Spark?
As per Spark online documentation, “A Broadcast variable allows a programmer to keep a read-only variable cached on each machine rather than shipping a copy of it with tasks.” Spark can also distribute broadcast variable with an efficient broadcast algorithm to reduce communication cost. In Shuffle operations, there is a need of common data. This common data is broadcast by Spark as a Broadcast variable. The data in these variables is serialized and de-serialized before running a task.
We can	use SparkContext.broadcast(v) to create a broadcast variable. It is recommended that we should use broadcast variable in place of original variable for running a function on cluster.

[Table of Contents](#Apache-Spark)

## What is Structured Streaming in Apache Spark?
Structured Streaming is a new feature in Spark 2.1. It is a scalable and fault-tolerant stream- processing engine. It is built on Spark SQL engine. We can use Dataset or DataFrame API to express streaming aggregations, event-time windows etc. The computations are done on the optimized Spark SQL engine.

[Table of Contents](#Apache-Spark)

## How will you pass functions to Apache Spark?
In Spark API, we pass functions to driver program so that it can be run on a cluster. Two common ways to pass functions in Spark are as follows:
+ Anonymous	Function Syntax: This is used for passing short pieces of code in an anonymous function.
+ Static	Methods in a Singleton object: We can also define static methods in an object with only once instance i.e. Singleton. This object along with its methods can be passed to cluster nodes.

[Table of Contents](#Apache-Spark)

## What is a Property Graph?
A Property Graph is a directed multigraph. We can attach an object on each vertex and edge of a Property Graph.In a directed multigraph, we can have multiple parallel edges that share same source and destination vertex. During modeling the data, the option of parallel edges helps in creating multiple relationships between same pair of vertices. E.g. Two persons can have two relationships Boss as well as Mentor.

[Table of Contents](#Apache-Spark)

## What is Neighborhood Aggregation in Spark?
Neighborhood Aggregation is a concept in Graph module of Spark. It refers to the task of aggregating information	about	the neighborhood of each vertex. E.g. We want to know the number of books referenced in a book. Or number of times a Tweet is retweeted. This concept is used in iterative graph algorithms. Some of the popular uses of this concept are in Page Rank, Shortest Path etc.
We can use aggregateMessages[] and mergeMsg[] operations in Spark for implementing Neighborhood Aggregation.

[Table of Contents](#Apache-Spark)

## What are different Persistence levels in Apache Spark?
Different Persistence levels in Apache Spark are as follows:
+ MEMORY_ONLY: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be recomputed.
+ MEMORY_AND_DISK: In this level, RDD object is stored as a de-serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
+ MEMORY_ONLY_SER: In this level, RDD object is stored as a serialized Java object in JVM. It is more efficient than de-serialized object.
+ MEMORY_AND_DISK_SE In this level, RDD object is stored as a serialized Java object in JVM. If an RDD doesn’t fit in the memory, it will be stored on the Disk.
+ DISK_ONLY: In this level, RDD object is stored only on Disk.

[Table of Contents](#Apache-Spark)

## How will you select the storage level in Apache Spark?
We use storage level to maintain balance between CPU efficiency and Memory usage. If our RDD objects fit in memory, we use MEMORY_ONLY option. In this option, the performance is very good due to objects being in Memory only. In case our RDD objects cannot fit in memory, we go for MEMORY_ONLY_SER option and select a serialization library that can provide space savings with serialization. This option is also quite fast in performance. In case our RDD object cannot fit in memory with a big gap in memory vs. total object size, we go for MEMORY_AND_DISK option. In this option some RDD object are stored on Disk. For fast fault recovery we use replication of objects to multiple partitions.

[Table of Contents](#Apache-Spark)

## What are the options in Spark to create a Graph?
We can create a Graph in Spark from a collection of vertices and edges. Some of the options in Spark to create a Graph are as follows:
+ Graph.apply: This is the simplest option to create graph. We use this option to create a graph from RDDs of vertices and edges.
+ Graph.fromEdges: We can also create a graph from RDD of edges. In this option, vertices are created automatically and a default value is assigned to each vertex.
+ Graph.fromEdgeTuples: We can also create a graph from only an RDD of tuples.

[Table of Contents](#Apache-Spark)

## What are the basic Graph operators in Spark?
Some common Graph operators in Apache Spark are as follows:
+ numEdges
+ numVertices
+ inDegrees
+ outDegrees
+ degrees
+ vertices
+ edges
+ persist
+ cache
+ unpersistVertices
+ partitionBy

[Table of Contents](#Apache-Spark)

## What is the partitioning approach used in GraphX of Apache Spark?
GraphX uses Vertex-cut approach to distributed graph partitioning. In this approach, a graph is not split along edges. Rather we partition graph along vertices. These vertices can span on multiple machines. This approach reduces communication and storage overheads. Edges are assigned to different partitions based on the partition strategy that we select.

[Table of Contents](#Apache-Spark)

## What is RDD?
RDD (Resilient Distribution Datasets) is a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed.

[Table of Contents](#Apache-Spark)

## Name the different types of RDD
There are primarily two types of RDD – parallelized collection and Hadoop datasets.

[Table of Contents](#Apache-Spark)

## What are the methods of creating RDDs in Spark?
There are two methods :
+ By paralleling a collection in your Driver program.
+ By loading an external dataset from external storage like HDFS, HBase, shared file system.

[Table of Contents](#Apache-Spark)

## What is a Sparse Vector?
A sparse vector has two parallel arrays –one for indices and the other for values.

[Table of Contents](#Apache-Spark)

## What are the languages supported by Apache Spark and which is the most popular one, What is JDBC and why it is popular?
There are four languages supported by Apache Spark – Scala, Java, Python, and R. Scala is the most popular one.
**Java Database Connectivity (JDBC)** is an application programming interface (API) that defines database connections in Java environments. Spark is written in Scala, which runs on the Java Virtual Machine (JVM). This makes JDBC the preferred method for connecting to data whenever possible. Hadoop, Hive, and MySQL all run on Java and easily interface with Spark clusters.
Databases are advanced technologies that benefit from decades of research and development. To leverage the inherent efficiencies of database engines, Spark uses an optimization called predicate pushdown. Predicate pushdown uses the database itself to handle certain parts of a query (the predicates). In mathematics and functional programming, a predicate is anything that returns a Boolean. In SQL terms, this often refers to the WHERE clause. Since the database is filtering data before it arrives on the Spark cluster, there less data transfer across the network and fewer records for Spark to process. Spark's Catalyst Optimizer includes predicate pushdown communicated through the JDBC API, making JDBC an ideal data source for Spark workloads.

[Table of Contents](#Apache-Spark)

## What is Yarn?
Yarn is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster.

[Table of Contents](#Apache-Spark)

## Do you need to install Spark on all nodes of Yarn cluster? Why?
No, because Spark runs on top of Yarn.

[Table of Contents](#Apache-Spark)

## Is it possible to run Apache Spark on Apache Mesos?
Yes.

[Table of Contents](#Apache-Spark)

## What is lineage graph?
The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph.

[Table of Contents](#Apache-Spark)

## Define Partitions in Apache Spark
Partition is a smaller and logical division of data similar to split in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process.

[Table of Contents](#Apache-Spark)

## What is a DStream?
Discretized Stream (DStream) is a sequence of Resilient Distributed Databases that represent a stream of data.

[Table of Contents](#Apache-Spark)

## What is a Catalyst framework?
Catalyst framework is an optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.

[Table of Contents](#Apache-Spark)

## What are Actions in Spark?
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations.

[Table of Contents](#Apache-Spark)

## What is a Parquet file?
Parquet is a columnar format file supported by many other data processing systems.

[Table of Contents](#Apache-Spark)

## What is GraphX?
Spark uses GraphX for graph processing to build and transform interactive graphs.

[Table of Contents](#Apache-Spark)

## What file systems does Spark support?
Hadoop distributed file system (HDFS), local file system, and Amazon S3.

[Table of Contents](#Apache-Spark)

## What are the different types of transformations on DStreams? Explain.
+ Stateless Transformations – Processing of the batch does not depend on the output of the previous batch. Examples – map (), reduceByKey (), filter ().
+ Stateful Transformations – Processing of the batch depends on the intermediary results of the previous batch. Examples –Transformations that depend on sliding windows.

[Table of Contents](#Apache-Spark)

## What is the difference between persist () and cache ()?
Persist () allows the user to specify the storage level whereas cache () uses the default storage level.

[Table of Contents](#Apache-Spark)

## What do you understand by SchemaRDD?
SchemaRDD is an RDD that consists of row objects (wrappers around the basic string or integer arrays) with schema information about the type of data in each column.
These are some popular questions asked in an Apache Spark interview. Always be prepared to answer all types of questions — technical skills, interpersonal, leadership or methodology. If you are someone who has recently started your career in big data, you can always get certified in Apache Spark to get the techniques and skills required to be an expert in the field.

[Table of Contents](#Apache-Spark)

## What is Apache Spark?
Spark is a fast, easy-to-use and flexible data processing framework. It has an advanced execution engine supporting cyclic data  flow and in-memory computing. Spark can run on Hadoop, standalone or in the cloud and is capable of accessing diverse data sources including HDFS, HBase, Cassandra and others.

[Table of Contents](#Apache-Spark)

## Explain key features of Spark.
Allows Integration with Hadoop and files included in HDFS.
Spark has an interactive language shell as it has an independent Scala (the language in which Spark is written) interpreter.
Spark consists of RDD’s (Resilient Distributed Datasets), which can be cached across computing nodes in a cluster.
Spark supports multiple analytic tools that are used for interactive query analysis , real-time analysis and graph      processing

[Table of Contents](#Apache-Spark)

## Define RDD?
RDD is the acronym for Resilient Distribution Datasets – a fault-tolerant collection of operational elements that run parallel. The partitioned data in RDD is immutable and distributed. There are primarily two types of RDD:
+ Parallelized Collections : The existing RDD’s running parallel with one another.
+ Hadoop datasets : perform function on each file record in HDFS or other storage system

[Table of Contents](#Apache-Spark)

## What does a Spark Engine do?
Spark Engine is responsible for scheduling, distributing and monitoring the data application across the cluster.

[Table of Contents](#Apache-Spark)

## Define Partitions?
As the name suggests, partition is a smaller and logical division of data  similar to split in MapReduce. Partitioning is the process to derive logical units of data to speed up the processing process. Everything in Spark is a partitioned RDD.

[Table of Contents](#Apache-Spark)

## What do you understand by Transformations in Spark?
Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filer() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements form current RDD that pass function argument.

[Table of Contents](#Apache-Spark)

## Define Actions.
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to local node.

[Table of Contents](#Apache-Spark)

## Define functions of SparkCore?
Serving as the base engine, SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems.

[Table of Contents](#Apache-Spark)

## What is RDD Lineage?
Spark does not support data replication in the memory and thus, if any data is lost, it is rebuild using RDD lineage. RDD lineage is a process that reconstructs lost data partitions. The best is that RDD always remembers how to build from other datasets.

[Table of Contents](#Apache-Spark)

## What is Spark Driver?
Spark Driver is the program that runs on the master node of the machine and declares transformations and actions on data RDDs. In simple terms, driver in Spark creates SparkContext, connected to a given Spark Master.
The driver also delivers the RDD graphs to Master, where the standalone cluster manager runs.

[Table of Contents](#Apache-Spark)

## What is Hive on Spark?
Hive contains significant support for Apache Spark, wherein Hive execution is configured to Spark:
hive> set spark.home=/location/to/sparkHome;
hive> set hive.execution.engine=spark;

Name commonly-used Spark Ecosystems.
+ Spark SQL (Shark)- for developers.
+ Spark Streaming for processing live data streams.
+ GraphX for generating and computing graphs.
+ MLlib (Machine Learning Algorithms).
+ SparkR to promote R Programming in Spark engine.

[Table of Contents](#Apache-Spark)

## Define Spark Streaming.
Spark supports stream processing – an extension to the Spark API , allowing stream processing of live data streams. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

[Table of Contents](#Apache-Spark)

## What is Spark SQL?
SQL Spark, better known as Shark is a novel module introduced in Spark to work with structured data and perform structured data processing. Through this module, Spark executes relational SQL queries on the data. The core of the component supports an altogether different RDD called SchemaRDD, composed of rows objects and schema objects defining data type of each column in the row. It is similar to a table in relational database.

[Table of Contents](#Apache-Spark)

## List the functions of Spark SQL?
Spark SQL is capable of:
+ Loading data from a variety of structured sources.
+ Querying data using SQL statements, both inside a Spark program and from external tools that connect to Spark SQL through standard database connectors (JDBC/ODBC). For instance, using business intelligence tools like Tableau.
+ Providing rich integration between SQL and regular Python/Java/Scala code, including the ability to join RDDs and SQL tables, expose custom functions in SQL, and more.

[Table of Contents](#Apache-Spark)

## What are benefits of Spark over MapReduce?
Due to the availability of in-memory processing, Spark implements the processing around 10-100x faster than Hadoop MapReduce. MapReduce makes use of persistence storage for any of the data processing tasks.
Unlike Hadoop, Spark provides in-built libraries to perform multiple tasks form the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.

[Table of Contents](#Apache-Spark)

## What is Spark Executor?
When SparkContext connect to a cluster manager, it acquires an Executor on nodes in the cluster. Executors are Spark processes that run computations and store the data on the worker node. The final tasks by SparkContext are transferred to executors for their execution.

[Table of Contents](#Apache-Spark)

## What do you understand by worker node?
Worker node refers to any node that can run the application code in a cluster.

[Table of Contents](#Apache-Spark)

## Illustrate some demerits of using Spark.
Since Spark utilizes more storage space compared to Hadoop and MapReduce, there may arise certain problems. Developers need to be careful while running their applications in Spark. Instead of running everything on a single node, the work must be distributed over multiple clusters.

[Table of Contents](#Apache-Spark)

## What is the advantage of a Parquet file?
Parquet file is a columnar format file that helps :
+ Limit I/O operations
+ Consumes less space
+ Fetches only required columns.

[Table of Contents](#Apache-Spark)

## What are different o/p methods to get result?
+ collect()
+ show()
+ take()
+ foreach(println)

[Table of Contents](#Apache-Spark)

## What are two ways to attain a schema from data?
Allow Spark to infer a schema from your data or provide a user defined schema. Schema inference is the recommended first step; however, you can customize this schema to your use case with a user defined schema.

Providing a schema increases performance two to three times, depending on the size of the cluster used. Since Spark doesn't infer the schema, it doesn't have to read through all of the data. This is also why  there are fewer jobs when a schema is provided: Spark doesn't need one job for each partition of the data to infer the schema.

[Table of Contents](#Apache-Spark)

## Why should you define your own schema?
Benefits of user defined schemas include:
-   Avoiding the extra scan of your data needed to infer the schema
-   Providing alternative data types
-   Parsing only the fields you need

[Table of Contents](#Apache-Spark)

## Why is JSON a common format in big data pipelines?
Semi-structured data works well with hierarchical data and where schemas need to evolve over time. It also easily contains composite data types such as arrays and maps.

[Table of Contents](#Apache-Spark)

## By default, how are corrupt records dealt with using  spark.read.json()?
They appear in a column called  _corrupt_record. These are the records that Spark can't read (e.g. when characters are missing from a JSON string).

[Table of Contents](#Apache-Spark)

## Explain the key features of Apache Spark.
+ Polyglot: Spark provides high-level APIs in Java, Scala, Python and R. Spark code can be written in any of these four languages. It provides a shell in Scala and Python. The Scala shell can be accessed through ./bin/spark-shell and Python shell through ./bin/pyspark from the installed directory.
+ Speed: Spark runs upto 100 times faster than Hadoop MapReduce for large-scale data processing. Spark is able to achieve this speed through controlled partitioning. It manages data using partitions that help parallelize distributed data processing with minimal network traffic.
+ Multiple Formats: Spark supports multiple data sources such as Parquet, JSON, Hive and Cassandra. The Data Sources API provides a pluggable mechanism for accessing structured data though Spark SQL. Data sources can be more than just simple pipes that convert data and pull it into Spark.
+ Lazy Evaluation: Apache Spark delays its evaluation till it is absolutely necessary. This is one of the key factors contributing to its speed. For transformations, Spark adds them to a DAG of computation and only when the driver requests some data, does this DAG actually gets executed.
+ Real Time Computation: Spark’s computation is real-time and has less latency because of its in-memory computation. Spark is designed for massive scalability and the Spark team has documented users of the system running production clusters with thousands of nodes and supports several computational models.
+ Hadoop Integration: Apache Spark provides smooth compatibility with Hadoop. This is a great boon for all the Big Data engineers who started their careers with Hadoop. Spark is a potential replacement for the MapReduce functions of Hadoop, while Spark has the ability to run on top of an existing Hadoop cluster using YARN for resource scheduling.
+ Machine Learning: Spark’s MLlib is the machine learning component which is handy when it comes to big data processing. It eradicates the need to use multiple tools, one for processing and one for machine learning. Spark provides data engineers and data scientists with a powerful, unified engine that is both fast and easy to use.

[Table of Contents](#Apache-Spark)

## What are benefits of Spark over MapReduce?
Spark has the following benefits over MapReduce:
Due to the availability of in-memory processing, Spark implements the processing around 10 to 100 times faster than Hadoop MapReduce whereas MapReduce makes use of persistence storage for any of the data processing tasks.
Unlike Hadoop, Spark provides inbuilt libraries to perform multiple tasks from the same core like batch processing, Steaming, Machine learning, Interactive SQL queries. However, Hadoop only supports batch processing.
Hadoop is highly disk-dependent whereas Spark promotes caching and in-memory data storage.
Spark is capable of performing computations multiple times on the same dataset. This is called iterative computation while there is no iterative computing implemented by Hadoop.

[Table of Contents](#Apache-Spark)

## What is YARN?
Similar to Hadoop, YARN is one of the key features in Spark, providing a central and resource management platform to deliver scalable operations across the cluster. YARN is a distributed container manager, like Mesos for example, whereas Spark is a data processing tool. Spark can run on YARN, the same way Hadoop Map Reduce can run on YARN. Running Spark on YARN necessitates a binary distribution of Spark as built on YARN support.

[Table of Contents](#Apache-Spark)

## Do you need to install Spark on all nodes of YARN cluster?
No, because Spark runs on top of YARN. Spark runs independently from its installation. Spark has some options to use YARN when dispatching jobs to the cluster, rather than its own built-in manager, or Mesos. Further, there are some configurations to run YARN. They include master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

[Table of Contents](#Apache-Spark)

## Is there any benefit of learning MapReduce if Spark is better than MapReduce?
Yes, MapReduce is a paradigm used by many big data tools including Spark as well. It is extremely relevant to use MapReduce when the data grows bigger and bigger. Most tools like Pig and Hive convert their queries into MapReduce phases to optimize them better.

[Table of Contents](#Apache-Spark)

## Explain the concept of Resilient Distributed Dataset (RDD).
RDD stands for Resilient Distribution Datasets. An RDD is a fault-tolerant collection of operational elements that run in parallel. The partitioned data in RDD is immutable and distributed in nature. There are primarily two types of RDD:
+ Parallelized Collections: Here, the existing RDDs running parallel with one another.
+ Hadoop Datasets: They perform functions on each file record in HDFS or other storage systems.
+ RDDs are basically parts of data that are stored in the memory distributed across many nodes. RDDs are lazily evaluated in Spark. This lazy evaluation is what contributes to Spark’s speed.

[Table of Contents](#Apache-Spark)

## How do we create RDDs in Spark?
Spark provides two methods to create RDD:
1. By parallelizing a collection in your Driver program.
2. This makes use of SparkContext’s parallelize
3. By loading an external dataset from external storage like HDFS, HBase, shared file system.

[Table of Contents](#Apache-Spark)

## What is Executor Memory in a Spark application?
Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag. Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

[Table of Contents](#Apache-Spark)

## Define Partitions in Apache Spark.
As the name suggests, partition is a smaller and logical division of data similar to split in MapReduce. It is a logical chunk of a large distributed data set. Partitioning is the process to derive logical units of data to speed up the processing process. Spark manages data using partitions that help parallelize distributed data processing with minimal network traffic for sending data between executors. By default, Spark tries to read data into an RDD from the nodes that are close to it. Since Spark usually accesses distributed partitioned data, to optimize transformation operations it creates partitions to hold the data chunks. Everything in Spark is a partitioned RDD.

[Table of Contents](#Apache-Spark)

## What operations does RDD support?
RDD (Resilient Distributed Dataset) is main logical data unit in Spark. An RDD has distributed a collection of objects. Distributed means, each RDD is divided into multiple partitions. Each of these partitions can reside in memory or stored on the disk of different machines in a cluster. RDDs are immutable (Read Only) data structure. You can’t change original RDD, but you can always transform it into different RDD with all changes you want.
RDDs support two types of operations: transformations and actions.
Transformations: Transformations create new RDD from existing RDD like map, reduceByKey and filter we just saw. Transformations are executed on demand. That means they are computed lazily.
Actions: Actions return final results of RDD computations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.

[Table of Contents](#Apache-Spark)

## What do you understand by Transformations in Spark?
Transformations are functions applied on RDD, resulting into another RDD. It does not execute until an action occurs. map() and filter() are examples of transformations, where the former applies the function passed to it on each element of RDD and results into another RDD. The filter() creates a new RDD by selecting elements from current RDD that pass function argument.
val rawData=sc.textFile("path to/movies.txt")
val moviesData=rawData.map(x=>x.split("  "))
As we can see here, rawData RDD is transformed into moviesData RDD. Transformations are lazily evaluated.

[Table of Contents](#Apache-Spark)

## Define Actions in Spark.
An action helps in bringing back the data from RDD to the local machine. An action’s execution is the result of all previously created transformations. Actions triggers execution using lineage graph to load the data into original RDD, carry out all intermediate transformations and return final results to Driver program or write it out to file system.
reduce() is an action that implements the function passed again and again until one value if left. take() action takes all the values from RDD to a local node.
moviesData.saveAsTextFile(“MoviesData.txt”)
As we can see here, moviesData RDD is saved into a text file called MoviesData.txt.

[Table of Contents](#Apache-Spark)

## Define functions of SparkCore.
Spark Core is the base engine for large-scale parallel and distributed data processing. The core is the distributed execution engine and the Java, Scala, and Python APIs offer a platform for distributed ETL application development. SparkCore performs various important functions like memory management, monitoring jobs, fault-tolerance, job scheduling and interaction with storage systems. Further, additional libraries, built atop the core allow diverse workloads for streaming, SQL, and machine learning. It is responsible for:

[Table of Contents](#Apache-Spark)

## Memory management and fault recovery
Scheduling, distributing and monitoring jobs on a cluster Interacting with storage systems

[Table of Contents](#Apache-Spark)

## What do you understand by Pair RDD?
Apache defines PairRDD functions class as class PairRDDFunctions[K, V] extends Logging with HadoopMapReduceUtil with Serializable
Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey() method that collects data based on each key and a join() method that combines different RDDs together, based on the elements having the same key.

[Table of Contents](#Apache-Spark)

## How is Streaming implemented in Spark? Explain with examples.
Spark Streaming is used for processing real-time streaming data. Thus it is a useful addition to the core Spark API. It enables high-throughput and fault-tolerant stream processing of live data streams. The fundamental stream unit is DStream which is basically a series of RDDs (Resilient Distributed Datasets) to process the real-time data. The data from different sources like Flume, HDFS is streamed and finally processed to file systems, live dashboards and databases. It is similar to batch processing as the input data is divided into streams like batches.

[Table of Contents](#Apache-Spark)

## Is there an API for implementing graphs in Spark?
GraphX is the Spark API for graphs and graph-parallel computation. Thus, it extends the Spark RDD with a Resilient Distributed Property Graph.
The property graph is a directed multi-graph which can have multiple edges in parallel. Every edge and vertex have user defined properties associated with it. Here, the parallel edges allow multiple relationships between the same vertices. At a high-level, GraphX extends the Spark RDD abstraction by introducing the Resilient Distributed Property Graph: a directed multigraph with properties attached to each vertex and edge.
To support graph computation, GraphX exposes a set of fundamental operators (e.g., subgraph, joinVertices, and mapReduceTriplets) as well as an optimized variant of the Pregel API. In addition, GraphX includes a growing collection of graph algorithms and builders to simplify graph analytics tasks.

[Table of Contents](#Apache-Spark)

## What is PageRank in GraphX?
PageRank measures the importance of each vertex in a graph, assuming an edge from u to v represents an endorsement of v’s importance by u. For example, if a Twitter user is followed by many others, the user will be ranked highly.
GraphX comes with static and dynamic implementations of PageRank as methods on the PageRank Object. Static PageRank runs for a fixed number of iterations, while dynamic PageRank runs until the ranks converge (i.e., stop changing by more than a specified tolerance). GraphOps allows calling these algorithms directly as methods on Graph.

[Table of Contents](#Apache-Spark)

## How is machine learning implemented in Spark?
MLlib is scalable machine learning library provided by Spark. It aims at making machine learning easy and scalable with common learning algorithms and use cases like clustering, regression filtering, dimensional reduction, and alike.

[Table of Contents](#Apache-Spark)

## Is there a module to implement SQL in Spark? How does it work?
Spark SQL is a new module in Spark which integrates relational processing with Spark’s functional programming API. It supports querying data either via SQL or via the Hive Query Language. For those of you familiar with RDBMS, Spark SQL will be an easy transition from your earlier tools where you can extend the boundaries of traditional relational data processing.
Spark SQL integrates relational processing with Spark’s functional programming. Further, it provides support for various data sources and makes it possible to weave SQL queries with code transformations thus resulting in a very powerful tool.
The following are the four libraries of Spark SQL.
+ Data Source API
+ DataFrame API
+ Interpreter & Optimizer
+ SQL Service

[Table of Contents](#Apache-Spark)

## What are receivers in Apache Spark Streaming?
Receivers are those entities that consume data from different data sources and then move them to Spark for processing. They are created by using streaming contexts in the form of long-running tasks that are scheduled for operating in a round-robin fashion. Each receiver is configured to use up only a single core. The receivers are made to run on various executors to accomplish the task of data streaming. There are two types of receivers depending on how the data is sent to Spark:
+ Reliable receivers: Here, the receiver sends an acknowledegment to the data sources post successful reception of data and its replication on the Spark storage space.
+ Unreliable receiver: Here, there is no acknowledgement sent to the data sources.

+ What is the difference between repartition and coalesce?
+ Repartition
    + Usage repartition can increase/decrease the number of data partitions.
    + Repartition creates new data partitions and performs a full shuffle of evenly distributed data.
    + Repartition internally calls coalesce with shuffle parameter thereby making it slower than coalesce.

+ Coalesce
    + Spark coalesce can only reduce the number of data partitions.
    + Coalesce makes use of already existing partitions to reduce the amount of shuffled data unevenly.
    + Coalesce is faster than repartition. However, if there are unequal-sized data partitions, the speed might be slightly slower.
+ What are the data formats supported by Spark?
  Spark supports both the raw files and the structured file formats for efficient reading and processing. File formats like paraquet, JSON, XML, CSV, RC, Avro, TSV, etc are supported by Spark.

[Table of Contents](#Apache-Spark)

## What do you understand by Shuffling in Spark?
The process of redistribution of data across different partitions which might or might not cause data movement across the JVM processes or the executors on the separate machines is known as shuffling/repartitioning. Partition is nothing but a smaller logical division of data.
It is to be noted that Spark has no control over what partition the data gets distributed across.

[Table of Contents](#Apache-Spark)

## How is Apache Spark different from MapReduce?
+ MapReduce
    + MapReduce does only batch-wise processing of data.
    + MapReduce does slow processing of large data.
    + MapReduce stores data in HDFS (Hadoop Distributed File System) which makes it take a long time to get the data.
    + MapReduce highly depends on disk which makes it to be a high latency framework.
    + MapReduce requires an external scheduler for jobs.

+ Apache Spark
    + Apache Spark can process the data both in real-time and in batches.
    + Apache Spark runs approximately 100 times faster than MapReduce for big data processing.
    + Spark stores data in memory (RAM) which makes it easier and faster to retrieve data when needed.
    + Spark supports in-memory data storage and caching and makes it a low latency computation framework.
    + Spark has its own job scheduler due to the in-memory data computation.

[Table of Contents](#Apache-Spark)

## Explain the working of Spark with the help of its architecture.
Spark applications are run in the form of independent processes that are well coordinated by the Driver program by means of a SparkSession object. The cluster manager or the resource manager entity of Spark assigns the tasks of running the Spark jobs to the worker nodes as per one task per partition principle. There are various iterations algorithms that are repeatedly applied to the data to cache the datasets across various iterations. Every task applies its unit of operations to the dataset within its partition and results in the new partitioned dataset. These results are sent back to the main driver application for further processing or to store the data on the disk. The following diagram illustrates this working as described above:

[Table of Contents](#Apache-Spark)

## What is the working of DAG in Spark?
DAG stands for Direct Acyclic Graph which has a set of finite vertices and edges. The vertices represent RDDs and the edges represent the operations to be performed on RDDs sequentially. The DAG created is submitted to the DAG Scheduler which splits the graphs into stages of tasks based on the transformations applied to the data. The stage view has the details of the RDDs of that stage.
The working of DAG in spark is defined as per the workflow diagram below:
The first task is to interpret the code with the help of an interpreter. If you use the Scala code, then the Scala interpreter interprets the code.
Spark then creates an operator graph when the code is entered in the Spark console.
When the action is called on Spark RDD, the operator graph is submitted to the DAG Scheduler.
The operators are divided into stages of task by the DAG Scheduler. The stage consists of detailed step-by-step operation on the input data. The operators are then pipelined together.
The stages are then passed to the Task Scheduler which launches the task via the cluster manager to work on independently without the dependencies between the stages.
The worker nodes then execute the task.
Each RDD keeps track of the pointer to one/more parent RDD along with its relationship with the parent. For example, consider the operation val childB=parentA.map() on RDD, then we have the RDD childB that keeps track of its parentA which is called RDD lineage.

[Table of Contents](#Apache-Spark)

## Under what scenarios do you use Client and Cluster modes for deployment?
In case the client machines are not close to the cluster, then the Cluster mode should be used for deployment. This is done to avoid the network latency caused while communication between the executors which would occur in the Client mode. Also, in Client mode, the entire process is lost if the machine goes offline.
If we have the client machine inside the cluster, then the Client mode can be used for deployment. Since the machine is inside the cluster, there won’t be issues of network latency and since the maintenance of the cluster is already handled, there is no cause of worry in cases of failure.

[Table of Contents](#Apache-Spark)

## What is Spark Streaming and how is it implemented in Spark?
Spark Streaming is one of the most important features provided by Spark. It is nothing but a Spark API extension for supporting stream processing of data from different sources.
Data from sources like Kafka, Kinesis, Flume, etc are processed and pushed to various destinations like databases, dashboards, machine learning APIs, or as simple as file systems. The data is divided into various streams (similar to batches) and is processed accordingly.
Spark streaming supports highly scalable, fault-tolerant continuous stream processing which is mostly used in cases like fraud detection, website monitoring, website click baits, IoT (Internet of Things) sensors, etc.
Spark Streaming first divides the data from the data stream into batches of X seconds which are called Dstreams or Discretized Streams. They are internally nothing but a sequence of multiple RDDs. The Spark application does the task of processing these RDDs using various Spark APIs and the results of this processing are again returned as batches. The following diagram explains the workflow of the spark streaming process.

[Table of Contents](#Apache-Spark)

## What can you say about Spark Datasets?
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

[Table of Contents](#Apache-Spark)

## Define Spark DataFrames.
Spark Dataframes are the distributed collection of datasets organized into columns similar to SQL. It is equivalent to a table in the relational database and is mainly optimized for big data operations.
Dataframes can be created from an array of data from different data sources such as external databases, existing RDDs, Hive Tables, etc. Following are the features of Spark Dataframes:
Spark Dataframes have the ability of processing data in sizes ranging from Kilobytes to Petabytes on a single node to large clusters.
They support different data formats like CSV, Avro, elastic search, etc, and various storage systems like HDFS, Cassandra, MySQL, etc.
By making use of SparkSQL catalyst optimizer, state of art optimization is achieved.
It is possible to easily integrate Spark Dataframes with major Big Data tools using SparkCore.

[Table of Contents](#Apache-Spark)

## Define Executor Memory in Spark
The applications developed in Spark have the same fixed cores count and fixed heap size defined for spark executors. The heap size refers to the memory of the Spark executor that is controlled by making use of the property spark.executor.memory that belongs to the -executor-memory flag. Every Spark applications have one allocated executor on each worker node it runs. The executor memory is a measure of the memory consumed by the worker node that the application utilizes.

[Table of Contents](#Apache-Spark)

## What are the functions of SparkCore?
SparkCore is the main engine that is meant for large-scale distributed and parallel data processing. The Spark core consists of the distributed execution engine that offers various APIs in Java, Python, and Scala for developing distributed ETL applications.
Spark Core does important functions such as memory management, job monitoring, fault-tolerance, storage system interactions, job scheduling, and providing support for all the basic I/O functionalities. There are various additional libraries built on top of Spark Core which allows diverse workloads for SQL, streaming, and machine learning. They are responsible for:
Fault recovery
Memory management and Storage system interactions
Job monitoring, scheduling, and distribution
Basic I/O functions

[Table of Contents](#Apache-Spark)

## What do you understand by worker node?
Worker nodes are those nodes that run the Spark application in a cluster. The Spark driver program listens for the incoming connections and accepts them from the executors addresses them to the worker nodes for execution. A worker node is like a slave node where it gets the work from its master node and actually executes them. The worker nodes do data processing and report the resources used to the master. The master decides what amount of resources needs to be allocated and then based on their availability, the tasks are scheduled for the worker nodes by the master.

[Table of Contents](#Apache-Spark)

## What are some demerits of using Spark in applications?
Despite Spark being the powerful data processing engine, there are certain demerits to using Apache Spark in applications. Some of them are:

Spark makes use of more storage space when compared to MapReduce or Hadoop which may lead to certain memory-based problems.
Care must be taken by the developers while running the applications. The work should be distributed across multiple clusters instead of running everything on a single node.
Since Spark makes use of “in-memory” computations, they can be a bottleneck to cost-efficient big data processing.
While using files present on the path of the local filesystem, the files must be accessible at the same location on all the worker nodes when working on cluster mode as the task execution shuffles between various worker nodes based on the resource availabilities. The files need to be copied on all worker nodes or a separate network-mounted file-sharing system needs to be in place.
One of the biggest problems while using Spark is when using a large number of small files. When Spark is used with Hadoop, we know that HDFS gives a limited number of large files instead of a large number of small files. When there is a large number of small gzipped files, Spark needs to uncompress these files by keeping them on its memory and network. So large amount of time is spent in burning core capacities for unzipping the files in sequence and performing partitions of the resulting RDDs to get data in a manageable format which would require extensive shuffling overall. This impacts the performance of Spark as much time is spent preparing the data instead of processing them.
Spark doesn’t work well in multi-user environments as it is not capable of handling many users concurrently.

[Table of Contents](#Apache-Spark)

## How can the data transfers be minimized while working with Spark?
Data transfers correspond to the process of shuffling. Minimizing these transfers results in faster and reliable running Spark applications. There are various ways in which these can be minimized. They are:
+ Usage of Broadcast Variables: Broadcast variables increases the efficiency of the join between large and small RDDs.
+ Usage of Accumulators: These help to update the variable values parallelly during execution.
  Another common way is to avoid the operations which trigger these reshuffles.

[Table of Contents](#Apache-Spark)

## What is SchemaRDD in Spark RDD?
SchemaRDD is an RDD consisting of row objects that are wrappers around integer arrays or strings that has schema information regarding the data type of each column. They were designed to ease the lives of developers while debugging the code and while running unit test cases on the SparkSQL modules. They represent the description of the RDD which is similar to the schema of relational databases. SchemaRDD also provides the basic functionalities of the common RDDs along with some relational query interfaces of SparkSQL.
Consider an example. If you have an RDD named Person that represents a person’s data. Then SchemaRDD represents what data each row of Person RDD represents. If the Person has attributes like name and age, then they are represented in SchemaRDD.

[Table of Contents](#Apache-Spark)

## What module is used for implementing SQL in Apache Spark?
Spark provides a powerful module called SparkSQL which performs relational data processing combined with the power of the functional programming feature of Spark. This module also supports either by means of SQL or Hive Query Language. It also provides support for different data sources and helps developers write powerful SQL queries using code transformations.
The four major libraries of SparkSQL are:
+ Data Source API
+ DataFrame API
+ Interpreter & Catalyst Optimizer
+ SQL Services
  Spark SQL supports the usage of structured and semi-structured data in the following ways:
+ Spark supports DataFrame abstraction in various languages like Python, Scala, and Java along with providing good optimization techniques.
+ SparkSQL supports data read and writes operations in various structured formats like JSON, Hive, Parquet, etc.
  S+ parkSQL allows data querying inside the Spark program and via external tools that do the JDBC/ODBC connections.

It is recommended to use SparkSQL inside the Spark applications as it empowers the developers to load the data, query the data from databases and write the results to the destination.

[Table of Contents](#Apache-Spark)

## What are the steps to calculate the executor memory?
Consider you have the below details regarding the cluster:
Number of nodes = 10
Number of cores in each node = 15 cores
RAM of each node = 61GB
To identify the number of cores, we follow the approach:
Number of Cores = number of concurrent tasks that can be run parallelly by the executor. The optimal value as part of a general rule of thumb is 5.
Hence to calculate the number of executors, we follow the below approach:

Number of executors = Number of cores/Concurrent Task = 15/5 = 3
Number of executors = Number of nodes * Number of executor in each node = 10 * 3 = 30 executors per Spark job

[Table of Contents](#Apache-Spark)

## Why do we need broadcast variables in Spark?
Broadcast variables let the developers maintain read-only variables cached on each machine instead of shipping a copy of it with tasks. They are used to give every node copy of a large input dataset efficiently. These variables are broadcasted to the nodes using different algorithms to reduce the cost of communication.
Differentiate between Spark Datasets, Dataframes and RDDs.
Criteria	Spark Datasets	Spark Dataframes	Spark RDDs
Representation of Data	Spark Datasets is a combination of Dataframes and RDDs with features like static type safety and object-oriented interfaces.	Spark Dataframe is a distributed collection of data that is organized into named columns.	Spark RDDs are a distributed collection of data without schema.
Optimization	Datasets make use of catalyst optimizers for optimization.	Dataframes also makes use of catalyst optimizer for optimization.	There is no built-in optimization engine.
Schema Projection	Datasets find out schema automatically using SQL Engine.	Dataframes also find the schema automatically.	Schema needs to be defined manually in RDDs.
Aggregation Speed	Dataset aggregation is faster than RDD but slower than Dataframes.	Aggregations are faster in Dataframes due to the provision of easy and powerful APIs.	RDDs are slower than both the Dataframes and the Datasets while performing even simple operations like data grouping.

[Table of Contents](#Apache-Spark)

## Can Apache Spark be used along with Hadoop? If yes, then how?
Yes! The main feature of Spark is its compatibility with Hadoop. This makes it a powerful framework as using the combination of these two helps to leverage the processing capacity of Spark by making use of the best of Hadoop’s YARN and HDFS features.
Hadoop can be integrated with Spark in the following ways:
HDFS: Spark can be configured to run atop HDFS to leverage the feature of distributed replicated storage.
MapReduce: Spark can also be configured to run alongside the MapReduce in the same or different processing framework or Hadoop cluster. Spark and MapReduce can be used together to perform real-time and batch processing respectively.
YARN: Spark applications can be configured to run on YARN which acts as the cluster management framework.

[Table of Contents](#Apache-Spark)

## What are Sparse Vectors? How are they different from dense vectors?
Sparse vectors consist of two parallel arrays where one array is for storing indices and the other for storing values. These vectors are used to store non-zero values for saving space.

val sparseVec: Vector = Vectors.sparse(5, Array(0, 4), Array(1.0, 2.0))
In the above example, we have the vector of size 5, but the non-zero values are there only at indices 0 and 4.
Sparse vectors are particularly useful when there are very few non-zero values. If there are cases that have only a few zero values, then it is recommended to use dense vectors as usage of sparse vectors would introduce the overhead of indices which could impact the performance.
Dense vectors can be defines as follows:
val denseVec = Vectors.dense(4405d,260100d,400d,5.0,4.0,198.0,9070d,1.0,1.0,2.0,0.0)
Usage of sparse or dense vectors does not impact the results of calculations but when used inappropriately, they impact the memory consumed and the speed of calculation.

[Table of Contents](#Apache-Spark)

## How are automatic clean-ups triggered in Spark for handling the accumulated metadata?
The clean-up tasks can be triggered automatically either by setting spark.cleaner.ttl parameter or by doing the batch-wise division of the long-running jobs and then writing the intermediary results on the disk.

[Table of Contents](#Apache-Spark)

## How is Caching relevant in Spark Streaming?
Spark Streaming involves the division of data stream’s data into batches of X seconds called DStreams. These DStreams let the developers cache the data into the memory which can be very useful in case the data of DStream is used for multiple computations. The caching of data can be done using the cache() method or using persist() method by using appropriate persistence levels. The default persistence level value for input streams receiving data over the networks such as Kafka, Flume, etc is set to achieve data replication on 2 nodes to accomplish fault tolerance.
Caching using cache method:
val cacheDf = dframe.cache()
Caching using persist method:
val persistDf = dframe.persist(StorageLevel.MEMORY_ONLY)
The main advantages of caching are:
+ Cost efficiency: Since Spark computations are expensive, caching helps to achieve reusing of data and this leads to reuse computations which can save the cost of operations.
+ Time-efficient: The computation reusage leads to saving a lot of time.
+ More Jobs Achieved: By saving time of computation execution, the worker nodes can perform/execute more jobs.

[Table of Contents](#Apache-Spark)

## Define Piping in Spark.
Apache Spark provides the pipe() method on RDDs which gives the opportunity to compose different parts of occupations that can utilize any language as needed as per the UNIX Standard Streams. Using the pipe() method, the RDD transformation can be written which can be used for reading each element of the RDD as String. These can be manipulated as required and the results can be displayed as String.

[Table of Contents](#Apache-Spark)

## What API is used for Graph Implementation in Spark?
Spark provides a powerful API called GraphX that extends Spark RDD for supporting graphs and graph-based computations. The extended property of Spark RDD is called as Resilient Distributed Property Graph which is a directed multi-graph that has multiple parallel edges. Each edge and the vertex has associated user-defined properties. The presence of parallel edges indicates multiple relationships between the same set of vertices. GraphX has a set of operators such as subgraph, mapReduceTriplets, joinVertices, etc that can support graph computation. It also includes a large collection of graph builders and algorithms for simplifying tasks related to graph analytics.

[Table of Contents](#Apache-Spark)

## How can you achieve machine learning in Spark?
Spark provides a very robust, scalable machine learning-based library called MLlib. This library aims at implementing easy and scalable common ML-based algorithms and has the features like classification, clustering, dimensional reduction, regression filtering, etc. More information about this library can be obtained in detail from Spark’s official documentation site here: https://spark.apache.org/docs/latest/ml-guide.html

[Table of Contents](#Apache-Spark)

## What are the limitations of Spark?
Does not have its file management system. Thus, it needs to integrate with Hadoop or other cloud-based data platforms.
In-memory capability can become a bottleneck. Especially when it comes to cost-efficient processing of Bigdata.
Memory consumption is very high. And the issues for the same are not handled in a user-friendly manner. d. It requires large data.
MLlib lack in some available algorithms, for example, Tanimoto distance.
Read more Apache Spark Limitations in detail.

[Table of Contents](#Apache-Spark)

## Compare Hadoop and Spark.
+ Cost Efficient – In Hadoop, during replication, a large number of servers, huge amount of storage, and the large data center is required. Thus, installing and using Apache Hadoop is expensive. While using Apache Spark is a cost effective solution for big data environment.
+ Performance – The basic idea behind Spark was to improve the performance of data processing. And Spark did this to 10x-100x times. And all the credit of faster processing in Spark goes to in-memory processing of data. In Hadoop, the data processing takes place in disc while in Spark the data processing takes place in memory. It moves to the disc only when needed. The Spark in-memory computation is beneficial for iterative algorithms. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow while the processing speed of Apache is faster as it supports micro-batching.
+ Ease of development – The core in Spark is the distributed execution engine. Various languages are supported by Apache Spark for distributed application development. For example, Java, Scala, Python, and R. On the top of spark core, various libraries are built that enables workload. they make use of streaming, SQL, graph and machine learning. Hadoop also supports some of these workloads but Spark eases the development by combining all into the same application. d. Failure recovery: The method of Fault
+ Failure recovery – The method of Fault Recovery is different in both Apache Hadoop and Apache Spark. In Hadoop after every operation data is written to disk. The data objects are stored in Spark in RDD distributed across data cluster. The RDDs are either in memory or on disk and provides full recovery from faults or failure.
+ File Management System – Hadoop has its own File Management System called HDFS (Hadoop Distributed File System). While Apache Spark an integration with one, it may be even HDFS. Thus, Hadoop can run over Apache Spark.
+ Computation model – Apache Hadoop uses batch processing model i.e. it takes a large amount of data and processes it. But Apache Spark adopts micro-batching. Must for handling near real time processing data model. When it comes to performance, because of batch processing in Hadoop it’s processing is quite slow. The processing speed of Apache is faster as it supports micro-batching.
+ Lines of code – Apache Hadoop has near about 23, 00,000 lines of code while Apache Spark has 20,000 lines of code.
+ Caching – By caching partial result in memory of distributed workers Spark ensures low latency computations. While MapReduce is completely disk oriented, there is no provision of caching.
+ Scheduler – Because of in-memory computation in Spark, it acts as its own flow scheduler. While with Hadoop MapReduce we need an extra job scheduler like Azkaban or Oozie so that we can schedule complex flows.
+ Spark API – Because of very Strict API in Hadoop MapReduce, it is not versatile. But since Spark discards many low-level details it is more productive.
+ Window criteria – Apache Spark has time-based window criteria. But Apache Hadoop does not have window criteria since it does not support streaming.
+ Faster – Apache Hadoop executes job 10 to 100 times faster than Apache Hadoop MapReduce.
+ License – Both Apache Hadoop and Apache MapReduce has a License Version 2.0.
+ DAG() – In Apache Spark, there is cyclic data flow in machine learning algorithm, which is a direct acyclic graph. While in Hadoop MapReduce data flow does not have any loops, rather it is a chain of the image.
+ Memory Management – Apache Spark has automatic memory management system. While Memory Management in Apache Hadoop can be either statistic or dynamic.
+ Iterative Processing – In Apache Spark, the data iterates in batches. Here processing and scheduling of each iteration are separate. While in Apache Hadoop there is no provision for iterative processing.
+ Latency – The time taken for processing by Apache Spark is less as compared to Hadoop since it caches its data on memory by means of RDD, thus the latency of Apache Spark is less as compared to Hadoop.

[Table of Contents](#Apache-Spark)

## What is lazy evaluation in Spark?
lazy evaluation known as call-by-need is a strategy that delays the execution until one requires a value. The transformation in Spark is lazy in nature. Spark evaluate them lazily. When we call some operation in RDD it does not execute immediately; Spark maintains the graph of which operation it demands. We can execute the operation at any instance by calling the action on the data. The data does not loads until it is necessary.

[Table of Contents](#Apache-Spark)

## What are the benefits of lazy evaluation?
Using lazy evaluation we can:
+ Increase the manageability of the program.
+ Saves computation overhead and increases the speed of the system.
+ Reduces the time and space complexity.
+ provides the optimization by reducing the number of queries.

[Table of Contents](#Apache-Spark)

## What do you mean by Persistence?
RDD persistence is an optimization technique which saves the result of RDD evaluation. Using this we save the intermediate result for further use. It reduces the computation overhead. We can make persisted RDD through cache() and persist() methods. It is a key tool for the interactive algorithm. Because, when RDD is persisted each node stores any partition of it that it computes in memory. Thus makes it reusable for future use. This process speeds up the further computation ten times.

[Table of Contents](#Apache-Spark)

## Explain the run time architecture of Spark?
The components of the run-time architecture of Spark are as follows:
+ The Driver – The main() method of the program runs in the driver. The process that runs the user code which creates RDDs performs transformation and action, and also creates SparkContext is called diver. When the Spark Shell is launched, this signifies that we have created a driver program. The application finishes, as the driver terminates. Finally, driver program splits the Spark application into the task and schedules them to run on the executor.
+ Cluster Manager –  Spark depends on cluster manager to launch executors. In some cases, even the drivers are launched by cluster manager. It is a pluggable component in Spark. On the cluster manager, the Spark scheduler schedules the jobs and action within a spark application in FIFO fashion. Alternatively, the scheduling can also be done in Round Robin fashion. The resources used by a Spark application can also be dynamically adjusted based on the workload. Thus, the application can free unused resources and request them again when there is a demand. This is available on all coarse-grained cluster managers, i.e. standalone mode, YARN mode, and Mesos coarse-grained mode.
+ The Executors –  Each task in the Spark job runs in the Spark executors. thus, Executors are launched once in the beginning of Spark Application and then they run for the entire lifetime of an application. Even after the failure of Spark executor, the Spark application can continue with ease.
  There are two main roles of the executors:
+ Runs the task that makes up the application and returns the result to the driver.
+ Provide in-memory storage for RDDs that the user program cache.

[Table of Contents](#Apache-Spark)

## What is the difference between DSM and RDD?
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

[Table of Contents](#Apache-Spark)

## How can data transfer be minimized when working with Apache Spark?
By minimizing data transfer and avoiding shuffling of data we can increase the performance. In Apache Spark, we can minimize the data transfer in three ways:
By using a broadcast variable – Since broadcast variable increases the efficiency of joins between small and large RDDs. the broadcast variable allows keeping a read-only variable cached on every machine in place of shipping a copy of it with tasks. We create broadcast variable v by calling SparlContext.broadcast(v) and we can access its value by calling the value method.
Using Accumulator – Using accumulator we can update the value of a variable in parallel while executing. Accumulators can only be added through the associative and commutative operation. We can also implement counters (as in MapReduce) or sums using an accumulator. Users can create named or unnamed accumulator. We can create numeric accumulator by calling SparkContext.longAccumulator() or SparkContext.doubleAccumulator() for Long or Double respectively.
By avoiding operations like ByKey, repartition or any other operation that trigger shuffle. we can minimize the data transfer.

[Table of Contents](#Apache-Spark)

## How does Apache Spark handles accumulated Metadata?
By triggering automatic cleanup Spark handles the automatic Metadata. We can trigger cleanup by setting the parameter “spark.cleaner.ttl“. the default value for this is infinite. It tells for how much duration Spark will remember the metadata. It is periodic cleaner. And also ensure that metadata older than the set duration will vanish. Thus, with its help, we can run Spark for many hours.

[Table of Contents](#Apache-Spark)

## What are the common faults of the developer while using Apache Spark?
The common mistake by developers are:
Customer hit web-service several time by using multiple clusters.
Customer runs everything on local node instead of distributing it.

[Table of Contents](#Apache-Spark)

## Which among the two is preferable for the project- Hadoop MapReduce or Apache Spark?
The answer to this question depends on the type of project one has. As we all know Spark makes use of a large amount of RAM and also needs a dedicated machine to provide an effective result. Thus the answer depends on the project and the budget of the organization.

[Table of Contents](#Apache-Spark)

## List the popular use cases of Apache Spark.
The most popular use-cases of Apache Spark are:
1. Streaming
2. Machine Learning
3. interactive Analysis
4. fog computing
5. Using Spark in the real world

[Table of Contents](#Apache-Spark)

## What is Spark.executor.memory in a Spark Application?
The default value for this is 1 GB. It refers to the amount of memory that will be used per executor process.
We have categorized the above Spark Interview Questions and Answers for Freshers and Experienced-
Spark Interview Questions and Answers for Fresher – Q.No.1-8, 37
Spark Interview Questions and Answers for Experienced – Q.No. 9-36, 38
Follow this link to read more Spark Basic interview Questions with Answers.
b. Spark SQL Interview Questions and Answers
In this section, we will discuss some basic Spark SQL Interview Questions and Answers.

[Table of Contents](#Apache-Spark)

## What is DataFrames?
It is a collection of data which organize in named columns. It is theoretically equivalent to a table in relational database. But it is more optimized. Just like RDD, DataFrames evaluates lazily. Using lazy evaluation we can optimize the execution. It optimizes by applying the techniques such as bytecode generation and predicate push-downs.

[Table of Contents](#Apache-Spark)

## What are the advantages of DataFrame?
It makes large data set processing even easier. Data Frame also allows developers to impose a structure onto a distributed collection of data. As a result, it allows higher-level abstraction.
Data frame is both space and performance efficient.
It can deal with both structured and unstructured data formats, for example, Avro, CSV etc . And also storage systems like HDFS, HIVE tables, MySQL, etc.
The DataFrame API’s are available in various programming languages. For example Java, Scala, Python, and R.
It provides Hive compatibility. As a result, we can run unmodified Hive queries on existing Hive warehouse.
Catalyst tree transformation uses DataFrame in four phases: a) Analyze logical plan to solve references. b) Logical plan optimization c) Physical planning d) Code generation to compile part of the query to Java bytecode.
It can scale from kilobytes of data on the single laptop to petabytes of data on the large cluster.

[Table of Contents](#Apache-Spark)

## What is DataSet?
Spark Datasets are the extension of Dataframe API. It creates object-oriented programming interface and type-safety. Dataset is Spark 1.6 release. It makes use of Spark’s catalyst optimizer. It reveals expressions and data fields to a query optimizer. Dataset also influences fast in-memory encoding. It also provides provision for compile time type-safety. We can check for errors in an application when they run.

[Table of Contents](#Apache-Spark)

## What are the advantages of DataSets?
It provides run-time type safety.
Influences fast in-memory encoding.
It provides a custom view of structured and semi-structured data.
It owns rich semantics and an easy set of domain-specific operations, as a result, it facilitates the use of structured data.
Dataset API decreases the use of memory. As Spark knows the structure of data in the dataset, thus it creates an optimal layout in memory while caching.

[Table of Contents](#Apache-Spark)

## Explain Catalyst framework.
The Catalyst is a framework which represents and manipulate a DataFrame graph. Data flow graph is a tree of relational operator and expressions. The three main features of catalyst are:
It has a TreeNode library for transforming tree. They are expressed as Scala case classes.
A logical plan representation for relational operator.
Expression library.
The TreeNode builds a query optimizer. It contains a number of the query optimizer. Catalyst Optimizer supports both rule-based and cost-based optimization. In rule-based optimization the optimizer use set of rule to determine how to execute the query. While the cost based optimization finds the most suitable way to carry out SQL statement. In cost-based optimization, many plans are generates using rules. And after this, it computes their cost. Catalyst optimizer makes use of standard features of Scala programming like pattern matching.

[Table of Contents](#Apache-Spark)

## What is DStream?
DStream is the high-level abstraction provided by Spark Streaming. It represents a continuous stream of data. Thus, DStream is internally a sequence of RDDs. There are two ways to create DStream:
by using data from different sources such as Kafka, Flume, and Kinesis.
by applying high-level operations on other DStreams.

[Table of Contents](#Apache-Spark)

## Explain different transformation on DStream.
DStream is a basic abstraction of Spark Streaming. It is a continuous sequence of RDD which represents a continuous stream of data. Like RDD, DStream also supports many transformations which are available on normal Spark RDD. For example, map(func), flatMap(func), filter(func) etc.

[Table of Contents](#Apache-Spark)

## What is written ahead log or journaling?
The write-ahead log is a technique that provides durability in a database system. It works in the way that all the operation that applies on data, we write it to write-ahead log. The logs are durable in nature. Thus, when the failure occurs we can easily recover the data from these logs. When we enable the write-ahead log Spark stores the data in fault-tolerant file system.

[Table of Contents](#Apache-Spark)

## Explain first operation in Apache Spark RDD.
It is an action and returns the first element of the RDD.

[Table of Contents](#Apache-Spark)

## Describe join operation. How is outer join supported?
join() is transformation and is in package org.apache.spark.rdd.pairRDDFunction
def join[W](other: RDD[(K, W)]): RDD[(K, (V, W))]Permalink
Return an RDD containing all pairs of elements with matching keys in this and other.
Each pair of elements will returns as a (k, (v1, v2)) tuple, where (k, v1) is in this and (k, v2) is in other. Performs a hash join across the cluster.
It is joining two datasets. When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.

[Table of Contents](#Apache-Spark)

## Describe coalesce operation. When can you coalesce to a larger number of partitions? Explain.
It is a transformation and it’s in a package org.apache.spark.rdd.ShuffledRDD
Return a new RDD that is reduced into numPartitions partitions.
This results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead, each of the 100 new partitions will claim 10 of the current partitions.
However, if you’re doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can pass shuffle = true. This will add a shuffle step but means the current upstream partitions will execut in parallel (per whatever the current partitioning is).
Note: With shuffle = true, you can actually coalesce to a larger number of partitions. This is useful if you have a small number of partitions, say 100, potentially with a few partitions being abnormally large. Calling coalesce(1000, shuffle = true) will result in 1000 partitions with the data distributed using a hash partitioner.
Coalesce() operation changes a number of the partition where data is stored. It combines original partitions to a new number of partitions, so it reduces the number of partitions. Coalesce() operation is an optimized version of repartition that allows data movement, but only if you are decreasing the number of RDD partitions. It runs operations more efficiently after filtering large datasets.

[Table of Contents](#Apache-Spark)

## Describe Partition and Partitioner in Apache Spark.
Partition in Spark is similar to split in HDFS. A partition in Spark is a logical division of data stored on a node in the cluster. They are the basic units of parallelism in Apache Spark. RDDs are a collection of partitions. When some actions are executed, a task is launched per partition.
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

[Table of Contents](#Apache-Spark)

## How can you manually partition the RDD?
When we create the RDD from a file stored in HDFS.
data = context.textFile("/user/dataflair/file-name")
By default one partition is created for one block. ie. if we have a file of size 1280 MB (with 128 MB block size) there will be 10 HDFS blocks, hence the similar number of partitions (10) will create.
If you want to create more partitions than the number of blocks, you can specify the same while RDD creation:
data = context.textFile("/user/dataflair/file-name", 20)
It will create 20 partitions for the file. ie for each block 2 partitions will create.
NOTE: It is often recommended to have more no of partitions than no of the block, it improves the performance

[Table of Contents](#Apache-Spark)

## Explain API create Or Replace TempView.
It’s basic Dataset function and under org.apache.spark.sql
def createOrReplaceTempView(viewName: String): Unit
Creates a temporary view using the given name.
scala> df.createOrReplaceTempView("titanicdata")

[Table of Contents](#Apache-Spark)

## What are the various advantages of DataFrame over RDD in Apache Spark?
DataFrames are the distributed collection of data. In DataFrame, data is organized into named columns. It is conceptually similar to a table in a relational database.
we can construct DataFrames from a wide array of sources. Such as structured data files, tables in Hive, external databases, or existing RDDs.
As same as RDDs, DataFrames are evaluated lazily(Lazy Evaluation). In other words, computation only happens when an action (e.g. display result, save output) is required.
Out of the box, DataFrame supports reading data from the most popular formats, including JSON files, Parquet files, Hive tables. Also, can read from distributed file systems (HDFS), local file systems, cloud storage (S3), and external relational database systems through JDBC. In addition, through Spark SQL’s external data sources API, DataFrames can extend to support any third-party data formats or sources. Existing third-party extensions already include Avro, CSV, ElasticSearch, and Cassandra.
There is much more to know about DataFrames. Refer link: Spark SQL DataFrame

[Table of Contents](#Apache-Spark)

## What is a DataSet and what are its advantages over DataFrame and RDD?
In Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.
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

[Table of Contents](#Apache-Spark)

## On what all basis can you differentiate RDD and DataFrame and DataSet?
DataFrame: A Data Frame is used for storing data into tables. It is equivalent to a table in a relational database but with richer optimization. Spark DataFrame is a data abstraction and domain-specific language (DSL) applicable on a structure and semi-structured data. It is distributed the collection of data in the form of named column and row. It has a matrix-like structure whose column may be different types (numeric, logical, factor, or character ). We can say data frame has the two-dimensional array like structure where each column contains the value of one variable and row contains one set of values for each column and combines feature of list and matrices
RDD is the representation of a set of records, immutable collection of objects with distributed computing. RDD is a large collection of data or RDD is an array of reference of partitioned objects. Each and every dataset in RDD is logically partitioned across many servers so that they can compute on different nodes of the cluster. RDDs are fault tolerant i.e. self-recovered/recomputed in the case of failure. The dataset can load externally by the users which can be in the form of JSON file, CSV file, text file or database via JDBC with no specific data structure.
DataSet in Apache Spark, Datasets are an extension of DataFrame API. It offers object-oriented programming interface. Through Spark SQL, it takes advantage of Spark’s Catalyst optimizer by exposing e data fields to a query planner.

[Table of Contents](#Apache-Spark)

## Explain the level of parallelism in Spark Streaming.
In order to reduce the processing time, one need to increase the parallelism. In Spark Streaming, there are three ways to increase the parallelism:
Increase the number of receivers : If there are too many records for single receiver (single machine) to read in and distribute so that is bottleneck. So we can increase the no. of receiver depends on scenario.
Re-partition the receive data : If one is not in a position to increase the no. of receivers in that case redistribute the data by re-partitioning.
Increase parallelism in aggregation :
for complete guide on Spark Streaming you may refer to Apache Spark-Streaming guide

[Table of Contents](#Apache-Spark)

## Discuss writeahead logging in Apache Spark Streaming.
There are two types of failures in any Apache Spark job – Either the driver failure or the worker failure.
When any worker node fails, the executor processes running in that worker node will kill, and the tasks which were scheduled on that worker node will be automatically moved to any of the other running worker nodes, and the tasks will accomplish.
When the driver or master node fails, all of the associated worker nodes running the executors will kill, along with the data in each of the executors’ memory. In the case of files being read from reliable and fault tolerant file systems like HDFS, zero data loss is always guaranteed, as the data is ready to be read anytime from the file system. Checkpointing also ensures fault tolerance in Spark by periodically saving the application data in specific intervals.
In the case of Spark Streaming application, zero data loss is not always guaranteed, as the data will buffer in the executors’ memory until they get processed. If the driver fails, all of the executors will kill, with the data in their memory, and the data cannot recover.
To overcome this data loss scenario, Write Ahead Logging (WAL) has been introduced in Apache Spark 1.2. With WAL enabled, the intention of the operation is first noted down in a log file, such that if the driver fails and is restarted, the noted operations in that log file can apply to the data. For sources that read streaming data, like Kafka or Flume, receivers will be receiving the data, and those will store in the executor’s memory. With WAL enabled, these received data will also store in the log files.
WAL can enable by performing the below:
1. Setting the checkpoint directory, by using streamingContext.checkpoint(path)
2. Enabling the WAL logging, by setting spark.stream.receiver.WriteAheadLog.enable to True.

[Table of Contents](#Apache-Spark)

## What do you mean by Speculative execution in Apache Spark?
The Speculative task in Apache Spark is task that runs slower than the rest of the task in the job.It is health check process that verifies the task is speculated, meaning the task that runs slower than the median of successfully completed task in the task sheet. Such tasks are submitted to another worker. It runs the new copy in parallel rather than shutting down the slow task.

In the cluster deployment mode, the thread starts as TaskSchedulerImp1with spark.speculation enabled. It executes periodically every spark.speculation.interval after the initial spark.speculation.interval passes.

[Table of Contents](#Apache-Spark)

## How do you parse data in XML? Which kind of class do you use with java to pass data?
One way to parse the XML data in Java is to use the JDOM library. One can download it and import the JDOM library in your project. You can get help from Google. If still, required help post your problem in the forum. I will try to give you the solution. For Scala, Scala has the inbuilt library for XML parsing. Scala-xml_2.11-1.0.2 jar (please check them for new version if available).

[Table of Contents](#Apache-Spark)

## Explain Machine Learning library in Spark.
It is a scalable machine learning library. It delivers both blazing speed (up to 100x faster than MapReduce) and high-quality algorithms (e.g., multiple iterations to increase accuracy). We can use this library in Java, Scala, and Python as part of Spark applications so that you can include it incomplete workflows. There are many tools, which are provided by MLlib. Such as-
ML Algorithms: Common learning algorithms such as classification, regression, clustering, and collaborative filtering.
Featurization: Feature extraction, transformation, dimensionality reduction, and selection.
Pipelines: Tools for constructing, evaluating, and tuning ML Pipelines.
Persistence: Saving and load algorithms, models, and Pipelines.
Utilities: Linear algebra, statistics, data handling, etc.
For detailed insights, follow link: Apache Spark MLlib (Machine Learning Library)

[Table of Contents](#Apache-Spark)

## List various commonly used Machine Learning Algorithm.
Basically, there are three types of Machine Learning Algorithms :
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

[Table of Contents](#Apache-Spark)

## Explain the Parquet File format in Apache Spark. When is it the best to choose this?
Parquet is the columnar information illustration that is that the best choice for storing long run massive information for analytics functions. It will perform each scan and write operations with Parquet file. It could be a columnar information storage format.

[Table of Contents](#Apache-Spark)

## What is Lineage Graph?
The RDDs in Spark, depend on one or more other RDDs. The representation of dependencies in between RDDs is known as the lineage graph. Lineage graph information is used to compute each RDD on demand, so that whenever a part of persistent RDD is lost, the data that is lost can be recovered using the lineage graph information.

[Table of Contents](#Apache-Spark)

## How can you Trigger Automatic Cleanups in Spark to Handle Accumulated Metadata?
You can trigger the clean-ups by setting the parameter spark.cleaner.ttl or by dividing the long running jobs into different batches and writing the intermediary results to the disk.

[Table of Contents](#Apache-Spark)

## What are the benefits of using Spark With Apache Mesos?
It renders scalable partitioning among various Spark instances and dynamic partitioning between Spark and other big data frameworks.

[Table of Contents](#Apache-Spark)

## What is the Significance of Sliding Window Operation?
Sliding Window controls transmission of data packets between various computer networks. Spark Streaming library provides windowed computations where the transformations on RDDs are applied over a sliding window of data. Whenever the window slides, the RDDs that fall within the particular window are combined and operated upon to produce new RDDs of the windowed DStream.

[Table of Contents](#Apache-Spark)

## When running Spark Applications is it necessary to install Spark on all Nodes of Yarn Cluster?
Spark need not be installed when running a job under YARN or Mesos because Spark can execute on top of YARN or Mesos clusters without affecting any change to the cluster.

[Table of Contents](#Apache-Spark)

## What is Catalyst Framework?
Catalyst framework is a new optimization framework present in Spark SQL. It allows Spark to automatically transform SQL queries by adding new optimizations to build a faster processing system.

[Table of Contents](#Apache-Spark)

## Which Spark Library allows reliable File Sharing at Memory Speed across different cluster frameworks?
Tachyon

[Table of Contents](#Apache-Spark)

## Why is Blinkdb used?
BlinkDB is a query engine for executing interactive SQL queries on huge volumes of data and renders query results marked with meaningful error bars. BlinkDB helps users balance query accuracy with response time.

[Table of Contents](#Apache-Spark)

## How can you compare Hadoop and Spark in terms of ease of use?
Hadoop MapReduce requires programming in Java which is difficult, though Pig and Hive make it considerably easier. Learning Pig and Hive syntax takes time. Spark has interactive APIs for different languages like Java, Python or Scala and also includes Shark i.e. Spark SQL for SQL lovers - making it comparatively easier to use than Hadoop.

[Table of Contents](#Apache-Spark)

## What are the common mistakes developers make when running Spark Applications?
Developers often make the mistake of:-
Hitting the web service several times by using multiple clusters.
Run everything on the local node instead of distributing it.
Developers need to be careful with this, as Spark makes use of memory for processing.

[Table of Contents](#Apache-Spark)

## What is the Advantage of a Parquet File?
Parquet file is a columnar format file that helps:
Limit I/O operations
Consumes less space
Fetches only required columns.

[Table of Contents](#Apache-Spark)

## What are the various Data Sources available in Sparksql?
Parquet file
JSON Datasets
Hive tables

[Table of Contents](#Apache-Spark)

## What are the Key Features of Apache Spark that you like?
Spark provides advanced analytic options like graph algorithms, machine learning, streaming data, etc
It has built-in APIs in multiple languages like Java, Scala, Python and R
It has good performance gains, as it helps run an application in the Hadoop cluster ten times faster on disk and 100 times faster in memory.

[Table of Contents](#Apache-Spark)

## What do you understand by Pair Rdd?
Special operations can be performed on RDDs in Spark using key/value pairs and such RDDs are referred to as Pair RDDs. Pair RDDs allow users to access each key in parallel. They have a reduceByKey () method that collects data based on each key and a join () method that combines different RDDs together, based on the elements having the same key.

[Table of Contents](#Apache-Spark)

## Explain about different Types of Transformations on Dstreams?
Stateless Transformations:- Processing of the batch does not depend on the output of the previous batch.
Examples: map (), reduceByKey (), filter ().
Stateful Transformations:- Processing of the batch depends on the intermediary results of the previous batch.
Examples: Transformations that depend on sliding windows.

[Table of Contents](#Apache-Spark)

## Explain about popular use cases of Apache Spark?
Apache Spark is mainly used for:
Iterative machine learning.
Interactive data analytics and processing.
Stream processing
Sensor data processing

[Table of Contents](#Apache-Spark)

## Is Apache Spark a good fit for reinforcement Learning?
No. Apache Spark works well only for simple machine learning algorithms like clustering, regression, classification.

[Table of Contents](#Apache-Spark)

## What is Spark Core?
It has all the basic functionalities of Spark, like - memory management, fault recovery, interacting with storage systems, scheduling tasks, etc.

[Table of Contents](#Apache-Spark)

## How can you remove the elements with a Key present in any other Rdd?
Use the subtractByKey () function.

[Table of Contents](#Apache-Spark)

## What is the difference between Persist and Cache?
persist () allows the user to specify the storage level where as cache () uses the default storage level.

[Table of Contents](#Apache-Spark)

## How Spark handles Monitoring and Logging in Standalone Mode?
Spark has a web based user interface for monitoring the cluster in standalone mode that shows the cluster and job statistics. The log output for each job is written to the work directory of the slave nodes.

[Table of Contents](#Apache-Spark)

## Does Apache Spark provide check pointing?
Lineage graphs are always useful to recover RDDs from a failure but this is generally time consuming if the RDDs have long lineage chains. Spark has an API for check pointing i.e. a REPLICATE flag to persist. However, the decision on which data to checkpoint - is decided by the user. Checkpoints are useful when the lineage graphs are long and have wide dependencies.

[Table of Contents](#Apache-Spark)

## How can you launch Spark Jobs inside Hadoop Mapreduce?
Using SIMR (Spark in MapReduce) users can run any spark job inside MapReduce without requiring any admin rights.

[Table of Contents](#Apache-Spark)

## How can you achieve High Availability in Apache Spark?
Implementing single node recovery with local file system
Using StandBy Masters with Apache ZooKeeper.

[Table of Contents](#Apache-Spark)

## Hadoop uses Replication to achieve Fault Tolerance and how is this achieved in Apache Spark?
Data storage model in Apache Spark is based on RDDs. RDDs help achieve fault tolerance through lineage. RDD always has the information on how to build from other datasets. If any partition of a RDD is lost due to failure, lineage helps build only that particular lost partition.

[Table of Contents](#Apache-Spark)

## Explain about Core Components of a distributed Spark Application?
Driver: The process that runs the main () method of the program to create RDDs and perform transformations and actions on them.
Executor: The worker processes that run the individual tasks of a Spark job.
Cluster Manager: A pluggable component in Spark, to launch Executors and Drivers. The cluster manager allows Spark to run on top of other external managers like Apache Mesos or YARN.

[Table of Contents](#Apache-Spark)

## What do you understand by Lazy Evaluation?
Spark is intellectual in the manner in which it operates on data. When you tell Spark to operate on a given dataset, it heeds the instructions and makes a note of it, so that it does not forget - but it does nothing, unless asked for the final result.
When a transformation like map () is called on a RDD-the operation is not performed immediately. Transformations in Spark are not evaluated till you perform an action. This helps optimize the overall data processing workflow.

[Table of Contents](#Apache-Spark)

## Define a Worker Node?
A node that can run the Spark application code in a cluster can be called as a worker node. A worker node can have more than one worker which is configured by setting the SPARK_ WORKER_INSTANCES property in the spark-env.sh file. Only one worker is started if the SPARK_ WORKER_INSTANCES property is not defined.

[Table of Contents](#Apache-Spark)

## What do you understand by Schemardd?
An RDD that consists of row objects (wrappers around basic string or integer arrays) with schema information about the type of data in each column.

[Table of Contents](#Apache-Spark)

## What are the disadvantages of using Apache Spark over Hadoop Mapreduce?
Apache spark does not scale well for compute intensive jobs and consumes large number of system resources. Apache Spark’s in-memory capability at times comes a major roadblock for cost efficient processing of big data. Also, Spark does have its own file management system and hence needs to be integrated with other cloud based data platforms or apache hadoop.

[Table of Contents](#Apache-Spark)

## Is it necessary to install Spark on all Nodes of Yarn Cluster while running Apache Spark on Yarn?
No , it is not necessary because Apache Spark runs on top of YARN.

[Table of Contents](#Apache-Spark)

## What do you understand by Executor Memory in Spark Application?
Every spark application has same fixed heap size and fixed number of cores for a spark executor. The heap size is what referred to as the Spark executor memory which is controlled with the spark.executor.memory property of the –executor-memory flag.
Every spark application will have one executor on each worker node. The executor memory is basically a measure on how much memory of the worker node will the application utilize.

[Table of Contents](#Apache-Spark)

## What does the Spark Engine do?
Spark engine schedules, distributes and monitors the data application across the spark cluster.

[Table of Contents](#Apache-Spark)

## What makes Apache Spark good at Low latency Workloads like Graph Processing and Machine Learning?
Apache Spark stores data in-memory for faster model building and training. Machine learning algorithms require multiple iterations to generate a resulting optimal model and similarly graph algorithms traverse all the nodes and edges.
These low latency workloads that need multiple iterations can lead to increased performance. Less disk access and  controlled network traffic make a huge difference when there is lots of data to be processed.

[Table of Contents](#Apache-Spark)

## What is Dstream in Apache Spark?
Dstream stands for Discretized Stream. It is a sequence of Resilient Distributed Database (RDD) representing a continuous stream of data. There are several ways to create Dstream from various sources like HDFS, Apache Flume, Apache Kafka, etc.

[Table of Contents](#Apache-Spark)

## What do you understand by YARN?
Just like in Hadoop, YARN is one of the key features in Apache Spark, which is used to provide a central and resource management platform to deliver scalable operations across the cluster. Spark can run on YARN, as the same way Hadoop Map Reduce can run on YARN.

[Table of Contents](#Apache-Spark)

## Is it necessary to install Spark on all nodes of the YARN cluster?
No. It doesn't seem necessary to install Spark on all YARN cluster nodes because Spark runs on top of the YARN. Apache Spark runs independently from its installation. Spark provides some options to use YARN when dispatching jobs to the cluster, rather than its built-in manager or Mesos. Besides this, there are also some configurations to run YARN, such as master, deploy-mode, driver-memory, executor-memory, executor-cores, and queue.

[Table of Contents](#Apache-Spark)

## What are the different data sources available in SparkSQL?
There are the following three data sources available in SparkSQL:
JSON Datasets
Hive tables
Parquet file

[Table of Contents](#Apache-Spark)

## Which are some important internal daemons used in Apache Spark?
Following are the important internal daemons used in Spark:
Blockmanager
Memestore
DAGscheduler
Driver
Worker
Executor
Tasks etc.

[Table of Contents](#Apache-Spark)

## What is the method to create a Data frame in Apache Spark?
In Apache Spark, we can create a data frame using Tables in Hive and Structured data files.

[Table of Contents](#Apache-Spark)

## What do you understand by accumulators in Apache Spark?
Accumulators are the write-only variables that are initialized once and sent to the workers. Then, these workers update based on the logic written, which will send back to the driver.

[Table of Contents](#Apache-Spark)

## What is the default level of parallelism in Apache Spark?
If it is not specified, then the number of partitions is called the default level of parallelism in Apache Spark.

[Table of Contents](#Apache-Spark)

## Which companies are using Spark streaming services?
The three most famous companies using Spark Streaming services are:
Uber
Netflix
Pinterest

[Table of Contents](#Apache-Spark)

## Is it possible to use Spark to access and analyze data stored in Cassandra databases?
Yes, it is possible to use Spark to access and analyze Cassandra databases' data by using Cassandra Connector.

[Table of Contents](#Apache-Spark)

## Can we run Apache Spark on Apache Mesos?
Yes, we can run Apache Spark on the hardware clusters managed by Mesos.

[Table of Contents](#Apache-Spark)

## What do you understand by Spark SQL?
Spark SQL is a module for structured data processing, which provides the advantage of SQL queries running on that database.

[Table of Contents](#Apache-Spark)

## How can you connect Spark to Apache Mesos?
Follow the steps given below to connect Spark to Apache Mesos:
Configure the spark driver program to connect to Mesos.
Set a path location for the Spark binary package that it can be accessible by Mesos.
Install Apache Spark in the same location as that of Apache Mesos and configure the property spark.mesos.executor.home to point to the location where it is installed.

[Table of Contents](#Apache-Spark)

## What is the best way to minimize data transfers when working with Spark?
To write a fast and reliable Spark program, we have to minimize data transfers and avoid shuffling. There are various ways to minimize data transfers while working with Apache Spark. These are:
Using Broadcast Variable- Broadcast variables enhance the efficiency of joins between small and large RDDs.
Using Accumulators- Accumulators are used to updating the values of variables in parallel while executing.

[Table of Contents](#Apache-Spark)

## What do you understand by lazy evaluation in Apache Spark?
As the name specifies, lazy evaluation in Apache Spark means that the execution will not start until an action is triggered. In Spark, the lazy evaluation comes into action when Spark transformations occur. Transformations are lazy. When a transformation such as a map() is called on an RDD, it is not performed instantly. Transformations in Spark are not evaluated until you perform an action, which aids in optimizing the overall data processing workflow, known as lazy evaluation. So we can say that in lazy evaluation, data is not loaded until it is necessary.

[Table of Contents](#Apache-Spark)

## What do you understand by Spark Driver?
Spark Driver is the program that runs on the master node of the machine and is used to declare transformations and actions on data RDDs.

[Table of Contents](#Apache-Spark)

## What is the Parquet file in Apache Spark?
Parquet is a column format file supported by many data processing systems. Spark SQL facilitates us to perform both read and write operations with the Parquet file.

[Table of Contents](#Apache-Spark)

## What is the way to store the data in Apache Spark?
Apache Spark is an open-source analytics and processing engine for large-scale data processing, but it does not have any storage engine. It can retrieve data from another storage engine like HDFS, S3.

[Table of Contents](#Apache-Spark)

## How is it possible to implement machine learning in Apache Spark?
Apache Spark itself provides a versatile machine learning library called MLif. By using this library, we can implement machine learning in Spark.

[Table of Contents](#Apache-Spark)

## What are some disadvantages or demerits of using Apache Spark?
Following is the list of some disadvantages or demerits of using Apache Spark:
Apache Spark requires more storage space than Hadoop and MapReduce, so that it may create some problems.
Apache Spark consumes a huge amount of data as compared to Hadoop.
Apache Spark requires more attentiveness because developers need to be careful while running their applications in Spark.
Spark runs on multiple clusters on different nodes instead of running everything on a single node. So, the work is distributed over multiple clusters.
The "in-memory" capability of Apache Spark makes it a more costly way for processing big data.

[Table of Contents](#Apache-Spark)

## What is the use of File system API in Apache Spark?
File system API is used to read data from various storage devices such as HDFS, S3 or Local Files.

[Table of Contents](#Apache-Spark)

## What are the tasks of a Spark Engine?
The main task of a Spark Engine is handling the process of scheduling, distributing and monitoring the data application across the clusters.

[Table of Contents](#Apache-Spark)

## What is the use of Apache SparkContext?
The SparkContent is the entry point to Apache Spark. SparkContext facilitates users to create RDDs, which provide various ways of churning data.

[Table of Contents](#Apache-Spark)

## Is it possible to do real-time processing with SparkSQL?
In SparkSQL, real-time data processing is not possible directly. We can register the existing RDD as a SQL table and trigger the SQL queries on priority.

[Table of Contents](#Apache-Spark)

## What is the use of Akka in Apache Spark?
Akka is used for scheduling in Apache Spark. Spark also uses Akka for messaging between the workers and masters.

[Table of Contents](#Apache-Spark)

## What do you understand by Spark map() Transformation?
Spark map() is a transformation operation used to apply the Transformation on every element of RDD, DataFrame, and Dataset and finally returns a new RDD/Dataset, respectively.

[Table of Contents](#Apache-Spark)

## What is the advantage of using the Parquet file?
In Apache Spark, the Parquet file is used to perform both read and write operations. Following is the list of some advantages of having a Parquet file:

Parquet file facilitates users to fetch specific columns for access.
It consumes less space.
It follows the type-specific encoding.
It supports limited I/O operations.

[Table of Contents](#Apache-Spark)

## What is the difference between persist() and cache() functions in Apache Spark?
In Apache Spark, the persist() function is used to allow the user to specify the storage level, whereas the cache() function uses the default storage level.

[Table of Contents](#Apache-Spark)

## Which Spark libraries allow reliable file sharing at memory speed across different cluster frameworks?
Tachyon is the Apache Spark library's name, which is used for reliable file sharing at memory speed across various cluster frameworks.

[Table of Contents](#Apache-Spark)

## What is shuffling in Apache Spark? When does it occur?
In Apache Spark, shuffling is the process of redistributing data across partitions that may lead to data movement across the executors. The implementation of shuffle operation is entirely different in Spark as compared to Hadoop.
Shuffling has two important compression parameters:
shuffle.compress: It is used to check whether the engine would compress shuffle outputs or not.
shuffle.spill.compress: It is used to decide whether to compress intermediate shuffle spill files or not.
Shuffling comes in the scene when we join two tables or perform byKey operations such as GroupByKey or ReduceByKey.

[Table of Contents](#Apache-Spark)

## What is the lineage in Spark?
In Apache Spark, when a transformation (map or filter etc.) is called, it is not executed by Spark immediately; instead, a lineage is created for each transformation. This lineage is used to keep track of what all transformations have to be applied on that RDD. It also traces the location from where it has to read the data.

[Table of Contents](#Apache-Spark)

## How can you trigger automatic clean-ups in Spark to handle accumulated metadata?
You can trigger the clean-ups by setting the parameter Spark.cleaner.ttl or dividing the long-running jobs into different batches and writing the intermediary results to the disk.

[Table of Contents](#Apache-Spark)

## Is it possible to launch Spark jobs inside Hadoop MapReduce?
Yes, you can run all kinds of spark jobs inside MapReduce without the need to obtain the admin rights of that application.

[Table of Contents](#Apache-Spark)

## What is the use of BlinkDB in Spark?
BlinkDB is a query engine tool used to execute SQL queries on massive volumes of data and renders query results in the meaningful error bars.

[Table of Contents](#Apache-Spark)