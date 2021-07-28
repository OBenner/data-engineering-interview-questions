Question 1. What Is Flume?

Answer :

Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data. It has a simple and flexible architecture based on streaming data flows. It is robust and fault tolerant with tunable reliability mechanisms and many fail over and recovery mechanisms. It uses a simple extensible data model that allows for online analytic application.

Question 2. What Is Apache Flume?

Answer :

Apache Flume is a distributed, reliable, and available system for efficiently collecting, aggregating and moving large amounts of log data from many different sources to a centralized data source. Review this Flume use case to learn how Mozilla collects and Analyse the Logs using Flume and Hive.

Flume is a framework for populating Hadoop with data. Agents are populated throughout ones IT infrastructure – inside web servers, application servers and mobile devices, for example – to collect data and integrate it into Hadoop.

Apache Tapestry Interview Questions
Question 3. Which Is The Reliable Channel In Flume To Ensure That There Is No Data Loss?

Answer :

FILE Channel is the most reliable channel among the 3 channels JDBC, FILE and MEMORY.

Question 4. How Can Flume Be Used With Hbase?

Answer :

Apache Flume can be used with HBase using one of the two HBase links:

HBaseSink (org.apache.flume.sink.hbase.HBaseSink) supports secure HBase clusters and also the novel HBase IPC that was introduced in the version HBase 0.96.
AsyncHBaseSink (org.apache.flume.sink.hbase.AsyncHBaseSink) has better performance than HBase sink as it can easily make non-blocking calls to HBase.
Working of the HBaseSink:

In HBaseSink, a Flume Event is converted into HBase Increments or Puts. Serializer implements the HBaseEventSerializer which is then instantiated when the sink starts. For every event, sink calls the initialize method in the serializer which then translates the Flume Event into HBase increments and puts to be sent to HBase cluster.

Working of the AsyncHBaseSink:

AsyncHBaseSink implements the AsyncHBaseEventSerializer. The initialize method is called only once by the sink when it starts. Sink invokes the setEvent method and then makes calls to the getIncrements and getActions methods just similar to HBase sink. When the sink stops, the cleanUp method is called by the serializer.



Apache Tapestry Tutorial
Question 5. What Is An Agent?

Answer :

A process that hosts flume components such as sources, channels and sinks, and thus has the ability to receive, store and forward events to their destination.

Apache Cassandra Interview Questions
Question 6. Is It Possible To Leverage Real Time Analysis On The Big Data Collected By Flume Directly? If Yes, Then Explain How?

Answer :

Data from Flume can be extracted, transformed and loaded in real-time into Apache Solr servers usingMorphlineSolrSink.

Question 7. What Is A Channel?

Answer :

It stores events,events are delivered to the channel via sources operating within the agent.An event stays in the channel until a sink removes it for further transport.

Apache Cassandra Tutorial Apache Spark Interview Questions
Question 8. Explain About The Different Channel Types In Flume. Which Channel Type Is Faster?

Answer :

The 3 different built in channel types available in Flume are:

MEMORY Channel – Events are read from the source into memory and passed to the sink.
JDBC Channel – JDBC Channel stores the events in an embedded Derby database.
FILE Channel –File Channel writes the contents to a file on the file system after reading the event from a source. The file is deleted only after the contents are successfully delivered to the sink.
MEMORY Channel is the fastest channel among the three however has the risk of data loss. The channel that you choose completely depends on the nature of the big data application and the value of each event.

Question 9. Explain About The Replication And Multiplexing Selectors In Flume?

Answer :

Channel Selectors are used to handle multiple channels. Based on the Flume header value, an event can be written just to a single channel or to multiple channels. If a channel selector is not specified to the source then by default it is the Replicating selector. Using the replicating selector, the same event is written to all the channels in the source’s channels list. Multiplexing channel selector is used when the application has to send different events to different channels.

Apache Solr Interview Questions
Question 10. Does Apache Flume Provide Support For Third Party Plug-ins?

Answer :

Most of the data analysts use Apache Flume has plug-in based architecture as it can load data from external sources and transfer it to external destinations.

Apache Solr Tutorial
Question 11. Does Apache Flume Support Third-party Plugins?

Answer :

Yes, Flume has 100% plugin-based architecture, it can load and ships data from external sources to external destination which separately from Flume. SO that most of the big data analysis use this tool for streaming data.

Apache Storm Interview Questions
Question 12. Differentiate Between Filesink And Filerollsink?

Answer :

The major difference between HDFS FileSink and FileRollSink is that HDFS File Sink writes the events into the Hadoop Distributed File System (HDFS) whereas File Roll Sink stores the events into the local file system.

Apache Tapestry Interview Questions
Question 13. Why We Are Using Flume?

Answer :

Most often Hadoop developer use this too to get data from social media sites. Its developed by Cloudera for aggregating and moving very large amount if data. The primary use is to gather log files from different sources and asynchronously persist in the hadoop cluster.

