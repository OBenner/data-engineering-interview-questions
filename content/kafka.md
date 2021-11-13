[Interview questions](full.md)

# Apache Kafka
+ [Mention what is Apache Kafka?](#Mention-what-is-Apache-Kafka)
+ [Mention what is the traditional method of message transfer?](#Mention-what-is-the-traditional-method-of-message-transfer)
+ [Mention what is the benefits of Apache Kafka over the traditional technique?](#Mention-what-is-the-benefits-of-Apache-Kafka-over-the-traditional-technique)
+ [Mention what is the meaning of Broker in Kafka?](#Mention-what-is-the-meaning-of-Broker-in-Kafka)
+ [Mention what is the Maximum Size of the Message does Kafka server can Receive?](#Mention-what-is-the-Maximum-Size-of-the-Message-does-Kafka-server-can-Receive)
+ [Explain what is Zookeeper in Kafka and can we use Kafka without Zookeeper?](#Explain-what-is-Zookeeper-in-Kafka-and-can-we-use-Kafka-without-Zookeeper)
+ [Explain how message is consumed by Consumer in Kafka?](#Explain-how-message-is-consumed-by-Consumer-in-Kafka)
+ [Explain how you can improve the throughput of a remote consumer?](#Explain-how-you-can-improve-the-throughput-of-a-remote-consumer)
+ [Explain how you can get Exactly Once Messaging from Kafka during data production?](#Explain-how-you-can-get-Exactly-Once-Messaging-from-Kafka-during-data-production)
+ [Explain how you can reduce churn in Isr and when does Broker leave the Isr?](#Explain-how-you-can-reduce-churn-in-Isr-and-when-does-Broker-leave-the-Isr)
+ [Why Replication is required in Kafka?](#Why-Replication-is-required-in-Kafka)
+ [What does it indicate if replica stays out of Isr for a long time?](#What-does-it-indicate-if-replica-stays-out-of-Isr-for-a-long-time)
+ [Mention what happens if the preferred replica is not in the Isr?](#Mention-what-happens-if-the-preferred-replica-is-not-in-the-Isr)
+ [Is it possible to get the Message Offset after Producing?](#Is-it-possible-to-get-the-Message-Offset-after-Producing)
+ [Mention what is the difference between Apache Kafka and Apache Storm?](#Mention-what-is-the-difference-between-Apache-Kafka-and-Apache-Storm)
+ [List the various components in Kafka?](#List-the-various-components-in-Kafka)
+ [Explain the role of the Offset?](#Explain-the-role-of-the-Offset)
+ [Explain the concept of Leader and Follower?](#Explain-the-concept-of-Leader-and-Follower)
+ [How do you define a Partitioning Key?](#How-do-you-define-a-Partitioning-Key)
+ [In the Producer when does Queuefullexception occur?](#In-the-Producer-when-does-Queuefullexception-occur)
+ [Explain the role of the Kafka Producer Api.](#Explain-the-role-of-the-Kafka-Producer-Api)

## Mention what is Apache Kafka?
Apache Kafka is a publish-subscribe messaging system developed by Apache written in Scala. It is a distributed, partitioned and replicated log service.

[Table of Contents](#Apache-Kafka)

## Mention what is the traditional method of message transfer?
The traditional method of message transfer includes two methods
+ Queuing: In a queuing, a pool of consumers may read message from the server and each message goes to one of them
+ Publish-Subscribe: In this model, messages are broadcasted to all consumers

Kafka caters single consumer abstraction that generalized both of the above- the consumer group.

[Table of Contents](#Apache-Kafka)

## Mention what is the benefits of Apache Kafka over the traditional technique?
Apache Kafka has following benefits above traditional messaging technique
+ Fast: A single Kafka broker can serve thousands of clients by handling megabytes of reads and writes per second
+ Scalable: Data are partitioned and streamlined over a cluster of machines to enable larger data
+ Durable: Messages are persistent and is replicated within the cluster to prevent data loss
+ Distributed by Design: It provides fault tolerance guarantees and durability

[Table of Contents](#Apache-Kafka)

## Mention what is the meaning of Broker in Kafka?
In Kafka cluster, broker term is used to refer Server.

[Table of Contents](#Apache-Kafka)

## Mention what is the Maximum Size of the Message does Kafka server can Receive?
The maximum size of the message that Kafka server can receive is 1000000 bytes.

[Table of Contents](#Apache-Kafka)

## Explain what is Zookeeper in Kafka and can we use Kafka without Zookeeper?
Zookeeper is an open source, high-performance co-ordination service used for distributed applications adapted by Kafka.
No, it is not possible to bye-pass Zookeeper and connect straight to the Kafka broker. Once the Zookeeper is down, it cannot serve client request.
Zookeeper is basically used to communicate between different nodes in a cluster
In Kafka, it is used to commit offset, so if node fails in any case it can be retrieved from the previously committed offset
Apart from this it also does other activities like leader detection, distributed synchronization, configuration management, identifies when a new node leaves or joins, the cluster, node status in real time, etc.

[Table of Contents](#Apache-Kafka)

## Explain how message is consumed by Consumer in Kafka?
Transfer of messages in Kafka is done by using sendfile API. It enables the transfer of bytes from the socket to disk via kernel space saving copies and call between kernel user back to the kernel.

[Table of Contents](#Apache-Kafka)

## Explain how you can improve the throughput of a remote consumer?
If the consumer is located in a different data center from the broker, you may require to tune the socket buffer size to amortize the long network latency.

[Table of Contents](#Apache-Kafka)

## Explain how you can get Exactly Once Messaging from Kafka during data production?
During data, production to get exactly once messaging from Kafka you have to follow two things avoiding duplicates during data consumption and avoiding duplication during data production.
Here are the two ways to get exactly one semantics while data production:
Avail a single writer per partition, every time you get a network error checks the last message in that partition to see if your last write succeeded
In the message include a primary key (UUID or something) and de-duplicate on the consumer

[Table of Contents](#Apache-Kafka)

## Explain how you can reduce churn in Isr and when does Broker leave the Isr?
ISR is a set of message replicas that are completely synced up with the leaders, in other word ISR has all messages that are committed. ISR should always include all replicas until there is a real failure. A replica will be dropped out of ISR if it deviates from the leader.

[Table of Contents](#Apache-Kafka)

## Why Replication is required in Kafka?
Replication of message in Kafka ensures that any published message does not lose and can be consumed in case of machine error, program error or more common software upgrades.

[Table of Contents](#Apache-Kafka)

## What does it indicate if replica stays out of Isr for a long time?
If a replica remains out of ISR for an extended time, it indicates that the follower is unable to fetch data as fast as data accumulated at the leader.

[Table of Contents](#Apache-Kafka)

## Mention what happens if the preferred replica is not in the Isr?
If the preferred replica is not in the ISR, the controller will fail to move leadership to the preferred replica.

[Table of Contents](#Apache-Kafka)

## Is it possible to get the Message Offset after Producing?
You cannot do that from a class that behaves as a producer like in most queue systems, its role is to fire and forget the messages. The broker will do the rest of the work like appropriate metadata handling with id’s, offsets, etc.
As a consumer of the message, you can get the offset from a Kafka broker. If you gaze in the SimpleConsumer class, you will notice it fetches MultiFetchResponse objects that include offsets as a list. In addition to that, when you iterate the Kafka Message, you will have MessageAndOffset objects that include both, the offset and the message sent.

[Table of Contents](#Apache-Kafka)

## Mention what is the difference between Apache Kafka and Apache Storm?
Apach Kafeka: It is a distributed and robust messaging system that can handle huge amount of data and allows passage of messages from one end-point to another.
Apache Storm: It is a real time message processing system, and you can edit or manipulate data in real time. Apache storm pulls the data from Kafka and applies some required manipulation.

[Table of Contents](#Apache-Kafka)

## List the various components in Kafka?
The four major components of Kafka are:
+ Topic – a stream of messages belonging to the same type
+ Producer – that can publish messages to a topic
+ Brokers – a set of servers where the publishes messages are stored
+ Consumer – that subscribes to various topics and pulls data from the brokers.

[Table of Contents](#Apache-Kafka)

## Explain the role of the Offset?
Messages contained in the partitions are assigned a unique ID number that is called the offset. The role of the offset is to uniquely identify every message within the partition.

[Table of Contents](#Apache-Kafka)

## Explain the concept of Leader and Follower?
Every partition in Kafka has one server which plays the role of a Leader, and none or more servers that act as Followers. The Leader performs the task of all read and write requests for the partition, while the role of the Followers is to passively replicate the leader. In the event of the Leader failing, one of the Followers will take on the role of the Leader. This ensures load balancing of the server.

[Table of Contents](#Apache-Kafka)

## How do you define a Partitioning Key?
Within the Producer, the role of a Partitioning Key is to indicate the destination partition of the message. By default, a hashing-based Partitioner is used to determine the partition ID given the key. Alternatively, users can also use customized Partitions.

[Table of Contents](#Apache-Kafka)

## In the Producer when does Queuefullexception occur?
QueueFullException typically occurs when the Producer attempts to send messages at a pace that the Broker cannot handle. Since the Producer doesn’t block, users will need to add enough brokers to collaboratively handle the increased load.

[Table of Contents](#Apache-Kafka)

## Explain the role of the Kafka Producer Api.
The role of Kafka’s Producer API is to wrap the two producers – kafka.producer.SyncProducer and the kafka.producer.async.AsyncProducer. The goal is to expose all the producer functionality through a single API to the client.

[Table of Contents](#Apache-Kafka)