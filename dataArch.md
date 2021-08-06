What Is The Main Difference Between View And Materialized View?
The main difference between view and materialized view is as follows:
+ View:
  + Data representation is provided by view where the data is accessed from its table.
  + View has a logical structure which does not occupy space
  + All the changes are affected in corresponding tables.
+ Materialized View:
  + Within materialized view, pre-calculated data is available
  + The materialized view has a physical structure which does occupy space
  + All the changes are not reflected in the corresponding tables.


What Is Junk Dimension?
A junk dimension is nothing but a dimension where a certain type of data is stored which is not appropriate to store in the schema. The nature of the junk dimension is usually a Boolean has flag values.
A single dimension is formed by a group of small dimensions got together. This can be considered as junk dimension.


What Is Data Warehouse Architecture?
The data warehouse architecture is a three-tier architecture.
The following is the three-tier architecture:
+ Bottom Tier
+ Middle Tier
+ Upper Tier

It is nothing but a repository of integrating data which is extracted from different data sources.

What Is An Integrity Constraints? What Are Different Types Of Integrity Constraints?
An integrity constraint is nothing but a specific requirement that the data in the database has to meet. It is nothing but a business rule for a particular column in a table. In the data warehouse concept, they are 5 integrity constraints.
The following are the integrity constraints:
+ Null
+ Unique key
+ Primary key
+ Foreign key
+ Check

Why Is That Data Architect Actually Monitor And Enforce Compliance Data Standards? What Is The Need?
The primary idea of keeping the standards high on compliance for data standards is because it will help to reduce the data redundancy and helps the team to have a quality data. As this information is actually carried out or used throughout the organization.

Explain The Different Data Models That Are Available In Detail?
There are three different kinds of data models that are available and they are as follows:
+ Conceptual
+ Logical
+ Physical

Conceptual data model:
+ As the name itself implies that this data model depicts the high-level design of the available physical data.

Logical data model:
+ Within the logical model, the entity names, entity relationships, attributes, primary keys and foreign keys will show up.

Physical data model:
+ Based on this data model, the view will give out more information and showcases how the model is implemented in the database. All the primary keys, foreign keys, tables names and column names will be showing up.

Differentiate Between Dimension And Attribute?
In short, dimensions are nothing but which represents qualitative data. For example data like a plan, product, class are all considered as dimensions.
The attribute is nothing but a subset of a dimension. Within a dimension table, we will have attributes. The attributes can be textual or descriptive. For example, product name and product category are nothing but an attribute of product dimensions.

Differentiate Between Oltp And Olap?
OLTP stands for Online Transaction Process System
OLTP is known for maintaining transactional level data of the organization and generally, they are highly normalized. If it is OLTP route then it is going to be a star schema design.
OLAP stands for Online Analytical process system.
OLAP is known for a lot of analysis and fulfills reporting purposes. It is de-normalized form.
If it is an OLAP route then it is going to be a snowflake schema design.

How To Become A Data Architect?
The following are the prerequisites for an individual to start his career in Data Architect.
No predefined certifications are necessary, but it is always good to have few certifications related to the field because few of the companies might expect. It is advisable to go through CDMA (Certified )
Data Management Professional)
Should have at least 3-8 years of IT experience.
Should be creative, innovative and good at problem-solving.
Has good programming knowledge and data modeling concepts
Should be well versed with the tools like SOA, ETL, ERP, XML etc

The Responsibilities Of A Data Architect And Data Administrator Are The Same?
No, not at all. The responsibilities of data architect are completely different from that of data administrator.
For example:
Data architect works on with data modeling and designs the database design in a robust manner where the users will be able to extract the information easily. When it comes to data administrators, they are responsible for having the databases run efficiently and effectively.

Is Data Architect And Data Scientist Roles Are Similar?
No, data architect and data scientist roles are two different roles in an organization.
The following are few activities that data architect is involved :
+ Data warehousing solutions
+ ETL activities
+ Data Architecture development activities
+ Data modelling

The following are few activities that data scientist is involved in:
+ Data cleansing and processing
+ Predictive modelling
+ Machine learning
+ Statistical analysis applied
+ Data visualization

How Can We Run The Graph? What Is The Procedure For That? How Can We Schedule The Graph In Unix?
If you want to run the graph through GDE then after save the graph just press F5 button of your keyboard, it will run automatically. If you want to run through the shell script then you have to fire the command at your UNIX box.

What Is A Real-time Data Warehouse? How Is It Different From Near To Real-time Data Warehouse?
As the term suggests, a real-time data warehouse is a system, which reflects all changes to its sources in real time. As simple as it sounds, this is still an area of active research in the field. In traditional DWH, the operational system(s) are kept separate from the DWH for a good reason.
The Operational systems are designed to accept inputs or changes to data regularly, hence have a good chance of being regularly queried. On the other hand, a DWH is supposed to do just the opposite - it is used to query data for reports only. No changes to data, through user actions is expected (or designed). The only inputs could come from the ETL feed at stipulated times.
The ETL would source its data from the Operational systems just explained above.
To create a real-time DWH we would have to merge both systems (several ways are being explored), a concept that is against the reason of creating a DWH. Bigger challenges occur in terms of updating aggregated data in facts at real time, still maintaining the surrogate keys.
Besides, we would need lightening fast hardware to try this.Near Real time DWH is a trade-off between the conventional design and the dream of all clients today. The frequency of ETL updates in higher in this case for e.g. once in 2 hours. We can also analyze and use selective refreshes at shorter time intervals, while complete refreshes may still be kept further apart. Selective refreshes would look at only those tables that get updated regularly.

What Is Difference Between Drill & Scope Of Analysis?
Drilling can be done in drill down, up, through, and across; scope is the overall view of the drill exercise.

I Have Two Universes Created By Two Difference Database Can We Join Them In Designer & Report Level? How
We can link one universe to other universe in Universe parameters.

For Faster Process, What We Will Do With The Universe?
For a faster process create aggregate tables and write better sql so that the process would fast.

What Is Type 2 Version Dimension?
Version dimension is the SCD type II in real time it using because of it will maintain the current data and full historical data.

What Is Unit Testing?
The Developer created the mapping that can be tested independently by the developer individually.

What Is Informatica Architecture?
Informatica Architecture contains Repository, Repository server, Repository server administration console, sources, repository server and Data warehousing and it have the Designer, Work for manager, work for monitor combination of all these are called Informatica Architecture.

What Is Data Warehouse Architecture?
Data warehousing is the repository of integrated information data will be extracted from the heterogeneous sources. Data warehousing architecture contains the different; sources like oracle, flat files and ERP then after it have the staging area and Data warehousing, after that it has the different Data marts then it have the reports and it also have the ODS - Operation Data Store. This complete architecture is called the Data warehousing Architecture.

What Is Data Analysis? Where It Will Be Used?
Data analysis: consider that you are running a business and u store the data of that; in some form say in register or in a comp and at the year end you want know the profit or loss then it called data analysis .Data analysis use: then u want to know which product was sold the highest and if the business is running in a loss then finding, where we went wrong we do analysis.

What Are Data Modeling And Data Mining? Where It Will Be Used?
Data modeling is the process of designing a data base model. In this data model data will be stored in two types of table fact table and dimension table.
Fact table contains the transaction data and dimension table contains the master data. Data mining is process of finding the hidden trends is called the data mining.

After The Generation Of A Report To Whom We Have To Deploy Or What We Do After The Completion Of A Report?
The generated report will be sent to the concerned business users through web or LAN.

After The Complete Generation Of A Report Who Will Test The Report And Who Will Analyze It?
After the completion of reporting, reports will be sent to business analysts. They will analyze the data from different points of view so that they can make a proper business decisions.

Can You Pass Sql Queries In Filter Transformation?
We cannot use sql queries in filter transformation. It will not allow you to override default sql query like other transformations (Source Qualifier, lookup)

Where The Data Cube Technology Is Used?
A multi-dimensional structure called the data cube. A data abstraction allows one to view aggregated data from a number of perspectives. Conceptually, the cube consists of a core or base cuboids, surrounded by a collection of sub-cubes/cuboids that represent the aggregation of the base cuboids along one or more dimensions. We refer to the dimension to be aggregated as the measure attribute, while the remaining dimensions are known as the feature attributes.

How Can You Implement Many Relations In Star Schema Model?
Many-many relations can be implemented by using snowflake schema .With a max of n dimensions.

What Is Critical Column?
Let us take one ex: Suppose 'XYZ' is customer in Bangalore, he was residing in the city from the last 5 years, in the period of 5 years he has made purchases worth of 3 lacs. Now, he moved to 'HYD'. When you update the 'XYZ' city to 'HYD' in your Warehouse, all the purchases by him will show in city 'HYD' only. This makes warehouse inconsistent. Here CITY is the Critical Column. Solution is use Surrogate Key.

What Is The Main Difference Between Star And Snowflake Star Schema? Which One Is Better And Why?
If u have one to may relation ship in the data then only we choose snowflake schema, as per the performance-wise every-one go for the Star schema. Moreover, if the ETL is concerned with reporting means choose for snowflake because this schema provides more browsing capability than the former schema.

What Is The Difference Between Dependent Data Warehouse And Independent Data Warehouse?
Dependent departments are those, which depend on a data ware to for their data.Independent department are those, which get their data directly from the operational data sources in the organization.

Which Technology Should Be Used For Interactive Data Querying Across Multiple Dimensions For A Decision Making For A Dw?
MOLAP

What Is Virtual Data Warehousing?
A virtual or point-to-point data warehousing strategy means that end-users are allowed to get at operational databases directly using whatever tools are enabled to the "data access network".

What Is The Difference Between Metadata And Data Dictionary?
Meta data is nothing but information about data. It contains the information (i.e. data) about the graphs, its related files, abinitio commands, server information etc i.e. all kinds of information about project related information etc.

What Is The Difference Between Mapping Parameter & Mapping Variable In Data Warehousing?
Mapping Parameter defines the constant value and it cannot change the value throughout the session. Mapping Variables defines the value and it can be change throughout the session.

Explain The Advantages Of Raid 1, 1/0, And 5. What Type Of Raid Setup Would You Put Your Tx Logs.
The basic advantage of RAID is to speed up the data reading from permanent storage device (hard disk).

What Are The Characteristics Of Data Files?
A data file can be associated with only one database. Once created a data file can't change size. One or more data files form a logical unit of database storage called a table space.

What Is Rollback Segment?
A Database contains one or more Rollback Segments to temporarily store "undo" information.

What Is A Table Space?
A database is divided into Logical Storage Unit called table spaces. A table space is used to grouped related logical structures together.

What Is Database Link?
A database link is a named object that describes a "path" from one database to another.

What Is A Private Synonyms?
A Private Synonyms can be accessed only by the owner.

