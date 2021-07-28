Question 8. What Is The Main Difference Between View And Materialized View?

Answer :

The main difference between view and materialized view is as follows:

View:

Data representation is provided by view where the data is accessed from its table.
View has a logical structure which does not occupy space
All the changes are affected in corresponding tables.
Materialized View:

Within materialized view, pre-calculated data is available
The materialized view has a physical structure which does occupy space
All the changes are not reflected in the corresponding tables.
Question 9. What Is Junk Dimension?

Answer :

A junk dimension is nothing but a dimension where a certain type of data is stored which is not appropriate to store in the schema. The nature of the junk dimension is usually a Boolean has flag values.

A single dimension is formed by a group of small dimensions got together. This can be considered as junk dimension.

Oracle Data Integrator (ODI) Interview Questions
Question 10. What Is Data Warehouse Architecture?

Answer :

The data warehouse architecture is a three-tier architecture.

The following is the three-tier architecture:

Bottom Tier
Middle Tier
Upper Tier
It is nothing but a repository of integrating data which is extracted from different data sources.

Hadoop Tutorial
Question 11. What Is An Integrity Constraints? What Are Different Types Of Integrity Constraints?

Answer :

An integrity constraint is nothing but a specific requirement that the data in the database has to meet. It is nothing but a business rule for a particular column in a table. In the data warehouse concept, they are 5 integrity constraints.

The following are the integrity constraints:

Null
Unique key
Primary key
Foreign key
Check
Telecom Analytics Interview Questions
Question 12. Why Is That Data Architect Actually Monitor And Enforce Compliance Data Standards? What Is The Need?

Answer :

The primary idea of keeping the standards high on compliance for data standards is because it will help to reduce the data redundancy and helps the team to have a quality data. As this information is actually carried out or used throughout the organization.

Data Warehousing Interview Questions
Question 13. Explain The Different Data Models That Are Available In Detail?

Answer :

There are three different kinds of data models that are available and they are as follows:

Conceptual
Logical
Physical
Conceptual data model:

As the name itself implies that this data model depicts the high-level design of the available physical data.

Logical data model:

Within the logical model, the entity names, entity relationships, attributes, primary keys and foreign keys will show up.

Physical data model:

Based on this data model, the view will give out more information and showcases how the model is implemented in the database. All the primary keys, foreign keys, tables names and column names will be showing up.

Sqoop Tutorial
Question 14. Differentiate Between Dimension And Attribute?

Answer :

In short, dimensions are nothing but which represents qualitative data. For example data like a plan, product, class are all considered as dimensions.

The attribute is nothing but a subset of a dimension. Within a dimension table, we will have attributes. The attributes can be textual or descriptive. For example, product name and product category are nothing but an attribute of product dimensions.

Question 15. Differentiate Between Oltp And Olap?

Answer :

OLTP stands for Online Transaction Process System
OLTP is known for maintaining transactional level data of the organization and generally, they are highly normalized. If it is OLTP route then it is going to be a star schema design.
OLAP stands for Online Analytical process system.
OLAP is known for a lot of analysis and fulfills reporting purposes. It is de-normalized form.
If it is an OLAP route then it is going to be a snowflake schema design.
Database Design Interview Questions
Question 16. How To Become A Data Architect?

Answer :

The following are the prerequisites for an individual to start his career in Data Architect.

A bachelor's degree is essential and preferably in computer science background
No predefined certifications are necessary, but it is always good to have few certifications related to the field because few of the companies might expect. It is advisable to go through CDMA (Certified )
Data Management Professional)
Should have at least 3-8 years of IT experience.
Should be creative, innovative and good at problem-solving.
Has good programming knowledge and data modeling concepts
Should be well versed with the tools like SOA, ETL, ERP, XML etc
Apache Hive Tutorial
Question 17. The Responsibilities Of A Data Architect And Data Administrator Are The Same?

Answer :

No, not at all. The responsibilities of data architect are completely different from that of data administrator.

For example:

Data architect works on with data modeling and designs the database design in a robust manner where the users will be able to extract the information easily. When it comes to data administrators, they are responsible for having the databases run efficiently and effectively.

Sqoop Interview Questions
Question 18. Is Data Architect And Data Scientist Roles Are Similar?

Answer :

No, data architect and data scientist roles are two different roles in an organization.

The following are few activities that data architect is involved :

Data warehousing solutions
ETL activities
Data Architecture development activities
Data modelling
The following are few activities that data scientist is involved in:

Data cleansing and processing
Predictive modelling
Machine learning
Statistical analysis applied
Data visualization



Question 1. How Can We Run The Graph? What Is The Procedure For That? How Can We Schedule The Graph In Unix?

Answer :

If you want to run the graph through GDE then after save the graph just press F5 button of your keyboard, it will run automatically. If you want to run through the shell script then you have to fire the command at your UNIX box.

Question 2. What Is A Real-time Data Warehouse? How Is It Different From Near To Real-time Data Warehouse?

Answer :

As the term suggests, a real-time data warehouse is a system, which reflects all changes to its sources in real time. As simple as it sounds, this is still an area of active research in the field. In traditional DWH, the operational system(s) are kept separate from the DWH for a good reason.

The Operational systems are designed to accept inputs or changes to data regularly, hence have a good chance of being regularly queried. On the other hand, a DWH is supposed to do just the opposite - it is used to query data for reports only. No changes to data, through user actions is expected (or designed). The only inputs could come from the ETL feed at stipulated times. The ETL would source its data from the Operational systems just explained above.

To create a real-time DWH we would have to merge both systems (several ways are being explored), a concept that is against the reason of creating a DWH. Bigger challenges occur in terms of updating aggregated data in facts at real time, still maintaining the surrogate keys.

Besides, we would need lightening fast hardware to try this.Near Real time DWH is a trade-off between the conventional design and the dream of all clients today. The frequency of ETL updates in higher in this case for e.g. once in 2 hours. We can also analyze and use selective refreshes at shorter time intervals, while complete refreshes may still be kept further apart. Selective refreshes would look at only those tables that get updated regularly.

Informatica Interview Questions
Question 3. What Is Difference Between Drill & Scope Of Analysis?

Answer :

Drilling can be done in drill down, up, through, and across; scope is the overall view of the drill exercise.

Question 4. I Have Two Universes Created By Two Difference Database Can We Join Them In Designer & Report Level? How

Answer :

We can link one universe to other universe in Universe parameters.

Informatica Tutorial
Question 5. For Faster Process, What We Will Do With The Universe?

Answer :

For a faster process create aggregate tables and write better sql so that the process would fast.

Networking Interview Questions
Question 6. What Is Type 2 Version Dimension?

Answer :

Version dimension is the SCD type II in real time it using because of it will maintain the current data and full historical data.

Question 7. What Is Unit Testing?

Answer :

The Developer created the mapping that can be tested independently by the developer individually.

Data Warehousing Tutorial System Administration Interview Questions
Question 8. What Is Informatica Architecture?

Answer :

Informatica Architecture contains Repository, Repository server, Repository server administration console, sources, repository server and Data warehousing and it have the Designer, Work for manager, work for monitor combination of all these are called Informatica Architecture.

Question 9. What Is Data Warehouse Architecture?

Answer :

Data warehousing is the repository of integrated information data will be extracted from the heterogeneous sources. Data warehousing architecture contains the different; sources like oracle, flat files and ERP then after it have the staging area and Data warehousing, after that it has the different Data marts then it have the reports and it also have the ODS - Operation Data Store. This complete architecture is called the Data warehousing Architecture.

Hadoop Interview Questions
Question 10. What Is Data Analysis? Where It Will Be Used?

Answer :

Data analysis: consider that you are running a business and u store the data of that; in some form say in register or in a comp and at the year end you want know the profit or loss then it called data analysis .Data analysis use: then u want to know which product was sold the highest and if the business is running in a loss then finding, where we went wrong we do analysis.

Networking Tutorial
Question 11. What Are Data Modeling And Data Mining? Where It Will Be Used?

Answer :

Data modeling is the process of designing a data base model. In this data model data will be stored in two types of table fact table and dimension table.

Fact table contains the transaction data and dimension table contains the master data. Data mining is process of finding the hidden trends is called the data mining.

MYSQL DBA Interview Questions
Question 12. What Is "method/1"?

Answer :

Method 1 is system develop lifecycle create by Arthur Anderson a while back.

Informatica Interview Questions
Question 13. After The Generation Of A Report To Whom We Have To Deploy Or What We Do After The Completion Of A Report?

Answer :

The generated report will be sent to the concerned business users through web or LAN.

Hadoop Tutorial
Question 14. After The Complete Generation Of A Report Who Will Test The Report And Who Will Analyze It?

Answer :

After the completion of reporting, reports will be sent to business analysts. They will analyze the data from different points of view so that they can make a proper business decisions.

Question 15. Can You Pass Sql Queries In Filter Transformation?

Answer :

We cannot use sql queries in filter transformation. It will not allow you to override default sql query like other transformations (Source Qualifier, lookup)

Data modeling Interview Questions
Question 16. Where The Data Cube Technology Is Used?

Answer :

A multi-dimensional structure called the data cube. A data abstraction allows one to view aggregated data from a number of perspectives. Conceptually, the cube consists of a core or base cuboids, surrounded by a collection of sub-cubes/cuboids that represent the aggregation of the base cuboids along one or more dimensions. We refer to the dimension to be aggregated as the measure attribute, while the remaining dimensions are known as the feature attributes.

Apache Flume Tutorial
Question 17. How Can You Implement Many Relations In Star Schema Model?

Answer :

Many-many relations can be implemented by using snowflake schema .With a max of n dimensions.

Hadoop Administration Interview Questions
Question 18. What Is Critical Column?

Answer :

Let us take one ex: Suppose 'XYZ' is customer in Bangalore, he was residing in the city from the last 5 years, in the period of 5 years he has made purchases worth of 3 lacs. Now, he moved to 'HYD'. When you update the 'XYZ' city to 'HYD' in your Warehouse, all the purchases by him will show in city 'HYD' only. This makes warehouse inconsistent. Here CITY is the Critical Column. Solution is use Surrogate Key.

Networking Interview Questions
Question 19. What Is The Main Difference Between Star And Snowflake Star Schema? Which One Is Better And Why?

Answer :

If u have one to may relation ship in the data then only we choose snowflake schema, as per the performance-wise every-one go for the Star schema. Moreover, if the ETL is concerned with reporting means choose for snowflake because this schema provides more browsing capability than the former schema.

Question 20. What Is The Difference Between Dependent Data Warehouse And Independent Data Warehouse?

Answer :

Dependent departments are those, which depend on a data ware to for their data.Independent department are those, which get their data directly from the operational data sources in the organization.

Apache Flume Interview Questions
Question 21. Which Technology Should Be Used For Interactive Data Querying Across Multiple Dimensions For A Decision Making For A Dw?

Answer :

MOLAP

Question 22. What Is Virtual Data Warehousing?

Answer :

A virtual or point-to-point data warehousing strategy means that end-users are allowed to get at operational databases directly using whatever tools are enabled to the "data access network".

Question 23. What Is The Difference Between Metadata And Data Dictionary?

Answer :

Meta data is nothing but information about data. It contains the information (i.e. data) about the graphs, its related files, abinitio commands, server information etc i.e. all kinds of information about project related information etc.

Informatica Admin Interview Questions
Question 24. What Is The Difference Between Mapping Parameter & Mapping Variable In Data Warehousing?

Answer :

Mapping Parameter defines the constant value and it cannot change the value throughout the session. Mapping Variables defines the value and it can be change throughout the session.

System Administration Interview Questions
Question 25. Explain The Advantages Of Raid 1, 1/0, And 5. What Type Of Raid Setup Would You Put Your Tx Logs.

Answer :

The basic advantage of RAID is to speed up the data reading from permanent storage device (hard disk).

Question 26. What Are The Characteristics Of Data Files?

Answer :

A data file can be associated with only one database. Once created a data file can't change size. One or more data files form a logical unit of database storage called a table space.

Question 27. What Is Rollback Segment?

Answer :

A Database contains one or more Rollback Segments to temporarily store "undo" information.

Hadoop Interview Questions
Question 28. What Is A Table Space?

Answer :

A database is divided into Logical Storage Unit called table spaces. A table space is used to grouped related logical structures together.

Question 29. What Is Database Link?

Answer :

A database link is a named object that describes a "path" from one database to another.

Question 30. What Is A Private Synonyms?

Answer :

A Private Synonyms can be accessed only by the owner.

Question 31. What Is A Hash Cluster?

Answer :

A row is stored in a hash cluster based on the result of applying a hash function to the row's cluster key value. All rows with the same hash key value are stores together on disk.

Question 32. Describe Referential Integrity?

Answer :

A rule defined on a column (or set of columns) in one table that allows the insert or update of a row only if the value for the column or set of columns (the dependent value) matches a value in a column of a related table (the referenced value). It also specifies the type of data manipulation allowed on referenced data and the action to be performed on dependent data as a result of any action on referenced data.

Question 33. What Is Schema?

Answer :

A schema is collection of database objects of a User.

MYSQL DBA Interview Questions
Question 34. What Is Table?

Answer :

A table is the basic unit of data storage in an ORACLE database. The tables of a database hold all of the user accessible data. Table data is stored in rows and columns.

Question 35. What Is A View?

Answer :

A view is a virtual table. Every view has a Query attached to it. (The Query is a SELECT statement that identifies the columns and rows of the table(s) the view uses.)

Question 36. What Is An Extent?

Answer :

An Extent is a specific number of contiguous data blocks, obtained in a single allocation, and used to store a specific type of information.

Data modeling Interview Questions
Question 37. What Is An Index?

Answer :

An Index is an optional structure associated with a table to have direct access to rows, which can be created to increase the performance of data retrieval. Index can be created on one or more columns of a table.

Question 38. What Is An Integrity Constrains?

Answer :

An integrity constraint is a declarative way to define a business rule for a column of a table.

Question 39. What Are Clusters?

Answer :

Clusters are groups of one or more tables physically stores together to share common columns and are often used together.

Question 40. What Are The Different Types Of Segments?

Answer :

Data Segment,
Index Segment,
Rollback Segment
and
Temporary Segment.

Hadoop Administration Interview Questions
Question 41. Explain The Relationship Among Database, Table Space And Data File?

Answer :

Each databases logically divided into one or more table spaces one or more data files are explicitly created for each table space.

Question 42. What Is An Index Segment?

Answer :

Each Index has an Index segment that stores all of its data.

Apache Flume Interview Questions
Question 43. What Is A Redo Log?

Answer :

The set of Redo Log files YSDATE, UID, USER or USERENV SQL functions, or the pseudo columns LEVEL or ROWNUM.

Question 44. What Are The Types Of Synonyms?

Answer :

There are two types of Synonyms Private and Public.

Question 45. What Are The Referential Actions Supported By Foreign Key Integrity Constraint?

Answer :

Update And Delete Restrict - A referential integrity rule that disallows the update or deletion of referenced data. DELETE Cascade - When a referenced row is deleted all associated dependent rows are deleted.

Question 46. Do You View Contain Data?

Answer :

Views do not contain or store data.

Question 47. What Is The Use Of Control File?

Answer :

When an instance of an ORACLE database is started, its control file is used to identify the database and redo log files that must be opened for database operation to proceed. It is also used in database recovery.

Question 48. Can Objects Of The Same Schema Reside In Different Table Spaces?

Answer :

Yes

Question 49. Can A Table Space Hold Objects From Different Schemes?

Answer :

Yes

Question 50. Can A View Based On Another View?

Answer :

Yes

Question 51. What Is A Full Backup?

Answer :

A full backup is an operating system backup of all data files, on- line redo log files and control file that constitute ORACLE database and the parameter.

Question 52. What Is Mirrored On-line Redo Log?

Answer :

A mirrored on-line redo log consists of copies of on-line redo log files physically located on separate disks; changes made to one member of the group are made to all members.

Question 53. What Is Partial Backup?

Answer :

A Partial Backup is any operating system backup short of a full backup, taken while the database is open or shut down.

Question 54. What Is Restricted Mode Of Instance Startup?

Answer :

An instance can be started in (or later altered to be in) restricted mode so that when the database is open connections are limited only to those whose user accounts have been granted the RESTRICTED SESSION system privilege.

Question 55. What Is Archived Redo Log?

Answer :

Archived Redo Log consists of Redo Log files that have archived before being reused.

Question 56. What Are The Steps Involved In Database Shutdown?

Answer :

Close the Database; Dismount the Database and Shutdown the Instance.

Question 57. What Are The Advantages Of Operating A Database In Archivelog Mode Over Operating It In No Archivelog Mode?

Answer :

Complete database recovery from disk failure is possible only in ARCHIVELOG mode. Online database backup is possible only in ARCHIVELOG mode.

Question 58. What Are The Different Modes Of Mounting A Database With The Parallel Server?

Answer :

Exclusive Mode If the first instance that mounts a database does so in exclusive mode, only that Instance can mount the database. Parallel Mode If the first instance that mounts a database is started in parallel mode, other instances that are started in parallel mode can also mount the database.

Question 59. Can Full Backup Be Performed When The Database Is Open?

Answer :

No

Question 60. What Are The Steps Involved In Instance Recovery?

Answer :

Rolling forward to recover data that has not been recorded in data files yet has been recorded in the on-line redo log, including the contents of rollback segments. Rolling back transactions that have been explicitly rolled back or have not been committed as indicated by the rollback segments regenerated in step a.

1) Releasing any resources (locks) held by transactions in process at the time of the failure.
2) Resolving any pending distributed transactions undergoing a two-phase commit at the time of the instance failure.

Question 61. What Are The Steps Involved In Database Startup?

Answer :

Start an instance, Mount the Database and Open the Database.

Question 62. Which Parameter Specified In The Default Storage Clause Of Create Tablespace Cannot Be Altered After Creating The Table Space?

Answer :

All the default storage parameters defined for the table space can be changed using the ALTER TABLESPACE command. When objects are created their INITIAL and MINEXTENS values cannot be changed.

Question 63. What Is On-line Redo Log?

Answer :

The On-line Redo Log is a set of tow or more on-line redo files that record all committed changes made to the database. Whenever a transaction is committed, the corresponding redo entries temporarily stores in redo log buffers of the SGA are written to an on-line redo log file by the background process LGWR. The on-line redo log files are used in cyclical fashion.

Question 64. What Is Log Switch?

Answer :

The point at which ORACLE ends writing to one online redo log file and begins writing to another is called a log switch.

Question 65. What Is Dimensional Modelling?

Answer :

Dimensional Modelling is a design concept used by many data warehouse designers to build their data warehouse. In this design model all the data is stored in two types of tables - Facts table and Dimension table. Fact table contains the facts/measurements of the business and the dimension table contains the context of measurements i.e., the dimensions on which the facts are calculated.

Question 66. What Are The Difference Between Snow Flake And Star Schema? What Are Situations Where Snow Flake Schema Is Better Than Star Schema To Use And When The Opposite Is True?

Answer :

Star schema contains the dimension tables mapped around one or more fact tables. It is a renormalized model and no need to use complicated joins. Also queries results fast.Snowflake schema: It is the normalized form of Star schema. It contains in-depth joins, because the tables are split in to many pieces. We can easily do modification directly in the tables. We have to use complicated joins, since we have more tables.There will be some delay in processing the query.

Question 67. What Is A Cube In Data Warehousing Concept?

Answer :

Cubes are logical representation of multidimensional data. The edge of the cube contains dimension members and the body of the cube contains data values.

Question 68. What Are The Differences Between Star And Snowflake Schema?

Answer :

Star schema: A single fact table with N number of DimensionSnowflake schema: Any dimensions with extended dimensions are known as snowflake schema.

Question 69. What Are Data Marts?

Answer :

A data mart is a collection of tables focused on specific business group/department. It may have multi-dimensional or normalized. Data marts are usually built from a bigger data warehouse or from operational data.

Question 70. What Is The Data Type Of The Surrogate Key?

Answer :

There is no data type for a Surrogate Key. Requirement of a surrogate Key: UNIQUE Recommended data type of a Surrogate key is NUMERIC.

Question 71. What Are Fact, Dimension, And Measure?

Answer :

Fact is key performance indicator to analyze the business. Dimension is used to analyze the fact. Without dimension there is no meaning for fact.

Question 72. What Are The Different Types Of Data Warehousing?

Answer :

Types of data warehousing are:

1. Enterprise Data warehousing
2. ODS (Operational Data Store)
3. Data Mart

Question 73. What Do You Mean By Static And Local Variable?

Answer :

Static variable is not created on function stack but is created in the initialized data segment and hence the variable can be shared across the multiple call of the same function. Usage of static variables within a function is not thread safe.On the other hand, local variable or auto variable is created on function stack and valid only in the context of the function call and is not shared across function calls.

Question 74. What Is A Source Qualifier?

Answer :

When you add a relational or a flat file source definition to a mapping, you need to connect it to a Source Qualifier transformation. The Source Qualifier represents the rows that the Informatica Server reads when it executes a session.

Question 75. What Are The Steps To Build The Data Warehouse?

Answer :

Gathering business requirements>>Identifying Sources>>Identifying Facts>>Defining Dimensions>>Define Attributes>>Redefine Dimensions / Attributes>>Organize Attribute Hierarchy>>Define Relationship>>Assign Unique Identifiers.

Question 76. What Is The Advantages Data Mining Over Traditional Approaches?

Answer :

Data Mining is used for the estimation of future. For example, if we take a company/business organization, by using the concept of Data Mining, we can predict the future of business in terms of Revenue (or) Employees (or) Customers (or) Orders etc.Traditional approaches use simple algorithms for estimating the future. However, it does not give accurate results when compared to Data Mining.

Question 77. What Is The Difference Between View And Materialized View?

Answer :

View - store the SQL statement in the database and let you use it as a table. Every time you access the view, the SQL statement executes. Materialized view - stores the results of the SQL in table form in the database. SQL statement only executes once and after that every time you run the query, the stored result set is used. Pros include quick query results.

Question 78. What Is The Main Difference Between Inmon And Kimball Philosophies Of Data Warehousing?

Answer :

Both differed in the concept of building the data warehouse.According to Kimball, Kimball views data warehousing as a constituency of data marts. Data marts are focused on delivering business objectives for departments in the organization. And the data warehouse is a conformed dimension of the data marts. Hence, a unified view of the enterprise can be obtained from the dimension modeling on a local departmental level.Inmon beliefs in creating a data warehouse on a subject-by-subject area basis. Hence, the development of the data warehouse can start with data from the online store. Other subject areas can be added to the data warehouse as their needs arise. Point-of-sale (POS) data can be added later if management decides it is necessary.

Question 79. What Is Junk Dimension? What Is The Difference Between Junk Dimension And Degenerated Dimension?

Answer :

Junk dimension: Grouping of Random flags and text attributes in a dimension and moving them to a separate sub dimension. Degenerate Dimension: Keeping the control information on Fact table ex: Consider a Dimension table with fields like order number and order line number and have 1:1 relationship with Fact table, In this case this dimension is removed and the order information will be directly store.

Question 80. Why Fact Table Is In Normal Form?

Answer :

The fact table consists of the Index keys of the dimension/look up tables and the measures. So whenever we have the keys in a table. That it implies that the table is in the normal form.

Question 81. What Is Difference Between E-r Modeling And Dimensional Modeling?

Answer :

Basic difference is E-R modeling will have logical and physical model. Dimensional model will have only physical model. E-R modeling is used for normalizing the OLTP database design.Dimensional modeling is used for de-normalizing the ROLAP/MOLAP design.

Question 82. What Is Conformed Fact?

Answer :

Conformed dimensions are the dimensions, which can be used across multiple Data Marts in combination with multiple facts tables accordingly.

Question 83. What Are The Methodologies Of Data Warehousing?

Answer :

Every company has methodology of their own. However, to name a few SDLC Methodology, AIM methodology is standard used.

Question 84. What Is Bus Schema?

Answer :

BUS Schema is composed of a master suite of confirmed dimension and standardized definition if facts.

Question 85. What Is Data Warehousing Hierarchy?

Answer :

Hierarchies are logical structures that use ordered levels as a means of organizing data. A hierarchy can be used to define data aggregation. For example, in a time dimension, a hierarchy might aggregate data from the month level to the quarter level to the year level. A hierarchy can also be used to define a navigational drill path and to establish a family structure.Within a hierarchy, each level is logically connected to the levels above and below it. Data values at lower levels aggregate into the data values at higher levels. A dimension can be composed of more than one hierarchy. For example, in the product dimension, there might be two hierarchies--one for product categories and one for product suppliers.Dimension hierarchies also group levels from general to granular. Query tools use hierarchies to enable you to drill down into your data to view different levels of granularity. This is one of the key benefits of a data warehouse.When designing hierarchies, you must consider the relationships in business structures. Hierarchies impose a family structure on dimension values. For a particular level value, a value at the next higher level is its parent, and values at the next lower level are its children. These familial relationships enable analysts to access data quickly.

Question 86. What Are Data Validation Strategies For Data Mart Validation After Loading Process?

Answer :

Data validation is to make sure that the loaded data is accurate and meets the business requirements. Strategies are different methods followed to meet the validation requirements.

Question 87. What Are The Data Types Present In Bo? What Happens If We Implement View In The Designer N Report?

Answer :

Three different data types: Dimensions, Measure, and DetailView is nothing but an alias and it can be used to resolve the loops in the universe.

Question 88. What Is Surrogate Key? Where We Use It? Explain With Examples.

Answer :

Surrogate key is a substitution for the natural primary key.It is just a unique identifier or number for each row that can be used for the primary key to the table. The only requirement for a surrogate primary key is that it is unique for each row in the table.

Data warehouses typically use a surrogate, (also known as artificial or identity key), key for the dimension tables primary keys. They can use Info sequence generator, or Oracle sequence, or SQL Server Identity values for the surrogate key.

It is useful because the natural primary key (i.e. Customer Number in Customer table) can change and this makes updates more difficult.

Some tables have columns such as AIRPORT_NAME OR CITY_NAME which are stated as the primary keys (according to the business users) but ,not only can these change, indexing on a numerical value is probably better and you could consider creating a surrogate key called, say, AIRPORT_ID. This would be internal to the system and as far as the client is concerned, you may display only the AIRPORT_NAME.

Question 89. What Is A Linked Cube?

Answer :

Linked cube in which a sub-set of the data can be analyzed into detail. The linking ensures that the data in the cubes remain consistent.

Question 90. What Is Meant By Metadata In Context Of A Data Warehouse And How It Is Important?

Answer :

Metadata is the data about data; Business Analyst or data modeler usually capture information about data - the source (where and how the data is originated), nature of data (char, varchar, nullable, existence, valid values etc) and behavior of data (how it is modified / derived and the life cycle) in data dictionary.

Metadata is also presented at the Datamart level, subsets, fact and dimensions, ODS etc. For a DW user, metadata provides vital information for analysis / DSS.

Question 91. What Are The Possible Data Marts In Retail Sales?

Answer :

Product information and sales information.

Question 92. What Are The Various Etl Tools In The Market?

Answer :

Various ETL tools used in market are Informatica Data Stage Oracle Warehouse Builder Ab Initio Data Junction.

Question 93. What Is Dimensional Modeling?

Answer :

Dimensional Modeling is a design concept used by many data warehouse designers to build their data warehouse. In this design model all the data is stored in two types of tables - Facts table and Dimension table. Fact table contains the facts/measurements of the business and the dimension table contains the context of measurements i.e., the dimensions on which the facts are calculated.Dimension modeling is a method for designing data warehouse. Three types of modeling are there

1. Conceptual modeling
2. Logical modeling
3. Physical modeling.

Question 94. What Is Vldb?

Answer :

The perception of what constitutes a VLDB continues to grow. A one-terabyte database would normally be considered VLDB.Degenerate dimension: it does not have any link with dimensions and it will not have any attribute.

Question 95. What Is Degenerate Dimension Table?

Answer :

Degenerate Dimensions: If a table contains the values, which r neither dimension nor measures is called degenerate dimensions. For example invoice id, employee no.A degenerate dimension is data that is dimensional in nature but stored in a fact table.

Question 96. What Is Er Diagram?

Answer :

The Entity-Relationship (ER) model was originally proposed by Peter in 1976 [Chen76] as a way to unify the network and relational database views. Simply stated the ER model is a conceptual data model that views the real world as entities and relationships. A basic component of the model is the Entity-Relationship diagram, which is used to visually represent data objects. Since Chen wrote his paper the model has been extended and today it is commonly used for database design for the database designer, the utility of the ER model is: it maps well to the relational model. The constructs used in the ER model can easily be transformed into relational tables. It is simple and easy to understand with a minimum of training. Therefore, the database designer to communicate the design to the end user can use the model. In addition, the model can be used as a design plan by the database developer to implement a data model in specific database management software.

