Mention What Is Apache Kafka?
Apache Kafka is a publish-subscribe messaging system developed by Apache written in Scala. It is a distributed, partitioned and replicated log service.

Mention What Is The Traditional Method Of Message Transfer?
The traditional method of message transfer includes two methods
+ Queuing: In a queuing, a pool of consumers may read message from the server and each message goes to one of them
+ Publish-Subscribe: In this model, messages are broadcasted to all consumers

Kafka caters single consumer abstraction that generalized both of the above- the consumer group.

Mention What Is The Benefits Of Apache Kafka Over The Traditional Technique?
Apache Kafka has following benefits above traditional messaging technique
+ Fast: A single Kafka broker can serve thousands of clients by handling megabytes of reads and writes per second
+ Scalable: Data are partitioned and streamlined over a cluster of machines to enable larger data
+ Durable: Messages are persistent and is replicated within the cluster to prevent data loss
+ Distributed by Design: It provides fault tolerance guarantees and durability

Mention What Is The Meaning Of Broker In Kafka?
In Kafka cluster, broker term is used to refer Server.

Mention What Is The Maximum Size Of The Message Does Kafka Server Can Receive?
The maximum size of the message that Kafka server can receive is 1000000 bytes.

Explain What Is Zookeeper In Kafka? Can We Use Kafka Without Zookeeper?
Zookeeper is an open source, high-performance co-ordination service used for distributed applications adapted by Kafka.
No, it is not possible to bye-pass Zookeeper and connect straight to the Kafka broker. Once the Zookeeper is down, it cannot serve client request.
Zookeeper is basically used to communicate between different nodes in a cluster
In Kafka, it is used to commit offset, so if node fails in any case it can be retrieved from the previously committed offset
Apart from this it also does other activities like leader detection, distributed synchronization, configuration management, identifies when a new node leaves or joins, the cluster, node status in real time, etc.

Explain How Message Is Consumed By Consumer In Kafka?
Transfer of messages in Kafka is done by using sendfile API. It enables the transfer of bytes from the socket to disk via kernel space saving copies and call between kernel user back to the kernel.

Explain How You Can Improve The Throughput Of A Remote Consumer?
If the consumer is located in a different data center from the broker, you may require to tune the socket buffer size to amortize the long network latency.

Explain How You Can Get Exactly Once Messaging From Kafka During Data Production?
During data, production to get exactly once messaging from Kafka you have to follow two things avoiding duplicates during data consumption and avoiding duplication during data production.
Here are the two ways to get exactly one semantics while data production:
Avail a single writer per partition, every time you get a network error checks the last message in that partition to see if your last write succeeded
In the message include a primary key (UUID or something) and de-duplicate on the consumer

Explain How You Can Reduce Churn In Isr? When Does Broker Leave The Isr?
ISR is a set of message replicas that are completely synced up with the leaders, in other word ISR has all messages that are committed. ISR should always include all replicas until there is a real failure. A replica will be dropped out of ISR if it deviates from the leader.

Why Replication Is Required In Kafka?
Replication of message in Kafka ensures that any published message does not lose and can be consumed in case of machine error, program error or more common software upgrades.

What Does It Indicate If Replica Stays Out Of Isr For A Long Time?
If a replica remains out of ISR for an extended time, it indicates that the follower is unable to fetch data as fast as data accumulated at the leader.

Mention What Happens If The Preferred Replica Is Not In The Isr?
If the preferred replica is not in the ISR, the controller will fail to move leadership to the preferred replica.

Is It Possible To Get The Message Offset After Producing?
You cannot do that from a class that behaves as a producer like in most queue systems, its role is to fire and forget the messages. The broker will do the rest of the work like appropriate metadata handling with id’s, offsets, etc.
As a consumer of the message, you can get the offset from a Kafka broker. If you gaze in the SimpleConsumer class, you will notice it fetches MultiFetchResponse objects that include offsets as a list. In addition to that, when you iterate the Kafka Message, you will have MessageAndOffset objects that include both, the offset and the message sent.



Mention What Is The Difference Between Apache Kafka And Apache Storm?
Apach Kafeka: It is a distributed and robust messaging system that can handle huge amount of data and allows passage of messages from one end-point to another.
Apache Storm: It is a real time message processing system, and you can edit or manipulate data in real time. Apache storm pulls the data from Kafka and applies some required manipulation.


List The Various Components In Kafka?
The four major components of Kafka are:
+ Topic – a stream of messages belonging to the same type
+ Producer – that can publish messages to a topic
+ Brokers – a set of servers where the publishes messages are stored
+ Consumer – that subscribes to various topics and pulls data from the brokers.

Explain The Role Of The Offset?
Messages contained in the partitions are assigned a unique ID number that is called the offset. The role of the offset is to uniquely identify every message within the partition.

Explain The Concept Of Leader And Follower?
Every partition in Kafka has one server which plays the role of a Leader, and none or more servers that act as Followers. The Leader performs the task of all read and write requests for the partition, while the role of the Followers is to passively replicate the leader. In the event of the Leader failing, one of the Followers will take on the role of the Leader. This ensures load balancing of the server.

How Do You Define A Partitioning Key?
Within the Producer, the role of a Partitioning Key is to indicate the destination partition of the message. By default, a hashing-based Partitioner is used to determine the partition ID given the key. Alternatively, users can also use customized Partitions.

In The Producer, When Does Queuefullexception Occur?
QueueFullException typically occurs when the Producer attempts to send messages at a pace that the Broker cannot handle. Since the Producer doesn’t block, users will need to add enough brokers to collaboratively handle the increased load.

Explain The Role Of The Kafka Producer Api.
The role of Kafka’s Producer API is to wrap the two producers – kafka.producer.SyncProducer and the kafka.producer.async.AsyncProducer. The goal is to expose all the producer functionality through a single API to the client.