1. What is EC2?
   EC2, a Virtual Machine in the cloud on which you have OS-level control. You can run this cloud server whenever you want and can be used when you need to deploy your own servers in the cloud, similar to your on-premises servers, and when you want to have full control over the choice of hardware and the updates on the machine.

2. What is SnowBall?
   SnowBall is a small application that enables you to transfer terabytes of data inside and outside of the AWS environment.


AWS Snowball
3. What is CloudWatch?
   CloudWatch helps you to monitor AWS environments like EC2, RDS Instances, and CPU utilization. It also triggers alarms depending on various metrics.


AWS Cloudwatch
You can download a PDF version of Aws Interview Questions.

Download PDF

4. What is Elastic Transcoder?
   Elastic Transcoder is an AWS Service Tool that helps you in changing a video’s format and resolution to support various devices like tablets, smartphones, and laptops of different resolutions.

5. What do you understand by VPC?
   VPC stands for Virtual Private Cloud. It allows you to customize your networking configuration. VPC is a network that is logically isolated from other networks in the cloud. It allows you to have your private IP Address range, internet gateways, subnets, and security groups.

6. DNS and Load Balancer Services come under which type of Cloud Service?
   DNS and Load Balancer are a part of IaaS-Storage Cloud Service.

7. What are the Storage Classes available in Amazon S3?
   Storage Classes available with Amazon S3 are:

Amazon S3 Standard
Amazon S3 Standard-Infrequent Access
Amazon S3 Reduced Redundancy Storage
Amazon Glacier
8. Explain what T2 instances are?
   T2 Instances are designed to provide moderate baseline performance and the capability to burst to higher performance as required by the workload.

9. What are Key-Pairs in AWS?
   Key-Pairs are secure login information for your Virtual Machines. To connect to the instances, you can use Key-Pairs which contain a Public Key and a Private Key.

10. How many Subnets can you have per VPC?
    You can have 200 Subnets per VPC.

11. List different types of Cloud Services.
    Different types of Cloud Services are:

Software as a Service (SaaS)
Data as a Service (DaaS)
Platform as a Service (PaaS)
Infrastructure as a Service (IaaS)
Advanced AWS Questions
12. Explain what S3 is?
    S3 stands for Simple Storage Service. You can use the S3 interface to store and retrieve any amount of data, at any time and from anywhere on the web. For S3, the payment model is “pay as you go”.

13. How does Amazon Route 53 provide high availability and low latency?
    Amazon Route 53 uses the following to provide high availability and low latency:

Globally Distributed Servers - Amazon is a global service and consequently has DNS Servers globally. Any customer creating a query from any part of the world gets to reach a DNS Server local to them that provides low latency.
Dependency - Route 53 provides a high level of dependability required by critical applications.
Optimal Locations - Route 53 serves the requests from the nearest data center to the client sending the request. AWS has data-centers across the world. The data can be cached on different data-centers located in different regions of the world depending on the requirements and the configuration chosen. Route 53 enables any server in any data-center which has the required data to respond. This way, it enables the nearest server to serve the client request, thus reducing the time taken to serve.

Amazon Route
As can be seen in the above image, the requests coming from a user in India are served from the Singapore Server, while the requests coming from a user in the US are routed to Oregon region.

14. How can you send a request to Amazon S3?
    Amazon S3 is a REST Service, and you can send a request by using the REST API or the AWS SDK wrapper libraries that wrap the underlying Amazon S3 REST API.

15. What does AMI include?
    An AMI includes the following things:

A template for the root volume for the instance.
Launch permissions to decide which AWS accounts can avail the AMI to launch instances.
A block device mapping that determines the volumes to attach to the instance when it is launched.
16. What are the different types of Instances?
    Following are the types of instances:

Compute Optimized
Memory-Optimized
Storage Optimized
Accelerated Computing
General Purpose
17. What is the relation between the Availability Zone and Region?
    An AWS Availability Zone is a physical location where an Amazon data center is located. On the other hand, an AWS Region is a collection or group of Availability Zones or Data Centers.

This setup helps your services to be more available as you can place your VMs in different data centers within an AWS Region. If one of the data centers fails in a Region, the client requests still get served from the other data centers located in the same Region. This arrangement, thus, helps your service to be available even if a Data Center goes down.

18. How do you monitor Amazon VPC?
    You can monitor Amazon VPC using:

CloudWatch
VPC Flow Logs
19. What are the different types of EC2 instances based on their costs?
    The three types of EC2 instances based on the costs are:

On-Demand Instance - These instances are prepared as and when needed. Whenever you feel the need for a new EC2 instance, you can go ahead and create an on-demand instance. It is cheap for the short-time but not when taken for the long term.

Spot Instance - These types of instances can be bought through the bidding model. These are comparatively cheaper than On-Demand Instances.

Reserved Instance - On AWS, you can create instances that you can reserve for a year or so. These types of instances are especially useful when you know in advance that you will be needing an instance for the long term. In such cases, you can create a reserved instance and save heavily on costs.

20. What do you understand by stopping and terminating an EC2 Instance?
    Stopping an EC2 instance means to shut it down as you would normally do on your Personal Computer. This will not delete any volumes attached to the instance and the instance can be started again when needed.

On the other hand, terminating an instance is equivalent to deleting an instance. All the volumes attached to the instance get deleted and it is not possible to restart the instance if needed at a later point in time.

21. What are the consistency models for modern DBs offered by AWS?
    Eventual Consistency - It means that the data will be consistent eventually, but may not be immediate. This will serve the client requests faster, but chances are that some of the initial read requests may read the stale data. This type of consistency is preferred in systems where data need not be real-time. For example, if you don’t see the recent tweets on Twitter or recent posts on Facebook for a couple of seconds, it is acceptable.

Strong Consistency - It provides an immediate consistency where the data will be consistent across all the DB Servers immediately. Accordingly. This model may take some time to make the data consistent and subsequently start serving the requests again. However, in this model, it is guaranteed that all the responses will always have consistent data.

22. What is Geo-Targeting in CloudFront?
    Geo-Targeting enables the creation of customized content based on the geographic location of the user. This allows you to serve the content which is more relevant to a user. For example, using Geo-Targeting, you can show the news related to local body elections to a user sitting in India, which you may not want to show to a user sitting in the US. Similarly, the news related to Baseball Tournament can be more relevant to a user sitting in the US, and not so relevant for a user sitting in India.

23. What are the advantages of AWS IAM?
    AWS IAM enables an administrator to provide granular level access to different users and groups. Different users and user groups may need different levels of access to different resources created. With IAM, you can create roles with specific access-levels and assign the roles to the users.

It also allows you to provide access to the resources to users and applications without creating the IAM Roles, which is known as Federated Access.

24. What do you understand by a Security Group?
    When you create an instance in AWS, you may or may not want that instance to be accessible from the public network. Moreover, you may want that instance to be accessible from some networks and not from others.

Security Groups are a type of rule-based Virtual Firewall using which you can control access to your instances. You can create rules defining the Port Numbers, Networks, or protocols from which you want to allow access or deny access.

25. What are Spot Instances and On-Demand Instances?
    When AWS creates EC2 instances, there are some blocks of computing capacity and processing power left unused. AWS releases these blocks as Spot Instances. Spot Instances run whenever capacity is available. These are a good option if you are flexible about when your applications can run and if your applications can be interrupted.

On the other hand, On-Demand Instances can be created as and when needed. The prices of such instances are static. Such instances will always be available unless you explicitly terminate them.

26. Explain Connection Draining.
    Connection Draining is a feature provided by AWS which enables your servers which are either going to be updated or removed, to serve the current requests.

If Connection Draining is enabled, the Load Balancer will allow an outgoing instance to complete the current requests for a specific period but will not send any new request to it. Without Connection Draining, an outgoing instance will immediately go off and the requests pending on that instance will error out.

27. What is a Stateful and a Stateless Firewall?
    A Stateful Firewall is the one that maintains the state of the rules defined. It requires you to define only inbound rules. Based on the inbound rules defined, it automatically allows the outbound traffic to flow.

On the other hand, a Stateless Firewall requires you to explicitly define rules for inbound as well as outbound traffic.

For example, if you allow inbound traffic from Port 80, a Stateful Firewall will allow outbound traffic to Port 80, but a Stateless Firewall will not do so.

28. What is a Power User Access in AWS?
    An Administrator User will be similar to the owner of the AWS Resources. He can create, delete, modify or view the resources and also grant permissions to other users for the AWS Resources.

A Power User Access provides Administrator Access without the capability to manage the users and permissions. In other words, a user with Power User Access can create, delete, modify or see the resources, but he cannot grant permissions to other users.

29. What is an Instance Store Volume and an EBS Volume?
    An Instance Store Volume is temporary storage that is used to store the temporary data required by an instance to function. The data is available as long as the instance is running. As soon as the instance is turned off, the Instance Store Volume gets removed and the data gets deleted.

