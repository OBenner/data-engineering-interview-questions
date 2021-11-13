# Apache Flink
+ [See you using Flink, briefly introduce Flink?](#See-you-using-Flink,-briefly-introduce-Flink)
+ [What are the differences between Flink and Spark Streaming?](#What-are-the-differences-between-Flink-and-Spark-Streaming)
+ [What are the Flink component stacks](#What-are-the-Flink-component-stack)
+ [Does Flink need to depend on Hadoop?](#Does-Flink-need-to-depend-on-Hadoop)
+ [How big is your FLink cluster?](#How-big-is-your-FLink-cluster)
+ [What is the Flink programming model?](#What-is-the-Flink-programming-model)
+ [What are the roles of Flink cluster? What are the functions?](#What-are-the-roles-of-Flink-cluster?-What-are-the-functions)
+ [What is TaskSolt?](#What-is-TaskSolt)
+ [What are the commonly used operators in Flink?](#What-are-the-commonly-used-operators-in-Flink)
+ [What is the parallelism of Flink and What is the parallelism setting of Flink?](#What-is-the-parallelism-of-Flink-and-What-is-the-parallelism-setting-of-Flink)
+ [What is the relationship between Flink's Solt and parallelism?](#What-is-the-relationship-between-Flink's-Solt-and-parallelism)
+ [What if Flink encounters an abnormal restart of the program?](#What-if-Flink-encounters-an-abnormal-restart-of-the-program)
+ [Flink's distributed cache](#Flink's-distributed-cach)
+ [Broadcast variables in Flink](#Broadcast-variables-in-Flin)
+ [Do you know what windows in Flink are?](#Do-you-know-what-windows-in-Flink-are)
+ [Flink's state storage?](#Flink's-state-storage)
+ [What kind of time are there in Flink?](#What-kind-of-time-are-there-in-Flink)
+ [What is Watermark in Flink?](#What-is-Watermark-in-Flink)
+ [What is Unbounded streams in Apache Flink?](#What-is-Unbounded-streams-in-Apache-Flink)
+ [Apache Flink Job Execution Architecture](#Apache-Flink-Job-Execution-Architectur)
+ [What is Bounded streams in Apache Flink?](#What-is-Bounded-streams-in-Apache-Flink)
+ [What is Dataset API in Apache Flink?](#What-is-Dataset-API-in-Apache-Flink)
+ [What is DataStream API in Apache Flink?](#What-is-DataStream-API-in-Apache-Flink)
+ [What is Apache Flink Table API?](#What-is-Apache-Flink-Table-API)
+ [What is Apache Flink FlinkML?](#What-is-Apache-Flink-FlinkML)
+ [What is Apache Flink?](#What-is-Apache-Flink)
+ [Explain Apache Flink Architecture?](#Explain-Apache-Flink-Architecture)
+ [Explain the Apache Flink Job Execution Architecture?](#Explain-the-Apache-Flink-Job-Execution-Architecture)
+ [What are the features of Apache Flink?](#What-are-the-features-of-Apache-Flink)
+ [What is Storage and Streaming in Apache Flink?](#What-is-Storage-and-Streaming-in-Apache-Flink)
+ [What is DataSet API?](#What-is-DataSet-API)
+ [What are the DSL Tool's in Flink?](#What-are-the-DSL-Tool's-in-Flink)
+ [What are the Apache Flink domain-specific libraries?](#What-are-the-Apache-Flink-domain-specific-libraries)
+ [What is the programing model of Apache Flink?](#What-is-the-programing-model-of-Apache-Flink)
+ [What are the different types of tools supported by Apache Flink?](#What-are-the-different-types-of-tools-supported-by-Apache-Flink)
+ [Can we consider Apache Flink as an alternative to Hadoop? if so then explain why?](#Can-we-consider-Apache-Flink-as-an-alternative-to-Hadoop?-if-so-then-explain-why)
+ [What are the use cases of Apache Flink?](#What-are-the-use-cases-of-Apache-Flink)
+ [What are the different ways to use Apache Flink?](#What-are-the-different-ways-to-use-Apache-Flink)
+ [What is the different component stack of Apache Flink?](#What-is-the-different-component-stack-of-Apache-Flink)
+ [What is the command to start Apache Flink Cluster?](#What-is-the-command-to-start-Apache-Flink-Cluster)
+ [What is the Apache Flink SQL client and how to start it?](#What-is-the-Apache-Flink-SQL-client-and-how-to-start-it)
+ [What are the SQL statements supported in Apache Flink?](#What-are-the-SQL-statements-supported-in-Apache-Flink)
+ [What is bounded and unbounded data in Apache Flink?](#What-is-bounded-and-unbounded-data-in-Apache-Flink)
+ [What is the building block of Apache Flink streaming applications?](#What-is-the-building-block-of-Apache-Flink-streaming-applications)
+ [What are the most common types of applications that use the Apache Flink?](#What-are-the-most-common-types-of-applications-that-use-the-Apache-Flink)
+ [What are the features of the Apache Flink execution Engine?](#What-are-the-features-of-the-Apache-Flink-execution-Engine)
+ [What is Apache FlinkML?](#What-is-Apache-FlinkML)
+ [How can I check the progress of an Apache Flink Program?](#How-can-I-check-the-progress-of-an-Apache-Flink-Program)
+ [How Apache Flink handles the fault-tolerance?](#How-Apache-Flink-handles-the-fault-tolerance)
+ [How to run an Apache Flink program using CLI mode?](#How-to-run-an-Apache-Flink-program-using-CLI-mode)
+ [What is the responsibility of JobManager in Apache Flink Cluster?](#What-is-the-responsibility-of-JobManager-in-Apache-Flink-Cluster)
+ [What is the responsibility of TaskManager in Apache Flink Cluster?](#What-is-the-responsibility-of-TaskManager-in-Apache-Flink-Cluster)
+ [What is the filesystem supported by Apache Flink?](#What-is-the-filesystem-supported-by-Apache-Flink)
+ [What is the difference between stream processing and batch processing?](#What-is-the-difference-between-stream-processing-and-batch-processing)
+ [What can I do with my state?](#What-can-I-do-with-my-state)
+ [Flink watermark Transmission mechanism.](#Flink-watermark-Transmission-mechanism)
+ [Flink The time semantics of?](#Flink-The-time-semantics-of)
+ [Flink window join:](#Flink-window-join)
+ [Flink What are the window functions:](#Flink-What-are-the-window-functions)
+ [keyedProcessFunction How it works](#keyedProcessFunction-How-it-work)
+ [How to deal with offline data such as the association with offline data?](#How-to-deal-with-offline-data-such-as-the-association-with-offline-data)
+ [ What if there is a data skew?](#What-if-there-is-a-data-skew)
+ [How to do dimension table Association?](#How-to-do-dimension-table-Association)
+ [Flink checkpoint The overtime problem of How to solve?](#Flink-checkpoint-The-overtime-problem-of-How-to-solve)
+ [FlinkTopN And offline TopN The difference between?](#FlinkTopN-And-offline-TopN-The-difference-between)
+ [Sparkstreaming and flink in checkpoint?](#Sparkstreaming-and-flink-in-checkpoint)
+ [A brief introduction cep State programming:](#A-brief-introduction-cep-State-programming)
+ [How to deal with abnormal data in Flink.](#How-to-deal-with-abnormal-data-in-Flink)
+ [Is there any possibility of data loss in Flink?](#Is-there-any-possibility-of-data-loss-in-Flink)
+ [At the time of submission How to make parallelism and how to allocate resources?](#At-the-time-of-submission-How-to-make-parallelism-and-how-to-allocate-resources)
+ [What's the common stream of API?](#What's-the-common-stream-of-API)
+ [How to maintain Checkpoint?](#How-to-maintain-Checkpoint)
+ [What's the difference at Spark and Flink Serialization?](#What's-the-difference-at-Spark-and-Flink-Serialization)
+ [ How to deal with late data?](#How-to-deal-with-late-data)
+ [ When to use aggregate perhaps process:](#When-to-use-aggregate-perhaps-process)

[Table of Contents](#Apache-Flink)

## See you using Flink, briefly introduce Flink?
   image-20200818110505537
Flink is a real-time computing framework. It and spark are both stream-batch integrated computing frameworks. Flink provides bounded stream and unbounded stream calculations. Bounded stream is actually the fact that flink considers data to be streaming for most cases, and batches are In a small part of the situation, that is to say, data that has a boundary is called a bounded flow, and data without a boundary is called an unbounded flow, which is data generated infinitely in real time.
The main external APIs of flink are DataSet API, DataStream API, Table API
Graph computing, machine learning. It provides two language interfaces: java, scala and python.

[Table of Contents](#Apache-Flink)

## What are the differences between Flink and Spark Streaming?
1. The design ideas are different. Flink considers batch to be a kind of streaming, and spark considers a streaming batch.
2. The architecture model is different. Spark has Driver, Master, Worker, and Executor. Flink has the concepts of TaskManager, JobManager, Task, SubTask, and Slot
3. Flink's streaming data processing is much stronger than spark, for example, time supports three kinds of time
There are more windows than spark
4. In the case of out-of-order data, Flink is stronger than spark, because flink has watermark. In fact, the calculation method when running is the time of the last data-if watermaker is greater than the end of the window, execute
5. For fault tolerance, flink is also better than spark. For example, flink supports two-stage transactions to ensure that data after program crashes will not be re-consumed. Spark also has checkpoints, but it only ensures that data is not lost, and it cannot be repeated. consumption.

[Table of Contents](#Apache-Flink)

## What are the Flink component stacks
   image-20200818111027643
1. The deployment mode can be Local, Cluster, Cloud
2. Then perform all basic services based on Runtime components
3. The upper layer provides DataStream API and DataSet API
4. At the high-level, there are Table API, CEP complex family care, ML machine learning, graph computing

[Table of Contents](#Apache-Flink)

## Does Flink need to depend on Hadoop?
Flink can be completely independent of Hadoop and run without relying on Hadoop components, but as the basis of big data, it is conceivable that most big data frameworks cannot bypass it. Flink can support many components, such as Yarn's resource scheduling, Hbase's real-time data storage and dimensional table access, HDFS state storage and offline computing, and so on.

[Table of Contents](#Apache-Flink)

## How big is your FLink cluster?
This can be done according to the situation of your own company. Most companies use the yarn mode of deployment. Of course, yarn also has multiple modes of deployment, such as a single job or directly apply for a large amount of resources in yarn to be responsible. Job submission, most companies choose, should be single job mode.

[Table of Contents](#Apache-Flink)

## What is the Flink programming model?
In fact, in one sentence,Source->Transformation->Sink*

[Table of Contents](#Apache-Flink)

## What are the roles of Flink cluster? What are the functions?
image-20200818131352139
Flink programs mainly have three roles: TaskManager, JobManager, and Client when they are running.
JobManager In the role of a manager in the cluster, it is the coordinator of the entire cluster. It is responsible for receiving the execution of Flink Job, coordinating checkpoints, recovering from failures, and managing Task Manager.
TaskManager It is responsible for the resource information on the node where the manager is located, such as memory, disk, and network. It will report the resource to the JobManager when it is started.
Client It is the client submitted by the Flink program. When a user submits a Flink program, a Client is first created. Then the program submitted by the user will be preprocessed and submitted to the cluster for processing.

[Table of Contents](#Apache-Flink)

## What is TaskSolt?
   image-20200818133034389
In Flink's architecture, TaskManager is the working node that is actually used to execute our program. TaskManager is a JVM process. In fact, in order to achieve the concept of resource isolation and parallel execution, the concept of TaskSlot was proposed at this time, which is actually In order to control how many Tasks the TaskManager can receive, the TaskManager is controlled by tasksolt, that is, if we have a source that specifies three parallelism, then he will use three solts, and the other one needs to be mainly parallel as an operator When the degree is the same, and there is no change in the degree of parallelism, or there is no shuffle, they will be together at this time. This is an optimized concept.

[Table of Contents](#Apache-Flink)

## What are the commonly used operators in Flink?
Map operator
Filter operator
KeyBy operator
Window window

[Table of Contents](#Apache-Flink)

## What is the parallelism of Flink and What is the parallelism setting of Flink?
In fact, the parallelism of Flink is well understood. For example, kafkaSource, its parallelism is the number of partitions by default. The degree of parallelism is this operator, and how many tasksolt are needed, we should know that is the advantage of parallel computing. Generally, the degree of parallelism is set according to the amount of data. It is best to keep the source and map operators without shuffle, because the pressure on the source and map operators is not very large, but when our data table is widened, It is better to set it larger.

[Table of Contents](#Apache-Flink)

## What is the relationship between Flink's Solt and parallelism?
Solt is a concept in TaskManager. Parallelism is a concept in the program, that is, the concept of execution level. In fact, Solt specifies how many slots this TaskManager has and how much parallelism can be supported, but the parallelism developed by the program uses slots That is Solt, that is, TaskManager is the provider and the program is the user

[Table of Contents](#Apache-Flink)

## What if Flink encounters an abnormal restart of the program?
Flink has some restart strategies, and as long as the checkpoint is done, it can be done at least once. Of course, it may not be accurate once, but some components can be done. The restart strategy generally set is a fixed delay restart strategy. The restart does not delete the checkpoint. Generally, the number of restarts set by our company is 4 times. If it stops, we will send a nail warning and start from the checkpoint when it starts.

[Table of Contents](#Apache-Flink)

## Flink's distributed cache
The distributed cache implemented by Flink is similar to Hadoop. The purpose is to read the file locally and put it in the taskmanager node to prevent the task from repeatedly pulling data and reduce performance.

[Table of Contents](#Apache-Flink)

## Broadcast variables in Flink
We know that Flink is parallel, and the calculation process may not be performed in a Slot. Then there is a situation: when we need to access the same data. Then the broadcast variable in Flink is to solve this situation. We can understand the broadcast variable as a public shared variable. We can broadcast a dataset, and then different tasks can be obtained on the node. There will only be one copy of this data on each node.

[Table of Contents](#Apache-Flink)

## Do you know what windows in Flink are?
Flink supports two ways to divide windows, according to time and count. session is also a kind of time
Tumbing Count Window： Perform calculation when reaching a certain number, no folding
Sliding Time Window： When a certain period of time is reached, roll over, there can be overlap, generally used to calculate the recent demand, such as nearly 5 minutes.
Tumbing time Window： When a certain period of time is reached, the slide is carried out, which can be thought of as the Nokia slide phone used before. This is actually a micro batch
Sliding Count Window： Slide when it reaches a certain number
Session Window: The window data has no fixed size, it is divided according to the parameters passed in by the user, and the window data does not overlap. It is similar to calculating the user's previous actions when the user logs out.

[Table of Contents](#Apache-Flink)

## Flink's state storage?
Flink often needs to store intermediate states during calculations to avoid data loss and recover from abnormal states. Choosing a different state storage strategy will affect the state interaction between JobManager and Subtask, that is, JobManager will interact with State to store state.
Flink provides three state storage:
MemoryStateBackend
FsSateBackend
RocksDBStateBackend

[Table of Contents](#Apache-Flink)

## What kind of time are there in Flink?
Event time: the time when the event actually occurred
Intake time: time to enter flink
Processing time: the time to enter the flink operator

[Table of Contents](#Apache-Flink)

## What is Watermark in Flink?
Watermark is an operation used by Flink to deal with out-of-order time. In fact, in Flink, if we use event time and take kafka's source, then the window execution time at this time is the smallest among the partitions Partitions are used for triggering, and each partition must be triggered to perform calculations. Why is this? In fact, it is because the partitions of Kafka are disordered. Orderly in the zone. The execution time is the maximum time minus the watermark>window end time, and the calculation will be executed at this time.

[Table of Contents](#Apache-Flink)

## What is Unbounded streams in Apache Flink?
Any type of data is produced as a stream of events. Data can be processed as unbounded or bounded streams.
Unbounded streams have a beginning but no end. They do not end and continue to provide data as it is produced. Unbounded streams should be processed continuously, i.e., events should be handled as soon as they are consumed. Since the input is unbounded and will not be complete at any point in time, it is not possible to wait for all of the data to arrive.

[Table of Contents](#Apache-Flink)

## Apache Flink Job Execution Architecture
Processing unbounded data sometimes requires that events are consuming in a specific order, such as the order in which events arrives, to be able to reason about result completeness.

[Table of Contents](#Apache-Flink)

## What is Bounded streams in Apache Flink?
Bounded streams have a beginning and an end point. Bounded streams could be processed by consuming all data before doing any computations. Ordered ingestion is not needed to process bounded streams since a bounded data set could always be sorted. Processing of bounded streams is also called as batch processing.

[Table of Contents](#Apache-Flink)

## What is Dataset API in Apache Flink?
The Apache Flink Dataset API is used to do batch operations on data over time. This API is available in Java, Scala, and Python. It may perform various transformations on datasets such as filtering, mapping, aggregating, joining, and grouping.
DataSet<Tuple2<String, Integer>> wordCounts = text
.flatMap(new LineSplitter())
.groupBy(0)
.sum(1);

[Table of Contents](#Apache-Flink)

## What is DataStream API in Apache Flink?
The Apache Flink DataStream API is used to handle data in a continuous stream. On the stream data, you can perform operations such as filtering, routing, windowing, and aggregation. On this data stream, there are different sources such as message queues, files, and socket streams, and the resulting data can be written to different sinks such as command line terminals. This API is supported by the Java and Scala programming languages.

DataStream<Tuple2<String, Integer>> dataStream = env
.socketTextStream("localhost", 9091)
.flatMap(new Splitter())
.keyBy(0)
.timeWindow(Time.seconds(7))
.sum(1);

[Table of Contents](#Apache-Flink)

## What is Apache Flink Table API?
Table API is a relational API with an expression language similar to SQL. This API is capable of batch and stream processing. It is compatible with the Java and Scala Dataset and Datastream APIs. Tables can be generated from internal Datasets and Datastreams as well as from external data sources. You can use this relational API to perform operations such as join, select, aggregate, and filter. The semantics of the query are the same if the input is batch or stream.
val tableEnvironment = TableEnvironment.getTableEnvironment(env)
// register a Table
tableEnvironment.registerTable("TestTable1", ...);
// create a new Table from a Table API query
val newTable2 = tableEnvironment.scan(TestTable1).select(...);

[Table of Contents](#Apache-Flink)

## What is Apache Flink FlinkML?
FlinkML is the Flink Machine Learning (ML) library. It is a new initiative in the Flink community, with an expanding list of algorithms and contributors. FlinkML aims to include scalable ML algorithms, an easy-to-use API, and tools to help reduce glue code in end-to-end ML systems. Note: Flink Community has planned to delete/deprecate the legacy flink-libraries/flink-ml package in Flink1.9, and replace it with the new flink-ml interface proposed in FLIP39 and FLINK-12470.

[Table of Contents](#Apache-Flink)

## What is Apache Flink?
The Apache Software Foundation created Apache Flink, an open-source, unified stream-processing and batch-processing framework. Apache Flink is built around a distributed streaming data-flow engine written in Java and Scala. Flink runs every dataflow programm in a data-parallel and pipelined fashion.

[Table of Contents](#Apache-Flink)

## Explain Apache Flink Architecture?
Apache Flink is based on the Kappa architecture. The Kappa architecture uses a single processor - stream, who accepts all information as a stream, and the streaming engine processes data in real-time. Batch data in kappa architecture is a form of streaming data.
Apache Flink Architecture
The majority of big data frameworks are built on the Lambda architecture, which uses different processors for batch and streaming data. In Lambda architecture, batch and stream views have different codebases. The codebases must be combined in order to query and retrieve the results. Maintaining different codebases/views and combining them is a hassle, but the Kappa architecture fixes this problem by having only one real-time view, which eliminates the need for codebase merging.
The core principle of the Kappa architecture is to manage batch and real-time data via a single stream processing engine.
That is not to say that Kappa architecture is preferred to Lambda architecture; it is entirely dependent on the use-case and application to determine which architecture is optimal.

[Table of Contents](#Apache-Flink)

## Explain the Apache Flink Job Execution Architecture?
The Apache Flink job execution architecture is shown in the diagram below.Apache Flink Job Execution Architecture
Program
It is a piece of code that is executed on the Flink Cluster.
Client
It is in charge of taking code from the given programm and creating a job dataflow graph, which is then passed to JobManager. It also retrieves the Job data.
JobManager
It is responsible for generating the execution graph after obtaining the Job Dataflow Graph from the Client. It assigns the job to TaskManagers in the cluster and monitors its execution.
TaskManager
It is in charge of executing all of the tasks assigned to it by JobManager. Both TaskManagers execute the tasks in their respective slots in the specified parallelism. It is in charge of informing JobManager about the status of the tasks.

[Table of Contents](#Apache-Flink)

## What are the features of Apache Flink?
Flink uses common runtime for data streaming applications and batch processing applications.
It can run both Batch and Stream programs.
Provides APIs.
It has lightning fast speed.
Can process data in low latency.
It can easily integrate with big data tools like Apache Hadoop, Apache MapReduce, etc.
It is highly scalable.
It acts as a Fault tolerent.

[Table of Contents](#Apache-Flink)

## What is Storage and Streaming in Apache Flink?
Flink compose various capacity framework and can devour information from gushing frameworks.The following gushing framework, flink can persue compose information like:
FLume - Acts as an Aggregation Tool
HBase - Acts like NoSQL Databse in a Hadoop ecosystem
HDFS - Helps as Hadoop Distributed File System
Kafka - Helps in distributing messaging queue
RabbitMQ - Acts as a Messaging queue
S3 - It is Simple Storage Service from Amazon

[Table of Contents](#Apache-Flink)

## What is DataSet API?
DataSet API helps us in enabling the client to actualize activities like a guide, channel, gathering and so on.It is utilized for appropriated preparing, it is an uncommon instance of stream preparing where we have a limited information source.They are regular programs that implement transformation on data sets like filtering, mapping, etc.
Data sets are created from sources like reading files, local collections, etc.All the results are returned through sinks, the execution can happen in a local JVM or on clusters of many machines.

[Table of Contents](#Apache-Flink)

## What are the DSL Tool's in Flink?
There are 3 types of DSL tools:
Table - Its is implanted in DataSet and DataStream API.As it helps in performing impromptu investigation utilizing SQL like articulation languague for preparing bunch and social strem.
Gelly - It enables clients to run a set of tasks and change the procedure of the diagram.
FlinkML - It is composed in Scala.It gives instinctive APIs and proficient calculation to deal with applications.

[Table of Contents](#Apache-Flink)

## What are the Apache Flink domain-specific libraries?
The following is the list of Apache Flink domain-specific libraries.
FlinkML: It is used for machine learning.
Table: It is used to perform the relational operation.
Gelly: It is used to perform the Graph operation.
CEP: It is used for complex event processing.

[Table of Contents](#Apache-Flink)

## What is the programing model of Apache Flink?
The Apache Flink Datastream and the Dataset work as a programming model of flink and its other layers of architecture. The Datastream programming model is useful in real-time stream processing whereas the Dataset programming model is useful in batch processing.

[Table of Contents](#Apache-Flink)

## What are the different types of tools supported by Apache Flink?
Apache Flink supports the below list of tools.
CLI(Command Line Interface
Apache Flink Dashboard
Apache Flink SQL Client
Scala Shell

[Table of Contents](#Apache-Flink)

## Can we consider Apache Flink as an alternative to Hadoop? if so then explain why?
Apache Flink provides more features and flexibility comparing to Hadoop because it uses the cycle dataflow programming model despite Mapreduce which is a two-stage disk storage model, Flink programs can work in memory and can be used with other filesystems apart from Hadoop. Flink provides the unified framework using that we can create a single data flow that will use batch, streaming, machine learning, and SQL queries.

[Table of Contents](#Apache-Flink)

## What are the use cases of Apache Flink?
Many real-world industries are using Apache Flink and their use cases are as mentioned below.

Financial Services
Financial industries are using Flink to perform fraud detection in real-time and send mobile notifications.

Healthcare
The hospitals are using Apache Flink to collect data from devices such as MRI, IVs for real-time issue detection and analysis.

Ad Tech
Ads companies are using Flink to find out the real-time customer preference.

Oil Gas
The Oil and Gas industries are using Flink for real-time monitoring of pumping and issue detection.

Telecommunications
The telecom companies are using Apache Flink to provide the best services to the users such as real-time view of billing and payment, the optimization of antenna per-user location, mobile offers, and so on.

[Table of Contents](#Apache-Flink)

## What are the different ways to use Apache Flink?
Apache Flink can be deployed and configured in the below ways.
Flink can be setup Locally (Single Machine)
It can be deployed on a VM machine.
We can use Flink as a Docker image.
We can configure and deploy Flink as a standalone cluster.
Flink can be deployed and configured on Hadoop YARN and another resource managing framework.
Flink can be deployed and configured on a Cloud system.

[Table of Contents](#Apache-Flink)

## What is the different component stack of Apache Flink?
Apache Flink has a stack of components such as at storage level it supports different types of file such as HDFS, local file system, it also supports the database like HBase, MongoDB. Flink can be deployed in the standalone mode, cluster mode, and on the cloud system. It provides the dataset API for batch processing and the datastream API for stream processing also supports SQL, machine learning, and graph processing.

[Table of Contents](#Apache-Flink)

## What is the command to start Apache Flink Cluster?
We can use the following command to start the Apache Flink Cluster.
cloudduggu@ubuntu:~/flink$ ./bin/start-cluster.sh

[Table of Contents](#Apache-Flink)

## What is the Apache Flink SQL client and how to start it?
Apache Flink SQL client provides a command-line interface to run SQL operations such as create a table, drop table, create a view, drop the view, and other SQL commands as well.
We can start the SQL client using the below command.
cloudduggu@ubuntu:~/flink/bin$ ./start-cluster.sh
cloudduggu@ubuntu:~/flink$ ./bin/sql-client.sh embedded

[Table of Contents](#Apache-Flink)

## What are the SQL statements supported in Apache Flink?
Apache Flink SQL supports the below list of statements.
SELECT query
CREATE TABLE, CREATE DATABASE, CREATE VIEW, CREATE FUNCTION
DROP TABLE, DROP DATABASE, DROP VIEW, DROP FUNCTION
ALTER TABLE, ALTER DATABASE, ALTER FUNCTION
INSERT TABLE
SQL HINTS
DESCRIBE
EXPLAIN
USE
SHOW

[Table of Contents](#Apache-Flink)

## What is bounded and unbounded data in Apache Flink?
Apache Flink processes data in the form of bounded and unbounded streams. The bounded data will have a start point and an endpoint and the computation starts once all data has arrived. It is also called batch processing. The unbounded data will have a start point but no endpoint because it is streaming of data. The processing of unbounded data is continous and doesn't wait for complete data. As soon the data is generated the processing will start.

[Table of Contents](#Apache-Flink)

## What is the building block of Apache Flink streaming applications?
The applications which are executed on the Apache Flink cluster are defined by the following three building blocks for stream processing.
Streams
State
Time

[Table of Contents](#Apache-Flink)

## What are the most common types of applications that use the Apache Flink?
The most common types of applications that use Apache Flinks are as below.

[Table of Contents](#Apache-Flink)

Event-driven applications such as Fraud Detection, Anomaly detection, rule-based alerting, and so on.
Data Analytics Applications such as a quality check of telecommunication companies, mobile applications product analysis, and so on.
Data Pipeline Applications such as the index building for e-commerce.

[Table of Contents](#Apache-Flink)

## What are the features of the Apache Flink execution Engine?
The core of the Apache Flink architecture is the robust, distributed, dataflow engine that performs execution as a stream using cycle dataflow execution. It provides the cost-based optimization for batch and stream programs for optimum processing and able to work in distributed memory.

[Table of Contents](#Apache-Flink)

## What is Apache FlinkML?
Apache FlinkML is the machine learning library that provides APIs and scalable algorithms to perform the machine learning operations. FlinkML helps developers to reduce the Glue codes and test the code locally. The same code can be used by the developer to run on a cluster of the machine. Some of the algorithms of FlinkML are Supervised Learning, Unsupervised Learning, Data Preprocessing, and so on.

[Table of Contents](#Apache-Flink)

## How can I check the progress of an Apache Flink Program?
The best way to track the progress of the Flink program is the Apache Flink Dashboard web interface. It shows the jobs which are in running such as its state the resources allocated for that job and so on. We can start the Apache Flink Dashboard using "http://localhost:8081/".

[Table of Contents](#Apache-Flink)

## How Apache Flink handles the fault-tolerance?
Apache Flink manages the fault-tolerance of stream applications by capturing the snapshot of the streaming dataflow state so in case of failure those snapshots will be used for recovery. For batch processing, Flink uses the program’s sequence of transformations for recovery.

[Table of Contents](#Apache-Flink)

## How to run an Apache Flink program using CLI mode?
We can use Apache Flink CLI(command-line interface) tool to run the programs which are built as JAR files.
For example, we can run a "WordCounts.jar" JAR file using the below command.
cloudduggu@ubuntu:~/flink$ ./bin/flink run ./examples/batch/WordCounts.jar

[Table of Contents](#Apache-Flink)

## What is the responsibility of JobManager in Apache Flink Cluster?
The Job Manager is responsible for managing and coordinating with distributed processing of a program. It assigns the task to node managers, handles the failures for recovery, and performs the checkpointing. It has three components namely ResourceManager, Dispatcher, and JobMaster.

[Table of Contents](#Apache-Flink)

## What is the responsibility of TaskManager in Apache Flink Cluster?
The Task Manager is responsible for executing the dataflow task and return the result to JobManager. It executes the task in the form of a slot hence the number of slots shows the number of process execution.

[Table of Contents](#Apache-Flink)

## What is the filesystem supported by Apache Flink?
Apache Flink supports the following list of the filesystem.
local filesystem
Hadoop HDFS
Amazon S3
MapR FS
OpenStack Swift FS
Aliyun OSS
Azure Blob Storage

[Table of Contents](#Apache-Flink)

## What is the difference between stream processing and batch processing?
In Batch processing, the data is a bounded set of the stream that has a start point and the endpoint, so once the entire data is ingested then only processing starts in batch processing mode. In-stream processing the nature of data is unbounded which means the processing will continue as the data will be received.
Flink How to ensure accurate one-time consumption
Flink There are two ways to ensure accurate one-time consumption Flink Mechanism
1、Checkpoint Mechanism
2、 Two stage submission mechanism
Checkpoint Mechanism
Mainly when Flink Turn on Checkpoint When , Will turn out for the Source Insert a barrir, And then this barrir As the data flows all the time , When it comes to an operator , This operator starts to make checkpoint, It's made from barrir The state of the current operator when it comes to the previous time , Write the state to the state backend . And then barrir Flow down , When it flows to keyby perhaps shuffle Operator time , For example, when the data of an operator , Depending on multiple streams , There will be barrir alignment , That is, when all barrir All come to this operator to make checkpoint, Flow in turn , When it flows to sink Operator time , also sink The operator is also finished checkpoint Will send to jobmanager The report checkpoint n Production complete .
Two stage submission mechanism
Flink Provides CheckpointedFunction And CheckpointListener These two interfaces ,CheckpointedFunction There is snapshotState Method , Every time checkpoint Trigger execution method , The cache data is usually put into the State , You can think of it as one hook, This method can be used to achieve pre submission ,CheckpointListyener There is notifyCheckpointComplete Method ,checkpoint Notification method after completion , There are some extra operations that can be done here . for example FLinkKafkaConumerBase Use this to do Kafka offset Submission of , In this method, you can implement the submit operation . stay 2PC If the corresponding process, such as a checkpoint Failure words , that checkpoint It will roll back , No impact on data consistency , So if you're informing checkpoint Success followed by failure , Then it will be in initalizeSate Method to complete the transaction commit , This ensures data consistency . It's mainly based on checkpoint The state file to judge .
flink and spark difference
flink It's a similar spark Of “ Open source technology stack ”, Because it also provides batch processing , Flow computation , Figure calculation , Interactive query , Machine learning, etc .flink It's also memory computing , similar spark, But the difference is ,spark The calculation model of is based on RDD, Consider streaming as a special batch process , His DStream In fact, or RDD. and flink Consider batch processing as a special stream computing , But there are two engines in the layer of batch processing and streaming computing , Abstract the DataSet and DataStream.flink It's also very good in performance , Streaming delay ratio spark Less , Can do real flow computing , and spark It can only be a quasi flow calculation . And in batch processing , When the number of iterations gets more ,flink Faster than spark faster , So if flink Come out earlier , Maybe more than what we have now Spark More fire .

[Table of Contents](#Apache-Flink)

## What can I do with my state?
Flink There are two main ways to use state ：
checkpoint Data recovery
Logical computing

[Table of Contents](#Apache-Flink)

## Flink watermark Transmission mechanism.
Flink Medium watermark Mechanism is used to deal with disorder ,flink It has to be event time , A simple example is , If the window is 5 second ,watermark yes 2 second , that All in all 7 second , When will calculation be triggered at this time , Suppose the initial time of the data is 1000, Then wait until 6999 It will trigger 5999 The calculation of windows , So the next one is 13999 Is triggered when 10999 The window of
In fact, this is watermark The mechanism of , In multi parallelism , For example, in kafka The window will not be triggered until all partitions are reached

[Table of Contents](#Apache-Flink)

## Flink The time semantics of?
Event Time Time of occurrence
Ingestion time Events enter Flink Time for
processing time The time that the event enters the operator

[Table of Contents](#Apache-Flink)

## Flink window join:
1、window join, That is, according to the specified fields and scrolling sliding window and session window inner join
2、 yes coGoup In fact, that is left join and right join,
3、interval join That is to say In the window join There are some problems , Because some of the data really came after the meeting , It's still a long time , Then there will be interval join But it has to be the time of the event , And also specify watermark And water level and getting event timestamps . And set it up Offset interval , because join I can't wait all the time .

[Table of Contents](#Apache-Flink)

## Flink What are the window functions:
Tumbing window
Silding window
Session window
Count winodw

[Table of Contents](#Apache-Flink)

## keyedProcessFunction How it works
keyedProcessFunction There is one ontime Operation of the , If so event In time that The time to call is to look at ,event Of watermark Is it greater than trigger time Time for , If it is greater than, calculate it , No, just wait , If it is kafka Words , Then the default is to trigger the partition key in the shortest time .

[Table of Contents](#Apache-Flink)

## How to deal with offline data such as the association with offline data?
1、async io
2、broadcast
3、async io + cache
4、open Method , Then the thread is refreshed at a fixed time , Cache updates are deleted first , Then write another one, and then write to the cache

[Table of Contents](#Apache-Flink)

##  What if there is a data skew?
Flink How to view data skew ：
stay flink Of web ui You can see the data skew in , It's every one subtask The amount of data processed varies greatly , For example, some have only one M yes , we have 100M This is a serious data skew .
KafkaSource Data skew at the end
For example, upstream kafka It was specified when it was sent key There are data hotspots , So just after the access , Do a load balancing （ The premise is not keyby）.
Aggregation class operator data skew
Pre aggregation plus global aggregation

[Table of Contents](#Apache-Flink)

## How to do dimension table Association?
1、async io
2、broadcast
3、async io + cache
4、open Method , Then the thread is refreshed at a fixed time , Cache updates are deleted first , Then write another one, and then write to the cache

[Table of Contents](#Apache-Flink)

## Flink checkpoint The overtime problem of How to solve?
1、 Is there a network problem
2、 Whether it is barrir problem
3、 see webui, Whether there is data skew
4、 If there's a data skew , So after solving the data skew , There will be improvements ,

[Table of Contents](#Apache-Flink)

## FlinkTopN And offline TopN The difference between?
topn It is a common function in both offline and real-time computing , It's different from... In offline computing topn, Real time data is continuous , This will give topn It's very difficult to calculate , Because it's going to keep a... In memory topn Data structure of , When new data comes , Update this data structure

[Table of Contents](#Apache-Flink)

## Sparkstreaming and flink in checkpoint?
sparkstreaming Of checkpoint It will lead to repeated consumption of data
however flink Of checkpoint Sure Make sure it's accurate one time , At the same time, it can be incremental , fast checkpoint Of , There are three states ,memery、rocksdb、hdfs

[Table of Contents](#Apache-Flink)

## A brief introduction cep State programming:
Complex Event Processing（CEP）：
FLink Cep Is in FLink Complex time processing library implemented in ,CEP Allows event patterns to be detected in an endless stream of time , Give us a chance to grasp the important parts of the data , One or more time streams composed of simple events are matched by certain rules , Then output the data the user wants , That is, complex events that satisfy the rules .
Flink Data aggregation in , How to aggregate without windows
valueState Used to save a single value
ListState Used to hold list Elements
MapState Used to save a set of key value pairs
ReducingState Provided with ListState Same method , Return to one ReducingFunction The aggregated value .
AggregatingState and ReducingState similar , Return to one AggregatingState The value after internal aggregation

[Table of Contents](#Apache-Flink)

## How to deal with abnormal data in Flink.
Abnormal data in our scenario , It is generally divided into missing fields and outlier data .
outliers ： For example, data on the age of the baby , For example, for the maternal and infant industry , The age of a baby is a crucial data , It's the most important , Because the baby is bigger than 3 At the age of 20, you hardly buy things from mothers and babies . There are days like ours 、 Unknown 、 And for a long time . This is an exception field , We will show the data to store managers and regional managers , Let them know how many ages are not allowed . If we have to deal with it , It can be corrected in real time according to the time of purchase , For example, maternity clothing 、 The rank of milk powder 、 The size of a diaper , As well as pacifiers, some can distinguish the age group to carry on the processing . We don't process the data in real time , We're going to have a low-level strategy task, night dimension, to run , Run once a week .
Missing field ： For example, some fields are really missing , If you can fix it, you can fix it . Give up if you can't fix it , It's like the news recommendation filter in the last company .

[Table of Contents](#Apache-Flink)

## Is there any possibility of data loss in Flink?
Flink There are three kinds of data consumption semantics ：
At Most Once One consumption at most In case of failure, it may be lost
At Least Once At least once If there is a fault, it may be repeated
Exactly-Once Exactly once If something goes wrong , It can also ensure that the data will not be lost or repeated .
flink The new version is no longer available At-Most-Once semantics .

Flink interval join Can you write it simply
DataStream<T> keyed1 = ds1.keyBy(o -> o.getString("key"))
DataStream<T> keyed2 = ds2.keyBy(o -> o.getString("key"))
// Time stamp on the right -5s<= Stream timestamp on the left <= Time stamp on the right -1s
keyed1.intervalJoin(keyed2).between(Time.milliseconds(-5), Time.milliseconds(5))

[Table of Contents](#Apache-Flink)

## At the time of submission How to make parallelism and how to allocate resources?
Parallelism based on kafka topic Parallelism of , A degree of parallelism 3 individual G

[Table of Contents](#Apache-Flink)

## What's the common stream of API?
window join ah cogroup ah map flatmap,async io etc.

[Table of Contents](#Apache-Flink)

## How to maintain Checkpoint?
By default , If set Checkpoint Options ,Flink Only the most recently generated 1 individual Checkpoint. When Flink When the program fails , From the nearest one Checkpoint To recover . however , If we want to keep more than one Checkpoint, And can choose one of them to recover according to the actual needs , It's more flexible .Flink Support to keep multiple Checkpoint, Need to be in Flink Configuration file for conf/flink-conf.yaml in , Add the following configuration to specify that at most Checkpoint The number of .
For small files, please refer to The death of Daedalus - Solutions to the problem of small files in the field of big data .

[Table of Contents](#Apache-Flink)

## What's the difference at Spark and Flink Serialization?
Spark The default is Java Serialization mechanism , At the same time, there is an optimization mechanism , That is to say kryo
Flink It's a self implemented serialization mechanism , That is to say TypeInformation

[Table of Contents](#Apache-Flink)

##  How to deal with late data?
Flink Of watermark It's a delayed trigger mechanism .
commonly watermark Is and window To process out of order data ,Watermark The most fundamental is a time mechanism , For example, I set the maximum out of order time to 2s, The window time is 5 second , So when the event time is greater than 7s The window will be triggered when the window is opened . Of course, if there are data partitions , for example kafka Medium access watermake Words , that watermake It will flow , Take the smallest of all partitions watermake To flow , Because only the smallest can guarantee , All the previous data has come to , You can trigger the calculation .
use flink Can replace spark Batch processing function of
Flink The future goal is to integrate batch and stream processing , Because the batch data set you can understand is a limited data stream .Flink In terms of approval management , Especially this year Flink 1.9 Release after , Join in a large number of Hive Function of aspect , You can use Flink SQL To read Hive Metadata and datasets in , And use Flink SQL It is logically processed , But so far Flink Performance in batch processing , I can't do it Spark Of .
So far ,Flink There is still a lot to do in batch processing , Of course , If it's the introduction of real-time computing engine ,Flink Of course, it's the first choice .

[Table of Contents](#Apache-Flink)

##  When to use aggregate perhaps process:
aggregate： Incremental aggregation
process： Total polymerization
When calculating the accumulation operation, you can use aggregate operation .
When calculating the full amount of data in the window, use process, For example, sorting and other operations.

[Table of Contents](#Apache-Flink)