What Is A Hash Cluster?
A row is stored in a hash cluster based on the result of applying a hash function to the row's cluster key value. All rows with the same hash key value are stores together on disk.

Describe Referential Integrity?
A rule defined on a column (or set of columns) in one table that allows the insert or update of a row only if the value for the column or set of columns (the dependent value) matches a value in a column of a related table (the referenced value). It also specifies the type of data manipulation allowed on referenced data and the action to be performed on dependent data as a result of any action on referenced data.

What Is Schema?
A schema is collection of database objects of a User.

What Is Table?
A table is the basic unit of data storage in an ORACLE database. The tables of a database hold all of the user accessible data. Table data is stored in rows and columns.

What Is A View?
A view is a virtual table. Every view has a Query attached to it. (The Query is a SELECT statement that identifies the columns and rows of the table(s) the view uses.)

What Is An Extent?
An Extent is a specific number of contiguous data blocks, obtained in a single allocation, and used to store a specific type of information.

What Is An Index?
An Index is an optional structure associated with a table to have direct access to rows, which can be created to increase the performance of data retrieval. Index can be created on one or more columns of a table.

What Is An Integrity Constrains?
An integrity constraint is a declarative way to define a business rule for a column of a table.

What Are Clusters?
Clusters are groups of one or more tables physically stores together to share common columns and are often used together.

What Are The Different Types Of Segments?
Data Segment,
Index Segment,
Rollback Segment
and
Temporary Segment.

Explain The Relationship Among Database, Table Space And Data File?
Each databases logically divided into one or more table spaces one or more data files are explicitly created for each table space.

What Is An Index Segment?
Each Index has an Index segment that stores all of its data.

What Is A Redo Log?
The set of Redo Log files YSDATE, UID, USER or USERENV SQL functions, or the pseudo columns LEVEL or ROWNUM.

What Are The Types Of Synonyms?
There are two types of Synonyms Private and Public.

What Are The Referential Actions Supported By Foreign Key Integrity Constraint?
Update And Delete Restrict - A referential integrity rule that disallows the update or deletion of referenced data. DELETE Cascade - When a referenced row is deleted all associated dependent rows are deleted.

Do You View Contain Data?
Views do not contain or store data.

What Is The Use Of Control File?
When an instance of an ORACLE database is started, its control file is used to identify the database and redo log files that must be opened for database operation to proceed. It is also used in database recovery.

Can Objects Of The Same Schema Reside In Different Table Spaces?
Yes

Can A Table Space Hold Objects From Different Schemes?
Yes

Can A View Based On Another View?
Yes

What Is A Full Backup?
A full backup is an operating system backup of all data files, on- line redo log files and control file that constitute ORACLE database and the parameter.

What Is Mirrored On-line Redo Log?
A mirrored on-line redo log consists of copies of on-line redo log files physically located on separate disks; changes made to one member of the group are made to all members.

What Is Partial Backup?
A Partial Backup is any operating system backup short of a full backup, taken while the database is open or shut down.

What Is Restricted Mode Of Instance Startup?
An instance can be started in (or later altered to be in) restricted mode so that when the database is open connections are limited only to those whose user accounts have been granted the RESTRICTED SESSION system privilege.

What Is Archived Redo Log?
Archived Redo Log consists of Redo Log files that have archived before being reused.

What Are The Steps Involved In Database Shutdown?
Close the Database; Dismount the Database and Shutdown the Instance.

What Are The Advantages Of Operating A Database In Archivelog Mode Over Operating It In No Archivelog Mode?
Complete database recovery from disk failure is possible only in ARCHIVELOG mode. Online database backup is possible only in ARCHIVELOG mode.

What Are The Different Modes Of Mounting A Database With The Parallel Server?
Exclusive Mode If the first instance that mounts a database does so in exclusive mode, only that Instance can mount the database. Parallel Mode If the first instance that mounts a database is started in parallel mode, other instances that are started in parallel mode can also mount the database.

Can Full Backup Be Performed When The Database Is Open?
No

What Are The Steps Involved In Instance Recovery?
Rolling forward to recover data that has not been recorded in data files yet has been recorded in the on-line redo log, including the contents of rollback segments. Rolling back transactions that have been explicitly rolled back or have not been committed as indicated by the rollback segments regenerated in step a.
1) Releasing any resources (locks) held by transactions in process at the time of the failure.
2) Resolving any pending distributed transactions undergoing a two-phase commit at the time of the instance failure.

What Are The Steps Involved In Database Startup?
Start an instance, Mount the Database and Open the Database.

Which Parameter Specified In The Default Storage Clause Of Create Tablespace Cannot Be Altered After Creating The Table Space?
All the default storage parameters defined for the table space can be changed using the ALTER TABLESPACE command. When objects are created their INITIAL and MINEXTENS values cannot be changed.

What Is On-line Redo Log?
The On-line Redo Log is a set of tow or more on-line redo files that record all committed changes made to the database. Whenever a transaction is committed, the corresponding redo entries temporarily stores in redo log buffers of the SGA are written to an on-line redo log file by the background process LGWR. The on-line redo log files are used in cyclical fashion.

What Is Log Switch?
The point at which ORACLE ends writing to one online redo log file and begins writing to another is called a log switch.

What Is Dimensional Modelling?
Dimensional Modelling is a design concept used by many data warehouse designers to build their data warehouse. In this design model all the data is stored in two types of tables - Facts table and Dimension table. Fact table contains the facts/measurements of the business and the dimension table contains the context of measurements i.e., the dimensions on which the facts are calculated.

What Are The Difference Between Snow Flake And Star Schema? What Are Situations Where Snow Flake Schema Is Better Than Star Schema To Use And When The Opposite Is True?
Star schema contains the dimension tables mapped around one or more fact tables. It is a renormalized model and no need to use complicated joins. Also queries results fast.Snowflake schema: It is the normalized form of Star schema. It contains in-depth joins, because the tables are split in to many pieces. We can easily do modification directly in the tables. We have to use complicated joins, since we have more tables.There will be some delay in processing the query.

What Is A Cube In Data Warehousing Concept?
Cubes are logical representation of multidimensional data. The edge of the cube contains dimension members and the body of the cube contains data values.

What Are The Differences Between Star And Snowflake Schema?
Star schema: A single fact table with N number of DimensionSnowflake schema: Any dimensions with extended dimensions are known as snowflake schema.

What Are Data Marts?
A data mart is a collection of tables focused on specific business group/department. It may have multi-dimensional or normalized. Data marts are usually built from a bigger data warehouse or from operational data.

What Is The Data Type Of The Surrogate Key?
There is no data type for a Surrogate Key. Requirement of a surrogate Key: UNIQUE Recommended data type of a Surrogate key is NUMERIC.

What Are Fact, Dimension, And Measure?
Fact is key performance indicator to analyze the business. Dimension is used to analyze the fact. Without dimension there is no meaning for fact.

What Are The Different Types Of Data Warehousing?
Types of data warehousing are:
1. Enterprise Data warehousing
2. ODS (Operational Data Store)
3. Data Mart

What Do You Mean By Static And Local Variable?
Static variable is not created on function stack but is created in the initialized data segment and hence the variable can be shared across the multiple call of the same function. Usage of static variables within a function is not thread safe.On the other hand, local variable or auto variable is created on function stack and valid only in the context of the function call and is not shared across function calls.

What Is A Source Qualifier?
When you add a relational or a flat file source definition to a mapping, you need to connect it to a Source Qualifier transformation. The Source Qualifier represents the rows that the Informatica Server reads when it executes a session.

What Are The Steps To Build The Data Warehouse?
Gathering business requirements>>Identifying Sources>>Identifying Facts>>Defining Dimensions>>Define Attributes>>Redefine Dimensions / Attributes>>Organize Attribute Hierarchy>>Define Relationship>>Assign Unique Identifiers.

What Is The Advantages Data Mining Over Traditional Approaches?
Data Mining is used for the estimation of future. For example, if we take a company/business organization, by using the concept of Data Mining, we can predict the future of business in terms of Revenue (or) Employees (or) Customers (or) Orders etc.Traditional approaches use simple algorithms for estimating the future. However, it does not give accurate results when compared to Data Mining.

What Is The Difference Between View And Materialized View?
View - store the SQL statement in the database and let you use it as a table. Every time you access the view, the SQL statement executes. Materialized view - stores the results of the SQL in table form in the database. SQL statement only executes once and after that every time you run the query, the stored result set is used. Pros include quick query results.

What Is The Main Difference Between Inmon And Kimball Philosophies Of Data Warehousing?
Both differed in the concept of building the data warehouse.According to Kimball, Kimball views data warehousing as a constituency of data marts. Data marts are focused on delivering business objectives for departments in the organization. And the data warehouse is a conformed dimension of the data marts. Hence, a unified view of the enterprise can be obtained from the dimension modeling on a local departmental level.Inmon beliefs in creating a data warehouse on a subject-by-subject area basis. Hence, the development of the data warehouse can start with data from the online store. Other subject areas can be added to the data warehouse as their needs arise. Point-of-sale (POS) data can be added later if management decides it is necessary.

What Is Junk Dimension? What Is The Difference Between Junk Dimension And Degenerated Dimension?
Junk dimension: Grouping of Random flags and text attributes in a dimension and moving them to a separate sub dimension. Degenerate Dimension: Keeping the control information on Fact table ex: Consider a Dimension table with fields like order number and order line number and have 1:1 relationship with Fact table, In this case this dimension is removed and the order information will be directly store.

Why Fact Table Is In Normal Form?
The fact table consists of the Index keys of the dimension/look up tables and the measures. So whenever we have the keys in a table. That it implies that the table is in the normal form.

What Is Difference Between E-r Modeling And Dimensional Modeling?
Basic difference is E-R modeling will have logical and physical model. Dimensional model will have only physical model. E-R modeling is used for normalizing the OLTP database design.Dimensional modeling is used for de-normalizing the ROLAP/MOLAP design.

Question 82. What Is Conformed Fact?
Conformed dimensions are the dimensions, which can be used across multiple Data Marts in combination with multiple facts tables accordingly.

What Are The Methodologies Of Data Warehousing?
Every company has methodology of their own. However, to name a few SDLC Methodology, AIM methodology is standard used.

What Is Bus Schema?
BUS Schema is composed of a master suite of confirmed dimension and standardized definition if facts.

What Is Data Warehousing Hierarchy?
Hierarchies are logical structures that use ordered levels as a means of organizing data. A hierarchy can be used to define data aggregation. For example, in a time dimension, a hierarchy might aggregate data from the month level to the quarter level to the year level. A hierarchy can also be used to define a navigational drill path and to establish a family structure.Within a hierarchy, each level is logically connected to the levels above and below it. Data values at lower levels aggregate into the data values at higher levels. A dimension can be composed of more than one hierarchy. For example, in the product dimension, there might be two hierarchies--one for product categories and one for product suppliers.Dimension hierarchies also group levels from general to granular. Query tools use hierarchies to enable you to drill down into your data to view different levels of granularity. This is one of the key benefits of a data warehouse.When designing hierarchies, you must consider the relationships in business structures. Hierarchies impose a family structure on dimension values. For a particular level value, a value at the next higher level is its parent, and values at the next lower level are its children. These familial relationships enable analysts to access data quickly.

