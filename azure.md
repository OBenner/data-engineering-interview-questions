Question 1. What Are The Three Main Components Of Windows Azure Platform?

Answer :

Compute
Storage
AppFabric
Question 2. What Are The Service Model In Cloud Computing?

Answer :

Cloud computing providers offer their services according to three fundamental models: Infrastructure as a service (IaaS), platform as a service (PaaS), and software as a service (SaaS) where IaaS is the most basic and each higher model abstracts from the details of the lower models.

Examples of IaaS include: Amazon CloudFormation (and underlying services such as Amazon EC2), Rackspace Cloud, Terremark, Windows Azure Virtual Machines, Google Compute Engine. and Joyent.

Examples of PaaS include: Amazon Elastic Beanstalk, Cloud Foundry, Heroku, Force.com, EngineYard, Mendix, Google App Engine, Windows Azure Compute and OrangeScape.

Examples of SaaS include: Google Apps, Microsoft Office 365, and Onlive.

Microsoft Outlook Interview Questions
Question 3. How Many Types Of Deployment Models Are Used In Cloud?

Answer :

There are 4 types of deployment models used in cloud:

Public cloud
Private cloud
Community cloud
Hybrid cloud
Question 4. What Is Windows Azure Platform?

Answer :

A collective name of Microsoft’s Platform as a Service (PaaS) offering which provides a programming platform, a deployment vehicle, and a runtime environment of cloud computing hosted in Microsoft datacenters.

MVC Framework Tutorial
Question 5. What Are The Roles Available In Windows Azure?

Answer :

All three roles (web, worker, VM) are essentially Windows Server 2008. Web and Worker roles are nearly identical: With Web and Worker roles, the OS and related patches are taken care for you; you build your app’s components without having to manage a VM.

MVC Framework Interview Questions
Question 6. What Is Difference Between Windows Azure Platform And Windows Azure?

Answer :

The former is Microsoft’s PaaS offering including Windows Azure, SQL Azure, and Appfabric; while the latter is part of the offering and the Microsoft’s cloud OS.

Question 7. What Are The Three Types Of Roles In Compute Component In Windows Azure?

Answer :

WEB
Worker
VM
Microsoft Entity Framework Tutorial Microsoft Entity Framework Interview Questions
Question 8. What Is Windows Azure Compute Emulator?

Answer :

The compute emulator is a local emulator of Windows Azure that you can use to build and test your application before deploying it to Windows Azure.

Question 9. What Is Fabric?

Answer :

In the Windows Azure cloud fabric is nothing but a combination of many virtualized instances which run client application.

JqueryUI Interview Questions
Question 10. How Many Instances Of A Role Should Be Deployed To Satisfy Azure Sla (service Level Agreement) ? And What’s The Benefit Of Azure Sla?

Answer :

TWO. And if we do so, the role would have external connectivity at least 99.95% of the time.

JqueryUI Tutorial
Question 11. What Are The Options To Manage Session State In Windows Azure?

Answer :

► Windows Azure Caching

► SQL Azure

► Azure Table

Microsoft Office SharePoint Server (MOSS) Interview Questions
Question 12. What Is Cspack?

Answer :

It is a command-line tool that generates a service package file (.cspkg) and prepares an application for deployment, either to Windows Azure or to the compute emulator.

Microsoft Outlook Interview Questions
Question 13. What Is Csrun?

Answer :

It is a command-line tool that deploys a packaged application to the Windows Azure compute emulator and manages the running service.

Windows Presentation Foundation(WPF) Tutorial
Question 14. What Is Guest Os?

Answer :

It is the operating system that runs on the virtual machine that hosts an instance of a role.

Question 15. How To Programmatically Scale Out Azure Worker Role Instances?

Answer :

Using AutoScaling Application Block.

Microsoft Solutions Framework (MSF) Interview Questions
Question 16. What Is Web Role In Windows Azure?

Answer :

Web roles in Windows Azure are special purpose, and provide a dedicated Internet Information Services (IIS) web-server used for hosting front-end web applications. You can quickly and easily deploy web applications to Web Roles and then scale your Compute capabilities up or down to meet demand.

Windows Communication Foundation (WCF) Tutorial
Question 17. What Is The Difference Between Public Cloud And Private Cloud?

Answer :

Public cloud is used as a service via Internet by the users, whereas a private cloud, as the name conveys is deployed within certain boundaries like firewall settings and is completely managed and monitored by the users working on it in an organization.

Windows Presentation Foundation(WPF) Interview Questions
Question 18. What Is Windows Azure Diagnostics?

Answer :

Windows Azure Diagnostics enables you to collect diagnostic data from an application running in Windows Azure. You can use diagnostic data for debugging and troubleshooting, measuring performance, monitoring resource usage, traffic analysis and capacity planning, and auditing.

MVC Framework Interview Questions
Question 19. What Is Blob?

Answer :

BLOB stands for Binary Large Object. Blob is file of any type and size.

