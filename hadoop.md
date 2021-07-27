[Interview questions](README.md)

# HADOOP
+ [What are the main components of a Hadoop Application?](#What are the main components of a Hadoop Application?)
+ [What is the core concept behind Apache Hadoop framework?](#What is the core concept behind Apache Hadoop framework?)



## What are the main components of a _Hadoop_ Application?
Over the time, there are various forms in which a Hadoop application is defined. But in most of the cases there are following four core components of Hadoop application:
+ _HDFS_: This is the file system in which Hadoop data is stored. It is a distributed file system with very high bandwidth.
+ _Hadoop Common_: This is common set of libraries and utilities used by Hadoop.
+ _Hadoop MapReduce_: This is based on MapReduce algorithm for providing large-scale data processing.
+ _Hadoop YARN_: This is used for resource management in a Hadoop cluster. It can also schedule tasks for users.

[Table of Contents](#HADOOP)


##What is the core concept behind Apache Hadoop framework?
Apache _Hadoop_ is based on the concept of MapReduce algorithm. In MapReduce algorithm, Map and Reduce operations are used to process very large data set.
In this concept, Map method does the filtering and sorting of data. Reduce method performs the summarizing of data.
This is a concept from functional programming.

The key points in this concept are _scalability_ and _fault tolerance_. In Apache Hadoop these features are achieved by multi-threading and efficient implementation of MapReduce.



##What is Hadoop Streaming?
Hadoop distribution provides a Java utility called Hadoop Streaming. It is packaged in a jar file. With Hadoop Streaming, we can create and run Map Reduce jobs with an executable script.
We can create executable scripts for Mapper and Reducer functions. These executable scripts are passed to Hadoop Streaming in a command.
Hadoop Streaming utility creates Map and Reduce jobs and submits these to a cluster. We can also monitor these jobs with this utility.

[Table of Contents](#HADOOP)

##What is the difference between NameNode, Backup Node and Checkpoint NameNode in HDFS?
The differences between NameNode, BackupNode and Checkpoint NameNode are as follows:
+ _NameNode_: NameNode is at the heart of the HDFS file system that manages the metadata i.e. the data of the files is not stored on the NameNode but rather it has the directory tree of all the files present in the HDFS file system on a Hadoop cluster. NameNode uses two files for the namespace:
fsimage file: This file keeps track of the latest checkpoint of the namespace.
edits file: This is a log of changes made to the namespace since checkpoint.
+ _Checkpoint Node_:	Checkpoint
Node keeps track of the latest checkpoint in a directory that has same structure as that of NameNode’s directory.
Checkpoint node creates checkpoints for the namespace at regular intervals by downloading the edits and fsimage file from the NameNode and merging it locally. The new image is then again updated back to the active NameNode.
+ _BackupNode_: This node also provides check pointing functionality like that of the Checkpoint node but it also maintains its up-to-date in-memory copy of the file system namespace that is in sync with the active NameNode.

[Table of Contents](#HADOOP)

##What is the optimum hardware configuration to run Apache Hadoop?
To run Apache Hadoop jobs, it is recommended to use dual core machines or dual processors. There should be 4GB or 8GB RAM with the processor with Error-correcting code (ECC) memory.
Without ECC memory, there is high chance of getting checksum errors.
For storage high capacity SATA drives (around 7200 rpm) should be used in Hadoop cluster.
Around
10GB bandwidth Ethernet networks are good for Hadoop.

[Table of Contents](#HADOOP)

##What do you know about Block and Block scanner in HDFS?
A large file in HDFS is broken into multiple parts and each part is stored on a different Block. By default a Block is of 64 MB capacity in HDFS.

[Table of Contents](#HADOOP)