Question 97. What Is The Difference Between Snowflake And Star Schema? What Are Situations Where Snowflake Schema Is Better Than Star Schema When The Opposite Is True?

Answer :

Star schema contains the dimension tables mapped around one or more fact tables.It is a renormalized model and no need to use complicated joins. Also Queries results fast.Snowflake schema is the normalized form of Star schema. It contains in-depth joins, because the tables are spited in to many pieces. We can easily do modification directly in the tables.We have to use complicated joins, since we have more tables. There will be some delay in processing the Query.

Question 98. What Is The Difference Between Star And Snowflake Schemas?

Answer :

Star schema:
A single fact table with N number of DimensionSnowflake schema: Any dimensions with extended dimensions are known as snowflake schema.

Question 99. Can A Dimension Table Contain Numeric Values?

Answer :

Yes. However, those data type will be char (only the values can numeric/char).Yes, dimensions even contain numerical because these are descriptive elements of our business.

Question 100. What Is Hybrid Slowly Changing Dimension?

Answer :

Hybrid SCDs are combination of both SCD 1 and SCD 2.It may happen that in a table, some columns are important and we need to track changes for them i.e. capture the historical data for them whereas in some columns even if the data changes, we don't care.For such tables we implement Hybrid SCDs, where in some columns are Type 1 and some are Type 2.You can add that it is not an intelligent key but similar to a sequence number and tied to a timestamp typically!

Question 101. How Many Clustered Indexes Can U Create For A Table In Dwh? In Case Of Truncate And Delete Command What Happens To Table, Which Has Unique Id.

Answer :

You can have only one clustered index per table. If you use delete command, you can rollback... it fills your redo log files.

If you do not want records, you may use truncate command, which will be faster and does not fill your redo log file.

Question 102. What Is Loop In Data Warehousing?

Answer :

In DWH loops may exist between the tables. If loops exist, then query generation will take more time, because more than one path is available. It creates ambiguity also. Loops can be avoided by creating aliases of the table or by context.

Example: 4 Tables - Customer, Product, Time, Cost forming a close loop. Create alias for the cost to avoid loop.

Question 103. What Is An Error Log Table In Informatica Occurs And How To Maintain It In Mapping?

Answer :

Error Log in Informatica is a one of output file created by Informatica Server while running the session for error messages. It is created in Informatica home directory.

Question 104. How Many Different Schemas Or Dw Models Can Be Used In Siebel Analytics. I Know Only Star And Snow Flake And Any Other Model That Can Be Used?

Answer :

Integrated schema design is also used to define an integrated schema design we have to define the following concepts

► Fact constellation
► Act less fact table
► Onformed dimension
A: A fact constellation is the process of joining two or more fact tables
B: A fact table with out any facts is known as fact less fact table
C:A dimension which is re useful and fixed is known as conformed dimensionA dimension, which is, shared with multiple fact tables known as conformed dimension.

Question 105. What Is Drilling Across?

Answer :

Drill across corresponds to switching from 1 classification in 1 dimension to a different classification in different dimension.

Question 106. How Can You Import Tables From A Database?

Answer :

In Business Objects Universe Designer you can open Table Browser and select the tables needed then insert them to designer.

Question 107. Where The Cache Files Stored?

Answer :

Caches are stored in Repository.

Question 108. What Is Dimension Modeling?

Answer :

A logical design technique that seeks to present the data in a standard, intuitive framework that allows for high-performance access. There are different data modeling concepts like ER Modeling (Entity Relationship modeling), DM (Dimensional modeling), Hierarchal Modeling, Network modeling. However, popular are ER and DM only.

Question 109. What Is Data Cleaning? How Can We Do That?

Answer :

Data cleaning is a self-explanatory term. Most of the data warehouses in the world source data from multiple systems - systems that were created long before data warehousing was well understood, and hence without the vision to consolidate the same in a single repository of information. In such a scenario, the possibilities of the following are there:

► Missing information for a column from one of the data sources;
► Inconsistent information among different data sources;
► Orphan records;
► Outlier data points;
► Different data types for the same information among various data sources, leading to improper conversion;
► Data breaching business rules

In order to ensure that the data warehouse is not infected by any of these discrepancies, it is important to cleanse the data using a set of business rules, before it makes its way into the data warehouse.

Question 110. Can Any One Explain The Hierarchies Level Data Warehousing.

Answer :

In Data warehousing, levels are columns available in dimension table. Levels are having attributes. Hierarchies are used for navigational purpose; there are two types of Hierarchies. You can define hierarchies in top down or bottom up.

1. Natural Hierarchy: Best example is Time Dimension - Year, Month, Day etc. In natural Hierarchy definite relationship exists between each level
2. Navigational Hierarchy: You can have levels like
   Ex - Production cost of Product, Sales Cost of Product.
   Ex - Lead Time defined to procure, Actual Procurement time,
   In this, two levels need not to have relationship. This Hierarchy is created for navigational purpose.

Question 111. Can Any One Explain About Core Dimension, Balanced Dimension, And Dirty Dimension?

Answer :

Dirty Dimension is nothing but Junk Dimensions. Core Dimensions are dedicated for a fact table or Data mart. Conformed Dimensions are used across fact tables or Data marts.

Question 112. How Much Data Hold In One Universe.

Answer :

Universe does not hold any data. However, practically the universe is known to have issues when the objects cross 6000.

Question 113. What Is Core Dimension?

Answer :

Core Dimension is a Dimension table, which is used dedicated for single fact table or Datamart. Conform Dimension is a Dimension table which is used across fact tables or Data marts.

Question 114. After We Create A Scd Table, Can We Use That Particular Dimension As A Dimension Table For Star Schema?

Answer :

Yes.

Question 115. Suppose You Are Filtering The Rows Using A Filter Transformation Only The Rows Meet The Condition Pass To The Target. Tell Me Where The Rows Will Go That Does Not Meet The Condition.

Answer :

Informatica filter transformation default value is 1 i.e. true. If you place a break point on filter transformation and run the mapping in a debugger mode, you will find these values 1 or 0 for each row passing through filter. If you change 0 to 1, the particular row will be passed to next stage.

Question 116. What Is Galaxy Schema?

Answer :

Galaxy schema is also known as fact constellation scheme. It requires no of fact tables to share dimension tables. In data, wares housing mainly the people are using the conceptual hierarchy.

Question 117. Briefly State Different Between Data Ware House & Data Mart?

Answer :

Data warehouse is made up of many datamarts. DWH contain many subject areas. However, data mart focuses on one subject area generally. E.g. If there will be DHW of bank then there can be one data mart for accounts, one for Loans etc. This is high-level definitions.

Question 118. What Is Meta Data?

Answer :

Metadata is data about data. E.g. if in data mart we are receiving any file. Then metadata will contain information like how many columns, file is fix width/limited, ordering of fields, data types of field etc.

Question 119. What Is Data Mart?

Answer :

Data Marts is used on a business division/department level. A data mart only contains the required subject specific data for local analysis. A database, or collection of databases, designed to help managers make strategicdecisions about their business. data marts are usually smaller and focus on a particular subject or department. Some data marts, called dependent data marts, are subsets of larger data warehouses. A data mart is a simpler form of a data warehouse focused on a single subject (or functional area) such as sales, finance, marketing, HR etc. Data Mart represents data from single business process.

Question 120. What Is The Definitions For Datawarehose And Datamart?

Answer :

Datamart is subset of Datawarehouse we can say a datamart is collection of individual departmental information...Where as datawarehouse in collection of datamart.

Data mart is a single subject and datawarehouse is a integration of multiple subjects.

Question 121. What Are Data Marts

Answer :

Data Mart is a segment of a data warehouse that can provide data for reporting and analysis on a section, unit, department or operation in the company, e.g. sales, payroll, production. Data marts are sometimes complete individual data warehouses which are usually smaller than the corporate data warehouse.

Question 122. What Is The Difference Between A Data Warehouse And A Data Mart?

Answer :

A data mart is a subject oriented database which supports the business needs of individual departments within the enterprise.It is an subset of the enterprise data warehouse.It is also known as high performance query structures.

Question 123. What Is Data Validation Strategies For Data Mart Validation After Loading Process

Answer :

Data validation is generally done manually in DWH in this case if source and TGT are relational you need to create SQL scripts to validate source and target data and if source isFlat file or non relational database you can use excel if data is very less or create dummy tables to validate your ETL code.

Question 124. What Is Data Mining?

Answer :

Data Mining is the process of analyzing data from different perspectives and summarizing it into useful information.

Question 125. What Is Ods?

Answer :

ODS is abbreviation of Operational Data Store. A database structure that is a repository for near real-time operational data rather than long term trend data. The ODS may further become the enterprise shared operational database, allowing operational systems that are being re-engineered to use the ODS as there operation databases.

Question 126. What Is Etl?

Answer :

ETL is abbreviation of extract, transform, and load. ETL is software that enables businesses to consolidate their disparate data while moving it from place to place, and it doesn’t really matter that that data is in different forms or formats. The data can come from any source.ETL is powerful enough to handle such data disparities. First, the extract function reads data from a specified source database and extracts a desired subset of data. Next, the transform function works with the acquired data – using rules orlookup tables, or creating combinations with other data – to convert it to the desired state. Finally, the load function is used to write the resulting data to a target database.

Question 127. Is Oltp Database Is Design Optimal For Data Warehouse?

Answer :

No. OLTP database tables are normalized and it will add additional time to queries to return results. Additionally OLTP database is smaller and it does not contain longer period (many years) data, which needs to be analyzed. A OLTP system is basically ER model and not Dimensional Model. If a complex query is executed on a OLTP system, it may cause a heavy overhead on the OLTP server that will affect the normal business processes.

Question 128. If De-normalized Is Improves Data Warehouse Processes, Why Fact Table Is In Normal Form?

Answer :

Foreign keys of facts tables are primary keys of Dimension tables. It is clear that fact table contains columns which are primary key to other table that itself make normal form table.

Question 129. What Are Lookup Tables?

Answer :

A lookup table is the table placed on the target table based upon the primary key of the target, it just updates the table by allowing only modified (new or updated) records based on thelookup condition.

Question 130. What Are Aggregate Tables?

Answer :

Aggregate table contains the summary of existing warehouse data which is grouped to certain levels of dimensions. It is always easy to retrieve data from aggregated tables than visiting original table which has million records. Aggregate tables reduces the load in the database server and increases the performance of the query and can retrieve the result quickly.

Question 131. What Is Real Time Data-warehousing?

Answer :

Data warehousing captures business activity data. Real-time data warehousing captures business activity data as it occurs. As soon as the business activity is complete and there is data about it, the completed activity data flows into the data warehouse and becomes available instantly.

Question 132. What Are Conformed Dimensions?

Answer :

Conformed dimensions mean the exact same thing with every possible fact table to which they are joined. They are common to the cubes.

Question 133. How Do You Load The Time Dimension?

Answer :

Time dimensions are usually loaded by a program that loops through all possible dates that may appear in the data. 100 years may be represented in a time dimension, with one row per day.

Question 134. What Is A Level Of Granularity Of A Fact Table?

Answer :

Level of granularity means level of detail that you put into the fact table in a data warehouse. Level of granularity would mean what detail are you willing to put for each transactional fact.

Question 135. What Are Non-additive Facts?

Answer :

Non-additive facts are facts that cannot be summed up for any of the dimensions present in the fact table. However they are not considered as useless. If there is changes in dimensions the same facts can be useful.

Question 136. What Is Factless Facts Table?

Answer :

A fact table which does not contain numeric fact columns it is called factless facts table.

Question 137. Explain About Olap ?

Answer :

OLAP is known as online analytical processing which provides answers to queries which are multi dimensional in nature. It composes relational reporting and data mining for providing solutions to business intelligence. This term OLAP is created from the term OLTP.

Question 138. Explain About The Functionality Of Olap?

Answer :

Hyper cube or multidimensional cube forms the core of OLAP system. This consists of measures which are arranged according to dimensions. Hyper cube Meta data is created by star or snow flake schema of tables in RDBMS. Dimensions are extracted from dimension table and measures from the fact table.

Question 139. Explain About Molap?

Answer :

Classic form of OLAP is known as MOLAP and it is often called as OLAP. Simple database structures such as time period, product, location, etc are used. Functioning of each and every dimension or data structure is defined by one or more hierarchies.

Question 140. Explain About Rolap?

Answer :

Functioning of ROLAP occurs simultaneously with relational databases. Data and tables are stored as relational tables. To hold new information or data new tables are created. Functioning of ROLAP depends upon specialized schema design.

Question 141. Explain About Aggregations?

Answer :

OLAP can process complex queries and give the output in less than 0.1 seconds, for it to achieve such a performance OLAP uses aggregations. Aggregations are built by aggregating and changing the data along the dimensions. Possible combination of aggregations can be determined by the combination possibilities of dimension granularities.

Question 142. Explain About The View Selection Problem?

Answer :

Often calculating all the data is not possible by aggregations for this reason some of the complex data problems are solved. In order to determine which data should be solved and calculated, developers use View selection application. This solution is often used to reduce calculation problem.

Question 143. Explain About The Role Of Bitmap Indexes To Solve Aggregation Problems?

Answer :

Bitmaps are very useful in start schema to join large databases to small databases. Answer queries and bit arrays are used to perform logical operations on the databases. Bit map indexes are very efficient in handling Gender differentiation; also repetitive tasks are performed with much larger efficiency.

Question 144. Explain About Encoding Technique Used In Bitmaps Indexes?

Answer :

Bitmaps commonly use one bitmap for every single distinct value. Number of bitmaps used can be reduced by opting for a different type of encoding. Space can be optimized but when a query is generated bitmaps have to be accessed.

Question 145. Explain About Binning?

Answer :

Binning process is very useful to save space. Performance may vary depending upon the query generated sometimes solution to a query can come within few seconds and sometimes it may take longer time. Binning process holds multiple values in the same bin.

Question 146. Explain About Candidate Check?

Answer :

The process which is underlined during the check of base data is known as candidate check. When performing candidate check performance varies either towards the positive side or to the negative side. Performance of candidate check depends upon the user query and also they examine the base data.

Question 147. Explain About Hybrid Olap?

Answer :

When a database developer uses Hybrid OLAP it divides the data between relational and specialized storage. In some particular modifications a HOLAP database may store huge amounts of data in its relational tables. Specialized data storage is used to store data which is less detailed and more aggregate.

Question 148. Explain About Api`s Of Olap?

Answer :

Microsoft in the late 1997 introduced a standard API known as OLE DB. After which XML was used for analysis specification and this specification was largely used by many vendors throughout the world as a standard specification. MDX is the standards specification for OLAP.

Question 149. Explain About Shared Features Of Olap?

Answer :

Shared implements most of the security features into OLAP. If multiple accesses are required admin can make necessary changes. The default security level for all OLAP products is read only. For multiple updates it is predominant to make necessary security changes.

Question 150. Explain About Analysis?

Answer :

Analysis defines about the logical and statistical analysis required for an efficient output. This involves writing of code and performing calculations, but most part of these languages does not require complex programming language knowledge. There are many specific features which are included such as time analysis, currency translation, etc.

Question 151. Explain About Multidimensional Features Present In Olap?

Answer :

Multidimensional support is very essential if we are to include multiple hierarchies in our data analysis. Multidimensional feature allows a user to analyze business and organization. OLAP efficiently handles support for multidimensional features.

Question 152. Explain About The Database Marketing Application Of Olap?

Answer :

Database marketing tool or application helps a user or marketing professional in determining the right tool or strategy for his valuable add campaign. This tool collects data from all sources and gives relevant information the specialist with their add campaign. It gives a complete picture to the developer.

Question 153. What Are The Different Industries Which Use This Marketing Tool?

Answer :

Many different companies can use this tool for developing their business strategy but it is often three major industries which use this tool more. Those three industries are Consumer goods industries, Retail industries, and financial services industry. These industry`s have huge amount of data in their disposal which makes then to use these tools to determine their exact customer.

Question 154. Compare Data Warehouse Database And Oltp Database

Answer :

The data warehouse and the OLTP data base are bothrelational databases. However, the objectives of both these databases are different.

The OLTP database records transactions in real time and aims to automate clerical data entry processes of a business entity. Addition, modification and deletion of data in the OLTP database is essential and the semantics of the applicationused in the front end impact on the organization of the data in the database.

The data warehouse on the other hand does not cater to real time operational requirements of the enterprise. It is more a storehouse of current and historical data and may alsocontain data extracted from external data sources.

Question 155. What Is The Difference Between Etl Tool And Olap Tool? What Are Various Etl In The Market? What Are Various Olap Tools? What Is The Future For Both For Next Five Years?

Answer :

ETL is a extraction,transformation,loading tool i.e u can extract , u can transform using different transformations available in tool and aggreagte the data. The output of thisETL tool is used as input to OLAP tool.

OLAP is online analytical process, where u can get online reports after doing some joines,creating some cubes

ETL tools in market
1 INFORMATICA-- univeral tool ,good market
2 ABINITO -- fastest loading tool,very good market
3 DATASTAGE-- difficult work, no good market
4 BODI-- good market
5 ORACLE WAREHOUSE BUILDER-- good market.

Question 156. How To Enable Security In Cognos Connection In Cognos Report Net

Answer :

You can imlement security via your Windows NT system accounts, LDAP accounts for Cognos connection. To do thisconfigure the desired Security section in the Cognos Configuration.

Question 157. Compare Data Warehouse Database And Oltp Database.

Answer :

Data Warehouse is used for business measures cannot be used to cater real time business needs of the organizationand is optimized for lot of data, unpredictable queries. On the other hand, OLTP database is for real time business operations that are used for a common set of transactions. Data warehouse does not require any validation of data. OLTP database requires validation of data.

Question 158. What Does Level Of Granularity Of A Fact Table Signify?

Answer :

In simple terms, level of granularity defines the extent of detail. As an example, let us look at geographical level of granularity. We may analyze data at the levels of COUNTRY, REGION, TERRITORY, CITY and STREET. In this case, we say the highest level of granularity is STREET.

Question 159. Differences Between Star And Snowflake Schemas ?

Answer :

The star schema is created when all the dimension tables directly link to the fact table. Since the graphical representation resembles a star it is called a star schema. It must be noted that the foreign keys in the fact table link to the primary key of the dimension table. This sample provides the star schema for a sales_ fact for the year 1998. The dimensions created are Store, Customer, Product_class and time_by_day. The Product table links to the product_class table through the primary key and indirectly to the fact table. The fact table contains foreign keys that link to the dimension tables.

Question 160. What Is Fact Table?

Answer :

Fact Table contains the measurements or metrics or facts of business process. If your business process is "Sales" , then a measurement of this business process such as "monthly sales number" is captured in the Fact table. Fact table also contains the foriegn keys for the dimension tables.

Question 161. What Is A Data Warehouse?

Answer :

Data Warehouse is a repository of integrated information, available for queries and analysis. Data and information are extracted from heterogeneous sources as they are generated….This makes it much easier and more efficient to run queries over data that originally came from different sources. Typical relational databases are designed for on-line transactional processing (OLTP) and do not meet the requirements for effective on-line analytical processing (OLAP). As a result, data warehouses are designed differently than traditional relational databases.

Question 162. Steps In Building The Data Model

Answer :

While ER model lists and defines the constructs required to build a data model, there is no standard process for doing so. Some methodologies, such as IDEFIX, specify a bottom-up.

Question 163. Why Is Data Modeling Important?

Answer :

Data modeling is probably the most labor intensive and time consuming part of the development process. Why bother especially if you are pressed for time? A common.

Question 164. What Type Of Indexing Mechanism Do We Need To Use For A Typical Datawarehouse?

Answer :

On the fact table it is best to use bitmap indexes. Dimension tables can use bitmap and/or the other types of clustered/non-clustered, unique/non-unique indexes.

To my knowledge, SQLServer does not support bitmap indexes. Only Oracle supports bitmaps.

Question 165. What Are Semi-additive And Factless Facts And In Which Scenario Will You Use Such Kinds Of Fact Tables?

Answer :

Semi-Additive: Semi-additive facts are facts that can be summed up for some of the dimensions in the fact table, but not the others. For example:

Current_Balance and Profit_Margin are the facts. Current_Balance is a semi-additive fact, as it makes sense to add them up for all accounts (what's the total current balance for all accounts in the bank?), but it does not make sense to add them up through time (adding up all current balances for a given account for each day of the month does not give us any useful information A factless fact table captures the many-to-many relationships between dimensions, but contains no numeric or textual facts. They are often used to record events or coverage information.

Common examples of factless fact tables include:

- Identifying product promotion events (to determine promoted products that didn?t sell)
- Tracking student attendance or registration events
- Tracking insurance-related accident events
- Identifying building, facility, and equipment schedules for a hospital or university.

Question 166. Is It Correct/feasible Develop A Data Mart Using An Ods?

Answer :

Yes it is correct to develop a Data Mart using an ODS.becoz ODS which is used to?store transaction data and few Days (less historical data) this is what datamart is required so it is coct to develop datamart using ODS .

Question 167. Explain Degenerated Dimension.

Answer :

A Degenerate dimension?is a?Dimension which has only a single attribute.

This dimension is typically represented as a single field in a fact table.

The data items thar are not facts and data items that do not fit into the existing dimensions are

termed as Degenerate Dimensions.
Degenerate Dimensions are the fastest way to group similar transactions.
Degenerate Dimensions are used when fact tables represent transactional data.
They can be used as primary key for the fact table but they cannot act as foreign keys.

Question 168. What Are The Different Methods Of Loading Dimension Tables?

Answer :

Conventional Load:
Before loading the data, all the Table constraints will be checked against the data.
Direct load:(Faster Loading)
All the Constraints will be disabled. Data will be loaded directly.Later the data will be checked against the table constraints and the bad data won't be indexed.

Question 169. What Are Slowly Changing Dimensions?

Answer :

Dimensions that change over time are called Slowly Changing Dimensions. For instance, a product price changes over time; People change their names for some reason; Country and State names may change over time. These are a few examples of Slowly Changing Dimensions since some changes are happening to them over a period of time.

If the data in the Dimension table happen to change very rarely,then it is called as slowly changing dimension.

ex: changing the name and address of a person,which happens rerely.

Question 170. What Are The Various Reporting Tools In The Market?

Answer :

1. MS-Excel
2. Business Objects (Crystal Reports)
3. Cognos (Impromptu, Power Play)
4. Microstrategy
5. MS reporting services
6. Informatica Power Analyzer
7. Actuate
8. Hyperion (BRIO)
9. Oracle Express OLAP
10. Proclarity.

Question 171. What Are The Data Types Present In Bo?n What Happens If We Implement View In The Designer N Report

Answer :

my knowlegde, these are?called as object types in the Business Objects.And alias is different from view in the universe. View is at database level, but alias?is a different name given for the same table to resolve the loops in universe.

Question 172. What Is Meant By Metadata In Context Of A Datawarehouse And How It Is Important?

Answer :

Metadata or Meta Data Metadata is data about data. Examples of metadata include data element descriptions, data type descriptions, attribute/property descriptions, range/domain descriptions, and process/method descriptions. The repository environment encompasses all corporate metadata resources: database catalogs, data dictionaries, and navigation services. Metadata includes things like the name, length, valid values, and description of a data element. Metadata is stored in a data dictionary and repository. It insulates the data warehouse from changes in the schema of operational systems. Metadata Synchronization The process of consolidating, relating and synchronizing data elements with the same or similar meaning from different systems. Metadata synchronization joins these differing elements together in the data warehouse to allow for easier access.

Question 173. What Are Modeling Tools Available In The Market

Answer :

These tools are used for Data/dimension modeling
Oracle Designer
ERWin (Entity Relationship for windows)
Informatica (Cubes/Dimensions)
Embarcadero
Power Designer Sybase.

Question 174. What Is The Main Differnce Between Schema In Rdbms And Schemas In Datawarehouse?

Answer :

RDBMS Schema
* Used for OLTP systems
* Traditional and old schema
* Normalized
* Difficult to understand and navigate
* Cannot solve extract and complex problems
* Poorly modelled
  DWH Schema
* Used for OLAP systems
* New generation schema
* De Normalized
* Easy to understand and navigate
* Extract and complex problems can be easily solved
* Very good model.

Question 175. What Is A General Purpose Scheduling Tool?

Answer :

The basic purpose of the scheduling tool in a DW Application is to stream line the flow of data from Source To Target at specific time or based on some condition.

Question 176. What Is The Need Of Surrogate Key;why Primary Key Not Used As Surrogate Key?

Answer :

Surrogate Key is an artificial identifier for an entity. In surrogate key values are generated by the system sequentially(Like Identity property in SQL Server and Sequence in Oracle). They do not describe anything. Primary Key is a natural identifier for an entity. In Primary keys all the values are entered manually by the user which are uniquely identified. There will be no repetition of data.

Question 177. Need For Surrogate Key Not Primary Key

Answer :

If a column is made a primary key and later there needs a change in the data type or the length for that column then all the foreign keys that are dependent on that primary key should be changed making the database Unstable . Surrogate Keys make the database more stable because it insulates the Primary and foreign key relationships from changes in the data types and length.

Question 178. What Is Snow Flake Schema?

Answer :

Snowflake schemas normalize dimensions to eliminate redundancy. That is, the dimension data has been grouped into multiple tables instead of one large table. For example, a product dimension table in a star schema might be normalized into a products table, a product_category table, and a product_manufacturer table in a snowflake schema. While this saves space, it increases the number of dimension tables and requires more foreign key joins. The result is more complex queries and reduced query performance.

Question 179. What Is The Difference Between Oltp And Olap?

Answer :

OLTP is nothing but OnLine Transaction Processing ,which contains a normalised tables and online data,which have frequent insert/updates/delete.

Question 180. How Are The Dimension Tables Designed?

Answer :

Find where data for this dimension are located.
Figure out how to extract this data.
Determine how to maintain changes to this dimension.
Change fact table and DW population routines.

Question 181. What Are The Advantages Data Mining Over Traditional Approaches?

Answer :

Data Mining is used for?the estimation of future. For example,?if we take a company/business organization, by using the concept of Data Mining, we can predict the future of business interms of Revenue (or) Employees (or) Cutomers (or) Orders etc.

Traditional approches use?simple algorithms?for estimating the future. But, it does not give accurate results when compared to Data Mining.

Question 182. Which Automation Tool Is Used In Data Warehouse Testing?

Answer :

No Tool testing in done in DWH, only manual testing is done.

Question 183. Give Examples Of Degenerated Dimensions

Answer :

Degenerated Dimension is a dimension key without corresponding dimension. Example:

In the PointOfSale Transaction Fact table, we have:

Date Key (FK), Product Key (FK), Store Key (FK), Promotion Key?(FP),?and POS Transaction Number?? Date Dimension corresponds to Date Key, Production Dimension corresponds to Production Key. In a traditional parent-child database, POS Transactional Number would be?the key to the transaction header record that contains all the info valid for the transaction as a whole, such as the transaction date and store?identifier.?But in this?dimensional model, we have already extracted this info into other dimension. Therefore, POS Transaction Number?looks like a dimension key in the fact table but does not have the corresponding dimension table.

Therefore, POS Transaction Number is a degenerated dimension.

Question 184. What Is The Datatype Of The Surrogate Key?

Answer :

Normally Surrogate keys are sequencers which keep on increasing with new records being injected into the table. The standard datatype is integer.

Question 185. How To Get Dml Using Utilities In Unix?

Answer :

If your source is a cobol copybook, then we have a command in unix which generates the required in Ab Initio. here it is:
cobol-to-dml.

Question 186. What Is Skew And Skew Measurement?

Answer :

skew is the mesaureof data flow to each partation .
suppose i/p is comming from 4 files and size is 1 gb
1 gb= ( 100mb+200mb+300mb+5oomb)
1000mb/4= 250 mb
(100- 250 )/500= --> -150/500 == cal ur self it wil come in -ve value.
calclu for 200,500,300.
+ve value of skew is allways desriable.
skew is a indericet measure of graph.

Question 187. What Is The Difference Between A Scan Component And A Rollup Component?

Answer :

Rollup is for group by and Scan is for successive total. Basically, when we need to produce summary then we use scan. Rollup is used to aggregate data.

Question 188. What Is M_dump?

Answer :

m_dump command prints the data in a formatted way.
m_dump

Question 189. What Is The Importance Of Eme In Abinitio?

Answer :

EME is a repository in Ab Inition and it used for checkin and checkout for graphs also maintains graph version.

Question 190. What Is Brodcasting And Replicate?

Answer :

Broadcast - Takes data from multiple inputs, combines it and sends it to all the output ports.

Eg - You have 2 incoming flows (This can be data parallelism or component parallelism) on Broadcast component, one with 10 records & other with 20 records. Then on all the outgoing flows (it can be any number of flows) will have 10 + 20 = 30 records.

Replicate - It replicates the data for a particular partition and send it out to multiple out ports of the component, but maintains the partition integrity.

Eg - Your incoming flow to replicate has a data parallelism level of 2. with one partition having 10 recs & other one having 20 recs. Now suppose you have 3 output flos from replicate. Then each flow will have 2 data partitions with 10 & 20 records respectively.

Question 191. What Is Local And Formal Parameter?

Answer :

Two are graph level parameters but in local you need to initialize the value at the time of declaration where as globle no need to initialize the data it will promt at the time of running the graph for that parameter.

Question 192. How To Run The Graph Without Gde?

Answer :

In RUN ==> Deploy >> As script , it create a .bat file at ur host directory ,and then run .bat file from Command prompt.

Question 193. What Are Differences Between Different Gde Versions(1.10,1.11,1.12,1.13and 1.15)? What Are Differences Between Different Versions Of Co-op?

Answer :

1.10 is a non key version and rest are key versions.

There are lot of components added and revised at following versions.

Question 194. Can Anyone Give Me An Exaple Of Realtime Start Script In The Graph?

Answer :

Here is a simple example to use a start script in a graph:
In start script lets give as:
export $DT=`date '+%m%d%y'`
Now this variable DT will have today's date before the graph is run.
Now somewhere in the graph transform we can use this variable as;
out.process_dt::$DT;
which provides the value from the shell.

Question 195. What Is The Syntax Of M_dump Command?

Answer :

The genaral syntax is "m_dump metadata data [action] "

Question 196. How Does Maxcore Works?

Answer :

Maxcore is a value (it will be in Kb).Whne ever a component is executed it will take that much memeory we specified for execution.

Question 197. What Is The Difference Between Dml Expression And Xfr Expression?

Answer :

The main difference b/w dml & xfr is that
DML represent format of the metadata.
XFR represent the tranform functions.which will contain business rules

Question 198. I Am Unable To Connect Sever Database(oracle) From Gde(db Config File) Local System.i Set All These?

Answer :

ChalapathiFirst we can check the properties in internet options and then you can check in cmd format telenet abinitio ip_add.

Question 199. What Is $mpjret? Where It Is Used In Ab-initio?

Answer :

You can use $mpjret in endscript like
if 0 -eq($mpjret)
then
echo "success"
else
mailx -s "[graphname] failed" mailid

Question 200. What Is The Latest Version That Is Available In Ab-initio?

Answer :

The latest version of GDE ism1.15 AND Co>operating system is 2.14.

Question 201. What Is Ab_local Expression Where Do You Use It In Ab-initio?

Answer :

ablocal_expr is a parameter of itable component of Ab Initio.ABLOCAL() is replaced by the contents of ablocal_expr.Which we can make use in parallel unloads.There are two forms of AB_LOCAL() construct, one with no arguments and one with single argument as a table name(driving table).

The use of AB_LOCAL() construct is in Some complex SQL statements contain grammar that is not recognized by the Ab Initio parser when unloading in parallel. You can use the ABLOCAL() construct in this case to prevent the Input Table component from parsing the SQL (it will get passed through to the database). It also specifies which table to use for the parallel clause.

Question 202. How Do You Convert 4-way Mfs To 8-way Mfs?

Answer :

To convert 4 way to 8 way partition we need to change the layout in the partioning component. There will be seperate parameters for each and every type of partioning eg. AI_MFS_HOME, AI_MFS_MEDIUM_HOME, AI_MFS_WIDE_HOME etc.

The appropriate parameter need to be selected in the component layout for the type of partioning.

Question 203. Have You Used Rollup Component? Describe How?

Answer :

If the user wants to group the records on particular field values then rollup is best way to do that. Rollup is a multi-stage transform function and it contains the following mandatory functions.
1. initialise
2. rollup
3. finalise
   Also need to declare one temporary variable if you want to get counts of a particular group.

For each of the group, first it does call the initialise function once, followed by rollup function calls for each of the records in the group and finally calls the finalise function once at the end of last rollup call.

Question 204. What Are Primary Keys And Foreign Keys?

Answer :

In RDBMS the relationship between the two tables is represented as Primary key and foreign key relationship. Wheras the primary key table is the parent table and foreignkey table is the child table.The criteria for both the tables is there should be a matching column.

Question 205. What Is An Outer Join?

Answer :

An outer join is used when one wants to select all the records from a port - whether it has satisfied the join criteria or not.

Question 206. What Are Cartesian Joins?

Answer :

A Cartesian join will get you a Cartesian product. A Cartesian join is when you join every row of one table to every row of another table. You can also get one by joining every row of a table to every row of itself.

Question 207. What Is The Purpose Of Having Stored Procedures In A Database?

Answer :

Main Purpose of Stored Procedure for reduse the network trafic and all sql statement executing in cursor so speed too high.

Question 208. Why Might You Create A Stored Procedure With The With Recompile Option?

Answer :

Recompile is useful when the tables referenced by the stored proc undergoes a lot of modification/ deletion/ addition of data. Due to the heavy modification activity the execute plan becomes outdated and hence the stored proc performance goes down. If we create the stored proc with recompile option, the sql server wont cache a plan for this stored proc and it will be recompiled every time it is run.

Question 209. What Is A Cursor? Within A Cursor, How Would You Update Fields On The Row Just Fetched?

Answer :

The oracle engine uses work areas for internal processing in order to the execute sql statement is called cursor.There are two types of cursors like Implecit cursor and Explicit cursor.Implicit cursor is using for internal processing and Explicit cursor is using for user open for data required.

Question 210. How Can You Force The Optimizer To Use A Particular Index?

Answer :

Use hints /*+ */, these acts as directives to the optimizer.

Question 211. Describe The Process Steps You Would Perform When Defragmenting A Data Table. This Table Contains Mission Critical Data?

Answer :

There are several ways to do this:
1) We can move the table in the same or other tablespace and rebuild all the indexes on the table.
   alter table move this activity reclaims the defragmented space in the table
   analyze table table_name compute statistics to capture the updated statistics.
   2)Reorg could be done by taking a dump of the table, truncate the table and import the dump back into the table.

