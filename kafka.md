Question 1. Mention What Is Apache Kafka?

Answer :

Apache Kafka is a publish-subscribe messaging system developed by Apache written in Scala. It is a distributed, partitioned and replicated log service.

Question 2. Mention What Is The Traditional Method Of Message Transfer?

Answer :

The traditional method of message transfer includes two methods

Queuing: In a queuing, a pool of consumers may read message from the server and each message goes to one of them
Publish-Subscribe: In this model, messages are broadcasted to all consumers
Kafka caters single consumer abstraction that generalized both of the above- the consumer group.

Apache Tapestry Interview Questions
Question 3. Mention What Is The Benefits Of Apache Kafka Over The Traditional Technique?

Answer :

Apache Kafka has following benefits above traditional messaging technique

Fast: A single Kafka broker can serve thousands of clients by handling megabytes of reads and writes per second
Scalable: Data are partitioned and streamlined over a cluster of machines to enable larger data
Durable: Messages are persistent and is replicated within the cluster to prevent data loss
Distributed by Design: It provides fault tolerance guarantees and durability
Question 4. Mention What Is The Meaning Of Broker In Kafka?

Answer :

In Kafka cluster, broker term is used to refer Server.

Apache Tapestry Tutorial
Question 5. Mention What Is The Maximum Size Of The Message Does Kafka Server Can Receive?

Answer :

The maximum size of the message that Kafka server can receive is 1000000 bytes.

Apache Cassandra Interview Questions
Question 6. Explain What Is Zookeeper In Kafka? Can We Use Kafka Without Zookeeper?

Answer :

Zookeeper is an open source, high-performance co-ordination service used for distributed applications adapted by Kafka.

No, it is not possible to bye-pass Zookeeper and connect straight to the Kafka broker. Once the Zookeeper is down, it cannot serve client request.

Zookeeper is basically used to communicate between different nodes in a cluster
In Kafka, it is used to commit offset, so if node fails in any case it can be retrieved from the previously committed offset
Apart from this it also does other activities like leader detection, distributed synchronization, configuration management, identifies when a new node leaves or joins, the cluster, node status in real time, etc.
Question 7. Explain How Message Is Consumed By Consumer In Kafka?

Answer :

Transfer of messages in Kafka is done by using sendfile API. It enables the transfer of bytes from the socket to disk via kernel space saving copies and call between kernel user back to the kernel.

Apache Cassandra Tutorial Apache Spark Interview Questions
Question 8. Explain How You Can Improve The Throughput Of A Remote Consumer?

Answer :

If the consumer is located in a different data center from the broker, you may require to tune the socket buffer size to amortize the long network latency.

Question 9. Explain How You Can Get Exactly Once Messaging From Kafka During Data Production?

Answer :

During data, production to get exactly once messaging from Kafka you have to follow two things avoiding duplicates during data consumption and avoiding duplication during data production.

Here are the two ways to get exactly one semantics while data production:

Avail a single writer per partition, every time you get a network error checks the last message in that partition to see if your last write succeeded
In the message include a primary key (UUID or something) and de-duplicate on the consumer
Apache Solr Interview Questions
Question 10. Explain How You Can Reduce Churn In Isr? When Does Broker Leave The Isr?

Answer :

ISR is a set of message replicas that are completely synced up with the leaders, in other word ISR has all messages that are committed. ISR should always include all replicas until there is a real failure. A replica will be dropped out of ISR if it deviates from the leader.

Apache Solr Tutorial
Question 11. Why Replication Is Required In Kafka?

Answer :

Replication of message in Kafka ensures that any published message does not lose and can be consumed in case of machine error, program error or more common software upgrades.

Apache Storm Interview Questions
Question 12. What Does It Indicate If Replica Stays Out Of Isr For A Long Time?

Answer :

If a replica remains out of ISR for an extended time, it indicates that the follower is unable to fetch data as fast as data accumulated at the leader.

Apache Tapestry Interview Questions
Question 13. Mention What Happens If The Preferred Replica Is Not In The Isr?

Answer :

If the preferred replica is not in the ISR, the controller will fail to move leadership to the preferred replica.

Apache Storm Tutorial
Question 14. Is It Possible To Get The Message Offset After Producing?

Answer :

You cannot do that from a class that behaves as a producer like in most queue systems, its role is to fire and forget the messages. The broker will do the rest of the work like appropriate metadata handling with id’s, offsets, etc.