On the other hand, an EBS Volume represents a persistent storage disk. The data stored in an EBS Volume will be available even after the instance is turned off.

30. What are Recovery Time Objective and Recovery Point Objective in AWS?
    Recovery Time Objective - It is the maximum acceptable delay between the interruption of service and restoration of service. This translates to an acceptable time window when the service can be unavailable.

Recover Point Objective - It is the maximum acceptable amount of time since the last data restore point. It translates to the acceptable amount of data loss which lies between the last recovery point and the interruption of service.

31. Is there a way to upload a file that is greater than 100 Megabytes in Amazon S3?
    Yes, it is possible by using the Multipart Upload Utility from AWS. With the Multipart Upload Utility, larger files can be uploaded in multiple parts that are uploaded independently. You can also decrease upload time by uploading these parts in parallel. After the upload is done, the parts are merged into a single object or file to create the original file from which the parts were created.

32. Can you change the Private IP Address of an EC2 instance while it is running or in a stopped state?
    No, a Private IP Address of an EC2 instance cannot be changed. When an EC2 instance is launched, a private IP Address is assigned to that instance at the boot time. This private IP Address is attached to the instance for its entire lifetime and can never be changed.

33. What is the use of lifecycle hooks is Autoscaling?
    Lifecycle hooks are used for Auto-scaling to put an additional wait time to a scale-in or a scale-out event.

34. What are the policies that you can set for your user’s passwords?
    Following are the policies that can be set for user’s passwords:

You can set a minimum length of the password.
You can ask the users to add at least one number or special character to the password.
Assigning the requirements of particular character types, including uppercase letters, lowercase letters, numbers, and non-alphanumeric characters.
You can enforce automatic password expiration, prevent the reuse of old passwords, and request for a password reset upon their next AWS sign-in.
You can have the AWS users contact an account administrator when the user has allowed the password to expire.



Question 1. What Do You Know About The Amazon Database?

Answer :

Amazon database is one of the Amazon Web Services that offers managed database along with managed service and NoSQL. It is also a fully managed petabyte-scale data warehouse service and in-memory caching as a service. There are four AWS database services, the user can choose to use one or multiple that meet the requirements. Amazon database services are – DynamoDB, RDS, RedShift, and Elastic ache.

Question 2. Explain Amazon Relational Database?

Answer :

Amazon relational database is a service that helps users with a number of services such as operation, lining up, and scaling an on-line database within the cloud. It automates the admin tasks such as info setup, hardware provisioning, backups, and mending. Amazon relational database provides users with resizable and cost-effective capability. By automating the tasks, it saves time and thus let user concentrate on the applications and provide them high availableness, quick performance, compatibility, and security.

There are a number of AWS RDS engines, such as:

Mysql
Oracle
PostgreSQL
SQL Server
MariaDB
Amazon Aurora
Amazon Web Services (AWS) Interview Questions
Question 3. What Are The Features Of Amazon Database?

Answer :

Following are the important features of Amazon Database:

Easy to administer
Highly scalable
Durable and reliable
Faster performance
Highly available
More secure
Cost-effective
Question 4. Which Of The Aws Db Service Is A Nosql Database And Server-less, And Delivers Consistent Single-digit Millisecond Latency At Any Scale?

Answer :

Amazon DynamoDB.

Question 5. What Is The Key-value Store?

Answer :

Key-value store is a database service which facilitates the storing, updating, and querying of the objects which are generally identified with the key and values. These objects consist of the keys and values which constitutes the actual content that is stored.

Aws Cloud Architect Interview Questions
Question 6. What Is Dynamodb?

Answer :

DynamoDB is a NoSQL database service that provides an inevitable and faster performance. DynamoDB is superintendent and offers a high level of scalability. DynamoDB makes users not to worry about the configuration, setup, hardware provisioning, throughput capacity, replication, software patching or cluster scaling. It helps users in offloading the scaling and operating distributed databases to AWS.

Question 7. List Some Of The Benefits Of Using Amazon Dynamodb?

Answer :

Amazon DynamoDB is the NoSQL service that provides a number of benefits to the users.

Some of the benefits of AWS DynamoDB are:–

Being a self-managed service, DynamoDB doesn’t require the experts for setup, installation, cluster etc.
It provides inevitable and faster performance.
It is highly scalable, available, and durable.
It provides very high throughput at the low latency.
It is highly cost-effective.
It supports and allows the creation of dynamic tables with multi-values attributes i.e. it’s flexible in nature.
Aws Devops Interview Questions
Question 8. What Is A Dynamodbmapper Class?