Question 212. Explain The Difference Between The Truncate And Delete Commands?

Answer :

Truncate :
It is a DDL command, used to delete tables or clusters. Since it is a DDL command hence it is auto commit and Rollback can't be performed. It is faster than delete.

Delete:
It is DML command, generally used to delete a record, clusters or tables. Rollback command can be performed , in order to retrieve the earlier deleted things. To make deleted things permanently, "commit" command should be used.

Question 213. How To Create Repository In Abinitio For Stand Alone System(local Nt)?

Answer :

If you are trying to install the Ab -Initio on stand alone machine , then it is not necessary to create the repository , While installing It creates automatically for you under abinitio folder ( where you installing the Ab-Initio) If you are still not clear please ask your Question on the same portal .

Question 214. How Would You Find Out Whether A Sql Query Is Using The Indices You Expect?

Answer :

Explain plan can be reviewed to check the execution plan of the query. This would guide if the expected indexes are used or not.

Question 215. How Can I Run The 2 Gui Merge Files?

Answer :

Do you mean by merging Gui map files in WR.If so, by merging GUI map files in GUI map editor it wont create corresponding test script.without testscript you cant run a file.So it is impossible to run a file by merging 2 GUI map files.

Question 216. Describe The Elements You Would Review To Ensure Multiple Scheduled Batch Jobs Do Not Collide With Each Other?

Answer :

Because every job depend upon another job for example if you first job result is successfull then another job will execute otherwise your job doesn't work.

Question 217. What Is The Difference Between Rollup And Scan?

Answer :

By using rollup we cant generate cumulative summary records for that we will be using scan.

Question 218. Describe The Grant/revoke Ddl Facility And How It Is Implemented?

Answer :

Basically,This is a part of D.B.A responsibilities GRANT means permissions for example GRANT CREATE TABLE ,CREATE VIEW AND MANY MORE .

REVOKE means cancel the grant (permissions).So,Grant or Revoke both commands depend upon D.B.A.

Question 219. When Using Multiple Dml Statements To Perform A Single Unit Of Work, Is It Preferable To Use Implicit Or Explicit Transactions, And Why?

Answer :

Because implicit is using for internal processing and explicit is using for user open data requied.

Question 220. What Does Dependency Analysis Mean In Ab Initio?

Answer :

Dependency analysis will answer the questions regarding datalinage.That is where does the data come from,what applications prodeuce and depend on this data etc.

We can retrieve the maximum (surrogate key) from the existing data,the by using scan or next_ in_ sequence/ reformat we can generate further sequence for new records.

Question 221. How Do We Design A Universe?

Answer :

The design method consists of two major phases.
During the first phase, you create the underlying database structure of your universe. This structure includes the tables and columns of a database and the joins by which they are linked. You may need to resolve loops which occur in the joins using aliases or contexts. You can conclude this phase by testing the integrity of the overall structure.

During the second phase, you can proceed to enhance the components of your universe. You can also prepare certain objects for multidimensional analysis. As with the first phase, you should test the integrity of your universe structure. You may also wish to perform tests on the universes you create from the BusinessObjects User module. Finally, you can distribute your universes to users by exporting them to the repository or via your file system.

For a universe based on a simple relational schema, Designer provides Quick Design, a wizard for creating a basic yet complete universe. You can use the resulting universe immediately, or you can modify the objects and create complex new ones. In this way, you can gradually refine the quality and structure of your universe.

Question 222. What Are Universe Requirements?

Answer :

At-least one object in the class must be present in the other class so that they can have a join n afcourse the datatypes.

Question 223. Explain In Detail Abt Measure Objects? And What Is The Use Of It? How To Create It?

Answer :

Measure objects are the objects which have facts i.e all $ amounts
a dimension object cannot be calculated with another dim object.
in order to have a seperate identity for $ amounts we define as measure objects.
just create an object for ex:revenue then right clicck on the object or double click on the object n then change the property of that object to measure its that simple.

Question 224. How To Create Generic Time Class, Which Includes Objects Year,month And Qtr? Database In Use Is Oracle?

Answer :

If your database consist all dates something like 01/02/2000 or 01-Feb-2000, you will need to break the date field into year, qtr,month & if required date.
to do this, create a class named TIME, under that create new object, in it's select box use oracle's date functions to get required information.

For E.g. : to_char(sales_date, 'YYYY') for getting only year from the date.
similarly, for quarter you can use to_char(sales_date, 'Q')
& for month to_char(sales_date, 'MM') for month number, instead of 'MM' if you use 'MON' it will return you abrevations like Jan for January & so on. for full name of month use 'MONTH'.

Question 225. How To Create Universe Using Flat File In Bo6.0?

Answer :

Business Objects deals with databases, for every universe you need to specify a database connection. flat files dont have the database format so you'll need to convert them into some database. to do that, you will need to write a procedure which will read data from flat files & relate it according to surrogate keys, then using that procedure populate the database & then use that database for the source of the universe.

using flat files ONLY , you can not create universe. because there is nothing as database connection available for flat file.

Question 226. What Are The Security Level Used In Bo?

Answer :

We have securities in business objects
Like
1.Windows authentication
2.RDBMS securities
3.supervisor level securities, ie User name/ password.

Question 227. How To Create Context?

Answer :

To create context :

goto Tools --> Detect Loops, BO will detect loops if there are any & will suggest the context candidate (something like Sales, Costs that is related to that specific subject area)

Select the suggested candidate & click on create Context. It will map all those joins that are required for say Sales subject area & put it in Sales Context. same with Costs.

So it will avoid the confilcts in path by using Contexts.

This Auto Detection works in most of the times....but not always.

Question 228. What Is The Difference In Creating Filters In Designer And Business Objects?

Answer :

Creating a filter in designer is different from creatind a filter in business object
if u create a filter in designer it can acessible to all the reports ur r using i'e,it can used for further applications where as creatin a filter vin business object is dynamic(run time) it will applicable to only tht particular report.

Question 229. I Need To Set Predefined Condition. How I Do This?

Answer :

We can set the predefined condition in the universe level. In the task bar of the designer there is an icon for filtering. Just click on the icon. It asks for the condition name. After giving the name for the condition type the sql for that condition. finally submit the sql.

Question 230. What Is Is The Guidelines To Build Universe With Better Performance? R Performance Tuning Issues Of Universes?

Answer :

Guidelines are provided in the Universe guide:
Here is the Summary:
1) Modify the array fetch size in SBO file
2) Assign table weights and change the default order of the tables in a query by changing parameter in PRM file
3) Use shorcut joins to avoid unnecessary tables that may come in Query
4) Use aggregated tables.

Question 231. How To Implement The The Built-in Strategy Script In Bo Designer?

Answer :

Using quick design wizard for developing the universe will invoke the built-in strategy.

Question 232. What Is Pragma?

Answer :

pragma pack preprocessor dirictive specifies the byte boundary for packing members of c structures.syntax: #pragma pack(n)

Question 233. What Is Slicing And Dicing In Business Objects?

Answer :

Slice & Dice is facility in BO. we can enables change the positions of data in Report..here in Bo we slice & dice panel by using this we can create cross tables and masterdetails tables.

Question 234. Which Command Using Query Analyzer Will Give You The Version Of Sql Server And Operating System?

Answer :

elect @@version is the command that will give the said details.

Question 235. How Will You Know The Version Of Bo Using Designer?

Answer :

Select the component business object Designer
Now it will prompt for userid/password/security domain
You will find a Help button, click that and find out what ever you want

Question 236. What Are The Steps To Taken Care To Improve The Report Performance?

Answer :

In DESIGNER Level
1)eliminate the unnecessory joins
2)use conditions as much as at the database level
3)edit the SQL query in the Query Panel as per requirment

In REPORTER level
1)eliminate the filters as much as possible
2)try to reduce the user variables.

Question 237. What Is Index Awareness In Universe?

Answer :

Index awareness is the ability to take advantage of the indexes on key columns to speed data retrieval.

Question 238. How Can We Acheive Correlated Sub-query In Designer?can Anyone Help Me In This Regard?

Answer :

Right click on any object,go to the properties.specify the query in select and put the next query in where clause,
like select COLNAME from TABNAME1 where COLNAME IN(select colname2 from tab2)

Question 239. What Is Mean By Aggregate Aware? How We Are Using This Function?

Answer :

Aggregate awareness is a term that describes the ability of a universe to make use of aggregate tables in a database. These are tables that contain precalculated data. You can use a function called @Aggregate_Aware in the Select statement for an object that directs a query to be run against aggregate tables rather than a table containing non aggregated data.
Pros:
Speed up the execution of query and Improve the performance of Sql transaction.
If you are using the aggregate tables then you must refresh the aggregate table with all fact tables to have the consistency in your result.

Question 240. Explain The Concepts And Capabilities Of Business Object.

Answer :

A business object can be used to represent entities of the business that are supported in the design. A business object can accommodate data and the behavior of the business associated with the entity.

Question 241. Explain The Functional Differences Between Bo And Cognos.

Answer :

Business objects in business intelligence are entities of the business. COGNOS makes BI and performance planning software.

Question 242. What Is A Universe? Explain The Types Of Universes In Business Objects.

Answer :

A universe connects the client to the data warehouse. It is a file defining relationships amongst the tables in the warehouse, classes and objects, database connection details.

Question 243. What Is Bomain.key?

Answer :

A BOMain.key file contains all relevant information about the repository. It contains the address of the repository security domain. The file is sotred in the LOCData folder.

Question 244. What Is Object Qualification?

Answer :

Object qualification is an attribute of an object that helps to determine how it can be used in multidimensional analysis. Using this, the multidimensional analysis objects can either be qualified as dimension, detailed and measure.

Question 245. What Is The Security Level Used In Bo?

Answer :

Security level used in BO:-
Row Level
Column Level
Both the levels are used to restrict data at a row or column level to a user or a group. Both the security levels are handled by the administrator of the tool.

Question 246. What Are The Functional & Architectural Differences Between Business Objects And Web Intelligence Reports?

Answer :

Functional differences
• Business objects, for building or accessing reports, needs to be installed on every pc. On the other hand, Web intelligence reports needs a browser and a URL of the server from where Business objects will be accessed.
• BOMain.key needs to be copied on every pc using BO client. This is not required for Web Intelligence Reports.
• Business objects expect you to use the same pc where they are installed. Web Intelligence reports can be accessed from anywhere, provided internet is available.

Architectural differences
For BO client, for sending info to BO Server BOMain.key, uses the key of the local drive. Once the information is sent, it is validated and checked into the repository upon which the user can access the BO services. On the other hand, Web Intelligence the web servers BOMain.key is used to check privilege of the user and then sending information to the BO Server BOMain.key.

Question 247. What Is Batch Processing In Business Objects?

Answer :

Batch processing can be used to schedule reports. Objects can be also be used for batch processing. Batch processing can be used to also select the objects to be processed. The batch can be run as a transaction in which if one process fails, the entire batch is rolled back or it can be run as a series of jobs.

Question 248. What Is Security Domain In Business Objects?

Answer :

Security domain in business objects is a domain containing all security information like login credentials etc. It checks for users and their privileges. This domain is a part of the repository that also manages access to documents and functionalities of each user.

Question 249. What Is Data Cardinality?

Answer :

Cardinality is the term used in database relations to denote the occurrences of data on either side of the relation.
There are 3 basic types of cardinality:
High data cardinality:
Values of a data column are very uncommon.
e.g.: email ids and the user names

Normal data cardinality:
Values of a data column are somewhat uncommon but never unique.
e.g.: A data column containing LAST_NAME (there may be several entries of the same last name)

Low data cardinality:
Values of a data column are very usual.
e.g.: flag statuses: 0/1

Question 250. What Is Chained Data Replication?

Answer :

In Chain Data Replication, the non-official data set distributed among many disks provides for load balancing among the servers within the data warehouse.

Blocks of data are spread across clusters and each cluster can contain a complete set of replicated data. Every data block in every cluster is a unique permutation of the data in other clusters.

When a disk fails then all the calls made to the data in that disk are redirected to the other disks when the data has been replicated.

At times replicas and disks are added online without having to move around the data in the existing copy or affect the arm movement of the disk.

In load balancing, Chain Data Replication has multiple servers within the data warehouse share data request processing since data already have replicas in each server disk.

Question 251. Explain In Brief Various Fundamental Stages Of Data Warehousing.

Answer :

The following are the stages of data warehousing:

Offline Operational Database: It is the stage where copying the data off an operational system to another server where the report processing load against the copied data takes place and OS performance does not impact.

Offline Data Warehouse: In this stage, data warehouses are updated from data in the OS and the data of data warehouse is stored in a data structure that is designed for facilitating reports.

Real time Data Warehouse: The data warehouses are updated often when an OS performs a transaction.

Integrated Data Warehouse: The data warehouses are updated by OS, at the time of performing a transaction. Then transactions are generated which are passed back into the operational systems.

Question 252. What Are Products Of Cognos?

Answer :

Cognos 6.6 7.0,7.3(PowerPlay, Impromptu)--ReportNet1.0,1.1mr1, 1.1mr22---ReportNet 8.0(latest)IWR is use by Impromptu to publish reports, PPES is used by PP, Cognos Connection is used by repornet. there are many other tools but these are the main.

Question 253. How Can I Test Reports In Cagonos?

Answer :

In cognos report net by the validate report option a report can be tested. If there will be any error, it will specify the the error, unless it will give message -'report specification is valid'.

After creating the report we will connect to the oracle and we will write the sql query and we will compare this 2 reports .

Question 254. How Can I Schedule Reports In Cognos?

Answer :

By using Cognos Schedular, one can schedule the running reports in Impromptu to execute and save it in desired format.

By using Cognos MACRO script language the reports can be executed and distributed to recipients by using mail applications.

Question 255. How Can Create Users And Permissions In Cognos?

Answer :

impromptu menu go to Catlog->User profiles -> userclass tab -> click on Creator ->u can give there folder access,table access,filters,Governor etc

you can crate users by using USERS PROFILE option......and you can give permissions using ROLE IN C8 and GOVERNERS in C7

Question 256. What Is Cognos Visualizer And Cognos Scripting?

Answer :

Visualizer is a representation of data cubes in a dashboard format. We can drill through to the ground level of a hierarchy as like in power play report but cannot add or remove fields dynamically.

Cognos script editor : We can write cognos macros or programs in this tool and can fine tune or process some execution.

Question 257. How Do Add Dynamic Titles In Pp?

Answer :

PowerplayFrom format menu-->title, header & footer-->title-->insert report filename

Question 258. What You Mean By Drill Across And What Is The Difference Between Drill Through, Drill Across?

Answer :

Drill across means when you are moving from one report to another report like country in one report and States in another Report whereas if the report is using same report from moving from country to state. In other when you are moving details level if you are using the different report it is drill across and if you are using same report it is drill through.

Question 259. What Is Loop In Frameworkmanager?

Answer :

Loop: loop is a closed path (relation) that exists among 3 (or) more tables. For example, if we have '3' tables T1, T2, T3 then, a loop exists among these tables only when we create joins in the following fashion:

Loop: T1 ---> T2 ---> T3 ---> T1

To resolve the above problem, we have to create a shortcut (or) Alias to the Table T1.

No Loop: T1 ---> T2 ---> T3 ---> Alias (or) Shortcut of T1

Question 260. How Create Measures And Demensions?

Answer :

You can create measure once you import all the data into the data source.You can create measures and dimensions by draging the required source from datasource into dimension map and measure tab.(need to find scope of measures for all the dimensions)

Question 261. What Is Meant By Alternate Drill Down With Ex?

Answer :

Alternate drill down path means there will be two path to opt.For example- We will have time dimension now the client requirement is they want two type of year -one is calender year(Jan-Dec) and another is fiscal year(Apr-Mar).

Question 262. What Is The Difference Between Enterprise Data Warehouse And Data Warehouse?

Answer :

Big Organizations have a lot of diversified sources of data.There might be a dataware house exclusively for transport and others for data related to the project the company runs.In such case the complete enterprise's(company's) date ware house is a big combination of all and is known the Enterprise data Warehouse(EDW)

Question 263. How You Drill From Powerplay To Impromptu? Explain All Steps?

Answer :

go to tran former,
build the cube
right click on the cube and open properties
go to drill through tab and select your report from that browse option

Question 264. Give Me Any Example Of Semi And Non Additive Measures?

Answer :

Semi-Additive: Semi-additive facts are facts that can be summed up for some of the dimensions in the fact table, but not the others. Non-Additive: Non-additive facts are facts that cannot be summed up for any of the dimensions present in the fact table. Current Balance and Profit Margin are the facts.Current Balance is a semi-additive fact, as it makes sense to add them up for all accounts (what's the total current balance for all accounts in the bank?), but it does not make sense to add them up through time (adding up all current balances for a given account for each day of the month does not give us any useful information). Profit Margin is a non-additive fact, for it does not make sense to add them up for the account level or the day level.

Question 265. What Is Drill Down And Slicing And Dicing Whats The Difference Between Them?

Answer :

Drilling lets you quickly move from one level of detail to another to explore different aspects of your business. Drilling down moves you down in the hierarchy; drilling up moves you up in the hierarchy.

Slicing and Dicing:
While you can drill to look at information at any level, you can slice and dice to select the exact information you want in your report.

Question 266. What Is The Difference Between A Cascading Report And Drillthru Report?why Do We Go For Drill Thru Report?

Answer :

Cascading report works based on the condition but drill thru work based on the data item what we select as a drill thru options.

Question 267. What Junk Dimension Contains?

Answer :

It contains the miscellaneous attributes such as flags , which does belong to the main dimension table.

for eg; In a sales order fact table ,some informations like, web-order , whether this is a online order or not new_cust , Is this person a new customer ?
verification , whether the order has been verified?

Question 268. What Is Catalog And Types Of Catalogs In Cagonos And Which Is Better?

Answer :

A catalog is a file containing the information (Database tables) that Impromptu users need to create reports.

► personal
► distributed
► shared
► secured

shared catalog is better.

Question 269. What Is Meant By Junk Dimension?

Answer :

The junk dimension is simply a structure that provides a convenient place to store the junk attributes.

Question 270. Suppose You Run A Report With Empty Data, How Will You Inform The End User That It Has No Data While Running The Report In Report Studio? Is It Possible, If So How?

Answer :

Add a list footer and a text messsage inside "No Data". create a booloean conditional variable "Test" with code "rownum()>0". Select the complete list footer and set Style Variable, if Yes, Box Type of the List footer should be set to "none". This should work...RD.

Question 271. What Is The Difference B/w Macros And Prompt?

Answer :

Macro-A macro is a set of instructions that can run applications.Example : A macro can open your catalog,select a report(say for instance) convert that to another format and export it to any specified location,provided the code (Program)is such.Prompt-A prompt specifies the manner in which data in the reports are to be displayed.A Prompt can be defined at the catalog level either or during report generation.

Question 272. What Is Cognos Powerhouse And What Is It Used For?

Answer :

Cognos Powerhouse is High-Productivity Application Development Solutions equips you with high-productivity development environments for creating your data-driven business solutions faster,whether for Web-based, client/server, or traditional terminal-based access. PowerHouse has gained a worldwide reputation for productivity, reliability, performance, and flexibility.

Question 273. How Can We Create A Dynamic Column Name In Cognos?

Answer :

Select Properties, and then click the Headers/Footers tab.

Question 274. When To Use Abort, Decode Functions?

Answer :

Abort can be used to Abort / stop the session on an error condition. If the primary key column contains NULL, and you need to stop the session from continuing then you may use ABORT function in the default value for the port. It can be used with IIF and DECODE function to Abort the session.

Question 275. What Is Constraint Based Loading ?

Answer :

Constraint based loading. the data was loaded into the target table based on the Constraints.i.e if we want to load the EMP&DEPT data, first it loads the data of DEPT then EMP because DEPT is PARENT table EMP is CHILD table. In simple terms, it loads PARENT table first then CHILD table.

Question 276. In A Joiner Transformation, You Should Specify The Source With Fewer Rows As The Master Source. Why?

Answer :

Joiner transformation compares each row of the master source against the detail source. The fewer unique rows in the master, the fewer iterations of the join comparison occur, which speeds the join process.

Question 277. What Is Incremental Aggregation?

Answer :

Whenever a session is created for a mapping Aggregate Transformation, the session option for Incremental Aggregation can be enabled. When PowerCenter performs incremental aggregation, it passes new source data through the mapping and uses historical cache data to perform new aggregation calculations incrementally.

Question 278. What Is The Default Join That Source Qualifier Provides?

Answer :

Inner equi join.

Question 279. What Are The Options In The Target Session Of Update Strategy Transformations?

Answer :

Insert
Delete
Update
Update as update
Update as insert
Update else insert
Truncate table

Question 280. Which Transformation Should We Use To Normalize The Cobol And Relational Sources?

Answer :

Normalizer Transformation.

Question 281. What Is The Use Of Tracing Levels In Transformation?

Answer :

Tracing levels store information about mapping and transformations.

Question 282. What Are The Basic Needs To Join Two Sources In A Source Qualifier?

Answer :

Two sources should have primary and foreign key relationships. Two sources should have matching data types.

Question 283. What Is Update Strategy Transformation?

Answer :

This transformation is used to maintain the history data or just most recent changes in to target table.

Question 284. Describe Two Levels In Which Update Strategy Transformation Sets?

Answer :

Within a session. When you configure a session, you can instruct the Informatica Server to either treat all records in the same way (for example, treat all records as inserts), or use instructions coded into the session mapping to flag records for different database operations. Within a mapping. Within a mapping, you use the Update Strategy transformation to flag records for insert, delete, update, or reject.

Question 285. What Are The Various Types Of Transformation?

Answer :

Various types of transformation are: Aggregator Transformation, Expression Transformation, Filter
Transformation, Joiner Transformation, Lookup Transformation, Normalizer Transformation, Rank Transformation,
Router Transformation, Sequence Generator Transformation, Stored Procedure Transformation, Sorter
Transformation, Update Strategy Transformation, XML Source Qualifier Transformation, Advanced External
Procedure Transformation, External Transformation.

Question 286. What Is The Difference Between Active Transformation And Passive Transformation?

Answer :

An active transformation can change the number of rows that pass through it, but a passive transformation can not change the number of rows that pass through it.

Question 287. What Is The Use Of Control Break Statements?

Answer :

They execute a set of codes within the loop and endloop.

Question 288. What Is The Difference Between Static Cache And Dynamic Cache?

Answer :

In case of dynamic cache, when we are inserting a new row it checks the lookup cache to see if it exists, if not inserts it into the target as well as the cache but in case of static cache the new row is written only in the target and not the lookup cache. The lookup cache remains static and does not change during the session but incase of dynamic cache the server inserts, updates in the cache during session.

Question 289. How Do We Join Two Tables Without Joiner Or Sql Override?

Answer :

We can join the tables using lookup tansformation and making a cartesian product.

Question 290. What Are Pre-session And Post-session Options?

Answer :

These are shell commands that Informatica server performs before running the session. We should have permission and privileges to run the options in Informatica.

Question 291. How Do We Copy Mapping?

Answer :

The steps to copy mapping are mentioned below: 1.) First, open navigator window 2.) Open the mapping in repository 3.) Click copy

