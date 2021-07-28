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




Question 2. Can You Elaborate About Mapreduce Job?

Answer :

Based on the configuration, the MapReduce Job first splits the input data into independent chunks called Blocks. These blocks processed by Map() and Reduce() functions. First Map function process the data, then processed by reduce function. The Framework takes care of sorts the Map outputs, scheduling the tasks.

Informatica Interview Questions
Question 3. Why Compute Nodes And The Storage Nodes Are The Same?

Answer :

Compute nodes for processing the data, Storage nodes for storing the data. By default Hadoop framework tries to minimize the network wastage, to achieve that goal Framework follows the Data locality concept. The Compute code execute where the data is stored, so the data node and compute node are the same.

Question 4. What Is The Configuration Object Importance In Mapreduce?

Answer :

It’s used to set/get of parameter name & value pairs in XML file.It’s used to initialize values, read from external file and set as a value parameter.Parameter values in the program always overwrite with new values which are coming from external configure files.Parameter values received from Hadoop’s default values.

Informatica Tutorial
Question 5. Where Mapreduce Not Recommended?

Answer :

Mapreduce is not recommended for Iterative kind of processing. It means repeat the output in a loop manner.To process Series of Mapreduce jobs, MapReduce not suitable. each job persists data in local disk, then again load to another job. It’s costly operation and not recommended.

Teradata Interview Questions
Question 6. What Is Namenode And It’s Responsibilities?

Answer :

Namenode is a logical daemon name for a particular node. It’s heart of the entire Hadoop system. Which store the metadata in FsImage and get all block information in the form of Heartbeat.

Question 7. What Is Jobtracker’s Responsibility?

Answer :

Scheduling the job’s tasks on the slaves. Slaves execute the tasks as directed by the JobTracker. Monitoring the tasks, if failed, re­execute the failed tasks.

Teradata Tutorial Hadoop Interview Questions
Question 8. What Are The Jobtracker & Tasktracker In Mapreduce?

Answer :

MapReduce Framework consists of a single Job Tracker per Cluster, one Task Tracker per node. Usually A cluster has multiple nodes, so each cluster has single Job Tracker and multiple TaskTrackers.JobTracker can schedule the job and monitor the Task Trackers. If Task Tracker failed to execute tasks, try to re-execute the failed tasks.

TaskTracker follow the JobTracker’s instructions and execute the tasks. As a slave node, it report the job status to Master JobTracker in the form of Heartbeat.

Question 9. What Is Job Scheduling Importance In Hadoop Mapreduce?

Answer :

Scheduling is a systematic procedure of allocating resources in the best possible way among multiple tasks. Hadoop task tracker performing many procedures, sometime a particular procedure should finish quickly and provide more prioriety, to do it few job schedulers come into the picture. Default Schedule is FIFO. Fair scheduling, FIFO and CapacityScheduler are most popular hadoop scheduling in hadoop.

Java Interview Questions
Question 10. When Used Reducer?

Answer :

To combine multiple mapper’s output used reducer. Reducer has 3 primary phases sort, shuffle and reduce. It’s possible to process data without reducer, but used when the shuffle and sort is required.

Hadoop Tutorial
Question 11. What Is Replication Factor?

Answer :

A chunk of data is stored in different nodes with in a cluster called replication factor. By default replication value is 3, but it’s possible to change it. Automatically each file is split into blocks and spread across the cluster.

Apache Pig Interview Questions
Question 12. Where The Shuffle And Sort Process Does?

Answer :

After Mapper generate the output temporary store the intermediate data on the local File System. Usually this temporary file configured at core­site.xml in the Hadoop file. Hadoop Framework aggregate and sort this intermediate data, then update into Hadoop to be processed by the Reduce function. The Framework deletes this temporary data in the local system after Hadoop completes the job.

Informatica Interview Questions
Question 13. Java Is Mandatory To Write Mapreduce Jobs?

Answer :

No, By default Hadoop implemented in JavaTM, but MapReduce applications need not be written in Java. Hadoop support Python, Ruby, C++ and other Programming languages. Hadoop Streaming API allows to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.Hadoop Pipes allows programmers to implement MapReduce applications by using C++ programs.

Java Tutorial
Question 14. What Methods Can Controle The Map And Reduce Function’s Output?

Answer :

setOutputKeyClass() and setOutputValueClass()

If they are different, then the map output type can be set using the methods.

setMapOutputKeyClass() and setMapOutputValueClass()

Question 15. What Is The Main Difference Between Mapper And Reducer?

Answer :

Map method is called separately for each key/value have been processed. It process input key/value pairs and emits intermediate key/value pairs.
Reduce method is called separately for each key/values list pair. It process intermediate key/value pairs and emits final key/value pairs.
Both are initialize and called before any other method is called. Both don’t have any parameters and no output.
Machine learning Interview Questions
Question 16. Why Compute Nodes And The Storage Nodes Are Same?

Answer :

Compute nodes are logical processing units, Storage nodes are physical storage units (Nodes). Both are running in the same node because of “data locality” issue. As a result Hadoop minimize the data network wastage and allows to process quickly.

Hadoop MapReduce Tutorial
Question 17. What Is Difference Between Mapside Join And Reduce Side Join? Or When We Goes To Mapside Join And Reduce Join?

Answer :

Join multple tables in mapper side, called map side join. Please note mapside join should has strict format and sorted properly. If dataset is smaller tables, goes through reducer phrase. Data should partitioned properly.

Join the multiple tables in reducer side called reduce side join. If you have large amount of data tables, planning to join both tables. One table is large amount of rows and columns, another one has few number of tables only, goes through Rreduce side join. It’s the best way to join the multiple tables

NoSQL Interview Questions
Question 18. What Happen If Number Of Reducer Is 0?

Answer :

Number of reducer = 0 also valid configuration in MapReduce. In this scenario, No reducer will execute, so mapper output consider as output, Hadoop store this information in separate folder.

Teradata Interview Questions
Question 19. When We Are Goes To Combiner? Why It Is Recommendable?

Answer :

Mappers and reducers are independent they dont talk each other. When the functions that are commutative(a.b = b.a) and associative {a.(b.c) = (a.b).c} we goes to combiner to optimize the mapreduce process. Many mapreduce jobs are limited by the bandwidth, so by default Hadoop framework minimizes the data bandwidth network wastage. To achieve it’s goal, Mapreduce allows user defined “Cominer function” to run on the map output. It’s an MapReduce optimization technique, but it’s optional.

Apache Pig Tutorial
Question 20. What Is The Main Difference Between Mapreduce Combiner And Reducer?

Answer :

Both Combiner and Reducer are optional, but most frequently used in MapReduce. There are three main differences such as:

combiner will get only one input from one Mapper. While Reducer will get multiple mappers from different mappers.
If aggregation required used reducer, but if the function follows commutative (a.b=b.a) and associative a.(b.c)= (a.b).c law, use combiner.
Input and output keys and values types must same in combiner, but reducer can follows any type input, any output format.
HBase Interview Questions
Question 21. What Is Combiner?

Answer :

It’s a logical aggregation of key and value pair produced by mapper. It’s reduces a lot amount of duplicated data transfer between nodes, so eventually optimize the job performance. The framework decides whether combiner runs zero or multiple times. It’s not suitable where mean function occurs.

Question 22. What Is Partition?

Answer :

After combiner and intermediate map­output the Partitioner controls the keys after sort and shuffle. Partitioner divides the intermediate data according to the number of reducers so that all the data in a single partition gets executed by a single reducer. It means each partition can executed by only a single reducer. If you call reducer, automatically partition called in reducer by automatically.

HBase Tutorial
Question 23. When We Goes To Partition?

Answer :

By default Hive reads entire dataset even the application have a slice of data. It’s a bottleneck for mapreduce jobs. So Hive allows special option called partitions. When you are creating table, hive partitioning the table based on requirement.

MongoDB Interview Questions
Question 24. What Are The Important Steps When You Are Partitioning Table?

Answer :

Don’t over partition the data with too small partitions, it’s overhead to the namenode.

if dynamic partition, atleast one static partition should exist and set to strict mode by using given commands.

SET hive.exec.dynamic.partition = true;
SET hive.exec.dynamic.partition.mode = nonstrict;

first load data into non­partitioned table, then load such data into partitioned table. It’s not possible to load data from local to partitioned table.
insert overwrite table table_name partition(year) select * from non­partition­table;

Hadoop Interview Questions
Question 25. Can You Elaborate Mapreduce Job Architecture?

Answer :

First Hadoop programmer submit Mpareduce program to JobClient.

Job Client request the JobTracker to get Job id, Job tracker provide JobID, its’s in the form of Job_HadoopStartedtime_00001. It’s unique ID.

Once JobClient receive received Job ID copy the Job resources (job.xml, job.jar) to File System (HDFS) and submit job to JobTracker. JobTracker initiate Job and schedule the job.

Based on configuration, job split the input splits and submit to HDFS. TaskTracker retrive the job resources from HDFS and launch Child JVM. In this Child JVM, run the map and reduce tasks and notify to the Job tracker the job status.

MongoDB Tutorial
Question 26. Why Task Tracker Launch Child Jvm?

Answer :

Most frequently, hadoop developer mistakenly submit wrong jobs or having bugs. If Task Tracker use existent JVM, it may interrupt the main JVM, so other tasks may influenced. Where as child JVM if it’s trying to damage existent resources, TaskTracker kill that child JVM and retry or relaunch new child JVM.

Data Science R Interview Questions
Question 27. Why Jobclient, Job Tracker Submits Job Resources To File System?

Answer :

Data locality. Move competition is cheaper than moving Data. So logic/ competition in Jar file and splits. So Where the data available, in File System Datanodes. So every resources copy where the data available.

Java Interview Questions
Question 28. How Many Mappers And Reducers Can Run?

Answer :

By default Hadoop can run 2 mappers and 2 reducers in one datanode. also each node has 2 map slots and 2 reducer slots. It’s possible to change this default values in Mapreduce.xml in conf file.

Lucene Tutorial
Question 29. What Is Inputsplit?

Answer :

A chunk of data processed by a single mapper called InputSplit. In another words logical chunk of data which processed by a single mapper called Input split, by default inputSplit = block Size.

Question 30. How To Configure The Split Value?

Answer :

By default block size = 64mb, but to process the data, job tracker split the data. Hadoop architect use these formulas to know split size.

split size = min (max_splitsize, max (block_size, min_split_size));
split size = max(min_split_size, min (block_size, max_split, size));
by default split size = block size
Always No of splits = No of mappers.

Apply above formula:

split size = Min (max_splitsize, max (64, 512kB) // max _splitsize = depends on env, may 1gb or 10gb split size = min (10gb (let assume), 64) split size = 64MB.
split size = max(min_split_size, min (block_size, max_split, size)); split size = max (512kb, min (64, 10GB)); split size = max (512kb, 64);split size = 64 MB;
Question 31. How Much Ram Required To Process 64mb Data?

Answer :

Leg assume. 64 block size, system take 2 mappers, 2 reducers, so 64*4 = 256 MB memory and OS take atleast 30% extra space so atleast 256 + 80 = 326MB Ram required to process a chunk of data.So in this way required more memory to process un­structured process.

Question 32. What Is Difference Between Block And Split?

Answer :

Block: How much chunk data to stored in the memory called block.
Split: how much data to process the data called split.
Question 33. Why Hadoop Framework Reads A File Parallel Why Not Sequential?

Answer :

To retrieve data faster, Hadoop reads data parallel, the main reason it can access data faster. While, writes in sequence, but not parallel, the main reason it might result one node can be overwritten by other and where the second node. Parallel processing is independent, so there is no relation between two nodes, if writes data in parallel, it’s not possible where the next chunk of data has. For example 100 MB data write parallel, 64 MB one block another block 36, if data writes parallel first block doesn’t know where the remaining data. So Hadoop reads parallel and write sequentially.

Apache Pig Interview Questions
Question 34. If I Am Change Block Size From 64 To 128, Then What Happen?

Answer :

Even you have changed block size not effect existent data. After changed the block size, every file chunked after 128 MB of block size. It means old data is in 64 MB chunks, but new data stored in 128 MB blocks.

Question 35. What Is Issplitable()?

Answer :

By default this value is true. It is used to split the data in the input format. if un­structured data, it’s not recommendable to split the data, so process entire file as a one split. to do it first change isSplitable() to false.

Question 36. How Much Hadoop Allows Maximum Block Size And Minimum Block Size?

Answer :

Minimum: 512 bytes. It’s local OS file system block size. No one can decrease fewer than block size.
Maximum: Depends on environment. There is no upper­bound.
Machine learning Interview Questions
Question 37. What Are The Job Resource Files?

Answer :

job.xml and job.jar are core resources to process the Job. Job Client copy the resources to the HDFS.

Question 38. What’s The Mapreduce Job Consists?

Answer :

MapReduce job is a unit of work that client wants to be performed. It consists of input data, MapReduce program in Jar file and configuration setting in XML files. Hadoop runs this job by dividing it in different tasks with the help of JobTracker

Question 39. What Is The Data Locality?

Answer :

Whereever the data is there process the data, computation/process the data where the data available, this process called data locality. “Moving Computation is Cheaper than Moving Data” to achieve this goal follow data locality. It’s possible when the data is splittable, by default it’s true.

Question 40. What Is Speculative Execution?

Answer :

Hadoop run the process in commodity hardware, so it’s possible to fail the systems also has low memory. So if system failed, process also failed, it’s not recommendable.Speculative execution is a process performance optimization technique.Computation/logic distribute to the multiple systems and execute which system execute quickly. By default this value is true. Now even the system crashed, not a problem, framework choose logic from other systems.

Eg: logic distributed on A, B, C, D systems, completed within a time.

System A, System B, System C, System D systems executed 10 min, 8 mins, 9 mins 12 mins simultaneously. So consider system B and kill remaining system processes, framework take care to kill the other system process.

NoSQL Interview Questions
Question 41. When We Goes To Reducer?

Answer :

When sort and shuffle is required then only goes to reducers otherwise no need partition. If filter, no need to sort and shuffle. So without reducer its possible to do this operation.

Question 42. What Is Chain Mapper?

Answer :

Chain mapper class is a special mapper class sets which run in a chain fashion within a single map task. It means, one mapper input acts as another mapper’s input, in this way n number of mapper connected in chain fashion.

HBase Interview Questions
Question 43. How To Do Value Level Comparison?

Answer :

Hadoop can process key level comparison only but not in the value level comparison.

Question 44. What Is Setup And Clean Up Methods?

Answer :

If you don’t no what is starting and ending point/lines, it’s much difficult to solve those problems. Setup and clean up can resolve it. N number of blocks, by default 1 mapper called to each split. each split has one start and clean up methods. N number of methods, number of lines. Setup is initialize job resources.

The purpose of clean up is close the job resources. Map is process the data. once last map is completed, cleanup is initialized. It Improves the data transfer performance. All these block size comparison can do in reducer as well. If you have any key and value, compare one key value to another key value use it. If you compare record level used these setup and cleanup. It open once and process many times and close once. So it save a lot of network wastage during process.

Question 45. How Many Slots Allocate For Each Task?

Answer :

By default each task has 2 slots for mapper and 2 slots for reducer. So each node has 4 slots to process the data.

Question 46. Why Tasktracker Launch Child Jvm To Do A Task? Why Not Use Existent Jvm?

Answer :

Sometime child threads currupt parent threads. It means because of programmer mistake entired MapReduce task distruped. So task tracker launch a child JVM to process individual mapper or tasker. If tasktracker use existent JVM, it might damage main JVM. If any bugs occur, tasktracker kill the child process and relaunch another child JVM to do the same task. Usually task tracker relaunch and retry the task 4 times.

Question 47. What Are The Main Components Of Mapreduce Job?

Answer :

Main Driver Class: providing job configuration parameters
Mapper Class: must extend org.apache.hadoop.mapreduce.Mapper class and performs execution of map() method
Reducer Class: must extend org.apache.hadoop.mapreduce.Reducer class
Question 48. What Main Configuration Parameters Are Specified In Mapreduce?

Answer :

The MapReduce programmers need to specify following configuration parameters to perform the map and reduce jobs:

The input location of the job in HDFs.
The output location of the job in HDFS.
The input’s and output’s format.
The classes containing map and reduce functions, respectively.
The .jar file for mapper, reducer and driver classes
Question 49. What Is Partitioner And Its Usage?

Answer :

Partitioner is yet another important phase that controls the partitioning of the intermediate map-reduce output keys using a hash function. The process of partitioning determines in what reducer, a key-value pair (of the map output) is sent. The number of partitions is equal to the total number of reduce jobs for the process.

Hash Partitioner is the default class available in Hadoop , which implements the following function.int getPartition(K key, V value, int numReduceTasks)

The function returns the partition number using the numReduceTasks is the number of fixed reducers.

Question 50. What Is Identity Mapper?

Answer :

Identity Mapper is the default Mapper class provided by Hadoop. when no other Mapper class is defined, Identify will be executed. It only writes the input data into output and do not perform and computations and calculations on the input data. The class name is org.apache.hadoop.mapred.lib.IdentityMapper.

Question 51. What Is Recordreader In A Map Reduce?

Answer :

RecordReader is used to read key/value pairs form the InputSplit by converting the byte-oriented view  and presenting record-oriented view to Mapper.

Question 52. What Is Outputcommitter?

Answer :

OutPutCommitter describes the commit of MapReduce task. FileOutputCommitter is the default available class available for OutputCommitter in MapReduce. It performs the following operations:

Create temporary output directory for the job during initialization.
Then, it cleans the job as in removes temporary output directory post job completion.
Sets up the task temporary output.
Identifies whether a task needs commit. The commit is applied if required.
JobSetup, JobCleanup and TaskCleanup are important tasks during output commit.
Question 53. What Are The Parameters Of Mappers And Reducers?

Answer :

The four parameters for mappers are:

LongWritable (input)
text (input)
text (intermediate output)
IntWritable (intermediate output)
The four parameters for reducers are:

Text (intermediate output)
IntWritable (intermediate output)
Text (final output)
IntWritable (final output)
Question 54. What Is A “reducer” In Hadoop?

Answer :

In Hadoop, a reducer collects the output generated by the mapper, processes it, and creates a final output of its own.

Question 55. What Is A “map” In Hadoop?

Answer :

In Hadoop, a map is a phase in HDFS query solving. A map reads data from an input location, and outputs a key value pair according to the input type.

Question 56. Explain Jobconf In Mapreduce?

Answer :

It is a primary interface to define a map-reduce job in the Hadoop for job execution. JobConf specifies mapper, Combiner, partitioner, Reducer,InputFormat , OutputFormat implementations and other advanced job faets liek Comparators.

Question 57. What Is Jobtracker?

Answer :

JobTracker is a Hadoop service used for the processing of MapReduce jobs  in the cluster. It submits and tracks the jobs to specific nodes having data. Only one JobTracker runs on single Hadoop cluster on its own JVM process. if JobTracker goes down, all the jobs halt.

Question 58. Explain Job Scheduling Through Jobtracker?

Answer :

JobTracker communicates with NameNode to identify data location and submits the work to TaskTracker node. The TaskTracker plays a major role as it notifies the JobTracker for any job failure. It actually is referred to the heartbeat reporter reassuring the JobTracker that it is still alive. Later, the JobTracker is responsible for the actions as in it may either resubmit the job or mark a specific record as unreliable or blacklist it.

Question 59. What Is Sequencefileinputformat?

Answer :

A compressed binary output file format to read in sequence files and extends the FileInputFormat.It passes data between output-input (between output of one MapReduce job to input of another MapReduce job)phases of MapReduce jobs.

Question 60. How To Set Mappers And Reducers For Hadoop Jobs?

Answer :

Users can configure JobConf variable to set number of mappers and reducers.

job.setNumMaptasks()
job.setNumreduceTasks()


uestion 1. On What Concept The Hadoop Framework Works?

Answer :

It works on MapReduce, and it is devised by the Google.

Question 2. What Is Mapreduce?

Answer :

Map reduce is an algorithm or concept to process Huge amount of data in a faster way. As per its name you can divide it Map and Reduce.

The main MapReduce job usually splits the input data-set into independent chunks. (Big data sets in the multiple small datasets)
MapTask: will process these chunks in a completely parallel manner (One node can process one or more chunks).The framework sorts the outputs of the maps.
Reduce Task : And the above output will be the input for the reducetasks, produces the final result.
Your business logic would be written in the MappedTask and ReducedTask. Typically both the input and the output of the job are stored in a file-system (Not database). The framework takes care of scheduling tasks, monitoring them and re-executes the failed tasks

Informatica Interview Questions
Question 3. What Is Compute And Storage Nodes?

Answer :

Compute Node: This is the computer or machine where your actual business logic will be executed.

torage Node: This is the computer or machine where your file system reside to store the processing data.

In most of the cases compute node and storage node would be the same machine.

Question 4. How Does Master Slave Architecture In The Hadoop?

Answer :

The MapReduce framework consists of a single master JobTracker and multiple slaves, each cluster-node will have one TaskTracker. The master is responsible for scheduling the jobs' component tasks on the slaves, monitoring them and re-executing the failed tasks. The slaves execute the tasks as directed by the master.

Informatica Tutorial
Question 5. How Does An Hadoop Application Look Like Or Their Basic Components?

Answer :

Minimally an Hadoop application would have following components.

Input location of data
Output location of processed data.
A map task.
A reduced task.
Job configuration
The Hadoop job client then submits the job (jar/executable etc.) and configuration to the JobTracker which then assumes the responsibility of distributing the software / configuration to the slaves, scheduling tasks and monitoring them, providing status and diagnostic information to the job-client.

Teradata Interview Questions
Question 6. Explain How Input And Output Data Format Of The Hadoop Framework?

Answer :

The MapReduce framework operates exclusively on pairs, that is, the framework views the input to the job as a set of pairs and produces a set of pairs as the output of the job, conceivably of different types.

See the flow mentioned below

(input) -> map -> -> combine/sorting -> -> reduce -> (output)

Question 7. What Are The Restriction To The Key And Value Class ?

Answer :

he key and value classes have to be serialized by the framework. To make them serializable Hadoop provides a Writable interface. As you know from the java itself that the key of the Map should be comparable, hence the key has to implement one more interface Writable Comparable.

Teradata Tutorial Java Interview Questions
Question 8. Explain The Wordcount Implementation Via Hadoop Framework ?

Answer :

We will count the words in all the input file flow as below

input Assume there are two files each having a sentence Hello World Hello World (In file 1) Hello World Hello World (In file 2)
Mapper : There would be each mapper for the a file For the given sample input the first map output:
< Hello, 1>
< World, 1>
< Hello, 1>
< World, 1>

The second map output:

< Hello, 1>
< World, 1>
< Hello, 1>
< World, 1>

Combiner/Sorting (This is done for each individual map) So output looks like this The output of the first map:
< Hello, 2>
< World, 2>

The output of the second map:

< Hello, 2>
< World, 2>

Reducer : It sums up the above output and generates the output as below
< Hello, 4>
< World, 4>

Output

Final output would look like

Hello 4 times
World 4 times

Question 9. Which Interface Needs To Be Implemented To Create Mapper And Reducer For The Hadoop?

Answer :

org.apache.hadoop.mapreduce.Mapper
org.apache.hadoop.mapreduce.Reducer

Hadoop MapReduce Interview Questions
Question 10. What Mapper Does?

Answer :

Maps are the individual tasks that transform input records into intermediate records. The transformed intermediate records do not need to be of the same type as the input records. A given input pair may map to zero or many output pairs.

Hadoop Tutorial
Question 11. What Is The Inputsplit In Map Reduce Software?

Answer :

An InputSplit is a logical representation of a unit (A chunk) of input work for a map task; e.g., a file name and a byte range within that file to process or a row set in a text file.

Apache Pig Interview Questions
Question 12. What Is The Inputformat ?

Answer :

The InputFormat is responsible for enumerate (itemise) the InputSplits, and producing a RecordReader which will turn those logical work units into actual physical input records.

Informatica Interview Questions
Question 13. Where Do You Specify The Mapper Implementation?

Answer :

Generally mapper implementation is specified in the Job itself.

Java Tutorial
Question 14. How Mapper Is Instantiated In A Running Job?

Answer :

The Mapper itself is instantiated in the running job, and will be passed a MapContext object which it can use to configure itself.

Question 15. Which Are The Methods In The Mapper Interface?

Answer :

The Mapper contains the run() method, which call its own setup() method only once, it also call a map() method for each input and finally calls it cleanup() method. All above methods you can override in your code.

Machine learning Interview Questions
Question 16. What Happens If You Don't Override The Mapper Methods And Keep Them As It Is?

Answer :

If you do not override any methods (leaving even map as-is), it will act as the identity function, emitting each input record as a separate output.

Hadoop MapReduce Tutorial
Question 17. What Is The Use Of Context Object?

Answer :

The Context object allows the mapper to interact with the rest of the Hadoop system. It Includes configuration data for the job, as well as interfaces which allow it to emit output.

NoSQL Interview Questions
Question 18. How Can You Add The Arbitrary Key-value Pairs In Your Mapper?

Answer :

You can set arbitrary (key, value) pairs of configuration data in your Job, e.g. with
Job.getConfiguration().set("myKey", "myVal"), and then retrieve this data in your mapper with
Context.getConfiguration().get("myKey"). This kind of functionality is typically done in the Mapper's setup() method.

Teradata Interview Questions
Question 19. How Does Mapper's Run() Method Works?

Answer :

The Mapper.run() method then calls map(KeyInType, ValInType, Context) for each key/value pair in the InputSplit for that task

Apache Pig Tutorial
Question 20. Which Object Can Be Used To Get The Progress Of A Particular Job ?

Answer :

Context

HBase Interview Questions
Question 21. What Is Next Step After Mapper Or Maptask?

Answer :

The output of the Mapper are sorted and Partitions will be created for the output. Number of partition depends on the number of reducer.

Question 22. How Can We Control Particular Key Should Go In A Specific Reducer?

Answer :

Users can control which keys (and hence records) go to which Reducer by implementing a custom Partitioned.

HBase Tutorial
Question 23. What Is The Use Of Combiner?

Answer :

It is an optional component or class, and can be specify via Job.setCombinerClass(ClassName), to perform local aggregation of the intermediate outputs, which helps to cut down the amount of data transferred from the Mapper to the Reducer.

MongoDB Interview Questions
Question 24. How Many Maps Are There In A Particular Job?

Answer :

The number of maps is usually driven by the total size of the inputs, that is, the total number of blocks of the input files.

Generally it is around 10-100 maps per-node. Task setup takes awhile, so it is best if the maps take at least a minute to execute.

Suppose, if you expect 10TB of input data and have a block size of 128MB, you'll end up with 82,000 maps, to control the number of block you can use the mapreduce.job.maps parameter (which only provides a hint to the framework). Ultimately, the number of tasks is controlled by the number of splits returned by the InputFormat.getSplits() method (which you can override).

Java Interview Questions
Question 25. What Is The Reducer Used For?

Answer :

Reducer reduces a set of intermediate values which share a key to a (usually smaller) set of values.

The number of reduces for the job is set by the user via Job.setNumReduceTasks(int).

MongoDB Tutorial
Question 26. Explain The Core Methods Of The Reducer?

Answer :

The API of Reducer is very similar to that of Mapper, there's a run() method that receives a Context containing the job's configuration as well as interfacing methods that return data from the reducer itself back to the framework. The run() method calls setup() once, reduce() once for each key associated with the reduce task, and cleanup() once at the end. Each of these methods can access the job's configuration data by using Context.getConfiguration().

As in Mapper, any or all of these methods can be overridden with custom implementations. If none of these methods are overridden, the default reducer operation is the identity function; values are passed through without further processing.

The heart of Reducer is its reduce() method. This is called once per key; the second argument is an Iterable which returns all the values associated with that key.

Data Science R Interview Questions
Question 27. What Are The Primary Phases Of The Reducer?

Answer :

Shuffle, Sort and Reduce.

Hadoop MapReduce Interview Questions
Question 28. Explain The Shuffle?

Answer :

Input to the Reducer is the sorted output of the mappers. In this phase the framework fetches the relevant partition of the output of all the mappers, via HTTP.

Lucene Tutorial
Question 29. Explain The Reducer's Sort Phase?

Answer :

The framework groups Reducer inputs by keys (since different mappers may have output the same key) in this stage. The shuffle and sort phases occur simultaneously; while map-outputs are being fetched they are merged (It is similar to merge-sort).

Question 30. Explain The Reducer's Reduce Phase?

Answer :

In this phase the reduce(MapOutKeyType, Iterable, Context) method is called for each pair in the grouped inputs. The output of the reduce task is typically written to the FileSystem via Context.write (ReduceOutKeyType, ReduceOutValType). Applications can use the Context to report progress, set application-level status messages and update Counters, or just indicate that they are alive. The output of the Reducer is not sorted.

Question 31. How Many Reducers Should Be Configured?

Answer :

The right number of reduces seems to be 0.95 or 1.75 multiplied by
(<no.of nades> * mapreduce.tasktracker.reduce.tasks.maximum).

With 0.95 all of the reduces can launch immediately and start transfering map outputs as the maps finish. With 1.75 the faster nodes will finish their first round of reduces and launch a second wave of reduces doing a much better job of load balancing. Increasing the number of reduces increases the framework overhead, but increases load balancing and lowers the cost of failures.

Question 32. It Can Be Possible That A Job Has 0 Reducers?

Answer :

It is legal to set the number of reduce-tasks to zero if no reduction is desired.

Question 33. What Happens If Number Of Reducers Are 0?

Answer :

In this case the outputs of the map-tasks go directly to the FileSystem, into the output path set by setOutputPath(Path). The framework does not sort the map-outputs before writing them out to the FileSystem.

Apache Pig Interview Questions
Question 34. How Many Instances Of Jobtracker Can Run On A Hadoop Cluster?

Answer :

Only one

Question 35. What Is The Jobtracker And What It Performs In A Hadoop Cluster?

Answer :

JobTracker is a daemon service which submits and tracks the MapReduce tasks to the Hadoop cluster. It runs its own JVM process. And usually it run on a separate machine, and each slave node is configured with job tracker node location. The JobTracker is single point of failure for the Hadoop MapReduce service. If it goes down, all running jobs are halted.

JobTracker in Hadoop performs following actions

Client applications submit jobs to the Job tracker.
The JobTracker talks to the NameNode to determine the location of the data
The JobTracker locates TaskTracker nodes with available slots at or near the data
The JobTracker submits the work to the chosen TaskTracker nodes.
A TaskTracker will notify the JobTracker when a task fails. The JobTracker decides what to do then: it may resubmit the job elsewhere, it may mark that specific record as something to avoid, and it may may even blacklist the TaskTracker as unreliable.
When the work is completed, the JobTracker updates its status.
The TaskTracker nodes are monitored. If they do not submit heartbeat signals often enough, they are deemed to have failed and the work is scheduled on a different TaskTracker.
A TaskTracker will notify the JobTracker when a task fails. The JobTracker decides what to do then: it may resubmit the job elsewhere, it may mark that specific record as something to avoid, and it may may even blacklist the TaskTracker as unreliable.
When the work is completed, the JobTracker updates its status.
Client applications can poll the JobTracker for information.
Question 36. How A Task Is Scheduled By A Jobtracker?

Answer :

The TaskTrackers send out heartbeat messages to the JobTracker, usually every few minutes, to reassure the JobTracker that it is still alive. These messages also inform the JobTracker of the number of available slots, so the JobTracker can stay up to date with where in the cluster work can be delegated. When the JobTracker tries to find somewhere to schedule a task within the MapReduce operations, it first looks for an empty slot on the same server that hosts the DataNode containing the data, and if not, it looks for an empty slot on a machine in the same rack.

Machine learning Interview Questions
Question 37. How Many Instances Of Tasktracker Run On A Hadoop Cluster?

Answer :

There is one Daemon Tasktracker process for each slave node in the Hadoop cluster.

Question 38. What Are The Two Main Parts Of The Hadoop Framework?

Answer :

Hadoop consists of two main parts.

Hadoop distributed file system, a distributed file system with high throughput,
Hadoop MapReduce, a software framework for processing large data sets.
Question 39. Explain The Use Of Tasktracker In The Hadoop Cluster?

Answer :

A Tasktracker is a slave node in the cluster which that accepts the tasks from JobTracker like Map, Reduce or shuffle operation. Tasktracker also runs in its own JVM Process.

Every TaskTracker is configured with a set of slots; these indicate the number of tasks that it can accept. The TaskTracker starts a separate JVM processes to do the actual work (called as Task Instance) this is to ensure that process failure does not take down the task tracker.

The Tasktracker monitors these task instances, capturing the output and exit codes. When the Task instances finish, successfully or not, the task tracker notifies the JobTracker.

The TaskTrackers also send out heartbeat messages to the JobTracker, usually every few minutes, to reassure the JobTracker that it is still alive. These messages also inform the JobTracker of the number of available slots, so the JobTracker can stay up to date with where in the cluster work can be delegated.

Question 40. What Do You Mean By Taskinstance?

Answer :

Task instances are the actual MapReduce jobs which run on each slave node. The TaskTracker starts a separate JVM processes to do the actual work (called as Task Instance) this is to ensure that process failure does not take down the entire task tracker.Each Task Instance runs on its own JVM process. There can be multiple processes of task instance running on a slave node. This is based on the number of slots configured on task tracker. By default a new task instance JVM process is spawned for a task.

NoSQL Interview Questions
Question 41. How Many Daemon Processes Run On A Hadoop Cluster?

Answer :

Hadoop is comprised of five separate daemons. Each of these daemons runs in its own JVM.

Following 3 Daemons run on Master nodes.

NameNode : This daemon stores and maintains the metadata for HDFS.

Secondary NameNode : Performs housekeeping functions for the NameNode.

JobTracker : Manages MapReduce jobs, distributes individual tasks to machines running the Task Tracker. Following 2 Daemons run on each Slave nodes

DataNode : Stores actual HDFS data blocks.

TaskTracker : It is Responsible for instantiating and monitoring individual Map and Reduce tasks.

Question 42. How Many Maximum Jvm Can Run On A Slave Node?

Answer :

One or Multiple instances of Task Instance can run on each slave node. Each task instance is run as a separate JVM process. The number of Task instances can be controlled by configuration. Typically a high end machine is configured to run more task instances.

HBase Interview Questions
Question 43. What Is Nas?

Answer :

It is one kind of file system where data can reside on one centralized machine and all the cluster member will read write data from that shared database, which would not be as efficient as HDFS.

Question 44. How Hdfa Differs With Nfs?

Answer :

Following are differences between HDFS and NAS

In HDFS Data Blocks are distributed across local drives of all machines in a cluster. Whereas in NAS data is stored on dedicated hardware.
HDFS is designed to work with MapReduce System, since computation is moved to data. NAS is not suitable for MapReduce since data is stored separately from the computations.
HDFS runs on a cluster of machines and provides redundancy using replication protocol. Whereas NAS is provided by a single machine therefore does not provide data redundancy.
Question 45. How Does A Namenode Handle The Failure Of The Data Nodes?

Answer :

HDFS has master/slave architecture. An HDFS cluster consists of a single

NameNode, a master server that manages the file system namespace and regulates access to files by clients.

In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on. The NameNode and DataNode are pieces of software designed to run on commodity machines.

NameNode periodically receives a Heartbeat and a Block report from each of the DataNodes in the cluster. Receipt of a Heartbeat implies that the DataNode is functioning properly. A Blockreport contains a list of all blocks on a DataNode. When NameNode notices that it has not received a heartbeat message from a data node after a certain amount of time, the data node is marked as dead. Since blocks will be under replicated the system begins replicating the blocks that were stored on the dead DataNode. The NameNode Orchestrates the replication of data blocks from one DataNode to another. The replication data transfer happens directly between DataNode and the data never passes through the NameNode.

Question 46. Can Reducer Talk With Each Other?

Answer :

No, Reducer runs in isolation.

Question 47. Where The Mapper's Intermediate Data Will Be Stored?

Answer :

The mapper output (intermediate data) is stored on the Local file system (NOT HDFS) of each individual mapper nodes. This is typically a temporary directory location which can be setup in config by the Hadoop administrator. The intermediate data is cleaned up after the Hadoop Job completes.

Question 48. What Is The Use Of Combiners In The Hadoop Framework?

Answer :

Combiners are used to increase the efficiency of a MapReduce program. They are used to aggregate intermediate map output locally on individual mapper outputs. Combiners can help you reduce the amount of data that needs to be transferred across to the reducers.

You can use your reducer code as a combiner if the operation performed is commutative and associative.

The execution of combiner is not guaranteed; Hadoop may or may not execute a combiner. Also, if required it may execute it more than 1 times. Therefore your MapReduce jobs should not depend on the combiners’ execution.

Question 49. What Is The Hadoop Mapreduce Api Contract For A Key And Value Class?

Answer :

The Key must implement the org.apache.hadoop.io.WritableComparable interface.
The value must implement the org.apache.hadoop.io.Writable interface.
Question 50. What Is A Identitymapper And Identityreducer In Mapreduce?

Answer :

org.apache.hadoop.mapred.lib.IdentityMapper: Implements the identity function, mapping inputs directly to outputs. If MapReduce programmer does not set the Mapper Class using JobConf.setMapperClass then IdentityMapper.class is used as a default value.
org.apache.hadoop.mapred.lib.IdentityReducer : Performs no reduction, writing all input values directly to the output. If MapReduce programmer does not set the Reducer Class using JobConf.setReducerClass then IdentityReducer.class is used as a default value.
Question 51. What Is The Meaning Of Speculative Execution In Hadoop? Why Is It Important?

Answer :

Speculative execution is a way of coping with individual Machine performance. In large clusters where hundreds or thousands of machines are involved there may be machines which are not performing as fast as others.

This may result in delays in a full job due to only one machine not performaing well. To avoid this, speculative execution in hadoop can run multiple copies of same map or reduce task on different slave nodes. The results from first node to finish are used.

Question 52. When The Reducers Are Are Started In A Mapreduce Job?

Answer :

In a MapReduce job reducers do not start executing the reduce method until the all Map jobs have completed. Reducers start copying intermediate key-value pairs from the mappers as soon as they are available. The programmer defined reduce method is called only after all the mappers have finished.

If reducers do not start before all mappers finish then why does the progress on MapReduce job shows something like Map(50%) Reduce(10%)? Why reducers progress percentage is displayed when mapper is not finished yet?

Reducers start copying intermediate key-value pairs from the mappers as soon as they are available. The progress calculation also takes in account the processing of data transfer which is done by reduce process, therefore the reduce progress starts showing up as soon as any intermediate key-value pair for a mapper is available to be transferred to reducer.

Though the reducer progress is updated still the programmer defined reduce method is called only after all the mappers have finished.

Question 53. What Is Hdfs ? How It Is Different From Traditional File Systems?

Answer :

HDFS, the Hadoop Distributed File System, is responsible for storing huge data on the cluster. This is a distributed file system designed to run on commodity hardware.

It has many similarities with existing distributed file systems. However, the differences from other distributed file systems are significant.

HDFS is highly fault-tolerant and is designed to be deployed on low-cost hardware.
HDFS provides high throughput access to application data and is suitable for applications that have large data sets.
HDFS is designed to support very large files. Applications that are compatible with HDFS are those that deal with large data sets. These applications write their data only once but they read it one or more times and require these reads to be satisfied at streaming speeds. HDFS supports write-once-read-many semantics on files.
Question 54. What Is Hdfs Block Size? How Is It Different From Traditional File System Block Size?

Answer :

In HDFS data is split into blocks and distributed across multiple nodes in the cluster. Each block is typically 64Mb or 128Mb in size. Each block is replicated multiple times. Default is to replicate each block three times. Replicas are stored on different nodes. HDFS utilizes the local file system to store each HDFS block as a separate file. HDFS Block size can not be compared with the traditional file system block size.

Question 55. What Is A Namenode? How Many Instances Of Namenode Run On A Hadoop Cluster?

Answer :

The NameNode is the centerpiece of an HDFS file system. It keeps the directory tree of all files in the file system, and tracks where across the cluster the file data is kept. It does not store the data of these files itself.

There is only One NameNode process run on any hadoop cluster. NameNode runs on its own JVM process. In a typical production cluster its run on a separate machine.

The NameNode is a Single Point of Failure for the HDFS Cluster. When the NameNode goes down, the file system goes offline.

Client applications talk to the NameNode whenever they wish to locate a file, or when they want to add /copy /move /delete a file. The NameNode responds the successful requests by returning a list of relevant DataNode servers where the data lives.

Question 56. What Is A Datanode? How Many Instances Of Datanode Run On A Hadoop Cluster?

Answer :

A DataNode stores data in the Hadoop File System HDFS. There is only One DataNode process run on any hadoop slave node. DataNode runs on its own JVM process. On startup, a DataNode connects to the NameNode. DataNode instances can talk to each other, this is mostly during replicating data.

Question 57. How The Client Communicates With Hdfs?

Answer :

The Client communication to HDFS happens using Hadoop HDFS API. Client applications talk to the NameNode whenever they wish to locate a file, or when they want to add/copy/move/delete a file on HDFS. The NameNode responds the successful requests by returning a list of relevant DataNode servers where the data lives. Client applications can talk directly to a DataNode, once the NameNode has provided the location of the data.

Question 58. How The Hdfs Blocks Are Replicated?

Answer :

HDFS is designed to reliably store very large files across machines in a large cluster. It stores each file as a sequence of blocks; all blocks in a file except the last block are the same size. The blocks of a file are replicated for fault tolerance. The block size and replication factor are configurable per file. An application can specify the number of replicas of a file. The replication factor can be specified at file creation time and can be changed later. Files in HDFS are write-once and have strictly one writer at any time.

The NameNode makes all decisions regarding replication of blocks. HDFS uses rack-aware replica placement policy. In default configuration there are total 3 copies of a datablock on HDFS, 2 copies are stored on datanodes on same rack and 3rd copy on a different rack.

Question 59. What Is Hadoop Framework?

Answer :

Hadoop is a open source framework which is written in java by apche software foundation. This framework is used to wirite software application which requires to process vast amount of data (It could handle multi tera bytes of data). It works in-paralle on large clusters which could have 1000 of computers (Nodes) on the clusters. It also process data very reliably and fault-tolerant manner.

Question 60. What Is Big Data?

Answer :

Big Data is nothing but an assortment of such a huge and complex data that it becomes very tedious to capture, store, process, retrieve and analyze it with the help of on-hand database management tools or traditional data processing techniques.

Question 61. Can You Give Some Examples Of Big Data?

Answer :

There are many real life examples of Big Data! Facebook is generating 500+ terabytes of data per day, NYSE (New York Stock Exchange) generates about 1 terabyte of new trade data per day, a jet airline collects 10 terabytes of censor data for every 30 minutes of flying time. All these are day to day examples of Big Data!

Question 62. Can You Give A Detailed Overview About The Big Data Being Generated By Facebook?

Answer :

As of December 31, 2012, there are 1.06 billion monthly active users on facebook and 680 million mobile users. On an average, 3.2 billion likes and comments are posted every day on Facebook. 72% of web audience is on Facebook. And why not! There are so many activities going on facebook from wall posts, sharing images, videos, writing comments and liking posts, etc. In fact, Facebook started using Hadoop in mid-2009 and was one of the initial users of Hadoop.

Question 63. According To Ibm, What Are The Three Characteristics Of Big Data?

Answer :

According to IBM, the three characteristics of Big Data are:

Volume: Facebook generating 500+ terabytes of data per day.

Velocity: Analyzing 2 million records each day to identify the reason for losses.

Variety: images, audio, video, sensor data, log files, etc.

Question 64. How Analysis Of Big Data Is Useful For Organizations?

Answer :

Effective analysis of Big Data provides a lot of business advantage as organizations will learn which areas to focus on and which areas are less important. Big data analysis provides some early key indicators that can prevent the company from a huge loss or help in grasping a great opportunity with open hands! A precise analysis of Big Data helps in decision making! For instance, nowadays people rely so much on Facebook and Twitter before buying any product or service. All thanks to the Big Data explosion.

Question 65. How Big Is 'big Data'?

Answer :

With time, data volume is growing exponentially. Earlier we used to talk about Megabytes or Gigabytes. But time has arrived when we talk about data volume in terms of terabytes, petabytes and also zettabytes! Global data volume was around 1.8ZB in 2011 and is expected to be 7.9ZB in 2015. It is also known that the global information doubles in every two years!

Question 66. Who Are 'data Scientists'?

Answer :

Data scientists are soon replacing business analysts or data analysts. Data scientists are experts who find solutions to analyze data. Just as web analysis, we have data scientists who have good business insight as to how to handle a business challenge. Sharp data scientists are not only involved in dealing business problems, but also choosing the relevant issues that can bring value-addition to the organization.

Question 67. Why The Name 'hadoop'?

Answer :

Hadoop doesn’t have any expanding version like ‘oops’. The charming yellow elephant you see is basically named after Doug’s son’s toy elephant!

Question 68. Why Do We Need Hadoop?

Answer :

Everyday a large amount of unstructured data is getting dumped into our machines. The major challenge is not to store large data sets in our systems but to retrieve and analyze the big data in the organizations, that too data present in different machines at different locations. In this situation a necessity for Hadoop arises. Hadoop has the ability to analyze the data present in different machines at different locations very quickly and in a very cost effective way. It uses the concept of MapReduce which enables it to divide the query into small parts and process them in parallel. This is also known as parallel computing.

Question 69. What Are Some Of The Characteristics Of Hadoop Framework?

Answer :

Hadoop framework is written in Java. It is designed to solve problems that involve analyzing large data (e.g. petabytes). The programming model is based on Google’s MapReduce. The infrastructure is based on Google’s Big Data and Distributed File System. Hadoop handles large files/data throughput and supports data intensive distributed applications. Hadoop is scalable as more nodes can be easily added to it.

Question 70. Give A Brief Overview Of Hadoop History?

Answer :

In 2002, Doug Cutting created an open source, web crawler project.

In 2004, Google published MapReduce, GFS papers.

In 2006, Doug Cutting developed the open source, Mapreduce and HDFS project.

In 2008, Yahoo ran 4,000 node Hadoop cluster and Hadoop won terabyte sort benchmark.

In 2009, Facebook launched SQL support for Hadoop.

Question 71. Give Examples Of Some Companies That Are Using Hadoop Structure?

Answer :

A lot of companies are using the Hadoop structure such as Cloudera, EMC, MapR, Hortonworks, Amazon, Facebook, eBay, Twitter, Google and so on.

Question 72. What Is The Basic Difference Between Traditional Rdbms And Hadoop?

Answer :

Traditional RDBMS is used for transactional systems to report and archive the data, whereas Hadoop is an approach to store huge amount of data in the distributed file system and process it. RDBMS will be useful when you want to seek one record from Big data, whereas, Hadoop will be useful when you want Big data in one shot and perform analysis on that later.

Question 73. What Is Structured And Unstructured Data?

Answer :

Structured data is the data that is easily identifiable as it is organized in a structure. The most common form of structured data is a database where specific information is stored in tables, that is, rows and columns. Unstructured data refers to any data that cannot be identified easily. It could be in the form of images, videos, documents, email, logs and random text. It is not in the form of rows and columns.

Question 74. What Are The Core Components Of Hadoop?

Answer :

Core components of Hadoop are HDFS and MapReduce. HDFS is basically used to store large data sets and MapReduce is used to process such large data sets.

Question 75. What Is Hdfs?

Answer :

HDFS is a file system designed for storing very large files with streaming data access patterns, running clusters on commodity hardware.

Question 76. What Are The Key Features Of Hdfs?

Answer :

HDFS is highly fault-tolerant, with high throughput, suitable for applications with large data sets, streaming access to file system data and can be built out of commodity hardware.

Question 77. What Is Fault Tolerance?

Answer :

Suppose you have a file stored in a system, and due to some technical problem that file gets destroyed. Then there is no chance of getting the data back present in that file. To avoid such situations, Hadoop has introduced the feature of fault tolerance in HDFS. In Hadoop, when we store a file, it automatically gets replicated at two other locations also. So even if one or two of the systems collapse, the file is still available on the third system.

Question 78. Replication Causes Data Redundancy Then Why Is Is Pursued In Hdfs?

Answer :

HDFS works with commodity hardware (systems with average configurations) that has high chances of getting crashed any time. Thus, to make the entire system highly fault-tolerant, HDFS replicates and stores data in different places. Any data on HDFS gets stored at at least 3 different locations. So, even if one of them is corrupted and the other is unavailable for some time for any reason, then data can be accessed from the third one. Hence, there is no chance of losing the data. This replication factor helps us to attain the feature of Hadoop called Fault Tolerant.

Question 79. Since The Data Is Replicated Thrice In Hdfs, Does It Mean That Any Calculation Done On One Node Will Also Be Replicated On The Other Two?

Answer :

Since there are 3 nodes, when we send the MapReduce programs, calculations will be done only on the original data. The master node will know which node exactly has that particular data. In case, if one of the nodes is not responding, it is assumed to be failed. Only then, the required calculation will be done on the second replica.

Question 80. What Is Throughput? How Does Hdfs Get A Good Throughput?

Answer :

Throughput is the amount of work done in a unit time. It describes how fast the data is getting accessed from the system and it is usually used to measure performance of the system. In HDFS, when we want to perform a task or an action, then the work is divided and shared among different systems. So all the systems will be executing the tasks assigned to them independently and in parallel. So the work will be completed in a very short period of time. In this way, the HDFS gives good throughput. By reading data in parallel, we decrease the actual time to read data tremendously.

Question 81. What Is Streaming Access?

Answer :

As HDFS works on the principle of ‘Write Once, Read Many‘, the feature of streaming access is extremely important in HDFS. HDFS focuses not so much on storing the data but how to retrieve it at the fastest possible speed, especially while analyzing logs. In HDFS, reading the complete data is more important than the time taken to fetch a single record from the data.

Question 82. What Is A Commodity Hardware? Does Commodity Hardware Include Ram?

Answer :

Commodity hardware is a non-expensive system which is not of high quality or high-availability. Hadoop can be installed in any average commodity hardware. We don’t need super computers or high-end hardware to work on Hadoop. Yes, Commodity hardware includes RAM because there will be some services which will be running on RAM.

Question 83. Is Namenode Also A Commodity?

Answer :

No. Namenode can never be a commodity hardware because the entire HDFS rely on it. It is the single point of failure in HDFS. Namenode has to be a high-availability machine.

Question 84. What Is A Metadata?

Answer :

Metadata is the information about the data stored in data nodes such as location of the file, size of the file and so on.

Question 85. What Is A Daemon?

Answer :

Daemon is a process or service that runs in background. In general, we use this word in UNIX environment. The equivalent of Daemon in Windows is “services” and in Dos is ” TSR”.

Question 86. What Is A Job Tracker?

Answer :

Job tracker is a daemon that runs on a namenode for submitting and tracking MapReduce jobs in Hadoop. It assigns the tasks to the different task tracker. In a Hadoop cluster, there will be only one job tracker but many task trackers. It is the single point of failure for Hadoop and MapReduce Service. If the job tracker goes down all the running jobs are halted. It receives heartbeat from task tracker based on which Job tracker decides whether the assigned task is completed or not.

Question 87. What Is A Task Tracker?

Answer :

Task tracker is also a daemon that runs on datanodes. Task Trackers manage the execution of individual tasks on slave node. When a client submits a job, the job tracker will initialize the job and divide the work and assign them to different task trackers to perform MapReduce tasks. While performing this action, the task tracker will be simultaneously communicating with job tracker by sending heartbeat. If the job tracker does not receive heartbeat from task tracker within specified time, then it will assume that task tracker has crashed and assign that task to another task tracker in the cluster.

Question 88. Is Namenode Machine Same As Datanode Machine As In Terms Of Hardware?

Answer :

It depends upon the cluster you are trying to create. The Hadoop VM can be there on the same machine or on another machine. For instance, in a single node cluster, there is only one machine, whereas in the development or in a testing environment, Namenode and data nodes are on different machines.

Question 89. What Is A Heartbeat In Hdfs?

Answer :

A heartbeat is a signal indicating that it is alive. A datanode sends heartbeat to Namenode and task tracker will send its heart beat to job tracker. If the Namenode or job tracker does not receive heart beat then they will decide that there is some problem in datanode or task tracker is unable to perform the assigned task.

Question 90. Are Namenode And Job Tracker On The Same Host?

Answer :

No, in practical environment, Namenode is on a separate host and job tracker is on a separate host.

Question 91. What Is A 'block' In Hdfs?

Answer :

A ‘block’ is the minimum amount of data that can be read or written. In HDFS, the default block size is 64 MB as contrast to the block size of 8192 bytes in Unix/Linux. Files in HDFS are broken down into block-sized chunks, which are stored as independent units. HDFS blocks are large as compared to disk blocks, particularly to minimize the cost of seeks.

Question 92. If A Particular File Is 50 Mb, Will The Hdfs Block Still Consume 64 Mb As The Default Size?

Answer :

No, not at all! 64 mb is just a unit where the data will be stored. In this particular situation, only 50 mb will be consumed by an HDFS block and 14 mb will be free to store something else. It is the MasterNode that does data allocation in an efficient manner.

Question 93. What Are The Benefits Of Block Transfer?

Answer :

A file can be larger than any single disk in the network. There’s nothing that requires the blocks from a file to be stored on the same disk, so they can take advantage of any of the disks in the cluster. Making the unit of abstraction a block rather than a file simplifies the storage subsystem. Blocks provide fault tolerance and availability. To insure against corrupted blocks and disk and machine failure, each block is replicated to a small number of physically separate machines (typically three). If a block becomes unavailable, a copy can be read from another location in a way that is transparent to the client.

Question 94. If We Want To Copy 10 Blocks From One Machine To Another, But Another Machine Can Copy Only 8.5 Blocks, Can The Blocks Be Broken At The Time Of Replication?

Answer :

In HDFS, blocks cannot be broken down. Before copying the blocks from one machine to another, the Master node will figure out what is the actual amount of space required, how many block are being used, how much space is available, and it will allocate the blocks accordingly.

Question 95. How Indexing Is Done In Hdfs?

Answer :

Hadoop has its own way of indexing. Depending upon the block size, once the data is stored, HDFS will keep on storing the last part of the data which will say where the next part of the data will be. In fact, this is the base of HDFS.

Question 96. If A Data Node Is Full How It's Identified?

Answer :

When data is stored in datanode, then the metadata of that data will be stored in the Namenode. So Namenode will identify if the data node is full.

Question 97. If Datanodes Increase, Then Do We Need To Upgrade Namenode?

Answer :

While installing the Hadoop system, Namenode is determined based on the size of the clusters. Most of the time, we do not need to upgrade the Namenode because it does not store the actual data, but just the metadata, so such a requirement rarely arise.

Question 98. Are Job Tracker And Task Trackers Present In Separate Machines?

Answer :

Yes, job tracker and task tracker are present in different machines. The reason is job tracker is a single point of failure for the Hadoop MapReduce service. If it goes down, all running jobs are halted.

Question 99. When We Send A Data To A Node, Do We Allow Settling In Time, Before Sending Another Data To That Node?

Answer :

Yes, we do.

Question 100. Does Hadoop Always Require Digital Data To Process?

Answer :

Yes. Hadoop always require digital data to be processed.

Question 101. On What Basis Namenode Will Decide Which Datanode To Write On?

Answer :

As the Namenode has the metadata (information) related to all the data nodes, it knows which datanode is free.

Question 102. Doesn't Google Have Its Very Own Version Of Dfs?

Answer :

Yes, Google owns a DFS known as “Google File System (GFS)” developed by Google Inc. for its own use.

Question 103. Who Is A 'user' In Hdfs?

Answer :

A user is like you or me, who has some query or who needs some kind of data.

Question 104. Is Client The End User In Hdfs?

Answer :

No, Client is an application which runs on your machine, which is used to interact with the Namenode (job tracker) or datanode (task tracker).

Question 105. What Is The Communication Channel Between Client And Namenode/datanode?

Answer :

The mode of communication is SSH.

Question 106. What Is A Rack?

Answer :

Rack is a storage area with all the datanodes put together. These datanodes can be physically located at different places. Rack is a physical collection of datanodes which are stored at a single location. There can be multiple racks in a single location.

Question 107. On What Basis Data Will Be Stored On A Rack?

Answer :

When the client is ready to load a file into the cluster, the content of the file will be divided into blocks. Now the client consults the Namenode and gets 3 datanodes for every block of the file which indicates where the block should be stored. While placing the datanodes, the key rule followed is “for every block of data, two copies will exist in one rack, third copy in a different rack“. This rule is known as “Replica Placement Policy“.

Question 108. Do We Need To Place 2nd And 3rd Data In Rack 2 Only?

Answer :

Yes, this is to avoid datanode failure.

Question 109. What If Rack 2 And Datanode Fails?

Answer :

If both rack2 and datanode present in rack 1 fails then there is no chance of getting data from it. In order to avoid such situations, we need to replicate that data more number of times instead of replicating only thrice. This can be done by changing the value in replication factor which is set to 3 by default.

Question 110. What Is A Secondary Namenode? Is It A Substitute To The Namenode?

Answer :

The secondary Namenode constantly reads the data from the RAM of the Namenode and writes it into the hard disk or the file system. It is not a substitute to the Namenode, so if the Namenode fails, the entire Hadoop system goes down.

Question 111. What Is The Difference Between Gen1 And Gen2 Hadoop With Regards To The Namenode?

Answer :

In Gen 1 Hadoop, Namenode is the single point of failure. In Gen 2 Hadoop, we have what is known as Active and Passive Namenodes kind of a structure. If the active Namenode fails, passive Namenode takes over the charge.

Question 112. Can You Explain How Do 'map' And 'reduce' Work?

Answer :

Namenode takes the input and divide it into parts and assign them to data nodes. These datanodes process the tasks assigned to them and make a key-value pair and returns the intermediate output to the Reducer. The reducer collects this key value pairs of all the datanodes and combines them and generates the final output.

Question 113. What Is 'key Value Pair' In Hdfs?

Answer :

Key value pair is the intermediate data generated by maps and sent to reduces for generating the final output.

Question 114. What Is The Difference Between Mapreduce Engine And Hdfs Cluster?

Answer :

HDFS cluster is the name given to the whole configuration of master and slaves where data is stored. Map Reduce Engine is the programming module which is used to retrieve and analyze data.

Question 115. Is Map Like A Pointer?

Answer :

No, Map is not like a pointer.

Question 116. Do We Require Two Servers For The Namenode And The Datanodes?

Answer :

Yes, we need two different servers for the Namenode and the datanodes. This is because Namenode requires highly configurable system as it stores information about the location details of all the files stored in different datanodes and on the other hand, datanodes require low configuration system.

Question 117. Why Are The Number Of Splits Equal To The Number Of Maps?

Answer :

The number of maps is equal to the number of input splits because we want the key and value pairs of all the input splits.

Question 118. Is A Job Split Into Maps?

Answer :

No, a job is not split into maps. Spilt is created for the file. The file is placed on datanodes in blocks. For each split, a map is needed.

Question 119. Which Are The Two Types Of 'writes' In Hdfs?

Answer :

There are two types of writes in HDFS: posted and non-posted write. Posted Write is when we write it and forget about it, without worrying about the acknowledgement. It is similar to our traditional Indian post. In a Non-posted Write, we wait for the acknowledgement. It is similar to the today’s courier services. Naturally, non-posted write is more expensive than the posted write. It is much more expensive, though both writes are asynchronous.

Question 120. Why 'reading' Is Done In Parallel And 'writing' Is Not In Hdfs?

Answer :

Reading is done in parallel because by doing so we can access the data fast. But we do not perform the write operation in parallel. The reason is that if we perform the write operation in parallel, then it might result in data inconsistency. For example, you have a file and two nodes are trying to write data into the file in parallel, then the first node does not know what the second node has written and vice-versa. So, this makes it confusing which data to be stored and accessed.

Question 121. Can Hadoop Be Compared To Nosql Database Like Cassandra?

Answer :

Though NOSQL is the closet technology that can be compared to Hadoop, it has its own pros and cons. There is no DFS in NOSQL. Hadoop is not a database. It’s a file system (HDFS) and distributed programming framework (MapReduce).

Question 122. How Can I Install Cloudera Vm In My System?

Answer :

When you enrol for the hadoop course at Edureka, you can download the Hadoop Installation steps.pdf file from our dropbox.

Question 123. How Jobtracker Schedules A Task?

Answer :

The TaskTrackers send out heartbeat messages to the JobTracker, usually every few minutes, to reassure the JobTracker that it is still alive. These message also inform the JobTracker of the number of available slots, so the JobTracker can stay up to date with where in the cluster work can be delegated. When the JobTracker tries to find somewhere to schedule a task within the MapReduce operations, it first looks for an empty slot on the same server that hosts the DataNode containing the data, and if not, it looks for an empty slot on a machine in the same rack.

Question 124. What Is A Task Tracker In Hadoop? How Many Instances Of Tasktracker Run On A Hadoop Cluster

Answer :

A TaskTracker is a slave node daemon in the cluster that accepts tasks (Map, Reduce and Shuffle operations) from a JobTracker. There is only One Task Tracker process run on any hadoop slave node. Task Tracker runs on its own JVM process. Every TaskTracker is configured with a set of slots, these indicate the number of tasks that it can accept. The TaskTracker starts a separate JVM processes to do the actual work (called as Task Instance) this is to ensure that process failure does not take down the task tracker. The TaskTracker monitors these task instances, capturing the output and exit codes. When the Task instances finish, successfully or not, the task tracker notifies the JobTracker. The TaskTrackers also send out heartbeat messages to the JobTracker, usually every few minutes, to reassure the JobTracker that it is still alive. These message also inform the JobTracker of the number of available slots, so the JobTracker can stay up to date with where in the cluster work can be delegated.

Question 125. What Is A Task Instance In Hadoop? Where Does It Run?

Answer :

Task instances are the actual MapReduce jobs which are run on each slave node. The TaskTracker starts a separate JVM processes to do the actual work (called as Task Instance) this is to ensure that process failure does not take down the task tracker. Each Task Instance runs on its own JVM process. There can be multiple processes of task instance running on a slave node. This is based on the number of slots configured on task tracker. By default a new task instance JVM process is spawned for a task.

Question 126. How Many Daemon Processes Run On A Hadoop System?

Answer :

Hadoop is comprised of five separate daemons. Each of these daemon run in its own JVM.Following 3 Daemons run on Master nodes

NameNode : This daemon stores and maintains the metadata for HDFS.

Secondary NameNode : Performs housekeeping functions for the NameNode.

JobTracker : Manages MapReduce jobs, distributes individual tasks to machines running the Task Tracker.

Following 2 Daemons run on each Slave nodes

DataNode : Stores actual HDFS data blocks.

TaskTracker : Responsible for instantiating and monitoring individual Map and Reduce tasks.

Question 127. What Is Configuration Of A Typical Slave Node On Hadoop Cluster? How Many Jvms Run On A Slave Node?

Answer :

Single instance of a Task Tracker is run on each Slave node. Task tracker is run as a separate JVM process.
Single instance of a DataNode daemon is run on each Slave node. DataNode daemon is run as a separate JVM process.
One or Multiple instances of Task Instance is run on each slave node. Each task instance is run as a separate JVM process. The number of Task instances can be controlled by configuration. Typically a high end machine is configured to run more task instances.
Question 128. What Is The Difference Between Hdfs And Nas ?

Answer :

The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It has many similarities with existing distributed file systems. However, the differences from other distributed file systems are significant.

Following are differences between HDFS and NAS

In HDFS Data Blocks are distributed across local drives of all machines in a cluster. Whereas in NAS data is stored on dedicated hardware.
HDFS is designed to work with MapReduce System, since computation are moved to data. NAS is not suitable for MapReduce since data is stored separately from the computations.
HDFS runs on a cluster of machines and provides redundancy using a replication protocol. Whereas NAS is provided by a single machine therefore does not provide data redundancy.
Question 129. How Namenode Handles Data Node Failures?

Answer :

NameNode periodically receives a Heartbeat and a Blockreport from each of the DataNodes in the cluster. Receipt of a Heartbeat implies that the DataNode is functioning properly. A Blockreport contains a list of all blocks on a DataNode. When NameNode notices that it has not recieved a hearbeat message from a data node after a certain amount of time, the data node is marked as dead. Since blocks will be under replicated the system begins replicating the blocks that were stored on the dead datanode. The NameNode Orchestrates the replication of data blocks from one datanode to another. The replication data transfer happens directly between datanodes and the data never passes through the namenode.

Question 130. Does Mapreduce Programming Model Provide A Way For Reducers To Communicate With Each Other? In A Mapreduce Job Can A Reducer Communicate With Another Reducer?

Answer :

Nope, MapReduce programming model does not allow reducers to communicate with each other. Reducers run in isolation.

Question 131. Can I Set The Number Of Reducers To Zero?

Answer :

Yes, Setting the number of reducers to zero is a valid configuration in Hadoop. When you set the reducers to zero no reducers will be executed, and the output of each mapper will be stored to a separate file on HDFS. [This is different from the condition when reducers are set to a number greater than zero and the Mappers output (intermediate data) is written to the Local file system(NOT HDFS) of each mappter slave node.]

Question 132. Where Is The Mapper Output (intermediate Kay-value Data) Stored ?

Answer :

The mapper output (intermediate data) is stored on the Local file system (NOT HDFS) of each individual mapper nodes. This is typically a temporary directory location which can be setup in config by the hadoop administrator. The intermediate data is cleaned up after the Hadoop Job completes.

Question 133. What Are Combiners? When Should I Use A Combiner In My Mapreduce Job?

Answer :

Combiners are used to increase the efficiency of a MapReduce program. They are used to aggregate intermediate map output locally on individual mapper outputs. Combiners can help you reduce the amount of data that needs to be transferred across to the reducers. You can use your reducer code as a combiner if the operation performed is commutative and associative. The execution of combiner is not guaranteed, Hadoop may or may not execute a combiner. Also, if required it may execute it more then 1 times. Therefore your MapReduce jobs should not depend on the combiners execution.

Question 134. What Is Writable & Writablecomparable Interface?

Answer :

org.apache.hadoop.io.Writable is a Java interface. Any key or value type in the Hadoop Map-Reduce framework implements this interface. Implementations typically implement a static read(DataInput) method which constructs a new instance, calls readFields(DataInput) and returns the instance.
org.apache.hadoop.io.WritableComparable is a Java interface. Any type which is to be used as a key in the Hadoop Map-Reduce framework should implement this interface. WritableComparable objects can be compared to each other using Comparators.
Question 135. What Is A Identitymapper And Identityreducer In Mapreduce ?

Answer :

org.apache.hadoop.mapred.lib.IdentityMapper Implements the identity function, mapping inputs directly to outputs. If MapReduce programmer do not set the Mapper Class using JobConf.setMapperClass then IdentityMapper.class is used as a default value.
org.apache.hadoop.mapred.lib.IdentityReducer Performs no reduction, writing all input values directly to the output. If MapReduce programmer do not set the Reducer Class using JobConf.setReducerClass then IdentityReducer.class is used as a default value.
Question 136. When Is The Reducers Are Started In A Mapreduce Job?

Answer :

In a MapReduce job reducers do not start executing the reduce method until the all Map jobs have completed. Reducers start copying intermediate key-value pairs from the mappers as soon as they are available. The programmer defined reduce method is called only after all the mappers have finished.

Question 137. If Reducers Do Not Start Before All Mappers Finish Then Why Does The Progress On Mapreduce Job Shows Something Like Map(50%) Reduce(10%)? Why Reducers Progress Percentage Is Displayed When Mapper Is Not Finished Yet?

Answer :

Reducers start copying intermediate key-value pairs from the mappers as soon as they are available. The progress calculation also takes in account the processing of data transfer which is done by reduce process, therefore the reduce progress starts showing up as soon as any intermediate key-value pair for a mapper is available to be transferred to reducer. Though the reducer progress is updated still the programmer defined reduce method is called only after all the mappers have finished.

Question 1. Who Is The Provider Of Hadoop?

Answer :

Hadoop forms part of Apache project provided by Apache Software Foundation.

Question 2. What Is Meant By Big Data?

Answer :

Big Data refers to assortment of huge amount of data which is difficult capturing, storing, processing or reprieving. Traditional database management tools cannot handle them but Hadoop can.

Informatica Interview Questions
Question 3. What Are The Operating Systems On Which Hadoop Works?

Answer :

Windows and Linux are the preferred operating system though Hadoop can work on OS x and BSD.

Question 4. What Is The Use Of Hadoop?

Answer :

With Hadoop the user can run applications on the systems that have thousands of nodes spreading through innumerable terabytes. Rapid data processing and transfer among nodes helps uninterrupted operation even when a node fails preventing system failure.

Informatica Tutorial
Question 5. What Is The Use Of Big Data Analysis For An Enterprise?

Answer :

Analysis of Big Data identifies the problem and focus points in an enterprise. It can prevent big losses and make profits helping the entrepreneurs take informed decision.

Teradata Interview Questions
Question 6. What Are Major Characteristics Of Big Data?

Answer :

The three characteristics of Big Data are volume, velocity, and veracity. Earlier it was assessed in megabytes and gigabytes but now the assessment is made in terabytes.

Question 7. Can You Indicate Big Data Examples?

Answer :

Facebook alone generates more than 500 terabytes of data daily whereas many other organizations like Jet Air and Stock Exchange Market generates 1+ terabytes of data every hour. These are Big Data.

Teradata Tutorial Hadoop Interview Questions
Question 8. What Is A Rack In Hdfs?

Answer :

Rack is the storage location where all the data nodes are put together. Thus it is a physical collection of data nodes stored in a single location.

Question 9. How The Client Communicates With Name Node And Data Node In Hdfs?

Answer :

The communication mode for clients with name node and data node in HDFS is SSH.

Java Interview Questions
Question 10. Who Is The ‘user’ In Hdfs?

Answer :

Anyone who tries to retrieve data from database using HDFS is the user. Client is not end user but an application that uses job tracker and task tracker to retrieve data.

Hadoop Tutorial
Question 11. How Name Node Determines Which Data Node To Write On?

Answer :

Name node contains metadata or information in respect of all the data nodes and it will decide which data node to be used for storing data.

Hadoop MapReduce Interview Questions
Question 12. What Type Of Data Is Processed By Hadoop?

Answer :

Hadoop processes the digital data only.

Informatica Interview Questions
Question 13. How A Data Node Is Identified As Saturated?

Answer :

When a data node is full and has no space left the name node will identify it.

Java Tutorial
Question 14. What Is The Process Of Indexing In Hdfs?

Answer :

Once data is stored HDFS will depend on the last part to find out where the next part of data would be stored.

Question 15. Can Blocks Be Broken Down By Hdfs If A Machine Does Not Have The Capacity To Copy As Many Blocks As The User Wants?

Answer :

Blocks in HDFS cannot be broken. Master node calculates the required space and how data would be transferred to a machine having lower space.

Apache Pig Interview Questions
Question 16. What Is Meant By ‘block’ In Hdfs?

Answer :

Block in HDFS refers to minimum quantum of data for reading or writing. Default block size is 64 MB in HDFS. If a file is 52 MB then HDFS would store it and leave 12 MB empty and ready to use.

Hadoop MapReduce Tutorial
Question 17. Is It Necessary That Name Node And Job Tracker Should Be On The Same Host?

Answer :

No! They can be on different hosts.

Machine learning Interview Questions
Question 18. What Is Meant By Heartbeat In Hdfs?

Answer :

Data nodes and task trackers send heartbeat signals to Name node and Job tracker respectively to inform that they are alive. If the signal is not received it would indicate problems with the node or task tracker.

Teradata Interview Questions
Question 19. What Is The Role Played By Task Trackers?

Answer :

Daemons that run on What data nodes, the task tracers take care of individual tasks on slave node as entrusted to them by job tracker.

Apache Pig Tutorial
Question 20. What Is The Function Of ‘job Tracker’?

Answer :

Job tracker is one of the daemons that runs on name node and submits and tracks the MapReduce tasks in Hadoop. There is only one job tracker who distributes the task to various task trackers. When it goes down all running jobs comes to a halt.

NoSQL Interview Questions
Question 21. What Is Daemon?

Answer :

Daemon is the process that runs in background in the UNIX environment. In Windows it is ‘services’ and in DOS it is ‘TSR’.

Question 22. What Is Meant By Data Node?

Answer :

Data node is the slave deployed in each of the systems and provides the actual storage locations and serves read and writer requests for clients.

HBase Tutorial
Question 23. Which One Is The Master Node In Hdfs? Can It Be Commodity?

Answer :

Name node is the master node in HDFS and job tracker runs on it. The node contains metadata and works as high availability machine and single pint of failure in HDFS. It cannot be commodity as the entire HDFS works on it.

HBase Interview Questions
Question 24. What Is Meant By ‘commodity Hardware’? Can Hadoop Work On Them?

Answer :

Average and non-expensive systems are known as commodity hardware and Hadoop can be installed on any of them. Hadoop does not require high end hardware to function.

Hadoop Interview Questions
Question 25. What Is Meant By Streaming Access?

Answer :

HDFS works on the principle of “write once, read many” and the focus is on fast and accurate data retrieval. Steaming access refers to reading the complete data instead of retrieving single record from the database.

MongoDB Tutorial
Question 26. Would The Calculations Made On One Node Be Replicated To Others In Hdfs?

Answer :

No! The calculation would be made on the original node only. In case the node fails then only the master node would replicate the calculation on to a second node.

MongoDB Interview Questions
Question 27. Why Replication Is Pursued In Hdfs Though It May Cause Data Redundancy?

Answer :

Systems with average configuration are vulnerable to crash at any time. HDFS replicates and stores data at three different locations that makes the system highly fault tolerant. If data at one location becomes corrupt and is inaccessible it can be retrieved from another location.

This insightful Cloudera article shows the steps for running HDFS on a cluster.

Java Interview Questions
Question 28. What Are The Main Features Of Hdfs?

Answer :

Great fault tolerance, high throughput, suitability for handling large data sets, and streaming access to file system data are the main features of HDFS. It can be built with commodity hardware.

Lucene Tutorial
Question 29. What Is Hdfs?

Answer :

HDFS is filing system use to store large data files. It handles streaming data and running clusters on the commodity hardware.

Data Science R Interview Questions
Question 30. What Are The Main Components Of Hadoop?

Answer :

Main components of Hadoop are HDFS used to store large databases and MapReduce used to analyze them.

Question 31. How Is Hadoop Different From Traditional Rdbms?

Answer :

RDBMS can be useful for single files and short data whereas Hadoop is useful for handling Big Data in one shot.

Question 32. Which Are The Major Players On The Web That Uses Hadoop?

Answer :

Introduce in 2002 by Doug Cutting, Hadoop was used in Google MapReduce and HDFS project in 2004 and 2006. Yahoo and Facebook adopted it in 2008 and 2009 respectively. Major commercial enterprises using Hadoop include EMC, Hortonworks, Cloudera, MaOR, Twitter, EBay, and Amazon among others.

Question 33. What Are The Basic Characteristics Of Hadoop?

Answer :

Written in Java, Hadoop framework has the capability of solving issues involving Big Data analysis. Its programming model is based on Google MapReduce and infrastructure is based on Google’s Big Data and distributed file systems. Hadoop is scalable and more nodes can be added to it.



Question 1. Explain About The Hadoop-core Configuration Files?

Answer :

Hadoop core is specified by two resources. It is configured by two well written xml files which are loaded from the classpath:

Hadoop-default.xml - Read-only defaults for Hadoop, suitable for a single machine instance.
Hadoop-site.xml - It specifies the site configuration for Hadoop distribution. The cluster specific information is also provided by the Hadoop administrator.
Question 2. Explain In Brief The Three Modes In Which Hadoop Can Be Run?

Answer :

The three modes in which Hadoop can be run are:

Standalone (local) mode - No Hadoop daemons running, everything runs on a single Java Virtual machine only.
Pseudo-distributed mode - Daemons run on the local machine, thereby simulating a cluster on a smaller scale.
Fully distributed mode - Runs on a cluster of machines.
Python Interview Questions
Question 3. Explain What Are The Features Of Standalone (local) Mode?

Answer :

In stand-alone or local mode there are no Hadoop daemons running,  and everything runs on a single Java process. Hence, we don't get the benefit of distributing the code across a cluster of machines. Since, it has no DFS, it utilizes the local file system. This mode is suitable only for running MapReduce programs by developers during various stages of development. Its the best environment for learning and good for debugging purposes.

Question 4. What Are The Features Of Fully Distributed Mode?

Answer :

In Fully Distributed mode, the clusters range from a few nodes to 'n' number of nodes. It is used in production environments, where we have thousands of machines in the Hadoop cluster. The daemons of Hadoop run on these clusters. We have to configure separate masters and separate slaves in this distribution, the implementation of which is quite complex. In this configuration, Namenode and Datanode runs on different hosts and there are nodes on which task tracker runs. The root of the distribution is referred as HADOOP_HOME.

Python Tutorial
Question 5. Explain What Are The Main Features Of Pseudo Mode?

Answer :

In Pseudo-distributed mode, each Hadoop daemon runs in a separate Java process, as such it simulates a cluster though on a small scale. This mode is used both for development and QA environments. Here, we need to do the configuration changes.

Hadoop Interview Questions
Question 6. What Are The Hadoop Configuration Files At Present?

Answer :

There are 3 configuration files in Hadoop:

1. conf/core-site.xml:

fs.default.name

hdfs: //localhost:9000

2. conf/hdfs-site.xml:

dfs.replication 1

3. conf/mapred-site.xml:

mapred.job.tracker local host: 9001

Question 7. Can You Name Some Companies That Are Using Hadoop?

Answer :

Numerous companies are using Hadoop, from large Software Companies, MNCs to small organizations. Yahoo is the top contributor with many open source Hadoop Softwares and frameworks. Social Media Companies like Facebook and Twitter have been using for a long time now for storing their mammoth data. Apart from that Netflix, IBM, Adobe and e-commerce websites like Amazon and eBay are also using multiple Hadoop technologies.

Hadoop Tutorial Java Interview Questions
Question 8. Which Is The Directory Where Hadoop Is Installed?

Answer :

Cloudera and Apache have the same directory structure. Hadoop is installed in cd /usr/lib/hadoop-0.20/.

Question 9. What Are The Port Numbers Of Name Node, Job Tracker And Task Tracker?

Answer :

The port number for Namenode is ’70′, for job tracker is ’30′ and for task tracker is ’60′.

Apache Hive Interview Questions
Question 10. Tell Us What Is A Spill Factor With Respect To The Ram?

Answer :

Spill factor is the size after which your files move to the temp file. Hadoop-temp directory is used for this. Default value for io.sort.spill.percent is 0.80. A value less than 0.5 is not recommended.

Java Tutorial
Question 11. Is Fs.mapr.working.for A Single Directory?

Answer :

Yes, fs.mapr.working.dir it is just one directory.

Hadoop MapReduce Interview Questions
Question 12. Which Are The Three Main Hdfs-site.xml Properties?

Answer :

The three main hdfs-site.xml properties are:

Dfs.name.dir which gives you the location on which metadata will be stored and where DFS is located – on disk or onto the remote.
Dfs.data.dir which gives you the location where the data is going to be stored.
Fs.checkpoint.dir which is for secondary Namenode.
Python Interview Questions
Question 13. How To Come Out Of The Insert Mode?

Answer :

To come out of the insert mode, press ESC,

Type: q (if you have not written anything) OR

Type: wq (if you have written anything in the file) and then press ENTER.

Apache Hive Tutorial
Question 14. Tell Us What Cloudera Is And Why It Is Used In Big Data?

Answer :

Cloudera is the leading Hadoop distribution vendor on the Big Data market, its termed as the next-generation data management software that is required for business critical data challenges that includes access, storage, management, business analytics, systems security, and search.

Question 15. We Are Using Ubuntu Operating System With Cloudera, But From Where We Can Download Hadoop Or Does It Come By Default With Ubuntu?

Answer :

This is a default configuration of Hadoop that you have to download from Cloudera or from eureka’s Dropbox and the run it on your systems. You can also proceed with your own configuration but you need a Linux box, be it Ubuntu or Red hat. There are installations steps present at the Cloudera location or in Eureka’s Drop box. You can go either ways.

Apache Pig Interview Questions
Question 16. What Is The Main Function Of The ‘jps’ Command?

Answer :

The jps’ command checks whether the Datanode, Namenode, tasktracker, jobtracker, and other components are working or not in Hadoop. One thing to remember is that if you have started Hadoop services with sudo then you need to run JPS with sudo privileges else the status will be not shown.

Hadoop MapReduce Tutorial
Question 17. How Can I Restart Namenode?

Answer :

Click on stop-all.sh and then click on start-all.sh OR
Write sudo hdfs (press enter), su-hdfs (press enter), /etc/init.d/ha (press enter) and then /etc/init.d/hadoop-0.20-namenode start (press enter).
Hadoop Administration Interview Questions
Question 18. How Can We Check Whether Namenode Is Working Or Not?

Answer :

To check whether Namenode is working or not, use the command /etc/init.d/hadoop- 0.20-namenode status or as simple as jps’.

Hadoop Interview Questions
Question 19. What Is "fsck" And What Is Its Use?

Answer :

"fsck" is File System Check. FSCK is used to check the health of a Hadoop Filesystem. It generates a summarized report of the overall health of the filesystem.

Usage:  hadoop fsck /

Apache Pig Tutorial
Question 20. At Times You Get A ‘connection Refused Java Exception’ When You Run The File System Check Command Hadoop Fsck /?

Answer :

The most possible reason is that the Namenode is not working on your VM.

Hadoop Distributed File System (HDFS) Interview Questions
Question 21. What Is The Use Of The Command Mapred.job.tracker?

Answer :

The command mapred.job.tracker is used by the Job Tracker to list out which host and port that the MapReduce job tracker runs at. If it is "local", then jobs are run in-process as a single map and reduce task.

Question 22. What Does /etc /init.d Do?

Answer :

/etc /init.d specifies where daemons (services) are placed or to see the status of these daemons. It is very LINUX specific, and nothing to do with Hadoop.

Question 23. How Can We Look For The Namenode In The Browser?

Answer :

If you have to look for Namenode in the browser, you don’t have to give localhost: 8021, the port number to look for Namenode in the browser is 50070.

Java Hadoop Developer Interview Questions
Question 24. How To Change From Su To Cloudera?

Answer :

To change from SU to Cloudera just type exit.

Java Interview Questions
Question 25. Which Files Are Used By The Startup And Shutdown Commands?

Answer :

Slaves and Masters are used by the startup and the shutdown commands.

Question 26. What Do Masters And Slaves Consist Of?

Answer :

Masters contain a list of hosts, one per line, that are to host secondary namenode servers. Slaves consist of a list of hosts, one per line, that host datanode and task tracker servers.

Hadoop Testing Interview Questions
Question 27. What Is The Function Of Hadoop-env.sh? Where Is It Present?

Answer :

This file contains some environment variable settings used by Hadoop; it provides the environment for Hadoop to run. The path of JAVA_HOME is set here for it to run properly. Hadoop-env.sh file is present in the conf/hadoop-env.sh location. You can also create your own custom configuration file conf/hadoop-user-env.sh, which will allow you to override the default Hadoop settings.

Apache Hive Interview Questions
Question 28. Can We Have Multiple Entries In The Master Files?

Answer :

Yes, we can have multiple entries in the Master files.

Question 29. In Hadoop_pid_dir, What Does Pid Stands For?

Answer :

PID stands for ‘Process ID’.

Question 30. What Does Hadoop-metrics? Properties File Do?

Answer :

Hadoop-metrics Properties is used for ‘Reporting‘purposes. It controls the reporting for hadoop. The default status is ‘not to report‘.

Question 31. What Are The Network Requirements For Hadoop?

Answer :

The Hadoop core uses Shell (SSH) to launch the server processes on the slave nodes. It requires password-less SSH connection between the master and all the slaves and the Secondary machines.

Question 32. Why Do We Need A Password-less Ssh In Fully Distributed Environment?

Answer :

We need a password-less SSH in a Fully-Distributed environment because when the cluster is LIVE and running in Fully Distributed environment, the communication is too frequent. The job tracker should be able to send a task to task tracker quickly.

Question 33. What Will Happen If A Namenode Has No Data?

Answer :

If a Namenode has no data it cannot be considered as a Namenode. In practical terms, Namenode needs to have some data.

Hadoop MapReduce Interview Questions
Question 34. What Happens To Job Tracker When Namenode Is Down?

Answer :

Namenode is the main point which keeps all the metadata, keep tracks of failure of datanode with the help of heart beats. As such when a namenode is down, your cluster will be completely down, because Namenode is the single point of failure in a Hadoop Installation.

Question 35. Explain What Do You Mean By Formatting Of The Dfs?

Answer :

Like we do in Windows, DFS is formatted for proper structuring of data. It is not usually recommended to do as it format the Namenode too in the process, which is not desired.

Question 36. We Use Unix Variants For Hadoop. Can We Use Microsoft Windows For The Same?

Answer :

In practicality, Ubuntu and Red Hat Linux are the best Operating Systems for Hadoop. On the other hand, Windows can be used but it is not used frequently for installing Hadoop as there are many support problems related to it. The frequency of crashes and the subsequent restarts makes it unattractive. As such, Windows is not recommended as a preferred environment for Hadoop Installation, though users can give it a try for learning purposes in the initial stage.

Apache Pig Interview Questions
Question 37. Which One Decides The Input Split - Hdfs Client Or Namenode?

Answer :

The HDFS Client does not decide. It is already specified in one of the configurations through which input split is already configured.

Question 38. Let’s Take A Scenario, Let’s Say We Have Already Cloudera In A Cluster, Now If We Want To Form A Cluster On Ubuntu Can We Do It. Explain In Brief?

Answer :

Yes, we can definitely do it. We have all the useful installation steps for creating a new cluster. The only thing that needs to be done is to uninstall the present cluster and install the new cluster in the targeted environment.

Question 39. Can You Tell Me If We Can Create A Hadoop Cluster From Scratch?

Answer :

Yes, we can definitely do that.  Once we become familiar with the Apache Hadoop environment, we can create a cluster from scratch.

Question 40. Explain The Significance Of Ssh? What Is The Port On Which Port Does Ssh Work? Why Do We Need Password In Ssh Local Host?

Answer :

SSH is a secure shell communication, is a secure protocol and the most common way of administering remote servers safely, relatively very simple and inexpensive to implement. A single SSH connection can host multiple channels and hence can transfer data in both directions. SSH works on Port No. 22, and it is the default port number. However, it can be configured to point to a new port number, but its not recommended. In local host, password is required in SSH for security and in a situation where password less communication is not set.

Hadoop Administration Interview Questions
Question 41. What Is Ssh? Explain In Detail About Ssh Communication Between Masters And The Slaves?

Answer :

Secure Socket Shell or SSH is a password-less secure communication that provides administrators with a secure way to access a remote computer and data packets are sent across the slave. This network protocol also has some format into which data is sent across. SSH communication is not only between masters and slaves but also between two hosts in a network.  SSH appeared in 1995 with the introduction of SSH - 1. Now SSH 2 is in use, with the vulnerabilities coming to the fore when Edward Snowden leaked information by decrypting some SSH traffic.

Question 42. Can You Tell Is What Will Happen To A Namenode, When Job Tracker Is Not Up And Running?

Answer :

When the job tracker is down, it will not be in functional mode, all running jobs will be halted because it is a single point of failure. Your whole cluster will be down but still Namenode will be present. As such the cluster will still be accessible if Namenode is working, even if the job tracker is not up and running. But you cannot run your Hadoop job.