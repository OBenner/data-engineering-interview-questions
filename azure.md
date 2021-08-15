# Azure
+ [What are the three Main Components of Windows Azure Platform?](#What-are-the-three-Main-Components-of-Windows-Azure-Platform)
+ [What are the Service Model in Cloud Computing?](#What-are-the-Service-Model-in-Cloud-Computing)
+ [How many Types of Deployment Models are used in Cloud?](#How-many-Types-of-Deployment-Models-are-used-in-Cloud)
+ [What is Windows Azure Platform?](#What-is-Windows-Azure-Platform)
+ [What are the Roles Available in Windows Azure?](#What-are-the-Roles-Available-in-Windows-Azure)
+ [What is difference between Windows Azure Platform and Windows Azure?](#What-is-difference-between-Windows-Azure-Platform-and-Windows-Azure)
+ [What are the three Types of Roles in Compute Component in Windows Azure?](#What-are-the-three-Types-of-Roles-in-Compute-Component-in-Windows-Azure)
+ [What is Windows Azure Compute Emulator?](#What-is-Windows-Azure-Compute-Emulator)
+ [What is Fabric?](#What-is-Fabric)
+ [How many instances of a Role should be deployed to Satisfy Azure Sla?](#How-many-instances-of-a-Role-should-be-deployed-to-Satisfy-Azure-Sla)
+ [What are the options to manage Session State in Windows Azure?](#What-are-the-options-to-manage-Session-State-in-Windows-Azure)
+ [What is Cspack?](#What-is-Cspack)
+ [What is Csrun?](#What-is-Csrun)
+ [What is Guest Os?](#What-is-Guest-Os)
+ [How to programmatically Scale Out Azure Worker Role Instances?](#How-to-programmatically-Scale-Out-Azure-Worker-Role-Instances)
+ [What is Web Role in Windows Azure?](#What-is-Web-Role-in-Windows-Azure)
+ [What is the difference between Public Cloud and Private Cloud?](#What-is-the-difference-between-Public-Cloud-and-Private-Cloud)
+ [What is Windows Azure Diagnostics?](#What-is-Windows-Azure-Diagnostics)
+ [What is Blob?](#What-is-Blob)
+ [What is the difference between Block Blob Vs Page Blob?](#What-is-the-difference-between-Block-Blob-Vs-Page-Blob)
+ [What is the difference between Windows Azure Queues and Windows Azure Service Bus Queues?](#What-is-the-difference-between-Windows-Azure-Queues-and-Windows-Azure-Service-Bus-Queues)
+ [What is Deadletter Queue?](#What-is-Deadletter-Queue)
+ [What are Instance Sizes of Azure?](#What-are-Instance-Sizes-of-Azure)
+ [ What is Table Storage in Windows Azure?](#What-is-Table-Storage-in-Windows-Azure)
+ [Difference between Web and Worker Roles in Windows Azure?](#Difference-between-Web-and-Worker-Roles-in-Windows-Azure)
+ [What is Azure Fabric Controller?](#What-is-Azure-Fabric-Controller)
+ [What is Autoscaling?](#What-is-Autoscaling)
+ [What is Vm Role in Windows Azure?](#What-is-Vm-Role-in-Windows-Azure)
+ [Apart from dotnet Framework please name other three language framework that can be used to Develop Windows Azure Applications?](#Apart-from-dotnet-Framework-please-name-other-three-language-framework-that-can-be-used-to-Develop-Windows-Azure-Applications)
+ [How would you categorize Windows Azure?](#How-would-you-categorize-Windows-Azure)
+ [What is Azure Cloud Service?](#What-is-Azure-Cloud-Service)
+ [What is Cloud Service Role?](#What-is-Cloud-Service-Role)
+ [What is Link Resource?](#What-is-Link-Resource)
+ [What is Scale Cloud Service?](#What-is-Scale-Cloud-Service)
+ [What is Web Role ?](#What-is-Web-Role)
+ [What is Worker Role ?](#What-is-Worker-Role)
+ [ What is Role Instance ?](#What-is-Role-Instance)
+ [What is Guest Operating System ?](#What-is-Guest-Operating-System)
+ [What is Cloud Service Components?](#What-is-Cloud-Service-Components)
+ [What is Deployment Environments?](#What-is-Deployment-Environments)
+ [What is Swap Deployments?](#What-is-Swap-Deployments)
+ [What is Minimal Vs Verbose Monitoring?](#What-is-Minimal-Vs-Verbose-Monitoring)
+ [What is Service Definition File?](#What-is-Service-Definition-File)
+ [What is Service Configuration File?](#What-is-Service-Configuration-File)
+ [What is Service Package ?](#What-is-Service-Package)
+ [What is Cloud Service Deployment ?](#What-is-Cloud-Service-Deployment)
+ [What is Azure Diagnostics ?](#What-is-Azure-Diagnostics)
+ [What is Azure Service Level Agreement?](#What-is-Azure-Service-Level-Agreement)
## What are the three Main Components of Windows Azure Platform?
+ Compute
+ Storage
+ AppFabric

[Table of Contents](#Azure)

## What are the Service Model in Cloud Computing?
Cloud computing providers offer their services according to three fundamental models: Infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS) where IaaS is the most basic and each higher model abstracts from the details of the lower models.
Examples of IaaS include: Amazon CloudFormation (and underlying services such as Amazon EC2), Rackspace Cloud, Terremark, Windows Azure Virtual Machines, Google Compute Engine. and Joyent.
Examples of PaaS include: Amazon Elastic Beanstalk, Cloud Foundry, Heroku, Force.com, EngineYard, Mendix, Google App Engine, Windows Azure Compute and OrangeScape.
Examples of SaaS include: Google Apps, Microsoft Office 365, and Onlive.

[Table of Contents](#Azure)

## How many Types of Deployment Models are used in Cloud?
There are 4 types of deployment models used in cloud:
+ Public cloud
+ Private cloud
+ Community cloud
+ Hybrid cloud

[Table of Contents](#Azure)

## What is Windows Azure Platform?
A collective name of Microsoft’s Platform as a Service (PaaS) offering which provides a programming platform, a deployment vehicle, and a runtime environment of cloud computing hosted in Microsoft datacenters.

[Table of Contents](#Azure)

## What are the Roles Available in Windows Azure?
All three roles (web, worker, VM) are essentially Windows Server 2008. Web and Worker roles are nearly identical: With Web and Worker roles, the OS and related patches are taken care for you; you build your app’s components without having to manage a VM.

[Table of Contents](#Azure)

## What is difference between Windows Azure Platform and Windows Azure?
The former is Microsoft’s PaaS offering including Windows Azure, SQL Azure, and Appfabric; while the latter is part of the offering and the Microsoft’s cloud OS.

[Table of Contents](#Azure)

## What are the three Types of Roles in Compute Component in Windows Azure?
+ WEB
+ Worker
+ VM

[Table of Contents](#Azure)

## What is Windows Azure Compute Emulator?
The compute emulator is a local emulator of Windows Azure that you can use to build and test your application before deploying it to Windows Azure.

[Table of Contents](#Azure)

## What is Fabric?
In the Windows Azure cloud fabric is nothing but a combination of many virtualized instances which run client application.

[Table of Contents](#Azure)

## How many instances of a Role should be deployed to Satisfy Azure Sla?
TWO. And if we do so, the role would have external connectivity at least 99.95% of the time.

[Table of Contents](#Azure)

## What are the options to manage Session State in Windows Azure?
► Windows Azure Caching
► SQL Azure
► Azure Table

[Table of Contents](#Azure)

## What is Cspack?
It is a command-line tool that generates a service package file (.cspkg) and prepares an application for deployment, either to Windows Azure or to the compute emulator.

[Table of Contents](#Azure)

## What is Csrun?
It is a command-line tool that deploys a packaged application to the Windows Azure compute emulator and manages the running service.

[Table of Contents](#Azure)

## What is Guest Os?
It is the operating system that runs on the virtual machine that hosts an instance of a role.

[Table of Contents](#Azure)

## How to programmatically Scale Out Azure Worker Role Instances?
Using AutoScaling Application Block.

[Table of Contents](#Azure)

## What is Web Role in Windows Azure?
Web roles in Windows Azure are special purpose, and provide a dedicated Internet Information Services (IIS) web-server used for hosting front-end web applications. You can quickly and easily deploy web applications to Web Roles and then scale your Compute capabilities up or down to meet demand.

[Table of Contents](#Azure)

## What is the difference between Public Cloud and Private Cloud?
Public cloud is used as a service via Internet by the users, whereas a private cloud, as the name conveys is deployed within certain boundaries like firewall settings and is completely managed and monitored by the users working on it in an organization.

[Table of Contents](#Azure)

## What is Windows Azure Diagnostics?
Windows Azure Diagnostics enables you to collect diagnostic data from an application running in Windows Azure. You can use diagnostic data for debugging and troubleshooting, measuring performance, monitoring resource usage, traffic analysis and capacity planning, and auditing.

[Table of Contents](#Azure)

## What is Blob?
BLOB stands for Binary Large Object. Blob is file of any type and size.
The Azure Blob Storage offers two types of blobs:
1. Block Blob
2. Page Blob
URL format: Blobs are addressable using the following URL format:
http://.blob.aaa.windows.net//

[Table of Contents](#Azure)

## What is the difference between Block Blob Vs Page Blob?
Block blobs are comprised of blocks, each of which is identified by a block ID.
You create or modify a block blob by uploading a set of blocks and committing them by their block IDs.
If you are uploading a block blob that is no more than 64 MB in size, you can also upload it in its entirety with a single Put Blob operation. -Each block can be a maximum of 4 MB in size. The maximum size for a block blob in version 2009-09-19 is 200 GB, or up to 50,000 blocks.
Page blobs are a collection of pages. A page is a range of data that is identified by its offset from the start of the blob. To create a page blob, you initialize the page blob by calling Put Blob and specifying its maximum size.
-The maximum size for a page blob is 1 TB. A page written to a page blob may be up to 1 TB in size.
what to use block blobs for: streaming video. “The application must provide random read/write access” which is supported by Page Blobs

[Table of Contents](#Azure)

## What is the difference between Windows Azure Queues and Windows Azure Service Bus Queues?
Windows Azure supports two types of queue mechanisms:
Windows Azure Queues and Service Bus Queues .
Windows Azure Queues: which are part of the Windows Azure storage infrastructure, feature a simple REST-based Get/Put/Peek interface, providing reliable, persistent messaging within and between services.
Service Bus Queues: are part of a broader Windows Azure messaging infrastructure that supports queuing as well as publish/subscribe, Web service remoting, and integration patterns.

[Table of Contents](#Azure)

## What is Deadletter Queue?
Messages are placed on the deadletter sub-queue by the messaging system in the following scenarios.
► When a message expires and deadlettering for expired messages is set to true in a queue or subscription.
► When the max delivery count for a message is exceeded on a queue or subscription.
► When a filter evaluation exception occurs in a subscription and deadlettering is enabled on filter evaluation exceptions.

[Table of Contents](#Azure)

## What are Instance Sizes of Azure?
Windows Azure will handle the load balancing for all the instances that are created. The VM sizes are as follows:
Compute Instance Size CPU Memory Instance Storage I/O Performance
► Extra Small 1.0 Ghz 768 MB 20 GB Low
► Small 1.6 GHz 1.75 GB 225 GB Moderate
► Medium 2 x 1.6 GHz 3.5 GB 490 GB High
► Large 4 x 1.6 GHz 7 GB 1,000 GB High
► Extra large 8 x 1.6 GHz 14 GB 2,040 GB High

[Table of Contents](#Azure)

##  What is Table Storage in Windows Azure?
The Windows Azure Table storage service stores large amounts of structured data.
The service is a NoSQL datastore which accepts authenticated calls from inside and outside the Windows Azure cloud.
Windows Azure tables are ideal for storing structured, non-relational data
Table: A table is a collection of entities. Tables don’t enforce a schema on entities, which means a single table can contain entities that have different sets of properties. An account can contain many tables
Entity: An entity is a set of properties, similar to a database row. An entity can be up to 1MB in size.
Properties: A property is a name-value pair. Each entity can include up to 252 properties to store data. Each entity also has 3 system properties that specify a partition key, a row key, and a timestamp.
Entities with the same partition key can be queried more quickly, and inserted/updated in atomic operations. An entity’s row key is its unique identifier within a partition.

[Table of Contents](#Azure)

## Difference between Web and Worker Roles in Windows Azure?
The main difference between the two is that an instance of a web role runs IIS, while an instance of a worker role does not. Both are managed in the same way, however, and it’s common for an application to use both.For example, a web role instance might accept requests from users, then pass them to a worker role instance for processing.

[Table of Contents](#Azure)

## What is Azure Fabric Controller?
The Windows Azure Fabric Controller is a resource provisioning and management layer that manages the hardware, and provides resource allocation, deployment/upgrade, and management for cloud services on the Windows Azure platform.

[Table of Contents](#Azure)

## What is Autoscaling?
Scaling by adding additional instances is often referred to as scaling out. Windows Azure also supports scaling up by using larger role instances instead of more role instances.
By adding and removing role instances to your Windows Azure application while it is running, you can balance the performance of the application against its running costs.
An autoscaling solution reduces the amount of manual work involved in dynamically scaling an application.

[Table of Contents](#Azure)

## What is Vm Role in Windows Azure?
Virtual Machine (VM) roles, now in Beta, enable you to deploy a custom Windows Server 2008 R2 (Enterprise or Standard) image to Windows Azure. You can use the VM role when your application requires a large number of server OS customizations and cannot be automated. The VM Role gives you full control over your application environment and lets you migrate existing applications to the cloud.

[Table of Contents](#Azure)

## Apart from dotnet Framework please name other three language framework that can be used to Develop Windows Azure Applications?
php, node.js, java

[Table of Contents](#Azure)

## How would you categorize Windows Azure?
PaaS (Platform as a Service)

[Table of Contents](#Azure)

## What is Azure Cloud Service?
By creating a cloud service, you can deploy a multi-tier web application in Azure, defining multiple roles to distribute processing and allow flexible scaling of your application. A cloud service consists of one or more web roles and/or worker roles, each with its own application files and configuration. Azure Websites and Virtual Machines also enable web applications on Azure. The main advantage of cloud services is the ability to support more complex multi-tier architectures

[Table of Contents](#Azure)

## What is Cloud Service Role?
A cloud service role is comprised of application files and a configuration. A cloud service can have two types of role.

[Table of Contents](#Azure)

## What is Link Resource?
To show your cloud service’s dependencies on other resources, such as an Azure SQL Database instance, you can “link” the resource to the cloud service. In the Preview Management Portal, you can view linked resources on the Linked Resources page, view their status on the dashboard, and scale a linked SQL Database instance along with the service roles on the Scale page. Linking a resource in this sense does not connect the resource to the application; you must configure the connections in the application code.

[Table of Contents](#Azure)

## What is Scale Cloud Service?
A cloud service is scaled out by increasing the number of role instances (virtual machines) deployed for a role. A cloud service is scaled in by decreasing role instances. In the Preview Management Portal, you can also scale a linked SQL Database instance, by changing the SQL Database edition and the maximum database size, when you scale your service roles.

[Table of Contents](#Azure)

## What is Web Role ?
A web role provides a dedicated Internet Information Services (IIS) web-server used for hosting front-end web applications.

[Table of Contents](#Azure)

## What is Worker Role ?
Applications hosted within worker roles can run asynchronous, long-running or perpetual tasks independent of user interaction or input.

[Table of Contents](#Azure)

##  What is Role Instance ?
A role instance is a virtual machine on which the application code and role configuration run. A role can have multiple instances, defined in the service configuration file.

[Table of Contents](#Azure)

## What is Guest Operating System ?
The guest operating system for a cloud service is the operating system installed on the role instances (virtual machines) on which your application code runs.

[Table of Contents](#Azure)

## What is Cloud Service Components?
Three components are required in order to deploy an application as a cloud service in Azure.

[Table of Contents](#Azure)

## What is Deployment Environments?
Azure offers two deployment environments for cloud services: a staging environment in which you can test your deployment before you promote it to the production environment. The two environments are distinguished only by the virtual IP addresses (VIPs) by which the cloud service is accessed. In the staging environment, the cloud service’s globally unique identifier (GUID) identifies it in URLs (GUID.cloudapp.net). In the production environment, the URL is based on the friendlier DNS prefix assigned to the cloud service (for example, myservice.cloudapp.net).

[Table of Contents](#Azure)

## What is Swap Deployments?
To promote a deployment in the Azure staging environment to the production environment, you can “swap” the deployments by switching the VIPs by which the two deployments are accessed. After the deployment, the DNS name for the cloud service points to the deployment that had been in the staging environment.

[Table of Contents](#Azure)

## What is Minimal Vs Verbose Monitoring?
Minimal monitoring, which is configured by default for a cloud service, uses performance counters gathered from the host operating systems for role instances (virtual machines). Verbose monitoring gathers additional metrics based on performance data within the role instances to enable closer analysis of issues that occur during application processing.

[Table of Contents](#Azure)

## What is Service Definition File?
The cloud service definition file (.csdef) defines the service model, including the number of roles.

[Table of Contents](#Azure)

## What is Service Configuration File?
The cloud service configuration file (.cscfg) provides configuration settings for the cloud service and individual roles, including the number of role instances.

[Table of Contents](#Azure)

## What is Service Package ?
The service package (.cspkg) contains the application code and the service definition file.

[Table of Contents](#Azure)

## What is Cloud Service Deployment ?
A cloud service deployment is an instance of a cloud service deployed to the Azure staging or production environment. You can maintain deployments in both staging and production.

[Table of Contents](#Azure)

## What is Azure Diagnostics ?
Azure Diagnostics is the API that enables you to collect diagnostic data from applications running in Azure. Azure Diagnostics must be enabled for cloud service roles in order for verbose monitoring to be turned on. For more information.

[Table of Contents](#Azure)

## What is Azure Service Level Agreement?
The Azure Compute SLA guarantees that, when you deploy two or more role instances for every role, access to your cloud service will be maintained at least 99.95 percent of the time. Also, detection and corrective action will be initiated 99.9 percent of the time when a role instance’s process is not running.

[Table of Contents](#Azure)