Question 292. What Are The Tasks Done By Informatica Server?

Answer :

Tasks done by Informatica server are:

a) Managing the sessions
b) Running the workflows
c) Tuning performance
d) Scheduling of sessions and workflows.

Question 293. What Is The Difference Between Source Qualifier And Joiner Transformation?

Answer :

We need matching keys in source qualifier which we do not need in joiner transformation.

Question 294. What Are Mapping Parameters And Mapping Variables?

Answer :

Mapping parameters are parameters which are constant through out the session. They are specified before running the session. Unlike parameters, variables change through out the session.

Question 295. Why Do We Use Partitioning The Session In Informatica?

Answer :

Partitioning achieves the session performance by reducing the time period of reading the source and loading the data into target.

Question 296. To Achieve The Session Partition What Are The Necessary Tasks You Have To Do?

Answer :

Configure the session to partition source data.
Install the Informatica server on a machine with multiple CPU’s.

Question 297. Can You Copy The Batches?

Answer :

NO

Question 298. How Many Number Of Sessions That You Can Create In A Batch?

Answer :

Any number of sessions.

Question 299. When The Informatica Server Marks That A Batch Is Failed?

Answer :

If one of session is configured to “run if previous completes” and that previous session fails.

Question 300. What Is A Command That Used To Run A Batch?

Answer :

pmcmd is used to start a batch.

Question 301. What Are The Different Options Used To Configure The Sequential Batches?

Answer :

Two options
Run the session only if previous session completes successfully.
Always runs the session.

Question 302. How Can You Recognize Whether Or Not The Newly Added Rows In The Source Are Getting Inserted In The Target?

Answer :

In the Type2 mapping we have three options to recognize the newly added rows Version number Flag value, Effective date Range.

Question 303. Can You Start A Session Within A Batch Individually?

Answer :

Let me tell you that one can start the sessions in this way in the case of sequential batches only. In case of the concurrent batches it is virtually impossible.

Question 304. Differences Between Normalizer And Normalizer Transformation.

Answer :

Normalizer: It is a transormation mainly using for cobol sources,
it's change the rows into coloums and columns into rows
Normalization:To remove the retundancy and inconsitecy.

Question 305. What Is The Use Of Incremental Aggregation? Explain Me In Brief With An Example.

Answer :

Its a session option. when the informatica server performs incremental aggr. it passes new source data through the mapping and uses historical chache data to perform new aggregation caluculations incrementaly. for performance we will use it.

Question 306. How Do You Handle Decimal Places While Importing A Flatfile Into Informatica?

Answer :

while importing flat file definetion just specify the scale for a neumaric data type. in the mapping, the flat file source supports only number datatype(no decimal and integer). In the SQ associated with that source will have a data type as decimal for that number port of the source.

source ->number datatype port ->SQ -> decimal datatype.Integer is not supported. hence decimal is taken care.

Question 307. Diff Between Static And Dynamiccache? And Please Explain With One Example?

Answer :

Difference between static and dynamic cache
Static- Once the data is cached , it will not change. example unconnected lookup uses static cache.
Dynamic- The cache is updated as to reflect the update in the table( or source) for which it is reffering to.(ex. connected lookup).

Question 308. What Is Power Center Repository?

Answer :

PC Repository is a relational database that stores the metadata describes different objects like mapping and transformation. This is managed by repository service.

Question 309. Define Informatica Repository?

Answer :

Infromatica Repository:The informatica repository is at the center of the informatica suite. You create a set of metadata tables within the repository database that the informatica application and tools access. The informatica client and server access the repository to save and retrieve metadata.

Question 310. How Many Types Of Dimensions Are Available In Informatica?

Answer :

There r 3 types of dimensions
1.star schema
2.snowflake schema
3.glaxy schema

Question 311. How Can We Use Pmcmd Command In A Workflow Or To Run A Session

Answer :

pmcmd>startworkflow -f foldername workflowname

Question 312. In Update Strategy Target Table Orflat File Which Gives More Performance ? Why?

Answer :

Pros: Loading, Sorting, Merging operations will be faster as there is no index concept and Data will be in ASCII mode.

Cons: There is no concept of updating existing records in flat file.

As there is no indexes, while lookups speed will be lesser.

Question 313. What Is The Difference Between Informatics 7x And 8x And What Is Latest Version?

Answer :

Java Transformation available in the 8x version and it is not available in 7x version.

Question 314. What Is The Main Advantage Of Impromptu Over Cognos Reportnet?

Answer :

One of the advantage's of Reportnet, is
It is web-based reporting wherein, reports can be easily accessed from anywhere through a browser. by using ipromptu we can use multidimensional analysis to see the data in diff formates.i.e we have drillup,drilldown features in cognos impromtu,but it is not possible in reportnet.

Question 315. What Is The Difference Between Native Sql And Cognos Sql?

Answer :

In cognos reportnet
Native SQL is used for the single datasource to import the meta data
Cognos SQL used for multiple datasources to import the metadata.

Question 316. What Is The Difference Between Powerplay Transformer And Power Play Reports?

Answer :

'Powerplay transformer' is an 'MOLAP' tool using which one can create multi dimensional structure called "CUBE".

'Powerplay for reports' is used to generate report from the cube.Only one report can be generated from one cube.If u want 'n' reports u must create 'n' cubes.

Question 317. Is There Any Comparison Available For Cognos Reportnet Vs Crystal Reports?

Answer :

There is a lot of difference between Crystal reports an Cognos Report net.

1.Crystal report is a product of Business Objects where as Reportnet is of cognos.

2.Cryatal reports is for only low 2 midrange analysis and that to some even says tha they wont use this for analysis used to make proper strategic decision But report net yes it is for high end analysis.

3.In reportnet we can login through web and can create our own desired report through web.

Question 318. How Do We Drill Through From A Powerplay Cube To Reportnet?

Answer :

Setting up drill-through access from PowerPlay Web to ReportNet involves

1. configuring Cognos Series 7 for drill-through access to ReportNet
2. preparing the Transformer model and cube
3. copying the search path of the folder that contains the target report
4. enabling the cube for drill-through access to ReportNet
5. deciding which filters to create in the target report
6. creating the target report
7. disabling the Drill Through Assistant.

Question 319. What Is Prompt?types Of Prompts?use Of Prompts?syntax Of Prompt?

Answer :

Prompts act as questions that help users to customize the information in a report to suit their own needs.The different types of Prompt are
Value prompt
Text Prompt
Date prompt
Time prompt
Date and time prompt
Using prompts is faster and easier than repeatedly changing the filter.

Cognos Report Studio provides several ways to create prompts. You can
• use the Build Prompt Page tool
• build your own prompt and prompt page
• create a parameter to produce a prompt
• create a Prompt directly in a report page.

Question 320. What Is Difference Between Qurry Studio And Report Studio?

Answer :

Query Studio:
1. Used to create Ad-hoc (or) simple reports.
2. It does not provide any pre-defined report templates.
3. It directly displays data (without running the report) when we insert attributes in the report.

Report Studio:
1. Used to create complex reports.
2. It provides pre-defined report templates.
3. It does not display the data directly in the report. We need to run the report to display the data.

Question 321. What Are Components Of Report Studio?

Answer :

Componenets of Report Studio:
1. Insertable Objects pane.
2. Properties pane.
3. Explorer bar - Conditional Explorer, Query Explorer, Page Explorer.
4. Report Viewer - Workarea, Report Layout Objects.

Question 322. What Are Components Of Reportnet?

Answer :

ReportNet has a three-tier architecture, namely,
(1) Web server (2) Applications and (3) Data.
The tiers are based on business function, and are typically separated by firewalls. ReportNet user interfaces sit above the tiers.ReportNet user interfaces include
(a) Web-based Cognos Connection, Cognos Report Studio, and Query Studio
(b) Windows-based Framework Manager.

Question 323. How Do We Provide Security In Frame Work Manager For A Query Subject?

Answer :

procedure for providing security for query subject in frame work manager is:
select querysubject -> in properties pane select ->security filters(click on edit)a specify data security wizard appears->click on add groups -> cognosnamesspace(select users and groups wizard opens)

Question 324. How Can I Create Prompts In Report Net

Answer :

Prompts is mean by the end user can be filter the data.
1.you can open the explore bar and added the new prompts page, And enter the new name.
2. you go to tool menu and track prompts button
3. you select prompts and then ok.

Question 325. Difference Between Filter And Condition?

Answer :

The difference between Filter and Condition:Condition returns true or false Ex: if Country = 'India' then ...Filter will return two types of results1.Detail information which is equal to where clause in SQL statement2.Summary information which is equal to Group by and Having clause in SQL statement.

Question 326. Can Report Net Connect Multiple Datasource At A Time In Report Creation Time

Answer :

Yes it can connect multiple datasources at a time when the frame work manager has the metta data regarding that datasources.

Question 327. How Can I Test Report In Reportnet

Answer :

If we wanna test the report in report net, first we can intially check by validating it in the report page.

After that we can test the out put of the report Using a sql anlyser and sql query.so here we will be comparing the sql analyzer output with the output of the report viewer.

Question 328. What Are The Various File Formats Involved In Reportnet?

Answer :

It has six (6) formats in report net. They are HTML, PDF, Excel 2000, Excel 2002, CSV, and XML format. We can see the types of formats in the report viewer on the right side .

Question 329. How To Generate Iqd File From Framework Manager

Answer :

Create a Query Subject, from the properties pane select externalise,there we have 4 options in that select IQD.

Question 330. What Are Versions Of Reportnet?

Answer :

In ReprotNet have two vertions
1.ReportNet 1.0
2.ReportNet 1.1 MR1, MR2.

Question 331. What Is Business Intelligence?

Answer :

Business Intelligence is a process for increasing the competitive advantage of a business by intelligent use of available data in decision making.

The five key stages of Business Intelligence:
► Data Sourcing
► Data Analysis
► Situation Awareness
► Risk Assessment
► Decision Support.

Question 332. What Is A Universe In Business Intelligence?

Answer :

"universe" is a "Business object" terminology. Business objects also happens to be the name of the company. The universe is the interfacing layer between the client and the datawarehouse . The universe defines the relationship among the various tables in the datawarehouse.

Or

Universe is a semantic layer between the database and the user interface (reports).

Question 333. What Is Olap In Business Intelligence?

Answer :

Online Analytical Processing, a category of software tools that provides analysis of data stored in a database. OLAP tools enable users to analyze different dimensions of multidimensional data. For example, it provides time series and trend analysis views. The chief component of OLAP is the OLAP server, which sits between a client and a database management systems (DBMS). The OLAP server understands how data is organized in the database and has special functions analyzing the data.

A good OLAP interface has writes an efficient sql and reads an accurate data from db.To design and architect having good knowledge on DB understanding the report requirements.

Question 334. What Are The Various Modules In Business Objects Product?

Answer :

► Business Objects Reporter
► Reporting & Analyzing tool
► Designer
► Universe creation
► database interaction
► connectivity
Supervisor - For Administrative purposes
Webintelligence - Access of report data through internet
BroadCast Agent - For scheduling the reports
Data Integrator - The ETL tool of Business Objects, designed to handle huge amounts of data.

Question 335. What Is Olap, Molap, Rolap, Dolap, Holap? Explain With Examples?

Answer :

OLAP - On-Line Analytical Processing.
Designates a category of applications and technologies that allow the collection, storage, manipulation and reproduction of multidimensional data, with the goal of analysis.

MOLAP - Multidimensional OLAP.
This term designates a cartesian data structure more specifically. In effect, MOLAP contrasts with ROLAP. Inb the former, joins between tables are already suitable, which enhances performances. In the latter, joins are computed during the request.
Targeted at groups of users because it's a shared environment. Data is stored in an exclusive server-based format. It performs more complex analysis of data.

DOLAP - Desktop OLAP.
Small OLAP products for local multidimensional analysis Desktop OLAP. There can be a mini multidimensional database (using Personal Express), or extraction of a datacube (using Business Objects).
Designed for low-end, single, departmental user. Data is stored in cubes on the desktop. It's like having your own spreadsheet. Since the data is local, end users dont have to worry about performance hits against the server.

ROLAP - Relational OLAP.
Designates one or several star schemas stored in relational databases. This technology permits multidimensional analysis with data stored in relational databases.
Used for large departments or groups because it supports large amounts of data and users.

HOLAP:Hybridization of OLAP, which can include any of the above.

Question 336. Why An Infocube Has Maximum Of 16 Dimensions?

Answer :

It depends upon the Database limits provided to define the Foreign key constraint, e.g. in Sql Server 2005, the recommended max limit for foreign keys is 253, but you can define more.

Question 337. What Is Bas? What Is The Function?

Answer :

The Business Application Support (BAS) functional area at SLAC provides administrative computing services to
the Business Services Division and Human Resources Department. We are responsible for software
development and maintenance of the PeopleSoft? Applications and consultation to customers with their
computer-related tasks.

Question 338. Name Some Of The Standard Business Intelligence Tools In The Market?

Answer :

Some of the standard Business Intelligence tools in the market According to their performance
► MICROSTRATEGY
► BUSINESS OBJECTS,CRYSTAL REPORTS
► COGNOS REPORT NET
► MS-OLAP SERVICES
Or
► Seagate Crystal report
► SAS
► Business objects
► Microstrategy
► Cognos
► Microsoft OLAP
Hyperion
Microsoft integrated services.

Question 339. How Do We Enhance The Functionality Of The Reports In Bo?

Answer :

You can format the BO Reports by using various features available. You can turn the table reports into a 2-Dimensional or 3-Dimensional charts. You can apply an Alert to show some data in a different format , based on some business rule. You can also create some prompts, which will asks user to give some input values before seeing the reports, this way they will see only filtered data. There are many similar exciting options available to enhance the reports.

Question 340. What Are Dashboards?

Answer :

A management reporting tool to gauge how well the organization company is performing. It normally uses "traffic-lights" or "smiley faces" to determine the status.

Question 341. Explain About Auditing In Bo Xi R2? What Is The Use Of It?

Answer :

Auditor is used by the business objects administrators to know the complete information of the business intelligence system.
► it monitors entire BIsystem at a glance.
► Analyzes usage and change impact
► optimises the BI deployment

Question 342. How Do We Tune The Bo Reports For Performance Improvement?

Answer :

We can tune the report by using index awareness in universe.

Question 343. Why We Ca Not Create An Aggregate On An Ods Object?

Answer :

► Operational Data Store has very low data latency. Data moved to ODS mostly on event based rather than time based ETL to Data Warehouse/Data Mart.
► ODS is more closer to OLTP system. We don't normally prefer to store aggregated data in OLTP. So it is with ODS.
► Unlike data warehouse where data is HISTORICAL, ODS is near real time(NRT). So data aggregation is less important is ODS as data keeps changing.

Question 344. What Is Hierarchy Relationship In A Dimension.

Answer :

whether it is:
1. 1:1
2. 1:m
3. m:m
   1:M

Question 345. How To Connect Gde To Co Operating System In Abinitio?

Answer :

We can connect Ab Initio GDE with Co>operating system using Run->Settings.In there u can specify the host IP address and the connection type .Refer Ab Initio help for further details.

Question 346. Explain The Name Of Some Standard Business Intelligence Tools In The Market?

Answer :

Some of the standard Business Intelligence tools in the market According to there performance
1)MICROSTRATEGY
2)BUSINESS OBJECTS,CRYSTAL REPORTS
3)COGNOS REPORT NET
4)MS-OLAP SERVICES.

Question 347. From Where You Get The Logical Query Of Your Request?

Answer :

The logical SQL generated by the server can be viewed in BI Answers. If I have not understood the question, Please raise your voice.

Question 348. Major Challenges You Faced While Creating The Rpd?

Answer :

Every now and then there are problems with the database connections but the problem while creating the repository RPD files comes with complex schemas made on OLTP systems consisting of lot of joins and checking the results. Th type of join made need to be checked. By default it is inner join but sometimes the requirement demands other types of joins. There are lot of problems with the date formats also.

Question 349. What Are Global Filter And How Thery Differ From Column Filter?

Answer :

Column filter- simply a filter applied on a column which we can use to restrict our column values while pulling the data or in charts to see the related content.

Global filter- Not sure. I understand this filter will have impact on across the application but I really dont understand where and how it can be user. I heard of global variables but not global filters.

Question 350. Where To Configure The Scheduler?

Answer :

We configure the OBIEE schedular in database.

Question 351. How To Hide Certain Columns From A User?

Answer :

Application access level security- Do not add the column in the report, Do not add the column in the presentation layer.

Question 352. How Can We Enable Drills In A Given Column Data?

Answer :

To enable Drill down for a column, it should be included in the hirarchy in OBIEE. Hyperion IR has a drill anywhere feature where dont have to define and can drill to any available column.

Question 353. Is Drill Down Possible Without The Attribute Being A Part Of A Hierarchical Dimension?

Answer :

No

Question 354. How Do U Conditional Format.?

Answer :

while creating a chat in BI Answers, you can define the conditions and can apply colour formatting.

Question 355. What Is Guided Navigation?

Answer :

I think it is just the arrangement of hyperlinks to guide the user to navigate between the reports to do the analysis.

Question 356. How The Users Created Differs From Rpd/answers/dashboards Level?

Answer :

RPD users can do administrator tasks like adding new data source, create hirarchies, change column names where as Answers users may create new charts, edit those charts and Dashboard users may only view and analyse the dashboard or can edit dashboard by adding/removing charts objects.

Question 357. Online/offline Mode How It Impact In Dev And Delpoyment?

Answer :

Online Mode- You can make changes in the RPD file and push in changes which will be immediately visible to the users who are already connected. This feature we may use in production environment.
Offline mode- can be useful in test or development environment.

Question 358. Explain The Concepts And Capabilities Of Business Intelligence?

Answer :

Business Intelligence helps to manage data by applying different skills, technologies, security and quality risks. This also helps in achieving a better understanding of data.Business intelligence can be considered as the collective information. It helps in making predictions of business operations using gathered data in a warehouse. Business intelligence application helps to tackle sales, financial, production etc business data. It helps in a better decision making and can be also considered as a decision support system.

Question 359. Explain The Dashboard In The Business Intelligence.

Answer :

A dashboard in business intellgence allows huge data and reports to be read in a single graphical interface. They help in making faster decisions by replying on measurable data seen at a glance. They can also be used to get into details of this data to analyze the root cause of any business performance. It represents the business data and business state at a high level. Dashboards can also be used for cost control. Example of need of a dashboard: Banks run thousands of ATM’s. They need to know how much cash is deposited, how much is left etc.

Question 360. Sas Business Intelligence.

Answer :

SAS business intelligence has analytical capabilities like statistics, reporting, data mining, predictions, fore casting and optimization. They help in getting data in the format desired. It helps in improving quality of data.

Question 361. Explain The Sql Server 2005 Business Intelligence Components.

Answer :

• SQL Server Integration Services:- Used for data transformation and creation. Used in data acquisition form a source system.
• SQL Server Analysis Services: Allows data discovery using data mining. Using business logic it supports data enhancement.
• SQL Server Reporting Services:- Used for Data presentation and distribution access.

Question 362. Web Services Make Use Of Which Vanilla Business Service To Update,insert Data In Siebel ?

Answer :

EAI Siebel Adapter
EAI UI Data Adapter
EAI MQ Series Server Transport

Question 363. When You Import A Wsdl File In Siebel Tools, What Type Of Web Service Is Created?

Answer :

Inbound Web Service
Outbound Web Service

Question 364. If I Import A Xsd Or A Dtd File In Siebel Tools, What Is The "type" Of Integration Object Is Created?

Answer :

Siebel Business Object
XML
SQL Database Wizard

Question 365. What User Keys A Web Service Use To Identify A Record?

Answer :

Base Table User Keys
Mod Id and Row Id of IC's
IC User Keys

Question 366. If An Io-ic Is Created On A Bo, And One Of The Ic Gets Two User Property Set As 'mvg'=y And Mvglink = . What Is True Below?

Answer :

Child BC is added in the BO via a Link
A MVL is created in the Parent BC connecting to Child

Question 367. What Is The Best Mode To Call A Workflow Asynchronously Using The Business Service - "asynchronous Server Request"?

Answer :

Sync
Async
DirectDB

Question 368. Soapui Is A Free Tool Which Can Be Used To Test, What ?

Answer :

Business Service
Web Services
Workflow

Question 369. How Can We Generate Empty Input Request Message Based On A Integration Object?

Answer :

Using ‘EAI XSLT Service’ Business Service
Using ‘PRM ANI Utilities’ Business Service
Using ‘EAI Data Transformation Engine’ Business Service.

Question 370. If I Do A Null Query Using A Siebel Operation Step On Action Bc In A Workflow, What Will Be Stored In 'siebel Operation Object Id' ?

Answer :

First Record of Actioin BC
* (a star character)

Question 371. Which Siebel Tools Objects Can Be Published As Web Services?

Answer :

Business Services and Workflows Both
Business Services Only
Workflow Only

Question 372. What Is Eai?

Answer :

EAI is a integration method for integrating the applications within your organization. There is another kind of integration called B2B. It is of two forms i.e Extended enterprise EE and market B2B.

There are different categories of EAI i.e Data level oriented, Application level oriented, Method oriented, portal oriented and process oriented.

Question 373. What Is Eim?

Answer :

EIM is a server task that manages exchange of data between external data in interface tables and user data in base tables.

Question 374. What Is User Data?

Answer :

User data only managed and populated by you. Installation populates seed data and repository data.

Question 375. What Is The Difference Between Eim And Eai?

Answer :

EIM: It is batch mode Integration. When data volume is large then we have to go to EIM.
EAI: It is real time Integration. When data volume is small then we have to go to EAI.

Question 376. How Many Type Of Siebel Data Model Extensions Are There?

Answer :

Standard and Custom extensions

Question 377. What Is Archiving?

Answer :

EIM Deletes are useful for archiving old data and deleting obsolete data. During delete processing the deleted rows are written to interface tables from which they can be archived in a format allowing easy re impact if necessary.

Question 378. Where The User Data Is Stored?

Answer :

The User data is stored in one or more base tables in the Siebel database. Relationship between the base tables relay upon PK & FK based on row ids.
-ROW_ID is the system primary key for every base table.
-ROW_ID is the system-generated value.

Question 379. What Are Interface Tables?

Answer :

Interface tables store external data inside the Siebel database.
These tables are:
Staging area for data to be imported, updated merged in to base tables via EIM.
Staging area for data exported by EIM.
Staging area for data to be deleted in the base table using EIM’s DELETE EXACT CLAUSE.

Question 380. What Is Data Cleansing?

Answer :

During imports, EIM attempts to import data from the interface table to the base table. It is important to note that if the data loaded in the interface table is faulty, it will remain faulty in the base tables. EIM Does not perform data cleansing.

Question 381. What Is Data Mapping?

Answer :

Data Mapping determines
–Which Siebel base table columns will store external source data
–Which interface table columns will be used to import from source to destination.

Question 382. What Is User Key?

Answer :

PK&FK based on ROW_ID are used for system wide referential integrity. Based on multiple columns user keys are used to uniquely identify a row for EIM.

Question 383. Can We Have Multiple Metaoutlines Based On One Olap Model In Integration Services?

Answer :

Yes

Question 384. What Are Lro's( Linked Reporting Objects)?

Answer :

They are specific objects like files, cell notes or URL's associated with specific data cells of Essbase database. You can link multiple objects to a single data cell. These linked objects are stored in the server. These LRO's can be exported or imported with the database for backup and migration activities.

Question 385. What Are The Three Primary Build Methods For Building Dimensions?

Answer :

1. Generation references
2. Level references
3. Parent-Child references

Question 386. How Does Uda's Impact Database Size?

Answer :

There will be no impact on the database as the UDA’s doesn’t store data in the database.

Question 387. Can We Have An Metaoutline Based On Two Different Olap Models.

Answer :

No.

Question 388. Can We Create Uda's And Apply It To Dense As Well As Sparse Dimensions?

Answer :

Yes

Question 389. Types Of Partitions Available In Essbase?

Answer :

Three types of partitions are there.
1. Transparent partition: A form of shared partition that provides the ability to access and manipulate remote data transparently as though it is part of your local database. The remote data is retrieved from the data source each time you request it. Any updates made to the data are written back to the data source and become immediately accessible to both local data target users and transparent data source users.
2. Replicated Partition:
3. Linked Partition:

Question 390. What Is Hybrid Analysis?

Answer :

Lower level members and associated data remains in relational database where as upper level members and associated data resides in Essbase database.

Question 391. Why Top-down Calculation Less Efficient Than A Bottom-up Calculation?being Less Efficient, Why Do We Use Them.

Answer :

In the process it calculates more blocks than is necessary. Sometimes it is necessary to perform top-down calculation to get the correct calculation results.

Question 392. On What Basis You Will Decide To Invoke A Serial Or Parellel Calculation Method.

Answer :

If we have a single processor, we will use serial calculation but if we have multiple processors we can break the task into threads and make them run on different processors.

Question 393. How Can You Display Uda's In Reports?

Answer :

UDA's values are never displayed in the reports and hence do not impact report performance.

Question 394. While Loading The Data, You Have Applied Both The Selection Criteria As Well As Rejection Criteria To A Same Record. What Will Be The Outcome?

Answer :

The record will be rejected.

Question 395. What Are The Specified Roles Other Than Aministrator To View Sessions, Disconnect Sessions Or Kill Users Requests For A Particular Application?

Answer :

You should have the role of Application manager for the specified application.

Question 396. What Is Block Locking System?

Answer :

Analytic services(or Essbase Services) locks the block and all other blocks which contain the childs of that block while calculating this block is block locking system.

Question 397. What Are The Three Options Specified In Username And Password Management Under Security Tab In Essbase Server Proprties.

Answer :

1. Login attempts allowed before username is disabled.
2. Number of inactive days before username is diabled.
3. Number of days before user must change password.

Question 398. Can We Have Multiple Databases In One Single Application?

Answer :

Yes. But only one database per application is recommended.
Depend on which database that you are going to create. For Example: If you are creating ASO then we can’t create more that 1 db per application. If you are creating BSO then you can create more than 1 db per application.

Question 399. How Is Data Stored In The Essbase Database?

Answer :

Essbase is an file based database where the data is stored in PAG files of 2 GB each and grows sequentially.

Question 400. We Have Created An Application As Unicode Mode. Can We Change It Later To Non-unicode Mode.

Answer :

No

Question 401. What Are The Types Of Partitioning Options Available In Essbase?

Answer :

1. Replicated partition. 2. Transparent partition 3. Linked partition.

Question 402. Dynamic Calc Decreases The Retreival Time And Increases Batch Database Calculation Time. How True Is The Statement?

Answer :

The statement should be just opposite. As dynamic calc members are calculated when requested, the retreival time should increase.

Question 403. What Is The Role Of Provider Services.

Answer :

To communicate between Essbase and Microsoft office tools.

Question 404. A Customer Wants To Run Two Instances Of An Essbase Server On A Same Machine To Have Both Test Environment And Development Environment On The Same Server. Can He Do That?

Answer :

Yes. We can have multiple instances of an Essbase server on a single machine and there will be different sets of windows services for all these instances.

Question 405. Why Top-down Calculation Less Efficient Than A Bottom-up Calculation?being Less Efficient, Why Do We Use Them?

Answer :

In the process it calculates more blocks than is necessary. Sometimes it is necessary to perform top-down calculation to get the correct calculation reset.

Question 406. What Are The Different Types Of Log Files?

Answer :

So many log files are there in essbase, but the important log files are
1. Application log
2. Essbase.log
3. Configtool.log
4. eas_install.log
5. essbaseserver-install.log

Question 407. Suppose We Have Assigned Generation 2 And Generation 4 As Of Now And Think Of Adding Generation 3 Later Some Time. Can We Build The Dimension.

Answer :

No. If gen 2 and gen 4 exists, we must assign gen 3.

Question 408. What Are Attributes?

Answer :

A classification of a member in a dimension. You can select and group members based on their associated attributes. You can also specify an attribute when you perform calculations and use calculation functions. Eg: The database in Sample Basic which has product dimension has some attributes like size, package type, and flavor. We can add these attributes to the dimensions where we can retrieve the data like for example to retrieve “coke with 8 Oz with bottles”, this is useful for generating reports.

Question 409. Why Do Objects Gets Locked And When Does This Happens?

Answer :

Objects gets locked to prevent users to make simultaneous and conflicting changes to Essbase database objects. By default whenever an object is accessed through Aministrative services console or Excel spreadsheet add-in, it gets locked.

Question 410. What Is The Difference Between Uda's And Attribute Dimensions?

Answer :

