## [Main title](../README.md)
### [Interview questions](full.md)

# Apache Kafka
+ [What is Apache Kafka?](#What-is-Apache-Kafka)
+ [What is the traditional method of transferring messages?](#What-is-the-traditional-method-of-transfering-messages)
+ [What are the benefits of Apache Kafka over the traditional technique?](#What-is-the-benefits-of-Apache-Kafka-over-the-traditional-technique)
+ [What is the meaning of broker in Apache Kafka?](#What-is-the-meaning-of-broker-in-Apache-Kafka)
+ [What is the maximum size of a message that Kafka can receive?](#What-is-the-maximum-size-of-a-message-that-kafka-can-receive)
+ [What is Zookeeper's role in Kafka's ecosystem and can we use Kafka without Zookeeper?](#What-is-the-Zookeepers-role-in-Kafkas-ecosystem-and-can-we-use-Kafka-without-Zookeeper)
+ [How are messages consumed by a consumer in Apache Kafka?](#How-are-messages-consumed-by-a-consumer-in-apache-Kafka)
+ [How can you improve the throughput of a remote consumer?](#How-can-you-improve-the-throughput-of-a-remote-consumer)
+ [How can you get Exactly-Once Messaging from Kafka during data production?](#How-can-get-Exactly-Once-Messaging-from-Kafka-during-data-production)
+ [What is In-Sync Replicas (ISR) in Apache Kafka?](#What-is-In-Sync-MessagesISR-in-Apache-Kafka)
+ [How can we reduce churn (frequent changes) in ISR?](#How-can-we-redcue-chrunfrequent-changes-in-ISR)
+ [When does a broker leave ISR?](#When-does-a-broker-leave-ISR)
+ [What does it indicate if a replica stays out of ISR for a long time?](#What-does-it-indicate-if-replica-stays-out-of-Isr-for-a-long-time)
+ [What happens if the preferred replica is not in the ISR list?](#What-happens-if-the-preferred-replica-is-not-in-the-ISR-list)
+ [What is the purpose of replication in Apache Kafka?](#What-is-the-purpose-of-replication-in-apache-kafka)
+ [Is it possible to get the message offset after producing to a topic?](#Is-it-possible-to-get-the-message-offset-after-producing-to-a-topic)
+ [Mention what is the difference between Apache Kafka, Apache Storm, and Apache Flink?](#Mention-what-is-the-difference-between-Apache-Kafka-and-Apache-Storm-and-apache-flink)
+ [List the various components in Kafka?](#List-the-various-components-in-Kafka)
+ [What is the role of the offset in Kafka?](#What-is-the-role-of-the-offset-in-kafka)
+ [Can you explain the concept of `leader` and `follower` in the Kafka ecosystem?](#Can-you-explain-the-concept-of-leader-and-follower-in-kafka-ecosystem)
+ [How do you define a Partitioning Key?](#How-do-you-define-a-Partitioning-Key)
+ [In the Producer, when does QueueFullException occur?](#In-the-Producer-when-does-Queuefullexception-occur)
+ [Can you please explain the role of the Kafka Producer API?](#Can-you-please-explain-the-role-of-the-Kafka-Producer-API)

## What is Apache Kafka?
Apache Kafka is a publish-subscribe messaging system developed by Apache written in Java and Scala. It is a distributed, partitioned and replicated log service.

[Table of Contents](#Apache-Kafka)

## What is the traditional method of transfering messages?
The traditional method of transfering messages includes two methods
+ Queuing: In a queuing, a pool of consumers may read message from the server and each message goes to one of them
+ Publish-Subscribe: In this model, messages are broadcasted to all consumers

Kafka caters single consumer abstraction that generalized both of the above- the consumer group.

[Table of Contents](#Apache-Kafka)

## What is the benefits of Apache Kafka over the traditional technique?
Apache Kafka has following benefits above traditional messaging technique
+ Scalability: Kafka is designed for horizontal scalability. It can scale out by adding more brokers (servers) to the Kafka cluster to handle more partitions and thereby increase throughput. This scalability is seamless and can handle petabytes of data without downtime.

+ Performance: Kafka provides high throughput for both publishing and subscribing to messages, even with very large volumes of data. It uses a disk structure that optimizes for batched writes and reads, significantly outperforming traditional databases in scenarios that involve high-volume, high-velocity data.

+ Durability and Reliability: Kafka replicates data across multiple nodes, ensuring that data is not lost even if some brokers fail. This replication is configurable, allowing users to balance between redundancy and performance based on their requirements.

+ Fault Tolerance: Kafka is designed to be fault-tolerant. The distributed nature of Kafka, combined with its replication mechanisms, ensures that the system continues to operate even when individual components .

+ Real-time Processing: Kafka enables real-time data processing by allowing producers to write data into Kafka topics and consumers to read data from these topics with minimal latency. This capability is critical for applications that require real-time analytics, monitoring, and response.

+ Decoupling of Data Streams: Kafka allows producers and consumers to operate independently. Producers can write data to Kafka topics without being concerned about how the data will be processed. Similarly, consumers can read data from topics without needing to coordinate with producers. This decoupling simplifies system architecture and enhances flexibility.

+ Replayability: Kafka stores data for a configurable period, enabling applications to replay historical data. This is valuable for new applications that need access to historical data or for recovering from errors by reprocessing data.

+ High Availability: Kafka's distributed nature and replication model ensure high availability. Even if some brokers or partitions become unavailable, the system can continue to function, ensuring continuous operation of critical applications.

[Table of Contents](#Apache-Kafka)

## What is the meaning of broker in Apache Kafka?
a broker refers to a server in the Kafka cluster that stores and manages the data. Each broker holds a set of topic partitions, allowing Kafka to efficiently handle large volumes of data by distributing the load across multiple brokers in the cluster. Brokers handle all read and write requests from Kafka producers and consumers and ensure data replication and fault tolerance to prevent data loss.

[Table of Contents](#Apache-Kafka)

## What is the maximum size of a message that kafka can receive?
The maximum size of a message that Kafka can receive is determined by the message.max.bytes configuration parameter for the broker and the max.message.bytes parameter for the topic. By default, Kafka allows messages up to 1 MB (1,048,576 bytes) in size, but both parameters can be adjusted to allow larger messages if needed.

[Table of Contents](#Apache-Kafka)

## What is the Zookeeper's role in Kafka's ecosystem and can we use Kafka without Zookeeper?
Zookeeper in Kafka is used for managing and coordinating Kafka brokers. It helps in leader election for partitions, cluster membership, and configuration management among other tasks. Historically, Kafka required Zookeeper to function.

However, with the introduction of KRaft mode (Kafka Raft Metadata mode), it's possible to use Kafka without Zookeeper. KRaft mode replaces Zookeeper by using a built-in consensus mechanism for managing cluster metadata, simplifying the architecture and potentially improving performance and scalability.

[Table of Contents](#Apache-Kafka)

## How are messages consumed by a consumer in apache Kafka?
In Apache Kafka, messages are consumed by a consumer through a pull-based model. The consumer subscribes to one or more topics and polls the Kafka broker at regular intervals to fetch new messages. Messages are consumed in the order they are stored in the topic's partitions. Each consumer keeps track of its offset in each partition, which is the position of the next message to be consumed, allowing it to pick up where it left off across restarts or failures.

[Table of Contents](#Apache-Kafka)

## How can you improve the throughput of a remote consumer?
+ Increase Bandwidth: Ensure the network connection has sufficient bandwidth to handle the data being consumed.
+ Optimize Data Serialization: Use efficient data serialization formats to reduce the size of the data being transmitted.
+ Concurrency: Implement concurrency in the consumer to process data in parallel, if possible.
+ Batch Processing: Where applicable, batch data together to reduce the number of round-trip times needed.
+ Caching: Cache frequently accessed data on the consumer side to reduce data retrieval times.
+ Compression: Compress data before transmission to reduce the amount of data being sent over the network.
+ Optimize Network Routes: Use optimized network paths or CDN services to reduce latency.
+ Adjust Timeouts and Buffer Sizes: Fine-tune network settings, including timeouts and buffer sizes, for optimal data transfer rates.

[Table of Contents](#Apache-Kafka)

## How can get Exactly-Once Messaging from Kafka during data production?

1. **Enable Idempotence**: Configure the producer for idempotence by setting `enable.idempotence` to `true`. This ensures that messages are not duplicated during network errors.

2. **Transactional API**: Use Kafka’s Transactional API by initiating transactions on the producer. This involves setting the `transactional.id` configuration and managing transactions with `beginTransaction()`, `commitTransaction()`, and `abortTransaction()` methods. It ensures that either all messages in a transaction are successfully published, or none are in case of failure, thereby achieving exactly-once semantics.

3. **Proper Configuration**: Alongside enabling idempotence, adjust `acks` to `all` (or `-1`) to ensure all replicas acknowledge the messages, and set an appropriate `retries` and `max.in.flight.requests.per.connection` (should be `1` when transactions are used) to handle retries without message duplication.

4. **Consistent Partitioning**: Ensure that messages are partitioned consistently if the order matters. This might involve custom partitioning strategies to avoid shuffling messages among partitions upon retries.

[Table of Contents](#Apache-Kafka)

## What is In-Sync Messages(ISR) in Apache Kafka?
In Apache Kafka, ISR stands for In-Sync Replicas. It's a concept related to Kafka's high availability and fault tolerance mechanisms.

For each partition, Kafka maintains a list of replicas that are considered "in-sync" with the leader replica. The leader replica is the one that handles all read and write requests for a specific partition, while the follower replicas replicate the leader's log. Followers that have fully caught up with the leader log are considered in-sync. This means they have replicated all messages up to the last message acknowledged by the leader.

The ISR ensures data durability and availability. If the leader fails, Kafka can elect a new leader from the in-sync replicas, minimizing data loss and downtime.

[Table of Contents](#Apache-Kafka)

## How can we redcue chrun(frequent changes) in ISR?
+ Optimize Network Configuration: Ensure that the network connections between brokers are stable and have sufficient bandwidth. Network issues can cause followers to fall behind and drop out of the ISR.

+ Adjust Replica Lag Configuration: Kafka allows configuration of parameters like replica.lag.time.max.ms which defines how long a replica can be behind the leader before it is considered out of sync. Adjusting this value can help manage ISR churn by allowing replicas more or less time to catch up.

+ Monitor and Scale Resources Appropriately: Ensure that all brokers have sufficient resources (CPU, memory, disk I/O) to handle their workload. Overloaded brokers may struggle to keep up, leading to replicas falling out of the ISR.

+ Use Dedicated Networks for Replication Traffic: If possible, use a dedicated network for replication traffic. This can help prevent replication traffic from being impacted by other network loads.

[Table of Contents](#Apache-Kafka)

## When does a broker leave ISR?
A broker may leave the ISR for a few reasons:

+ Falling Behind: If a replica falls behind the leader by more than the configured thresholds (replica.lag.time.max.ms or replica.lag.max.messages), it is removed from the ISR.

+ Broker Failure: If a broker crashes or is otherwise disconnected from the cluster, its replicas are removed from the ISR.

+ Manual Intervention: An administrator can manually remove a replica from the ISR, although this is not common practice and should be done with caution.

[Table of Contents](#Apache-Kafka)

## What does it indicate if replica stays out of Isr for a long time?
If a replica stays out of the ISR (In-Sync Replicas) for a long time, it indicates that the replica is not able to keep up with the leader's log updates. This can be due to network issues, hardware failure, or high load on the broker. As a result, the replica might become a bottleneck for partition availability and durability, since it cannot participate in acknowledging writes or be elected as a leader if the current leader fails.

[Table of Contents](#Apache-Kafka)

## What happens if the preferred replica is not in the ISR list?
If the preferred replica is not in the In-Sync Replicas (ISR) for a Kafka topic, the producer will either wait for the preferred replica to become available (if configured with certain ack settings) or send messages to another available broker that is part of the ISR. This ensures data integrity by only using replicas that are fully up-to-date with the leader. Consumers might experience a delay in data availability if they are set to consume only from the preferred replica and it is not available.
[Table of Contents](#Apache-Kafka)

## What is the purpose of replication in apache kafka?
Replication in Kafka serves to increase data availability and durability. By replicating data across multiple brokers, Kafka ensures that even if a broker fails, the data is not lost and can still be accessed from other brokers. It is a fundamental feature for fault tolerance and high availability, making it essential for production environments where data reliability is critical.

[Table of Contents](#Apache-Kafka)

## Is it possible to get the message offset after producing to a topic?
Yes, it is possible to get the message offset after producing a message in Kafka. When you send a message to a Kafka topic, the producer API can return metadata about the message, including the offset of the message in the topic partition.

[Table of Contents](#Apache-Kafka)

## Mention what is the difference between Apache Kafka and Apache Storm and apache flink?
Apache Kafka, Apache Storm, and Apache Flink are all distributed systems designed for processing large volumes of data, but they serve different purposes and operate differently:

+ Apache Kafka is primarily a distributed messaging system or streaming platform aimed at high-throughput, fault-tolerant storage and processing of streaming data. It is often used as a buffer or storage system between data producers and consumers.

+ Apache Storm is a real-time computation system for processing streaming data. It excels at high-speed data ingestion and processing tasks that require immediate response, such as real-time analytics. Storm processes data in a record-by-record fashion.

+ Apache Flink is a stream processing framework that can also handle batch processing. It is known for its ability to perform complex computations on streaming data, including event time processing and state management. Flink is designed to run in all common cluster environments and perform computations at in-memory speed.

[Table of Contents](#Apache-Kafka)

## List the various components in Kafka?
The four major components of Kafka are:
+ Topic – a stream of messages belonging to the same type
+ Producer – that can publish messages to a topic
+ Brokers – a set of servers where the publishes messages are stored
+ Consumer – that subscribes to various topics and pulls data from the brokers.

[Table of Contents](#Apache-Kafka)

## What is the role of the offset in kafka?
In Kafka, the offset is a unique identifier for each record within a Kafka topic's partition. It denotes the position of a record within the partition. The offset is used by consumers to track which records have been read and which haven't, allowing for fault-tolerant and scalable message consumption. Essentially, it enables consumers to pick up reading from the exact point they left off, even in the event of a failure or restart, thereby ensuring that no messages are lost or read multiple times.

[Table of Contents](#Apache-Kafka)

## Can you explain the concept of `leader` and `follower` in kafka ecosystem?
In Apache Kafka, the concepts of "leader" and "follower" refer to roles that brokers play within a Kafka cluster to manage partitions of a topic.

+ Leader: For each partition of a topic, there is one broker that acts as the leader. The leader is responsible for handling all read and write requests for that partition. When messages are produced to a partition, they are sent to the leader broker, which then writes the messages to its local storage. The leader broker ensures that messages are stored in the order they are received.

+ Follower: Followers are other brokers in the cluster that replicate the data of the leader for fault tolerance. Each follower continuously pulls messages from the leader to stay up-to-date, ensuring that it has an exact copy of the leader's data. In case the leader broker fails, one of the followers can be elected as the new leader, ensuring high availability.

[Table of Contents](#Apache-Kafka)

## How do you define a Partitioning Key?
Within the Producer, the role of a Partitioning Key is to indicate the destination partition of the message. By default, a hashing-based Partitioner is used to determine the partition ID given the key. Alternatively, users can also use customized Partitions.

[Table of Contents](#Apache-Kafka)

## In the Producer when does Queuefullexception occur?
QueueFullException typically occurs when the Producer attempts to send messages at a pace that the Broker cannot handle. Since the Producer doesn’t block, users will need to add enough brokers to collaboratively handle the increased load.

[Table of Contents](#Apache-Kafka)

## Can you please explain the role of the Kafka Producer API?
The Kafka Producer API allows applications to send streams of data to topics in the Kafka cluster. Essentially, it enables the production of message data to one or more Kafka topics, facilitating the reliable and scalable distribution of messages across the Kafka ecosystem.

we usually have two producer types – SyncProducer and AsyncProducer. The goal is to expose all the producer functionality through a single API to the client.

[Table of Contents](#Apache-Kafka)