As a consumer of the message, you can get the offset from a Kafka broker. If you gaze in the SimpleConsumer class, you will notice it fetches MultiFetchResponse objects that include offsets as a list. In addition to that, when you iterate the Kafka Message, you will have MessageAndOffset objects that include both, the offset and the message sent.

Question 15. Which Components Are Used For Stream Flow Of Data?

Answer :

Bolt:- Bolts represent the processing logic unit in Storm. One can utilize bolts to do any kind of processing such as filtering, aggregating, joining, interacting with data stores, talking to external systems etc. Bolts can also emit tuples (data messages) for the subsequent bolts to process. Additionally, bolts are responsible to acknowledge the processing of tuples after they are done processing.

Spout:- Spouts represent the source of data in Storm. You can write spouts to read data from data sources such as database, distributed file systems, messaging frameworks etc. Spouts can broadly be classified into following –

Reliable:- These spouts have the capability to replay the tuples (a unit of data in data stream). This helps applications achieve ‘at least once message processing’ semantic as in case of failures, tuples can be replayed and processed again. Spouts for fetching the data from messaging frameworks are generally reliable as these frameworks provide the mechanism to replay the messages.

Unreliable:- These spouts don’t have the capability to replay the tuples. Once a tuple is emitted, it cannot be replayed irrespective of whether it was processed successfully or not. This type of spouts follow ‘at most once message processing’ semantic.

Tuple:- The tuple is the main data structure in Storm. A tuple is a named list of values, where each value can be any type. Tuples are dynamically typed — the types of the fields do not need to be declared. Tuples have helper methods like getInteger and getString to get field values without having to cast the result. Storm needs to know how to serialize all the values in a tuple. By default, Storm knows how to serialize the primitive types, strings, and byte arrays. If you want to use another type, you’ll need to implement and register a serializer for that type.

Apache Hive Interview Questions
Question 16. What Are The Key Benefits Of Using Storm For Real Time Processing?

Answer :

Easy to operate: Operating storm is quiet easy

Real fast: It can process 100 messages per second per node

Fault Tolerant: It detects the fault automatically and re-starts the functional attributes

Reliable: It guarantees that each unit of data will be executed at least once or exactly once

Scalable: It runs across a cluster of machine.

Apache Hive Tutorial
Question 17. Does Apache Act As A Proxy Server?

Answer :

Yes, It acts as proxy also by using the mod_proxy module. This module implements a proxy, gateway or cache for Apache. It implements proxying capability for AJP13 (Apache JServ Protocol version 1.3), FTP, CONNECT (for SSL),HTTP/0.9, HTTP/1.0, and (since Apache 1.3.23) HTTP/1.1. The module can be configured to connect to other proxy modules for these and other protocols.

Apache Pig Interview Questions
Question 18. While Installing, Why Does Apache Have Three Config Files - Srm.conf, Access.conf And Httpd.conf?

Answer :

The first two are remnants from the NCSA times, and generally you should be ok if you delete the first two, and stick with httpd.conf.

Apache Cassandra Interview Questions
Question 19. What Is Zeromq?

Answer :

ZeroMQ is “a library which extends the standard socket interfaces with features traditionally provided by specialized messaging middleware products”. Storm relies on ZeroMQ primarily for task-to-task communication in running Storm topologies.

Apache Pig Tutorial
Question 20. How Many Distinct Layers Are Of Storm’s Codebase?

Answer :

There are three distinct layers to Storm’s codebase.

First, Storm was designed from the very beginning to be compatible with multiple languages. Nimbus is a Thrift service and topologies are defined as Thrift structures. The usage of Thrift allows Storm to be used from any language.
Second, all of Storm’s interfaces are specified as Java interfaces. So even though there’s a lot of Clojure in Storm’s implementation, all usage must go through the Java API. This means that every feature of Storm is always available via Java.
Third, Storm’s implementation is largely in Clojure. Line-wise, Storm is about half Java code, half Clojure code. But Clojure is much more expressive, so in reality the great majority of the implementation logic is in Clojure.
Apache Flume Interview Questions
Question 21. When Do You Call The Cleanup Method?

Answer :

The cleanup method is called when a Bolt is being shutdown and should cleanup any resources that were opened. There’s no guarantee that this method will be called on the cluster: For instance, if the machine the task is running on blows up, there’s no way to invoke the method. The cleanup method is intended when you run topologies in local mode (where a Storm cluster is simulated in process), and you want to be able to run and kill many topologies without suffering any resource leaks.

Question 22. How Can We Kill A Topology?

Answer :

To kill a topology, simply run:

storm kill {stormname}