Answer :

The mapper class is the entry point of the DynamoDB. It allows users to enter the DynamoDB and access the endpoint. DynamoDB mapper class helps users access the data stored in various tables, then execute queries, scan them against the tables, and perform CRUD operations on the data items.

Question 9. What Are The Data Types Supported By Dynamodb?

Answer :

DynamoDB supports different types of data types such as collection data types, scalar data types, and even null values.

Scalar Data Types – The scalar data types supported by DynamoDB are:

Binary
Number
Boolean
String
Collection Data Types – The collection data types supported by DynamoDB are:

Binary Set
Number Set
String Set
Heterogeneous Map
Heterogeneous List
AWS EC2 Interview Questions
Question 10. What Do You Understand By Dynamodb Auto Scaling?

Answer :

DynamoDB Auto scaling specifies its specialized feature to automatically scale up and down its own read and write capacity or global secondary index.

Question 11. What Is A Data Warehouse And How Aws Redshift Can Play A Vital Role In The Storage?

Answer :

A data warehouse can be thought of a repository where the data generated from the company’s systems and other sources is collected and stored. So a data warehouse has three-tier architecture:

In the bottom tier, we have the tools which cleanse and collect the data.
In the middle tier, we have tools which transform the data using Online Analytical Processing Server.
In the top tier, we have different tools where data analysis and data mining is performed at the front end.
Setting up and managing a data warehouse involves a lot of money as the data in an organization continuously increases and the organization has to continuously upgrade their data storage servers. So here AWS RedShift comes into existence where the companies store their data in the cloud-based warehouses provided by Amazon.

AWS VPC Interview Questions
Question 12. What Is Amazon Redshift And Why Is It Popular Among Other Cloud Data Warehouses?

Answer :

Amazon RedShift is a fast and scalable data warehouse which is easy to use and is cost effective to manage all the organization’s data. The database is ranged from gigabytes to 100’s of petabyte of cloud data storage. A person does not need knowledge of any programming language to use this feature, just upload the cluster and tools which are already known to the user he can start using RedShift.

AWS RedShift is popular due to the following reasons:

AWS RedShift is very easy to use: In the console of AWS RedShift, you will find an option of creating a cluster. Just click on that and leave the rest on the machine programming of RedShift. Just fill the correct details as asked and launch the cluster. Now the cluster is ready to be used as RedShift automated most of the task like managing, monitoring and scaling.
Scaling of Warehouse is very easy: You just have to resize the cluster size by increasing the number of compute nodes.
RedShift gives 10x times better and fast performance: It makes use of specific strategies like columnar storage and massive parallel processing strategies to deliver high throughput and response time.
Economical: As it does not require any setup so cost reduces down to 1/10th of the traditional data warehouse.
Amazon Web Services (AWS) Interview Questions
Question 13. What Is Redshift Spectrum?

Answer :

The RedShift Spectrum allows you to run queries alongside petabyte of data which is unstructured and that too with no requirement of loading ETL. Spectrum scales millions of queries and allows you to allocate and store the data wherever you want and whatever the type of format is suitable for you.

Question 14. What Is A Leader Node And Compute Node?

Answer :

In a leader node the queries from the client application are received and then the queries are parsed and the execution plan is developed. The steps to process these queries are developed and the result is sent back to the client application.

In a compute node the steps assigned in the leader node are executed and the data is transmitted. The result is then sent back to the leader node before sending it to the client application.

Question 15. How To Load Data In Amazon Redshift?

Answer :

Amazon DynamoDB, Amazon EMR, AWS Glue, AWS Data Pipeline are some of the data sources by which you can load data in RedShift data warehouse. The clients can also connect to RedShift with the help of ODBC or JDBC and give the SQL command ‘insert’ to load the data.

AWS Cloud Support Engineer Interview Questions
Question 16. Mention The Database Engines Which Are Supported By Amazon Rds?

Answer :

The database engines that are supported by Amazon RDS are Amazon Aurora, Mysql, MariaDB, Oracle, SQL Server, and PostgreSQL database engine.

Question 17. What Is The Work Of Amazon Rds?

Answer :

When a user wants to set up a relational database then Amazon RDS is used. It provisions the infrastructure capacity that a user requests to install the database software. Once the database is set up and functional RDS automates the tasks like patching up of the software, taking the backup of the data and management of synchronous data replication with automatic failover.