Attribute dimensions provides more flexibility than UDA's. Attribute calculations dimensions which include five members with the default names sum, count, min, max and avg are automatically created for the attribute dimensions and are calculate dynamically.

Question 411. How Does Attribute Dimensions And Uda's Impact Batch Calculation Performance?

Answer :

UDA's- No Impact as they do not perform any inherent calculations.
Attribute dim- No Impact as they perform only dynamic calculations.

Question 412. What Are Different Types Of Attributes?

Answer :

Essbase supports two different types of attributes.
1. User-Defined attributes
2. Simple attributes
   User-Defined attributes: The attributes that are defined by the user.
   Simple attributes: Essbase supports some attributes, they are: Boolean, date, number, and string.

Question 413. What Are Filters?

Answer :

A method of controlling access to database cells in essbase. A filter is the most detailed level of security, allowing you to define varying access levels different users can have to individual database values.

Question 414. What Is Tb First And Tb Last?

Answer :

TB First: in the Sample.Basic database, the accounts member Opening Inventory is tagged as TB First. Opening Inventory consolidates the value of the first month in each quarter and uses that value for that month’s parent. For example, the value for Qtr1 is the same as the value for Jan.

TB Last: in the Sample.Basic database, the accounts member Ending Inventory is tagged as TB Last. Ending Inventory consolidates the value for the last month in each quarter and uses that value for that month’s parent. For example, the value for Qtr1 is the same as the value for Mar.

Question 415. How Can We Display Uda's In Reports? How Do They Impact Report Report Performance?

Answer :

UDA's values are never displayed in the reports and hence do not impact report performance.

Question 416. How Does Attribute Dim Impact Report Performance?

Answer :

They highly impact the report performance as the attributes are calculated dynamically when referenced in the report. For very large number of att dim displayed in the report, the performance could drastically reduce.

Question 417. What Are The File Extensions For An Outline, Rule File And A Calc Script.

Answer :

OTL, .RUL and .CSC

Question 418. What Is Data File Cache?

Answer :

A buffer in memory that holds compressed data (.PAG) files.

Question 419. What Is Custom Defined Function?

Answer :

Essbase calculation functions that you develop in the Java programming language and then add to the standard Essbase calculation scripting language by means of MaxL.

Question 420. What Is Tibco?

Answer :

Tibco is an organization which provides Intergration software to software industry.

Question 421. What Are The Different Modes Of Service Invocation In Tibco?

Answer :

Services can be invoked in several ways.
• A one-way operation is executed once and does not wait for a response.
• A request-response oriented operation, in which client needs to wait the response. In a request-response service,communication flows in both directions.

Question 422. What Are The Tibco Bw Activities That Can Participate In Transactions?

Answer :

There are some specific TIBCO BW activities are supported in transaction not all.
• JDBC activities
• EJB activities
• JMS activities
• ActiveEnterprise Adapter activities that use JMS transports
• TIBCO iProcess BusinessWorks Connector activities.

Question 423. What Are The Modes Of Tibco Bw Installations ?

Answer :

• GUI mode
• Console mode
• Silent mode

Question 424. If You Have Installed A Particular Version Of Tibco Software E.g. Tibco Bw X.y.z, What Are X, Y And Z Number Stands For?

Answer :

Integration can be at different application layers:
• X:Patch
• Y:Major
• Z:Minor

Question 425. What Is The Role Of Tra?

Answer :

TRA stands for TIBCO Runtime Agent.
The TRA has two main functions:
• Supplies an agent that is running in the background on each machine.
1. The agent is responsible for starting and stopping processes that run on a machine according to the deployment information.
2. The agent monitors the machine. That information is then visible via TIBCO Administrator.
   • Supplies the run-time environment, that is, all shared libraries including third-party libraries.

Question 426. What Are The Revision Control System Options Available In Tibco Designer?

Answer :

• File sharing
• VSS
• Perforce
• XML Canon
• ClearCase
• iPlanet
• CVS
• PVCS

Question 427. What Are The Different Modes Of Service Invocation?

Answer :

Services can be invoked in several ways.
• A one-way operation is executed once and does not wait for a response.
• A request-response operation is executed once and waits for one response. In a request-response service, communication flows in both directions. The complete interaction consists of two point-to-point messages—a request and a response. The interaction is only considered complete after the response has arrived.
• Publication (notification) means an operation sends information on an as-needed basis, potentially multiple times.
• Subscription means incoming information is processed on an as-needed basis, potentially multiple times.

Question 428. What Is Vcrepo.dat?

Answer :

TIBCO Designer creates a file named vcrepo.dat in the project root directory when you first save the project. This file is used to store properties such as display name, TIBCO Rendezvous encoding, and description. This file can be used for identification in place of the project root directory and can be used as the repository locator string (repoUrl).

Question 429. What Are The Different Types Of Transactions Tibco Provides?

Answer :

TIBCO BusinessWorks offers a variety of types of transactions that can be used in different situations. You can use the type of transaction that suits the needs of your integration project. When you create a transaction group, you must specify the type of transaction. TIBCO BusinessWorks supports the following types of transactions:
• JDBC
• Java Transaction API (JTA) UserTransaction
• XA Transaction.

Question 430. What Activities Are Supported In Jta Transaction?

Answer :

The Java Transaction API (JTA) UserTransaction type allows:
• JDBC
• JMS
• ActiveEnterprise Adapter (using JMS transports)
• EJB activities
to participate in transactions.

Question 431. What Activities Are Supported In Xa Transaction ?

Answer :

The XA Transaction type allows:
• JDBC activities
• ActiveEnterprise Adapter activities that use the JMS transport
• JMS activities

Question 432. What Are The Possible Error Output's Of Read File Activity?

Answer :

Integration can be at different application layers:
• FileNotFoundException :Thrown when yhe file does not exist.
• UnsupportedEncodingException:Thrown when the text file’s encoding is not valid and the content of the file is read into process data.
• FileIOException :Thrown when an I/O exception occurred when trying to read the file.

Question 433. What Is The Purpose Of The Inspector Activity ?

Answer :

The Inspector activity is used to write the output of any or all activities and process variables to a file and/or stdout. This is particularly useful when debugging process definitions and you wish to see the entire schema instead of mapping specific elements to the Write File activity.

Question 434. What Are The Maximum/minimum Of Threads Available For Incoming Http ?

Answer :

The maximum/minimum of threads available for incoming HTTP : 75/10.

Question 435. How Can Unauthorized Users Be Prevented From Triggering A Process ?

Answer :

Unauthorized users be prevented from triggering a process by giving 'write' access for the process engine to only selected users. Only users with 'write' access can do activities like deploying applications, starting/stopping process engines etc.

Question 436. What Are The Mandatory Configuration Parameters For Ftp Connection & Ftp With Firewall ?

Answer :

The mandatory configuration parameters for FTP Connection
• FTP host
• Port
• Username & Password
If Firewall is enabled in addition the proxy host and port are required.

Question 437. How To Design A Process Such That Depending On Number Of Records Updated In A Database, 3 Different Sub-processes May Be Called ?

Answer :

Define 3 transitions from JDBC update with condition on the no of updates and call appropriate child processes.

Question 438. How To Use Legacy .dat File Format With Latest Designer ?

Answer :

Convert .dat file to multi file project using Administration tab while starting up Designer(Other one being Project tab) and then open the multifile project in the normal way.

Question 439. What Are The Encodings Supported By Designer ?

Answer :

Encodings supported by designer are
• ISO8859-1(Latin-1)
• UTF-8

Question 440. What Are The 4 Main Panels Of The Designer Window ?

Answer :

The 4 main panels of the Designer window are
• Project panel
• Palette panel
• Design panel
• Configuration panel.

Question 441. How Do You Determine If There Are Broken References In The Project?

Answer :

Project -> Validate for deployment

Question 442. Where Are The Designer Preferences Stored ?

Answer :

Designer preferences stored are stores in a file called 'Designer .prefs' in the user home directory.

Question 443. Explain The Process Configuration Parameters - Max Jobs, Flow Limit & Activation Limit ?

Answer :

• Max Jobs :
Max Jobs specifies the number of process instances that are kept in memmory. Once this limit is reached newly created process instances (subject to flow limit) are paged out to disk.0 specifies no limit and is the default.

• Flow Limit :
Flow Limit specifies the maximum number of running process instances that are spawned before the process starter is suspended ie it enters a FLOW_CONTROLLED state and does not accept new events. This can be used to control the number of process instances running simultaneously and when the protocol generating the event can store the event till it is received, like email servers, JMS, RV etc. 0 specifies no limit and is the default.

• Activation Limit :
Activation limit flag specifies that once a process instance is loaded it must be placed in memmory till it completes execution. By default it is enabled.

Question 444. What Are The Options For Configuring Storage For Process Engine's Checkpoint Repository ?

Answer :

The options for configuring storage for process engine's checkpoint repository are:
• Local File
• Database. Fault tolerant engines can recover from a checkpoint only when database is used.

Question 445. Process Engines In A Fault Tolerant Group Can Be Configured As Peers Or Master Secondary.how Do These Differ ?

Answer :

The options for configuring storage for process engine's checkpoint repository are:
•  Peer means all of them have the same weight. In this case when one engine fails another one takes over and continues processing till it fails.
•  In master secondary configuration weights are unequal, the secondary starts processing when master fails. But when master recovers, secondary stops and master continues processing.

Question 446. What Are The Uses Of Grouping Activities ?

Answer :

Uses of grouping activities are:
• Create a set of activities having a common error transition.
• Repeat group of activities based on a condition.
1. Iterate over a list.
2. Repeat until condition true.
3. Repeat on Error until condition true.
   • Group activities into a transaction.
   • To create a critical section area that synchronizes process instances.
   • A 'Pick First Group' allows you to wait for the occurence of multiple events and proceed along a path following the first event to occur.

Question 447. What Is The Purpose Of A Lock Shared Configuration Resource?

Answer :

A Lock is specified for a 'Critical Section' group when the scope is 'Multiple'. It can be used to ensure synchronization across process instances belonging to multiple processs definitions or for process instances across engines(Check multi engine flag for lock in this case and the BW engine needs to be configured with database persistence while deployment). If synchronization is for process instances belonging to the same processs definition inside one engine, just specify the scope as 'Single'.

Question 448. How To Control The Sequence Of Execution Of Process Instances Created By A Process Starter ?

Answer :

Use the sequencing key field in the Misc tab of any process starter. Process instances with the same value for this field are executed in the sequence in which they are started.

Question 449. Can There Be Two Error Transitions Out Of An Activity ?

Answer :

No. There can be only one Error and one Success if no matching condition transition out of each activity.

Question 450. When Is A 'no Action' Group Used ?

Answer :

'No Action' group used to have a set of activities having a common error transition

Question 451. What Activity Can Be Used To Set The Value Of A 'user Defined Process Variable' ?

Answer :

The 'Assign' activity can be used to set the value of a 'User defined process variable'.

Question 452. Which Are The Two Process Variables Available To All Activities With Inputs ?

Answer :

• $_globalVariables
• $_processContext

Question 453. Which Mechanism Can Be Used To Pass Data Between A Process Instance And A Called Sub Process Other Than Mapping From/to The Callee's Input/output ?

Answer :

This can be accomplished using job shared variables, unless in the call process activity the 'Spawn' flag is enabled in which case the called sub process is a new job and hence gets a fresh copy of the job shared variable initialized as per its configuration. A shared variable can overcome this limitation as it's scope is not limited to one job.

Question 454. What Are The Three Scenarios Where Bw Engine Has To Be Configured With Database Persistence Instead Of Local File ?

Answer :

The three scenarios are:
• Shared Variables across BW engines.
• Locking across groups in multiple BW engines.
• Wait Notify across BW engines.

Question 455. If You Want A Group To Be Executed If There Is Some Unhandled Error But Subject To Some Max Number Of Iterations Which Group Do You Use ?

Answer :

We can use Repeat on Error until true.

Question 456. When Is A 'generate Error' Activity Useful?

Answer :

When you handle an error inside a called subprocess or group and want to rethrow the error to the caller (happens by default if you dont handle the error in the called process)

Question 457. Which Activity Is Used For Detecting Duplicate Message Processing?

Answer :

CheckPoint activity - Specify the uniqueID for the duplicate key field and engine maintains list of these key fields. When a process come to checkpoint activity with the same value for duplicate key which already exists, it throws a DuplicateException. An error transition can then handle this case.

Question 458. Give An Example Where Graceful Migration Of Service From One Machine To Another Is Not Possible.

Answer :

HTTP Receiver. In this case the receiver on new machine starts listening on the same port, but you need to redirect requests from the old machine to the new one.

Question 459. What Are The Types Of Adapter Services ?

Answer :

Types of adapter services are :
• Subscriber Service
• Publisher Service
• Request-Response Service
• Request-Response Invocation Service .

Question 460. If The Business Process Needs To Invoke Another Web Service Which Resource Do You Use ?

Answer :

SOAP request reply activity. If the business process needs to be exposed as SOAP service use SOAP Event Source in conjunction with SOAP Send Reply or SOAP Send Fault.

Question 461. What Is The Scope Of User Defined Process Variables ?

Answer :

The scope of user defined process variables is only the process in which it is defined.(Not even inside a sub process that is invoked from this process)

Question 462. What Is Difference Between Shared Variable And Job Shared Variable ?

Answer :

• Both of them can be manipulated via the palette resources 'Get shared variable' and 'Set shared variable'.
• A job shared variable is private to one instance of job or in other words each job has a fresh copy. In the case of shared variable the same copy is shared across all job instances. It can even be persisted and can survive BW engine restarts and even shared across multiple BW engines(when deployed using DB persistence).

Question 463. How Do Wait-notify Resources Work ?

Answer :

Basically wait and notify should share a common notification configuration which is just a schema definition for data that will be passed from notifier to waiter. Specific instances of waiter & notifier are corrrelated via a key.
For example: when one process is in wait state for key 'Order-1', it waits till another process issues a notification with the same key value.

Question 464. What Is The Default Axis In Xpath ?

Answer :

Child axis- What this means is that when you select "BOOK" from the current context, it selects a child node with that name, not a sibling with that name. Other axes are parent , self , sibling etc.

Question 465. What Are The Output Formats For Xslt?

Answer :

• XML
• HTML
• Text

Question 466. What Is The Purpose Of $_error Variable ?

Answer :

$_error variable is available in the node following the error transition. It captures the error message, error code etc.

Question 467. What Are The Cases Where Business Process Cant Proceed Correctly Subsequent To Restart From A Checkpoint ?

Answer :

• Sending HTTP response, confirming an email/jms message etc. This is because the confirmation or sending HTTP response has to done in the same session. When engine crashes these sessions are closed at their socket level. In such cases send response/confirm before checkpoint.

Question 468. Which Group Do You Use To Wait For Multiple Events And Proceed With The First To Occur ?

Answer :

'Pick First Group'.

Question 469. What Is Rolap And Molap? Is Microstrategy A Rolap Or Molap Tool?

Answer :

ROLAP (Relational online Analytical Processing) tools do not use pre-calculated data cubes. Instead, they intercept the query and pose the question to the standard relational database and its tables in order to bring back the data required to answer the question.

MOLAP (Multidimensional online Analytical Processing) tools utilize a pre-calculated data set, commonly referred to as a data cube, that contains all the possible answers to a given range of questions.

MicroStartegy is ROLAP tool.

Question 470. What Is Star Schema And Snowflake Schema?

Answer :

Star Schema is a highly denormalized schema whereas snowflake schema is hight normalized schema.Star schema is characterized by large number of rows in a table and less number of joins between tables.Snowflake schema is characterized by less number of rows in a table while more number of joins between tables.

Question 471. What Are The Advantages And Disadvantages Of Star And Snowflake Schema?

Answer :

Star Schema Advantages: Reduces the number of joins between the tables and hence faster performance.

Star Schema Disadvantages:Requires Most amount of storage space.

Snowflake Schema Advantages: Minimum storage space and minimum data redundancy.

Snowflake Schema Disadvantages:Requires more joins to get information from look up tables hence slow performance.

Question 472. What Is The Difference Between 2 Tier,3 Tier And 4 Tier Architecture In Microstrategy?

Answer :

In 2 tier architecture, the MicroStrategy Desktop itself queries aganist the Data warehoue and the Metadata with out the Intermediate tier of the Intelligence server.

The 3 Tier architecture comprises a Intelligence server between MicroStrategy Desktop and the data Warehouse and the Metadata.

The 4 tier architecture is same as 3 tier except it has a additional component of MicroStratey Web.

Question 473. What Are Adhoc Reports And Static Reports?

Answer :

Adhoc reports run in real time based on the input parameters provided by the user at the run time.In Microstrategy, adhoc reports are created using Prompts.

In static reports, users won't be provide any input parameters.These reports are usaully schedule to run overnight and ready to view immediatley in the mornings using cache.

Question 474. What Is A Filter?

Answer :

Filter is a public object.It is used to restrict the data retrived by the report from the database tables.From SQL perspective it corresponds to the "WHERE" Clause.

Question 475. What Are Vldb Properties?

Answer :

Using VLDB properties we can change the way how the SQL is generated.Some of them are below:
Perform full outer joins
Check for Zeros and Nulls in the denominator while performing divisions in Metrics.
Creating Sub queries
Creating temperory tables.

Question 476. What Are Consolidations?

Answer :

Consloidations enable to group together attibute elements and create a virtual attribute.They perform Row level maths.

Question 477. What Are Custom Groups?

Answer :

Custom groups are used to create different filters to different rows of a report.For example, a report can created to display top 5 customers as well as bottom 5 customers in the one report using custom group.

Question 478. What Are Passthrough Functions?

Answer :

Pass through functions are used to utilize various special functions that specific to databases.Some of the passthrough functions available are Applysimple and Applycomparision.

Question 479. What Is A Security Filter?

Answer :

Security filter is used to apply security at the database data level.Whenever a users associated with security filter runs a report, a WHERE clause is always included in the report sql with the condition defined in the Security Filter.

Question 480. What Functionality Is Contained In Microstrategy Administrator - Object Manager 7.x And 8.0.x?

Answer :

MicroStrategy Administrator - Object Manager allows users to perform the following actions:
• Duplicate and upgrade projects
• Copy objects within and across related projects
• Move objects within a project
• Delete objects within a project
• Rename objects within a project
• Search for objects within a project
• Find an object's parents or children within a project.

Question 481. Are There Any Special Requirements Needed To Move Objects Across Projects?

Answer :

Yes. In order to perform cross-project operations, the projects involved must originate from the same source project. In other words, the projects can only be related by the duplication of a single project. This ensures that the projects have a similar set of schema and application objects, and that the object ID's in the two projects are the same. MicroStrategy Object Manager uses the object and version ID's across the projects to perform comparisons. MicroStrategy Object Manager prevents the user from attempting operations across unrelated projects.

Question 482. How Does Microstrategy Object Manager Determine If Two Projects Are Related?

Answer :

MicroStrategy Object Manager compares the Schema ID's of the two projects. Duplicated projects have different Project ID's, but their Schema ID's are the same.

Question 483. What Happens If A User Tries To Move Objects Between Two Unrelated Projects?

Answer :

If a user tries to perform cross-project operations between two unrelated projects, MicroStrategy Object Manager will not permit the operation and will display the following error:

Objects cannot be copied across the projects because these two projects, "Project name of the source" and "Project name of the destination", have not been created from the same source.

Question 484. What Is The Conflict Resolution Window?

Answer :

The Conflict Resolution window provides the user with a means to decide how to handle object conflicts between the source project and the destination project. In addition, the Conflict Resolution window displays the object name in the original project, the object name in the destination project and the type of conflict. Users may also specify a new name for the object depending on the action choosen.

Question 485. How Does Microstrategy Object Manager Determine If Two Objects In Different Projects Are The Same?

Answer :

To determine if two objects are the same, MicroStrategy Object Manager compares their Object ID's. If these ID's are the same, MicroStrategy Object Manager then compares the Version ID's. If the Version ID's are the same, the Conflict Resolution grid lists the conflict as 'Exists Identically.' If the Version ID's are different, the Conflict Resolution grid lists the conflict as 'Exists Differently.'

Question 486. How Can The User Determine The Object Id Of An Object?

Answer :

To view the Object ID of an object, right-mouse click on the object and select 'Properties.' The Object ID and Version ID are listed on the 'General' tab.

Question 487. Why Does Microstrategy Object Manager Search For Object Dependencies?

Answer :

MicroStrategy Object Manager makes a list of all object dependencies before copying an object to prevent metadata inconsistency. The time required for dependency checking varies based on a customer's metadata size and schema complexity. For large metadata and complex schemas, gathering all the dependencies may take a long time.

Question 488. Can Schema Objects Be Copied Across Projects With Microstrategy Object Manager?

Answer :

Yes, schema objects can be copied across projects using MicroStrategy Object Manager. MicroStrategy Object Manager moves objects seamlessly between similar projects such as from a development project version to a production project version where the warehouses are the same in terms of views, prefixes, and warehouse structure. However, subtle changes in the warehouse that relate to prefixes, views, or table structure cannot be tracked by MicroStrategy Object Manager. For situations where the projects' warehouse structures or setups are dissimilar, users may be required to make further edits of the objects to ensure full integration into the destination project. These edits may include hierarchical relationship changes or modifications to the prefixes.

Question 489. How Does Microstrategy Object Manager Integrate With The Microstrategy Product Suite Security Model?

Answer :

Security in MicroStrategy Object Manager is based on the MicroStrategy 7.x Product Suite security model. All activities that can be performed in MicroStrategy Object Manager are governed by privileges and access control lists. For example, if a user is not allowed to access a certain folder in MicroStrategy Agent, they will not be able to access the folder in MicroStrategy Object Manager.

Question 490. Is It Possible To Use Microstrategy Object Manager While Other Users Are Making Changes In Microstrategy Agent?

Answer :

Using MicroStrategy Object Manager to copy/move objects around is not recommended while other user sessions are making changes using MicroStrategy Agent, as it could lead to metadata inconsistency. Project and schema locking prevent multiple users sessions from manipulating the schema at the same time. This prevents metadata inconsistency from occurring.

Question 491. What Are The Tracing Options Available In Microstrategy Object Manager?

Answer :

Tracing is available under the Tools/Diagnostics menu. These tracing options apply to every MicroStrategy product installed on the machine.

To see the SQL that has been executed against the metadata, go to the Advanced tab and turn on 'SQL Tracing' under the DSS MDServer key.

Function level tracing can be accomplished by going to the Advanced tab and turning on 'Function Level Tracing' under the DSS ObjectManager key.

Question 492. Where Are Dependent Objects Copied If They Do Not Already Exist In The Destination Project?

Answer :

If the location exists in the destination project, the dependent object is copied to that location. If the location does not exist in the destination project, a new folder entitled 'Dependencies' is created and the object is copied to that folder.

Question 493. What Happens If The Owner Of An Object Does Not Exist In The Destination Project?

Answer :

If the owner of the source object does not exist in the destination project, the user login for the destination project takes ownership of the object when it is copied or replaced.

Question 494. Where Can Users Find More Information On Microstrategy Object Manager?

Answer :

Further information can be found in the release notes, as well as in MicroStrategy Object Manager's online help.

Question 495. How Long Does It Take To Get Microstrategy Desktop Up And Running?

Answer :

Microstrategy Desktop installs in minutes and automatically presents a list of available Microstrategy Intelligence Servers. Within an hour, the installation and setup are completed.

Question 496. How Does Microstrategy Desktop Integrate With The Rest Of The Microstrategy Platform?

Answer :

Microstrategy Desktop is the intuitive client-server interface used by business analysts and application developers. Microstrategy Desktop interacts with the Intelligence Server to build metrics, create and format reports, and retrieve timely, accurate information to the desktop to enhance the decision-making process.

Question 497. What Security Is Provided With Microstrategy Desktop?

Answer :

Microstrategy Desktop provides a host of security options to ensure that data is kept confidential and private. To facilitate easy deployment and minimal maintenance, Microstrategy Desktop integrates with Windows NT and 2000 security and with Novell directory. As a result, users who have logged into these systems will not need to log on again.

Question 498. To What Extend Can Microstrategy Desktop Be Personalized?

Answer :

Each Microstrategy Desktop user has a security profile defined by their administrator. This profile controls access to application functionality, specific reports or particular data for individual users or groups of users. The Desktop interface will adapt and display only what this user is allowed to see.

Question 499. Is The Microstrategy Mdx Engine Certified By Sap?

Answer :

Yes. This new Dynamic MDX Engine generates optimized MDX syntax that is fully certified with SAP BW using SAP's high performance BAPI interfaces.

Question 500. Can Users Join Data Across Sap Bw Info Cubes And Query Cubes?

Answer :

Yes. Users can use Microstrategy Desktop to create reports that access SAP data and join data across SAP BW Info Cubes and Query Cubes as well as access multiple instances of SAP BW at once.

Question 501. Can Microstrategy Desktop Join Data Across Heterogeneous Data Sources?

Answer :

Yes. Microstrategy 8 extends the Microstrategy data modeling flexibility to include integrated views of data across heterogeneous data stores. By mapping conforming dimensions from different sources, Microstrategy Desktop can automatically join data from multiple different sources in the same report document. Data can come from any source accessible by Microstrategy 8, including the data warehouse, data marts, SAP BW, and any number of operational system databases.

Question 502. Does Microstrategy Provide Predictive Modeling Capabilities Commonly Available In Data Mining Tools?

Answer :

Yes. Microstrategy 8 can calculate four of the primary data mining functions including neural network algorithms, clustering algorithms, regression algorithms, and tree algorithms.

Question 503. Can Microstrategy Incorporate Best-of-breed Data Mining Insight Into Mainstream Business Reports And Analysis?

Answer :

Yes. Microstrategy 8 has extended its analytic engine with "Data Mining Services" capability that allows reports and analyses to include predictive capabilities in every Microstrategy report or analysis. Microstrategy 8 includes the new ability to import data mining models directly from best-of-breed data mining products from vendors like IBM, Teradata, SAS, and SPSS using the new PMML or predictive modeling mark-up language standard.

Question 504. Can Microstrategy Desktop Export Data To Other Software Applications?

Answer :

You can export information from Microstrategy Desktop to text files, Microsoft Word, Microsoft Excel, Microsoft Access and HTML files. The formatting of the tables and data are preserved when you export to these file formats.

Question 505. What Data Sources Does Microstrategy Desktop Support?

Answer :

You can access data in all the major databases including Oracle, IBM DB2, Informix, NCR Teradata, Microsoft Access, Microsoft SQL Server, Red Brick, Sybase and Non-Stop SQL.

Question 506. To Save Time, Can Many Reports Be Run At The Same Time?

Answer :

Microstrategy Desktop can execute multiple reports simultaneously. Report results are saved in a personal History folder when ready.

Question 507. Can Reports Be Executed In Off-peak Periods?

Answer :

Reports can be attached to time-based or event-based schedules that are defined by the administrator. These schedules automatically trigger the report execution and place a notification message in the History folder on completion.

Question 508. What Is Microstrategy Olap Services?

Answer :

Microstrategy OLAP Services is an extension to Microstrategy Intelligence Server that allows Microstrategy Web and Desktop users to manipulate Intelligent Cubes™. With OLAP Services end users can add or remove report objects, add derived metrics and modify the filter -- all with speed-of-thought response time against Intelligent Cubes. OLAP Services enables full multi-dimensional OLAP analysis within Intelligent Cubes, while retaining users' ability to seamlessly drill through to the full breadth and depth of the data warehouse.

Question 509. What Are The Intelligent Cubes Used By Olap Services?

Answer :

Intelligent Cubes are user or administrator created multi-dimensional cubes that operate within Microstrategy Intelligence Server. On Microstrategy's BI platform, creating an Intelligent Cube is as easy as creating a report. Intelligent Cubes enable Microstrategy to combine the speed and interactivity of multi-dimensional OLAP analysis and the analytical power and depth of relational OLAP.

Question 510. What Is Microstrategy Desktop?

Answer :

Microstrategy Desktop is a Windows client-server software application that provides integrated monitoring, reporting, and analysis capabilities.

Question 511. What Does Microstrategy Desktop Allow Users To Do?

Answer :

Using Microstrategy Desktop, users can easily access and share critical corporate information they need to make cost-cutting decisions and improve business processes. The information found in databases can also be used to help increase revenue and boost profits. Users can access this database and SAP data without having to learn technical database query (SQL) or multi-dimensional expression (MDX) syntax.

Question 512. What Can Users Do With The Information They Access Using Microstrategy Desktop?

Answer :

Users can analyze the information using standard aggregations and more sophisticated functions such as average, summation, percentage contribution, standard deviation and net present value. Investigative reporting, using pivoting, sorting, slicing, and drilling to more detail, can be performed with simple mouse clicks. Users can also format reports to their specifications and view the data as intuitive charts and graphs to identify trends and anomalies quickly.

