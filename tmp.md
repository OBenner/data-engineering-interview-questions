+ [В чём заключается разница между IO и NIO?](#В-чём-заключается-разница-между-io-и-nio)

## What is the core concept behind Apache Hadoop framework?
    Apache Hadoop is based on the concept of MapReduce algorithm. In MapReduce algorithm, Map and Reduce operations are used to process very large data set.
    In this concept, Map method does the filtering and sorting of data. Reduce method performs the summarizing of data.
    This is a concept from functional programming.
    The key points in this concept are scalability and fault tolerance. In Apache Hadoop these features are achieved by multi-threading and efficient implementation of MapReduce.

[Table of Contents](#HADOOP)

## What is Hadoop Streaming?
    Hadoop distribution provides a Java utility called Hadoop Streaming. It is packaged in a jar file. With Hadoop Streaming, we can create and run Map Reduce jobs with an executable script.
    We can create executable scripts for Mapper and Reducer functions. These executable scripts are passed to Hadoop Streaming in a command.
    Hadoop Streaming utility creates Map and Reduce jobs and submits these to a cluster. We can also monitor these jobs with this utility.

[Table of Contents](#HADOOP)

## What is the difference between Nodes in HDFS?
    The differences between NameNode, BackupNode and Checkpoint NameNode are as follows:
        NameNode: NameNode is at the heart of the HDFS file system that manages the metadata i.e. the data of the files is not stored on the NameNode but rather it has the directory tree of all the files present in the HDFS file system on a Hadoop cluster. NameNode uses two files for the namespace:
            fsimage file: This file keeps track of the latest checkpoint of the namespace.
            edits file: This is a log of changes made to the namespace since checkpoint.
        Checkpoint Node:	Checkpoint Node keeps track of the latest checkpoint in a directory that has same structure as that of NameNode’s directory.
            Checkpoint node creates checkpoints for the namespace at regular intervals by downloading the edits and fsimage file from the NameNode and merging it locally. The new image is then again updated back to the active NameNode.
        BackupNode: This node also provides check pointing functionality like that of the Checkpoint node but it also maintains its up-to-date in-memory copy of the file system namespace that is in sync with the active NameNode.

[Table of Contents](#HADOOP)

## What is the optimum hardware configuration to run Apache Hadoop?
    To run Apache Hadoop jobs, it is recommended to use dual core machines or dual processors. There should be 4GB or 8GB RAM with the processor with Error-correcting code (ECC) memory.
    Without ECC memory, there is high chance of getting checksum errors.
    For storage high capacity SATA drives (around 7200 rpm) should be used in Hadoop cluster.
    Around 10GB bandwidth Ethernet networks are good for Hadoop.

[Table of Contents](#HADOOP)

## What do you know about Block and Block scanner in HDFS?
    A large file in HDFS is broken into multiple parts and each part is stored on a different Block. By default a Block is of 64 MB capacity in HDFS.
    Block Scanner is a program that every Data node in HDFS runs periodically to verify the checksum of every block stored on the data node.
    The purpose of a Block Scanner is to detect any data corruption errors on Data node.

[Table of Contents](#HADOOP)

## What are the default port numbers on which  Nodes run in Hadoop?
    Default port numbers of Name Node, Job Tracker and Task Tracker are as follows:
    NameNode runs on port 50070
    Task Tracker runs on port 50060
    Job Tracker runs on port 50030

[Table of Contents](#HADOOP)

## How will you disable a Block Scanner on HDFS DataNode?
    In HDFS, there is a configuration dfs.datanode.scan.period.hours in hdfs- site.xml to set the number of hours interval at which Block Scanner should run.
    We can set dfs.datanode.scan.period.hours=0 to disable the Block Scanner. It means it will not run on HDFS DataNode.

[Table of Contents](#HADOOP)

## How will you get the distance between two nodes in Apache Hadoop?
    In Apache Hadoop we can use NetworkTopology.getDistance() method to get the distance between two nodes.
    Distance from a node to its parent is considered as 1.

[Table of Contents](#HADOOP)

## Why do we use commodity hardware in Hadoop?
    Hadoop does not require a very high-end server with large memory and processing power. Due to this we can use any inexpensive system with average RAM and processor. Such kind of system is called commodity hardware.
    Since there is parallel processing in Hadoop MapReduce, it is convenient to distribute a task among multiple servers and then do the execution. It saves cost as well as it is much faster compared to other options. Another benefit of using commodity hardware in Hadoop is scalability. Commodity hardware is readily available in market. Whenever we need to scale up our operations in Hadoop cluster we can obtain more commodity hardware. In case of high-end machines, we have to raise purchase orders and get them built on demand.

[Table of Contents](#HADOOP)

## How does inter cluster data copying works in Hadoop?
    In Hadoop, there is a utility called DistCP (Distributed Copy) to perform large inter/intra-cluster copying of data. This utility is also based on MapReduce. It creates Map tasks for files given as input.
    After every copy using DistCP, it is recommended to run crosschecks to confirm that there is no data corruption and copy is complete.

[Table of Contents](#HADOOP)

## How can we update a file at an arbitrary location in HDFS?
    This is a trick question. In HDFS, it is not allowed to update a file at an arbitrary location. All the files are written in append only mode. It means all writes are done at the end of a file.
    So there is no possibility of updating the files at any random location.

[Table of Contents](#HADOOP)

## What is Replication factor in HDFS?
    Replication factor in HDFS is the number of copies of a file in file system. A Hadoop application can specify the number of replicas of a file it wants HDFS to maintain. This information is stored in NameNode. We can set the replication factor in following ways:
    We can use Hadoop fs shell, to specify the replication factor for a file. Command as follows:
        $hadoop fs –setrep –w 5 /file_name
    In above command, replication factor of file_name  file is set as 5.
    We can also use Hadoop fs shell, to specify the replication factor of all the files in a directory.
        $hadoop fs –setrep –w 2 /dir_name
    In above command, replication factor of all the files under directory dir_name is set as 2.

## В чём заключается разница между IO и NIO?
+ Java IO (input-output) является потокоориентированным, а Java NIO (new/non-blocking io) – буфер-ориентированным. Потокоориентированный ввод/вывод подразумевает чтение/запись из потока/в поток одного или нескольких байт в единицу времени поочередно. Данная информация нигде не кэшируются. Таким образом, невозможно произвольно двигаться по потоку данных вперед или назад. В Java NIO данные сначала считываются в буфер, что дает больше гибкости при обработке данных.
+ Потоки ввода/вывода в Java IO являются блокирующими. Это значит, что когда в потоке выполнения вызывается `read()` или `write()` метод любого класса из пакета `java.io.*`, происходит блокировка до тех пор, пока данные не будут считаны или записаны. Поток выполнения в данный момент не может делать ничего другого. Неблокирующий режим Java NIO позволяет запрашивать считанные данные из канала (channel) и получать только то, что доступно на данный момент, или вообще ничего, если доступных данных пока нет. Вместо того, чтобы оставаться заблокированным пока данные не станут доступными для считывания, поток выполнения может заняться чем-то другим. Тоже самое справедливо и для неблокирующего вывода. Поток выполнения может запросить запись в канал некоторых данных, но не дожидаться при этом пока они не будут полностью записаны.
+ В Java NIO имеются селекторы, которые позволяют одному потоку выполнения мониторить несколько каналов ввода. Т.е. существует возможность зарегистрировать несколько каналов с селектором, а потом использовать один поток выполнения для обслуживания каналов, имеющих доступные для обработки данные, или для выбора каналов, готовых для записи.
