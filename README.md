# Interview questions for Data Engineer

+ [Apache Hadoop](#Apache Hadoop)
+ [Apache Flume](#Apache Flume)
+ [Apache NiFi](#Apache NiFi)
+ [Apache Avro](#Apache Avro)
+ [Apache Kafka](#Apache Kafka)
+ [Apache Impala](#Apache Impala)



## Apache Hadoop
+ [What are the main components of a Hadoop Application?](hadoop.md#What-are-the-main-components-of-a-Hadoop-Application)
+ [What is the core concept behind Apache Hadoop framework?](hadoop.md#What-is-the-core-concept-behind-Apache-Hadoop-framework)
+ [What is Hadoop Streaming?](hadoop.md#What-is-Hadoop-Streaming)
+ [What is the difference between Nodes in HDFS?](hadoop.md#What-is-the-difference-between-Nodes-in-HDFS)
+ [What is the optimum hardware configuration to run Apache Hadoop?](hadoop.md#What-is-the-optimum-hardware-configuration-to-run-Apache-Hadoop)
+ [What do you know about Block and Block scanner in HDFS?](hadoop.md#What-do-you-know-about-Block-and-Block-scanner-in-HDFS)
+ [What are the default port numbers on which  Nodes run in Hadoop?](hadoop.md#What-are-the-default-port-numbers-on-which-Nodes-run-in-Hadoop)
+ [How will you disable a Block Scanner on HDFS DataNode?](hadoop.md#How-will-you-disable-a-Block-Scanner-on-HDFS-DataNode)
+ [How will you get the distance between two nodes in Apache Hadoop?](hadoop.md#How-will-you-get-the-distance-between-two-nodes-in-Apache-Hadoop)
+ [Why do we use commodity hardware in Hadoop?](hadoop.md#Why-do-we-use-commodity-hardware-in-Hadoop)
+ [How does inter cluster data copying works in Hadoop?](hadoop.md#How-does-inter-cluster-data-copying-works-in-Hadoop)
+ [How can we update a file at an arbitrary location in HDFS?](hadoop.md#How-can-we-update-a-file-at-an-arbitrary-location-in-HDFS)
+ [What is Replication factor in HDFS?](hadoop.md#What-is-Replication-factor-in-HDFS)
+ [What is the difference between NAS and DAS in Hadoop cluster?](hadoop.md#What-is-the-difference-between-NAS-and-DAS-in-Hadoop-cluster)
+ [What are the two messages that NameNode receives from DataNode?](hadoop.md#What-are-the-two-messages-that-NameNode-receives-from-DataNode)
+ [How does indexing work in Hadoop?](hadoop.md#How-does-indexing-work-in-Hadoop)
+ [What data is stored in a HDFS NameNode?](hadoop.md#What-data-is-stored-in-a-HDFS-NameNode)
+ [What would happen if NameNode crashes in a HDFS cluster?](hadoop.md#What-would-happen-if-NameNode-crashes-in-a-HDFS-cluster)
+ [What are the main functions of Secondary NameNode?](hadoop.md#What-are-the-main-functions-of-Secondary-NameNode)
+ [What happens if HDFS file is set with replication factor of 1 and DataNode crashes?](hadoop.md#What-happens-if-HDFS-file-is-set-with-replication-factor-of-1-and-DataNode-crashes)
+ [What is the meaning of Rack Awareness in Hadoop?](hadoop.md#What-is-the-meaning-of-Rack-Awareness-in-Hadoop)
+ [How will you check if a file exists in HDFS?](hadoop.md#How-will-you-check-if-a-file-exists-in-HDFS)
+ [Why do we use fsck command in HDFS?](hadoop.md#Why-do-we-use-fsck-command-in-HDFS)
+ [What will happen when NameNode is down and a user submits a new job?](hadoop.md#What-will-happen-when-NameNode-is-down-and-a-user-submits-a-new-job)
+ [What are the core methods of a Reducer in Hadoop?](hadoop.md#What-are-the-core-methods-of-a-Reducer-in-Hadoop)
+ [What are the primary phases of a Reducer in Hadoop?](hadoop.md#What-are-the-primary-phases-of-a-Reducer-in-Hadoop)
+ [What is the use of Context object in Hadoop?](hadoop.md#What-is-the-use-of-Context-object-in-Hadoop)
+ [How does partitioning work in Hadoop?](hadoop.md#How-does-partitioning-work-in-Hadoop)
+ [What is a Combiner in Hadoop?](hadoop.md#What-is-a-Combiner-in-Hadoop)
+ [What is the default replication factor in HDFS?](hadoop.md#What-is-the-default-replication-factor-in-HDFS)
+ [How much storage is allocated by HDFS for storing a file of 25 MB size?](hadoop.md#How-much-storage-is-allocated-by-HDFS-for-storing-a-file-of-25-MB-size)
+ [Why does HDFS store data in Block structure?](hadoop.md#Why-does-HDFS-store-data-in-Block-structure)
+ [How will you create a custom Partitioner in a Hadoop job?](hadoop.md#How-will-you-create-a-custom-Partitioner-in-a-Hadoop-job)
+ [What is a Checkpoint node in HDFS?](hadoop.md#What-is-a-Checkpoint-node-in-HDFS)
+ [What is a Backup Node in HDFS?](hadoop.md#What-is-a-Backup-Node-in-HDFS)
+ [What is the meaning of term Data Locality in Hadoop?](hadoop.md#What-is-the-meaning-of-term-Data-Locality-in-Hadoop)
+ [What is a Balancer in HDFS?](hadoop.md#What-is-a-Balancer-in-HDFS)
+ [What are the important points a NameNode considers before selecting the DataNode for placing a data block?](hadoop.md#What-are-the-important-points-a-NameNode-considers-before-selecting-the-DataNode-for-placing-a-data-block)
+ [How will you replace HDFS data volume before shutting down a DataNode?](hadoop.md#How-will-you-replace-HDFS-data-volume-before-shutting-down-a-DataNode)
+ [What are the important configuration files in Hadoop?](hadoop.md#What-are-the-important-configuration-files-in-Hadoop)
+ [How will you monitor memory used in a Hadoop cluster?](hadoop.md#How-will-you-monitor-memory-used-in-a-Hadoop-cluster)
+ [Why do we need Serialization in Hadoop map reduce methods?](hadoop.md#Why-do-we-need-Serialization-in-Hadoop-map-reduce-methods)
+ [What is the use of Distributed Cache in Hadoop?](hadoop.md#What-is-the-use-of-Distributed-Cache-in-Hadoop)
+ [How will you synchronize the changes made to a file in Distributed Cache in Hadoop?](hadoop.md#How-will-you-synchronize-the-changes-made-to-a-file-in-Distributed-Cache-in-Hadoop)
+ [Can you elaborate about Mapreduce Job](hadoop.md#Can-you-elaborate-about-Mapreduce-job)
+ [Why compute nodes and the storage nodes are the same?](hadoop.md#Why-compute-nodes-and-the-storage-nodes-are-the-same)
+ [What is the configuration object importance in Mapreduce?](hadoop.md#What-is-the-configuration-object-importance-in-Mapreduce)
+ [Where Mapreduce not recommended?](hadoop.md#Where-Mapreduce-not-recommended?)
+ [What is Namenode and it’s responsibilities?](hadoop.md#What-is-Namenode-and-it’s-responsibilities)
+ [What is Jobtracker’s responsibility?](hadoop.md#What-is-Jobtracker’s-responsibility)
+ [What are the Jobtracker and Tasktracker?](hadoop.md#What-are-the-Jobtracker-and-Tasktracker)
+ [What is Job scheduling importance in Hadoop Mapreduce?](hadoop.md#What-is-Job-scheduling-importance-in-Hadoop-Mapreduce)
+ [When used Reducer?](hadoop.md#When-used-Reducer)
+ [Where the Shuffle and Sort process does?](hadoop.md#Where-the-Shuffle-and-Sort-process-does)
+ [Java is mandatory to write Mapreduce Jobs?](hadoop.md#Java-is-mandatory-to-write-Mapreduce-Jobs)
+ [What methods can controle the Map And Reduce function’s output?](hadoop.md#What-methods-can-controle-the-Map-And-Reduce-function’s-output)
+ [What is the main difference between Mapper And Reducer?](hadoop.md#What-is-the-main-difference-between-Mapper-And-Reducer)
+ [Why compute Nodes and the Storage Nodes are same?](hadoop.md#Why-compute-Nodes-and-the-Storage-Nodes-are-same?)
+ [What is difference between mapside join and reduce side join?](hadoop.md#What-is-difference-between-mapside-join-and-reduce-side-join)
+ [What happen if number of Reducer is 0?](hadoop.md#What-happen-if-number-of-Reducer-is-0)
+ [When we are goes to Combiner? Why it is Recommendable?](hadoop.md#When-we-are-goes-to-Combiner)
+ [What is the main difference between Mapreduce Combiner and Reducer?](hadoop.md#What-is-the-main-difference-between-Mapreduce-Combiner-and-Reducer)
+ [What Is Partition?](hadoop.md#What-is-partition)
+ [When we goes to Partition?](hadoop.md#When-we-goes-to-Partition)
+ [What are the important steps when you are partitioning table?](hadoop.md#What-are-the-important-steps-when-you-are-partitioning-table)
+ [Can you elaborate Mapreduce Job architecture?](hadoop.md#Can-you-elaborate-Mapreduce-Job-architecture)
+ [Why task Tracker launch child Jvm?](hadoop.md#Why-task-Tracker-launch-child-Jvm)
+ [Why JobClient and Job Tracker submits job resources to file system?](hadoop.md#Why-Jobclient-and-Job-Tracker-submits-job-resources-to-file-system)
+ [How many Mappers and Reducers can run?](hadoop.md#How-many-Mappers-and-Reducers-can-run)
+ [What is InputSplit?](hadoop.md#What-is-Inputsplit)
+ [How to configure the split value?](hadoop.md#How-to-configure-the-split-value)
+ [How much ram required to process 64mb data?](hadoop.md#How-much-ram-required-to-process-64mb-data)
+ [What is difference between block And split?](hadoop.md#What-is-difference-between-block-And-split)
+ [Why Hadoop Framework reads a file parallel why not sequential?](hadoop.md#Why-Hadoop-Framework-reads-a-file-parallel-why-not-sequential)
+ [If I am change block size from 64 to 128?](hadoop.md#If-I-am-change-block-size-from-64-to-128)
+ [What is IsSplitable()?](hadoop.md#What-is-Issplitable())
+ [How much Hadoop allows maximum block size and minimum block size?](hadoop.md#How-much-Hadoop-allows-maximum-block-size-and-minimum-block-size)
+ [What are the Job Resource files?](hadoop.md#What-are-the-Job-Resource-files)
+ [What’s the Mapreduce Job consists?](hadoop.md#What’s-the-Mapreduce-Job-consists)
+ [What is the data locality?](hadoop.md#What-is-the-data-locality)
+ [What is speculative execution?](hadoop.md#What-is-speculative-execution)
+ [What is chain Mapper?](hadoop.md#What-is-chain-Mapper)
+ [How to do value level comparison?](hadoop.md#How-to-do-value-level-comparison)
+ [What is setup and clean up methods?](hadoop.md#What-is-setup-and-clean-up-methods)
+ [How many slots allocate for each task?](hadoop.md#How-many-slots-allocate-for-each-task)
+ [Why TaskTracker launch child Jvm to do a task? Why not use Existent Jvm?](hadoop.md#Why-Tasktracker-launch-child-Jvm-to-do-a-task)
+ [What main configuration parameters are specified in Mapreduce?](hadoop.md#What-main-configuration-parameters-are-specified-in-Mapreduce)
+ [What is identity Mapper?](hadoop.md#What-is-identity-Mapper)
+ [What is RecordReader in a MapReduce?](hadoop.md#What-is-RecordReader-in-a-MapReduce)
+ [What is OutputCommitter?](hadoop.md#What-is-OutputCommitter)
+ [What are the parameters of Mappers and Reducers?](hadoop.md#What-are-the-parameters-of-Mappers-and-Reducers)
+ [Explain JobConf in Mapreduce?](hadoop.md#Explain-Jobconf-in-Mapreduce)
+ [Explain Job scheduling through Jobtracker?](hadoop.md#Explain-Job-scheduling-through-Jobtracker)
+ [What is SequenceFileInputFormat?](hadoop.md#What-is-SequenceFileInputFormat)
+ [Explain how input and output data format of the Hadoop Framework?](hadoop.md#Explain-how-input-and-output-data-format-of-the-Hadoop-Framework)
+ [What are the restriction to the Key and Value Class ?](hadoop.md#What-are-the-restriction-to-the-Key-and-Value-Class)
+ [Explain the wordcount implementation via Hadoop Framework?](hadoop.md#Explain-the-wordcount-implementation-via-Hadoop-Framework)
+ [How Mapper is instantiated in a running Job?](hadoop.md#How-Mapper-is-instantiated-in-a-running-Job)
+ [Which are the methods in the Mapper Interface?](hadoop.md#Which-are-the-methods-in-the-Mapper-Interface)
+ [What happens if You don't Override the Mapper methods and keep them as it is?](hadoop.md#What-happens-if-You-don't-Override-the-Mapper-methods-and-keep-them-as-it-is)
+ [What is the use of context Object?](hadoop.md#What-is-the-use-of-context-Object)
+ [How can you Add the arbitrary Key-value pairs in your Mapper?](hadoop.md#How-can-you-Add-the-arbitrary-Key-value-pairs-in-your-Mapper)
+ [How Does Mapper's Run() Method Works?](hadoop.md#How-does-Mapper's-run-method-works)
+ [Which Object can be used to get the progress of a particular Job?](hadoop.md#Which-Object-can-be-used-to-get-the-progress-of-a-particular-Job)
+ [What is next step after Mapper Or Maptask?](hadoop.md#What-is-next-step-after-Mapper-Or-Maptask)
+ [How can we control particular Key should go in a specific Reducer?](hadoop.md#How-can-we-control-particular-Key-should-go-in-a-specific-Reducer)
+ [What is the use of Combiner?](hadoop.md#What-is-the-use-of-Combiner)
+ [How many Maps are there in a particular Job?](hadoop.md#How-many-Maps-are-there-in-a-particular-Job)
+ [What is the Reducer used for?](hadoop.md#What-is-the-Reducer-used-for)
+ [Explain the core methods of the Reducer?](hadoop.md#Explain-the-core-methods-of-the-Reducer)
+ [What are the primary phases of the Reducer?](hadoop.md#What-are-the-primary-phases-of-the-Reducer)
+ [Explain the Shuffle?](hadoop.md#Explain-the-Shuffle)
+ [Explain the Reducer's sort phase?](hadoop.md#Explain-the-Reducer's-sort-phase)
+ [Explain the Reducer's reduce phase?](hadoop.md#Explain-the-Reducer's-reduce-phase)
+ [How many Reducers should be configured?](hadoop.md#How-many-Reducers-should-be-configured)
+ [It can be possible that a Job has 0 Reducers?](hadoop.md#It-can-be-possible-that-a-Job-has-0-Reducers)
+ [What happens if number of Reducers are 0?](hadoop.md#What-happens-if-number-of-Reducers-are-0)
+ [How many instances of Jobtracker can run on a Hadoop Cluster?](hadoop.md#How-many-instances-of-Jobtracker-can-run-on-a-Hadoop-Cluster)
+ [What is the Jobtracker and what it performs in a Hadoop Cluster?](hadoop.md#What-is-the-Jobtracker-and-what-it-performs-in-a-Hadoop-Cluster)
+ [How a task is scheduled by a Jobtracker?](hadoop.md#How-a-task-is-scheduled-by-a-Jobtracker)
+ [How many instances of Tasktracker run on a Hadoop Cluster?](hadoop.md#How-many-instances-of-Tasktracker-run-on-a-Hadoop-Cluster)
+ [How many maximum Jvm can run on a Slave Node?](hadoop.md#How-many-maximum-Jvm-can-run-on-a-Slave-Node)
+ [What is Nas?](hadoop.md#What-is-Nas)
+ [How Hdfs differs with Nfs?](hadoop.md#How-Hdfs-differs-with-Nfs)
+ [How does a NameNode handle the failure of the Data Nodes?](hadoop.md#How-does-a-NameNode-handle-the-failure-of-the-Data-Nodes)
+ [Can Reducer talk with each other?](hadoop.md#Can-Reducer-talk-with-each-other)
+ [Where the Mapper's intermediate data will be stored?](hadoop.md#Where-the-Mapper's-intermediate-data-will-be-stored)
+ [What is the Hadoop Mapreduce api contract for a Key and Value Class?](hadoop.md#What-is-the-Hadoop-Mapreduce-api-contract-for-a-Key-and-Value-Class)
+ [What is a IdentityMapper and IdentityReducer in Mapreduce?](hadoop.md#What-is-a-IdentityMapper-and-IdentityReducer-in-Mapreduce)
+ [What is the meaning of Speculative Execution in Hadoop?](hadoop.md#What-is-the-meaning-of-Speculative-Execution-in-Hadoop)
+ [How Hdfs is different from traditional File Systems?](hadoop.md#How-Hdfs-is-different-from-traditional-File-Systems)
+ [What is Hdfs block size and how is it different from Traditional File System block size?](hadoop.md#What-is-Hdfs-block-size-and-how-is-it-different-from-Traditional-File-System-block-size)
+ [What is a NameNode and how many instances of NameNode run on a Hadoop Cluster?](hadoop.md#What-is-a-NameNode-and-how-many-instances-of-NameNode-run-on-a-Hadoop-Cluster)
+ [How the client communicates with Hdfs?](hadoop.md#How-the-client-communicates-with-Hdfs)
+ [How the Hdfs blocks are replicated?](hadoop.md#How-the-Hdfs-blocks-are-replicated)
+ [Can you give some examples of Big Data?](hadoop.md#Can-you-give-some-examples-of-Big-Data)
+ [What is the basic difference between traditional Rdbms and Hadoop?](hadoop.md#What-is-the-basic-difference-between-traditional-Rdbms-and-Hadoop)
+ [What is structured and unstructured Data?](hadoop.md#What-is-structured-and-unstructured-Data)
+ [Since the data is replicated thrice in Hdfs so does it mean that any calculation done on One Node will also be replicated on the other Two?](hadoop.md#Since-the-data-is-replicated-thrice-in-Hdfs-so-does-it-mean-that-any-calculation-done-on-One-Node-will-also-be-replicated-on-the-other-Two)
+ [What is throughput and how does Hdfs get a good throughput?](hadoop.md#What-is-throughput-and-how-does-Hdfs-get-a-good-throughput)
+ [What is streaming access?](hadoop.md#What-is-streaming-access)
+ [What is a Commodity Hardware so does Commodity Hardware include Ram?](hadoop.md#What-is-a-Commodity-Hardware-so-does-Commodity-Hardware-include-Ram)
+ [Is NameNode also a Commodity?](hadoop.md#Is-NameNode-also-a-Commodity)
+ [What is a Metadata?](hadoop.md#What-is-a-Metadata?)
+ [What is a Daemon?](hadoop.md#What-is-a-Daemon)
+ [What is a Heartbeat in Hdfs?](hadoop.md#What-is-a-Heartbeat-in-Hdfs)
+ [How indexing is done in Hdfs?](hadoop.md#How-indexing-is-done-in-Hdfs)
+ [If a Data Node is full how it's identified?](hadoop.md#If-a-Data-Node-is-full-how-it's-identified)
+ [If DataNodes increase then do we need to upgrade NameNode?](hadoop.md#If-DataNodes-increase-then-do-we-need-to-upgrade-NameNode)
+ [Are Job Tracker and Task Trackers present in separate machines?](hadoop.md#Are-Job-Tracker-and-Task-Trackers-present-in-separate-machines)
+ [On what basis NameNode will decide which DataNode to write on?](hadoop.md#On-what-basis-NameNode-will-decide-which-DataNode-to-write-on)
+ [Who is a user in Hdfs?](hadoop.md#Who-is-a-user-in-Hdfs)
+ [Is client the end user in Hdfs?](hadoop.md#Is-client-the-end-user-in-Hdfs)
+ [What is the Communication Channel between client and NameNode/DataNode?](hadoop.md#What-is-the-Communication-Channel-between-client-and-NameNode/DataNode)
+ [What is a Rack?](hadoop.md#What-is-a-Rack)
+ [On what basis Data will be stored on a Rack?](hadoop.md#On-what-basis-Data-will-be-stored-on-a-Rack)
+ [Do we need to place 2nd and 3rd Data in Rack 2 only?](hadoop.md#Do-we-need-to-place-2nd-and-3rd-Data-in-Rack-2-only)
+ [What if Rack 2 and DataNode fails?](hadoop.md#What-if-Rack-2-and-DataNode-fails)
+ [What is the difference between Gen1 and Gen2 Hadoop with regards to the NameNode?](hadoop.md#What-is-the-difference-between-Gen1-and-Gen2-Hadoop-with-regards-to-the-NameNode)
+ [Do we require two servers for the NameNode and the DataNodes?](hadoop.md#Do-we-require-two-servers-for-the-NameNode-and-the-DataNodes)
+ [Why are the number of splits equal to the number of Maps?](hadoop.md#Why-are-the-number-of-splits-equal-to-the-number-of-Maps)
+ [Is a Job split into maps?](hadoop.md#Is-a-Job-split-into-maps)
+ [Which are the two types of writes in Hdfs?](hadoop.md#Which-are-the-two-types-of-writes-In-Hdfs)
+ [Why reading is done in parallel and writing is not in Hdfs?](hadoop.md#Why-reading-is-done-in-parallel-and-writing-is-not-in-Hdfs)
+ [Can Hadoop be compared to Nosql Database like Cassandra?](hadoop.md#Can-Hadoop-be-compared-to-Nosql-Database-like-Cassandra)
+ [How JobTracker schedules a task?](hadoop.md#How-JobTracker-schedules-a-task)
+ [What is a Task Tracker in Hadoop and how many instances of Task Tracker run on a Hadoop Cluster?](hadoop.md#What-is-a-Task-Tracker-in-Hadoop-and-how-many-instances-of-Task-Tracker-run-on-a-Hadoop-Cluster)
+ [What is a task instance in Hadoop and where does it run?](hadoop.md#What-is-a-task-instance-in-Hadoop-and-where-does-it-run)
+ [What is configuration of a typical Slave Node on Hadoop Cluster and how many Jvms run on a Slave Node?](hadoop.md#What-is-configuration-of-a-typical-Slave-Node-on-Hadoop-Cluster-and-how-many-Jvms-run-on-a-Slave-Node)
+ [How NameNode handles DataNode failures?](hadoop.md#How-NameNode-handles-DataNode-failures)
+ [Does Mapreduce programming model provide a way for Reducers to communicate with each other and in a Mapreduce Job can a Reducer communicate with another Reducer?](hadoop.md#Does-Mapreduce-programming-model-provide-a-way-for-Reducers-to-communicate-with-each-other-and-in-a-Mapreduce-Job-can-a-Reducer-communicate-with-another-Reducer)
+ [Can I set the number of Reducers to Zero?](hadoop.md#Can-I-set-the-number-of-Reducers-to-Zero)
+ [Where is the Mapper Output intermediate Kay-value data stored?](hadoop.md#Where-is-the-Mapper-Output-intermediate-Kay-value-data-stored)
+ [If Reducers do not start before all Mappers finish then why does the progress on Mapreduce Job shows something like Map 50 percents Reduce 10 percents and why Reducers progress percentage is displayed when Mapper is not Finished yet?](hadoop.md#If-Reducers-do-not-start-before-all-Mappers-finish-then-why-does-the-progress-on-Mapreduce-Job-shows-something-like-Map-50-percents-Reduce-10-percents-and-why-Reducers-progress-percentage-is-displayed-when-Mapper-is-not-Finished-yet)
+ [Explain in brief the three Modes in which Hadoop can be run?](hadoop.md#Explain-in-brief-the-three-Modes-in-which-Hadoop-can-be-run)
+ [Explain what are the features of Standalone local Mode?](hadoop.md#Explain-what-are-the-features-of-Standalone-local-Mode)
+ [What are the features of fully distributed mode?](hadoop.md#What-are-the-features-of-fully-distributed-mode)
+ [Explain what are the main features Of pseudo mode?](hadoop.md#Explain-what-are-the-main-features-Of-pseudo-mode)
+ [What are the port numbers of NameNode and JobTracker and TaskTracker?](hadoop.md#What-are-the-port-numbers-of-NameNode-and-JobTracker-and-TaskTracker)
+ [Tell us what is a spill factor with respect to the ram?](hadoop.md#Tell-us-what-is-a-spill-factor-with-respect-to-the-ram)
+ [Is fs.mapr working for a single directory?](hadoop.md#Is-fs.mapr-working-for-a-single-directory)
+ [Which are the three main Hdfs-site.xml properties?](hadoop.md#Which-are-the-three-main-Hdfs-site.xml-properties)
+ [How can I restart NameNode?](hadoop.md#How-can-I-restart-Namenode)
+ [How can we check whether Namenode is working or not?](hadoop.md#How-can-we-check-whether-Namenode-is-working-or-not)
+ [At times you get a connection refused Java Exception when you run the file system check command Hadoop fsck?](hadoop.md#At-times-you-get-a-connection-refused-Java-Exception-when-you-run-the-file-system-check-command-Hadoop-fsck)
+ [What is the use of the command Mapred.job.tracker?](hadoop.md#What-is-the-use-of-the-command-Mapred.job.tracker)
+ [What does etc/init.d do?](hadoop.md#What-does-etc.init.d-do)
+ [How can we look for the Namenode in the browser?](hadoop.md#How-can-we-look-for-the-Namenode-in-the-browser)
+ [What do masters and slaves consist of?](hadoop.md#What-do-masters-and-slaves-consist-of)
+ [What is the function Of Hadoop-env.sh and where is it present?](hadoop.md#What-is-the-function-Of-Hadoop-env.sh-and-where-is-it-present)
+ [Can we have multiple entries in the master files?](hadoop.md#Can-we-have-multiple-entries-in-the-master-files)
+ [In Hadoop_pid_dir and what does pid stands for?](hadoop.md#In-Hadoop_pid_dir-and-what-does-pid-stands-for)
+ [What does Hadoop-metrics and properties file do?](hadoop.md#What-does-Hadoop-metrics-and-properties-file-do)
+ [What are the network requirements for hadoop?](hadoop.md#What-are-the-network-requirements-for-hadoop)
+ [Why do we need a password-less ssh in fully distributed environment?](hadoop.md#Why-do-we-need-a-passwordless-ssh-in-fully-distributed-environment)
+ [What will happen if a NameNode has no data?](hadoop.md#What-will-happen-if-a-NameNode-has-no-data)
+ [What happens to job tracker when NameNode is down?](hadoop.md#What-happens-to-job-tracker-when-NameNode-is-down)
+ [Explain what do you mean by formatting of the Dfs?](hadoop.md#Explain-what-do-you-mean-by-formatting-of-the-Dfs)
+ [We use Unix variants for hadoop and can we use Microsoft Windows for the same?](hadoop.md#We-use-Unix-variants-for-hadoop-and-can-we-use-Microsoft-Windows-for-the-same)
+ [Which one decides the input split hdfs client or NameNode?](hadoop.md#Which-one-decides-the-input-split-hdfs-client-or-NameNode)
+ [Can you tell me if we can create a hadoop cluster from scratch?](hadoop.md#Can-you-tell-me-if-we-can-create-a-hadoop-cluster-from-scratch)
+ [Explain the significance of ssh and what is the port on which port does ssh work and why do we need password in ssh local host?](hadoop.md#Explain-the-significance-of-ssh-and-what-is-the-port-on-which-port-does-ssh-work-and-why-do-we-need-password-in-ssh-local-host)
+ [What is ssh and explain in detail about ssh communication between masters and the slaves?](hadoop.md#What-is-ssh-and-explain-in-detail-about-ssh-communication-between-masters-and-the-slaves)
+ [Can You Tell Is What Will Happen To A NameNode and When Job Tracker Is Not Up And Running?](hadoop.md#Can-you-tell-is-what-will-happen-to-a-NameNode-and-when-Job-tracker-is-not-up-and-running)

[Table of Contents](#Interview questions for Data Engineer)

## Apache Flume
+ [What is Flume?](flume.md#What-is-Flume)
+ [What is Apache Flume?](flume.md#What-is-Apache-Flume)
+ [Which is the reliable channel in Flume to ensure that there is no Data Loss?](flume.md#Which-is-the-reliable-channel-in-Flume-to-ensure-that-there-is-no-Data-Loss)
+ [How can Flume be used with Hbase?](flume.md#How-can-Flume-be-used-with-Hbase)
+ [What is an Agent?](flume.md#What-is-an-Agent)
+ [Is it possible to Leverage Real Time Analysis on the Big Data collected by Flume directly?](flume.md#Is-it-possible-to-Leverage-Real-Time-Analysis-on-the-Big-Data-collected-by-Flume-directly)
+ [What is a Channel?](flume.md#What-is-a-Channel)
+ [Explain about the different channel types in Flume and which channel type is faster?](flume.md#Explain-about-the-different-channel-types-in-Flume-and-which-channel-type-is-faster)
+ [Explain about the replication and multiplexing selectors in Flume?](flume.md#Explain-about-the-replication-and-multiplexing-selectors-in-Flume)
+ [Does Apache Flume provide support for third party Plugins?](flume.md#Does-Apache-Flume-provide-support-for-third-party-Plugins)
+ [Differentiate between FileSink and FileRollSink?](flume.md#Differentiate-between-FileSink-and-FileRollSink)
+ [Why we are using Flume?](flume.md#Why-we-are-using-Flume)
+ [What is Flumeng?](flume.md#What-is-Flumeng)
+ [What are the complicated steps in Flume configurations?](flume.md#What-are-the-complicated-steps-in-Flume-configurations)
+ [What are Flume core components?](flume.md#What-are-Flume-core-components)
+ [What are the Data Extraction Tools in Hadoop?](flume.md#What-are-the-Data-Extraction-Tools-in-Hadoop)
+ [Does Flume provide 100% reliability to the Data Flow?](flume.md#Does-Flume-provide-100-percents-reliability-to-the-Data-Flow)
+ [Tell any two Features of Flume?](flume.md#Tell-any-two-Features-of-Flume)
+ [What are Interceptors?](flume.md#What-are-Interceptors)
+ [Why Flume?](flume.md#Why-Flume)
+ [What is Flume Event?](flume.md#What-is-Flume-Event)
+ [How Multi hop agent can be setup in Flume?](flume.md#How-Multi-hop-agent-can-be-setup-in-Flume)
+ [Can Flume can distribute data to multiple destinations?](flume.md#Can-Flume-can-distribute-data-to-multiple-destinations)
+ [Can you explain about configuration files?](flume.md#Can-you-explain-about-configuration-files)
+ [What are the similarities and differences between Apache Flume and Apache Kafka?](flume.md#What-are-the-similarities-and-differences-between-Apache-Flume-and-Apache-Kafka)
+ [Explain Reliability and Failure Handling in Apache Flume?](flume.md#Explain-Reliability-and-Failure-Handling-in-Apache-Flume)

[Table of Contents](#Interview questions for Data Engineer)

## Apache NiFi
+ [What is Apache Nifi?](nifi.md#What-is-Apache-Nifi)
+ [What is Nifi FlowFile?](nifi.md#What-is-Nifi-FlowFile)
+ [What is Relationship in Nifi DataFlow?](nifi.md#What-is-Relationship-in-Nifi-DataFlow)
+ [What is Reporting Task?](nifi.md#What-is-Reporting-Task)
+ [What is a Nifi Processor?](nifi.md#What-is-a-Nifi-Processor)
+ [Is there a programming language that Apache Nifi supports?](nifi.md#Is-there-a-programming-language-that-Apache-Nifi-supports)
+ [How do you define Nifi content Repository?](nifi.md#How-do-you-define-Nifi-content-Repository)
+ [What is the Backpressure in Nifi system?](nifi.md#What-is-the-Backpressure-in-Nifi-system)
+ [What is the template in Nifi?](nifi.md#What-is-the-template-in-Nifi)
+ [What is the bulleting and how it helps in Nifi?](nifi.md#What-is-the-bulleting-and-how-it-helps-in-Nifi)
+ [Do the attributes get added to content (actual Data) when data is pulled by Nifi?](nifi.md#Do-the-attributes-get-added-to-content-when-data-is-pulled-by-Nifi)
+ [What happens if you have stored a password in a dataflow and create a template out of it?](nifi.md#What-happens-if-you-have-stored-a-password-in-a-dataflow-and-create-a-template-out-of-it)
+ [How does Nifi support huge volume of Payload in a Dataflow?](nifi.md#How-does-Nifi-support-huge-volume-of-Payload-in-a-Dataflow)
+ [What is a Nifi custom properties registry?](nifi.md#What-is-a-Nifi-custom-properties-registry)
+ [Does Nifi works as a Master Slave architecture?](nifi.md#Does-Nifi-works-as-a-Master-Slave-architecture)

[Table of Contents](#Interview questions for Data Engineer)

## Apache Avro
+ [What is Apache Avro?](avro.md#What-is-Apache-Avro)
+ [State some Key Points about Apache Avro?](avro.md#State-some-Key-Points-about-Apache-Avro)
+ [What Avro Offers?](avro.md#What-Avro-Offers)
+ [Who is intended audience to Learn Avro?](avro.md#Who-is-intended-audience-to-Learn-Avro)
+ [What are prerequisites to learn Avro?](avro.md#What-are-prerequisites-to-learn-Avro)
+ [Explain Avro schemas?](avro.md#Explain-Avro-schemas)
+ [Explain Thrift and Protocol Buffers and Avro?](avro.md#Explain-Thrift-and-Protocol-Buffers-and-Avro)
+ [Why Avro?](avro.md#Why-Avro)
+ [How to use Avro?](avro.md#How-to-use-Avro)
+ [Name some primitive types of Data Types which Avro Supports.](avro.md#Name-some-primitive-types-of-Data-Types-which-Avro-Supports)
+ [Name some complex types of Data Types which Avro Supports.](avro.md#Name-some-complex-types-of-Data-Types-which-Avro-Supports)
+ [What are best features of Apache Avro?](avro.md#What-are-best-features-of-Apache-Avro)
+ [Explain some advantages of Avro.](avro.md#Explain-some-advantages-of-Avro)
+ [Explain some disadvantages of Avro.](avro.md#Explain-some-disadvantages-of-Avro)
+ [What do you mean by schema declaration?](avro.md#What-do-you-mean-by-schema-declaration)
+ [Explain the term Serialization?](avro.md#Explain-the-term-Serialization)
+ [What do you mean by Schema Resolution?](avro.md#What-do-you-mean-by-Schema-Resolution)
+ [Explain the Avro Sasl profile?](avro.md#Explain-the-Avro-Sasl-profile)
+ [What is the way of creating Avro Schemas?](avro.md#What-is-the-way-of-creating-Avro-Schemas)
+ [Name some Avro Reference Apis?](avro.md#Name-some-Avro-Reference-Apis)
+ [When to use Avro?](avro.md#When-to-use-Avro)
+ [Explain sort order in brief?](avro.md#Explain-sort-order-in-brief)
+ [What is the advantage of Hadoop Over Java Serialization?](avro.md#What-is-the-advantage-of-Hadoop-Over-Java-Serialization)
+ [What are the disadvantages of Hadoop Serialization?](avro.md#What-are-the-disadvantages-of-Hadoop-Serialization)

[Table of Contents](#Interview questions for Data Engineer)

## Apache Kafka
+ [Mention what is Apache Kafka?](kafka.md#Mention-what-is-Apache-Kafka)
+ [Mention what is the traditional method of message transfer?](kafka.md#Mention-what-is-the-traditional-method-of-message-transfer)
+ [Mention what is the benefits of Apache Kafka over the traditional technique?](kafka.md#Mention-what-is-the-benefits-of-Apache-Kafka-over-the-traditional-technique)
+ [Mention what is the meaning of Broker in Kafka?](kafka.md#Mention-what-is-the-meaning-of-Broker-in-Kafka)
+ [Mention what is the Maximum Size of the Message does Kafka server can Receive?](kafka.md#Mention-what-is-the-Maximum-Size-of-the-Message-does-Kafka-server-can-Receive)
+ [Explain what is Zookeeper in Kafka and can we use Kafka without Zookeeper?](kafka.md#Explain-what-is-Zookeeper-in-Kafka-and-can-we-use-Kafka-without-Zookeeper)
+ [Explain how message is consumed by Consumer in Kafka?](kafka.md#Explain-how-message-is-consumed-by-Consumer-in-Kafka)
+ [Explain how you can improve the throughput of a remote consumer?](kafka.md#Explain-how-you-can-improve-the-throughput-of-a-remote-consumer)
+ [Explain how you can get Exactly Once Messaging from Kafka during data production?](kafka.md#Explain-how-you-can-get-Exactly-Once-Messaging-from-Kafka-during-data-production)
+ [Explain how you can reduce churn in Isr and when does Broker leave the Isr?](kafka.md#Explain-how-you-can-reduce-churn-in-Isr-and-when-does-Broker-leave-the-Isr)
+ [Why Replication is required in Kafka?](kafka.md#Why-Replication-is-required-in-Kafka)
+ [What does it indicate if replica stays out of Isr for a long time?](kafka.md#What-does-it-indicate-if-replica-stays-out-of-Isr-for-a-long-time)
+ [Mention what happens if the preferred replica is not in the Isr?](kafka.md#Mention-what-happens-if-the-preferred-replica-is-not-in-the-Isr)
+ [Is it possible to get the Message Offset after Producing?](kafka.md#Is-it-possible-to-get-the-Message-Offset-after-Producing)
+ [Mention what is the difference between Apache Kafka and Apache Storm?](kafka.md#Mention-what-is-the-difference-between-Apache-Kafka-and-Apache-Storm)
+ [List the various components in Kafka?](kafka.md#List-the-various-components-in-Kafka)
+ [Explain the role of the Offset?](kafka.md#Explain-the-role-of-the-Offset)
+ [Explain the concept of Leader and Follower?](kafka.md#Explain the concept of Leader and Follower?)
+ [How do you define a Partitioning Key?](kafka.md#How-do-you-define-a-Partitioning-Key)
+ [In the Producer when does Queuefullexception occur?](kafka.md#In-the-Producer-when-does-Queuefullexception-occur)
+ [Explain the role of the Kafka Producer Api.](kafka.md#Explain-the-role-of-the-Kafka-Producer-Api)

[Table of Contents](#Interview questions for Data Engineer)

## Apache Impala
+ [How do I try Impala out?](impala.md#How-do-I-try-Impala-out)
+ [Does Cloudera offer a Vm for demonstrating Impala?](impala.md#Does-Cloudera-offer-a-Vm-for-demonstrating-Impala)
+ [How much Memory is required?](impala.md#How-much-Memory-is-required)
+ [What are the main features of Impala?](impala.md#What-are-the-main-features-of-Impala)
+ [What features from relational databases or hive are not available in Impala?](impala.md#What-features-from-relational-databases-or-hive-are-not-available-in-Impala)
+ [Does Impala support Generic Jdbc?](impala.md#Does-Impala-support-Generic-Jdbc)
+ [Is Avro supported?](impala.md#Is-Avro-supported)
+ [How do I Know how many Impala Nodes are in my cluster?](impala.md#How-do-I-Know-how-many-Impala-Nodes-are-in-my-cluster)
+ [Are results returned as they become available or all at once when a query completes?](impala.md#Are-results-returned-as-they-become-available-or-all-at-once-when-a-query-completes)
+ [Why does my select statement fail?](impala.md#Why-does-my-select-statement-fail)
+ [Why does my insert statement fail?](impala.md#Why-does-my-insert-statement-fail)
+ [Does Impala performance improve as it is deployed to more hosts in a cluster in much the same way that Hadoop performance does?](impala.md#Does-Impala-performance-improve-as-it-is-deployed-to-more-hosts-in-a-cluster-in-much-the-same-way-that-Hadoop-performance-does)
+ [Is the Hdfs Block Size reduced to achieve faster query results?](impala.md#Is-the-Hdfs-Block-Size-reduced-to-achieve-faster-query-results)
+ [Does Impala use caching?](impala.md#Does-Impala-use-caching)
+ [What are the good use cases for Impala as opposed to Hive or Mapreduce?](impala.md#What-are-the-good-use-cases-for-Impala-as-opposed-to-Hive-or-Mapreduce)
+ [Is Mapreduce required for impala and will Impala continue to work as expected if Mapreduce is stopped?](impala.md#Is-Mapreduce-required-for-impala-and-will-Impala-continue-to-work-as-expected-if-Mapreduce-is-stopped)
+ [Can Impala be used for complex event processing?](impala.md#Can-Impala-be-used-for-complex-event-processing)
+ [Is Impala intended to handle Real Time Queries in Low latency Applications or is it for ad-Hoc Queries for the purpose of data exploration?](impala.md#Is-Impala-intended-to-handle-Real-Time-Queries-in-Low-latency-Applications-or-is-it-for-ad-Hoc-Queries-for-the-purpose-of-data-exploration)
+ [How does Impala compare to Hive and Pig?](impala.md#How-does-Impala-compare-to-Hive-and-Pig)
+ [Can I do transforms or add New functionality?](impala.md#Can-I-do-transforms-or-add-New-functionality)
+ [Can any Impala Query also be executed in Hive?](impala.md#Can-any-Impala-Query-also-be-executed-in-Hive)
+ [Can I use Impala to Query data already loaded into Hive and Hbase?](impala.md#Can-I-use-Impala-to-Query-data-already-loaded-into-Hive-and-Hbase)
+ [Is Hive an Impala requirement?](impala.md#Is-Hive-an-Impala-requirement)
+ [Is Impala production ready?](impala.md#Is-Impala-production-ready)
+ [How do I configure Hadoop High Availability for Impala?](impala.md#How-do-I-configure-Hadoop-High-Availability-for-Impala)
+ [What happens if there is an Error in Impala?](impala.md#What-happens-if-there-is-an-Error-in-Impala)
+ [What is the Maximum number of Rows in a Table?](impala.md#What-is-the-Maximum-number-of-Rows-in-a-Table)
+ [On which hosts does Impala run?](impala.md#On-which-hosts-does-Impala-run)
+ [How are Joins performed in Impala?](impala.md#How-are-Joins-performed-in-Impala)
+ [How does Impala process Join Queries for large tables?](impala.md#How-does-Impala-process-Join-Queries-for-large-tables)
+ [What is Impala's aggregation strategy?](impala.md#What-is-Impala's-aggregation-strategy)
+ [How is Impala Metadata managed?](impala.md#How-is-Impala-Metadata-managed)
+ [What load do concurrent queries produce on the Name Node?](impala.md#What-load-do-concurrent-queries-produce-on-the-Name-Node)
+ [How does Impala achieve its performance improvements?](impala.md#How-does-Impala-achieve-its-performance-improvements)
+ [What happens when the data set exceeds available memory?](impala.md#What-happens-when-the-data-set-exceeds-available-memory)
+ [What are the most Memory intensive operations?](impala.md#What-are-the-most-Memory-intensive-operations)
+ [When does Impala hold on to or return memory?](impala.md#When-does-Impala-hold-on-to-or-return-memory)
+ [Is there an update statement?](impala.md#Is-there-an-update-statement)
+ [Can Impala do User defined functions?](impala.md#Can-Impala-do-User-defined-functions)
+ [Why do I have to use refresh and invalidate Metadata and what do they do?](impala.md#Why-do-I-have-to-use-refresh-and-invalidate-Metadata-and-what-do-they-do)
+ [Why is space not freed up when I issue drop table?](impala.md#Why-is-space-not-freed-up-when-I-issue-drop-table)
+ [Is there a dual table?](impala.md#Is-there-a-dual-table)
+ [How do I load a big Csv file into a partitioned table?](impala.md#How-do-I-load-a-big-Csv-file-into-a-partitioned-table)
+ [Can I Do Insert ... Select * Into a partitioned table?](impala.md#Can-I-Do-Insert-Select-Into-a-partitioned-table)
+ [What kinds of Impala Queries or data are best suited for Hbase?](impala.md#What-kinds-of-Impala-Queries-or-data-are-best-suited-for-Hbase)

[Table of Contents](#Interview questions for Data Engineer)