Question 513. What Are The Benefits Of Using Microstrategy Desktop?

Answer :

Users can obtain critical information immediately without waiting for IT departments to create reports. The software is easy to use and provides context sensitive help, thus eliminating the need for extensive support and maintenance staff.

Question 514. Are The Reports Created Using Microstrategy Desktop Available To Other Products Such As Microstrategy Web?

Answer :

Yes. Reports created using Microstrategy Desktop are immediately available to other Microstrategy products because of our centralized metadata architecture.

Question 515. Can Microstrategy Desktop Access Sap Data?

Answer :

Yes. With the release of Microstrategy 8, Microstrategy Desktop incorporates a new dynamic data access engine designed to access multi-dimensional databases (MDDBs or OLAP Cube Databases) such as those from SAP Business Information Warehouse (BW) databases.

Question 516. Can Microstrategy Desktop Access Operational Data Systems?

Answer :

Yes. Microstrategy Desktop users can use a new Operational SQL Engine to include data from any operational system using completely free-form SQL, including stored procedures and views.

Question 517. How Fast Is The Performance On Microstrategy Desktop?

Answer :

Microstrategy Desktop provides instant access and analysis of information. This high performance is enabled through Intelligence Cubes, caches, incremental fetches and advanced analytic features.

Question 518. How Long Does It Take To Learn Microstrategy Desktop?

Answer :

Microstrategy Desktop preserves the look and feel of popular desktop software such as Microsoft Windows Explorer and Microsoft Office. As such, users are immediately comfortable with Microstrategy Desktop. A customized interface using HTML can be created, simplifying navigation and report execution.

Question 519. Can I Make My Data And Graphs Look Professional?

Answer :

Yes. Users can format their data into appealing reports using various formatting styles and graphs for maximum visual impact. Users can choose from more than 30 different charting options to present information in the best layout possible.

Question 520. Is It Possible To Display Multiple Reports, Images And Information On The Same Page?

Answer :

Yes, users can easily combine tables, images, graphs and other information onto the same page in a document. Visually impressive and compelling documents can be printed out and shared with corporate executives. Business users can now rearrange the organization of any report with simple drag and drop actions or by clicking on the new toolbar icons to get entirely new views of the data, all from the same report and without requiring assistance from IT.

Question 521. What Printing Capabilities Are Available In Microstrategy Desktop?

Answer :

Microstrategy Desktop offers advanced printing capabilities. Features include repeating row /column headers, customizable headers and footers, and a comprehensive page setup menu. Users can preview reports before sending it to the printer.

Question 522. What Subtotaling Features Does Microstrategy Desktop Contain?

Answer :

Microstrategy Desktop has more than 10 different subtotaling functions that aid analysis of the data. Subtotals can be presented at any level in the rows, columns and pages on the report.

Question 523. What Are The Minimum Requirements For Microstrategy Desktop?

Answer :

Minimum requirements are a computer with at least a 450MHZ Pentium- compatible CPU, 256MB of RAM and 500MB of hard disk.

Question 524. Is Microstrategy Desktop Available In Other Languages?

Answer :

Microstrategy Desktop is available in English, French, German, Spanish, Korean, Italian, Swedish, Japanese and Portuguese.

Question 525. How Long Does It Take To Get Microstrategy Desktop Up And Running?

Answer :

Microstrategy Desktop installs in minutes and automatically presents a list of available Microstrategy Intelligence Servers. Within an hour, the installation and setup are completed.

Question 526. How Does The Microstrategy Narrowcast Server Support Enterprise Wide Mission Critical Applications?

Answer :

Microstrategy Narrowcast Server's world-class clustering and fail-over ensures support for mission-critical 24x7 systems. Rigorous in-house testing has proven that Narrowcast Server can personalize and deliver millions of messages a day. The system tracks fail-over down to each message.

Question 527. To Which Devices Can Microstrategy Narrowcast Server Deliver Information?

Answer :

Narrowcast Server can deliver information to email, mobile phones, pagers, faxes, PDAs, intranet and extranet web portals. Businesses can also build and plug in their own Information Transmission Module to support their own devices.

Question 528. What Formatting Can Be Applied To The Information That Is Sent Out By Microstrategy Narrowcast Server?

Answer :

Information can be formatted into HTML, plain text, Microsoft Excel, or PDF files. The size and display of these files are adjusted to suit the email type or the wireless device for different users.

Question 529. What Kinds Of Information Can Users Receive?

Answer :

Users can receive both tables and charts from the Microstrategy platform, and content from current information sources such as transaction processing systems, Enterprise Resource Planning systems, databases, XML files, and web servers.

Question 530. Can Users Turn Off The Information Delivery?

Answer :

Yes, users can switch on and off their own information delivery. Administrators can also set up some ‘non-optional’ information delivery so that everyone receives the information. As a result, users can obtain information without having to wait for IT to develop the reports.

Question 531. How Do Users Receive Only Information That They Want?

Answer :

Through an easy-to-use subscription web page, users specify what information they want. Some personalization options include the language choices and specific information criteria such as certain products. Using this user profile, Microstrategy Narrowcast Server sends only the information that the user has requested.

Question 532. How Do Current Microstrategy Narrowcast Server Customers Use Intelligent Alerting?

Answer :

Customers use Microstrategy Narrowcast Server to deliver inventory alerts, business performance alerts, supply chain alerts, customer activity alerts, stock and personal finance alerts, last minute travel alerts, data load alerts, customer account activity alerts, and fraud alerts. New uses are constantly being developed for intelligent alerting.

Question 533. Why Do Businesses Need To Send Information Out To Users Proactively?

Answer :

People do not have time to search through information to identify information that requires immediate action. An intelligent alerting system understands and constantly monitors the information users need, and delivers information only when users need it. Users save time and take action when required.

Question 534. How Did You Handle Reject Data?

Answer :

Typically a Reject-link is defined and the rejected data is loaded back into data warehouse. So Reject link has to be defined every Output link you wish to collect rejected data. Rejected data is typically bad data like duplicates of Primary keys or null-rows where data is expected.

Question 535. If Worked With Ds6.0 And Latest Versions What Are Link-partitioner And Link-collector Used For?

Answer :

Link Partitioner - Used for partitioning the data.
Link Collector - Used for collecting the partitioned data.

Question 536. What Are Routines And Where/how Are They Written And Have You Written Any Routines Before?

Answer :

Routines are stored in the Routines branch of the DataStage Repository, where you can create, view or edit. The following are different types of routines:
1) Transform functions
2) Before-after job subroutines
3) Job Control routines.

Question 537. What Are Oconv () And Iconv () Functions And Where Are They Used?

Answer :

IConv() - Converts a string to an internal storage format
OConv() - Converts an expression to an output format.

Question 538. How Did You Connect To Db2 In Your Last Project?

Answer :

Using DB2 ODBC drivers.

Question 539. Explain Metastage?

Answer :

MetaStage is used to handle the Metadata which will be very useful for data lineage and data analysis later on. Meta Data defines the type of data we are handling. This Data Definitions are stored in repository and can be accessed with the use of MetaStage.

Question 540. Do You Know About Integrity/quality Stage?

Answer :

Qulaity Stage can be integrated with DataStage, In Quality Stage we have many stages like investigate, match, survivorship like that so that we can do the Quality related works and we can integrate with datastage we need Quality stage plugin to achieve the task.

Question 541. Explain The Differences Between Oracle8i/9i?

Answer :

Oracle 8i does not support pseudo column sysdate but 9i supports
Oracle 8i we can create 256 columns in a table but in 9i we can upto 1000 columns(fields).

Question 542. How Do You Merge Two Files In Ds?

Answer :

Either use Copy command as a Before-job subroutine if the metadata of the 2 files are same or create a job to concatenate the 2 files into one if the metadata is different.

Question 543. What Is Ds Designer Used For?

Answer :

You use the Designer to build jobs by creating a visual design that models the flow and transformation of data from the data source through to the target warehouse. The Designer graphical interface lets you select stage icons, drop them onto the Designer work area, and add links.

Question 544. What Is Ds Administrator Used For?

Answer :

The Administrator enables you to set up DataStage users, control the purging of the Repository, and, if National Language Support (NLS) is enabled, install and manage maps and locales.

Question 545. What Is Ds Director Used For?

Answer :

datastage director is used to run the jobs and validate the jobs. we can go to datastage director from datastage designer it self.

Question 546. What Is Ds Manager Used For?

Answer :

The Manager is a graphical tool that enables you to view and manage the contents of the DataStage Repository.

Question 547. What Are Static Hash Files And Dynamic Hash Files?

Answer :

As the names itself suggest what they mean. In general we use Type-30 dynamic Hash files. The Data file has a default size of 2Gb and the overflow file is used if the data exceeds the 2GB size.

Question 548. What Is Hash File Stage And What Is It Used For?

Answer :

Used for Look-ups. It is like a reference table. It is also used in-place of ODBC, OCI tables for better performance.

Question 549. Have You Ever Involved In Updating The Ds Versions Like Ds 5.x, If So Tell Us Some The Steps You Have Taken In Doing So?

Answer :

Yes. The following are some of the steps; I have taken in doing so:
1) Definitely take a back up of the whole project(s) by exporting the project as a .dsx file.
2) See that you are using the same parent.

Question 550. How Many Jobs Have You Created In Your Last Project?

Answer :

100+ jobs for every 6 months if you are in Development, if you are in testing 40 jobs for every 6 months although it need not be the same number for everybody.

Question 551. What Are The Often Used Stages Or Stages You Worked With In Your Last Project?

Answer :

Transformer, ORAOCI8/9, ODBC, Link-Partitioner, Link-Collector, Hash, ODBC, Aggregator, Sort.

Question 552. How Did You Connect With Db2 In Your Last Project?

Answer :

Most of the times the data was sent to us in the form of flat files. The data is dumped and sent to us. In some cases were we need to connect to DB2 for look-ups as an instance then we used ODBC drive.

Question 553. Did You Parameterize The Job Or Hard-coded The Values In The Jobs?

Answer :

Always parameterized the job. Either the values are coming from Job Properties or from a ‘Parameter Manager’ – a third part tool. There is no way you will hard–code some parameters in your jobs.

Question 554. Explain Dimension Modelling Types Along With Their Significance?

Answer :

Data Modelling is Broadly classified into 2 types.

a) E-R Diagrams (Entity - Relatioships).
b) Dimensional Modelling.

Question 555. What Is Functionality Of Link Partitioner And Link Collector?

Answer :

Containers : Usage and Types?

Containers is a collection of stages used for the purpose of Reusability. There are 2 types of Containers.

a) Local Container: Job Specific
b) Shared Container: Used in any job within a project.

Question 556. Compare And Contrast Odbc And Plug-in Stages?

Answer :

ODBC :
a) Poor Performance.
b) Can be used for Variety of Databases.
c) Can handle Stored Procedures.
Plug-In: a) Good Performance. b) Database specific.(Only one database)

Question 557. Is It Possible To Calculate A Hash Total For An Ebcdic File And Have The Hash Total Stored As Ebcdic Using Datastage ?

Answer :

Currently, the total is converted to ASCII, even tho the individual records are stored as EBCDIC.

Question 558. How Did You Handle An 'aborted' Sequencer?

Answer :

In almost all cases we have to delete the data inserted by this from DB manually and fix the job and then run the job again.

Question 559. How Many Places You Can Call Routines?

Answer :

Four Places you can call

(i) Transform of routine

Date Transformation
Upstring Transformation
(ii) Transform of the Before & After Subroutines
(iii) XML transformation
(iv)Web base.

Question 560. What Does A Config File In Parallel Extender Consist Of?

Answer :

Config file consists of the following.

a) Number of Processes or Nodes.
b) Actual Disk Storage Location.

Question 561. What Is The Importance Of Surrogate Key In Data Warehousing?

Answer :

Surrogate Key is a Primary Key for a Dimension table. Most importance of using it is it is independent of underlying database. i.e Surrogate Key is not affected by the changes going on with a database.

Question 562. Name Some Of The Standard Business Intelligence Tools

Answer :

Some of the standard Business Intelligence tools in the market According to their performance
1)MICROSTRATEGY
2)BUSINESS OBJECTS,CRYSTAL REPORTS
3)COGNOS REPORT NET
4)MS-OLAP SERVICES.

Question 563. Why An Infocube Has Maximum Of 16dimensions?

Answer :

It depends upon the Database limits provided to define the Foreign key constraint, e.g. in Sql Server 2005, the recommended max limit for foreign keys is 253, but you can define more.

Question 564. What Is The Difference B/w Variable & Formula?

Answer :

Whenever we execute the formula , the result will be stored in the variable.

Question 565. What Is Ment By Incompatable Object Error In The Report Level?

Answer :

When the contexts are not properly defined we will get the error as incompaitable combination of objects.

Question 566. What Is Meant By For Each For All Function. In Which Case We Use The Option In Bo?

Answer :

for each-add all objects to the contex
for all-delete all objects from the context
we use forall for summary purpose and foreach for detail purpose.

Question 567. How We Improve The Performance Of Report And Universe?

Answer :

By creating the summary tables and using aggregate awareness.

Question 568. Which Is The Best Way To Resolve Loops? Context Or Alias?

Answer :

In a schema we have only one look loop u can create Alias. But, when we have multiple look up u can create contexts. most of the cases are using context can be use to resolve the loops. why because more number of complexity loops and also schema contains 2 or more fact tables in ur universe design. If there are more than one fact table use a context or if only one fact table use alias.

Question 569. What Are The Types Of Joins Universe Supports?

Answer :

Inner Join, outerjoin, left, right outer join, full outer Join.

Question 570. What Are The Universe Connection Types?

Answer :

Shared connection
Secured connection
Personal connection - used only stand alone system.

Question 571. What Are The Advantages Of Creating The Universe?

Answer :

The main fact behind creating universes is "Business users need not have strong SQL back ground. But sometimes they need to develop reports". In such case the importance of universe comes. The universe designer needs to have a strong SQL back ground and he/she will create universe which in turn has objects like dimensions, measures, etc,...

The business user then uses these objects just by dragging and dropping in the query editor pane. Dragging, dropping and running is more easy for him rather than writing SQL by his own.

Question 572. How Do U Drag 2 Sources From 2 Diff Data Providers, How We Take These 2 Sources Into 1 Single Report?

Answer :

By using data synchronization Option.... synchronization is the term used to describe the merging of data from multiple data sources into a single block in a report.

Question 573. How To Hide Rows & Columns In A Report ?

Answer :

hide the colomn ---

menu>formate>table formate>pivote>hide button, Rows can be hide only when the break is applied on a particular column using...

Format-->Breaks-->Fold.

Question 574. What Do U Mean By Merged Dimensions In B.o.?

Answer :

merged dimension is nothing but to synchronize the data from different data sources with a common dimension.

Web Intelligence allows you to synchronize multiple data providers in the same document. This allows you to build reports which synchronize data from multiple sources. When you synchronize queries through merging, you can include report objects from different queries in the same report block.

Question 575. What Is Full Path Client?

Answer :

Full path client is nothing but an info-view.

Question 576. How To Sort On A Particular Object, That Object Is Not Picked Up While Creating The Cross Tab But We Need To Sort On The Object That Is Not In The Cross Tab?

Answer :

Go to Format--Sorts then click on Add. We will get all the objects select the object and apply it which is not in the Cross tab report.

Question 577. How Can We Retrieve Particular Number Of Rows From Data Ware House? For Ex: My Report Wants To Display With 10 Records In A Report? How?

Answer :

We can do this in 2 levels in BO.
1. In Universe parameters, set the no of records for your requirements.
   But I will apply to all reports.
2. We can do this to a particular report in the query panel.
   Select OPTION button (Left side down placed) and set the no of records how many you want.

Question 578. What Is Custom Sorting?

Answer :

Custom sorting is nothing but sorting as per our requirement suppose months like
jan
feb
mar
apr
may
jun
jul
We can display first jan next mar next jun for these purpose we can use custom sort.

Question 579. What Is Metrics?

Answer :

A metric is the measure of actual performance. A metric is defined using objects in the universe. These are used to track trends and productivity.

Question 580. What Is Dashboards?

Answer :

Dashboards is nothing but collection of information.

Question 581. In Boxir2 Creating Universe By Using Designer And Business View. What Is The Difference B/t Two?

Answer :

Business view is used to create a lovs in crystal reports. This can be schedule to refresh to daily. business view can be used by only in crystal reports a universe can also be a source for crystal reports as well as web intelligence. in business view we can connect to multiple database and create a business view, it is not there in universe.

Question 582. How Many Universe Dfi You Create If You Have 2 Years Of Experience In Bo ?

Answer :

1. Two Universe
2. Depends on my data base and my project. example.in my project if i have 100 tables i will create 6 universe.
   Any way u have a two years of exp in bO .u dont have chance to create universe.we need min 5 to 6 + exp and good domain knowledge.

Question 583. How To Restrict Null Values In Webi Report?

Answer :

I believe you can define a formula like below
Not IsNull(object). This formula should bypass all records that has null values..There might be some other ways too..

Question 584. What Is Difference Between Folders And Category ?

Answer :

folders: folders and subfolders are used to organize documents
categories: categories are a way to classify your information
for example, you could place your financial reports and documents into a folder name finance and you could classify or tag your reports that deal with specific financial matters as payroll, accounts, payble and accounts receivable.

Question 585. How Do You Share The Universe?

Answer :

By moving it as a file through the file server and exporting it to the repository.

Question 586. How Do You Give Security To Universe?

Answer :

We can secure the universe by applying security restrictions through Universe Designer.
We can apply following types of security restrictions on different users:
1. Object Restriction
2. Row Level Restriction.
3. Table Mapping.
4. Connection Restriction.

Question 587. What Are Zero Client And Thin Client?

Answer :

Zero-client viewers do not require client-side software to be installed or downloaded. Instead these viewers display the reports as DHTML.

Thin Client Viewers require components to be downloaded and installed on the client‟s computers. These client viewers offers better report fidelity but can require more administrative overhead.

Question 588. What Is A Variable?

Answer :

a) Variables are used to prevent the same computation being performed several times as the variable allows you to store the values so that they can be used later.
b) A variable represents specific data or a value, and acts as a placeholder for that value. Unlike a constant value, which is fixed and unchanging, a variable can be repeatedly assigned different values. You assign a value to a variable and the variable maintains the value until you later assign a new value. Because of this flexibility, it is necessary for you to declare variables before you use them. Variables can be treated as a normal attribute, that is, it can be a source or target of a transform.

Question 589. How To Analyze "join"problem And Which Method Is The Best To Resolve That?

Answer :

Join problems are analyzed by Integrity checking and resolve by setting cardinalities.

Question 590. Say, The Query Gets Executed And We Got The Results. In Case If We Have A Large Number Of Rows, How Can We Know The Exact No Of Rows Returned?

Answer :

a) From the data manager tab we can know the no of rows returned and the time taken to run the report.
b) Click on any column in result set, right click and select count all. This will display the total number of columns in the result set.

Question 591. Is There Any Way To Know How Long The Report Executes And How Many Records Will Be Returned Before Hitting The "run" Option?

Answer :

a) Go to Definition tab in the data manager there u find these query options.
b) Before run a report just click on view button u can see the report.
c) Simple! Take the report query and modify to take the count in the query and execute it at the back end.

Question 592. How To Connect To A Server In A Business Objects?

Answer :

There are some third party software are there to connect like "CITRIX".

Question 593. How Do U Migrate Bo 6.x To Xi?

Answer :

There are 2ways to migrate 6.5 to xi.
1) Open migrate wizard. IMPORT WIZARD window appears. Import wizard is a tool to migrate reports, Universes, Repository objects to one environment to other environment with in XI and also from prior versions to XIR2 versions.
2) While using this option, Report Conversion tool.

Question 594. What Is The Computation Error? How To Solve It?

Answer :

The computation error is related to the misuse of context operators in formula.

Question 595. What Are The Degenerated Objects?

Answer :

Objects created using SQL queries or stored procedures called Degenerated Objects.

Question 596. What Is Input Level Context And Output Level Context In Webi?

Answer :

The input context determines what dimension to go into the calculations to produce the values. Whereas the out put context determines how the values are combined. It is generated by the cell location with the report.

Question 597. What Is Casual Dimension?

Answer :

Casual dimension is a dimension that should not change the fundamental grain of a fact table.
Ex: sex- Male, Female.

Question 598. What Is The Use Of Surrogate Key In Bo?

Answer :

a) Surrogate Key is a primary key in data warehousing, the only difference between surrogate key and primary key is that surrogate key allows duplicate values and primary key doesn‟t.
b) Surrogate key is the dummy key which is used to allow the duplicate values.
c) Surrogate key is contiguous numbers generated by DB in a table which acts as a primary key since surrogate key has unique values.
d). It is used for duplicate values in a database. Primary keys cannot be changed when a unique error occurs. With the help of this surrogate key a new column values will be created and that will be as primary keys.
e) Surrogate key is unique key which is used in type 2 dimension.

Question 599. What Is Maximum Scope Of Analysis --> Can We Define More Than 3 Levels?

Answer :

By default, you can do only up to 3 levels. But with custom, you can do more than 3 levels.

Question 600. Difference Between Scope Of Analysis In Webi And In Deski?

Answer :

In Deski: all the data for all objects will be retrieved from the database and that is stored in micro cube. Whenever you want to drill down for next level dimension, it doesn‟t need to connect to the database.

In Webi: all values for all objects that are dragged into the query panel will be retrieved. Hierarchical objects values won‟t be retrieved like deski. When ever you drill down the report, to display the values this report is to meet database again and retrieves the data.

Question 601. How To Overcome Overflow Of Data In A Report?

Answer :

a) By giving filters and conditions in the report level.
b) OVERFLOW occurs when a calculation returns a value that is too large for Web Intelligence to handle.
c) Select the properties at the report level and choose appearance from the tab. You can adjust the tables horizontally and vertically.
d) When you have huge number of rows in report then u will get partial results in that report.
For that you have to increase the (Limit Size of the Results) check box button in Universe Parameters. Then your report will not overflows.

Question 602. Is There Any Limit For Rows And Columns In Cross Tab?

Answer :

No

Question 603. What Is Static Filter And Dynamic Filter?

Answer :

In Static filter, record set is filtered based on a table field value.
In Dynamic filter, record set is filtered based on the value specified for a specific business object property.

Question 604. What Is Report Tracing In Bo?

Answer :

Mainly the tracing concept is coming in designer level. Tracing means if you have 2 tables, if you select one table column drag the cursor to the next table column, at that time cursor will turns into pencil symbol.

Question 605. How Many Micro Cubes Can A Report Have?

Answer :

Only one.

Question 606. What Is A Local Filter?

Answer :

A local filter is applicable only to a particular block i.e. the block on which it is created like on a particular table or cross tab.

Question 607. What Is A Prompt?

Answer :

Prompts are used for asking the user for Dynamic Inputs while refreshing the Report.

Question 608. Can We Create Reports Without Creating Universe?

Answer :

Yes we can create reports without creating Universe.

Question 609. What Are Ad-hoc Reports?

Answer :

Ad-hoc reports means with in the organization user can create reports by directly interact with IT peoples. That is time depended reports not detailed reports.

Question 610. How To Hide The Tables In Webi?

Answer :

We can hide a table in webI when the table is empty.
From the properties tab, deselect 'Show when empty' check box.

Question 611. How Do U Receive Requirements From The Client?

Answer :

Through web intelligence and through browser.

Question 612. How To Explain Short Cut Join And Theta Join?

Answer :

a) Shortcut join: it is direct join between source and destination
Example: country-->region-> city
We can connect country and city using shortcut join
Theta join: non equality condition between two tables.

b) Short cut Join providing an alternative path between two tables. passing intermediate tables, leading to the same result, regardless of direction. Optimizes query time by cutting long join paths as short as possible.
Theta join Link tables based on a relationship other than equality between two columns.

Question 613. What Are The Types Of Universes? Plz Explain It?

Answer :

Universes are two types
1) Simple Universe and
2) Complex Universe
   b) Derived Universe, Linked Universe and Core Universe are the Types of Universe.
   Simple and complex (linked universe)

Question 614. What Are The Types Of Connections?

Answer :

1) Shared: Available to multiple users
2) Personal: Belongs to user, who created it, others cannot use it.
3) Secured: These are centralized and any one can use it and used to deploy business objects reports.

Question 615. What Is Meant By Slowly Changing Dimensions?

Answer :

Master data occur in the OLTP system and that can't change regularly, when the changes are occurred in the OLTP system, that changes can be handled by the dimension tables. Such type of dimensions is called slowly changing dimensions.
There are three types of dimensions
TYPE1 (Maintain only current data)
TYPE2 (Maintain complete historic data)
TYPE3 (Maintain one time historic data)

Question 616. What Is Meant By Scorecards?

Answer :

Provide fast and effective way of monitoring key measures.
Scorecard is a concept used for measuring a company's activities in terms of its vision and strategies, to give managers a comprehensive view of the performance of the business.

Question 617. Case1: A Person Buy A Car, Case2: Rent A Car Which Is Context & Which Is Alias? Why?

Answer :

Buy a car is context & rent a car is alias
Because, buy a car is a fact & rent a car is a look up, alias is created on look up tables.

Question 618. What Is Meant By Ad Hoc Reports? Can Any Body Will Explain With Examples.

Answer :

Ad hoc reporting is a user friendly feature designed for all levels of users. Custom reports are created using queries.

Ad hoc meant for management users.

Example BO is ad hoc reporting tool used to make quick decisions.
Example: if you have a one shopping mall u want find out the stock status. For clearance of the stock u need to take a decision what type of decision u need to take for clearance of stock.

Question 619. What Is A Query?

Answer :

A query is one or more statements that request data from a database. If the data is available, then the requested data returns in the form of a table which contains rows and columns. Queries are sent to the databases in a language called SQL. However, when using the Report Panel, SQL knowledge is not required.

Question 620. Is It Possible To Create Reports From Different Universes In One Document?

Answer :

Yes, it is possible to use different universe to generate a single report....multiple data providers.

Question 621. What Is Row Level Security?

Answer :

The measure of specifying user can retrieve which rows of data based on a column of data or combination of columns is called row level security.

Question 622. How To Spot A Hierarchy?

Answer :

From the designer u can spot the already mentioned hierarchy and also u can change or edit the same.
Go to Tool->Hierarchies
Here u can ether add a new one or can also edit the existing one.

Question 623. What Type Of Joins Returns Incorrect Results?

Answer :

Isolated joins, cross join, non equi join.

Question 624. What Kind Of Tool Bo Is?

Answer :

a) Bo is a reporting tool to Query the database or data warehouse.
b) Bo is a query, reporting and analysis tool.
c) Bo is an OLAP tool. (ROLAP)

Question 625. What Is The Purpose Of Testing Integrity Of The Universe?

Answer :

a) To check the universe weather it is correct or in correct, means that any isolated joins, divergence, loops, contexts, wrong joins, parsing happened in the universe.

b) An integrity check detects:
1. Invalid syntax
2. Loops
3. Isolated tables
4. Isolated joins
5. Loops with in contexts
6. Missing and Invalid cardinalities.

Question 626. How You Worked With Multiple Data Sources?if Yes ?how Do You Link Them?

Answer :

you can create different universe for different sources and link them in BO.

Question 627. Genarally What Are The Problems Are Facing While Creating Reports?

Answer :

THE MOST COMMON PROBLEM IS JOIN PATH PROBLEM
i.e,
LOOPS
CHASAM TRAPS
FAN TRAPS.

Question 628. Where Do You Use Global Filters ,explain With Example?

Answer :

gobal filter acts on all fields in the report table.

Question 629. What Problems Are Not Known While Performing Integrity Check?

Answer :

We can't find traps i.e. chasm trap and fan trap. It can be identified only by visualization.

Question 630. What Is Context? How U Create? With Example.

Answer :

It is a set of joins that specefies one of several paths through tables in loop.
if a loop is having 2 or more fact tables(multiple fact tables) then the loop can be resolved by detecting context
tools-->insert context
then
you can select the path.

Question 631. How Can We Improve Performance?

Answer :

By making use of Aggregate tables.
1)usinf aggregated tables
2)using shortcut joins
3)removing unwanted classes and objects
4)removing unwanted joins
5)lov should be based on smaller look up tables

Question 632. What Is The Use Of Bo Sdk?

Answer :

Bo SDK main use is to suppress ?no data to fetch? using Macros.

The BusinessObjects Enterprise SDK allows you to build web applications that interface directly with your BusinessObjects Enterprise system.

BO SBK Means, BO Software Development Kit.

It Used for BO With Java or BO With Dot Net Integration. You can integrate BO in java or .Net application. It provide Java & .Net Api classes & functions.

Question 633. Why Do We Need Metrics And Sets?

Answer :

Metrics are used for analysis and Sets are used for grouping.

Question 634. What Is The Source For Metrics?

