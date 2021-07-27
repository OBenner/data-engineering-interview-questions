[Interview questions](README.md)

# HADOOP
+ [What are the main components of a Hadoop Application?](#What are the main components of a Hadoop Application?)
+ [What is the core concept behind Apache Hadoop framework?](#What is the core concept behind Apache Hadoop framework?)
+ [What is Hadoop Streaming?](#What is Hadoop Streaming?)
+ [What is the difference between NameNode, Backup Node and Checkpoint NameNode in HDFS?](#What is the difference between NameNode, Backup Node and Checkpoint NameNode in HDFS?)
+ [What is the optimum hardware configuration to run Apache Hadoop?](#What is the optimum hardware configuration to run Apache Hadoop?)
+ [What do you know about Block and Block scanner in HDFS?](#What do you know about Block and Block scanner in HDFS?)



## What are the main components of a Hadoop Application?
Over the time, there are various forms in which a Hadoop application is defined. But in most of the cases there are following four core components of Hadoop application:
+ _HDFS_: This is the file system in which Hadoop data is stored. It is a distributed file system with very high bandwidth.
+ _Hadoop Common_: This is common set of libraries and utilities used by Hadoop.
+ _Hadoop MapReduce_: This is based on MapReduce algorithm for providing large-scale data processing.
+ _Hadoop YARN_: This is used for resource management in a Hadoop cluster. It can also schedule tasks for users.

[Table of Contents](#HADOOP)


## What is the core concept behind Apache Hadoop framework?
Apache _Hadoop_ is based on the concept of MapReduce algorithm. In MapReduce algorithm, Map and Reduce operations are used to process very large data set.
In this concept, Map method does the filtering and sorting of data. Reduce method performs the summarizing of data.
This is a concept from functional programming.

The key points in this concept are _scalability_ and _fault tolerance_. In Apache Hadoop these features are achieved by multi-threading and efficient implementation of MapReduce.



## What is Hadoop Streaming?
Hadoop distribution provides a Java utility called Hadoop Streaming. It is packaged in a jar file. With Hadoop Streaming, we can create and run Map Reduce jobs with an executable script.
We can create executable scripts for Mapper and Reducer functions. These executable scripts are passed to Hadoop Streaming in a command.
Hadoop Streaming utility creates Map and Reduce jobs and submits these to a cluster. We can also monitor these jobs with this utility.

[Table of Contents](#HADOOP)

## What is the difference between NameNode, Backup Node and Checkpoint NameNode in HDFS?
The differences between NameNode, BackupNode and Checkpoint NameNode are as follows:
+ NameNode: NameNode is at the heart of the HDFS file system that manages the metadata i.e. the data of the files is not stored on the NameNode but rather it has the directory tree of all the files present in the HDFS file system on a Hadoop cluster. NameNode uses two files for the namespace:
fsimage file: This file keeps track of the latest checkpoint of the namespace.
edits file: This is a log of changes made to the namespace since checkpoint.
+ Checkpoint Node:	Checkpoint
Node keeps track of the latest checkpoint in a directory that has same structure as that of NameNode’s directory.
Checkpoint node creates checkpoints for the namespace at regular intervals by downloading the edits and fsimage file from the NameNode and merging it locally. The new image is then again updated back to the active NameNode.
+ BackupNode: This node also provides check pointing functionality like that of the Checkpoint node but it also maintains its up-to-date in-memory copy of the file system namespace that is in sync with the active NameNode.

[Table of Contents](#HADOOP)

## What is the optimum hardware configuration to run Apache Hadoop?
To run Apache Hadoop jobs, it is recommended to use dual core machines or dual processors. There should be 4GB or 8GB RAM with the processor with Error-correcting code (ECC) memory.
Without ECC memory, there is high chance of getting checksum errors.
For storage high capacity SATA drives (around 7200 rpm) should be used in Hadoop cluster.
Around
10GB bandwidth Ethernet networks are good for Hadoop.

[Table of Contents](#HADOOP)

## What do you know about Block and Block scanner in HDFS?
A large file in HDFS is broken into multiple parts and each part is stored on a different Block. By default a Block is of 64 MB capacity in HDFS.

Block Scanner is a program that every Data node in HDFS runs periodically to verify the checksum of every block stored on the data node.
The purpose of a Block Scanner is to detect any data corruption errors on Data node.

[Table of Contents](#HADOOP)

What are the default port numbers on which Name Node, Job Tracker and Task Tracker run in Hadoop?
Default port numbers of Name Node, Job Tracker and Task Tracker are as follows:
NameNode runs on port 50070
Task Tracker runs on port 50060
Job Tracker runs on port 50030

How will you disable a Block Scanner on HDFS DataNode?
In HDFS, there is a configuration dfs.datanode.scan.period.hours in hdfs- site.xml to set the number of hours interval at which Block Scanner should run.
We can set dfs.datanode.scan.period.hours=0 to disable the Block Scanner. It means it will not run on HDFS DataNode.

How will you get the distance between two nodes in Apache Hadoop?
In Apache Hadoop we can use NetworkTopology.getDistance() method to get the distance between two nodes.
Distance from a node to its parent is considered as 1.

Why do we use commodity hardware in Hadoop?
Hadoop does not require a very high-end server with large memory and processing power. Due to this we can use any inexpensive system with average RAM and processor. Such kind of system is called commodity hardware.
Since there is parallel processing in Hadoop MapReduce, it is convenient to distribute a task among multiple servers and then do the execution. It saves cost as well as it is much faster compared to other options. Another benefit of using commodity hardware in Hadoop is scalability. Commodity hardware is readily available in market. Whenever we need to scale up our operations in Hadoop cluster we can obtain more commodity hardware. In case of high-end machines, we have to raise purchase orders and get them built on demand.



How does inter cluster data copying works in Hadoop?
In Hadoop, there is a utility called DistCP (Distributed Copy) to perform large inter/intra-cluster copying of data. This utility is also based on MapReduce. It creates Map tasks for files given as input.
After every copy using DistCP, it is recommended to run crosschecks to confirm that there is no data corruption and copy is complete.

How can we update a file at an arbitrary location in HDFS?
This is a trick question. In HDFS, it is not allowed to update a file at an arbitrary location. All the files are written in append only mode. It means all writes are done at the end of a file.
So there is no possibility of updating the files at any random location.

What is Replication factor in HDFS, and how can we set it?
Replication factor in HDFS is the number of copies of a file in file system. A Hadoop application can specify the number of replicas of a file it wants HDFS to maintain. This information is stored in NameNode. We can set the replication factor in following ways:
We can use Hadoop fs shell, to specify the replication factor for a file. Command as follows:
$hadoop fs –setrep –w 5
/file_name
In above command, replication factor of file_name  file is set as 5.
We can also use Hadoop fs shell, to specify the replication factor of all the files in a directory.
$hadoop fs –setrep –w 2
/dir_name
In above command, replication factor of all the files under directory dir_name is set as 2.

What is the difference between NAS and DAS in Hadoop cluster?
NAS stands for Network Attached Storage and DAS stands for Direct Attached Storage.
In NAS, compute and storage layers are separated. Storage is distributed over different servers on a network.
In DAS, storage is attached to the node where computation takes place.
Apache Hadoop is based on the principle of moving processing near the location of data. So it needs storage disk to be local to computation.
With DAS, we get very good performance on a Hadoop cluster. Also DAS can be implemented on commodity hardware. So it is more cost effective.
Only when we have very high bandwidth (around 10 GbE) it is preferable to use NAS storage.

What are the two messages that NameNode receives from DataNode in Hadoop?
NameNode receives following two messages from every DataNode:
Heartbeat: This message signals that DataNode is still alive. Periodic receipt of Heartbeat is vey important for NameNode to decide whether to use a DataNode or not.
Block Report: This is a list of all the data blocks hosted on a DataNode. This report is also very useful for functioning of NameNode. With this report, NameNode gets information about what data is stored on a specific DataNode.

18. How does indexing work in Hadoop?
    Indexing in Hadoop has two different levels.
    Index based on File URI: In this case data is indexed based on different files. When we search for data, index will return the files that contain the data.
    Index based on InputSplit: In this case, data is indexed based on locations where input split is located.

What data is stored in a HDFS NameNode?
NameNode is the central node of an HDFS system. It does not store any actual data on which MapReduce operations have to be done. But it has all the metadata about the data stored in HDFS DataNodes.
NameNode has the directory tree of all the files in HDFS filesystem. Using this meta data it manages all the data stored in different DataNodes.


What would happen if NameNode crashes in a HDFS cluster?
There is only one NameNode in a HDFS cluster. This node maintains metadata about DataNodes. Since there is only one NameNode, it is the single point of failure in a HDFS cluster. When NameNode crashes, system may become unavailable.
We can specify a secondary NameNode in HDFS cluster. The secondary
NameNode takes the periodic checkpoints of the file system in HDFS. But it is not the backup of NameNode. We can use it to recreate the NameNode and restart it in case of a crash.

What are the main functions of Secondary NameNode?
Main functions of Secondary NameNode are as follows:
FsImage: It stores a copy of FsImage file and EditLog.
NameNode crash: In case NameNode crashes, we can use Secondary NameNode's FsImage to recreate the NameNode.
Checkpoint: Secondary NameNode runs Checkpoint to confirm that data is not corrupt in HDFS.

Update: It periodically applies the updates from EditLog to FsImage file. In this way FsImage file on Secondary NameNode is kept up to date. This helps in saving time during NameNode restart.

What happens if HDFS file is set with replication factor of 1 and DataNode crashes?
Replication factor is same as the number of copies of a file on HDFS. If we set the replication factor of 1, it means there is only 1 copy of the file.
In case, DataNode that has this copy of file crashes, the data is lost. There is no way to recover it. It is essential to keep replication factor of more than 1 for any business critical data.

What is the meaning of Rack Awareness in Hadoop?
In Hadoop, most of the components like NameNode, DataNode etc are rack- aware. It means they have the information about the rack on which they exist. The main use of rack awareness is in implementing fault-tolerance.
Any communication between nodes on same rack is much faster than the communication between nodes on two different racks.
In Hadoop, NameNode maintains information about rack of each DataNode. While reading/writing data, NameNode tries to choose the DataNodes that are closer to each other. Due to performance reasons, it is recommended to use close data nodes for any operation. So Rack Awareness is an important concept for high performance and fault- tolerance in Hadoop.
If we set Replication factor 3 for a file, does it mean any computation will also take place 3 times?
No. Replication factor of 3 means that there are 3 copies of a file. But computation takes place only one the one copy of file. If the node on which first copy exists, does not respond then computation will be done on second copy.

How will you check if a file exists in HDFS?
In Hadoop, we can run hadoop fs command with option e to check the existence of a file in HDFS. This is generally used for testing purpose. Command will be as follows:
%>hadoop fs -test -ezd file_uri e is for checking the existence of file z is for checking non-zero size of
File d is for checking if the path is directory

Why do we use fsck command in HDFS?
fsck command is used for getting the details of files and directories in HDFS. Main uses of fsck command in HDFS are as follows:
delete: We use this option to delete files in HDFS.
move: This option is for moving corrupt files to lost/found.
locations: This option prints all the locations of a block in HDFS.

racks: This option gives the network topology of data-node locations.
blocks: This option gives the report of blocks in HDFS.

What will happen when NameNode is down and a user submits a new job?
Since NameNode is the single point of failure in Hadoop, user job cannot execute. The job will fail when the NameNode is down. User will have to wait for NameNode to restart and come up, before running a job.

What are the core methods of a Reducer in Hadoop?
The main task of Reducer is to reduce a larger set of data that shares a key to a smaller set of data. In Hadoop, Reducer has following three core methods:
setup(): At the start of a task, setup() method is called to configure various parameters for Reducer.
reduce(): This is the main
operation of Reducer. In reduce() method we define the task that has to be done for a set of values that share a key.
cleanup(): Once reduce() task is done, we can use cleanup() to clean any intermediate data or temporary files.

29. What are the primary phases of a Reducer in Hadoop?
    In Hadoop, there are three primary phases of a Reducer:
    Shuffle: In this phase, Reducer copies the sorted output from each Mapper.
    Sort: In this phase, Hadoop framework sorts the input to Reducer by same key. It uses merge sort in this phase. Sometimes, shuffle and sort phases occur at the same time.
    Reduce: This is the phase in which output values associated with a key are reduced to give output result. Output from Reducer is not re-sorted.

What is the use of Context object in Hadoop?
Hadoop uses Context object with Mapper to interact with rest of the system. Context object gets the configuration of the system and job in its constructor.
We use Context object to pass the information in setup(), cleanup() and map() methods. This is an important object that makes the important information available during the map operations.

How does partitioning work in Hadoop?
Partitioning is the phase between Map phase and Reduce phase in Hadoop workflow. Since partitioner gives output to Reducer, the number of partitions is same as the number of Reducers.

Partitioner will partition the output from Map phase into distinct partitions by using a user-defined condition.
Partitions can be like Hash based buckets.
E.g. If we have to find the student with the maximum marks in each gender in each subject. We can first use Map function to map the keys with each gender. Once mapping is done, the result is passed to Partitioner. Partitioner will partition each row with gender on the basis of subject. For each subject there will be a different Reducer. Reducer will take input from each partition and find the student with the highest marks.

What is a Combiner in Hadoop?
Combiner is an optional step between Map and Reduce. Combiner is also called Semi-Reducer. Combiner takes output from Map, creates Key-value pairs and passes these to Reducer.
Combiner's task is to summarize the outputs from Map into summary records with same key.
By using Combiner, we can reduce the data transfer between Mapper and
Reducer. Combiner does the task similar to reduce but it is done on the Map machine itself.

What is the default replication factor in HDFS?
Default replication factor in HDFS is 3. It means there will be 3 copies of each data.
We can configure it with dfs.replication in hdfs-site.xml file.
We can even set it from command line in Hadoop fs command.

How much storage is allocated by HDFS for storing a file of 25 MB size?
This is a question to test the basic concepts of HDFS. In HDFS, all the data is stored in blocks. The size of block can be configured in HDFS.In Apache Hadoop, the default block size is 64 MB. To store a file of 25 MB size, at least one block will be allocated. This means at least 64 MB will be allocated for the file of 25 MB size.

Why does HDFS store data in Block structure?
HDFS stores all the data in terms of Blocks. With Block structure there are some benefits that HDFS gets. Some of these are as follows:
Fault Tolerance: With Block structure, HDFS implements replication. By replicating same block in multiple locations, fault tolerance of the system increases. Even if some copy is not accessible, we can get the data from another copy.
Large Files: We can store very large files that cannot be even stored one disk, in HDFS by using Block structure. We just divide the data of file in multiple Blocks. Each Block can be stored on same or different machines.

Storage management: With Block storage it is easier for Hadoop nodes to calculate the data storage as well as perform optimization in the algorithm to minimize data transfer across the network.

How will you create a custom Partitioner in a Hadoop job?
Partition phase runs between Map and Reduce phase. It is an optional phase. We can create a custom partitioner by extending the org.apache.hadoop.mapreduce.Partitio class in Hadoop. In this class, we have to override getPartition(KEY key, VALUE value, int numPartitions) method.
This method takes three inputs. In this method, numPartitions is same as the number of reducers in our job. We pass key and value to get the partition number to which this key,value record will be assigned. There will be a reducer corresponding to that partition. The reducer will further handle to summarizing of the data.Once custom Partitioner class is ready, we have to set it in the Hadoop job. We can use following method to set it:
job.setPartitionerClass(CustomPartitione

What is a Checkpoint node in HDFS?
A Checkpoint node in HDFS periodically fetches fsimage and edits from NameNode, and merges them. This merge result is called a Checkpoint. Once a Checkpoint is created, Checkpoint Node uploads the Checkpoint to NameNode. Secondary node also takes Checkpoint similar to Checkpoint Node. But it does not upload the Checkpoint to NameNode.
Main benefit of Checkpoint Node is in case of any failure on NameNode. A NameNode does not merge its edits to fsimage automatically during the runtime. If we have long running task, the edits will become huge. When we restart NameNode, it will take much longer time, because it will first merge the edits. In such a scenario, Checkpoint node helps for a long running task.
Checkpoint nodes performs the task of merging the edits with fsimage and then uploads these to NameNode. This saves time during the restart of NameNode.



What is a Backup Node in HDFS?
Backup Node in HDFS is similar to Checkpoint Node. It takes the stream of edits from NameNode. It keeps these edits in memory and also writes these to storage to create a new checkpoint. At any point of time, Backup Node is in sync with the Name Node.
The difference between Checkpoint Node and Backup Node is that Backup Node does not upload any checkpoints to Name Node. Also Backup node takes a stream instead of periodic reading of edits from Name Node.

What is the meaning of term Data Locality in Hadoop?
In a Big Data system, the size of data is huge. So it does not make sense to move data across the network. In such a scenario, Hadoop tries to move computation closer to data. So the Data remains local to the location wherever it was stored. But the computation tasks will be moved to data nodes that hold the data locally.
Hadoop follows following rules for Data Locality optimization:
Hadoop first tries to schedule the task on node that has an HDFS file on a local disk. If it cannot be done, then Hadoop will try to schedule the task on a node on the same rack as the node that has data. If this also cannot be done, Hadoop will schedule the task on the node with same data on a different rack. The above method works well, when we work with the default replication factor of 3 in Hadoop.

What is the difference between Data science, Big Data and Hadoop?
The difference between Data Science, Big Data and Hadoop is as follows:
Data Science is an approach of handling problem with the help of Statistics, Mathematics, Computer Science, Machine learning, Data mining and predictive analysis. With Data Science we can extract knowledge from data in different forms. Current Data Science methods make very good use of Big Data processing systems.
Big Data is the solution for handling huge amount of data with the modern tools and algorithms. It is a way of processing and analyzing the data that is too big for a traditional database management system to handle. With the mobile devices, Internet of things and sharing applications, datasets have become huge. Big Data tools and techniques come handy in processing such a large data set. Hadoop is a framework for handling Big Data. It uses commodity hardware and distributed storage to process large data sets. It is one of the most popular Big Data frameworks these days.

What is a Balancer in HDFS?
In HDFS, data is stored in blocks on a DataNode. There can be a situation when data is not uniformly spread into blocks on a DataNode. When we add a new DataNode to a cluster, we can face such a situation. In such a case, HDFS provides a useful tool Balancer to analyze the placement of blocks on a DataNode. Some people call it as Rebalancer also. This is an administrative tool used by admin staff. We can use this tool to spread the blocks in a uniform manner on a DataNode.

What are the important points a NameNode considers before selecting the DataNode for placing a data block?
Some of the important points for selecting a DataNode by NameNode are as follows:
NameNode tries to keep at least one replica of a Block on the same node that is writing the block.
It tries to spread the different replicas of same block on different racks, so that in case of one rack failure, other rack has the data.
One replica will be kept on a node on the same node as the one that it writing it. It is different from point 1. In Point 1, block is written to same node. In this point block is written on a different node on same rack. This is important for minimizing the network I/O. NameNode also tries to spread the blocks uniformly among all the DataNodes in a cluster.

What is Safemode in HDFS?
Safemode is considered as the read-only mode of NameNode in a cluster. During the startup of NameNode, it is in SafeMode. It does not allow writing to file-system in Safemode. At this time, it collects data and statistics from all the DataNodes. Once it has all the data on blocks, it leaves Safemode.
The main reason for Safemode is to avoid the situation when NameNode starts replicating data in DataNodes before collecting all the information from DataNodes. It may erroneously assume that a block is not replicated well enough, whereas, the issue is that NameNode does not know about whereabouts of all the replicas of a block. Therefore, in Safemode, NameNode first collects the information about how many replicas exist in cluster and then tries to create replicas wherever the number of replicas is less than the policy.

How will you replace HDFS data volume before shutting down a DataNode?
In HDFS, DataNode supports hot swappable drives. With a swappable drive we can add or replace HDFS data volumes while the DataNode is still running. The procedure for replacing a hot swappable drive is as follows:
First we format and mount the new drive. We update the DataNode configuration dfs.datanode.data.dir to reflect the data volume directories. Run the "dfsadmin -reconfig datanode HOST:PORT start" command to start the reconfiguration process Once the reconfiguration is complete, we just unmount the old data volume After unmount we can physically remove the old disks.

What are the important configuration files in Hadoop?
There are two important configuration files in a Hadoop cluster:
Default Configuration: There are core-default.xml, hdfs-default.xml and mapred-default.xml files in which we specify the default configuration for Hadoop cluster. These are read only files.
Custom Configuration: We have site-specific custom files like core-site.xml, hdfs-site.xml, mapred-site.xml in which we can specify the site-specific configuration.

All the Jobs in Hadoop and HDFS implementation uses the parameters defined in the above-mentioned files. With customization we can tune these processes according to our use case. In Hadoop API, there is a Configuration class that loads these files and provides the values at run time to different jobs.

How will you monitor memory used in a Hadoop cluster?
In Hadoop, TaskTracker is the one that uses high memory to perform a task. We can configure the TastTracker to monitor memory usage of the tasks it creates. It can monitor the memory usage to find the badly behaving tasks, so that these tasks do not bring the machine down with excess memory consumption. In memory monitoring we can also limit the maximum memory used by a tasks. We can even limit the memory usage per node. So that all the tasks executing together on a node do not consume more memory than a limit. Some of the parameters for setting memory monitoring in Hadoop are as follows:
mapred.cluster.map.memory.mb, mapred.cluster.reduce.memory.mb: This is the size of virtual memory of a single map/reduce slot in a cluster of Map-Reduce framework. mapred.job.map.memory.mb, mapred.job.reduce.memory.mb: This is the default limit of memory
set on each map/reduce task in Hadoop. mapred.cluster.max.map.memory.m mapred.cluster.max.reduce.memory This is the maximum limit of memory set on each map/reduce task in Hadoop.

Why do we need Serialization in Hadoop map reduce methods?
In Hadoop, there are multiple data nodes that hold data. During the processing of map and reduce methods data may transfer from one node to another node. Hadoop uses serialization to convert the data from Object structure to Binary format. With serialization, data can be converted to binary format and with de-serialization data can be converted back to Object format with reliability.

What is the use of Distributed Cache in Hadoop?
Hadoop provides a utility called Distributed Cache to improve the performance of jobs by caching the files used by applications. An application can specify which file it wants to cache by using JobConf configuration. Hadoop framework copies these files to the nodes one which a task has to be executed. This is done before the start of execution of a task. DistributedCache supports distribution of simple read only text files as well as complex files like jars, zips etc.

How will you synchronize the changes made to a file in Distributed Cache in Hadoop?
It is a trick question. In Distributed Cache, it is not allowed to make any changes to a file. This is a mechanism to cache read-only data across multiple nodes.Therefore, it is not possible to update a cached file or run any synchronization in Distributed Cache.
 