Give the same name to storm kill as you used when submitting the topology. Storm won’t kill the topology immediately. Instead, it deactivates all the spouts so that they don’t emit any more tuples, and then Storm waits Config.TOPOLOGY_MESSAGE_TIMEOUT_SECS seconds before destroying all the workers. This gives the topology enough time to complete any tuples it was processing when it got killed.

Apache Flume Tutorial
Question 23. What Is Combiner Aggregator?

Answer :

A Combiner Aggregator is used to combine a set of tuples into a single field. It has the following signature:

public interface CombinerAggregator {
T init (TridentTuple tuple);
T combine(T val1, T val2);
T zero();
}

Storm calls the init() method with each tuple, and then repeatedly calls the combine()method until the partition is processed. The values passed into the combine() method are partial aggregations, the result of combining the values returned by calls to init().

Apache Ant Interview Questions
Question 24. Is It Necessary To Kill The Topology While Updating The Running Topology?

Answer :

Yes, to update a running topology, the only option currently is to kill the current topology and resubmit a new one. A planned feature is to implement a Storm swap command that swaps a running topology with a new one, ensuring minimal downtime and no chance of both topologies processing tuples at the same time.

Apache Spark Interview Questions
Question 25. Explain How To Write The Output Into A File Using Storm?

Answer :

In Spout, when you are reading file, make FileReader object in Open() method, as such that time it initializes the reader object for worker node. And use that object in nextTuple() method.

Apache Kafka Tutorial
Question 26. Mention What Is The Difference Between Apache Kafka And Apache Storm?

Answer :

Apach Kafeka: It is a distributed and robust messaging system that can handle huge amount of data and allows passage of messages from one end-point to another.

Apache Storm: It is a real time message processing system, and you can edit or manipulate data in real time. Apache storm pulls the data from Kafka and applies some required manipulation.

Apache Camel Interview Questions
Question 27. Explain When Using Field Grouping In Storm, Is There Any Time-out Or Limit To Known Field Values?

Answer :

Field grouping in storm uses a mod hash function to decide which task to send a tuple, ensuring which task will be processed in the correct order. For that, you don’t require any cache. So, there is no time-out or limit to known field values.

Apache Solr Interview Questions
Question 28. In Which Folder Are Java Applications Stored In Apache?

Answer :

Java applications are not stored in Apache, it can be only connected to a other Java webapp hosting webserver using the mod_jk connector.

Apache Ant Tutorial
Question 29. What Is Mod_vhost_alias?

Answer :

This module creates dynamically configured virtual hosts, by allowing the IP address and/or the Host: header of the HTTP request to be used as part of the pathname to determine what files to serve. This allows for easy use of a huge number of virtual hosts with similar configurations.

Apache Tajo Interview Questions
Question 30. What Is Struct And Explain Its Purpose?

Answer :

A struts is a open source framework for creating a Java web applications.

Question 31. List The Various Components In Kafka?

Answer :

The four major components of Kafka are:

Topic – a stream of messages belonging to the same type
Producer – that can publish messages to a topic
Brokers – a set of servers where the publishes messages are stored
Consumer – that subscribes to various topics and pulls data from the brokers.
Apache Tajo Tutorial
Question 32. Explain The Role Of The Offset?

Answer :

Messages contained in the partitions are assigned a unique ID number that is called the offset. The role of the offset is to uniquely identify every message within the partition.

Apache Impala Interview Questions
Question 33. Explain The Concept Of Leader And Follower?

Answer :

Every partition in Kafka has one server which plays the role of a Leader, and none or more servers that act as Followers. The Leader performs the task of all read and write requests for the partition, while the role of the Followers is to passively replicate the leader. In the event of the Leader failing, one of the Followers will take on the role of the Leader. This ensures load balancing of the server.

Apache Storm Interview Questions
Question 34. How Do You Define A Partitioning Key?

Answer :

Within the Producer, the role of a Partitioning Key is to indicate the destination partition of the message. By default, a hashing-based Partitioner is used to determine the partition ID given the key. Alternatively, users can also use customized Partitions.

Question 35. In The Producer, When Does Queuefullexception Occur?

Answer :

QueueFullException typically occurs when the Producer attempts to send messages at a pace that the Broker cannot handle. Since the Producer doesn’t block, users will need to add enough brokers to collaboratively handle the increased load.

Question 36. Explain The Role Of The Kafka Producer Api.

Answer :

The role of Kafka’s Producer API is to wrap the two producers – kafka.producer.SyncProducer and the kafka.producer.async.AsyncProducer. The goal is to expose all the producer functionality through a single API to the client.