Answer :

measure objects.

Question 635. What Is The Use Of Afd? Where It Can Be Stored?

Answer :

used to create dashboards. It can be stored in repository, corporate or personal.

Question 636. What Is A Set?

Answer :

Its nothing but grouping of users.

Question 637. What Is A Loop? How Can We Overcome?

Answer :

loop is a closed path between end to end.continuous floe of data.creation of alias table is solution to resolve loops

Loop is nothing but a closed circular flow; it can be overcome by making use of Alias and Context.

A loop is a set of joins that defines a closed path through a set of tables in a schema. Loops occur when joins form multiple paths between lookup tables.

Loops can be solved by using aliases or contexts.

loop is a closed path between end to end.continuous floe of data.creation of alias table is solution to resolve loops.

Question 638. What Is The Size Of Data Base?

Answer :

In general it will be anything between 4-8 Terabytes.

Question 639. What Do You Mean By Object Qualification?

Answer :

Object qualification represents what kind of object is that, usually we have three types of object qualifiers they are measure, dimension, detailed.

Object qualification is nothing but a property of an object determines how it can be used in multidimensional analysis. For the purpose of multidimensional analysis objects can be qualified as dimension, detailed and measure.

Question 640. How Do You Restrict Access To Rows Of A Database?

Answer :

In XI version it can be done by using row-level security in designer module whereas in 5i/6i it is done by supervisor.

Question 641. Can We Have Multiple Domains?

Answer :

Yes.
we have multiple domains,but security domain is not multiple,only document domain and universe domain is multiple.

Question 642. When Is The Repository Created?

Answer :

In 5i/6i versions after installing the software, whereas in Xi version a repository is created at the time of installation.

Question 643. What Is The Test Methodology For Testing Bo Universes?

Answer :

Integrity Check is the option through which one can test the universse in BO.

Question 644. How Can You Access Your Repository With Different User Profiles?

Answer :

first thing we are under the member(user) of the repository.and we need to rights to access repository. we also need to create perticular user name and pass.

Question 645. Differentiate Between Data Mining And Data Warehousing.

Answer :

Data warehousing is merely extracting data from different sources, cleaning the data and storing it in the warehouse. Where as data mining aims to examine or explore the data using queries. These queries can be fired on the data warehouse. Explore the data in data mining helps in reporting, planning strategies, finding meaningful patterns etc.

E.g. a data warehouse of a company stores all the relevant information of projects and employees. Using Data mining, one can use this data to generate different reports like profits generated etc.

Question 646. What Are Olap And Oltp?

Answer :

An IT system can be divided into Analytical Process and Transactional Process.

OLTP – categorized by short online transactions. The emphasis is query processing, maintaining data integration in multi-access environment.

OLAP – Low volumes of transactions are categorized by OLAP. Queries involve aggregation and very complex. Response time is an effectiveness measure and used widely in data mining techniques.

Question 647. Explain How To Mine An Olap Cube.

Answer :

A data mining extension can be used to slice the data the source cube in the order as discovered by data mining. When a cube is mined the case table is a dimension.

Question 648. Multi Pass Sql:

Answer :

Multipass: Breaking one large SQL into multiple SQLs.If you are using the star schema with two or more fact tables,and you enable this feature, BO will automatically generate two or more SQLs (i.e. one SQL for each fact table object used in the report). Then the results will be synchronised in the report.

Question 649. Who Launches The Supervisor Product In Business Objects For First Time?

Answer :

general supervisor

Question 650. Analysis In Business Objects?

Answer :

Analysis in BO is Utility in BO with the help of that we can manage our document..

Anlysis in BO with the help we can Slide, Dice and Drill the reports.

Question 1. What Is Database Design?

Answer :

Database design is the process of producing a detailed data model of database. This data model contains all the needed logical and physical design choices and physical storage parameters needed to generate a design in a data definition language, which can then be used to create a database.

Question 2. What Is The Logical Design Of A Database?

Answer :

The process of logical design involves arranging data into a series of logical relationships called entities and attributes. An entity represents a chunk of information. In relational databases, an entity often maps to a table. An attribute is a component of an entity and helps define the uniqueness of the entity.

Data Warehouse ETL Toolkit Interview Questions
Question 3. What Is The Structure Of A Database?

Answer :

Instead of having all the data in a list with a random order, a database provides a structure to organize the data. One of the most common data structures is a database table. A database table consists of rows and columns. A database table is also called a two-dimensional array.

Question 4. What Is A Logical Data Model?

Answer :

A logical data model or logical schema is a data model of a specific problem domain expressed independently of a particular database management product or storage technology (physical data model) but in terms of data structures such as relational tables and columns, object-oriented classes, or XML tags.

Data Warehouse ETL Toolkit Tutorial
Question 5. What Is A Conceptual Data Model?

Answer :

A conceptual schema is a high-level description of a business's informational needs. It typically includes only the main concepts and the main relationships among them. ... The conceptual model is also known as the data model as data model can be used to describe the conceptual schema when a database system is implemented.

PL/SQL Interview Questions
Question 6. What Is The Physical Data Model?

Answer :

A physical database model shows all table structures, including column name, column data type, column constraints, primary key, foreign key, and relationships between tables. Features of a physical data model include: Specification all tables and columns. Foreign keys are used to identify relationships between tables.

Question 7. What Is The Conceptual Design Of A Database?

Answer :

This phase is called conceptual design. The result of this phase is an Entity-Relationship (ER) diagram or UML class diagram. It is a high-level data model of the specific application area. It describes how different entities (objects, items) are related to each other.

T-SQL Tutorial T-SQL Interview Questions
Question 8. What Is A Conceptual Model For Research?

Answer :

A conceptual model is a representation of a system, made of the composition of concepts which are used to help people know, understand, or simulate a subject the model represents. Some models are physical objects; for example, a toy model which may be assembled, and may be made to work like the object it represents.

Question 9. What Is An Iconic Model?

Answer :

An Iconic Model is a look-alike representation of some specific entity. (e.g. a house) Classification. Iconic Models can be represented in: - Two Dimensions : e.g. photos, drawings, etc.

SQL Database Interview Questions
Question 10. What Is The Framework Of A Research?

Answer :

Theories are formulated to explain, predict, and understand phenomena and, in many cases, to challenge and extend existing knowledge within the limits of critical bounding assumptions. The theoretical framework is the structure that can hold or support a theory of a research study.

SQL Database Tutorial
Question 11. What Is The Conceptual Framework?

Answer :

A conceptual framework is an analytical tool with several variations and contexts. It is used to make conceptual distinctions and organize ideas. Strong conceptual frameworks capture something real and do this in a way that is easy to remember and apply.

Oracle MySQL 5.6 Database Administrator Interview Questions
Question 12. What Is A Working Model?

Answer :

Working Model is an engineering simulation software product by Design Simulation Technologies, Inc.. Virtual mechanical components, such as springs, ropes, and motors are combined with objects in a 2D working space.

Data Warehouse ETL Toolkit Interview Questions
Question 13. What Is An Example Of A Physical Model?

Answer :

Physical model (most commonly referred to simply as a model but in this context distinguished from a conceptual model) is a smaller or larger physical copy of an object. The object being modelled may be small (for example, an atom) or large (for example, the Solar System).

Question 14. What Is The Internal Working Model?

Answer :

This internal working model is a cognitive framework comprising mental representations for understanding the world, self and others.

Question 15. What Is The Data Modeling?

Answer :

Data modeling is often the first step in database design and object-oriented programming as the designers first create a conceptual model of how data items relate to each other. Data modeling involves a progression from conceptual model to logical model to physical schema.

Database Administration Interview Questions
Question 16. What Are The Features Of A Physical Data Model?

Answer :

Features of a physical data model include:

Specification all tables and columns.
Foreign keys are used to identify relationships between tables.
Denormalization may occur based on user requirements.
Physical considerations may cause the physical data model to be quite different from the logical data model.
Physical data model will be different for different RDBMS. For example, data type for a column may be different between MySQL and SQL Server.
Question 17. What Are The Steps To Design A Physical Model?

Answer :

The steps for physical data model design are as follows:

Convert entities into tables.
Convert relationships into foreign keys.
Convert attributes into columns.
Modify the physical data model based on physical constraints / requirements.
IDMS (Integrated Database Management System) Interview Questions
Question 18. What Are The Features Of Conceptual Data Model?

Answer :

Features of conceptual data model include:

Includes the important entities and the relationships among them.
No attribute is specified.
No primary key is specified.
PL/SQL Interview Questions
Question 19. What Are The Difference Between Logical Data Model And Conceptual Data Model?

Answer :

In a logical data model, primary keys are present, whereas in a conceptual data model, no primary key is present.
In a logical data model, all attributes are specified within an entity. No attributes are specified in a conceptual data model.
Relationships between entities are specified using primary keys and foreign keys in a logical data model. In a conceptual data model, the relationships are simply stated, not specified, so we simply know that two entities are related, but we do not specify what attributes are used for this relationship.
Question 20. What Are The Steps To Design Logical Data Model?

Answer :

The steps for designing the logical data model are as follows:

Specify primary keys for all entities.
Find the relationships between different entities.
Find all attributes for each entity.
Resolve many-to-many relationships.
Normalization.


Question 1. What Is Etl?

Answer :

ETL stands for extraction transformation and loading
ETL provide developers with an interface for designing source-to-target mappings, transformation and job control parameter
* Extraction
  Take data from an external source and move it to the warehouse pre-processor database
* Transformation
  Transform data task allows point-to-point generating, modifying and transforming data
* Loading
  Load data task adds records to a database table in a warehouse.

Question 2. What Is A Three Tier Data Warehouse?

Answer :

A data warehouse can be thought of as a three-tier system in which a middle system provides usable data in a secure way to end users. On either side of this middle system are the end users and the back-end data stores.

Informatica Interview Questions
Question 3. What Is The Metadata Extension?

Answer :

Informatica allows end users and partners to extend the metadata stored in the repository by associating information with individual objects in the repository. For example, when you create a mapping, you can store your contact information with the mapping. You associate information with repository metadata using metadata extensions.

Informatica Client applications can contain the following types of metadata extensions:
Vendor-defined: Third-party application vendors create vendor-defined metadata extensions. You can view and change the values of vendor-defined metadata extensions, but you cannot create, delete, or redefine them.

User-defined: You create user-defined metadata extensions using PowerCenter/PowerMart. You can create, edit, delete, and view user-defined metadata extensions. You can also change the values of user-defined extensions.

Question 4. Can We Override A Native Sql Query Within Informatica? Where Do We Do It? How Do We Do It?

Answer :

Yes,we can override a native sql query in source qualifier and lookup transformation.

In lookup transformation we can find "Sql override" in lookup properties. by using this option we can do this.

Informatica Tutorial
Question 5. How Can We Use Mapping Variables In Informatica? Where Do We Use Them?

Answer :

Yes. we can use mapping variable in Informatica.

The Informatica server saves the value of mapping variable to the repository at the end of session run and uses that value next time we run the session.

Data Warehousing Interview Questions
Question 6. What Are Snapshots? What Are Materialized Views & Where Do We Use Them? What Is A Materialized View Log?

Answer :

Snapshots are read-only copies of a master table located on a remote node which is periodically refreshed to reflect changes made to the master table. Snapshots are mirror or replicas of tables.

Views are built using the columns from one or more tables. The Single Table View can be updated but the view with multi table cannot be updated.

A View can be updated/deleted/inserted if it has only one base table if the view is based on columns from one or more tables then insert, update and delete is not possible.
Materialized view:
A pre-computed table comprising aggregated or joined data from fact and possibly dimension tables. Also known as a summary or aggregate table.

Question 7. Can Informatica Load Heterogeneous Targets From Heterogeneous Sources?

Answer :

No, In Informatica 5.2 and
Yes, in Informatica 6.1 and later.

Data Warehousing Tutorial Networking Interview Questions
Question 8. What Is Etl Process ?how Many Steps Etl Contains Explain With Example?

Answer :

ETL is extraction , transforming , loading process , you will extract data from the source and apply the business role on it then you will load it in the target
The steps are :
1-define the source (create the odbc and the connection to the source DB)
2-define the target (create the odbc and the connection to the target DB)
3-create the mapping ( you will apply the business role here by adding transformations , and define how the data flow will go from the source to the target )
4-create the session (its a set of instruction that run the mapping )
5-create the work flow (instruction that run the session)

Question 9. What Is Full Load & Incremental Or Refresh Load?

Answer :

Full Load: completely erasing the contents of one or more tables and reloading with fresh data.
Incremental Load: applying ongoing changes to one or more tables based on a predefined schedule.

System Administration Interview Questions
Question 10. Is There Any Way To Read The Ms Excel Data's Directly Into Informatica? Like Is There Any Possibilities To Take Excel File As Target?

Answer :

we can’t directly import the xml file in informatica.
we have to define the Microsoft excel odbc driver on our system and define the name in exce sheet by defining ranges then in informatica open the folder using sources ->import from database->select excel odbc driver->connect->select the excel sheet name .

Networking Tutorial
Question 11. What Is A Staging Area? Do We Need It? What Is The Purpose Of A Staging Area?

Answer :

Data staging is actually a collection of processes used to prepare source system data for loading a data warehouse. Staging includes the following steps:
Source data extraction, Data transformation (restructuring),
Data transformation (data cleansing, value transformations),
Surrogate key assignments

Hadoop Interview Questions
Question 12. How Do We Call Shell Scripts From Informatica?

Answer :

Specify the Full path of the Shell script the "Post session properties of session/workflow".

Informatica Interview Questions
Question 13. What Is The Difference Between Power Center & Power Mart?

Answer :

PowerCenter - ability to organize repositories into a data mart domain and share metadata across repositories.
PowerMart - only local repository can be created.

Hadoop Tutorial
Question 14. Can We Lookup A Table From Source Qualifier Transformation. Ie. Unconnected Lookup

Answer :

You cannot lookup from a source qualifier directly. However, you can override the SQL in the source qualifier to join with the lookup table to perform the lookup.

Question 15. Do We Need An Etl Tool? When Do We Go For The Tools In The Market?

Answer :

ETL Tool:
It is used to Extract(E) data from multiple source systems(like RDBMS, Flat files, Mainframes, SAP,XML etc) transform(T) them based on Business requirements and Load(L) in target locations.(like tables, files etc).
Need of ETL Tool:
An ETL tool is typically required when data scattered across different systems. (like RDBMS, Flat files, Mainframes, SAP,XML etc).

MYSQL DBA Interview Questions
Question 16. What Is Informatica Metadata And Where Is It Stored?

Answer :

Informatica Metadata is data about data which stores in Informatica repositories.

Apache Flume Tutorial
Question 17. Techniques Of Error Handling - Ignore , Rejecting Bad Records To A Flat File , Loading The Records And Reviewing Them (default Values)

Answer :

Rejection of records either at the database due to constraint key violation or the informatica server when writing data into target table. These rejected records we can find in the bad files folder where a reject file will be created for a session. we can check why a record has been rejected. And this bad file contains first column a row indicator and second column a column indicator.

These row indicators or of four types:
D-valid data,
O-overflowed data,
N-null data,
T- Truncated data,
And depending on these indicators we can changes to load data successfully to target.

Data modeling Interview Questions
Question 18. What Are The Various Methods Of Getting Incremental Records Or Delta Records From The Source Systems?

Answer :

One foolproof method is to maintain a field called 'Last Extraction Date' and then impose a condition in the code saying 'current_extraction_date > last_extraction_date'.

Data Warehousing Interview Questions
Question 19. What Are The Different Versions Of Informatica?

Answer :

Here are some popular versions of Informatica.
Informatica Powercenter 4.1,
Informatica Powercenter 5.1,
Powercenter Informatica 6.1.2,
Informatica Powercenter 7.1.2,
Informatica Powercenter 8.1,
Informatica Powercenter 8.5,
Informatica Powercenter 8.6.

Question 20. What Is Ods (operation Data Source)

Answer :

ODS - Operational Data Store.
ODS Comes between staging area & Data Warehouse. The data is ODS will be at the low level of granularity.
Once data was populated in ODS aggregated data will be loaded into into EDW through ODS.

Hadoop Administration Interview Questions
Question 21. What Is Latest Version Of Power Center / Power Mart?

Answer :

The Latest Version is 7.2

Question 22. What Are The Various Tools?

Answer :

- Cognos Decision Stream
- Oracle Warehouse Builder
- Business Objects XI (Extreme Insight)
- SAP Business Warehouse
- SAS Enterprise ETL Server

Question 23. Compare Etl & Manual Development?

Answer :

ETL - The process of extracting data from multiple sources.(ex. flat files, XML, COBOL, SAP etc) is more simpler with the help of tools.
Manual - Loading the data other than flat files and oracle table need more effort.
ETL - High and clear visibility of logic.
Manual - complex and not so user friendly visibility of logic.
ETL - Contains Meta data and changes can be done easily.
Manual - No Meta data concept and changes needs more effort.
ETL- Error handling, log summary and load progress makes life easier for developer and maintainer.
Manual - need maximum effort from maintenance point of view.
ETL - Can handle Historic data very well.
Manual - as data grows the processing time degrades.

These are some differences b/w manual and ETL development.

Apache Flume Interview Questions
Question 24. When Do We Analyze The Tables? How Do We Do It?

Answer :

The ANALYZE statement allows you to validate and compute statistics for an index, table, or cluster. These statistics are used by the cost-based optimizer when it calculates the most efficient plan for retrieval. In addition to its role in statement optimization, ANALYZE also helps in validating object structures and in managing space in your system. You can choose the following operations: COMPUTER, ESTIMATE, and DELETE. Early version of Oracle7 produced unpredictable results when the ESTIMATE operation was used. It is best to compute your statistics.

Networking Interview Questions
Question 25. How Do You Calculate Fact Table Granularity?

Answer :

Granularity, is the level of detail in which the fact table is describing, for example if we are making time analysis so the granularity maybe day based - month based or year based

Question 26. What Are The Modules In Power Mart?

Answer :

1. PowerMart Designer
2. Server
3. Server Manager
4. Repository
5. Repository Manager

Informatica Admin Interview Questions
Question 27. If A Flat File Contains 1000 Records How Can I Get First And Last Records Only?

Answer :

By using Aggregator transformation with first and last functions we can get first and last record.

System Administration Interview Questions
Question 28. Lets Suppose We Have Some 10,000 Odd Records In Source System And When Load Them Into Target.how Do We Ensure That All 10,000 Records That Are Loaded To Target Doesn't Contain Any Garbage Values?

Answer :

we can do ltrim, rtrim in the expression or can have check for null and then insert the data.

Question 29. How Do We Extract Sap Data Using Informatica? What Is Abap? What Are Idocs?

Answer :

SAP Data can be loaded into Informatica in the form of Flat files.
Condition:
Informatica source qualifier column sequence must match the SAP source file.

Question 30. What Is The Difference Between Joiner And Lookup ?

Answer :

joiner is used to join two or more tables to retrieve data from tables (just like joins in sql).
Look up is used to check and compare source table and target table . (just like correlated sub-query in sql).

Question 31. What Are The Various Test Procedures Used To Check Whether The Data Is Loaded In The Backend, Performance Of The Mapping, And Quality Of The Data Loaded In Informatica.

Answer :

The best procedure to take a help of debugger where we monitor each and every process of mappings and how data is loading based on conditions breaks.

Question 32. What Is The Difference Between Etl Tool And Olap Tools ?

Answer :

ETL tool is meant for extraction data from the legacy systems and load into specified data base with some process of cleansing data.
ex: Informatica, data stage ....etc
OLAP is meant for Reporting purpose. in OLAP data available in Multidirectional model. so that u can write simple query to extract data from the data base.
ex: Business objects, Cognos....etc

Question 33. What Are Active Transformation / Passive Transformations?

Answer :

Active transformation can change the number of rows that pass through it. (Decrease or increase rows)
Passive transformation cannot change the number of rows that pass through it.

Hadoop Interview Questions
Question 34. What Are The Different Lookup Methods Used In Informatica?

Answer :

1. Connected lookup
2. Unconnected lookup

Connected lookup will receive input from the pipeline and sends output to the pipeline and can return any number of values. it does not contain return port.

Unconnected lookup can return only one column. it contain return port.

Question 35. What Are Parameter Files ? Where Do We Use Them?

Answer :

Parameter file defines the value for parameter and variable used in a workflow, work let or session.

Question 36. What Are The Various Transformation Available?

Answer :

Aggregator Transformation
Expression Transformation
Filter Transformation
Joiner Transformation
Lookup Transformation
Normalizer Transformation
Rank Transformation
Router Transformation
Sequence Generator Transformation
Stored Procedure Transformation
Sorter Transformation
Update Strategy Transformation
XML Source Qualifier Transformation
Advanced External Procedure Transformation
External Transformation
MYSQL DBA Interview Questions
Question 37. How To Determine What Records To Extract?

Answer :

When addressing a table some dimension key must reflect the need for a record to get extracted. Mostly it will be from time dimension (e.g. date >= 1st of current month) or a transaction flag (e.g. Order Invoiced Stat). Foolproof would be adding an archive flag to record which gets reset when record changes.

Question 38. What Are Snapshots? What Are Materialized Views & Where Do We Use Them? What Is A Materialized View Do?

Answer :

Materialized view is a view in which data is also stored in some temp table. i.e if we will go with the View concept in DB in that we only store query and once we call View it extract data from DB. But In materialized View data is stored in some temp tables.

Question 39. Give Some Popular Tools?

Answer :

Popular Tools:
IBM WebSphere Information Integration (Accentual DataStage)
Ab Initio
Informatica
Talend

Question 40. Give Some Etl Tool Functionalities?

Answer :

While the selection of a database and a hardware platform is a must, the selection of an ETL tool is highly recommended, but it's not a must. When you evaluate ETL tools, it pays to look for the following characteristics:

Functional capability: This includes both the 'transformation' piece and the 'cleansing' piece. In general, the typical ETL tools are either geared towards having strong transformation capabilities or having strong cleansing capabilities, but they are seldom very strong in both. As a result, if you know your data is going to be dirty coming in, make sure your ETL tool has strong cleansing capabilities. If you know there are going to be a lot of different data transformations, it then makes sense to pick a tool that is strong in transformation.

Ability to read directly from your data source: For each organization, there is a different set of data sources. Make sure the ETL tool you select can connect directly to your source data.

Metadata support: The ETL tool plays a key role in your metadata because it maps the source data to the destination, which is an important piece of the metadata. In fact, some organizations have come to rely on the documentation of their ETL tool as their metadata source. As a result, it is very important to select an ETL tool that works with your overall metadata strategy.

Data modeling Interview Questions
Question 41. How To Fine Tune The Mappings?

Answer :

1.Use filter condition in source qualifies without using filter
2.use persistence and shared cache in look up t/r
3.use in aggregations t/r in sorted i/p, group by ports
4.in expression use operators instead of functions
5.increase the cache size
6. increase the commit interval

Question 42. Where Do We Use Connected And Un Connected Lookups

Answer :

If return port only one then we can go for unconnected. More than one return port is not possible with Unconnected. If more than one return port then go for Connected.

Hadoop Administration Interview Questions
Question 43. What Are The Various Tools? - Name A Few.

Answer :

- Abinitio
- DataStage
- Informatica
- Cognos Decision Stream
- Oracle Warehouse Builder
- Business Objects XI (Extreme Insight)
- SAP Business Warehouse
- SAS Enterprise ETL Server

Question 1. What Is Rdbms?

Answer :

Relational Data Base Management Systems (RDBMS) are database management systems that maintain data records and indices in tables. Relationships may be created and maintained across and among the data and tables. In a relational database, relationships between data items are expressed by means of tables. Interdependencies among these tables are expressed by data values rather than by pointers. This allows a high degree of data independence. An RDBMS has the capability to recombine the data items from different files, providing powerful tools for data usage.

Question 2. What Is Normalization?

Answer :

Database normalization is a data design and organization process applied to data structures based on rules that help build relational databases. In relational database design, the process of organizing data to minimize redundancy. Normalization usually involves dividing a database into two or more tables and defining relationships between the tables. The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database via the defined relationships.

ETL Testing Interview Questions
Question 3. What Are Different Normalization Forms?

Answer :

1NF: Eliminate Repeating Groups Make a separate table for each set of related attributes, and give each table a primary key. Each field contains at most one value from its attribute domain.

2NF: Eliminate Redundant Data If an attribute depends on only part of a multi-valued key, remove it to a separate table.

3NF: Eliminate Columns Not Dependent On Key If attributes do not contribute to a description of the key, remove them to a separate table. All attributes must be directly dependent on the primary key.

BCNF: Boyce-Codd Normal Form If there are non-trivial dependencies between candidate key attributes, separate them out into distinct tables.

4NF: Isolate Independent Multiple Relationships No table may contain two or more 1:n or n:m relationships that are not directly related.

5NF: Isolate Semantically Related Multiple Relationships There may be practical constrains on information that justify separating logically related many-to-many relationships.

ONF: Optimal Normal Form A model limited to only simple (elemental) facts, as expressed in Object Role Model notation.

DKNF: Domain-Key Normal Form A model free from all modification anomalies. Remember, these normalization guidelines are cumulative. For a database to be in 3NF, it must first fulfill all the criteria of a 2NF and 1NF database.

Question 4. What Is Stored Procedure?

Answer :

A stored procedure is a named group of SQL statements that have been previously created and stored in the server database. Stored procedures accept input parameters so that a single procedure can be used over the network by several clients using different input data. And when the procedure is modified, all clients automatically get the new version. Stored procedures reduce network traffic and improve performance. Stored procedures can be used to help ensure the integrity of the database.
e.g. sp_helpdb, sp_renamedb, sp_depends etc.

ETL Testing Tutorial
Question 5. What Is Trigger?

Answer :

A trigger is a SQL procedure that initiates an action when an event (INSERT, DELETE or UPDATE) occurs. Triggers are stored in and managed by the DBMS. Triggers are used to maintain the referential integrity of data by changing the data in a systematic fashion. A trigger cannot be called or executed; the DBMS automatically fires the trigger as a result of a data modification to the associated table. Triggers can be viewed as similar to stored procedures in that both consist of procedural logic that is stored at the database level. Stored procedures, however, are not event-drive and are not attached to a specific table as triggers are. Stored procedures are explicitly executed by invoking a CALL to the procedure while triggers are implicitly executed. In addition, triggers can also execute stored procedures.

SQL Server 2008 Interview Questions
Question 6. What Is View?

Answer :

A simple view can be thought of as a subset of a table. It can be used for retrieving data, as well as updating or deleting rows. Rows updated or deleted in the view are updated or deleted in the table the view was created with. It should also be noted that as data in the original table changes, so does data in the view, as views are the way to look at part of the original table. The results of using a view are not permanently stored in the database. The data accessed through a view is actually constructed using standard T-SQL select command and can come from one to many different base tables or even other views.

Question 7. What Is Index?

Answer :

An index is a physical structure containing pointers to the data. Indices are created in an existing table to locate rows more quickly and efficiently. It is possible to create an index on one or more columns of a table, and each index is given a name. The users cannot see the indexes, they are just used to speed up queries. Effective indexes are one of the best ways to improve performance in a database application. A table scan happens when there is no index available to help a query. In a table scan SQL Server examines every row in the table to satisfy the query results. Table scans are sometimes unavoidable, but on large tables, scans have a terrific impact on performance. Clustered indexes define the physical sorting of a database table’s rows in the storage media. For this reason, each database table may have only one clustered index. Non-clustered indexes are created outside of the database table and contain a sorted list of references to the table itself.

SQL Server 2008 Tutorial SQL Database Interview Questions
Question 8. What Is Database?

Answer :

A database is a logically coherent collection of data with some inherent meaning, representing some aspect of real world and which is designed, built and populated with data for a specific purpose.

Question 9. What Is Dbms?

Answer :

It is a collection of programs that enables user to create and maintain a database. In other words it is general-purpose software that provides the users with the processes of defining, constructing and manipulating the database for various applications.

Oracle 11g Interview Questions
Question 10. What Is A Database System?

Answer :

The database and DBMS software together is called as Database system.

SQL Database Tutorial
Question 11. Advantages Of Dbms?

Answer :

Redundancy is controlled.
Unauthorised access is restricted.
Providing multiple user interfaces.
Enforcing integrity constraints.
Providing backup and recovery.
PostgreSQL Interview Questions
Question 12. Disadvantage In File Processing System?

Answer :

Data redundancy & inconsistency.
Difficult in accessing data.
Data isolation.
Data integrity.
Concurrent access is not possible.
Security Problems.
ETL Testing Interview Questions
Question 13. Describe The Three Levels Of Data Abstraction?

Answer :

There are three levels of abstraction:

Physical level: The lowest level of abstraction describes how data are stored.
Logical level: The next higher level of abstraction, describes what data are stored in database and what relationship among those data.
View level: The highest level of abstraction describes only part of entire database.
Oracle 11g Tutorial
Question 14. Define The "integrity Rules"?