What Are Data Validation Strategies For Data Mart Validation After Loading Process?
Data validation is to make sure that the loaded data is accurate and meets the business requirements. Strategies are different methods followed to meet the validation requirements.

What Are The Data Types Present In Bo? What Happens If We Implement View In The Designer N Report?
Three different data types: Dimensions, Measure, and DetailView is nothing but an alias and it can be used to resolve the loops in the universe.

What Is Surrogate Key? Where We Use It? Explain With Examples.
Surrogate key is a substitution for the natural primary key.It is just a unique identifier or number for each row that can be used for the primary key to the table. The only requirement for a surrogate primary key is that it is unique for each row in the table.
Data warehouses typically use a surrogate, (also known as artificial or identity key), key for the dimension tables primary keys. They can use Info sequence generator, or Oracle sequence, or SQL Server Identity values for the surrogate key.
It is useful because the natural primary key (i.e. Customer Number in Customer table) can change and this makes updates more difficult.
Some tables have columns such as AIRPORT_NAME OR CITY_NAME which are stated as the primary keys (according to the business users) but ,not only can these change, indexing on a numerical value is probably better and you could consider creating a surrogate key called, say, AIRPORT_ID. This would be internal to the system and as far as the client is concerned, you may display only the AIRPORT_NAME.

What Is A Linked Cube?
Linked cube in which a sub-set of the data can be analyzed into detail. The linking ensures that the data in the cubes remain consistent.

What Is Meant By Metadata In Context Of A Data Warehouse And How It Is Important?
Metadata is the data about data; Business Analyst or data modeler usually capture information about data - the source (where and how the data is originated), nature of data (char, varchar, nullable, existence, valid values etc) and behavior of data (how it is modified / derived and the life cycle) in data dictionary.
Metadata is also presented at the Datamart level, subsets, fact and dimensions, ODS etc. For a DW user, metadata provides vital information for analysis / DSS.

What Are The Possible Data Marts In Retail Sales?
Product information and sales information.

What Are The Various Etl Tools In The Market?
Various ETL tools used in market are Informatica Data Stage Oracle Warehouse Builder Ab Initio Data Junction.

What Is Dimensional Modeling?
Dimensional Modeling is a design concept used by many data warehouse designers to build their data warehouse. In this design model all the data is stored in two types of tables - Facts table and Dimension table. Fact table contains the facts/measurements of the business and the dimension table contains the context of measurements i.e., the dimensions on which the facts are calculated.Dimension modeling is a method for designing data warehouse. Three types of modeling are there
1. Conceptual modeling
2. Logical modeling
3. Physical modeling.

What Is Vldb?
The perception of what constitutes a VLDB continues to grow. A one-terabyte database would normally be considered VLDB.Degenerate dimension: it does not have any link with dimensions and it will not have any attribute.

What Is Degenerate Dimension Table?
Degenerate Dimensions: If a table contains the values, which r neither dimension nor measures is called degenerate dimensions. For example invoice id, employee no.A degenerate dimension is data that is dimensional in nature but stored in a fact table.

What Is Er Diagram?
The Entity-Relationship (ER) model was originally proposed by Peter in 1976 [Chen76] as a way to unify the network and relational database views. Simply stated the ER model is a conceptual data model that views the real world as entities and relationships. A basic component of the model is the Entity-Relationship diagram, which is used to visually represent data objects. Since Chen wrote his paper the model has been extended and today it is commonly used for database design for the database designer, the utility of the ER model is: it maps well to the relational model. The constructs used in the ER model can easily be transformed into relational tables. It is simple and easy to understand with a minimum of training. Therefore, the database designer to communicate the design to the end user can use the model. In addition, the model can be used as a design plan by the database developer to implement a data model in specific database management software.

What Is The Difference Between Snowflake And Star Schema? What Are Situations Where Snowflake Schema Is Better Than Star Schema When The Opposite Is True?
Star schema contains the dimension tables mapped around one or more fact tables.It is a renormalized model and no need to use complicated joins. Also Queries results fast.Snowflake schema is the normalized form of Star schema. It contains in-depth joins, because the tables are spited in to many pieces. We can easily do modification directly in the tables.We have to use complicated joins, since we have more tables. There will be some delay in processing the Query.

What Is The Difference Between Star And Snowflake Schemas?
Star schema:
A single fact table with N number of DimensionSnowflake schema: Any dimensions with extended dimensions are known as snowflake schema.

Can A Dimension Table Contain Numeric Values?
Yes. However, those data type will be char (only the values can numeric/char).Yes, dimensions even contain numerical because these are descriptive elements of our business.

What Is Hybrid Slowly Changing Dimension?
Hybrid SCDs are combination of both SCD 1 and SCD 2.It may happen that in a table, some columns are important and we need to track changes for them i.e. capture the historical data for them whereas in some columns even if the data changes, we don't care.For such tables we implement Hybrid SCDs, where in some columns are Type 1 and some are Type 2.You can add that it is not an intelligent key but similar to a sequence number and tied to a timestamp typically!

How Many Clustered Indexes Can U Create For A Table In Dwh? In Case Of Truncate And Delete Command What Happens To Table, Which Has Unique Id.
You can have only one clustered index per table. If you use delete command, you can rollback... it fills your redo log files.
If you do not want records, you may use truncate command, which will be faster and does not fill your redo log file.

What Is Loop In Data Warehousing?
In DWH loops may exist between the tables. If loops exist, then query generation will take more time, because more than one path is available. It creates ambiguity also. Loops can be avoided by creating aliases of the table or by context.
Example: 4 Tables - Customer, Product, Time, Cost forming a close loop. Create alias for the cost to avoid loop.

What Is An Error Log Table In Informatica Occurs And How To Maintain It In Mapping?
Error Log in Informatica is a one of output file created by Informatica Server while running the session for error messages. It is created in Informatica home directory.

How Many Different Schemas Or Dw Models Can Be Used In Siebel Analytics. I Know Only Star And Snow Flake And Any Other Model That Can Be Used?
Integrated schema design is also used to define an integrated schema design we have to define the following concepts
► Fact constellation
► Act less fact table
► Onformed dimension
A: A fact constellation is the process of joining two or more fact tables
B: A fact table with out any facts is known as fact less fact table
C:A dimension which is re useful and fixed is known as conformed dimensionA dimension, which is, shared with multiple fact tables known as conformed dimension.

What Is Drilling Across?
Drill across corresponds to switching from 1 classification in 1 dimension to a different classification in different dimension.

How Can You Import Tables From A Database?
In Business Objects Universe Designer you can open Table Browser and select the tables needed then insert them to designer.

Where The Cache Files Stored?
Caches are stored in Repository.

What Is Dimension Modeling?
A logical design technique that seeks to present the data in a standard, intuitive framework that allows for high-performance access. There are different data modeling concepts like ER Modeling (Entity Relationship modeling), DM (Dimensional modeling), Hierarchal Modeling, Network modeling. However, popular are ER and DM only.

What Is Data Cleaning? How Can We Do That?
Data cleaning is a self-explanatory term. Most of the data warehouses in the world source data from multiple systems - systems that were created long before data warehousing was well understood, and hence without the vision to consolidate the same in a single repository of information. In such a scenario, the possibilities of the following are there:
► Missing information for a column from one of the data sources;
► Inconsistent information among different data sources;
► Orphan records;
► Outlier data points;
► Different data types for the same information among various data sources, leading to improper conversion;
► Data breaching business rules
In order to ensure that the data warehouse is not infected by any of these discrepancies, it is important to cleanse the data using a set of business rules, before it makes its way into the data warehouse.

Can Any One Explain The Hierarchies Level Data Warehousing.
In Data warehousing, levels are columns available in dimension table. Levels are having attributes. Hierarchies are used for navigational purpose; there are two types of Hierarchies. You can define hierarchies in top down or bottom up.
1. Natural Hierarchy: Best example is Time Dimension - Year, Month, Day etc. In natural Hierarchy definite relationship exists between each level
2. Navigational Hierarchy: You can have levels like
   Ex - Production cost of Product, Sales Cost of Product.
   Ex - Lead Time defined to procure, Actual Procurement time,
   In this, two levels need not to have relationship. This Hierarchy is created for navigational purpose.

Can Any One Explain About Core Dimension, Balanced Dimension, And Dirty Dimension?
Dirty Dimension is nothing but Junk Dimensions. Core Dimensions are dedicated for a fact table or Data mart. Conformed Dimensions are used across fact tables or Data marts.

How Much Data Hold In One Universe.
Universe does not hold any data. However, practically the universe is known to have issues when the objects cross 6000.

What Is Core Dimension?
Core Dimension is a Dimension table, which is used dedicated for single fact table or Datamart. Conform Dimension is a Dimension table which is used across fact tables or Data marts.

After We Create A Scd Table, Can We Use That Particular Dimension As A Dimension Table For Star Schema?
Yes.

Suppose You Are Filtering The Rows Using A Filter Transformation Only The Rows Meet The Condition Pass To The Target. Tell Me Where The Rows Will Go That Does Not Meet The Condition.
Informatica filter transformation default value is 1 i.e. true. If you place a break point on filter transformation and run the mapping in a debugger mode, you will find these values 1 or 0 for each row passing through filter. If you change 0 to 1, the particular row will be passed to next stage.

What Is Galaxy Schema?
Galaxy schema is also known as fact constellation scheme. It requires no of fact tables to share dimension tables. In data, wares housing mainly the people are using the conceptual hierarchy.

Briefly State Different Between Data Ware House & Data Mart?
Data warehouse is made up of many datamarts. DWH contain many subject areas. However, data mart focuses on one subject area generally. E.g. If there will be DHW of bank then there can be one data mart for accounts, one for Loans etc. This is high-level definitions.

What Is Meta Data?
Metadata is data about data. E.g. if in data mart we are receiving any file. Then metadata will contain information like how many columns, file is fix width/limited, ordering of fields, data types of field etc.

What Is Data Mart?
Data Marts is used on a business division/department level. A data mart only contains the required subject specific data for local analysis. A database, or collection of databases, designed to help managers make strategicdecisions about their business. data marts are usually smaller and focus on a particular subject or department. Some data marts, called dependent data marts, are subsets of larger data warehouses. A data mart is a simpler form of a data warehouse focused on a single subject (or functional area) such as sales, finance, marketing, HR etc. Data Mart represents data from single business process.

