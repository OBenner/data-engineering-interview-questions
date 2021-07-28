Question 1. What Is Apache Nifi?

Answer :

NiFi is helpful in creating DataFlow. It means you can transfer data from one system to another system as well as process the data in between.

Question 2. What Is Nifi Flowfile?

Answer :

A FlowFile is a message or event data or user data, which is pushed or created in the NiFi. A FlowFile has mainly two things attached with it. Its content (Actual payload: Stream of bytes) and attributes. Attributes are key value pairs attached to the content (You can say metadata for the content).

Apache Solr Interview Questions
Question 3. What Is Relationship In Nifi Dataflow?

Answer :

When a processor finishes with processing of FlowFile. It can result in Failure or Success or any other relationship. And based on this relationship you can send data to the Downstream or next processor or mediated accordingly.

Question 4. What Is Reporting Task?

Answer :

A Reporting Task is a NiFi extension point that is capable of reporting and analyzing NiFi's internal metrics in order to provide the information to external resources or report status information as bulletins that appear directly in the NiFi User Interface.

Apache Solr Tutorial
Question 5. What Is A Nifi Processor?

Answer :

Processor is a main component in the NiFi, which will really work on the FlowFile content and helps in creating, sending, receiving, transforming routing, splitting, merging, and processing FlowFile.

Apache Pig Interview Questions
Question 6. Is There A Programming Language That Apache Nifi Supports?

Answer :

NiFi is implemented in the Java programming language and allows extensions (processors, controller services, and reporting tasks) to be implemented in Java. In addition, NiFi supports processors that execute scripts written in Groovy, Jython, and several other popular scripting languages.

Question 7. How Do You Define Nifi Content Repository?

Answer :

As we mentioned previously, contents are not stored in the FlowFile. They are stored in the content repository and referenced by the FlowFile. This allows the contents of FlowFiles to be stored independently and efficiently based on the underlying storage mechanism.

Apache Pig Tutorial Apache Flume Interview Questions
Question 8. What Is The Backpressure In Nifi System?

Answer :

Sometime what happens that Producer system is faster than consumer system. Hence, the messages which are consumed is slower. Hence, all the messages (FlowFiles) which are not being processed will remain in the connection buffer. However, you can limit the connection backpressure size either based on number of FlowFiles or number of data size. If it reaches to defined limit, connection will give back pressure to producer processor not run. Hence, no more FlowFiles generated, until backpressure is reduced.

Question 9. What Is The Template In Nifi?

Answer :

Template is a re-usable workflow. Which you can import and export in the same or different NiFi instances. It can save lot of time rather than creating Flow again and again each time. Template is created as an xml file.

Apache Kafka Interview Questions
Question 10. What Is The Bulleting And How It Helps In Nifi?

Answer :

If you want to know if any problems occur in a dataflow. You can check in the logs for anything interesting, it is much more convenient to have notifications pop up on the screen. If a Processor logs anything as a WARNING or ERROR, we will see a "Bulletin Indicator" show up in the top-right-hand corner of the Processor.

This indicator looks like a sticky note and will be shown for five minutes after the event occurs. Hovering over the bulletin provides information about what happened so that the user does not have to sift through log messages to find it. If in a cluster, the bulletin will also indicate which node in the cluster emitted the bulletin. We can also change the log level at which bulletins will occur in the Settings tab of the Configure dialog for a Processor.

Apache Flume Tutorial
Question 11. Do The Attributes Get Added To Content (actual Data) When Data Is Pulled By Nifi ?

Answer :

You can certainly add attributes to your FlowFiles at anytime, that’s the whole point of separating metadata from the actual data. Essentially, one FlowFile represents an object or a message moving through NiFi. Each FlowFile contains a piece of content, which is the actual bytes. You can then extract attributes from the content, and store them in memory. You can then operate against those attributes in memory, without touching your content. By doing so you can save a lot of IO overhead, making the whole flow management process extremely efficient.

Apache Ant Interview Questions
Question 12. What Happens, If You Have Stored A Password In A Dataflow And Create A Template Out Of It?

Answer :

Password is a sensitive property. Hence, while exporting the DataFlow as a template password will be dropped. As soon as you import the template in the same or different NiFi system.

Apache Solr Interview Questions
Question 13. How Does Nifi Support Huge Volume Of Payload In A Dataflow?

Answer :

Huge volume of data can transit from DataFlow. As data moves through NiFi, a pointer to the data is being passed around, referred to as a FlowFile. The content of the FlowFile is only accessed as needed.

Apache Kafka Tutorial
Question 14. What Is A Nifi Custom Properties Registry?

Answer :

You can use to load custom key, value pair you can use custom properties registry, which can be configure as (in nifi.properties file)

nifi.variable.registry.properties=/conf/nifi_registry

And you can put key value pairs in that file and you can use that properties in you NiFi processor using expression language e.g. ${OS} , if you have configured that property in registry file.

Question 15. Does Nifi Works As A Master-slave Architecture?

Answer :

No, from NiFi 1.0 there is 0-master philosophy is considered. And each node in the NiFi cluster is the same. NiFi cluster is managed by the Zookeeper. Apache ZooKeeper elects a single node as the Cluster Coordinator, and failover is handled automatically by ZooKeeper. All cluster nodes report heartbeat and status information to the Cluster Coordinator. The Cluster Coordinator is responsible for disconnecting and connecting nodes. Additionally, every cluster has one Primary Node, also elected by ZooKeeper.