Answer :

There are two Integrity rules.

Entity Integrity: States that “Primary key cannot have NULL value”.
Referential Integrity: States that “Foreign Key can be either a NULL value or should be Primary Key value of other relation.
Question 15. What Is Extension And Intension?

Answer :

Extension : It is the number of tuples present in a table at any instance. This is time dependent.

Intension : It is a constant value that gives the name, structure of table and the constraints laid on it.

SQL DBA Interview Questions
Question 16. What Is System R? What Are Its Two Major Subsystems?

Answer :

System R was designed and developed over a period of 1974-79 at IBM San Jose Research Center. It is a prototype and its purpose was to demonstrate that it is possible to build a Relational System that can be used in a real life environment to solve real life problems, with performance at least comparable to that of existing system.
Its two subsystems are

Research Storage
System Relational Data System.
Apache Cassandra Tutorial
Question 17. How Is The Data Structure Of System R Different From The Relational Structure?

Answer :

Unlike Relational systems in System R

Domains are not supported
Enforcement of candidate key uniqueness is optional
Enforcement of entity integrity is optional
Referential integrity is not enforced
SSRS(SQL Server Reporting Services) Interview Questions
Question 18. What Is Data Independence?

Answer :

Data independence means that “the application is independent of the storage structure and access strategy of data”. In other words, The ability to modify the schema definition in one level should not affect the schema definition in the next higher level.
Two types of Data Independence:

Physical Data Independence: Modification in physical level should not affect the logical level.
Logical Data Independence: Modification in logical level should affect the view level.
SQL Server 2008 Interview Questions
Question 19. What Is A View? How It Is Related To Data Independence?

Answer :

A view may be thought of as a virtual table, that is, a table that does not really exist in its own right but is instead derived from one or more underlying base table. In other words, there is no stored file that direct represents the view instead a definition of view is stored in data dictionary. Growth and restructuring of base tables is not reflected in views. Thus the view can insulate users from the effects of restructuring and growth in the database. Hence accounts for logical data independence.

MongoDB Tutorial
Question 20. What Is Data Model?

Answer :

A collection of conceptual tools for describing data, data relationships data semantics and constraints.

MYSQL DBA Interview Questions
Question 21. What Is E-r Model?

Answer :

This data model is based on real world that consists of basic objects called entities and of relationship among these objects. Entities are described in a database by a set of attributes.

Question 22. What Is Object Oriented Model?

Answer :

This model is based on collection of objects. An object contains values stored in instance variables with in the object. An object also contains bodies of code that operate on the object. These bodies of code are called methods. Objects that contain same types of values and the same methods are grouped together into classes.

Question 23. What Is An Entity?

Answer :

It is a 'thing' in the real world with an independent existence.

IBM Websphere Application Server Interview Questions
Question 24. What Is An Entity Type?

Answer :

It is a collection (set) of entities that have same attributes.

SQL Database Interview Questions
Question 25. What Is An Entity Set?

Answer :

It is a collection of all entities of particular entity type in the database.

Question 26. What Is An Extension Of Entity Type?

Answer :

The collections of entities of a particular entity type are grouped together into an entity set.

Apache Cassandra Interview Questions
Question 27. What Is Weak Entity Set?

Answer :

An entity set may not have sufficient attributes to form a primary key, and its primary key compromises of its partial key and primary key of its parent entity, then it is said to be Weak Entity set.

Oracle 11g Interview Questions
Question 28. What Is An Attribute?

Answer :

It is a particular property, which describes the entity.

Question 29. What Is A Relation Schema And A Relation?

Answer :

A relation Schema denoted by R(A1, A2, …, An) is made up of the relation name R and the list of attributes Ai that it contains.

A relation is defined as a set of tuples. Let r be the relation which contains set tuples (t1, t2, t3, ..., tn). Each tuple is an ordered list of n-values t=(v1,v2, ..., vn).

MongoDB Interview Questions
Question 30. What Is Degree Of A Relation?

Answer :

It is the number of attribute of its relation schema.

Question 31. What Is Relationship?

Answer :

It is an association among two or more entities.

Question 32. What Is Relationship Set?

Answer :

The collection (or set) of similar relationships.

Sql Loader Interview Questions
Question 33. What Is Relationship Type?

Answer :

Relationship type defines a set of associations or a relationship set among a given set of entity types.

PostgreSQL Interview Questions
Question 34. What Is Degree Of Relationship Type?

Answer :

It is the number of entity type participating.

Question 35. What Is Ddl (data Definition Language)?

Answer :

A data base schema is specifies by a set of definitions expressed by a special language called DDL.

Question 36. What Is Vdl (view Definition Language)?

Answer :

It specifies user views and their mappings to the conceptual schema.

SQL DBA Interview Questions
Question 37. What Is Sdl (storage Definition Language)?

Answer :

This language is to specify the internal schema. This language may specify the mapping between two schemas.

Question 38. What Is Data Storage - Definition Language?

Answer :

The storage structures and access methods used by database system are specified by a set of definition in a special type of DDL called data storage-definition language.

Question 39. What Is Dml (data Manipulation Language)?

Answer :

This language that enable user to access or manipulate data as organized by appropriate data model.

Procedural DML or Low level: DML requires a user to specify what data are needed and how to get those data.
Non-Procedural DML or High level: DML requires a user to specify what data are needed without specifying how to get those data.
Question 40. What Is Dml Compiler?

Answer :

It translates DML statements in a query language into low-level instruction that the query evaluation engine can understand.

SSRS(SQL Server Reporting Services) Interview Questions
Question 41. What Is Query Evaluation Engine?

Answer :

It executes low-level instruction generated by compiler.

Question 42. What Is Ddl Interpreter?

Answer :

It interprets DDL statements and record them in tables containing metadata.

MYSQL DBA Interview Questions
Question 43. What Is Record-at-a-time?

Answer :

The Low level or Procedural DML can specify and retrieve each record from a set of records. This retrieve of a record is said to be Record-at-a-time.

Question 44. What Is Set-at-a-time Or Set-oriented?

Answer :

The High level or Non-procedural DML can specify and retrieve many records in a single DML statement. This retrieve of a record is said to be Set-at-a-time or Set-oriented.

Question 45. What Is Relational Algebra?

Answer :

It is procedural query language. It consists of a set of operations that take one or two relations as input and produce a new relation.

Question 46. What Is Relational Calculus?

Answer :

It is an applied predicate calculus specifically tailored for relational databases proposed by E.F. Codd.
E.g. of languages based on it are DSL ALPHA, QUEL.

Question 47. How Does Tuple-oriented Relational Calculus Differ From Domain-oriented Relational Calculus?

Answer :

The tuple-oriented calculus uses a tuple variables i.e., variable whose only permitted values are tuples of that relation. E.g. QUEL
The domain-oriented calculus has domain variables i.e., variables that range over the underlying domains instead of over relation. E.g. ILL, DEDUCE.

Question 48. What Is Functional Dependency?

Answer :

A Functional dependency is denoted by X Y between two sets of attributes X and Y that are subsets of R specifies a constraint on the possible tuple that can form a relation state r of R. The constraint is for any two tuples t1 and t2 in r if t1[X] = t2[X] then they have t1[Y] = t2[Y]. This means the value of X component of a tuple uniquely determines the value of component Y.

Question 49. When Is A Functional Dependency F Said To Be Minimal?

Answer :

Every dependency in F has a single attribute for its right hand side.
We cannot replace any dependency X A in F with a dependency Y A where Y is a proper subset of X and still have a set of dependency that is equivalent to F.
We cannot remove any dependency from F and still have set of dependency that is equivalent to F.
Question 50. What Is Multivalued Dependency?

Answer :

Multivalued dependency denoted by X Y specified on relation schema R, where X and Y are both subsets of R, specifies the following constraint on any relation r of R: if two tuples t1 and t2 exist in r such that t1[X] = t2[X] then t3 and t4 should also exist in r with the following properties

t3[x] = t4[X] = t1[X] = t2[X]
t3[Y] = t1[Y] and t4[Y] = t2[Y]
t3[Z] = t2[Z] and t4[Z] = t1[Z]
where [Z = (R-(X U Y)) ]

Question 51. What Is Lossless Join Property?

Answer :

It guarantees that the spurious tuple generation does not occur with respect to relation schemas after decomposition.

Question 52. What Is 1 Nf (normal Form)?

Answer :

The domain of attribute must include only atomic (simple, indivisible) values.

Question 53. What Is Fully Functional Dependency?

Answer :

It is based on concept of full functional dependency. A functional dependency X Y is full functional dependency if removal of any attribute A from X means that the dependency does not hold any more.

Question 54. What Is 2nf?

Answer :

A relation schema R is in 2NF if it is in 1NF and every non-prime attribute A in R is fully functionally dependent on primary key.

Question 55. What Is 3nf?

Answer :

A relation schema R is in 3NF if it is in 2NF and for every FD X A either of the following is true

X is a Super-key of R.
A is a prime attribute of R.
In other words, if every non prime attribute is non-transitively dependent on primary key.

Question 56. What Is Bcnf (boyce-codd Normal Form)?

Answer :

A relation schema R is in BCNF if it is in 3NF and satisfies an additional constraint that for every FD X A, X must be a candidate key.

Question 57. What Is 4nf?

Answer :

A relation schema R is said to be in 4NF if for every Multivalued dependency X Y that holds over R, one of following is true

X is subset or equal to (or) XY = R.
X is a super key.
Question 58. What Is 5nf?

Answer :

A Relation schema R is said to be 5NF if for every join dependency {R1, R2, ..., Rn} that holds R, one the following is true

Ri = R for some i.
The join dependency is implied by the set of FD, over R in which the left side is key of R.
Question 59. What Is Domain-key Normal Form?

Answer :

A relation is said to be in DKNF if all constraints and dependencies that should hold on the constraint can be enforced by simply enforcing the domain constraint and key constraint on the relation.

Question 60. What Are Partial, Alternate, Artificial, Compound And Natural Key?

Answer :

Partial Key:
It is a set of attributes that can uniquely identify weak entities and that are related to same owner entity. It is sometime called as Discriminator.

Alternate Key:
All Candidate Keys excluding the Primary Key are known as Alternate Keys.

Artificial Key:
If no obvious key, either stand alone or compound is available, then the last resort is to simply create a key, by assigning a unique number to each record or occurrence. Then this is known as developing an artificial key.

Compound Key:
If no single data element uniquely identifies occurrences within a construct, then combining multiple elements to create a unique identifier for the construct is known as creating a compound key.

Natural Key:
When one of the data elements stored within a construct is utilized as the primary key, then it is called the natural key.

Question 61. What Is Indexing And What Are The Different Kinds Of Indexing?

Answer :

Indexing is a technique for determining how quickly specific data can be found.
Types:

Binary search style indexing
B-Tree indexing
Inverted list indexing
Memory resident table
Table indexing
Question 62. What Is System Catalog Or Catalog Relation? How Is Better Known As?

Answer :

A RDBMS maintains a description of all the data that it contains, information about every relation and index that it contains. This information is stored in a collection of relations maintained by the system called metadata. It is also called data dictionary.

Question 63. What Is Meant By Query Optimization?

Answer :

The phase that identifies an efficient execution plan for evaluating a query that has the least estimated cost is referred to as query optimization.

Question 64. What Is Join Dependency And Inclusion Dependency?

Answer :

Join Dependency:

A Join dependency is generalization of Multivalued dependency.A JD {R1, R2, ..., Rn} is said to hold over a relation R if R1, R2, R3, ..., Rn is a lossless-join decomposition of R . There is no set of sound and complete inference rules for JD.

Inclusion Dependency:

An Inclusion Dependency is a statement of the form that some columns of a relation are contained in other columns. A foreign key constraint is an example of inclusion dependency.

Question 65. What Is Durability In Dbms?

Answer :

Once the DBMS informs the user that a transaction has successfully completed, its effects should persist even if the system crashes before all its changes are reflected on disk. This property is called durability.

Question 66. What Do You Mean By Atomicity And Aggregation?

Answer :

Atomicity:
Either all actions are carried out or none are. Users should not have to worry about the effect of incomplete transactions. DBMS ensures this by undoing the actions of incomplete transactions.
Aggregation:
A concept which is used to model a relationship between a collection of entities and relationships. It is used when we need to express a relationship among relationships.

Question 67. What Is A Phantom Deadlock?

Answer :

In distributed deadlock detection, the delay in propagating local information might cause the deadlock detection algorithms to identify deadlocks that do not really exist. Such situations are called phantom deadlocks and they lead to unnecessary aborts.

Question 68. What Is A Checkpoint And When Does It Occur?

Answer :

A Checkpoint is like a snapshot of the DBMS state. By taking checkpoints, the DBMS can reduce the amount of work to be done during restart in the event of subsequent crashes.

Question 69. What Are The Different Phases Of Transaction?

Answer :

Different phases are

Analysis phase
Redo Phase
Undo phase
Question 70. What Do You Mean By Flat File Database?

Answer :

It is a database in which there are no programs or user access languages. It has no cross-file capabilities but is user-friendly and provides user-interface management.

Question 71. What Is "transparent Dbms"?

Answer :

It is one, which keeps its Physical Structure hidden from user.

Question 72. Brief Theory Of Network, Hierarchical Schemas And Their Properties?

Answer :

Network schema uses a graph data structure to organize records example for such a database management system is CTCG while a hierarchical schema uses a tree data structure example for such a system is IMS.

Question 73. What Is A Query?

Answer :

A query with respect to DBMS relates to user commands that are used to interact with a data base. The query language can be classified into data definition language and data manipulation language.

Question 74. What Do You Mean By Correlated Subquery?

Answer :

Subqueries, or nested queries, are used to bring back a set of rows to be used by the parent query. Depending on how the subquery is written, it can be executed once for the parent query or it can be executed once for each row returned by the parent query. If the subquery is executed for each row of the parent, this is called a correlated subquery.
A correlated subquery can be easily identified if it contains any references to the parent subquery columns in its WHERE clause. Columns from the subquery cannot be referenced anywhere else in the parent query. The following example demonstrates a non-correlated subquery.
E.g. Select * From CUST Where '10/03/1990' IN (Select ODATE From ORDER Where CUST.CNUM = ORDER.CNUM)

Question 75. What Are The Primitive Operations Common To All Record Management Systems?

Answer :

Addition, deletion and modification.

Question 76. Name The Buffer In Which All The Commands That Are Typed In Are Stored?

Answer :

‘Edit’ Buffer.

Question 77. What Are The Unary Operations In Relational Algebra?

Answer :

PROJECTION and SELECTION.

Question 78. Are The Resulting Relations Of Product And Join Operation The Same?

Answer :

No.
PRODUCT: Concatenation of every row in one relation with every row in another.
JOIN: Concatenation of rows from one relation and related rows from another.

Question 79. What Is Rdbms Kernel?

Answer :

Two important pieces of RDBMS architecture are the kernel, which is the software, and the data dictionary, which consists of the system-level data structures used by the kernel to manage the database
You might think of an RDBMS as an operating system (or set of subsystems), designed specifically for controlling data access; its primary functions are storing, retrieving, and securing data. An RDBMS maintains its own list of authorized users and their associated privileges; manages memory caches and paging; controls locking for concurrent resource usage; dispatches and schedules user requests; and manages space usage within its table-space structures.

Question 80. Name The Sub-systems Of A Rdbms?

Answer :

I/O, Security, Language Processing, Process Control, Storage Management, Logging and Recovery, Distribution Control, Transaction Control, Memory Management, Lock Management.

Question 81. Which Part Of The Rdbms Takes Care Of The Data Dictionary? How

Answer :

Data dictionary is a set of tables and database objects that is stored in a special area of the database and maintained exclusively by the kernel.

Question 82. What Is The Job Of The Information Stored In Data-dictionary?

Answer :

The information in the data dictionary validates the existence of the objects, provides access to them, and maps the actual physical storage location.

Question 83. Not Only Rdbms Takes Care Of Locating Data It Also?

Answer :

determines an optimal access path to store or retrieve the data.

Question 84. How Do You Communicate With An Rdbms?

Answer :

You communicate with an RDBMS using Structured Query Language (SQL).

Question 85. Define Sql And State The Differences Between Sql And Other Conventional Programming Languages?

Answer :

SQL is a nonprocedural language that is designed specifically for data access operations on normalized relational database structures. The primary difference between SQL and other conventional programming languages is that SQL statements specify what data operations should be performed rather than how to perform them.

Question 86. Name The Three Major Set Of Files On Disk That Compose A Database In Oracle?

Answer :

There are three major sets of files on disk that compose a database. All the files are binary. These are

Database files
Control files
Redo logs
The most important of these are the database files where the actual data resides. The control files and the redo logs support the functioning of the architecture itself.
All three sets of files must be present, open, and available to Oracle for any data on the database to be useable. Without these files, you cannot access the database, and the database administrator might have to recover some or all of the database using a backup, if there is one.

Question 87. What Is An Oracle Instance?

Answer :

The Oracle system processes, also known as Oracle background processes, provide functions for the user processes—functions that would otherwise be done by the user processes themselves Oracle database-wide system memory is known as the SGA, the system global area or shared global area. The data and control structures in the SGA are shareable, and all the Oracle background processes and user processes can use them.
The combination of the SGA and the Oracle background processes is known as an Oracle instance.

Question 88. What Are The Four Oracle System Processes That Must Always Be Up And Running For The Database To Be Useable

Answer :

The four Oracle system processes that must always be up and running for the database to be useable include DBWR (Database Writer), LGWR (Log Writer), SMON (System Monitor), and PMON (Process Monitor).

Question 89. What Is Rowid?

Answer :

The ROWID is a unique database-wide physical address for every row on every table. Once assigned (when the row is first inserted into the database), it never changes until the row is deleted or the table is dropped.
The ROWID consists of the following three components, the combination of which uniquely identifies the physical storage location of the row.

Oracle database file number, which contains the block with the rows
Oracle block address, which contains the row
The row within the block (because each block can hold many rows)
The ROWID is used internally in indexes as a quick means of retrieving rows with a particular key value. Application developers also use it in SQL statements as a quick way to access a row once they know the ROWID.

Question 90. What Is Oracle Block? Can Two Oracle Blocks Have The Same Address?

Answer :

Oracle "formats" the database files into a number of Oracle blocks when they are first created—making it easier for the RDBMS software to manage the files and easier to read data into the memory areas.
The block size should be a multiple of the operating system block size. Regardless of the block size, the entire block is not available for holding data; Oracle takes up some space to manage the contents of the block. This block header has a minimum size, but it can grow.
These Oracle blocks are the smallest unit of storage. Increasing the Oracle block size can improve performance, but it should be done only when the database is first created.
Each Oracle block is numbered sequentially for each database file starting at 1. Two blocks can have the same block address if they are in different database files.

Question 91. What Is Database Trigger?

Answer :

A database trigger is a PL/SQL block that can defined to automatically execute for insert, update, and delete statements against a table. The trigger can be defined to execute once for the entire statement or once for every row that is inserted, updated, or deleted. For any one table, there are twelve events for which you can define database triggers. A database trigger can call database procedures that are also written in PL/SQL.

Question 92. Name Two Utilities That Oracle Provides, Which Are Use For Backup And Recovery.

Answer :

Along with the RDBMS software, Oracle provides two utilities that you can use to back up and restore the database. These utilities are Export and Import.
The Export utility dumps the definitions and data for the specified part of the database to an operating system binary file. The Import utility reads the file produced by an export, recreates the definitions of objects, and inserts the data.
If Export and Import are used as a means of backing up and recovering the database, all the changes made to the database cannot be recovered since the export was performed. The best you can do is recover the database to the time when the export was last performed.

Question 93. What Are Stored-procedures? And What Are The Advantages Of Using Them.

Answer :

Stored procedures are database objects that perform a user defined operation. A stored procedure can have a set of compound SQL statements. A stored procedure executes the SQL commands and returns the result to the client. Stored procedures are used to reduce network traffic.

Question 94. Does Pl/sql Support "overloading"? Explain

Answer :

The concept of overloading in PL/SQL relates to the idea that you can define procedures and functions with the same name. PL/SQL does not look only at the referenced name, however, to resolve a procedure or function call. The count and data types of formal parameters are also considered.
PL/SQL also attempts to resolve any procedure or function calls in locally defined packages before looking at globally defined packages or internal functions. To further ensure calling the proper procedure, you can use the dot notation. Prefacing a procedure or function name with the package name fully qualifies any procedure or function reference.

Question 95. What Is Storage Manager?

Answer :

It is a program module that provides the interface between the low-level data stored in database, application programs and queries submitted to the system.

Question 96. What Is Buffer Manager?

Answer :

It is a program module, which is responsible for fetching data from disk storage into main memory and deciding what data to be cache in memory.

Question 97. What Is Transaction Manager?

Answer :

It is a program module, which ensures that database, remains in a consistent state despite system failures and concurrent transaction execution proceeds without conflicting.

Question 98. What Is File Manager?

Answer :

It is a program module, which manages the allocation of space on disk storage and data structure used to represent information stored on a disk.

Question 99. What Is Authorization And Integrity Manager?

Answer :

It is the program module, which tests for the satisfaction of integrity constraint and checks the authority of user to access data.

Question 100. What Are Stand-alone Procedures?

Answer :

Procedures that are not part of a package are known as stand-alone because they independently defined. A good example of a stand-alone procedure is one written in a SQL*Forms application. These types of procedures are not available for reference from other Oracle tools. Another limitation of stand-alone procedures is that they are compiled at run time, which slows execution.

Question 101. What Are Cursors Give Different Types Of Cursors.

Answer :

PL/SQL uses cursors for all database information accesses statements. The language supports the use two types of cursors.

Implicit
Explicit
Question 102. What Is Meant By Proactive, Retroactive And Simultaneous Update?

Answer :

Proactive Update:
The updates that are applied to database before it becomes effective in real world .

1) What is a data warehouse?
   A data warehouse is a huge store of data accumulated from a broad range of sources within an organization and used to guide business decisions.

Click here for more information
2) What is a dimensional table?
   Dimensional tables include textual attributes of measurement saved in the fact tables. A dimensional table is a group of hierarchies, categories, and logic which can be used for the customer to traverse in hierarchy nodes.

3) What is a fact table?
   The fact table includes the measurement of the business process. Fact table includes the foreign keys for the dimension tables.

Example: If we are business phase is "paper production," "normal production of paper by one device, "or "weekly production of paper" will be treated as a measurement of the business process.

4) What are the different methods of loading dimension tables?
   There are two different methods to load data in dimension tables:

Conventional (slow): All the constraints and keys are validated against the information before, it is loaded, and this method data integrity is maintained.
Direct (fast): All the constraints and keys are disabled before the information is loaded. Once the information is loaded, it is validated against all the constraints and keys. If the data is found invalid, it is not contained in the index, and all the future processes are skipped in this data.
5) Describe the foreign key columns in fact tables and dimension tables?
   Foreign keys of dimension tables are the primary key of entity tables.

Foreign keys of fact tables are the primary key of dimension tables.

6) What is Data Mining?
   Data mining is the phase of analysing data from several perspectives and summarizing it into useful data.

7) What is Business Intelligence?
   Business Intelligence defines the technologies, functions, and systems for the collection, integration, analysis, and demonstration of business data and sometimes to the data itself. The purpose of business intelligence is to provide better business decision making. Thus, BI is also defined as a decision support system (DSS).

8) What is OLTP?
   OLTP stands for online transaction processing. This system is a function that modifies data the instance it receives and has a huge number of concurrent users.

9) What is OLAP?
   OLAP stands for online analytical processing. This system is a function that collects, manages, processes, and presents multidimensional data for analysis and management process.

10) What is the difference between OLTP and OLAP?
    Basic	OLTP	OLAP
    Meaning	OLTP stands for online transaction processing.	OLAP stands for online analytical processing.
    Data Source	Operational data is initial data source of data.	Consolidation data is from different sources.
    Process Goal	Snapshot of business processes which does essential business tasks	Multidimensional view of business events of planning and decision making
    Queries and Process scripts	Simple quick running queries ran by customers.	Complex long-running queries by a scheme to update the aggregate data.
    Database Design	Normalize small databases. Speed will not be an issue due to the smaller database, and normalization will not degrade performance. This adopts an entity-relationship (ER) model and function-oriented database design.	De-normalized large databases. Speed is an issue due to the larger databases, and de-normalizing will improve performance as there will be lesser tables to scan while performing tasks. This adopts star, snowflake, or fact constellation mode of subject-oriented database design.
    Back-up and system administration	Regular database back-up and system administration can do the job.	Reloading the OLTP data is well treated as a good backup option.
    Click here for more information
11) What is ODS?
    ODS stands for Operational data store. A database architecture that is a repository for near real-time operational records rather than long term trend data. The ODS may further become the enterprise shared an operational database, allowing operational functions that are being re-engineered to use the ODS as there operational databases.

Click here for more information
12) What is ETL?
    ETL stands for extraction, transformation, and loading process. ETL is software that allows the business to develop their disparate records while moving it from place to place, and it doesn't really matter that data is in several forms or formats. The data can come from any source. ETL is powerful enough to manage such data disparities.

First, the extract function reads data from a particular source database and extracts a desired subset of data.

Second, the transform function works with the acquired record using rules or lookup tables, or creating a combination with other records to convert it to the desired state.

Finally, the load function is used to write the resulting information to a target database.

Click here for more information
13) What is VLDB?
    VLDB stands for a Very large database. A one terabyte database would generally be considered to be a VLDB. Typically, there are decision support applications or transaction processing applications serving a huge number of users.

14) What is real-time data warehousing?
    Data warehousing capture business event data. Real-time data warehousing capture business event data as it occurs. As soon as the business event is complete, and there is data about it, the completed event data flows into the data warehouse and becomes feasible instantly.

15) What are conformed dimensions?
    Conformed dimension defines the exact same thing with every possible fact table to which they are joined. They are simple to the cubes.

16) What are non-additive facts?
    Non-additive facts are the facts that cannot be examined for any of the dimensions present in the fact table. They are not treated as useless. If there is a transformation in dimensions, the same facts can be useful.

17) What is Star Schema?
    Star schema is a type of organizing the tables such that we can fetch the result from the database instantly in the warehouse environment.

Click here for more information
18) What is a Snowflake Schema?
    Any dimension with extended dimensions is called snowflake schema, the dimension may be interlinked or may have one too many relationships with other tables. This schema is normalized and outcome in complex join and very complex queries as well as slower results.

Click here for more information
19) What is a surrogate key?
    A surrogate key is a substitution for the essential primary key. It is just a unique identifier or statistic for each row that can be used for the primary key to the table. The only requirement for a surrogate primary key is that it is unique for each row in the table. It is useful because the essential primary key can change, and this makes updates more difficult. Surrogate keys are always integer or numeric.

20) What is a junk dimension?
    A number of very small dimension may be lumped together to form a single dimension, a junk dimension is the attributes are not closely related. Grouping of random flags and text attributes in dimensions and changing them to a separate subdimension is called the junk dimension.

21) What is dimensional modeling?
    Dimensional data model concept contains two types of tables, and it is different from the third normal form. This concept uses a fact table, which includes the measurement of the business and Dimensional tables, which includes the context (dimension of the calculations) of the dimensions.

Click here for more information
22) What is BUS Schema?
    BUS schema is collected from a master suite of confirmed size and a standardized description of facts.

23) What is active data warehousing?
    An active data warehouses provide data that allow decision-makers within an organization to handle customer relationships efficiently and proactively.

24) What is the difference between data warehousing and Business Intelligence?
    Data warehousing handle with all methods of managing the development, implementation and applications of a data warehouse or data mart containing metadata management, data acquisition, data cleansing, data transformation, storage management, data distribution, data archiving, operational documenting, analytical documenting, security management, backup/recovery planning, etc.

Business Intelligence is a set of software tools that allows an organization to analyse measurable methods of their business, such as sales performance, profitability, operational efficiency, effectiveness, of marketing campaigns, market penetration among certain user groups, cost trends, anomalies and exceptions, etc. Business Intelligence is used to encompass OLAP, data visualization, data mining, and query document tools.

25) Which one is faster, Multidimensional OLAP, or Relational OLAP?
    Multidimensional OLAP (MOLAP) is faster than Relational OLAP (ROLAP).

MOLAP: Here, data is saved in a multidimensional cube. The storage is not in the relational database but in a proprietary plan (one example is PowerOLAP's .olp file). MOLAP products are compatible with Excel, which can make record interactions easy to learn.
ROLAP: ROLAP products approach a relational database by using SQL (structured query language), which is the standard language that is used to describe and manipulate data in an RDBMS. Subsequent processing may occur in the RDBMS or within a middle-tier server, which accepts requests from users, translates them into SQL statements, and passes them on to the RDBMS.