What Is The Definitions For Datawarehose And Datamart?
Datamart is subset of Datawarehouse we can say a datamart is collection of individual departmental information...Where as datawarehouse in collection of datamart.
Data mart is a single subject and datawarehouse is a integration of multiple subjects.

What Are Data Marts
Data Mart is a segment of a data warehouse that can provide data for reporting and analysis on a section, unit, department or operation in the company, e.g. sales, payroll, production. Data marts are sometimes complete individual data warehouses which are usually smaller than the corporate data warehouse.

What Is The Difference Between A Data Warehouse And A Data Mart?
A data mart is a subject oriented database which supports the business needs of individual departments within the enterprise.It is an subset of the enterprise data warehouse.It is also known as high performance query structures.

What Is Data Validation Strategies For Data Mart Validation After Loading Process
Data validation is generally done manually in DWH in this case if source and TGT are relational you need to create SQL scripts to validate source and target data and if source isFlat file or non relational database you can use excel if data is very less or create dummy tables to validate your ETL code.

What Is Data Mining?
Data Mining is the process of analyzing data from different perspectives and summarizing it into useful information.

What Is Ods?
ODS is abbreviation of Operational Data Store. A database structure that is a repository for near real-time operational data rather than long term trend data. The ODS may further become the enterprise shared operational database, allowing operational systems that are being re-engineered to use the ODS as there operation databases.

What Is Etl?
ETL is abbreviation of extract, transform, and load. ETL is software that enables businesses to consolidate their disparate data while moving it from place to place, and it doesn’t really matter that that data is in different forms or formats. The data can come from any source.ETL is powerful enough to handle such data disparities. First, the extract function reads data from a specified source database and extracts a desired subset of data. Next, the transform function works with the acquired data – using rules orlookup tables, or creating combinations with other data – to convert it to the desired state. Finally, the load function is used to write the resulting data to a target database.

Is Oltp Database Is Design Optimal For Data Warehouse?
No. OLTP database tables are normalized and it will add additional time to queries to return results. Additionally OLTP database is smaller and it does not contain longer period (many years) data, which needs to be analyzed. A OLTP system is basically ER model and not Dimensional Model. If a complex query is executed on a OLTP system, it may cause a heavy overhead on the OLTP server that will affect the normal business processes.

If De-normalized Is Improves Data Warehouse Processes, Why Fact Table Is In Normal Form?
Foreign keys of facts tables are primary keys of Dimension tables. It is clear that fact table contains columns which are primary key to other table that itself make normal form table.

What Are Lookup Tables?
A lookup table is the table placed on the target table based upon the primary key of the target, it just updates the table by allowing only modified (new or updated) records based on thelookup condition.

What Are Aggregate Tables?
Aggregate table contains the summary of existing warehouse data which is grouped to certain levels of dimensions. It is always easy to retrieve data from aggregated tables than visiting original table which has million records. Aggregate tables reduces the load in the database server and increases the performance of the query and can retrieve the result quickly.

What Is Real Time Data-warehousing?
Data warehousing captures business activity data. Real-time data warehousing captures business activity data as it occurs. As soon as the business activity is complete and there is data about it, the completed activity data flows into the data warehouse and becomes available instantly.

What Are Conformed Dimensions?
Conformed dimensions mean the exact same thing with every possible fact table to which they are joined. They are common to the cubes.

How Do You Load The Time Dimension?
Time dimensions are usually loaded by a program that loops through all possible dates that may appear in the data. 100 years may be represented in a time dimension, with one row per day.

What Is A Level Of Granularity Of A Fact Table?
Level of granularity means level of detail that you put into the fact table in a data warehouse. Level of granularity would mean what detail are you willing to put for each transactional fact.

What Are Non-additive Facts?
Non-additive facts are facts that cannot be summed up for any of the dimensions present in the fact table. However they are not considered as useless. If there is changes in dimensions the same facts can be useful.

What Is Factless Facts Table?
A fact table which does not contain numeric fact columns it is called factless facts table.

Explain About Olap ?
OLAP is known as online analytical processing which provides answers to queries which are multi dimensional in nature. It composes relational reporting and data mining for providing solutions to business intelligence. This term OLAP is created from the term OLTP.

Explain About The Functionality Of Olap?
Hyper cube or multidimensional cube forms the core of OLAP system. This consists of measures which are arranged according to dimensions. Hyper cube Meta data is created by star or snow flake schema of tables in RDBMS. Dimensions are extracted from dimension table and measures from the fact table.

Explain About Molap?
Classic form of OLAP is known as MOLAP and it is often called as OLAP. Simple database structures such as time period, product, location, etc are used. Functioning of each and every dimension or data structure is defined by one or more hierarchies.

Explain About Rolap?
Functioning of ROLAP occurs simultaneously with relational databases. Data and tables are stored as relational tables. To hold new information or data new tables are created. Functioning of ROLAP depends upon specialized schema design.

Explain About Aggregations?
OLAP can process complex queries and give the output in less than 0.1 seconds, for it to achieve such a performance OLAP uses aggregations. Aggregations are built by aggregating and changing the data along the dimensions. Possible combination of aggregations can be determined by the combination possibilities of dimension granularities.

Explain About The View Selection Problem?
Often calculating all the data is not possible by aggregations for this reason some of the complex data problems are solved. In order to determine which data should be solved and calculated, developers use View selection application. This solution is often used to reduce calculation problem.

Explain About The Role Of Bitmap Indexes To Solve Aggregation Problems?
Bitmaps are very useful in start schema to join large databases to small databases. Answer queries and bit arrays are used to perform logical operations on the databases. Bit map indexes are very efficient in handling Gender differentiation; also repetitive tasks are performed with much larger efficiency.

Explain About Encoding Technique Used In Bitmaps Indexes?
Bitmaps commonly use one bitmap for every single distinct value. Number of bitmaps used can be reduced by opting for a different type of encoding. Space can be optimized but when a query is generated bitmaps have to be accessed.

Explain About Binning?
Binning process is very useful to save space. Performance may vary depending upon the query generated sometimes solution to a query can come within few seconds and sometimes it may take longer time. Binning process holds multiple values in the same bin.


Explain About Hybrid Olap?
When a database developer uses Hybrid OLAP it divides the data between relational and specialized storage. In some particular modifications a HOLAP database may store huge amounts of data in its relational tables. Specialized data storage is used to store data which is less detailed and more aggregate.

Explain About Shared Features Of Olap?
Shared implements most of the security features into OLAP. If multiple accesses are required admin can make necessary changes. The default security level for all OLAP products is read only. For multiple updates it is predominant to make necessary security changes.

Explain About Analysis?
Analysis defines about the logical and statistical analysis required for an efficient output. This involves writing of code and performing calculations, but most part of these languages does not require complex programming language knowledge. There are many specific features which are included such as time analysis, currency translation, etc.

Explain About Multidimensional Features Present In Olap?
Multidimensional support is very essential if we are to include multiple hierarchies in our data analysis. Multidimensional feature allows a user to analyze business and organization. OLAP efficiently handles support for multidimensional features.

Explain About The Database Marketing Application Of Olap?
Database marketing tool or application helps a user or marketing professional in determining the right tool or strategy for his valuable add campaign. This tool collects data from all sources and gives relevant information the specialist with their add campaign. It gives a complete picture to the developer.