AWS Lambda Interview Questions
Question 18. What Is The Purpose Of Standby Rds Instance?

Answer :

The main purpose of launching a standby RDS instance is to prevent the infrastructure failure (in case failure occurs) so it is stored in a different availability zone which is a totally different infrastructure physically and independent.

Aws Cloud Architect Interview Questions
Question 19. Are Rds Instances Upgradable Or Down Gradable According To The Need?

Answer :

Yes, you can upgrade the RDS instances with the help of following command: modify-db-instance. If you are unable to detect the amount of CPU needed to upgrade then start with db.m1.small DB instance class and monitor the utilization of CPU with the help of tool Amazon Cloud Watch Service.

Question 20. What Is Amazon Elastic Ache?

Answer :

Amazon Elastic ache is an in-memory key-value store which is capable of supporting two key-value engines – Redis and Memcached. It is a fully managed and zero administrations which are hardened by Amazon. With the help of Amazon Elastic ache, you can either build a new high-performance application or improve the existing application. You can find the various application of Elastic ache in the field of Gaming, Healthcare, etc.

Aws Cloudwatch Interview Questions
Question 21. What Is The Use Of Amazon Elastic Ache?

Answer :

The performance of web applications could be improved with the help of the caching of information that is used again and again. The information can be accessed very fast using in-memory-caching. With Elastic ache there is no need of managing a separate caching server. You can easily deploy or run an open source compatible in-memory data source with high throughput and low latency.

Question 22. What Are The Benefits Of Amazon Elastic Ache?

Answer :

There are various benefits of using Amazon Elastic ache some of which are discussed below:

The cache node failures are automatically detected and recovered.
It can be easily integrated with other AWS so as to provide a high performance and secured in-memory cache.
As most of the data is managed by Elastic ache such as setup, configuration, and monitoring so that the user can focus on other high-value applications.
The performance is enhanced greatly as it only supports the applications which require a very less response time.
The Elastic ache can easily scale itself up or scale down according to the need.
Question 23. Explain The Types Of Engines In Elastic Ache?

Answer :

There is two type of engine supported in Elastic ache: Memcached and Redis.

Memcached:

It is a popular in-memory data store which the developers use for the high-performance cache to speed up applications. By storing the data in memory instead of disk Memcached can retrieve the data in less than a millisecond. It works by keeping every value of the key for every other data to be stored and uniquely identifies each data and lets Memcached quickly find the record.

Redis:

Today’s applications need low latency and high throughput performance for real-time processing. Due to the performance, simplicity, and capability of redis, it is most favored by the developers. It provides high performance for real-time apps and sub-millisecond latency. It supports complex data types i.n. string, hashes, etc and has a backup and restore capabilities. While Memcached supports key names and values up to 1 MB only redis supports up to 512 MB.

Question 24. Is It Possible To Run Multiple Db Instances For Free For Amazon Rds?

Answer :

Yes, it is possible to run more than one Single-AZ micro DB instance for Amazon RDS and that’s for free. However, if the usage exceeds 750 instance hours across all the RDS Single-AZ micro DB instances, billing will be done at the standard Amazon RDS pricing across all the regions and database engines.

For example, consider we are running 2 Single-AZ micro DB instances for 400 hours each in one month only; the accumulated usage will be 800 instance hours from which 750 instance hours will be free. In this case, you will be billed for the remaining 50 hours at the standard pricing of Amazon RDS.

Aws Devops Interview Questions
Question 25. Which Aws Services Will You Choose For Collecting And Processing E-commerce Data For Real-time Analysis?

Answer :

I’ll use DynamoDB for collecting and processing e-commerce data for real-time analysis. DynamoDB is a fully managed NoSQL database service that can be used for any type of unstructured data. It can even be used for the e-commerce data taken from e-commerce websites. On this retrieved e-commerce data, analysis can be then performed using RedShift. Elastic MapReduce can also be used for analysis but we’ll avoid it here as real-time analysis if required.

Question 26. What Will Happen To The Db Snapshots And Backups If Any User Deletes Db Instance?

Answer :

When a dB instance is deleted, the user receives an option of making a final dB snapshot. If you will do that it will restore your information from that snapshot. AWS RDS keeps all these dB snapshots together that are created by the user along with the all other manually created dB snapshots when the dB instance is deleted. At the same time, automated backups are deleted while manually created dB snapshots are preserved.