The Azure Blob Storage offers two types of blobs:

1. Block Blob
2. Page Blob

URL format: Blobs are addressable using the following URL format:

http://.blob.aaa.windows.net//

Spring MVC Framework Tutorial
Question 20. What Is The Difference Between Block Blob Vs Page Blob?

Answer :

Block blobs are comprised of blocks, each of which is identified by a block ID.

You create or modify a block blob by uploading a set of blocks and committing them by their block IDs.

If you are uploading a block blob that is no more than 64 MB in size, you can also upload it in its entirety with a single Put Blob operation. -Each block can be a maximum of 4 MB in size. The maximum size for a block blob in version 2009-09-19 is 200 GB, or up to 50,000 blocks.

Page blobs are a collection of pages. A page is a range of data that is identified by its offset from the start of the blob. To create a page blob, you initialize the page blob by calling Put Blob and specifying its maximum size.

-The maximum size for a page blob is 1 TB. A page written to a page blob may be up to 1 TB in size.

what to use block blobs for: streaming video. “The application must provide random read/write access” which is supported by Page Blobs

Windows Communication Foundation (WCF) Interview Questions
Question 21. What Is The Difference Between Windows Azure Queues And Windows Azure Service Bus Queues?

Answer :

Windows Azure supports two types of queue mechanisms:

Windows Azure Queues and Service Bus Queues .

Windows Azure Queues: which are part of the Windows Azure storage infrastructure, feature a simple REST-based Get/Put/Peek interface, providing reliable, persistent messaging within and between services.

Service Bus Queues: are part of a broader Windows Azure messaging infrastructure that supports queuing as well as publish/subscribe, Web service remoting, and integration patterns.

Question 22. What Is Deadletter Queue?

Answer :

Messages are placed on the deadletter sub-queue by the messaging system in the following scenarios.

► When a message expires and deadlettering for expired messages is set to true in a queue or subscription.

► When the max delivery count for a message is exceeded on a queue or subscription.

► When a filter evaluation exception occurs in a subscription and deadlettering is enabled on filter evaluation exceptions.

Windows Server 2012 Tutorial
Question 23. What Are Instance Sizes Of Azure?

Answer :

Windows Azure will handle the load balancing for all of the instances that are created. The VM sizes are as follows:

Compute Instance Size CPU Memory Instance Storage I/O Performance

► Extra Small 1.0 Ghz 768 MB 20 GB Low

► Small 1.6 GHz 1.75 GB 225 GB Moderate

► Medium 2 x 1.6 GHz 3.5 GB 490 GB High

► Large 4 x 1.6 GHz 7 GB 1,000 GB High

► Extra large 8 x 1.6 GHz 14 GB 2,040 GB High

Spring MVC Framework Interview Questions
Question 24. What Is Table Storoage In Windows Azure?

Answer :

The Windows Azure Table storage service stores large amounts of structured data.

The service is a NoSQL datastore which accepts authenticated calls from inside and outside the Windows Azure cloud.

Windows Azure tables are ideal for storing structured, non-relational data

Table: A table is a collection of entities. Tables don’t enforce a schema on entities, which means a single table can contain entities that have different sets of properties. An account can contain many tables

Entity: An entity is a set of properties, similar to a database row. An entity can be up to 1MB in size.

Properties: A property is a name-value pair. Each entity can include up to 252 properties to store data. Each entity also has 3 system properties that specify a partition key, a row key, and a timestamp.

Entities with the same partition key can be queried more quickly, and inserted/updated in atomic operations. An entity’s row key is its unique identifier within a partition.

Microsoft Entity Framework Interview Questions
Question 25. Difference Between Web And Worker Roles In Windows Azure?

Answer :

The main difference between the two is that an instance of a web role runs IIS, while an instance of a worker role does not. Both are managed in the same way, however, and it’s common for an application to use both.For example, a web role instance might accept requests from users, then pass them to a worker role instance for processing.

Question 26. What Is Azure Fabric Controller?

Answer :

The Windows Azure Fabric Controller is a resource provisioning and management layer that manages the hardware, and provides resource allocation, deployment/upgrade, and management for cloud services on the Windows Azure platform.

Advanced jQuery Interview Questions
Question 27. What Is Autoscaling?

Answer :

Scaling by adding additional instances is often referred to as scaling out. Windows Azure also supports scaling up by using larger role instances instead of more role instances.

By adding and removing role instances to your Windows Azure application while it is running, you can balance the performance of the application against its running costs.

An autoscaling solution reduces the amount of manual work involved in dynamically scaling an application.

JqueryUI Interview Questions
Question 28. What Is Vm Role In Windows Azure?

Answer :

Virtual Machine (VM) roles, now in Beta, enable you to deploy a custom Windows Server 2008 R2 (Enterprise or Standard) image to Windows Azure. You can use the VM role when your application requires a large number of server OS customizations and cannot be automated. The VM Role gives you full control over your application environment and lets you migrate existing applications to the cloud.