What Are The Different Industries Which Use This Marketing Tool?
Many different companies can use this tool for developing their business strategy but it is often three major industries which use this tool more. Those three industries are Consumer goods industries, Retail industries, and financial services industry. These industry`s have huge amount of data in their disposal which makes then to use these tools to determine their exact customer.

Compare Data Warehouse Database And Oltp Database
The data warehouse and the OLTP data base are bothrelational databases. However, the objectives of both these databases are different.
The OLTP database records transactions in real time and aims to automate clerical data entry processes of a business entity. Addition, modification and deletion of data in the OLTP database is essential and the semantics of the applicationused in the front end impact on the organization of the data in the database.
The data warehouse on the other hand does not cater to real time operational requirements of the enterprise. It is more a storehouse of current and historical data and may alsocontain data extracted from external data sources.

What Is The Difference Between Etl Tool And Olap Tool? What Are Various Etl In The Market? What Are Various Olap Tools? What Is The Future For Both For Next Five Years?
ETL is a extraction,transformation,loading tool i.e u can extract , u can transform using different transformations available in tool and aggreagte the data. The output of thisETL tool is used as input to OLAP tool.
OLAP is online analytical process, where u can get online reports after doing some joines,creating some cubes

ETL tools in market
1 INFORMATICA-- univeral tool ,good market
2 ABINITO -- fastest loading tool,very good market
3 DATASTAGE-- difficult work, no good market
4 BODI-- good market
5 ORACLE WAREHOUSE BUILDER-- good market.

How To Enable Security In Cognos Connection In Cognos Report Net
You can imlement security via your Windows NT system accounts, LDAP accounts for Cognos connection. To do thisconfigure the desired Security section in the Cognos Configuration.

Compare Data Warehouse Database And Oltp Database.
Data Warehouse is used for business measures cannot be used to cater real time business needs of the organizationand is optimized for lot of data, unpredictable queries. On the other hand, OLTP database is for real time business operations that are used for a common set of transactions. Data warehouse does not require any validation of data. OLTP database requires validation of data.

What Does Level Of Granularity Of A Fact Table Signify?
In simple terms, level of granularity defines the extent of detail. As an example, let us look at geographical level of granularity. We may analyze data at the levels of COUNTRY, REGION, TERRITORY, CITY and STREET. In this case, we say the highest level of granularity is STREET.

Differences Between Star And Snowflake Schemas ?
The star schema is created when all the dimension tables directly link to the fact table. Since the graphical representation resembles a star it is called a star schema. It must be noted that the foreign keys in the fact table link to the primary key of the dimension table. This sample provides the star schema for a sales_ fact for the year 1998. The dimensions created are Store, Customer, Product_class and time_by_day. The Product table links to the product_class table through the primary key and indirectly to the fact table. The fact table contains foreign keys that link to the dimension tables.


Steps In Building The Data Model
While ER model lists and defines the constructs required to build a data model, there is no standard process for doing so. Some methodologies, such as IDEFIX, specify a bottom-up.

Why Is Data Modeling Important?
Data modeling is probably the most labor intensive and time consuming part of the development process. Why bother especially if you are pressed for time? A common.

What Type Of Indexing Mechanism Do We Need To Use For A Typical Datawarehouse?
On the fact table it is best to use bitmap indexes. Dimension tables can use bitmap and/or the other types of clustered/non-clustered, unique/non-unique indexes.
To my knowledge, SQLServer does not support bitmap indexes. Only Oracle supports bitmaps.

What Are Semi-additive And Factless Facts And In Which Scenario Will You Use Such Kinds Of Fact Tables?
Semi-Additive: Semi-additive facts are facts that can be summed up for some of the dimensions in the fact table, but not the others. For example:
Current_Balance and Profit_Margin are the facts. Current_Balance is a semi-additive fact, as it makes sense to add them up for all accounts (what's the total current balance for all accounts in the bank?), but it does not make sense to add them up through time (adding up all current balances for a given account for each day of the month does not give us any useful information A factless fact table captures the many-to-many relationships between dimensions, but contains no numeric or textual facts. They are often used to record events or coverage information.
Common examples of factless fact tables include:

- Identifying product promotion events (to determine promoted products that didn?t sell)
- Tracking student attendance or registration events
- Tracking insurance-related accident events
- Identifying building, facility, and equipment schedules for a hospital or university.

Is It Correct/feasible Develop A Data Mart Using An Ods?
Yes it is correct to develop a Data Mart using an ODS.becoz ODS which is used to?store transaction data and few Days (less historical data) this is what datamart is required so it is coct to develop datamart using ODS .

Explain Degenerated Dimension.
A Degenerate dimension?is a?Dimension which has only a single attribute.
This dimension is typically represented as a single field in a fact table.
The data items thar are not facts and data items that do not fit into the existing dimensions are termed as Degenerate Dimensions.
Degenerate Dimensions are the fastest way to group similar transactions.
Degenerate Dimensions are used when fact tables represent transactional data.
They can be used as primary key for the fact table but they cannot act as foreign keys.

What Are The Different Methods Of Loading Dimension Tables?
Conventional Load:
Before loading the data, all the Table constraints will be checked against the data.
Direct load:(Faster Loading)
All the Constraints will be disabled. Data will be loaded directly.Later the data will be checked against the table constraints and the bad data won't be indexed.

What Are Slowly Changing Dimensions?
Dimensions that change over time are called Slowly Changing Dimensions. For instance, a product price changes over time; People change their names for some reason; Country and State names may change over time. These are a few examples of Slowly Changing Dimensions since some changes are happening to them over a period of time.
If the data in the Dimension table happen to change very rarely,then it is called as slowly changing dimension.
ex: changing the name and address of a person,which happens rerely.

What Are The Various Reporting Tools In The Market?
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

What Are The Data Types Present In Bo?n What Happens If We Implement View In The Designer N Report
my knowlegde, these are?called as object types in the Business Objects.And alias is different from view in the universe. View is at database level, but alias?is a different name given for the same table to resolve the loops in universe.

What Is Meant By Metadata In Context Of A Datawarehouse And How It Is Important?
Metadata or Meta Data Metadata is data about data. Examples of metadata include data element descriptions, data type descriptions, attribute/property descriptions, range/domain descriptions, and process/method descriptions. The repository environment encompasses all corporate metadata resources: database catalogs, data dictionaries, and navigation services. Metadata includes things like the name, length, valid values, and description of a data element. Metadata is stored in a data dictionary and repository. It insulates the data warehouse from changes in the schema of operational systems. Metadata Synchronization The process of consolidating, relating and synchronizing data elements with the same or similar meaning from different systems. Metadata synchronization joins these differing elements together in the data warehouse to allow for easier access.

What Are Modeling Tools Available In The Market
These tools are used for Data/dimension modeling
Oracle Designer
ERWin (Entity Relationship for windows)
Informatica (Cubes/Dimensions)
Embarcadero
Power Designer Sybase.

What Is The Main Differnce Between Schema In Rdbms And Schemas In Datawarehouse?
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

What Is A General Purpose Scheduling Tool?
The basic purpose of the scheduling tool in a DW Application is to stream line the flow of data from Source To Target at specific time or based on some condition.

What Is The Need Of Surrogate Key;why Primary Key Not Used As Surrogate Key?
Surrogate Key is an artificial identifier for an entity. In surrogate key values are generated by the system sequentially(Like Identity property in SQL Server and Sequence in Oracle). They do not describe anything. Primary Key is a natural identifier for an entity. In Primary keys all the values are entered manually by the user which are uniquely identified. There will be no repetition of data.

Need For Surrogate Key Not Primary Key
If a column is made a primary key and later there needs a change in the data type or the length for that column then all the foreign keys that are dependent on that primary key should be changed making the database Unstable . Surrogate Keys make the database more stable because it insulates the Primary and foreign key relationships from changes in the data types and length.

What Is Snow Flake Schema?
Snowflake schemas normalize dimensions to eliminate redundancy. That is, the dimension data has been grouped into multiple tables instead of one large table. For example, a product dimension table in a star schema might be normalized into a products table, a product_category table, and a product_manufacturer table in a snowflake schema. While this saves space, it increases the number of dimension tables and requires more foreign key joins. The result is more complex queries and reduced query performance.

What Is The Difference Between Oltp And Olap?
OLTP is nothing but OnLine Transaction Processing ,which contains a normalised tables and online data,which have frequent insert/updates/delete.

How Are The Dimension Tables Designed?
Find where data for this dimension are located.
Figure out how to extract this data.
Determine how to maintain changes to this dimension.
Change fact table and DW population routines.

What Are The Advantages Data Mining Over Traditional Approaches?
Data Mining is used for?the estimation of future. For example,?if we take a company/business organization, by using the concept of Data Mining, we can predict the future of business interms of Revenue (or) Employees (or) Cutomers (or) Orders etc.
Traditional approches use?simple algorithms?for estimating the future. But, it does not give accurate results when compared to Data Mining.

Which Automation Tool Is Used In Data Warehouse Testing?
No Tool testing in done in DWH, only manual testing is done.

Give Examples Of Degenerated Dimensions
Degenerated Dimension is a dimension key without corresponding dimension. Example:
In the PointOfSale Transaction Fact table, we have:
Date Key (FK), Product Key (FK), Store Key (FK), Promotion Key?(FP),?and POS Transaction Number?? Date Dimension corresponds to Date Key, Production Dimension corresponds to Production Key. In a traditional parent-child database, POS Transactional Number would be?the key to the transaction header record that contains all the info valid for the transaction as a whole, such as the transaction date and store?identifier.?But in this?dimensional model, we have already extracted this info into other dimension. Therefore, POS Transaction Number?looks like a dimension key in the fact table but does not have the corresponding dimension table.
Therefore, POS Transaction Number is a degenerated dimension.

What Is The Datatype Of The Surrogate Key?
Normally Surrogate keys are sequencers which keep on increasing with new records being injected into the table. The standard datatype is integer.

What Is Skew And Skew Measurement?
skew is the mesaureof data flow to each partation .
suppose i/p is comming from 4 files and size is 1 gb
1 gb= ( 100mb+200mb+300mb+5oomb)
1000mb/4= 250 mb
(100- 250 )/500= --> -150/500 == cal ur self it wil come in -ve value.
calclu for 200,500,300.
+ve value of skew is allways desriable.
skew is a indericet measure of graph.

What Is The Difference Between A Scan Component And A Rollup Component?
Rollup is for group by and Scan is for successive total. Basically, when we need to produce summary then we use scan. Rollup is used to aggregate data.

What Is M_dump?
m_dump command prints the data in a formatted way.

What Is Brodcasting And Replicate?
Broadcast - Takes data from multiple inputs, combines it and sends it to all the output ports.
Eg - You have 2 incoming flows (This can be data parallelism or component parallelism) on Broadcast component, one with 10 records & other with 20 records. Then on all the outgoing flows (it can be any number of flows) will have 10 + 20 = 30 records.
Replicate - It replicates the data for a particular partition and send it out to multiple out ports of the component, but maintains the partition integrity.
Eg - Your incoming flow to replicate has a data parallelism level of 2. with one partition having 10 recs & other one having 20 recs. Now suppose you have 3 output flos from replicate. Then each flow will have 2 data partitions with 10 & 20 records respectively.

What Is Local And Formal Parameter?
Two are graph level parameters but in local you need to initialize the value at the time of declaration where as globle no need to initialize the data it will promt at the time of running the graph for that parameter.

What Is The Difference Between Dml Expression And Xfr Expression?
The main difference b/w dml & xfr is that
DML represent format of the metadata.
XFR represent the tranform functions.which will contain business rules

I Am Unable To Connect Sever Database(oracle) From Gde(db Config File) Local System.i Set All These?
ChalapathiFirst we can check the properties in internet options and then you can check in cmd format telenet abinitio ip_add.


Have You Used Rollup Component? Describe How?
If the user wants to group the records on particular field values then rollup is best way to do that. Rollup is a multi-stage transform function and it contains the following mandatory functions.
1. initialise
2. rollup
3. finalise
   Also need to declare one temporary variable if you want to get counts of a particular group.

For each of the group, first it does call the initialise function once, followed by rollup function calls for each of the records in the group and finally calls the finalise function once at the end of last rollup call.

What Are Primary Keys And Foreign Keys?
In RDBMS the relationship between the two tables is represented as Primary key and foreign key relationship. Wheras the primary key table is the parent table and foreignkey table is the child table.The criteria for both the tables is there should be a matching column.

What Is An Outer Join?
An outer join is used when one wants to select all the records from a port - whether it has satisfied the join criteria or not.

What Are Cartesian Joins?
A Cartesian join will get you a Cartesian product. A Cartesian join is when you join every row of one table to every row of another table. You can also get one by joining every row of a table to every row of itself.

What Is The Purpose Of Having Stored Procedures In A Database?
Main Purpose of Stored Procedure for reduse the network trafic and all sql statement executing in cursor so speed too high.

Why Might You Create A Stored Procedure With The With Recompile Option?
Recompile is useful when the tables referenced by the stored proc undergoes a lot of modification/ deletion/ addition of data. Due to the heavy modification activity the execute plan becomes outdated and hence the stored proc performance goes down. If we create the stored proc with recompile option, the sql server wont cache a plan for this stored proc and it will be recompiled every time it is run.

What Is A Cursor? Within A Cursor, How Would You Update Fields On The Row Just Fetched?
The oracle engine uses work areas for internal processing in order to the execute sql statement is called cursor.There are two types of cursors like Implecit cursor and Explicit cursor.Implicit cursor is using for internal processing and Explicit cursor is using for user open for data required.

How Can You Force The Optimizer To Use A Particular Index?
Use hints /*+ */, these acts as directives to the optimizer.

Describe The Process Steps You Would Perform When Defragmenting A Data Table. This Table Contains Mission Critical Data?
There are several ways to do this:
1) We can move the table in the same or other tablespace and rebuild all the indexes on the table.
   alter table move this activity reclaims the defragmented space in the table
   analyze table table_name compute statistics to capture the updated statistics.
   2)Reorg could be done by taking a dump of the table, truncate the table and import the dump back into the table.

Explain The Difference Between The Truncate And Delete Commands?
Truncate :
It is a DDL command, used to delete tables or clusters. Since it is a DDL command hence it is auto commit and Rollback can't be performed. It is faster than delete.

Delete:
It is DML command, generally used to delete a record, clusters or tables. Rollback command can be performed , in order to retrieve the earlier deleted things. To make deleted things permanently, "commit" command should be used.

How Would You Find Out Whether A Sql Query Is Using The Indices You Expect?
Explain plan can be reviewed to check the execution plan of the query. This would guide if the expected indexes are used or not.

Describe The Elements You Would Review To Ensure Multiple Scheduled Batch Jobs Do Not Collide With Each Other?
Because every job depend upon another job for example if you first job result is successfull then another job will execute otherwise your job doesn't work.

What Is The Difference Between Rollup And Scan?
By using rollup we cant generate cumulative summary records for that we will be using scan.

Describe The Grant/revoke Ddl Facility And How It Is Implemented?
Basically,This is a part of D.B.A responsibilities GRANT means permissions for example GRANT CREATE TABLE ,CREATE VIEW AND MANY MORE .
REVOKE means cancel the grant (permissions).So,Grant or Revoke both commands depend upon D.B.A.

When Using Multiple Dml Statements To Perform A Single Unit Of Work, Is It Preferable To Use Implicit Or Explicit Transactions, And Why?
Because implicit is using for internal processing and explicit is using for user open data requied.

Explain In Detail Abt Measure Objects? And What Is The Use Of It? How To Create It?
Measure objects are the objects which have facts i.e all $ amounts
a dimension object cannot be calculated with another dim object.
in order to have a seperate identity for $ amounts we define as measure objects.
just create an object for ex:revenue then right clicck on the object or double click on the object n then change the property of that object to measure its that simple.

How To Create Generic Time Class, Which Includes Objects Year,month And Qtr? Database In Use Is Oracle?
If your database consist all dates something like 01/02/2000 or 01-Feb-2000, you will need to break the date field into year, qtr,month & if required date.
to do this, create a class named TIME, under that create new object, in it's select box use oracle's date functions to get required information.
For E.g. : to_char(sales_date, 'YYYY') for getting only year from the date.
similarly, for quarter you can use to_char(sales_date, 'Q')
& for month to_char(sales_date, 'MM') for month number, instead of 'MM' if you use 'MON' it will return you abrevations like Jan for January & so on. for full name of month use 'MONTH'.


What Are The Security Level Used In Bo?
We have securities in business objects
Like
1.Windows authentication
2.RDBMS securities
3.supervisor level securities, ie User name/ password.

What Is The Difference In Creating Filters In Designer And Business Objects?
Creating a filter in designer is different from creatind a filter in business object
if u create a filter in designer it can acessible to all the reports ur r using i'e,it can used for further applications where as creatin a filter vin business object is dynamic(run time) it will applicable to only tht particular report.



What Are The Functional & Architectural Differences Between Business Objects And Web Intelligence Reports?
Functional differences
• Business objects, for building or accessing reports, needs to be installed on every pc. On the other hand, Web intelligence reports needs a browser and a URL of the server from where Business objects will be accessed.
• BOMain.key needs to be copied on every pc using BO client. This is not required for Web Intelligence Reports.
• Business objects expect you to use the same pc where they are installed. Web Intelligence reports can be accessed from anywhere, provided internet is available.

Architectural differences
For BO client, for sending info to BO Server BOMain.key, uses the key of the local drive. Once the information is sent, it is validated and checked into the repository upon which the user can access the BO services. On the other hand, Web Intelligence the web servers BOMain.key is used to check privilege of the user and then sending information to the BO Server BOMain.key.

What Is Batch Processing In Business Objects?
Batch processing can be used to schedule reports. Objects can be also be used for batch processing. Batch processing can be used to also select the objects to be processed. The batch can be run as a transaction in which if one process fails, the entire batch is rolled back or it can be run as a series of jobs.

What Is Data Cardinality?
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

What Is Chained Data Replication?

In Chain Data Replication, the non-official data set distributed among many disks provides for load balancing among the servers within the data warehouse.
Blocks of data are spread across clusters and each cluster can contain a complete set of replicated data. Every data block in every cluster is a unique permutation of the data in other clusters.
When a disk fails then all the calls made to the data in that disk are redirected to the other disks when the data has been replicated.
At times replicas and disks are added online without having to move around the data in the existing copy or affect the arm movement of the disk.
In load balancing, Chain Data Replication has multiple servers within the data warehouse share data request processing since data already have replicas in each server disk.

Explain In Brief Various Fundamental Stages Of Data Warehousing.
The following are the stages of data warehousing:
Offline Operational Database: It is the stage where copying the data off an operational system to another server where the report processing load against the copied data takes place and OS performance does not impact.
Offline Data Warehouse: In this stage, data warehouses are updated from data in the OS and the data of data warehouse is stored in a data structure that is designed for facilitating reports.
Real time Data Warehouse: The data warehouses are updated often when an OS performs a transaction.
Integrated Data Warehouse: The data warehouses are updated by OS, at the time of performing a transaction. Then transactions are generated which are passed back into the operational systems.

What Is The Difference Between Enterprise Data Warehouse And Data Warehouse?
Big Organizations have a lot of diversified sources of data.There might be a dataware house exclusively for transport and others for data related to the project the company runs.In such case the complete enterprise's(company's) date ware house is a big combination of all and is known the Enterprise data Warehouse(EDW)


Give Me Any Example Of Semi And Non Additive Measures?
Semi-Additive: Semi-additive facts are facts that can be summed up for some of the dimensions in the fact table, but not the others. Non-Additive: Non-additive facts are facts that cannot be summed up for any of the dimensions present in the fact table. Current Balance and Profit Margin are the facts.Current Balance is a semi-additive fact, as it makes sense to add them up for all accounts (what's the total current balance for all accounts in the bank?), but it does not make sense to add them up through time (adding up all current balances for a given account for each day of the month does not give us any useful information). Profit Margin is a non-additive fact, for it does not make sense to add them up for the account level or the day level.


What Are The Options In The Target Session Of Update Strategy Transformations?
Insert
Delete
Update
Update as update
Update as insert
Update else insert
Truncate table

What Are The Various Types Of Transformation?

Answer :

Various types of transformation are: Aggregator Transformation, Expression Transformation, Filter
Transformation, Joiner Transformation, Lookup Transformation, Normalizer Transformation, Rank Transformation,
Router Transformation, Sequence Generator Transformation, Stored Procedure Transformation, Sorter
Transformation, Update Strategy Transformation, XML Source Qualifier Transformation, Advanced External
Procedure Transformation, External Transformation.

What Is The Difference Between Active Transformation And Passive Transformation?
An active transformation can change the number of rows that pass through it, but a passive transformation can not change the number of rows that pass through it.

What Is The Difference Between Static Cache And Dynamic Cache?
In case of dynamic cache, when we are inserting a new row it checks the lookup cache to see if it exists, if not inserts it into the target as well as the cache but in case of static cache the new row is written only in the target and not the lookup cache. The lookup cache remains static and does not change during the session but incase of dynamic cache the server inserts, updates in the cache during session.

How Do We Join Two Tables Without Joiner Or Sql Override?
We can join the tables using lookup tansformation and making a cartesian product.

What Are Pre-session And Post-session Options?
These are shell commands that Informatica server performs before running the session. We should have permission and privileges to run the options in Informatica.

Differences Between Normalizer And Normalizer Transformation.
Normalizer: It is a transormation mainly using for cobol sources,
it's change the rows into coloums and columns into rows
Normalization:To remove the retundancy and inconsitecy.

What Is The Use Of Incremental Aggregation? Explain Me In Brief With An Example.
Its a session option. when the informatica server performs incremental aggr. it passes new source data through the mapping and uses historical chache data to perform new aggregation caluculations incrementaly. for performance we will use it.



What Is Business Intelligence?
Business Intelligence is a process for increasing the competitive advantage of a business by intelligent use of available data in decision making.
The five key stages of Business Intelligence:
► Data Sourcing
► Data Analysis
► Situation Awareness
► Risk Assessment
► Decision Support.

Question 332. What Is A Universe In Business Intelligence?
"universe" is a "Business object" terminology. Business objects also happens to be the name of the company. The universe is the interfacing layer between the client and the datawarehouse . The universe defines the relationship among the various tables in the datawarehouse.
Or Universe is a semantic layer between the database and the user interface (reports).

What Is Olap In Business Intelligence?
Online Analytical Processing, a category of software tools that provides analysis of data stored in a database. OLAP tools enable users to analyze different dimensions of multidimensional data. For example, it provides time series and trend analysis views. The chief component of OLAP is the OLAP server, which sits between a client and a database management systems (DBMS). The OLAP server understands how data is organized in the database and has special functions analyzing the data.
A good OLAP interface has writes an efficient sql and reads an accurate data from db.To design and architect having good knowledge on DB understanding the report requirements.

What Are The Various Modules In Business Objects Product?
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

What Is Olap, Molap, Rolap, Dolap, Holap? Explain With Examples?
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

Why An Infocube Has Maximum Of 16 Dimensions?
It depends upon the Database limits provided to define the Foreign key constraint, e.g. in Sql Server 2005, the recommended max limit for foreign keys is 253, but you can define more.

Name Some Of The Standard Business Intelligence Tools In The Market?
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

What Are Dashboards?
A management reporting tool to gauge how well the organization company is performing. It normally uses "traffic-lights" or "smiley faces" to determine the status.


What Is Hierarchy Relationship In A Dimension.
whether it is:
1. 1:1
2. 1:m
3. m:m
   1:M

From Where You Get The Logical Query Of Your Request?
The logical SQL generated by the server can be viewed in BI Answers. If I have not understood the question, Please raise your voice.


What Are The Advantages And Disadvantages Of Star And Snowflake Schema?
Star Schema Advantages: Reduces the number of joins between the tables and hence faster performance.
Star Schema Disadvantages:Requires Most amount of storage space.
Snowflake Schema Advantages: Minimum storage space and minimum data redundancy.
Snowflake Schema Disadvantages:Requires more joins to get information from look up tables hence slow performance.


What Are Adhoc Reports And Static Reports?
Adhoc reports run in real time based on the input parameters provided by the user at the run time.In Microstrategy, adhoc reports are created using Prompts.
In static reports, users won't be provide any input parameters.These reports are usaully schedule to run overnight and ready to view immediatley in the mornings using cache.



What Is The Importance Of Surrogate Key In Data Warehousing?
Surrogate Key is a Primary Key for a Dimension table. Most importance of using it is it is independent of underlying database. i.e Surrogate Key is not affected by the changes going on with a database.


What Is A Query?
A query is one or more statements that request data from a database. If the data is available, then the requested data returns in the form of a table which contains rows and columns. Queries are sent to the databases in a language called SQL. However, when using the Report Panel, SQL knowledge is not required.

What Are The Features Of A Physical Data Model?

Features of a physical data model include:
Specification all tables and columns.
Foreign keys are used to identify relationships between tables.
Denormalization may occur based on user requirements.
Physical considerations may cause the physical data model to be quite different from the logical data model.
Physical data model will be different for different RDBMS. For example, data type for a column may be different between MySQL and SQL Server.


What Are The Steps To Design A Physical Model?
The steps for physical data model design are as follows:
Convert entities into tables.
Convert relationships into foreign keys.
Convert attributes into columns.
Modify the physical data model based on physical constraints / requirements.
IDMS (Integrated Database Management System) Interview Questions


What Are The Features Of Conceptual Data Model?
Features of conceptual data model include:
Includes the important entities and the relationships among them.
No attribute is specified.
No primary key is specified.
PL/SQL Interview Questions


What Are The Difference Between Logical Data Model And Conceptual Data Model?
In a logical data model, primary keys are present, whereas in a conceptual data model, no primary key is present.
In a logical data model, all attributes are specified within an entity. No attributes are specified in a conceptual data model.
Relationships between entities are specified using primary keys and foreign keys in a logical data model. In a conceptual data model, the relationships are simply stated, not specified, so we simply know that two entities are related, but we do not specify what attributes are used for this relationship.

What Are The Steps To Design Logical Data Model?
The steps for designing the logical data model are as follows:

Specify primary keys for all entities.
Find the relationships between different entities.
Find all attributes for each entity.
Resolve many-to-many relationships.
Normalization.


What Is Etl?
ETL stands for extraction transformation and loading
ETL provide developers with an interface for designing source-to-target mappings, transformation and job control parameter
* Extraction
  Take data from an external source and move it to the warehouse pre-processor database
* Transformation
  Transform data task allows point-to-point generating, modifying and transforming data
* Loading
  Load data task adds records to a database table in a warehouse.

What Is A Three Tier Data Warehouse?
A data warehouse can be thought of as a three-tier system in which a middle system provides usable data in a secure way to end users. On either side of this middle system are the end users and the back-end data stores.

What Is Etl Process ?how Many Steps Etl Contains Explain With Example?
ETL is extraction , transforming , loading process , you will extract data from the source and apply the business role on it then you will load it in the target
The steps are :
1-define the source (create the odbc and the connection to the source DB)
2-define the target (create the odbc and the connection to the target DB)
3-create the mapping ( you will apply the business role here by adding transformations , and define how the data flow will go from the source to the target )
4-create the session (its a set of instruction that run the mapping )
5-create the work flow (instruction that run the session)

What Is Full Load & Incremental Or Refresh Load?
Full Load: completely erasing the contents of one or more tables and reloading with fresh data.
Incremental Load: applying ongoing changes to one or more tables based on a predefined schedule.

What Is A Staging Area? Do We Need It? What Is The Purpose Of A Staging Area?
Data staging is actually a collection of processes used to prepare source system data for loading a data warehouse. Staging includes the following steps:
Source data extraction, Data transformation (restructuring),
Data transformation (data cleansing, value transformations),
Surrogate key assignments

Compare Etl & Manual Development?
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


When Do We Analyze The Tables? How Do We Do It?
The ANALYZE statement allows you to validate and compute statistics for an index, table, or cluster. These statistics are used by the cost-based optimizer when it calculates the most efficient plan for retrieval. In addition to its role in statement optimization, ANALYZE also helps in validating object structures and in managing space in your system. You can choose the following operations: COMPUTER, ESTIMATE, and DELETE. Early version of Oracle7 produced unpredictable results when the ESTIMATE operation was used. It is best to compute your statistics.

How Do You Calculate Fact Table Granularity?
Granularity, is the level of detail in which the fact table is describing, for example if we are making time analysis so the granularity maybe day based - month based or year based


Lets Suppose We Have Some 10,000 Odd Records In Source System And When Load Them Into Target.how Do We Ensure That All 10,000 Records That Are Loaded To Target Doesn't Contain Any Garbage Values?
we can do ltrim, rtrim in the expression or can have check for null and then insert the data.


What Is Rdbms?
Relational Data Base Management Systems (RDBMS) are database management systems that maintain data records and indices in tables. Relationships may be created and maintained across and among the data and tables. In a relational database, relationships between data items are expressed by means of tables. Interdependencies among these tables are expressed by data values rather than by pointers. This allows a high degree of data independence. An RDBMS has the capability to recombine the data items from different files, providing powerful tools for data usage.

What Is Normalization?
Database normalization is a data design and organization process applied to data structures based on rules that help build relational databases. In relational database design, the process of organizing data to minimize redundancy. Normalization usually involves dividing a database into two or more tables and defining relationships between the tables. The objective is to isolate data so that additions, deletions, and modifications of a field can be made in just one table and then propagated through the rest of the database via the defined relationships.

What Are Different Normalization Forms?
1NF: Eliminate Repeating Groups Make a separate table for each set of related attributes, and give each table a primary key. Each field contains at most one value from its attribute domain.

2NF: Eliminate Redundant Data If an attribute depends on only part of a multi-valued key, remove it to a separate table.

3NF: Eliminate Columns Not Dependent On Key If attributes do not contribute to a description of the key, remove them to a separate table. All attributes must be directly dependent on the primary key.

BCNF: Boyce-Codd Normal Form If there are non-trivial dependencies between candidate key attributes, separate them out into distinct tables.

4NF: Isolate Independent Multiple Relationships No table may contain two or more 1:n or n:m relationships that are not directly related.

5NF: Isolate Semantically Related Multiple Relationships There may be practical constrains on information that justify separating logically related many-to-many relationships.

ONF: Optimal Normal Form A model limited to only simple (elemental) facts, as expressed in Object Role Model notation.

DKNF: Domain-Key Normal Form A model free from all modification anomalies. Remember, these normalization guidelines are cumulative. For a database to be in 3NF, it must first fulfill all the criteria of a 2NF and 1NF database.

What Is Stored Procedure?
A stored procedure is a named group of SQL statements that have been previously created and stored in the server database. Stored procedures accept input parameters so that a single procedure can be used over the network by several clients using different input data. And when the procedure is modified, all clients automatically get the new version. Stored procedures reduce network traffic and improve performance. Stored procedures can be used to help ensure the integrity of the database.
e.g. sp_helpdb, sp_renamedb, sp_depends etc.

What Is Trigger?
A trigger is a SQL procedure that initiates an action when an event (INSERT, DELETE or UPDATE) occurs. Triggers are stored in and managed by the DBMS. Triggers are used to maintain the referential integrity of data by changing the data in a systematic fashion. A trigger cannot be called or executed; the DBMS automatically fires the trigger as a result of a data modification to the associated table. Triggers can be viewed as similar to stored procedures in that both consist of procedural logic that is stored at the database level. Stored procedures, however, are not event-drive and are not attached to a specific table as triggers are. Stored procedures are explicitly executed by invoking a CALL to the procedure while triggers are implicitly executed. In addition, triggers can also execute stored procedures.

What Is View?
A simple view can be thought of as a subset of a table. It can be used for retrieving data, as well as updating or deleting rows. Rows updated or deleted in the view are updated or deleted in the table the view was created with. It should also be noted that as data in the original table changes, so does data in the view, as views are the way to look at part of the original table. The results of using a view are not permanently stored in the database. The data accessed through a view is actually constructed using standard T-SQL select command and can come from one to many different base tables or even other views.

Advantages Of Dbms?

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


Describe The Three Levels Of Data Abstraction?
There are three levels of abstraction:
Physical level: The lowest level of abstraction describes how data are stored.
Logical level: The next higher level of abstraction, describes what data are stored in database and what relationship among those data.
View level: The highest level of abstraction describes only part of entire database.
Oracle 11g Tutorial

Define The "integrity Rules"?

There are two Integrity rules.

Entity Integrity: States that “Primary key cannot have NULL value”.
Referential Integrity: States that “Foreign Key can be either a NULL value or should be Primary Key value of other relation.


What Is Extension And Intension?
Extension : It is the number of tuples present in a table at any instance. This is time dependent.
Intension : It is a constant value that gives the name, structure of table and the constraints laid on it.


What Is Data Independence?
Data independence means that “the application is independent of the storage structure and access strategy of data”. In other words, The ability to modify the schema definition in one level should not affect the schema definition in the next higher level.
Two types of Data Independence:
Physical Data Independence: Modification in physical level should not affect the logical level.
Logical Data Independence: Modification in logical level should affect the view level.


What Is A View? How It Is Related To Data Independence?
A view may be thought of as a virtual table, that is, a table that does not really exist in its own right but is instead derived from one or more underlying base table. In other words, there is no stored file that direct represents the view instead a definition of view is stored in data dictionary. Growth and restructuring of base tables is not reflected in views. Thus the view can insulate users from the effects of restructuring and growth in the database. Hence accounts for logical data independence.

What Is Data Model?
A collection of conceptual tools for describing data, data relationships data semantics and constraints.


What Is Object Oriented Model?
This model is based on collection of objects. An object contains values stored in instance variables with in the object. An object also contains bodies of code that operate on the object. These bodies of code are called methods. Objects that contain same types of values and the same methods are grouped together into classes.

What Is An Entity?
It is a 'thing' in the real world with an independent existence.

What Is An Entity Type?
It is a collection (set) of entities that have same attributes.

What Is An Entity Set?
It is a collection of all entities of particular entity type in the database.


What Is An Attribute?
It is a particular property, which describes the entity.

What Is A Relation Schema And A Relation?
A relation Schema denoted by R(A1, A2, …, An) is made up of the relation name R and the list of attributes Ai that it contains.
A relation is defined as a set of tuples. Let r be the relation which contains set tuples (t1, t2, t3, ..., tn). Each tuple is an ordered list of n-values t=(v1,v2, ..., vn).

What Is Degree Of A Relation?
It is the number of attribute of its relation schema.

What Is Relationship?
It is an association among two or more entities.

What Is Relationship Set?
The collection (or set) of similar relationships.

What Is Relationship Type?
Relationship type defines a set of associations or a relationship set among a given set of entity types.


What Is Ddl (data Definition Language)?
A data base schema is specifies by a set of definitions expressed by a special language called DDL.

What Is Vdl (view Definition Language)?
It specifies user views and their mappings to the conceptual schema.

What Is Sdl (storage Definition Language)?
This language is to specify the internal schema. This language may specify the mapping between two schemas.

What Is Data Storage - Definition Language?
The storage structures and access methods used by database system are specified by a set of definition in a special type of DDL called data storage-definition language.

What Is Dml (data Manipulation Language)?
This language that enable user to access or manipulate data as organized by appropriate data model.
Procedural DML or Low level: DML requires a user to specify what data are needed and how to get those data.
Non-Procedural DML or High level: DML requires a user to specify what data are needed without specifying how to get those data.


What Is Query Evaluation Engine?
It executes low-level instruction generated by compiler.

What Is Ddl Interpreter?
It interprets DDL statements and record them in tables containing metadata.

What Is Record-at-a-time?
The Low level or Procedural DML can specify and retrieve each record from a set of records. This retrieve of a record is said to be Record-at-a-time.

What Is Set-at-a-time Or Set-oriented?
The High level or Non-procedural DML can specify and retrieve many records in a single DML statement. This retrieve of a record is said to be Set-at-a-time or Set-oriented.

What Is Relational Algebra?
It is procedural query language. It consists of a set of operations that take one or two relations as input and produce a new relation.

What Is Relational Calculus?
It is an applied predicate calculus specifically tailored for relational databases proposed by E.F. Codd.
E.g. of languages based on it are DSL ALPHA, QUEL.

How Does Tuple-oriented Relational Calculus Differ From Domain-oriented Relational Calculus?
The tuple-oriented calculus uses a tuple variables i.e., variable whose only permitted values are tuples of that relation. E.g. QUEL
The domain-oriented calculus has domain variables i.e., variables that range over the underlying domains instead of over relation. E.g. ILL, DEDUCE.

What Is Functional Dependency?
A Functional dependency is denoted by X Y between two sets of attributes X and Y that are subsets of R specifies a constraint on the possible tuple that can form a relation state r of R. The constraint is for any two tuples t1 and t2 in r if t1[X] = t2[X] then they have t1[Y] = t2[Y]. This means the value of X component of a tuple uniquely determines the value of component Y.

When Is A Functional Dependency F Said To Be Minimal?
Every dependency in F has a single attribute for its right hand side.
We cannot replace any dependency X A in F with a dependency Y A where Y is a proper subset of X and still have a set of dependency that is equivalent to F.
We cannot remove any dependency from F and still have set of dependency that is equivalent to F.

What Is Multivalued Dependency?
Multivalued dependency denoted by X Y specified on relation schema R, where X and Y are both subsets of R, specifies the following constraint on any relation r of R: if two tuples t1 and t2 exist in r such that t1[X] = t2[X] then t3 and t4 should also exist in r with the following properties

t3[x] = t4[X] = t1[X] = t2[X]
t3[Y] = t1[Y] and t4[Y] = t2[Y]
t3[Z] = t2[Z] and t4[Z] = t1[Z]
where [Z = (R-(X U Y)) ]

What Is Lossless Join Property?
It guarantees that the spurious tuple generation does not occur with respect to relation schemas after decomposition.

What Is 1 Nf (normal Form)?
The domain of attribute must include only atomic (simple, indivisible) values.

What Is Fully Functional Dependency?
It is based on concept of full functional dependency. A functional dependency X Y is full functional dependency if removal of any attribute A from X means that the dependency does not hold any more.

What Is 2nf?
A relation schema R is in 2NF if it is in 1NF and every non-prime attribute A in R is fully functionally dependent on primary key.

What Is 3nf?
A relation schema R is in 3NF if it is in 2NF and for every FD X A either of the following is true

X is a Super-key of R.
A is a prime attribute of R.
In other words, if every non prime attribute is non-transitively dependent on primary key.

What Is Bcnf (boyce-codd Normal Form)?
A relation schema R is in BCNF if it is in 3NF and satisfies an additional constraint that for every FD X A, X must be a candidate key.

What Is 4nf?
A relation schema R is said to be in 4NF if for every Multivalued dependency X Y that holds over R, one of following is true
X is subset or equal to (or) XY = R.
X is a super key.

What Is 5nf?
A Relation schema R is said to be 5NF if for every join dependency {R1, R2, ..., Rn} that holds R, one the following is true
Ri = R for some i.
The join dependency is implied by the set of FD, over R in which the left side is key of R.

What Is Domain-key Normal Form?
A relation is said to be in DKNF if all constraints and dependencies that should hold on the constraint can be enforced by simply enforcing the domain constraint and key constraint on the relation.


What Are Partial, Alternate, Artificial, Compound And Natural Key?
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


What Is Indexing And What Are The Different Kinds Of Indexing?
Indexing is a technique for determining how quickly specific data can be found.
Types:
+ Binary search style indexing
+ B-Tree indexing
+ Inverted list indexing
M+ emory resident table
+ Table indexing


What Is System Catalog Or Catalog Relation? How Is Better Known As?
A RDBMS maintains a description of all the data that it contains, information about every relation and index that it contains. This information is stored in a collection of relations maintained by the system called metadata. It is also called data dictionary.

What Is Meant By Query Optimization?
The phase that identifies an efficient execution plan for evaluating a query that has the least estimated cost is referred to as query optimization.

What Is Join Dependency And Inclusion Dependency?
Join Dependency:
A Join dependency is generalization of Multivalued dependency.A JD {R1, R2, ..., Rn} is said to hold over a relation R if R1, R2, R3, ..., Rn is a lossless-join decomposition of R . There is no set of sound and complete inference rules for JD.
Inclusion Dependency:
An Inclusion Dependency is a statement of the form that some columns of a relation are contained in other columns. A foreign key constraint is an example of inclusion dependency.

What Is Durability In Dbms?
Once the DBMS informs the user that a transaction has successfully completed, its effects should persist even if the system crashes before all its changes are reflected on disk. This property is called durability.

What Do You Mean By Atomicity And Aggregation?
Atomicity:
Either all actions are carried out or none are. Users should not have to worry about the effect of incomplete transactions. DBMS ensures this by undoing the actions of incomplete transactions.
Aggregation:
A concept which is used to model a relationship between a collection of entities and relationships. It is used when we need to express a relationship among relationships.

What Is A Phantom Deadlock?
In distributed deadlock detection, the delay in propagating local information might cause the deadlock detection algorithms to identify deadlocks that do not really exist. Such situations are called phantom deadlocks and they lead to unnecessary aborts.

What Is A Checkpoint And When Does It Occur?
A Checkpoint is like a snapshot of the DBMS state. By taking checkpoints, the DBMS can reduce the amount of work to be done during restart in the event of subsequent crashes.

What Are The Different Phases Of Transaction?
Different phases are
Analysis phase
Redo Phase
Undo phase

What Do You Mean By Flat File Database?
It is a database in which there are no programs or user access languages. It has no cross-file capabilities but is user-friendly and provides user-interface management.

What Is "transparent Dbms"?
It is one, which keeps its Physical Structure hidden from user.

What Do You Mean By Correlated Subquery?
Subqueries, or nested queries, are used to bring back a set of rows to be used by the parent query. Depending on how the subquery is written, it can be executed once for the parent query or it can be executed once for each row returned by the parent query. If the subquery is executed for each row of the parent, this is called a correlated subquery.
A correlated subquery can be easily identified if it contains any references to the parent subquery columns in its WHERE clause. Columns from the subquery cannot be referenced anywhere else in the parent query. The following example demonstrates a non-correlated subquery.
E.g. Select * From CUST Where '10/03/1990' IN (Select ODATE From ORDER Where CUST.CNUM = ORDER.CNUM)

What Are The Primitive Operations Common To All Record Management Systems?
Addition, deletion and modification.

What Are The Unary Operations In Relational Algebra?
PROJECTION and SELECTION.

Are The Resulting Relations Of Product And Join Operation The Same?
No.
PRODUCT: Concatenation of every row in one relation with every row in another.
JOIN: Concatenation of rows from one relation and related rows from another.

What Is Rdbms Kernel?
Two important pieces of RDBMS architecture are the kernel, which is the software, and the data dictionary, which consists of the system-level data structures used by the kernel to manage the database
You might think of an RDBMS as an operating system (or set of subsystems), designed specifically for controlling data access; its primary functions are storing, retrieving, and securing data. An RDBMS maintains its own list of authorized users and their associated privileges; manages memory caches and paging; controls locking for concurrent resource usage; dispatches and schedules user requests; and manages space usage within its table-space structures.

Name The Sub-systems Of A Rdbms?
I/O, Security, Language Processing, Process Control, Storage Management, Logging and Recovery, Distribution Control, Transaction Control, Memory Management, Lock Management.

Which Part Of The Rdbms Takes Care Of The Data Dictionary? How
Data dictionary is a set of tables and database objects that is stored in a special area of the database and maintained exclusively by the kernel.

What Is Rowid?
The ROWID is a unique database-wide physical address for every row on every table. Once assigned (when the row is first inserted into the database), it never changes until the row is deleted or the table is dropped.
The ROWID consists of the following three components, the combination of which uniquely identifies the physical storage location of the row.
Oracle database file number, which contains the block with the rows
Oracle block address, which contains the row
The row within the block (because each block can hold many rows)
The ROWID is used internally in indexes as a quick means of retrieving rows with a particular key value. Application developers also use it in SQL statements as a quick way to access a row once they know the ROWID.


What Is Storage Manager?
It is a program module that provides the interface between the low-level data stored in database, application programs and queries submitted to the system.

What Is Buffer Manager?
It is a program module, which is responsible for fetching data from disk storage into main memory and deciding what data to be cache in memory.

What Is Transaction Manager?
It is a program module, which ensures that database, remains in a consistent state despite system failures and concurrent transaction execution proceeds without conflicting.

 What Is File Manager?
It is a program module, which manages the allocation of space on disk storage and data structure used to represent information stored on a disk.

What Is Authorization And Integrity Manager?
It is the program module, which tests for the satisfaction of integrity constraint and checks the authority of user to access data.

What Are Stand-alone Procedures?
Procedures that are not part of a package are known as stand-alone because they independently defined. A good example of a stand-alone procedure is one written in a SQL*Forms application. These types of procedures are not available for reference from other Oracle tools. Another limitation of stand-alone procedures is that they are compiled at run time, which slows execution.

What Are Cursors Give Different Types Of Cursors.
PL/SQL uses cursors for all database information accesses statements. The language supports the use two types of cursors.

What Is Meant By Proactive, Retroactive And Simultaneous Update?
Proactive Update:
The updates that are applied to database before it becomes effective in real world .

What is a fact table?
The fact table includes the measurement of the business process. Fact table includes the foreign keys for the dimension tables.
Example: If we are business phase is "paper production," "normal production of paper by one device, "or "weekly production of paper" will be treated as a measurement of the business process.

What are the different methods of loading dimension tables?
There are two different methods to load data in dimension tables:
+ Conventional (slow): All the constraints and keys are validated against the information before, it is loaded, and this method data integrity is maintained.
+ Direct (fast): All the constraints and keys are disabled before the information is loaded. Once the information is loaded, it is validated against all the constraints and keys. If the data is found invalid, it is not contained in the index, and all the future processes are skipped in this data.

Describe the foreign key columns in fact tables and dimension tables?
Foreign keys of dimension tables are the primary key of entity tables.
Foreign keys of fact tables are the primary key of dimension tables.