Apache Storm Tutorial
Question 14. What Is Flumeng?

Answer :

A real time loader for streaming your data into Hadoop. It stores data in HDFS and HBase. You’ll want to get started with FlumeNG, which improves on the original flume.

Question 15. Explain What Are The Tools Used In Big Data?

Answer :

Tools used in Big Data includes

Hadoop
Hive
Pig
Flume
Mahout
Sqoop
Apache Hive Interview Questions
Question 16. What Are The Complicated Steps In Flume Configurations?

Answer :

Flume can processing streaming data. so if started once, there is no stop/end to the process. asynchronously it can flows data from source to HDFS via agent. First of all agent should know individual components how they are connected to load data. so configuration is trigger to load streaming data. for example consumerkey, consumersecret accessToken and accessTokenSecret are key factor to download data from twitter.

Apache Hive Tutorial
Question 17. What Are Flume Core Components ?

Answer :

Cource, Channels and sink are core components in Apache Flume. When Flume source receives event from externalsource, it stores the event in one or multiple channels. Flume channel is temporarily store and keep the event until’s consumed by the Flume sink. It act as Flume repository. Flume Sink removes the event from channel and put into an external repository like HDFS or Move to the next flume.

Apache Pig Interview Questions
Question 18. What Are The Data Extraction Tools In Hadoop?

Answer :

Sqoop can be used to transfer data between RDBMS and HDFS. Flume can be used to extract the streaming data from social media, web log etc and store it on HDFS.

Apache Cassandra Interview Questions
Question 19. Does Flume Provide 100% Reliability To The Data Flow?

Answer :

Yes, Apache Flume provides end to end reliability because of its transactional approach in data flow.

Apache Pig Tutorial
Question 20. Tell Any Two Features Of Flume?

Answer :

Fume collects data efficiently, aggregate and moves large amount of log data from many different sources to centralized data store.
Flume is not restricted to log data aggregation and it can transport massive quantity of event data including but not limited to network traffic data, social-media generated data , email message na pretty much any data storage.

Apache Kafka Interview Questions
Question 21. What Are Interceptors?

Answer :

Interceptors are used to filter the events between source and channel, channel and sink. These channels can filter un-necessary or targeted log files. Depends on requirements you can use n number of interceptors.

Question 22. Why Flume.?

Answer :

Flume is not limited to collect logs from distributed systems, but it is capable of performing other use cases such as

Collecting readings from array of sensors
Collecting impressions from custom apps for an ad network
Collecting readings from network devices in order to monitor their performance.
Flume is targeted to preserve the reliability, scalability, manageability and extensibility while it serves maximum number of clients with higher QoS
Apache Flume Tutorial
Question 23. What Is Flume Event?

Answer :

A unit of data with set of string attribute called Flume event. The external source like web-server send events to the source. Internally Flume has inbuilt functionality to understand the source format.

Each log file is consider as an event. Each event has header and value sectors, which has header information and appropriate value that assign to articular header.

Apache Ant Interview Questions
Question 24. What Is Apache Spark?

Answer :

Spark is a fast, easy-to-use and flexible data processing framework. It has an advanced execution engine supporting cyclic data  flow and in-memory computing. Spark can run on Hadoop, standalone or in the cloud and is capable of accessing diverse data sources including HDFS, HBase, Cassandra and others.

Apache Spark Interview Questions
Question 25. What Is Sink Processors?

Answer :

Sinc processors is mechanism by which you can create a fail-over task and load balancing.

Apache Kafka Tutorial
Question 26. How Multi-hop Agent Can Be Setup In Flume?

Answer :

Avro RPC Bridge mechanism is used to setup Multi-hop agent in Apache Flume.

Apache Camel Interview Questions
Question 27. Can Flume Can Distribute Data To Multiple Destinations?

Answer :

Yes. It support multiplexing flow. The event flows from one source to multiple channel and multiple destionations, It is acheived by defining a flow multiplexer.

Apache Solr Interview Questions
Question 28. Can You Explain About Configuration Files?

Answer :

The agent configuration is stored in local configuration file. it  comprises of each agents source,  sink and channel information.

Apache Ant Tutorial
Question 29. What Are The Similarities And Differences Between Apache Flume And Apache Kafka?

Answer :

Flume pushes messages to their destination via its Sinks.With Kafka you need to consume messages from Kafka Broker using a Kafka Consumer API.

Apache Tajo Interview Questions
Question 30. Explain Reliability And Failure Handling In Apache Flume?

Answer :

Flume NG uses channel-based transactions to guarantee reliable message delivery. When a message moves from one agent to another, two transactions are started, one on the agent that delivers the event and the other on the agent that receives the event. In order for the sending agent to commit it’s transaction, it must receive success indication from the receiving agent.

The receiving agent only returns a success indication if it’s own transaction commits properly first. This ensures guaranteed delivery semantics between the hops that the flow makes. Figure  below shows a sequence diagram that illustrates the relative scope and duration of the transactions operating within the two interacting agents.