Question 29. Apart From .net Framework, Name Other Three Language/framework That Can Be Used To Develop Windows Azure Applications?

Answer :

php, node.js, java

Azure Cosmos DB Interview Questions
Question 30. How Would You Categorize Windows Azure? (iaas/paas/saas)?

Answer :

PaaS (Platform as a Service)

Question 31. What Is Azure Cloud Service?

Answer :

By creating a cloud service, you can deploy a multi-tier web application in Azure, defining multiple roles to distribute processing and allow flexible scaling of your application. A cloud service consists of one or more web roles and/or worker roles, each with its own application files and configuration. Azure Websites and Virtual Machines also enable web applications on Azure. The main advantage of cloud services is the ability to support more complex multi-tier architectures

Question 32. What Is A Cloud Service Role?

Answer :

A cloud service role is comprised of application files and a configuration. A cloud service can have two types of role.

Windows Controls Interview Questions
Question 33. What Is Link A Resource ?

Answer :

To show your cloud service’s dependencies on other resources, such as an Azure SQL Database instance, you can “link” the resource to the cloud service. In the Preview Management Portal, you can view linked resources on the Linked Resources page, view their status on the dashboard, and scale a linked SQL Database instance along with the service roles on the Scale page. Linking a resource in this sense does not connect the resource to the application; you must configure the connections in the application code.

Microsoft Office SharePoint Server (MOSS) Interview Questions
Question 34. What Is Scale A Cloud Service ?

Answer :

A cloud service is scaled out by increasing the number of role instances (virtual machines) deployed for a role. A cloud service is scaled in by decreasing role instances. In the Preview Management Portal, you can also scale a linked SQL Database instance, by changing the SQL Database edition and the maximum database size, when you scale your service roles.

Question 35. What Is A Web Role ?

Answer :

A web role provides a dedicated Internet Information Services (IIS) web-server used for hosting front-end web applications.

Question 36. What Is A Worker Role ?

Answer :

Applications hosted within worker roles can run asynchronous, long-running or perpetual tasks independent of user interaction or input.

Microsoft Solutions Framework (MSF) Interview Questions
Question 37. What Is A Role Instance ?

Answer :

A role instance is a virtual machine on which the application code and role configuration run. A role can have multiple instances, defined in the service configuration file.

Question 38. What Is A Guest Operating System ?

Answer :

The guest operating system for a cloud service is the operating system installed on the role instances (virtual machines) on which your application code runs.

Question 39. What Is A Cloud Service Components?

Answer :

Three components are required in order to deploy an application as a cloud service in Azure.

Question 40. What Is Deployment Environments?

Answer :

Azure offers two deployment environments for cloud services: a staging environment in which you can test your deployment before you promote it to the production environment. The two environments are distinguished only by the virtual IP addresses (VIPs) by which the cloud service is accessed. In the staging environment, the cloud service’s globally unique identifier (GUID) identifies it in URLs (GUID.cloudapp.net). In the production environment, the URL is based on the friendlier DNS prefix assigned to the cloud service (for example, myservice.cloudapp.net).

Windows Presentation Foundation(WPF) Interview Questions
Question 41. What Is Swap Deployments?

Answer :

To promote a deployment in the Azure staging environment to the production environment, you can “swap” the deployments by switching the VIPs by which the two deployments are accessed. After the deployment, the DNS name for the cloud service points to the deployment that had been in the staging environment.

Question 42. What Is Minimal Vs. Verbose Monitoring?

Answer :

Minimal monitoring, which is configured by default for a cloud service, uses performance counters gathered from the host operating systems for role instances (virtual machines). Verbose monitoring gathers additional metrics based on performance data within the role instances to enable closer analysis of issues that occur during application processing.

Windows Communication Foundation (WCF) Interview Questions
Question 43. What Is A Service Definition File?

Answer :

The cloud service definition file (.csdef) defines the service model, including the number of roles.

Question 44. What Is A Service Configuration File?

Answer :

The cloud service configuration file (.cscfg) provides configuration settings for the cloud service and individual roles, including the number of role instances.

Question 45. What Is A Service Package ?

Answer :

The service package (.cspkg) contains the application code and the service definition file.

Question 46. What Is A Cloud Service Deployment ?

Answer :

A cloud service deployment is an instance of a cloud service deployed to the Azure staging or production environment. You can maintain deployments in both staging and production.

Question 47. What Is Azure Diagnostics ?

Answer :

Azure Diagnostics is the API that enables you to collect diagnostic data from applications running in Azure. Azure Diagnostics must be enabled for cloud service roles in order for verbose monitoring to be turned on. For more information.

Question 48. What Is Azure Service Level Agreement (sla) ?

Answer :

The Azure Compute SLA guarantees that, when you deploy two or more role instances for every role, access to your cloud service will be maintained at least 99.95 percent of the time. Also, detection and corrective action will be initiated 99.9 percent of the time when a role instance’s process is not running.