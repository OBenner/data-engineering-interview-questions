[Interview questions](README.md)
# SQL


[Table of Contents](#SQL)

## Write SQL query to get the second highest salary among all Employees?
Given a Employee Table with two columns
ID, Salary 10, 2000
11, 5000
12, 3000

[Table of Contents](#SQL)

There are multiple ways to get the second highest salary among all Employees.
Option 1: Use Subquery
SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee );
In this approach, we are getting the maximum salary in a subquery and then excluding this from the rest of the resultset.
Option 2: Use Not equals
select MAX(Salary) from Employee WHERE Salary <> (select MAX(Salary) from Employee )
This is same as option 1 but we are using <> instead of NOT IN.

[Table of Contents](#SQL)

How can we retrieve alternate records from a table in Oracle?
We can use rownum and MOD function to retrieve the alternate records from a table.
To get Even number records:
SELECT * FROM (SELECT rownum, ID, Name FROM Employee) WHERE MOD(rownum,2)=0
To get Odd number records: SELECT * FROM (SELECT rownum, ID, Name FROM Employee)
WHERE MOD(rownum,2)=1

[Table of Contents](#SQL)

Write SQL Query to find Max salary and Department name from each department.
Given Employee table with three columns
ID, Salary, DeptID
10, 1000, 2
20, 5000, 3
30, 3000, 2

Department table with two columns: ID, DeptName
1, Marketing
2, IT
3, Finance

This is a trick question. There can be some department without any employee. So we have to ask interviewer if they expect the name of such Department also in result.
If yes then we have to join Department table with Employee table by using foreign key DeptID. We have to use LEFT OUTER JOIN to print all the departments.
Query would be like as follows:
SELECT d.DeptName, MAX(e.Salary) FROM Department d LEFT OUTER JOIN Employee e ON e.DeptId = d.ID GROUP BY DeptName

[Table of Contents](#SQL)

Write a SQL query to find records in Table A that are not in Table B without using NOT IN operator.
Consider two tables
Table_A

10
20
30

Table_B
15
30
45
We can use MINUS operator in this case for Oracle and EXCEPT for SQL Server.
Query will be as follows:
SELECT * FROM Table_A MINUS SELECT * FROM Table_B

[Table of Contents](#SQL)

What is the result of following query?
SELECT CASE WHEN null = null THEN ‘True’ ELSE ‘False’ END AS Result;
Answer: In SQL null can not be compared with itself. There fore null = null is not true. We can compare null with a non-null value to check whether a value is not null.
Therefore the result of above query is False.
The correct way to check for null is to use IS NULL clause.
Following query will give result True. SELECT CASE WHEN null IS NULL THEN ‘True’ ELSE ‘False’ END AS Result;

[Table of Contents](#SQL)

Write SQL Query to find employees that have same name and email.
Employee table:
ID	NAME	EMAIL
10	John	jbaldwin
20	George	gadams
30	John	jsmith

This is a simple question with one trick. The trick here is to use Group by on two columns Name and Email.
Query would be as follows: SELECT name, email, COUNT(*) FROM Employee GROUP BY name, email HAVING COUNT(*) > 1

[Table of Contents](#SQL)

Write SQL Query to find Max salary from each department.
Given a Employee table with three columns
ID, Salary, DeptID 10, 1000, 2
20, 5000, 3
30, 3000, 2

We can first use group by DeptID on Employee table and then get the Max salary from each Dept group.
SELECT	DeptID, MAX(salary) FROM Employee GROUP BY DeptID

[Table of Contents](#SQL)

Write SQL query to get the nth highest salary among all Employees.
Given a Employee Table with two columns
ID, Salary 10, 2000
11, 5000
12, 3000

Option 1: Use Subquery We can use following sub query approach for this:
SELECT * FROM Employee emp1 WHERE (N-1) = ( SELECT COUNT(DISTINCT(emp2.salary)) FROM Employee emp2 WHERE emp2.salary > emp1.salary)
Option 2: Using Rownum in Oracle
SELECT * FROM (SELECT emp.*,row_number() OVER (ORDER BY salary DESC) rnum FROM Employee emp) WHERE rnum = n;

[Table of Contents](#SQL)

How can you find 10 employees with Odd number as Employee ID?
In Oracle we can use Top to limit the number of records. We can also use Rownum < 11 to get the only 10 or less number of records.To find the Odd number Employee ID, we can use % function.
Sample Query with TOP:
SELECT TOP 10 ID FROM Employee WHERE ID % 2 = 1;
Sample Query with ROWNUM:
SELECT ID FROM Employee WHERE ID % 2 = 1 AND ROWNUM < 11;

[Table of Contents](#SQL)

Write SQL Query to get the names of employees whose date of birth is between 01/01/1990 to 31/12/2000.
This SQL query appears a bit tricky. We can use BETWEEN clause to get all the employees whose date of birth lies between two given dates.
Query will be as follows:
SELECT EmpName FROM Employees WHERE birth_date BETWEEN ‘01/01/1990’ AND ‘31/12/2000’
Remember BETWEEN is always inclusive of both the dates.

[Table of Contents](#SQL)

Write SQL Query to get the Quarter from date.
Answer: We can use to_char function with ‘Q’ option for quarter to get quarter from a date.
Use TO_CHAR with option ‘Q’ for Quarter
SELECT TO_CHAR(TO_DATE('3/31/2016', 'MM/DD/YYYY'), 'Q') AS quarter FROM DUAL

[Table of Contents](#SQL)

Write Query to find employees with duplicate email.
Employee table:
ID	NAME	EMAIL
10	John	jsmith
20	George	gadams
30	Jane	jsmith
We can use Group by clause on the column in which we want to find duplicate values.
Query would be as follows:
SELECT name, COUNT(email) FROM Employee GROUP BY email HAVING ( COUNT(email) > 1 )

[Table of Contents](#SQL)

Write a Query to find all Employee whose name contains the word "Rich", regardless of case.
E.g. Rich, RICH, rich.
We can use UPPER function for comparing the both sides with uppercase.
SELECT * FROM Employees WHERE UPPER(emp_name) like '%RICH%'

[Table of Contents](#SQL)

Is it safe to use ROWID to locate a record in Oracle SQL queries?
ROWID is the physical location of a row. We can do very fast lookup based on ROWID. In a transaction where we first search a few rows and then update them one by one, we can use ROWID. But ROWID of a record can change over time. If we rebuild a table a record can get a new ROWID. If a record is deleted, its ROWID can be given to another record. So it is not recommended to store and use ROWID in long term. It should be used in same transactions.

[Table of Contents](#SQL)

What is a Pseudocolumn?
A Pseudocolumn is like a table column, but it is not stored in the same table. We can select from a Pseudocolumn, but we can not insert, update or delete on a Pseudocolumn. A Pseudocolumn is like a function with no arguments. Two most popular Pseudocolumns in Oracle are ROWID and ROWNUM. NEXTVAL and CURRVAL are also pseudo columns.

[Table of Contents](#SQL)

What are the reasons for de- normalizing the data?
We de-normalize data when we need better performance. Sometimes there are many joins in a query due to highly normalized data. In that case, for faster data retrieval it becomes essential to de-normalize data.

[Table of Contents](#SQL)

What is the feature in SQL for writing If and Else statements?
In SQL, we can use CASE statements to write If/Else statements. We can also use DECODE function in Oracle SQL for writing simple If/Else logic.

[Table of Contents](#SQL)

What is the difference between DELETE and TRUNCATE in SQL?
Main differences between DELETE and TRUNCATE commands are:
DML vs. DDL: DELETE is a Data Manipulation Language (DML) command. TRUNCATE is a Data Definition Language (DDL) command.

Number of Rows: We can use DELETE command to remove one or more rows from a table. TRUNCATE command will remove all the rows from a table.
WHERE clause: DELETE command provides support for WHERE clause that can be used to filter the data that we want to delete. TRUNCATE command can only delete all the rows. There is no WHERE clause in TRUNCATE command.
Commit: After DELETE command we have to issue COMMIT or ROLLBACK command to confirm our changes. After TRUNCATE command there is no need to run COMMIT. Changes done by TRUNCATE command can not be rolled back.

[Table of Contents](#SQL)

What is the difference between DDL and DML commands in SQL?
Main differences between Data Definition Language (DDL) and Data Manipulation Language (DML) commands are:
+ DDL vs. DML: DDL statements are used for creating and defining the Database structure. DML statements are used for managing data within Database. Sample Statements: DDL statements are CREATE, ALTER, DROP, TRUNCATE, RENAME etc. DML statements are SELECT, INSERT, DELETE, UPDATE, MERGE, CALL etc.
+ Number of Rows: DDL statements work on whole table. CREATE will a create a new table. DROP will remove the whole table. TRUNCATE will delete all records in a table. DML statements can work on one or more rows. INSERT can insert one or more rows. DELETE can remove one or more rows.
+ WHERE clause: DDL statements do not have a WHERE clause to filter the data. Most of DML statements support filtering the data by WHERE clause.
+ Commit: Changes done by a DDL statement can not be rolled back. So there is no need to issue a COMMIT or ROLLBACK command after DDL statement. We need to run COMMIT or ROLLBACK to confirm our changed after running a DML statement.
+ Transaction: Since each DDL statement is permanent, we can not run multiple DDL statements in a group like Transaction. DML statements can be run in a Transaction. Then we can COMMIT or ROLLBACK this group as a transaction. E.g. We can insert data in two tables and commit it together in a transaction.
+ Triggers: After DDL statements no triggers are fired. But after DML statements relevant triggers can be fired.

[Table of Contents](#SQL)

Why do we use Escape characters in SQL queries?
In SQL, there are certain special characters and words that are reserved for special purpose. E.g. & is a reserved character. When we want to use these special characters in the context of our data, we have to use Escape characters to pass the message to database to interpret these as non Special / non Reserved characters.

[Table of Contents](#SQL)

What is the difference between Primary key and Unique key in SQL?
Main differences between Primary key and Unique key in SQL are:
+ Number: There can be only one Primary key in a table. There can be more than one Unique key in a table.
+ Null value: In some DBMS Primary key cannot be NULL. E.g. MySQL adds NOT NULL to Primary key. A Unique key can have null values.
+ Unique Identifier: Primary Key is a unique identifier of a record in database table. Unique key can be null and we may not be able to identify a record in a unique way by a unique key
+ Changes: It is not recommended to change a Primary key. A Unique key can be changed much easily.
+ Usage: Primary Key is used to identify a row in a table. A Unique key is used to prevent duplicate non-null values in a column.

[Table of Contents](#SQL)

What is the difference between INNER join and OUTER join in SQL?
Let say we have two tables X and Y.
The result of an INNER JOIN of X and Y is X intersect. It is the INNER overlapping intersection part of a Venn diagram. The result of an OUTER JOIN of X and Y is X union Y. It is the OUTER parts of a Venn diagram. E.g. Consider following two tables, with just one column x and y:

x	| y
- - -|- - 10 | 30
    20 | 40
    30 | 50
    40 | 60
    In above tables (10,20) are unique to table X, (30,40) are common, and (50,60) are unique to table Y.
    INNER JOIN An INNER JOIN by using following query will give the intersection of the two tables X and Y. The intersection is the common data between these tables.
    select * from X INNER JOIN Y on X.x =Y.y;
    x	| y
    --- +-- 30 | 30
    40 | 40

OUTER JOIN
A full OUTER JOIN by using following query will us the union of X and Y. It will have all the rows in X and all the rows in Y. If some row in X has not corresponding value in Y, then Y side will be null, and vice versa.
select * from X FULL OUTER JOIN Y on X.x = Y.y;
x| y
----- + -----
10 | null
20 | null

30 |	30
40 |	40
null |	60
null |	50

[Table of Contents](#SQL)

What is the difference between Left OUTER Join and Right OUTER Join?
Let say we have two tables X and Y.
The result of an LEFT OUTER JOIN of X and Y is all rows of X and common rows between X and Y.
The result of an RIGHT OUTER JOIN of X and Y is all rows of Y and common rows between X and Y.
E.g.
Consider following two tables, with just one column x and y:

x| y
- - -|- - 10 | 30
    20 | 40
    30 | 50
    40 | 60

In above tables (10,20) are unique to table X, (30,40) are common, and (50,60) are unique to table Y.
LEFT OUTER JOIN
A left OUTER JOIN by using following query will give us all rows in X and common rows in X and Y.
select * from X LEFT OUTER JOIN Y on X.x = Y.y;
x| y
-- -+-----
10 | null
20 | null
30 |30
40 |40
RIGHT OUTER JOIN
A right OUTER JOIN by using following query will give all rows in Y and common rows in X and Y.
select * from X RIGHT OUTER JOIN Y on X.x = Y.y;
x| y
----- +----
30	|	30
40	|	40
null	|	50
null	|	60

[Table of Contents](#SQL)

What is the datatype of ROWID?
ROWID Pseudocolumn in Oracle is of ROWID datatype. It is a string that represents the address of a row in the database.

[Table of Contents](#SQL)

What is the difference between where clause and having clause?
We use where clause to filter elements based on some criteria on individual records of a table.
E.g. We can select only employees with first name as John.
SELECT ID, Name FROM Employee WHERE name = ‘John’
We use having clause to filter the groups based on the values of aggregate functions.
E.g. We can group by department and only select departments that have more than 10 employees.
SELECT deptId, count(1) FROM Employee GROUP BY deptId HAVING count(*) > 10.

[Table of Contents](#SQL)

How will you calculate the number of days between two dates in MySQL?
We can use DATEDIFF function for this purpose. The query to get the number of days between two dates in MySQL is as follows:
SELECT DATEDIFF('2016-12- 31', '2015-01-01');

[Table of Contents](#SQL)

What are the different types of Triggers in MySQL?
MySQL	supports	six	types	of triggers. These are as follows:
+ Before Insert: This trigger runs before inserting a new row in a table.
+ After Insert: This triggerruns after inserting a new row in a table.
+ Before Update: This trigger runs before updating an existing row in a table.
+ After Update: This trigger runs after updating an existing row in a table.
+ Before Delete: This trigger runs before deleting an existing row in a table.
+ After Delete: This trigger runs after deleting an existing row in a table.

[Table of Contents](#SQL)

What are the differences between Heap table and temporary table in MySQL?
+ Duration: Heap tables are stored in memory. Therefore a Heap table remains in existence even if the session is disconnected. When we restart Database, Heap tables get cleaned up.
+ Temporary tables are valid only during a session. Once the session is disconnected, temporary table is cleaned up.
+ Privilege: We need special privilege to create a Temporary table. Heap tables are just another form of storage in MySQL.
+ Sharing: Temporary tables are not shared between clients. Each connection will have a unique temporary table. But Heap tables can be shared between clients.

[Table of Contents](#SQL)

What is a Heap table in MySQL?
In MySQL there are tables that are present in memory. These are called Heap tables. During table creation we specify TYPE as HEAP for HEAP tables.
Heap tables provide very fast access to data. We can not store BLOB or TEXT datatype in a HEAP table. These tables also do not support AUTO_INCREMENT. Once we restart the Database, data in HEAP tables is lost.

[Table of Contents](#SQL)

What is the difference between BLOB and TEXT data type in MySQL?
BLOB is a Binary large Object. We can store a large amount of binary data in a BLOB data type column.
TEXT is non-binary, character based string data type. We can store text data in TEXT column. We have to define a character set with a TEXT column.
TEXT can be easily converted into plain text.
BLOB has four types: TINYBLOB, BLOB, MEDIUMBLOB and LONGBLOB.
Where as, TEXT has its own four types: TINYTEXT,TEXT, MEDIUMTEXT, LONGTEXT.

[Table of Contents](#SQL)

What will happen when AUTO_INCREME on an INTEGER column reaches MAX_VALUE in MySQL?
Once a column reaches the MAX_VALUE,		the AUTO_INCREMENT	stops working. It gives following error in log:
ERROR: 1467 (HY000): Failed to read	auto-increment	value	from storage engine

[Table of Contents](#SQL)

What are the advantages of MySQL as compared with Oracle DB?
Some of the main advantages of MySQL over Oracle DB are as follows:
+ Cost: MySQL is an Open Source and free RDBMS software. Oracle is usually a paid option for RDBMS.
+ Space: MySQL uses around 1 MB to run whereas Oracle may need as high as 128 MB to run the database server.
+ Flexibility: MySQL can be used to run a small website as well as very large scale systems. Oracle is generally used in medium to large scale systems.
+ Management: In MySQL, database administration is much easier due to self- management features like- automatic space expansion,
+ auto-restart and dynamic configuration changes. In Oracle dedicated DBA has to work on managing the Database.
+ Portable: MySQL is easily portable to different hardware and operating system. Migrating Oracle from one platform to another is a tougher task.

[Table of Contents](#SQL)

What are the disadvantages of MySQL?
Some of the main disadvantages of MySQL are as follows:
Dependent on Additional S/W: MySQL has less number of features in standard out-of-box version. So we have to add additional software to get more features. It gets difficult to find, decide and use the additional software with MySQL. SQL Compliance: MySQL is not full SQL compliant. Due to this developers find it difficult to cope with the syntax of SQL in MySQL. Transaction handling: Some users complain that DB transactions are not handled properly in MySQL.

[Table of Contents](#SQL)

What is the difference between CHAR and VARCHAR datatype in MySQL?
Some of the main differences between CHAR and VARCHAR datatypes in MySQL are as follows:
+ Size: In CHAR type column, length is fixed. In a VARCHAR	type	column length can vary.
+ Storage: There are different mechanisms to store and retrieve CHAR and VARCHAR data types in MySQL.
+ Maximum Size: A CHAR data type can hold maximum 255 characters. A VARCHAR datatype can store up to 4000 characters.
+ Speed: CHAR datatype is 50% faster than VARCHAR datatype in MySQL.
+ Memory Allocation: A CHAR datatype column uses static memory allocation. Since the length of data stored in a VARCHAR can vary, this datatype uses dynamic memory allocation.

[Table of Contents](#SQL)

What is the use of 'i_am_a_dummy flag' in MySQL?
In MySQL, there is falg "ia_am_a_dummy" that can be used to save beginner developers from erroneous query like 'DELETE FROM table_name'. If we run this query it will delete all the data from table names table_name. With     'i_am_a_dummy      flag', MySQL will not permit running such a query. It will prompt user to create a query with WHERE clause so that only specific data is deleted. We can achieve similar functionality with 'safe_updates' option in MySQL. This flag also works on UPDATE statement to restrict updates on a table without WHERE clause.

[Table of Contents](#SQL)

How can we get current date and time in MySQL?
We can use following query in MySQL to get the current date:
SELECT CURRENT_DATE();
We can use following query in MySQL to get the current time as well as date:
SELECT NOW();

[Table of Contents](#SQL)

What is the difference between timestamp in Unix and MySQL?
In Unix as well as in MySQL, timestamp is stored as a 32-bit integer.
A timestamp is the number of seconds from the Unix Epoch on January 1st, 1970 at UTC.
In MySQL we can represent the timestamp in a readable format.
Timestamp format in MySQL is YYYY-MM-DD HH:MM:SS

[Table of Contents](#SQL)

How will you limit a MySQL query to display only top 10 rows?
We can use LIMIT clause in MySQL to limit a query to a range of rows.
Following query will give top 10 rows from the table with table_name:
SELECT * FROM <table_name> LIMIT 0,10;
Following query will give 6 rows starting from the 4th row in table with table_name:
SELECT * FROM <table_name> LIMIT 3,6;

[Table of Contents](#SQL)

What is automatic initialization and updating for TIMESTAMP in a MySQL table?
In MySQL, there is a TIMESTAMP datatype that provides features like automatic initialization and updating to current time and date. If a column is auto-initialized, then it will be set to current timestamp on inserting a new row with no value for the column. If a column is auto-updated, then its value will be updated to current timestamp when the value of any other column in the same row is updated. We can mark a column as DEFAULT to prevent this auto- initialize and auto-update behavior.

[Table of Contents](#SQL)

How can we get the list of all the indexes on a table?
We can use following command to get the list of all the indexes on a table in MySQL:
SHOW INDEX FROM table_name; At maximum we can use 16 columns in a multi-column index of table.

[Table of Contents](#SQL)

What is SAVEPOINT in MySQL?
SAVEPOINT is a statement in SQL. We can use SAVEPOINT <savepoint_name> statement to create a point of time in a Database transaction with a name. Later we can use this savepoint to rollback the transaction upto that point of time.

[Table of Contents](#SQL)

What is the difference between ROLLBACK TO SAVEPOINT and RELEASE SAVEPOINT?
We use ROLLBACK TO SAVEPOINT statement to undo the effect of a transaction upto the SAVEPOINT mentioned in ROLLBACK statement.
RELEASE SAVEPOINT is simply used to delete the SAVEPOINT with a name from a transaction. There is commit or rollback for SAVEPOINT in RELEASE statement.In both the cases we should have first created a SAVEPOINT. Else we will get the error while doing ROLLBACK or RELEASE of a SAVEPOINT.

[Table of Contents](#SQL)

How will you search for a String in MySQL column?
We can use REGEXP operator to search for a String in MySQL column. It is regular expression search on columns with text type value. We can define different types of regular expressions and search them in a text with the REGEXP expression that can match our crietria.

[Table of Contents](#SQL)

How can we find the version of the MySQL server and the name of the current database by SELECT query?
We can use built in functions VERSION() and DATABASE() in MySQL to get the version of MySQL server and the name of database in MySQL.
Query is as follows: SELECT	VERSION(), DATABASE();

[Table of Contents](#SQL)

What is the use of IFNULL() operator in MySQL?
We use IFNULL operator in MySQL to get a non-null value for a column with null value.
IFNULL(expr1, expr2)
If expr1 is not null then expr1 is returned. If expr1 is null then expr2 is returned.
Eg.	SELECT	name, IFNULL(id,'Unknown') AS 'id' FROM user;
If id is not null then id is returned. If id is null then Unknown is returned.

[Table of Contents](#SQL)

How will you check if a table exists in MySQL?
We can use CHECK TABLE query to see the existence of a table in MySQL.
Query is as follows: CHECK TABLE <table_name>;

[Table of Contents](#SQL)

How will you see the structure of a table in MySQL?
We can use DESC query to see the structure of a table in MySQL. It will return the name of columns and their datatype in a table. Query is as follows: DESC <table_name>;

[Table of Contents](#SQL)

What are the objects that can be created by CREATE statement in MySQL?
We can create following objects by CREATE statement in MySQL:
DATABASE USER TABLE INDEX
VIEW TRIGGER EVENT FUNCTION PROCEDURE

[Table of Contents](#SQL)

How will you see the current user logged into MySQL connection?
We can use USER() command to get the user logged into MySQL connection.
Command is as follows: SELECT USER();
How can you copy the structure of a table into another table without copying the data?
It is a  trick question. But it has practical use in day to day work.
Query for this is as follows: CREATE TABLE table_name AS SELECT * FROM USER WHERE 1 > 2;
In this example condition in WHERE clause will be always false. Due to this no data is retrieved by SELECT query.

[Table of Contents](#SQL)

What is the difference between Batch and Interactive modes of MySQL?
In Interactive mode, we use command line interface and enter queries one by one. MySQL will execute the query and return the result in command line interface. In Batch mode of MySQL we can write all the queries in a SQL file. Then we can run this SQL file from MySQL command line or from Scheduler Job. MySQL will execute all the queries and return the result.

[Table of Contents](#SQL)

How can we get a random number between 1 and 100 in MySQL?
In MySQL we have a RAND() function that returns a random number between 0 and 1.
SELECT RAND();
If we want to get a random number between 1 and 100, we can use following query:
SELECT RAND() * 100;

[Table of Contents](#SQL)

What does SQL in MySQL stand for?
The SQL in MySQL stands for Structured Query Language. This language is also used in other databases such as Oracle and Microsoft SQL Server.  One can use commands such as the following to send requests from a database:
SELECT title FROM publications WHERE author = ' J. K. Rowling’;
Note that SQL is not case sensitive. However, it is a good practice to write the SQL keywords in CAPS and other names and variables in a small case.

[Table of Contents](#SQL)

What does a MySQL database contain?
A MySQL database contains one or more tables, each of which contains records or rows. Within these rows are various columns or fields that contain the data itself.

[Table of Contents](#SQL)

How can you interact with MySQL?
There are three main ways you can interact with MySQL:
+ using a command line
+ via a web interface
+ through a programming language

[Table of Contents](#SQL)

What is MySQL Database Queries?
A query is a specific request or a question. One can query a database for specific information and have a record returned.

[Table of Contents](#SQL)

What are some common MySQL commands?
+ ALTER	To alter a database or table
+ BACKUP	To back-up a table
+ \c	To cancel Input
+ CREATE	To create a database
+ DELETE	To delete a row from a table
+ DESCRIBE	To describe a table's columns
+ DROP	To delete a database or table
+ EXIT(ctrl+c)	To exit
+ GRANT	To change user privileges
+ HELP (\h, \?)	Display help
+ INSERT	Insert data
+ LOCK	Lock table(s)
+ QUIT(\q)	Same as EXIT
+ RENAME	Rename a Table
+ SHOW	List details about an object
+ SOURCE	Execute a file
+ STATUS (\s)	Display the current status
+ TRUNCATE	Empty a table
+ UNLOCK	Unlock table(s)
+ UPDATE	Update an existing record
+ USE	Use a database

[Table of Contents](#SQL)

How do you create a database in MySQL?
Use the following command to create a new database called ‘books’:
CREATE DATABASE books;

[Table of Contents](#SQL)

How do you create a table using MySQL?
Use the following to create a table using MySQL:
CREATE TABLE history (
author VARCHAR(128),
title VARCHAR(128),
type VARCHAR(16),
year CHAR(4)) ENGINE InnoDB;

[Table of Contents](#SQL)

How do you Insert Data Into MySQL?
The INSERT INTO statement is used to add new records to a MySQL table:
INSERT INTO table_name (column1, column2, column3,...)
VALUES (value1, value2, value3,...)
If we want to add values for all the columns of the table, we do not need to specify the column names in the SQL query. However, the order of the values should be in the same order as the columns in the table. The INSERT INTO syntax would be as follows:
INSERT INTO table_name
VALUES (value1, value2, value3, ...);

[Table of Contents](#SQL)

How do you remove a column from a database?
You can remove a column by using the DROP keyword:
ALTER TABLE classics DROP pages;

[Table of Contents](#SQL)

How to create an Index in MySQL?
In MySQL, there are different index types, such as a regular INDEX, a PRIMARY KEY, or a FULLTEXT index. You can achieve fast searches with the help of an index. Indexes speed up performance by either ordering the data on disk so it's quicker to find your result or, telling the SQL engine where to go to find your data.
Example: Adding indexes to the history table:
+ ALTER TABLE history ADD INDEX(author(10));
+ ALTER TABLE history ADD INDEX(title(10));
+ ALTER TABLE history ADD INDEX(category(5));
+ ALTER TABLE history ADD INDEX(year);

[Table of Contents](#SQL)

How to Delete Data From a MySQL Table?
In MySQL, the DELETE statement is used to delete records from a table:
DELETE FROM table_name
WHERE column_name = value_name

[Table of Contents](#SQL)

How do you view a database in MySQL?
One can view all the databases on the MySQL server host using the following command:
mysql> SHOW DATABASES;

[Table of Contents](#SQL)

What are the Numeric Data Types in MySQL?
MySQL has numeric data types for integer, fixed-point, floating-point, and bit values, as shown in the table below. Numeric types can be signed or unsigned, except BIT. A special attribute enables the automatic generation of sequential integer or floating-point column values, which is useful for applications that require a series of unique identification numbers.

+ TINYINT	Very Small Integer
+ SMALLINT	Small Integer
+ MEDIUMINT	Medium-sized Integer
+ INT	Standard Integer
+ BIGINT	Large Integer
+ DECIMAL	Fixed-point number
+ FLOAT	Single-precision floating-point number
+ DOUBLE	Double-precision floating-point number
+ BIT	Bit-field

[Table of Contents](#SQL)

What are the String Data Types in MySQL?
+ CHAR - fixed-length nonbinary(character) string
+ VARCHAR	variable-length nonbinary string
+ BINARY	fixed-length binary string
+ VARBINARY	variable-length binary string
+ TINYBLOB	Very small BLOB(binary large object)
+ BLOB	Small BLOB
+ MEDIUMBLOB	Medium-sized BLOB
+ LONGBLOB	Large BLOB
+ TINYTEXT	A very small nonbinary string
+ TEXT	Small nonbinary string
+ MEDIUMTEXT	Medium-sized nonbinary string
+ LONGTEXT	Large nonbinary string
+ ENUM	An enumeration; each column value is assigned, one enumeration member
+ SET	A set; each column value is assigned zero or more set members
+ NULL	NULL in SQL is the term used to represent a missing value. A NULL value in a table is a value in a field that appears to be blank. This value is different than a zero value or a field that contains spaces.

[Table of Contents](#SQL)

What are the Temporal Data Types in MySQL?
+ DATE	A date value, in ' CCYY-MM-DD ' Format
+ TIME	A Time value, in ' hh : mm :ss ' format
+ DATETIME	Date and time value, in ' CCYY-MM-DD hh : mm :ss ' format
+ TIMESTAMP	A timestamp value, in ' CCYY-MM-DD hh : mm :ss ' format
+ YEAR	A year value, in CCYY or YY format
Example: To select the records with an Order Date of "2018-11-11" from a table:
SELECT * FROM Orders WHERE OrderDate='2018-11-11'

[Table of Contents](#SQL)

What is BLOB in MySQL?
BLOB is an acronym that stands for a binary large object. It is used to hold a variable amount of data.
There are four types of BLOB:
+ TINYBLOB
+ BLOB
+ MEDIUMBLOB
+ LONGBLOB
A BLOB can hold a very large amount of data. For example - documents, images, and even videos. You could store your complete novel as a file in a BLOB if needed.

[Table of Contents](#SQL)

How to add users in MySQL?
You can add a User by using the CREATE command and specifying the necessary credentials. For example:
CREATE USER ‘testuser’ IDENTIFIED BY ‘sample password’;

[Table of Contents](#SQL)

What is MySQL Views?
In MySQL, a view consists of a set of rows that is returned if a particular query is executed. This is also known as a ‘virtual table’. Views make it easy to retrieve the way of making the query available via an alias.
The advantages of views are:
+ Simplicity
+ Security
+ Maintainability

[Table of Contents](#SQL)

How do you create and execute views in MySQL?
Creating a view is accomplished with the CREATE VIEW statement. As an example:
CREATE [OR REPLACE] [ALGORITHM = {MERGE | TEMPTABLE | UNDEFINED }] [DEFINER = { user | CURRENT_USER }][SQL SECURITY { DEFINER | INVOKER }] VIEW view_name [(column_list)] AS select_statement [WITH [CASCADED | LOCAL] CHECK OPTION]

[Table of Contents](#SQL)

What is MySQL Triggers?
A trigger is a task that executes in response to some predefined database event, such as after a new row is added to a particular table. Specifically, this event involves inserting, modifying, or deleting table data, and the task can occur either prior to or immediately following any such event.
Triggers have many purposes, including:
+ Audit Trails
+ Validation
+ Referential integrity enforcement

[Table of Contents](#SQL)

How many Triggers are possible in MySQL?
There are six Triggers allowed to use in the MySQL database:
+ Before Insert
+ After Insert
+ Before Update
+ After Update
+ Before Delete
+ After Delete

[Table of Contents](#SQL)

What is the MySQL server?
The server, mysqld, is the hub of a MySQL installation; it performs all manipulation of databases and tables.

[Table of Contents](#SQL)

What are the MySQL clients and utilities?
Several MySQL programs are available to help you communicate with the server. For administrative tasks, some of the most important ones are listed here:
• mysql—An interactive program that enables you to send SQL statements to the server and to view the results. You can also use mysql to execute batch scripts (text files containing SQL statements).
• mysqladmin—An administrative program for performing tasks such as shutting down the server, checking its configuration, or monitoring its status if it appears not to be functioning properly.
• mysqldump—A tool for backing up your databases or copying databases to another server.
• mysqlcheck and myisamchk—Programs that help you perform table checking, analysis, and optimization, as well as repairs if tables become damaged. mysqlcheck works with MyISAM tables and to some extent with tables for other storage engines. myisamchk is for use only with MyISAM tables.

[Table of Contents](#SQL)

Can you explain the logical architecture of MySQL?
The top layer contains the services most network-based client/server tools or servers need such as connection handling, authentication, security, and so forth.
The second layer contains much of MySQL’s brains. This has the code for query parsing, analysis, optimization, caching, and all the built-in functions.
The third layer contains the storage engines that are responsible for storing and retrieving the data stored in MySQL.

[Table of Contents](#SQL)

What is Scaling in MySQL?
In MySQL, scaling capacity is actually the ability to handle the load, and it’s useful to think of load from several different angles such as:
Quantity of data
Number of users
User activity
Size of related datasets

[Table of Contents](#SQL)

What is Sharding in SQL?
The process of breaking up large tables into smaller chunks (called shards) that are spread across multiple servers is called Sharding.
The advantage of Sharding is that since the sharded database is generally much smaller than the original; queries, maintenance, and all other tasks are much faster.

[Table of Contents](#SQL)

What are Transaction Storage Engines in MySQL?
To be able to use MySQL’s transaction facility, you have to be using MySQL’s InnoDB storage engine (which is the default from version 5.5 onward). If you are not sure which version of MySQL your code will be running on, rather than assuming InnoDB is the default engine you can force its use when creating a table, as follows.

[Table of Contents](#SQL)

What is MySQL?
MySQL is a database management system for web servers. It can grow with the website as it is highly scalable. Most of the websites today are powered by MySQL.

[Table of Contents](#SQL)

What are some of the advantages of using MySQL?
Flexibility: MySQL runs on all operating systems
Power: MySQL focuses on performance
Enterprise-Level SQL Features: MySQL had for some time been lacking in advanced features such as subqueries, views, and stored procedures.
Full-Text Indexing and Searching
Query Caching: This helps enhance the speed of MySQL greatly
Replication: One MySQL server can be duplicated on another, providing numerous advantages
Configuration and Security

[Table of Contents](#SQL)

What do you mean by databases?
A database is a structured collection of data stored in a computer system and organized in a way to be quickly searched. With databases, information can be rapidly retrieved.

[Table of Contents](#SQL)

Query to find Second Highest marks of a Student?
Based On the Below Student table We are Written All the Queries.
Student Table
SELECT marks FROM Student ORDER by marks DESC limit 1, 1;

[Table of Contents](#SQL)

Query to Find Duplicate Rows in Table?
SELECT std_id, COUNT(std_id) as cnt FROM Student GROUP by std_id having cnt > 1

[Table of Contents](#SQL)

What is the Query to Fetch First Record from Student Table?
SELECT * from Student where id = 1;

[Table of Contents](#SQL)

What is the Query to Fetch Last Record from Student Table?
SELECT * FROM Student order by id desc limit 1

[Table of Contents](#SQL)

What is Query to Display First 4 Records from Student Table?
SELECT *  FROM Student limit 4

[Table of Contents](#SQL)

What is Query to Display Last 3 Records from Student Table?
SELECT *  FROM Student order by std_id Desc limit 3

[Table of Contents](#SQL)

What is Query to Display Nth Record from Student Table?
Select * from Student  where id = $n;

[Table of Contents](#SQL)

How To Get 3 Highest Marks From Student Table?
SELECT distinct(marks) FROM Student ORDER BY marks DESC LIMIT 0,3

How To Display Odd Rows In Student Table?
SELECT * FROM Student where MOD(id,2) = 1

How To Display Even Rows In Student Table?
SELECT * FROM Student where MOD(id,2) = 0

How Can I Create Table With Same Structure Of Student Table?
Create table std as Select * from Student;

Select All Records From Student Table Whose Name Is abhi And geethasri.
Select * from Student  where Name in(‘Abhi’ , ’Geethasri’);

What Is Ddl, Dml And Dcl ?
If you look at the large variety of SQL commands, they can be divided into three large subgroups. Data Definition Language deals with database schemas and descriptions of how the data should reside in the database, therefore language statements like CREATE TABLE or ALTER TABLE belong to DDL. DML deals with data manipulation, and therefore includes most common SQL statements such SELECT, INSERT, etc. Data Control Language includes commands such as GRANT, and mostly concerns with rights, permissions and other controls of the database system.

How Do You Get The Number Of Rows Affected By Query?
SELECT COUNT (user_id) FROM users would only return the number of user_id’s.

If The Value In The Column Is Repeatable, How Do You Find Out The Unique Values?
Use DISTINCT in the query, such as SELECT DISTINCT user_firstname FROM users; You can also ask for a number of distinct values by saying SELECT COUNT (DISTINCT user_firstname) FROM users;

How Do You Return The A Hundred Books Starting From 25th?
SELECT book_title FROM books LIMIT 25, 100. The first number in LIMIT is the offset, the second is the number.

You Wrote A Search Engine That Should Retrieve 10 Results At A Time, But At The Same Time You'd Like To Know How Many Rows There're Total. How Do You Display That To The User?
SELECT SQL_CALC_FOUND_ROWS page_title FROM web_pages LIMIT 1,10; SELECT FOUND_ROWS(); The second query (not that COUNT() is never used) will tell you how many results there’re total, so you can display a phrase "Found 13,450,600 results, displaying 1-10". Note that FOUND_ROWS does not pay attention to the LIMITs you specified and always returns the total number of rows affected by query.

How Would You Write A Query To Select All Teams That Won Either 2, 4, 6 Or 8 Games?
SELECT team_name FROM teams WHERE team_won IN (2, 4, 6, 8)

How Would You Select All The Users, Whose Phone Number Is Null?
SELECT user_name FROM users WHERE ISNULL(user_phonenumber);

What Does This Query Mean: Select User_name, User_isp From Users Left Join Isps Using (user_id) ?
It’s equivalent to saying SELECT user_name, user_isp FROM users LEFT JOIN isps WHERE users.user_id=isps.user_id

How Do You Find Out Which Auto Increment Was Assigned On The Last Insert?
SELECT LAST_INSERT_ID() will return the last value assigned by the auto_increment function. Note that you don’t have to specify the table name.

What Does -i-am-a-dummy Flag To Do When Starting Mysql?
Makes the MySQL engine refuse UPDATE and DELETE commands where the WHERE clause is not present.

On Executing The Delete Statement I Keep Getting The Error About Foreign Key Constraint Failing. What Do I Do?
What it means is that so of the data that you’re trying to delete is still alive in another table. Like if you have a table for universities and a table for students, which contains the ID of the university they go to, running a delete on a university table will fail if the students table still contains people enrolled at that university. Proper way to do it would be to delete the offending data first, and then delete the university in question. Quick way would involve running SET foreign_key_checks=0 before the DELETE command, and setting the parameter back to 1 after the DELETE is done. If your foreign key was formulated with ON DELETE CASCADE, the data in dependent tables will be removed automatically.

When Would You Use Order By In Delete Statement?
When you’re not deleting by row ID. Such as in DELETE FROM techpreparation_com_questions ORDER BY timestamp LIMIT 1.

How Can You See All Indexes Defined For A Table?
SHOW INDEX FROM techpreparation_questions;

How Would You Change A Column From Varchar(10) To Varchar(50)?
ALTER TABLE techpreparation_questions CHANGE techpreparation_content techpreparation_CONTENT VARCHAR(50).

How Would You Delete A Column?
ALTER TABLE techpreparation_answers DROP answer_user_id.

How Would You Change A Table To Innodb?
ALTER TABLE techpreparation_questions ENGINE innodb;

When You Create A Table, And Then Run Show Create Table On It, You Occasionally Get Different Results Than What You Typed In. What Does Mysql Modify In Your Newly Created Tables?
1. VARCHARs with length less than 4 become CHARs
2. CHARs with length more than 3 become VARCHARs.
3. NOT NULL gets added to the columns declared as PRIMARY KEYs
4. Default values such as NULL are specified for each column

How Do I Find Out All Databases Starting With tech To Which I Have Access To?
SHOW DATABASES LIKE ‘tech%’;

How Do You Concatenate Strings In Mysql?
CONCAT (string1, string2, string3)

How Do You Get A Portion Of A String?
SELECT SUBSTR(title, 1, 10) from techpreparation_questions;

What's The Difference Between Char_length And Length?
The first is, naturally, the character count. The second is byte count. For the Latin characters the numbers are the same, but they’re not the same for Unicode and other encodings.

How Do You Convert A String To Utf-8?
SELECT (techpreparation_question USING utf8);

What Do % And _ Mean Inside Like Statement?
% corresponds to 0 or more characters, _ is exactly one character.

What Does + Mean In Regexp?
At least one character. Appendix G. Regular Expressions from MySQL manual is worth perusing before the interview.

How Do You Get The Month From A Timestamp?
SELECT MONTH(techpreparation_timestamp) from techpreparation_questions;

How Do You Offload The Time/date Handling To Mysql?
SELECT DATE_FORMAT(techpreparation_timestamp, ‘%Y-%m-%d’) from techpreparation_questions; A similar TIME_FORMAT function deals with time.

How Do You Add Three Minutes To A Date?
ADDDATE(techpreparation_publication_date, INTERVAL 3 MINUTE)

What's The Difference Between Unix Timestamps And Mysql Timestamps?
Internally Unix timestamps are stored as 32-bit integers, while MySQL timestamps are stored in a similar manner, but represented in readable YYYY-MM-DD HH:MM:SS format.

How Do You Convert Between Unix Timestamps And Mysql Timestamps?
UNIX_TIMESTAMP converts from MySQL timestamp to Unix timestamp, FROM_UNIXTIME converts from Unix timestamp to MySQL timestamp.

What Are Enums Used For In Mysql?
You can limit the possible values that go into the table. CREATE TABLE months (month ENUM ‘January’, ‘February’, ‘March’,…); INSERT months VALUES (’April’);

How Are Enums And Sets Represented Internally?
As unique integers representing the powers of two, due to storage optimizations.

How Do You Start And Stop Mysql On Windows?
net start MySQL, net stop MySQL

How Do You Start Mysql On Linux?
/etc/init.d/mysql start

Explain The Difference Between Mysql And Mysql Interfaces In Php?
mysql is the object-oriented version of mysql library functions.

What's The Default Port For Mysql Server?
3306 is the default port for MYSQL.

What Does Tee Command Do In Mysql?
tee followed by a filename turns on MySQL logging to a specified file. It can be stopped by command note.

Can You Save Your Connection Settings To A Conf File?
Yes, and name it ~/.my.conf. You might want to change the permissions on the file to 600, so that it’s not readable by others.

How Do You Change A Password For An Existing User Via Mysqladmin?
mysqladmin -u root -p password "newpassword"

Use Mysqldump To Create A Copy Of The Database?
mysqldump -h mysqlhost -u username -p mydatabasename > dbdump.sql

Have You Ever Used Mysql Administrator And Mysql Query Browser?
Describe the tasks you accomplished with these tools.

What Are Some Good Ideas Regarding User Security In Mysql?
There is no user without a password. There is no user without a user name. There is no user whose Host column contains % (which here indicates that the user can log in from anywhere in the network or the Internet). There are as few users as possible (in the ideal case only root) who have unrestricted access.

Explain The Difference Between Myisam Static And Myisam Dynamic. ?
In MyISAM static all the fields have fixed width. The Dynamic MyISAM table would include fields such as TEXT, BLOB, etc. to accommodate the data types with various lengths. MyISAM Static would be easier to restore in case of corruption, since even though you might lose some data, you know exactly where to look for the beginning of the next record.

What Does Myisamchk Do?
It compressed the MyISAM tables, which reduces their disk usage.

Explain Advantages Of Innodb Over Myisam?
Row-level locking, transactions, foreign key constraints and crash recovery.

Explain Advantages Of Myisam Over Innodb?
Much more conservative approach to disk space management - each MyISAM table is stored in a separate file, which could be compressed then with myisamchk if needed. With InnoDB the tables are stored in tablespace, and not much further optimization is possible. All data except for TEXT and BLOB can occupy 8,000 bytes at most. No full text indexing is available for InnoDB. TRhe COUNT(*)s execute slower than in MyISAM due to tablespace complexity.

What Are Heap Tables In Mysql?
HEAP tables are in-memory. They are usually used for high-speed temporary storage. No TEXT or
BLOB fields are allowed within HEAP tables. You can only use the comparison operators = and <=>. HEAP tables do not support AUTO_INCREMENT. Indexes must be NOT NULL.

How Do You Control The Max Size Of A Heap Table?
MySQL config variable max_heap_table_size.

What Are Csv Tables?
Those are the special tables, data for which is saved into comma-separated values files. They cannot be indexed.

Explain Federated Tables?
Introduced in MySQL 5.0, federated tables allow access to the tables located on other databases on other servers.

What Is Serial Data Type In Mysql?
BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT
SERIAL is an alias for BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE

What Happens When The Column Is Set To Auto Increment And You Reach The Maximum Value For That Table?
It stops incrementing. It does not overflow to 0 to prevent data losses, but further inserts are going to produce an error, since the key has been used already.

Explain The Difference Between Bool, Tinyint And Bit. ?
Prior to MySQL 5.0.3: those are all synonyms. After MySQL 5.0.3: BIT data type can store 8 bytes of data and should be used for binary data.

Explain The Difference Between Float, Double And Real. ?
+ FLOATs store floating point numbers with 8 place accuracy and take up 4 bytes.
+ DOUBLEs store floating point numbers with 16 place accuracy and take up 8 bytes.
+ REAL is a synonym of FLOAT for now.

If You Specify The Data Type As Decimal (5,2), What's The Range Of Values That Can Go In This Table?
999.99 to -99.99. Note that with the negative number the minus sign is considered one of the digits.

What Happens If A Table Has One Column Defined As Timestamp?
That field gets the current timestamp whenever the row gets altered.

But What If You Really Want To Store The Timestamp Data, Such As The Publication Date Of The Article?
Create two columns of type TIMESTAMP and use the second one for your real data.

Explain Data Type Timestamp Default Current_timestamp On Update Current_timestamp ?
The column exhibits the same behavior as a single timestamp column in a table with no other timestamp columns.

What Does Timestamp On Update Current_timestamp Data Type Do?
On initialization places a zero in that column, on future updates puts the current value of the timestamp in.

Explain Timestamp Default 2006:09:02 17:38:44? On Update Current_timestamp. ?
A default value is used on initialization, a current timestamp is inserted on update of the row.

If I Created A Column With Data Type Varchar(3), What Would I Expect To See In Mysql Table?
CHAR(3), since MySQL automatically adjusted the data type.

General Information About Mysql.
MySQL is a very fast, multi-threaded, multi-user, and robust SQL (Structured Query Language) database server.

Why Sql Is A Database Management System?
A database is a structured collection of data. It may be anything from a simple shopping list to a picture gallery or the vast amounts of information in a corporate network. To add, access, and process data stored in a computer database, you need a database management system such as MySQL. Since computers are very good at handling large amounts of data, database management plays a central role in computing, as stand-alone utilities, or as parts of other applications.

Why Use Mysql?
MySQL is very fast, reliable, and easy to use. If that is what you are looking for, you should give it a try. MySQL also has a very practical set of features developed in very close cooperation with our users. You can find a performance comparison of MySQL to some other database managers on our benchmark page. See section 12.7 Using Your Own Benchmarks. MySQL was originally developed to handle very large databases much faster than existing solutions and has been successfully used in highly demanding production environments for several years. Though under constant development, MySQL today offers a rich and very useful set of functions. The connectivity, speed, and security make MySQL highly suited for accessing databases on the Internet.

How Mysql Optimizes Distinct ?
DISTINCT is converted to a GROUP BY on all columns, DISTINCT combined with ORDER BY will in many cases also need a temporary table.
When combining LIMIT # with DISTINCT, MySQL will stop as soon as it finds # unique rows.
If you don't use columns from all used tables, MySQL will stop the scanning of the not used tables as soon as it has found the first match.
SELECT DISTINCT t1.a FROM t1,t2 where t1.a=t2.a;
In the case, assuming t1 is used before t2 (check with EXPLAIN), then MySQL will stop reading from t2 (for that particular row in t1) when the first row in t2 is found.

How Mysql Optimizes Limit ?
In some cases MySQL will handle the query differently when you are using LIMIT # and not using HAVING:
+ If you are selecting only a few rows with LIMIT, MySQL will use indexes in some cases when it normally would prefer to do a full table scan.
+ If you use LIMIT # with ORDER BY, MySQL will end the sorting as soon as it has found the first # lines instead of sorting the whole table.
When combining LIMIT # with DISTINCT, MySQL will stop as soon as it finds # unique rows.
In some cases a GROUP BY can be resolved by reading the key in order (or do a sort on the key) and then calculate summaries until the key value changes. In this case LIMIT # will not calculate any unnecessary GROUP BY's.
As soon as MySQL has sent the first # rows to the client, it will abort the query.
LIMIT 0 will always quickly return an empty set. This is useful to check the query and to get the column types of the result columns.
The size of temporary tables uses the LIMIT # to calculate how much space is needed to resolve the query.

Mysql - Speed Of Delete Queries ?
If you want to delete all rows in the table, you should use TRUNCATE TABLE table_name. The time to delete a record is exactly proportional to the number of indexes. To delete records more quickly, you can increase the size of the index cache.

What Is The Difference Between Mysql_fetch_array And Mysql_fetch_object?
+ mysql_fetch_array — Fetch a result row as an associative ARRAY, a numeric array, or both
+ mysql_fetch_object — Fetch a result row as an OBJECT.

What Are The Different Table Present In Mysql?
+ MyISAM : This is default. Based on Indexed Sequntial Access Method. The above SQL will create a MyISA table.
+ ISAM : same
+ HEAP : Fast data access, but will loose data if there is a crash. Cannot have BLOB, TEXT & AUTO INCRIMENT fields
+ BDB : Supports Transactions using COMMIT & ROLLBACK. Slower that others.
+ InnoDB : same as BDB

What Is Primary Key?
A primary key is a single column or multiple columns defined to have unique values that can be used as row identifications.

What Is Foreign Key?
A foreign key is a single column or multiple columns defined to have values that can be mapped to a primary key in another table.

What Is Index?
An index is a single column or multiple columns defined to have values pre-sorted to speed up data retrieval speed.

What Is Join?
Join is data retrieval operation that combines rows from multiple tables under certain matching conditions to form a single row.

What Is Union?
Join is data retrieval operation that combines multiple query outputs of the same structure into a single output. By default the MySQL UNION removes all duplicate rows from the result set even if you don’t explicit using DISTINCT after the keyword UNION.
SELECT customerNumber id, contactLastname name FROM customers UNION SELECT employeeNurrber id, firstname name FROM employees

id name
103 Schmitt
112 King
114 Ferguson
119 Labrune
121 Bergulfsen



What Is Isam?
ISAM (Indexed Sequential Access Method) was developed by IBM to store and retrieve data on secondary storage systems like tapes.

What Is Innodb?
lnnoDB is a transaction safe storage engine developed by Innobase Oy (an Oracle company now).

What Is Bdb berkeleydb?
BDB (BerkeleyDB) is transaction safe storage engine originally developed at U.C. Berkeley. It is now developed by Sleepycat Software, Inc. (an Oracle company now).

What Is Csv?
CSV (Comma Separated Values) is a file format used to store database table contents, where one table row is stored as one line in the file, and each data field is separated with comma.

What Is Transaction?
A transaction is a logical unit of work requested by a user to be applied to the database objects. MySQL server introduces the transaction concept to allow users to group one or more SQL statements into a single transaction, so that the effects of all the SQL statements in a transaction can be either all committed (applied to the database) or all rolled back (undone from the database).

What Is Commit?
Commit is a way to terminate a transaction with all database changes to be saved permanently to the database server.

What Is Rollback?
Rollback is a way to terminate a transaction with all database changes not saving to the database server.

How Many Groups Of Data Types?
MySQL support 3 groups of data types as listed below:
+ String Data Types - CHAR, NCHAR, VARCHAR, NVARCHAR, BINARY, VARBINARY, TINYBLOB, TINYTEXT, BLOB, TEXT, MEDIUMBLOB, MEDIUMTEXT, LONGBLOB, LONGTEXT, ENUM, SET.
+ Numeric Data Types - BIT, TINYINT, BOOLEAN, SMALLINT, MEDIUMINT, INTEGER, BIGINT, FLOAT, DOUBLE, REAL, DECIMAL.
+ Date and Time Data Types - DATE, DATETIME, TIMESTAMP, TIME, YEAR.

What Is The Differences Between Char And Nchar?
Both CHAR and NCHAR are fixed length string data types. But they have the following differences:
+ CHARs full name is CHARACTER.
+ NCHARs full name is NATIONAL CHARACTER.
By default, CHAR uses ASCII character set. So 1 character is always stored as 1 byte.
By default, NCHAR uses Unicode character set. NCHAR data are stored in UTF8 format. So 1 character could be stored as 1 byte or upto 4 bytes.
Both CHAR and NCHAR columns are defined with fixed lengths in units of characters.

How To Escape Special Characters In Sql Statements?
There are a number of special characters that needs to be escaped (protected), if you want to include them in a character string. Here are some basic character escaping rules:
The escape character () needs to be escaped as (\).
The single quote (‘) needs to be escaped as (‘) or (“) in single-quote quoted strings.
The double quote () needs to be escaped as (“) or (““) in double-quote quoted strings.
The wild card character for a single character () needs to be escaped as (_).
The wild card character for multiple characters (%) needs to be escaped as (%).
The tab character needs to be escaped as (t).
The new line character needs to be escaped as (n).
The carriage return character needs to be escaped as (r).

How To Concatenate Two Character Strings?
If you want concatenate multiple character strings into one, you need to use the CONCAT() function. Here are some good examples:
SELECT CONCAT(’Welcome’,’ to’) FROM DUAL;
Welcome to
SELECT CONCAT(wj’,’center’,’.com’) FROM DUAL;
wisdomjobs.com

How To Enter Characters As Hex Numbers?
If you want to enter characters as HEX numbers, you can quote HEX numbers with single quotes and a prefix of (X), or just prefix HEX numbers with (Ox). A HEX number string will be automatically converted into a character string, if the expression context is a string. Here are some good examples:

SELECT X313233’ FROM DUAL;
123
SELECT 0x414243 FROM DUAL;
ABC


How To Enter Boolean Values In Sql Statements?
If you want to enter Boolean values in SQL statements, you use (TRUE), (FALSE), (true), or (false). Here are some good examples:
SELECT TRUE, true, FALSE, false FROM DUAL;

How To Convert Numeric Values To Character Strings?
You can convert numeric values to character strings by using the CAST(value AS CHAR) function as shown in the following examples:
SELECT CAST(4123.45700 AS CHAR) FROM DUAL;
4123.45700

How To Get Rid Of The Last 2 0's?
SELECT CAST(4.12345700E+3 AS CHAR) FROM DUAL;
4123.457
SELECT CAST(1/3 AS CHAR);
0.3333

How To Use In Conditions?
An IN condition is single value again a list of values. It returns TRUE, if the specified value is in the list. Otherwise, it returns FALSE. Some examples are :
SELECT 3 IN (1,2,3,4,5) FROM DUAL;
1
SELECT 3 NOT IN (1,2,3,4,5) FROM DUAL;
0
SELECT Y’ IN (‘F’,’Y’,I) FROM DUAL;
1

How To Use Like Conditions?
A LIKE condition is also called pattern patch. There are 3 main rules on using LIKE condition:
is used in the pattern to match any one character.
% is used in the pattern to match any zero or more characters.
ESCAPE clause is used to provide the escape character in the pattern.

How To Present A Past Time In Hours, Minutes And Seconds?
If you want show an article was posted “n hours n minutes and n seconds ago’, you can use the TIMEDIFF(NOWO, pastTime) function as shown in the following are:

SELECT TIMEDIFF(NOWO, ‘2006-07-01 04:09:49’) FROM DUAL;
06:42:58
SELECT TIM E_FORMAT(TI M EDI FF( NOWO, ‘2006-06-30 04:09:49’),‘%H hours, %i minutes and %s seconds ago.’) FROM DUAL;
30 hours, 45 minutes and 22 seconds ago.

How To Add A New Column To An Existing Table In Mysql?
ALTER TABLE tip ADD COLUMN author VARCHAR(40);
Query OK, 1 row affected (0.18 sec)
Records: 1 Duplicates: 0 Warnings: 0

How To Delete An Existing Column In A Table?
ALTER TABLE tip DROP COLUMN create_date;
Query OK, 1 row affected (0.48 sec)
Records: 1 Duplicates: 0 Warnings: 0

How To Rename An Existing Column In A Table?
ALTER TABLE tip CHANGE COLUMN subject title VARCHAR(60);

How To Rename An Existing Table In Mysql?
ALTER TABLE tip RENAME TO faq;

How To Create A Table Index In Mvsql?
If you have a table with a lots of rows, and you know that one of the columns will be used often as a search criteria, you can add an index for that column to improve the search performance. To add an index, you can use the “CREATE INDEX” statement as shown in the following script:

<pre>mysql> CREATE TABLE tip (id INTEGER PRIMARY KEY,
subject VARCHAR(80) NOT NULL, 
description VARCHAR(256) NOT NULL, 
create_date DATE NULL);  Query OK, 
0 rows affected (0.08 sec)</pre>
mysql> CREATE INDEX tip_subject ON tip(subject);
Query OK,
0 rows affected (0.19 sec)
Records: 0 Duplicates: 0 Warnings: 0

How To Get A List Of Indexes Of An Existing Table?
If you want to see the index you have just created for an existing table, you can use the “SHOW INDEX FROM tableName” command to get a list of all indexes in a given table.

How To Drop An Existing Index In Mysql?
If you don’t need an existing index any more, you should delete it with the “DROP INDEX indexName ON tableName” statement. Here is an example SQL script :

mysqi> DROP INDEX tip_subject ON tip;
Query OK, 0 rows affected (0.13 sec)
Records: 0 Duplicates: 0 Warnings: 0

How To Drop An Existing View In Mysql?
If you have an existing view, and you dont want it anymore, you can delete it by using the “DROP VIEW viewName” statement

How To Create A New View In Mysql?
You can create a new view based on one or more existing tables by using the
“CREATE VIEW viewName AS selectStatement” .

How To Increment Dates By 1111 Mysql?
If you have a date, and you want to increment it by 1 day, you can use the DATE_ADD(date, INTERVAL 1 DAY) function. You can also use the date interval add operation as “date + INTERVAL 1 DAY.

Explain What Is A Database?
A database is a collection of information in an organized form for faster and better access, storage and manipulation. It can also be defined as a collection of tables, schema, views and other database objects.

Explain What Is Dbms?
Database Management System is a collection of programs that enables a user to store, retrieve, update and delete information from a database.

Explain What Is Rdbms?
RDBMS stands for Relational Database Management System. RDBMS is a database management system (DBMS) that is based on the relational model. Data from relational database can be accessed using Structured Query Language (SQL)

What Are The Popular Database Management Systems In The It Industry?
Oracle, MySQL, Microsoft SQL Server, PostgreSQL, Sybase, MongoDB, DB2, and Microsoft Access etc.,

Explain What Is Sql?
SQL stands for Structured Query Language. It is an American National Standard Institute (ANSI) standard. It is a standard language for accessing and manipulating databases. Using SQL, some of the action we could do are to create databases, tables, stored procedures (SP’s), execute queries, retrieve, insert, update, delete data against a database.

Explain What Is Table In A Database?
A table is a database object used to store records in a field in the form of columns and rows that holds data.

Explain What Is A Field In A Database And Record In A Database?
A field in a Database table is a space allocated to store a particular record within a table.
A record (also called a row of data) is an ordered set of related data in a table.

What Is The Use Of Nvl Function?
NVL function is used to convert the null value to its actual value.

Explain What Is A Column In A Table?
A column is a vertical entity in a table that contains all information associated with a specific field in a table.

What Are The Different Types Of Sql Commands?
SQL commands are segregated into following types:
+ DDL – Data Definition Language
+ DML – Data Manipulation Language
+ DQL – Data Query Language
+ DCL – Data Control Language
+ TCL – Transaction Control Language

What Are The Different Ddl Commands In Sql?
DDL commands are used to define or alter the structure of the database.
+ CREATE: To create databases and database objects
+ ALTER: To alter existing database objects
+ DROP: To drop databases and databases objects
+ TRUNCATE: To remove all records from a table but not its database structure
+ RENAME: To rename database objects

What Are The Different Dml Commands In Sql?
DML commands are used for managing data present in the database.
+ SELECT: To select specific data from a database
+ INSERT: To insert new records into a table
+ UPDATE: To update existing records
+ DELETE: To delete existing records from a table

What Are The Different Dcl Commands In Sql?
DCL commands are used to create roles, grant permission and control access to the database objects.
+ GRANT: To provide user access
+ DENY: To deny permissions to users
+ REVOKE: To remove user access

What Are The Different Tcl Commands In Sql?
TCL commands are used to manage the changes made by DML statements.
+ COMMIT: To write and store the changes to the database
+ ROLLBACK: To restore the database since the last commit

Explain What Is An Index?
An index is used to speed up the performance of queries. It makes faster retrieval of data from the table. The index can be created on one column or a group of columns.

Explain What Is A View?
A view is like a subset of a table which is stored logically in a database. A view is a virtual table. It contains rows and columns similar to a real table. The fields in the view are fields from one or more real tables. Views do not contain data of their own. They are used to restrict access to the database or to hide data complexity.

Explain What Is A Subquery ?
A Subquery is a SQL query within another query. It is a subset of a Select statement whose return values are used in filtering the conditions of the main query.

What Is The Difference Between Rename And Alias?
+ ‘Rename’ is a permanent name given to a table or column
+ ‘Alias’ is a temporary name given to a table or column.

What Is A Join?
Join is a query, which retrieves related columns or rows from multiple tables.

What Are The Different Types Of Joins?
Types of Joins are as follows:
+ INNER JOIN: It is also known as SIMPLE JOIN which returns all rows from BOTH tables when it has at least one column matched
+ + Syntax: SELECT column_name(s) FROM table_name1 INNER JOIN table_name2 ON column_name 1=column_name 2;
+ LEFT JOIN (LEFT OUTER JOIN): This join returns all rows from a LEFT table and its matched rows from a RIGHT table.
+ + Syntax: SELECT column_name(s) FROM table_name1 LEFT JOIN table_name2 ON column_name 1=column_name 2;
+ RIGHT JOIN (RIGHT OUTER JOIN): This joins returns all rows from the RIGHT table and its matched rows from a LEFT table.
+ + Syntax: SELECT column_name(s) FROM table_name1 RIGHT JOIN table_name2 ON column_name1=column_name2;
+ FULL JOIN (FULL OUTER JOIN): This joins returns all when there is a match either in the RIGHT table or in the LEFT table.
+ + Syntax: SELECT column_name(s) FROM table_name1 FULL OUTER JOIN table_name2 ON column_name1=column_name2;

What Are Sql Constraints?
SQL constraints are the set of rules that enforced some restriction while inserting, deleting or updating of data in the databases.

What Are The Constraints Available In Sql?
Some constraints in SQL are : Primary Key, Foreign Key, Unique Key, SQL Not Null, Default, Check and Index constraint.

What Is A Unique Key And Primary Key And Foreign Key?
+ A UNIQUE KEY constraint is used to ensure that there are no duplication values in the field/column.
+ A PRIMARY KEY constraint uniquely identifies each record in a database table. All columns participating in a primary key constraint must not contain NULL values.
+ A FOREIGN KEY is a key used to link two tables together. A FOREIGN KEY in a table is linked with the PRIMARY KEY of another table.

What Is The Difference Between Unique And Primary Key Constraints?
There should be only one PRIMARY KEY in a table whereas there can be any number of UNIQUE Keys.
PRIMARY KEY doesn’t allow NULL values whereas Unique key allows NULL values.

What Is A Null Value?
A field with a NULL value is a field with no value. A NULL value is different from a zero value or a field that contains spaces. A field with a NULL value is one that has been left blank during record creation. Assume, there is a field in a table is optional and it is possible to insert a record without adding a value to the optional field then the field will be saved with a NULL value.

What Is Normalization?
Normalization is the process of table design to minimize the data redundancy.
There are different types of Noramalization forms in SQL:-
+ First Normal Form (1NF): It removes all duplicate columns from the table. Creates table for related data and identifies unique column values
+ First Normal Form (2NF): Follows 1NF and creates and places data subsets in an individual table and defines relationship between tables using primary key
+ Third Normal Form (3NF): Follows 2NF and removes those columns which are not related through primary key
+ Fourth Normal Form (4NF): Follows 3NF and do not define multi-valued dependencies. 4NF also known as BCNF

What Is Stored Procedure?
A Stored Procedure is a collection of SQL statements that have been created and stored in the database to perform a particular task. The stored procedure accepts input parameters and processes them and returns a single value such as a number or text value or a result set (set of rows).

What Is A Trigger?
A Trigger is a SQL procedure that initiates an action in response to an event (Insert, Delete or Update) occurs. When a new Employee is added to an Employee_Details table, new records will be created in the relevant tables such as Employee Payroll, Employee Time Sheet etc.,

List Out The Acid Properties And Explain?
Following are the four properties of ACID. These guarantees that the database transactions are processed reliably.
+ Atomicity
+ Consistency
+ Isolation
+ Durability

What Is The Difference Between Delete, Truncate And Drop Command?
The difference between the Delete, Truncate and Drop command is:
Delete command is a DML command, it is used to delete rows from a table. It can be rolled back.
Truncate is a DDL command, it is used to delete all the rows from the table and free the space containing the table. It cant be rolled back.
Drop is a DDL command, it removes the complete data along with the table structure(unlike truncate command that removes only the rows). All the tables’ rows, indexes, and privileges will also be removed.

What Is The Difference Between Having And Where Clause?
Where clause is used to fetch data from a database that specifies particular criteria whereas a Having clause is used along with ‘GROUP BY’ to fetch data that meets particular criteria specified by the Aggregate functions. Where clause cannot be used with Aggregate functions, but the Having clause can.

What Are Aggregate Functions In Sql?
SQL aggregate functions return a single value, calculated from values in a column.
Some aggregate functions in SQL are as follows:
+ AVG() : This function returns the average value
+ COUNT() : This function returns the number of rows
+ MAX() : This function returns the largest value
+ MIN() : This function returns the smallest value
+ ROUND() : This function rounds a numeric field to the number of decimals specified
+ SUM() : This function returns the sum

What Are String Functions In Sql?
SQL string functions are used primarily for string manipulation.
Some widely used SQL string functions are:
+ LEN() : It returns the length of the value in a text field
+ LOWER() : It converts character data to lower case
+ UPPER() : It converts character data to upper case
+ SUBSTRING() : It extracts characters from a text field
+ LTRIM() : It is to remove all whitespace from the beginning of the string
+ RTRIM() : It is to remove all whitespace at the end of the string
+ CONCAT() : Concatenate function combines multiple character strings together
+ REPLACE() :To update the content of a string.

Explain The Working Of Sql Privileges?
SQL GRANT and REVOKE commands are used to implement privileges in SQL multiple user environments.  The administrator of the database can grant or revoke privileges to or from users of database object like SELECT, INSERT, UPDATE, DELETE, ALL etc.
GRANT Command: This command is used provide database access to user apart from an administrator.
Syntax: GRANT privilege_name
ON object_name
TO {user_name|PUBLIC|role_name}
[WITH GRANT OPTION];
In above syntax WITH GRANT OPTIONS indicates that the user can grant the access to another user too.
REVOKE Command: This command is used provide database deny or remove access to database objects.
Syntax: REVOKE privilege_name
ON object_name
FROM {user_name|PUBLIC|role_name};

How Many Types Of Privileges Are Available In Sql?
There are two types of privileges used in SQL, such as
System Privilege: System privileges deal with an object of a particular type and specifies the right to perform one or more actions on it which include Admin allows a user to perform administrative tasks, ALTER ANY INDEX, ALTER ANY CACHE GROUP CREATE/ALTER/DELETE TABLE, CREATE/ALTER/DELETE VIEW etc.
Object Privilege: This allows to perform actions on an object or object of another user(s) viz. table, view, indexes etc. Some of the object privileges are EXECUTE, INSERT, UPDATE, DELETE, SELECT, FLUSH, LOAD, INDEX, REFERENCES etc.

What Is Sql Injection?
SQL Injection is a type of database attack technique where malicious SQL statements are inserted into an entry field of database such that once it is executed the database is opened for an attacker. This technique is usually used for attacking Data-Driven Applications to have an access to sensitive data and perform administrative tasks on databases.

What Is The Difference Between Clustered And Non-clustered Indexes?
One table can have only one clustered index but multiple nonclustered indexes.
Clustered indexes can be read rapidly rather than non-clustered indexes.
Clustered indexes store data physically in the table or view and non-clustered indexes do not store data in table as it has separate structure from data row

What Is Relationship? How Many Types Of Relationship Are There?
The relationship can be defined as the connection between more than one tables in the database.
There are 4 types of relationships:
+ One to One Relationship
+ Many to One Relationship
+ Many to Many Relationship
+ One to Many Relationship

What Is Collation?
Collation is set of rules that check how the data is sorted by comparing it. Such as Character data is stored using correct character sequence along with case sensitivity, type, and accent.

What Is Database White Box Testing And Black Box Testing?
+ Database White Box Testing involves:
+ + Database Consistency and ACID properties
+ + Database triggers and logical views
+ + Decision Coverage, Condition Coverage, and Statement Coverage
+ + Database Tables, Data Model, and Database Schema
+ + Referential integrity rules
+ Database Black Box Testing involves:
+ + Data Mapping
+ + Data stored and retrieved
+ + Use of Black Box techniques such as Equivalence Partitioning and Boundary Value Analysis (BVA)

What Are The Advantages Of Views?
Advantages of Views:
Views restrict access to the data because the view can display selective columns from the table.
Views can be used to make simple queries to retrieve the results of complicated queries. For example, views can be used to query information from multiple tables without the user knowing.

What Is Schema?
A schema is a collection of database objects of a User.

What Is The Difference Between Sql And Pl/sql?
SQL is a structured query language to create and access databases whereas PL/SQL comes with procedural concepts of programming languages.

What Is The Difference Between Sql And Mysql?
SQL is a structured query language that is used for manipulating and accessing the relational database, on the other hand, MySQL itself is a relational database that uses SQL as the standard database language.

What Is Sql Sandbox In Sql Server?
SQL Sandbox is the safe place in SQL Server Environment where untrusted scripts are executed. There are 3 types of SQL sandbox, such as
Safe Access Sandbox: Here a user can perform SQL operations such as creating stored procedures, triggers etc. but cannot have access to the memory and cannot create files.
External Access Sandbox: User can have access to files without having a right to manipulate the memory allocation.
Unsafe Access Sandbox: This contains untrusted codes where a user can have access to memory.

What Are The Steps To Take To Improve Performance Of A Poor Performing Query?
Maximum use of indexes, stored procures should be done.
Avoid excessive use of complicated joins and cursors.
Avoid using conditional operators using columns of different tables.
Make use of computed columns and rewriting the query.

What Is A Deadlock And What Is A Live Lock?
Deadlock occur in interconnection n/w when group of process are unable to act because of waiting each other to release some resource.
live lock packets continue to move through n/w, but does not advance towards destination.

What Is Blocking And How Would You Troubleshoot It?
Blocking occurs when two or more rows are locked by one SQL connection and a second connection to the SQL server requires a conflicting on lock on those rows. This results in the second connection to wait until the first lock is released.
Troubleshooting blocking:

SQL scripts can be written that constantly monitor the state of locking and blocking on SQL Server
The common blocking scenarios must be identified and resolved.
The scripts output must be checked constantly.
The SQL profilers data must be examined regularly to detect blocking.

Explain The Different Types Of Backups Available In Sql Server.
Complete database backup: This type of backup will backup all the information in the database. Used most commonly for disaster recovery and takes the longest time to backup.
Differential databse backup: The database is divided into partitions that have been modified since last complete backup. Most suitable for large databases. The most recent differential backup contains the changes from previous backups.
Transaction log backups: Backups only the changes logged in the transaction log. The transaction log has all changes logged about a database. Once the changes are accommodated on the database, the log is truncated or backed up.
File/File Group backups: used to recover individual files or file groups. Each filegroup can be individually backed up. This helps in recovery only the required file or filegroup for disaster recovery.

What Is Database Isolation In Sql Server?
Isolation in database defines how and when changes made by one transaction can be visible to other transactions. Different isolation levels are:
+ Serializable
+ Repeatable read
+ Read committed
+ Read uncommitted

What Is A Schema In Sql Server 2005? Explain How To Create A New Schema In A Database?
A schema is used to create database objects. It can be created using CREATE SCHEMA statement. The objects created can be moved between schemas. Multiple database users can share a single default schema.
CREATE SCHEMA sample;
Table creation
Create table sample.sampleinfo
{
id int primary key,
name varchar(20)
}

Explain How To Create A Scrollable Cursor With The Scroll Option.
Using the SCROLL keyword while declaring a cursor allows fetching of rows in any sequence.
Example:
DECLARE employee_curs SCROLL CURSOR FOR SELECT * FROM employee;
The active set of the cursor is stored can be accessed in any order without the need of opening and closing the cursor. The Scroll cursors can be set for select and function cursors but not insert or update statements.

Explain How To Create A Dynamic Cursor With The Dynamic Option?
When a cursor is declared as DYNAMIC, the cursor reflects all changes made to the base tables as the cursor is scrolled around.
Declare cursor_name cursor
[ STATIC | KEYSET | DYNAMIC | FAST_FORWARD ]
FOR select_statement
The dynamic option does not support ABSOLUTE FETCH.

What Are Database Files And Filegroups?
Database files are used for mapping the database over some operating system files. Data and log information are separate. SQL server database has three types of database files:
+ Primary: starting point of a database. It also points to other files in database.
+ + Extension: .mdf
+ Secondary: All data files except primary data file is a part of secondary files.
+ + Extension: .ndf
+ Log files: All log information used to recover database.
+ + Extension: .ldf

Describe In Brief Databases And Sql Server Databases Architecture.
SQL Server consists of a set of various components which fulfill data storage and data analysis needs for enterprise applications. Database architecture: All the data is stored in databases which is organized into logical components visible to the end users. It’s only the administrator who needs to actually deal with the physical storage aspect of the databases, whereas users only deal with database tables.
Every SQL Server instance has primarily 4 system database i.e. master, model, tempdb and msdb. All other databases are user created databases as per their needs and requirements.
A single SQL Server instance is capable of handling thousands of users working on multiple databases.

What Are The Steps To Improve The Performance Of A Query?
+ Number of joins and use of complex views/cursors have to be reduced.
+ The use of the stored procedures and indexes have to be maximized.
+ The optimized use of the complex conditional checks and computer columns have to be in place.
+ Tracking of performance analysis for the query helps us in identifying the right aspects to optimize.

How Would You Use The Sp_ Functions To Identify The Blocking Problems?
Blocking is the deadlock situation when two SQL connections race to obtain the control over the same set of rows in conflicting terms. This can be tracked by the status of WAIT present in the SP_LOCK procedure’s output. All the active LOCKS and the different rows that are being involved are shown in this output. The identification of the connections involved in the specific row contention lock can be identified with sp_who and sp_who2 procedures. This way the causal agents of the blocking is identifies. KILL command issued against the specific SQL connection causing the BLOCK can resolve the issue. But the permanent solution lies in the proper design of the application code to execute in concurrence across different connections.

What Are The Different Types Of Backups?
The SQL server offers 4 types of backups to suit the need of the administrator.

+ Complete backup- The complete back up is just zipping the content of the entire database in terms of the different tables and procedures etc. This back up can server as an independent entity that can be restored in different systems with just the base SQL server installed.
+ Transaction log backup: This is the mechanism of backing up the transaction logs that have been maintained in the server. This way the details of the database getting updated is obtained. This cannot be a stand-alone back up mechanism. But can save a lot of time if we already have the file system related to the DB backed up on the new deployment server.
+ Differential backup: This is a subset of the complete backup, where only the modified datasets are backed up. This can save the time when we are just trying to maintain a backup server to main server.
+ File backup: This is the quickest way to take the backup of entire database. Instead of taking in the data actually stored in DB, the files are backed up and the file system thus obtained when combined with the transaction logs of the original system will render the database that we are trying to back up.

What Are The Different Levels Of Isolation?
The isolation represents the way of separating the database from the effects of network accesses, thereby maintaining the consistency. The different levels of isolation are:
+ read committed: This level of isolation uses the shared locks and the reads to the database give the constant and consistent values.
+ read uncommitted: No locks implemented. This is the least effective isolation level.
+ repeatable read: There are locks over the rows and values but the updates are maintained as a separate phantom row which is the next set of values for the specific record. Values can change within a specific transaction of a SQL function.
+ SERIALIZABLE reads: This is the implementation of pure lock mechanism where one specific transaction is not allowed access to specific record before another one completes.

How Can You Start The Sql Server In The Single User Mode And The Minimal Configuration Mode?
The SQLServer.exe is the executable which can be called in the command prompt with the parameters -m and -f. These are the options that will start the SQL server in the user mode and minimal configuration mode respectively.

How Can You Know That Statistics Should Be Updated?
Statistics represent the uniqueness for the indexes that are being used for selecting the records. This can make the query execution pretty efficient. The tables that we are dealing with if truncated and repopulated, there is a good chance that the indexes and statistics are out of sync and this is when we have to update the statistics. There are also other situations like when the table has been modified and lot of rows have been added recently or like when a server has been updated with different version of software. These also give us the reason to use the UPDATE_STATISTICS, DBCC SHOW_STATISTICS etc to update it accordingly.

What Is Replication In Sql Server?
Replication refers to the moving or copying of the database elements from one system to another. This can be done in the SQL Server in one of the following methods:
+ Transactional.
+ Snapshot.
+ Merge replication.

Can We Initiate A External Com Object From Within Sql?
Yes we can use the stored procedure sp_OACreate to initiate the external COM object from the T-SQL.

What Is A Schema? How Is It Useful In Sql Servers?
The Schema refers to the overall structure of the database with all related information like users, access privileges, interaction information between the different tables etc. The CREATE SCHEMA is the command that can be used to create the schema in the SQL Server. This when done can be used to re deploy the same database in another system for demonstrative or test purposes. This holds intact the underlying framework over which the database has been built.

What Is A Write-ahead Log?
The write-ahead log is the logging system that just updates the buffer cache of the database for the transactions and updates the logs and only then the actual changes are incorporated in the actual database. This is the reason why it is called “write ahead”. This helps in maintaining the consistency in the database. This can also be useful in getting the actual database values even in case of failures.

What Is The Use Of Check Points In The Transaction Logs?
The check points are restoration points that indicate the specific state of the database. When there is some failure in the database that is occurring before the next check point, the database can be reverted back to the previous check point and thus the database would still be consistent.

What Is A Column With Identity?
The column with a defined identity in turn means that there is an unique value that the system assigns to the specific column. This is similar to the AUTONumber property of the Access backend.

What Are Scrollable Cursors? How Are They Created?
The scrollable cursors are the ones that can get the entire set of rows as single entity, within which all the rows present can be accessed in any order without the open/close of cursor done for every row access. The scrollable cursors are created with the keyword SCROLL added to the CREATE Cursor statements. The scrollable cursors are useful for the access of information from different rows but not for the delete/insert of new rows.

What Is Raid? How Does It Help Storage Of Databases?
The RAID stands for Redundant Array of Independent Disks. With its own RAID controllers, the RAID implements a fail-safe storage mechanism with its own backup mechanisms. There are different configurations of the RAID that all give us the ACID properties of storage along with other such facilities. This kind of storage will make the SQL Server database to be failsafe and stable. This can sometimes mean that the backup mechanisms and other such reliability measures can be taken off from the SQL Server level of operations.

How Can You Identify The Version Number Of The Sql Server Installed?
The global variable version has the build and version information for the SQL Server and the service packs.

What Is The Use Of Cascade Constraints?
cascading is used for maintaining referencial integrity rules, which says that foreign key attributes values should be either subset of primary key values or null.

What Is The Function Of A Odbc Manager ?
The ODBC Manager manages all the data sources that exists in the system.

What Are The Different Types Of Indexes Available In Sql Server?
“Clustered and Non-Clustered Indexes”. There are other types of Indexes such as Unique, XML, Spatial and Filtered Indexes.

What Is The Difference Between Clustered And Non-clustered Index?
In a clustered index, the leaf level pages are the actual data pages of the table. When a clustered index is created on a table, the data pages are arranged accordingly based on the clustered index key. There can only be one Clustered index on a table.
In a Non-Clustered index, the leaf level pages does not contain data pages instread it contains pointers to the data pages. There can multiple non-clustered indexes on a single table.

What Are The High-availability Solutions In Sql Server?
Failover Clustering, Database Mirroring, Log Shipping and Replication are the High- Availability features available in SQL Server.

What Is Denormalization And When Would You Go For It?
As the name indicates, denormalization is the reverse process of normalization. It's the controlled introduction of redundancy in to the database design. It helps improve the query performance as the number of joins could be reduced.

How Do You Implement One-to-one, One-to-many And Many-to-many Relationships While Designing Tables?
+ One-to-One relationship can be implemented as a single table and rarely as two tables with primary and foreign key relationships.
+ One-to-Many relationships are implemented by splitting the data into two tables with primary key and foreign key relationships.
+ Many-to-Many relationships are implemented using a junction table with the keys from both the tables forming the composite primary key of the junction table.

What's The Difference Between A Primary Key And A Unique Key?
Both primary key and unique enforce uniqueness of the column on which they are defined. But by default primary key creates a clustered index on the column, where are unique creates a nonclustered index by default. Another major difference is that, primary key doesn't allow NULLs, but unique key allows one NULL only.

What Are User Defined Datatypes And When You Should Go For Them?
User defined datatypes let you extend the base SQL Server datatypes by providing a descriptive name, and format to the database. Take for example, in your database, there is a column called Flight_Num which appears in many tables. In all these tables it should be varchar(8). In this case you could create a user defined datatype called Flight_num_type of varchar(8) and use it across all your tables.

What Is Bit Datatype And What's The Information That Can Be Stored Inside A Bit Column?
Bit datatype is used to store boolean information like 1 or 0 (true or false). Untill SQL Server 6.5 bit datatype could hold either a 1 or 0 and there was no support for NULL. But from SQL Server 7.0 onwards, bit datatype can represent a third state, which is NULL.

Define Candidate Key, Alternate Key, Composite Key.
A candidate key is one that can identify each row of a table uniquely. Generally a candidate key becomes the primary key of the table. If the table has more than one candidate key, one of them will become the primary key, and the rest are called alternate keys.
A key formed by combining at least two or more columns is called composite key.

What Are Defaults? Is There A Column To Which A Default Can't Be Bound?
A default is a value that will be used by a column, if no value is supplied to that column while inserting data. IDENTITY columns and timestamp columns can't have defaults bound to them.

What Is A Transaction And What Are Acid Properties?
A transaction is a logical unit of work in which, all the steps must be performed or none. ACID stands for Atomicity, Consistency, Isolation, Durability. These are the properties of a transaction.

Explain Different Isolation Levels?
An isolation level determines the degree of isolation of data between concurrent transactions. The default SQL Server isolation level is Read Committed. Here are the other isolation levels (in the ascending order of isolation): Read Uncommitted, Read Committed, Repeatable Read, Serializable. See SQL Server books online for an explanation of the isolation levels. Be sure to read about SET TRANSACTION ISOLATION LEVEL, which lets you customize the isolation level at the connection level.
CREATE INDEX myIndex ON myTable(myColumn)

What Type Of Index Will Get Created After Executing The Above Statement?
Non-clustered index. Important thing to note: By default a clustered index gets created on the primary key, unless specified otherwise.

What's The Maximum Size Of A Row?
8060 bytes.

Differences Between Active/active And Active/passive Cluster Configurations?
+ Active/Active :
+ + It is the bassically use for the default nodes, Here first node will be default and second node will be named instance. Both node will be active.
+ + Its Move group from cluster administration is possible for both side.
+ + System performance will go down, if both resources are in one node.
+ Active/Passive :
+ + Its also basically use for nodes But in this case Only one Active node with default instance. No system performance degradation will be there for this case even if we switchover to the other node. Both have same configuration.

What Is Lock Escalation?
Lock escalation is the process of converting a lot of low level locks (like row locks, page locks) into higher level locks (like table locks). Every lock is a memory structure too many locks would mean, more memory being occupied by locks. To prevent this from happening, SQL Server escalates the many fine-grain locks to fewer coarse-grain locks. Lock escalation threshold was definable in SQL Server 6.5, but from SQL Server 7.0 onwards it's dynamically managed by SQL Server.

What's The Difference Between Delete Table And Truncate Table Commands?
DELETE TABLE is a logged operation, so the deletion of each row gets logged in the transaction log, which makes it slow. TRUNCATE TABLE also deletes all the rows in a table, but it won't log the deletion of each row, instead it logs the deallocation of the data pages of the table, which makes it faster. Of course, TRUNCATE TABLE can be rolled back.

What Are Constraints? Explain Different Types Of Constraints.
Constraints enable the RDBMS enforce the integrity of the database automatically, without needing you to create triggers, rule or defaults.
Types of constraints: NOT NULL, CHECK, UNIQUE, PRIMARY KEY, FOREIGN KEY

Whar Is An Index? What Are The Types Of Indexes? How Many Clustered Indexes Can Be Created On A Table? I Create A Separate Index On Each Column Of A Table. What Are The Advantages And Disadvantages Of This Approach?
Indexes in SQL Server are similar to the indexes in books. They help SQL Server retrieve the data quicker.
Indexes are of two types. Clustered indexes and non-clustered indexes. When you craete a clustered index on a table, all the rows in the table are stored in the order of the clustered index key. So, there can be only one clustered index per table. Non-clustered indexes have their own storage separate from the table data storage. Non-clustered indexes are stored as B-tree structures (so do clustered indexes), with the leaf level nodes having the index key and it's row locater. The row located could be the RID or the Clustered index key, depending up on the absence or presence of clustered index on the table.
If you create an index on each column of a table, it improves the query performance, as the query optimizer can choose from all the existing indexes to come up with an efficient execution plan. At the same t ime, data modification operations (such as INSERT, UPDATE, DELETE) will become slow, as every time data changes in the table, all the indexes need to be updated. Another disadvantage is that, indexes need disk space, the more indexes you have, more disk space is used.

How To Restart Sql Server In Single User Mode? How To Start Sql Server In Minimal Configuration Mode?
SQL Server can be started from command line, using the SQLSERVR.EXE. This EXE has some very important parameters with which a DBA should be familiar with. -m is used for starting SQL Server in single user mode and -f is used to start the SQL Server in minimal confuguration mode.

What Are Statistics, Under What Circumstances They Go Out Of Date, How Do You Update Them?
Statistics determine the selectivity of the indexes. If an indexed column has unique values then the selectivity of that index is more, as opposed to an index with non-unique values. Query optimizer uses these indexes in determining whether to choose an index or not while executing a query.
Some situations under which you should update statistics:

If there is significant change in the key values in the index?
If a large amount of data in an indexed column has been added, changed, or removed (that is, if the distribution of key values has changed), or the table has been truncated using the TRUNCATE TABLE statement and then repopulated
Database is upgraded from a previous version
Look up SQL Server books online for the following commands: UPDATE STATISTICS, STATS_DATE, DBCC SHOW_STATISTICS, CREATE STATISTICS, DROP STATISTICS, sp_autostats, sp_createstats, sp_updatestats.

What Is Database Replicaion? What Are The Different Types Of Replication You Can Set Up In Sql Server?
Replication is the process of copying/moving data between databases on the same or different servers. SQL Server supports the following types of replication scenarios:
+ Snapshot replication
+ Transactional replication (with immediate updating subscribers, with queued updating subscribers)
+ Merge replication

What Are The Components Of Physical Database Structure Of Oracle Database?
Oracle database is comprised of three types of files. One or more datafiles, two are more redo log files, and one or more control files.

What Are The Components Of Logical Database Structure Of Oracle Database?
There are tablespaces and database's schema objects.

What Is A Tablespace?
A database is divided into Logical Storage Unit called tablespaces. A tablespace is used to group related logical structures together.

What Is System Tablespace And When Is It Created?
Every Oracle database contains a tablespace named SYSTEM, which is automatically created when the database is created. The SYSTEM tablespace always contains the data dictionary tables for the entire database.

Explain The Relationship Among Database, Tablespace And Data File.
Each databases logically divided into one or more tablespaces one or more data files are explicitly created for each tablespace.

What Is Schema?
A schema is collection of database objects of a user.

What Are Schema Objects?
Schema objects are the logical structures that directly refer to the database's data. Schema objects include tables, views, sequences, synonyms, indexes, clusters, database triggers, procedures, functions packages and database links.

Can Objects Of The Same Schema Reside In Different Tablespaces?
Yes.

Can A Tablespace Hold Objects From Different Schemes?
Yes.

What Is Oracle Table?
A table is the basic unit of data storage in an Oracle database. The tables of a database hold all of the user accessible data. Table data is stored in rows and columns.

What Is An Oracle View?
A view is a virtual table. Every view has a query attached to it. (The query is a SELECT statement that identifies the columns and rows of the table(s) the view uses.)

What Is Partial Backup ?
A Partial Backup is any operating system backup short of a full backup, taken while the database is open or shut down.

What Is Mirrored On-line Redo Log ?
A mirrored on-line redo log consists of copies of on-line redo log files physically located on separate disks, changes made to one member of the group are made to all members.

What Is Full Backup?
A full backup is an operating system backup of all data files, on-line redo log files and control file that constitute ORACLE database and the parameter.

Can A View Based On Another View ?
Yes.

Can A Tablespace Hold Objects From Different Schemes ?
Yes.

Can Objects Of The Same Schema Reside In Different Tablespaces.?
Yes.

What Is The Use Of Control File ?
When an instance of an ORACLE database is started, its control file is used to identify the database and redo log files that must be opened for database operation to proceed. It is also used in database recovery.

Do View Contain Data ?
Views do not contain or store data.

What Are The Referential Actions Supported By Foreign Key Integrity Constraint ?
UPDATE and DELETE Restrict - A referential integrity rule that disallows the update or deletion of referenced data.
DELETE Cascade - When a referenced row is deleted all associated dependent rows are deleted.

What Are The Type Of Synonyms?
There are two types of Synonyms Private and Public.

What Is A Redo Log ?
The set of Redo Log files YSDATE,UID,USER or USERENV SQL functions, or the pseudo columns LEVEL or ROWNUM.

What Is An Index Segment ?
Each Index has an Index segment that stores all of its data.

Explain The Relationship Among Database, Tablespace And Data File?
Each databases logically divided into one or more tablespaces one or more data files are explicitly created for each tablespace.

What Are The Different Type Of Segments ?
Data Segment, Index Segment, Rollback Segment and Temporary Segment.

What Are Clusters ?
Clusters are groups of one or more tables physically stores together to share common columns and are often used together.

What Is An Integrity Constrains ?
An integrity constraint is a declarative way to define a business rule for a column of a table.

What Is An Index?
An Index is an optional structure associated with a table to have direct access to rows, which can be created to increase the performance of data retrieval. Index can be created on one or more columns of a table.

What Is An Extent?
An Extent is a specific number of contiguous data blocks, obtained in a single allocation, and used to store a specific type of information.

What Is A View ?
A view is a virtual table. Every view has a Query attached to it. (The Query is a SELECT statement that identifies the columns and rows of the table(s) the view uses.)

What Is Table ?
A table is the basic unit of data storage in an ORACLE database. The tables of a database hold all of the user accessible data. Table data is stored in rows and columns.

Can A View Based On Another View?
Yes.

What Are The Advantages Of Views?
Provide an additional level of table security, by restricting access to a predetermined set of rows and columns of a table.
Hide data complexity.
Simplify commands for the user.
Present the data in a different perspective from that of the base table.
Store complex queries.

What Is An Oracle Sequence?
A sequence generates a serial list of unique numbers for numerical columns of a database's tables.

What Is A Synonym?
A synonym is an alias for a table, view, sequence or program unit.

What Are The Types Of Synonyms?
There are two types of synonyms private and public.

What Is A Private Synonym?
Only its owner can access a private synonym.

What Is A Public Synonym?
Any database user can access a public synonym.

What Are Synonyms Used For?
Mask the real name and owner of an object.
Provide public access to an object
Provide location transparency for tables, views or program units of a remote database.
Simplify the SQL statements for database users.

What Is An Oracle Index?
An index is an optional structure associated with a table to have direct access to rows, which can be created to increase the performance of data retrieval. Index can be created on one or more columns of a table.

How Are The Index Updates?
Indexes are automatically maintained and used by Oracle. Changes to table data are automatically incorporated into all relevant indexes.

What Is Rollback Segment ?
Database contains one or more Rollback Segments to temporarily store "undo" information.

What Are The Characteristics Of Data Files ?
A data file can be associated with only one database. Once created a data file can't change size. One or more data files form a logical unit of database storage called a tablespace.

How To Define Data Block Size ?
A data block size is specified for each ORACLE database when the database is created. A database users and allocated free database space in ORACLE datablocks. Block size is specified in INIT.ORA file and can’t be changed latter.

What Does A Control File Contain ?
A Control file records the physical structure of the database. It contains the following information.
Database Name
Names and locations of a database's files and redolog files.
Time stamp of database creation.

What Is Difference Between Unique Constraint And Primary Key Constraint ?
A column defined as UNIQUE can contain Nulls while a column defined as PRIMARY KEY can't contain Nulls.

What Is Index Cluster ?
A Cluster with an index on the Cluster Key.

When Does A Transaction End ?
When it is committed or Rollbacked.

What Is The Effect Of Setting The Value "choose" For Optimizer_goal, Parameter Of The Alter Session Command ?
The Optimizer chooses Cost_based approach and optimizes with the goal of best throughput if statistics for atleast one of the tables accessed by the SQL statement exist in the data dictionary. Otherwise the OPTIMIZER chooses RULE_based approach.

What Is The Effect Of Setting The Value "all_rows" For Optimizer_goal Parameter Of The Alter Session Command ? What Are The Factors That Affect Optimizer In Choosing An Optimization Approach ?
The OPTIMIZER_MODE initialization parameter Statistics in the Data Dictionary. The OPTIMIZER_GOAL parameter of the ALTER SESSION command hints in the statement.

How Does One Create A New Database?
One can create and modify Oracle databases using the Oracle "dbca" (Database Configuration Assistant) utility. The dbca utility is located in the $ORACLE_HOME/bin directory. The Oracle Universal Installer (oui) normally starts it after installing the database server software. One can also create databases manually using scripts. This option, however, is falling out of fashion, as it is quite involved and error prone. Look at this example for creating and Oracle 9i database:
CONNECT SYS AS SYSDBA
ALTER SYSTEM SET DB_CREATE_FILE_DEST='/u01/oradata/';
ALTER SYSTEM SET DB_CREATE_ONLINE_LOG_DEST_1='/u02/oradata/';
ALTER SYSTEM SET DB_CREATE_ONLINE_LOG_DEST_2='/u03/oradata/';
CREATE DATABASE;

What Database Block Size Should I Use?
Oracle recommends that your database block size match, or be multiples of your operating system block size. One can use smaller block sizes, but the performance cost is significant. Your choice should depend on the type of application you are running. If you have many small transactions as with OLTP, use a smaller block size. With fewer but larger transactions, as with a DSS application, use a larger block size. If you are using a volume manager, consider your "operating system block size" to be 8K. This is because volume manager products use 8K blocks (and this is not configurable).

What Are The Different Approaches Used By Optimizer In Choosing An Execution Plan ?
Rule-based and Cost-based.

What Does Rollback Do?
ROLLBACK retracts any of the changes resulting from the SQL statements in the transaction.

What Is Cost-based Approach To Optimization ?
Considering available access paths and determining the most efficient execution plan based on statistics in the data dictionary for the tables accessed by the statement and their associated clusters and indexes.

What Does Commit Do?
COMMIT makes permanent changes resulting from all SQL statements in the transaction. The changes made by the SQL statements of a transaction become visible to other user sessions transactions that start only after transaction is committed.

Define Transaction?
A Transaction is a logical unit of work that comprises one or more SQL statements executed by a single user.

What Is Read-only Transaction?
A Read-Only transaction ensures that the results of each query executed in the transaction are consistent with respect to the same point in time.

What Is A Deadlock?
Two processes wating to update the rows of a table which are locked by the other process then deadlock arises. In a database environment this will often happen because of not issuing proper row lock commands. Poor design of front-end application may cause this situation and the performance of server will reduce drastically.
These locks will be released automatically when a commit/rollback operation performed or any one of this processes being killed externally.

What Is A Schema?
The set of objects owned by user account is called the schema.

What Is A Cluster Key?
The related columns of the tables are called the cluster key. The cluster key is indexed using a cluster index and its value is stored only once for multiple tables in the cluster.

What Is Parallel Server?
Multiple instances accessing the same database (Only In Multi-CPU environments).

What Is Cluster?
Group of tables physically stored together because they share common columns and are often used together is called Cluster.

What Is An Index ? How It Is Implemented In Oracle Database?
An index is a database structure used by the server to have direct access of a row in a table. An index is automatically created when a unique of primary key constraint clause is specified in create table comman (Ver 7.0)

What Is A Database Instance ? Explain
A database instance (Server) is a set of memory structure and background processes that access a set of database files.The process can be shared by all users. The memory structure that are used to store most queried data from database. This helps up to improve database performance by decreasing the amount of I/O performed against data file.

What Is The Use Of Analyze Command?
To perform one of these function on an index,table, or cluster:
+ To collect statistics about object used by the optimizer and store them in the data dictionary.
+ To delete statistics about the object used by object from the data dictionary.
+ To validate the structure of the object.
+ To identify migrated and chained rows of the table or cluster.

What Is Default Tablespace?
The Tablespace to contain schema objects created without specifying a tablespace name.

What Are The System Resources That Can Be Controlled Through Profile?
The number of concurrent sessions the user can establish the CPU processing time available to the user's session.
The CPU processing time available to a single call to ORACLE made by a SQL statement.
The amount of logical I/O available to the user's session.
The amout of logical I/O available to a single call to ORACLE made by a SQL statement.
The allowed amount of idle time for the user's session.
The allowed amount of connect time for the user's session.

What Is Tablespace Quota?
The collective amount of disk space available to the objects in a schema on a particular tablespace.

What Are The Different Levels Of Auditing ?
Statement Auditing, Privilege Auditing and Object Auditing.

What Is Statement Auditing ?
Statement auditing is the auditing of the powerful system privileges without regard to specifically named objects.

What Are The Database Administrators Utilities Avaliable ?
+ SQL * DBA - This allows DBA to monitor and control an ORACLE database.
+ SQL * Loader - It loads data from standard operating system files (Flat files) into ORACLE database tables. Export (EXP) and Import (imp) utilities allow you to move existing data in ORACLE format to and from ORACLE database.

How Can You Enable Automatic Archiving ?
Shut the database
Backup the database
Modify/Include LOG_ARCHIVE_START_TRUE in init.ora file.
Start up the database.

What Are Roles? How Can We Implement Roles ?
Roles are the easiest way to grant and manage common privileges needed by different groups of database users. Creating roles and assigning provides to roles. Assign each role to group of users. This will simplify the job of assigning privileges to individual users.

What Are Roles ?
Roles are named groups of related privileges that are granted to users or other roles.

What Are The Uses Of Roles ?
+ REDUCED GRANTING OF PRIVILEGES - Rather than explicitly granting the same set of privileges to many users a database administrator can grant the privileges for a group of related user's granted to a role and then grant only the role to each member of the group.
+ DYNAMIC PRIVILEGE MANAGEMENT - When the privileges of a group must change, only the privileges of the role need to be modified. The security domains of all users granted the group's role automatically reflect the changes made to the role.
+ SELECTIVE AVAILABILITY OF PRIVILEGES - The roles granted to a user can be selectively enable (available for use) or disabled (not available for use). This allows specific control of a user's privileges in any given situation.
+ APPLICATION AWARENESS - A database application can be designed to automatically enable and disable selective roles when a user attempts to use the application.

What Is Privilege Auditing?
Privilege auditing is the auditing of the use of powerful system privileges without regard to specifically named objects.

What Is Object Auditing?
Object auditing is the auditing of accesses to specific schema objects without regard to user.

What Is Auditing?
Monitoring of user access to aid in the investigation of database use.

Where Are My Tempfiles?
Tempfiles, unlike normal datafiles, are not listed in v$datafile or dba_data_files. Instead query v$tempfile or dba_temp_files:
SELECT * FROM v$tempfile;
SELECT * FROM dba_temp_files;

How Do I Find Used/free Space In A Temporary Tablespace?
Unlike normal tablespaces, true temporary tablespace information is not listed in DBA_FREE_SPACE. Instead use the V$TEMP_SPACE_HEADER view:
SELECT tablespace_name, SUM (bytes used), SUM (bytes free)
FROM V$temp_space_header
GROUP BY tablespace_name;

What Is A Profile?
Each database user is assigned a Profile that specifies limitations on various system resources available to the user.

How Will You Enforce Security Using Stored Procedures?
Don't grant user access directly to tables within the application. Instead grant the ability to access the procedures that access the tables. When procedure executed it will execute the privilege of procedures owner. Users cannot access tables except via the procedure.

How Does One Get The View Definition Of Fixed Views/tables?
Query v$fixed_view_definition.
Example: SELECT * FROM v$fixed_view_definition WHERE view_name='V$SESSION';

What Are The Dictionary Tables Used To Monitor A Database Spaces ?
+ DBA_FREE_SPACE
+ DBA_SEGMENTS
+ DBA_DATA_FILES.

What Is User Account In Oracle Database?
A user account is not a physical structure in Database but it is having important relationship to the objects in the database and will be having certain privileges.

What Is Dynamic Data Replication?
Updating or Inserting records in remote database through database triggers. It may fail if remote database is having any problem.

What Is Two-phase Commit ?
Two-phase commit is mechanism that guarantees a distributed transaction either commits on all involved nodes or rolls back on all involved nodes to maintain data consistency across the global distributed database. It has two phase, a Prepare Phase and a Commit Phase.

How Can You Enforce Referential Integrity In Snapshots ?
Time the references to occur when master tables are not in use. Peform the reference manually immediately locking the master tables. We can join tables in snapshots by creating a complex snapshots that will be based on the master tables.

What Is A Sql * Net?
SQL *NET is ORACLE's mechanism for interfacing with the communication protocols used by the networks that facilitate distributed processing and distributed databases. It is used in Clint-Server and Server-Server communications.

What Is A Snapshot ?
Snapshots are read-only copies of a master table located on a remote node which is periodically refreshed to reflect changes made to the master table.

What Is The Mechanism Provided By Oracle For Table Replication ?
Snapshots and SNAPSHOT LOGs.

What Is Snapshot?
Snapshot is an object used to dynamically replicate data between distribute database at specified time intervals. In version 7.0 they are read only.

What Are The Various Type Of Snapshots?
Simple and Complex.

Describe Two Phases Of Two-phase Commit ?
+ Prepare phase - The global coordinator (initiating node) ask a participants to prepare (to promise to commit or rollback the transaction, even if there is a failure.
+ Commit Phase - If all participants respond to the coordinator that they are prepared, the coordinator asks all nodes to commit the transaction, if all participants cannot prepare, the coordinator asks all nodes to roll back the transaction.

What Is Snapshot Log ?
It is a table that maintains a record of modifications to the master table in a snapshot. It is stored in the same database as master table and is only available for simple snapshots. It should be created before creating snapshots.

What Are The Benefits Of Distributed Options In Databases?
Database on other servers can be updated and those transactions can be grouped together with others in a logical unit.
Database uses a two phase commit.

What Are The Options Available To Refresh Snapshots ?
+ COMPLETE - Tables are completely regenerated using the snapshots query and the master tables every time the snapshot referenced.
+ FAST - If simple snapshot used then a snapshot log can be used to send the changes to the snapshot tables.
+ FORCE - Default value. If possible it performs a FAST refresh; Otherwise it will perform a complete refresh.

What Is A Snapshot Log ?
A snapshot log is a table in the master database that is associated with the master table. ORACLE uses a snapshot log to track the rows that have been updated in the master table. Snapshot logs are used in updating the snapshots based on the master table.

What Is Distributed Database ?
A distributed database is a network of databases managed by multiple database servers that appears to a user as single logical database. The data of all databases in the distributed database can be simultaneously accessed and modified.

How Can We Reduce The Network Traffic?
+ Replication of data in distributed environment.
+ Using snapshots to replicate data.
+ Using remote procedure calls.

Differentiate Simple And Complex, Snapshots ?
+ A simple snapshot is based on a query that does not contains GROUP BY clauses, CONNECT BY clauses, JOINs, sub-query or snashot of operations.
+ A complex snapshots contain atleast any one of the above.

What Are The Built-ins Used For Sending Parameters To Forms?
You can pass parameter values to a form when an application executes the call_form, New_form, Open_form or Run_product.

Can You Have More Than One Content Canvas View Attached With A Window?
Yes. Each window you create must have atleast one content canvas view assigned to it. You can also create a window that has manipulated content canvas view. At run time only one of the content canvas views assign to a window is displayed at a time.

Is The After Report Trigger Fired If The Report Execution Fails?
Yes.

Does A Before Form Trigger Fire When The Parameter Form Is Suppressed?
Yes.

What Is Sga?
The System Global Area in an Oracle database is the area in memory to facilitate the transfer of information between users. It holds the most recently requested structural information between users. It holds the most recently requested structural information about the database. The structure is database buffers, dictionary cache, redo log buffer and shared pool area.

What Is A Shared Pool?
The data dictionary cache is stored in an area in SGA called the shared pool. This will allow sharing of parsed SQL statements among concurrent users.

What Is Mean By Program Global Area (pga)?
It is area in memory that is used by a single Oracle user process.

What Is A Data Segment?
Data segment are the physical areas within a database block in which the data associated with tables and clusters are stored.

What Are The Factors Causing The Reparsing Of Sql Statements In Sga?
Due to insufficient shared pool size.
Monitor the ratio of the reloads takes place while executing SQL statements. If the ratio is greater than 1 then increase the SHARED_POOL_SIZE.

Do A View Contain Data?
Views do not contain or store data.

If A Parameter Is Used In A Query Without Being Previously Defined, What Difference Exist Between Report 2.0 And 2.5 When The Query Is Applied?
While both reports 2.0 and 2.5 create the parameter, report 2.5 gives a message that a bind parameter has been created.

What Is Trigger Associated With The Timer?
When-timer-expired.

What Are The Triggers Associated With Image Items?
When-image-activated fires, when the operators double clicks on an image item, when-image-pressed fires, when an operator clicks or double clicks on an image item.

What Are The Different Windows Events Activated At Runtimes?
+ When_window_activated
+ When_window_closed
+ When_window_deactivated
+ When_window_resized

Within this triggers, you can examine the built in system variable system. event_window to determine the name of the window for which the trigger fired.

When Do You Use Data Parameter Type?
When the value of a data parameter being passed to a called product is always the name of the record group defined in the current form. Data parameters are used to pass data to produts invoked with the run_product built-in subprogram.

What Is Difference Between Open_form And Call_form?
when one form invokes another form by executing open_form the first form remains displayed, and operators can navigate between the forms as desired. when one form invokes another form by executing call_form, the called form is modal with respect to the calling form. That is, any windows that belong to the calling form are disabled, and operators cannot navigate to them until they first exit the called form.

What Is New_form Built-in?
When one form invokes another form by executing new_form oracle form exits the first form and releases its memory before loading the new form calling new form completely replace the first with the second. If there are changes pending in the first form, the operator will be prompted to save them before the new form is loaded.

What Is The Diff. When Flex Mode Is Mode On And When It Is Off?
When flex mode is on, reports automatically resizes the parent when the child is resized.

What Is The Diff. When Confine Mode Is On And When It Is Off?
When confine mode is on, an object cannot be moved outside its parent in the layout.

What Are Visual Attributes?
Visual attributes are the font, color, pattern proprieties that you set for form and menu objects that appear in your application interface.

What Are The Two Types Of Views Available In The Object Navigator(specific To Report 2.5)?
View by structure and view by type .

What Are The Vbx Controls?
Vbx control provide a simple method of building and enhancing user interfaces. The controls can use to obtain user inputs and display program outputs.vbx control where originally develop as extensions for the ms visual basic environments and include such items as sliders, rides and knobs.

What Is The Use Of Transactional Triggers?
Using transactional triggers we can control or modify the default functionality of the oracle forms.

How Do You Create A New Session While Open A New Form?
Using open_form built-in setting the session option Ex. Open_form('Stocks ',active,session). when invoke the mulitiple forms with open form and call_form in the same application, state whether the following are true/False

What Are The Ways To Monitor The Performance Of The Report?
Use reports profile executable statement. Use SQL trace facility.

An Open Form Can Not Be Execute The Call_form Procedure If You Chain Of Called Forms Has Been Initiated By Another Open Form?
True.

Explain About Horizontal, Vertical Tool Bar Canvas Views?
Tool bar canvas views are used to create tool bars for individual windows. Horizontal tool bars are display at the top of a window, just under its menu bar. Vertical Tool bars are displayed along the left side of a window

What Is The Purpose Of The Product Order Option In The Column Property Sheet?
To specify the order of individual group evaluation in a cross products.

What Is The Use Of Image_zoom Built-in?
To manipulate images in image items.

What Is A Timer?
Timer is an "internal time clock" that you can programmatically create to perform an action each time the times.

What Are The Two Phases Of Block Coordination?
There are two phases of block coordination: the clear phase and the population phase. During, the clear phase, Oracle Forms navigates internally to the detail block and flushes the obsolete detail records. During the population phase, Oracle Forms issues a SELECT statement to repopulate the detail block with detail records associated with the new master record. These operations are accomplished through the execution of triggers.

What Are Most Common Types Of Complex Master-detail Relationships?
There are three most common types of complex master-detail relationships:
+ master with dependent details
+ master with independent details
+ detail with two masters
 
What Is A Text List?
The text list style list item appears as a rectangular box which displays the fixed number of values. When the text list contains values that can not be displayed, a vertical scroll bar appears, allowing the operator to view and select undisplayed values.

What Is Term?
The term is terminal definition file that describes the terminal form which you are using r20run.

What Is Use Of Term?
The term file which key is correspond to which oracle report functions.

What Is Pop List?
The pop list style list item appears initially as a single field (similar to a text item field). When the operator selects the list icon, a list of available choices appears.

What Is The Maximum No. Of Chars The Parameter Can Store?
The maximum no. of chars the parameter can store is only valid for char parameters, which can be upto 64K. No parameters default to 23Bytes and Date parameter default to 7Bytes.

What Are The Default Extensions Of The Files Created By Library Module?
The default file extensions indicate the library module type and storage format .pll - pl/sql library module binary.

How Do You Display Console On A Window ?
The console includes the status line and message line, and is displayed at the bottom of the window to which it is assigned.To specify that the console should be displayed, set the console window form property to the name of any window in the form. To include the console, set console window to Null.

What Are The Coordination Properties In A Master-detail Relationship?
The coordination properties are
+ Deferred
+ Auto-Query
These Properties determine when the population phase of block coordination should occur.

What Are The Different Parameter Types?
+ Text Parameters
+ Data Parameters

What Are The Types Of Calculated Columns Available?
Summary, Formula, Placeholder column.

Explain About Stacked Canvas Views?
Stacked canvas view is displayed in a window on top of, or "stacked" on the content canvas view assigned to that same window. Stacked canvas views obscure some part of the underlying content canvas view, and or often shown and hidden programmatically.

What Is The Difference Between Show_editor And Edit_textitem?
Show editor is the generic built-in which accepts any editor name and takes some input string and returns modified output string. Whereas the edit_textitem built-in needs the input focus to be in the text item before the built-in is executed.

What Are The Different File Extensions That Are Created By Oracle Reports?
Rep file and Rdf file.

What Is The Basic Data Structure That Is Required For Creating An Lov?
Record Group.

What Is The Maximum Allowed Length Of Record Group Column?
Record group column names cannot exceed 30 characters.

Which Parameter Can Be Used To Set Read Level Consistency Across Multiple Queries?
Read only.

What Are The Different Types Of Record Groups?
+ Query Record Groups
+ NonQuery Record Groups
+ State Record Groups

From Which Designation Is It Preferred To Send The Output To The Printed?
Previewer.

What Is Difference Between Post Database Commit And Post-form Commit?
Post-form commit fires once during the post and commit transactions process, after the database commit occurs. The post-form-commit trigger fires after inserts, updates and deletes have been posted to the database but before the transactions have been finalized in the issuing the command. The post-database-commit trigger fires after oracle forms issues the commit to finalized transactions.

With Which Function Of Summary Item Is The Compute At Options Required?
percentage of total functions.

What Are Parameters?
Parameters provide a simple mechanism for defining and setting the values of inputs that are required by a form at startup. Form parameters are variables of type char,number,date that you define at design time.

What Are The Three Types Of User Exits Available ?
Oracle Precompiler exits, Oracle call interface, NonOracle user exits.

How Many Windows In A Form Can Have Console?
Only one window in a form can display the console, and you cannot change the console assignment at runtime.

Is It Possible To Modify An External Query In A Report Which Contains It?
No.

Does A Grouping Done For Objects In The Layout Editor Affect The Grouping Done In The Data Model Editor?
No.

If A Break Order Is Set On A Column Would It Affect Columns Which Are Under The Column?
No.

Do User Parameters Appear In The Data Modal Editor In 2.5?
No.

Can You Pass Data Parameters To Forms?
No.

Is It Possible To Link Two Groups Inside A Cross Products After The Cross Products Group Has Been Created?
No.

What Are The Different Modals Of Windows?
+ Modalless windows
+ Modal windows

What Are Modal Windows?
Modal windows are usually used as dialogs, and have restricted functionality compared to modelless windows. On some platforms for example operators cannot resize, scroll or iconify a modal window.

What Is The Advantage Of The Library?
Libraries provide a convenient means of storing client-side program units and sharing them among multiple applications. Once you create a library, you can attach it to any other form, menu, or library modules. When you can call library program units from triggers menu items commands and user named routine, you write in the modules to which you have attach the library. When a library attaches another library, program units in the first library can reference program units in the attached library. Library support dynamic loading-that is library program units are loaded into an application only when needed. This can significantly reduce the run-time memory requirements of applications.

What Is Lexical Reference? How Can It Be Created?
Lexical reference is place_holder for text that can be embedded in a sql statements. A lexical reference can be created using & before the column or parameter name.

What Is System.coordination_operation?
It represents the coordination causing event that occur on the master block in master-detail relation.

What Is Synchronize?
It is a terminal screen with the internal state of the form. It updates the screen display to reflect the information that oracle forms has in its internal representation of the screen.

What Use Of Command Line Parameter Cmd File?
It is a command line argument that allows you to specify a file that contain a set of arguments for r20run.

What Is A Text_io Package?
It allows you to read and write information to a file in the file system.

What Is Forms_ddl?
Issues dynamic Sql statements at run time, including server side pl/SQl and DDL


What Are The Built-ins Used For Processing Rows?
+ Get_group_row_count(function)
+ Get_group_selection_count(function)
+ Get_group_selection(function)
+ Reset_group_selection(procedure)
+ Set_group_selection(procedure)
+ Unset_group_selection(procedure)

What Are The Built-ins Used For Getting Cell Values?
+ GET_GROUP_CHAR_CELL (function)
+ GET_GROUPCELL(function)
+ GET_GROUP_NUMBET_CELL(function)

At least How Many Set Of Data Must A Data Model Have Before A Data Model Can Be Based On It?
Four.

To Execute Row From Being Displayed That Still Use Column In The Row Which Property Can Be Used?
Format trigger.

What Is The Remove On Exit Property?
For a modelless window, it determines whether oracle forms hides the window automatically when the operators navigates to an item in the another window.

What Is A Difference Between Pre-select And Pre-query?
Fires during the execute query and count query processing after oracle forms constructs the select statement to be issued, but before the statement is actually issued. The pre-query trigger fires just before oracle forms issues the select statement to the database after the operator as define the example records by entering the query criteria in enter query mode.Pre-query trigger fires before pre-select trigger.

What Are The Built-ins Used For Finding Object Id Function?
+ FIND_GROUP(function)
+ FIND_COLUMN(function)

Any Attempt To Navigate Programmatically To Disabled Form In A Call_form Stack Is Allowed?
False

How Can A Break Order Be Created On A Column In An Existing Group? What Are The Various Sub Events A Mouse Double Click Event Involves?
By dragging the column outside the group.

What Is The Use Of Place Holder Column? What Are The Various Sub Events A Mouse Double Click Event Involves?
A placeholder column is used to hold calculated values at a specified place rather than allowing is to appear in the actual row where it has to appear.

What Are The Built-ins Used For Creating And Deleting Groups?
+ CREATE-GROUP (function)
+ CREATE_GROUP_FROM_QUERY(function)
+ DELETE_GROUP(procedure)

What Are The Different Types Of Delete Details We Can Establish In Master-details?
+ Cascade
+ Isolate
+ Non-isolate



Where Is The External Query Executed At The Client Or The Server?
At the server.

Where Is A Procedure Return In An External Pl/sql Library Executed At The Client Or At The Server?
At the client.

What Is Coordination Event?
Any event that makes a different record in the master block the current record is a coordination causing event.

What Is The Difference Between Ole Server & Ole Container?
An Ole server application creates ole Objects that are embedded or linked in ole Containers ex. Ole servers are ms_word & ms_excel. OLE containers provide a place to store, display and manipulate objects that are created by ole server applications. Ex. oracle forms is an example of an ole Container.

What Is An Object Group?
An object group is a container for a group of objects; you define an object group when you want to package related objects, so that you copy or reference them in other modules.

What Is The Difference Between The Conventional And Direct Path Loader?
The conventional path loader essentially loads the data by using standard INSERT statements. The direct path loader (DIRECT=TRUE) bypasses much of the logic involved with that, and loads directly into the Oracle data files.

How Does One Load Multi-line Records?
One can create one logical record from multiple physical records using one of the following two clauses:
CONCATENATE: - use when SQL*Loader should combine the same number of physical records together to form one logical record.
CONTINUEIF - use if a condition indicates that multiple records should be treated as one. Eg. by having a '#' character in column 1.

[Table of Contents](#SQL)

Why is Where Clause faster than Group Filter or Format Trigger?
Because, in a where clause the condition is applied during data retrieval then after retrieving the data.

[Table of Contents](#SQL)

Difference between Substr and Instr?
INSTR (String1,String2(n,(m)),INSTR returns the position of the mth occurrence of the string 2 instring1. The search begins from nth position of string1.SUBSTR (String1 n,m)SUBSTR returns a character string of size m in string1, starting from nth position of string1.

[Table of Contents](#SQL)

What is Rman?
Recovery Manager is a tool that manages the process of creating backups and also manages the process of restoring and recovering from them.

[Table of Contents](#SQL)

What are Two Parts of procedure?
Procedure Specification and Procedure Body.

[Table of Contents](#SQL)

What are the DataTypes available in Plsql?
Some scalar data types such as NUMBER, VARCHAR2, DATE, CHAR, LONG, BOOLEAN. Some composite data types such as RECORD & TABLE.

[Table of Contents](#SQL)

What is Overloading of Procedures ?
The Same procedure name is repeated with parameters of different datatypes and parameters in different positions, varying number of parameters is called overloading of procedures. e.g. DBMS_OUTPUT put_line

[Table of Contents](#SQL)

What is Master Detail Relationship?
A master detail relationship is an association between two base table blocks- a master block and a detail block. The relationship between the blocks reflects a primary key to foreign key relationship between the tables on which the blocks are based.

[Table of Contents](#SQL)

How many Number of Columns A Record group can have?
A record group can have an unlimited number of columns of type CHAR, LONG, NUMBER, or DATE provided that the total number of column does not exceed 64K.

[Table of Contents](#SQL)

