Write SQL query to get the second highest salary among all Employees?
Given a Employee Table with two columns
ID, Salary 10, 2000
11, 5000
12, 3000

Answer: There are multiple ways to get the second highest salary among all Employees.
Option 1: Use Subquery
SELECT MAX(Salary) FROM Employee WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employee );
In this approach, we are getting the maximum salary in a subquery and then excluding this from the rest of the resultset.
Option 2: Use Not equals
select MAX(Salary) from Employee WHERE Salary <> (select MAX(Salary) from Employee )
This is same as option 1 but we are using <> instead of NOT IN.


How can we retrieve alternate records from a table in Oracle?
We can use rownum and MOD function to retrieve the alternate records from a table.
To get Even number records:
SELECT * FROM (SELECT rownum, ID, Name FROM Employee) WHERE MOD(rownum,2)=0
To get Odd number records: SELECT * FROM (SELECT rownum, ID, Name FROM Employee)
WHERE MOD(rownum,2)=1

Write a SQL Query to find Max salary and Department name from each department.
Given a Employee table with three columns
ID, Salary, DeptID
10, 1000, 2
20, 5000, 3
30, 3000, 2

Department table with two columns: ID, DeptName
1, Marketing
2, IT
3, Finance

Answer:
This is a trick question. There can be some department without any employee. So we have to ask interviewer if they expect the name of such Department also in result.
If yes then we have to join Department table with Employee table by using foreign key DeptID. We have to use LEFT OUTER JOIN to print all the departments.
Query would be like as follows:
SELECT d.DeptName, MAX(e.Salary) FROM Department d LEFT OUTER JOIN Employee e ON e.DeptId = d.ID GROUP BY DeptName

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
Answer: We can use MINUS operator in this case for Oracle and EXCEPT for SQL Server.
Query will be as follows:
SELECT * FROM Table_A MINUS SELECT * FROM Table_B

What is the result of following query?
SELECT CASE WHEN null = null THEN ‘True’ ELSE ‘False’ END AS Result;
Answer: In SQL null can not be compared with itself. There fore null = null is not true. We can compare null with a non-null value to check whether a value is not null.
Therefore the result of above query is False.
The correct way to check for null is to use IS NULL clause.
Following query will give result True. SELECT CASE WHEN null IS NULL THEN ‘True’ ELSE ‘False’ END AS Result;

Write SQL Query to find employees that have same name and email.
Employee table:
ID	NAME	EMAIL
10	John	jbaldwin
20	George	gadams
30	John	jsmith

Answer: This is a simple question with one trick. The trick here is to use Group by on two columns Name and Email.
Query would be as follows: SELECT name, email, COUNT(*) FROM Employee GROUP BY name, email HAVING COUNT(*) > 1

Write a SQL Query to find Max salary from each department.
Given a Employee table with three columns
ID, Salary, DeptID 10, 1000, 2
20, 5000, 3
30, 3000, 2
Answer:
We can first use group by DeptID on Employee table and then get the Max salary from each Dept group.

SELECT	DeptID, MAX(salary) FROM Employee GROUP BY DeptID

Write SQL query to get the nth highest salary among all Employees.
Given a Employee Table with two columns
ID, Salary 10, 2000
11, 5000
12, 3000
Answer:
Option 1: Use Subquery We can use following sub query approach for this:
SELECT * FROM Employee emp1 WHERE (N-1) = ( SELECT COUNT(DISTINCT(emp2.salary)) FROM Employee emp2 WHERE emp2.salary > emp1.salary)
Option 2: Using Rownum in Oracle

SELECT * FROM (SELECT emp.*,row_number() OVER (ORDER BY salary DESC) rnum FROM Employee emp) WHERE rnum = n;
How can you find 10 employees with Odd number as Employee ID?
Answer:
In Oracle we can use Top to limit the number of records. We can also use Rownum < 11 to get the only 10 or less number of records.To find the Odd number Employee ID, we can use % function.
Sample Query with TOP:
SELECT TOP 10 ID FROM Employee WHERE ID % 2 = 1;
Sample Query with ROWNUM:
SELECT ID FROM Employee WHERE ID % 2 = 1 AND ROWNUM < 11;

Write a SQL Query to get the names of employees whose date of birth is between 01/01/1990 to 31/12/2000.
This SQL query appears a bit tricky. We can use BETWEEN clause to get all the employees whose date of birth lies between two given dates.
Query will be as follows:
SELECT EmpName FROM Employees WHERE birth_date BETWEEN ‘01/01/1990’ AND ‘31/12/2000’
Remember BETWEEN is always inclusive of both the dates.

Write a SQL Query to get the Quarter from date.
Answer: We can use to_char function with ‘Q’ option for quarter to get quarter from a date.
Use TO_CHAR with option ‘Q’ for Quarter
SELECT TO_CHAR(TO_DATE('3/31/2016', 'MM/DD/YYYY'), 'Q') AS quarter FROM DUAL

Write Query to find employees with duplicate email.
Employee table:
ID	NAME	EMAIL
10	John	jsmith
20	George	gadams
30	Jane	jsmith
Answer: We can use Group by clause on the column in which we want to find duplicate values.
Query would be as follows:
SELECT name, COUNT(email) FROM Employee GROUP BY email HAVING ( COUNT(email) > 1 )

Write a Query to find all Employee whose name contains the word "Rich", regardless of case.
E.g. Rich, RICH, rich.
Answer:
We can use UPPER function for comparing the both sides with uppercase.
SELECT * FROM Employees WHERE UPPER(emp_name) like '%RICH%'

Is it safe to use ROWID to locate a record in Oracle SQL queries?
ROWID is the physical location of a row. We can do very fast lookup based on ROWID. In a transaction where we first search a few rows and then update them one by one, we can use ROWID. But ROWID of a record can change over time. If we rebuild a table a record can get a new ROWID. If a record is deleted, its ROWID can be given to another record. So it is not recommended to store and use ROWID in long term. It should be used in same transactions.

What is a Pseudocolumn?
A Pseudocolumn is like a table column, but it is not stored in the same table. We can select from a Pseudocolumn, but we can not insert, update or delete on a Pseudocolumn. A Pseudocolumn is like a function with no arguments. Two most popular Pseudocolumns in Oracle are ROWID and ROWNUM. NEXTVAL and CURRVAL are also pseudo columns.

What are the reasons for de- normalizing the data?
We de-normalize data when we need better performance. Sometimes there are many joins in a query due to highly normalized data. In that case, for faster data retrieval it becomes essential to de-normalize data.

What is the feature in SQL for writing If/Else statements?
In SQL, we can use CASE statements to write If/Else statements. We can also use DECODE function in Oracle SQL for writing simple If/Else logic.

What is the difference between DELETE and TRUNCATE in SQL?
Main differences between DELETE and TRUNCATE commands are:
DML vs. DDL: DELETE is a Data Manipulation Language (DML) command. TRUNCATE is a Data Definition Language (DDL) command.

Number of Rows: We can use DELETE command to remove one or more rows from a table. TRUNCATE command will remove all the rows from a table.
WHERE clause: DELETE command provides support for WHERE clause that can be used to filter the data that we want to delete. TRUNCATE command can only delete all the rows. There is no WHERE clause in TRUNCATE command.
Commit: After DELETE command we have to issue COMMIT or ROLLBACK command to confirm our changes. After TRUNCATE command there is no need to run COMMIT. Changes done by TRUNCATE command can not be rolled back.

170.	What is the difference between DDL and DML commands in SQL?
        Main differences between Data Definition Language (DDL) and Data Manipulation Language (DML) commands are:
        DDL vs. DML: DDL statements are used for creating and defining the Database structure. DML statements are used for managing data within Database. Sample Statements: DDL statements are CREATE, ALTER, DROP, TRUNCATE, RENAME etc. DML statements are SELECT, INSERT, DELETE, UPDATE, MERGE, CALL etc.
        Number of Rows: DDL statements work on whole table. CREATE will a create a new table. DROP will remove the whole table. TRUNCATE will delete all records in a table. DML statements can work on one or more rows. INSERT can insert one or more rows. DELETE can remove one or more rows.

WHERE clause: DDL statements do not have a WHERE clause to filter the data. Most of DML statements support filtering the data by WHERE clause.
Commit: Changes done by a DDL statement can not be rolled back. So there is no need to issue a COMMIT or ROLLBACK command after DDL statement. We need to run COMMIT or ROLLBACK to confirm our changed after running a DML statement.
Transaction: Since each DDL statement is permanent, we can not run multiple DDL statements in a group like Transaction. DML statements can be run in a Transaction. Then we can COMMIT or ROLLBACK this group as a transaction. E.g. We can insert data in two tables and commit it together in a transaction.
Triggers: After DDL statements no triggers are fired. But after DML statements relevant triggers can be fired.

Why do we use Escape characters in SQL queries?
In SQL, there are certain special characters and words that are reserved for special purpose. E.g. & is a reserved character. When we want to use these special characters in the context of our data, we have to use Escape characters to pass the message to database to interpret these as non Special / non Reserved characters.

What is the difference between Primary key and Unique key in SQL?
Main differences between Primary key and Unique key in SQL are:
Number: There can be only one Primary key in a table. There can be more than one Unique key in a table.
Null value: In some DBMS Primary key cannot be NULL. E.g. MySQL adds NOT NULL to Primary key. A Unique key can have null values.
Unique Identifier: Primary Key is a unique identifier of a record in database table. Unique key can be null and we may not be able to identify a record in a unique way by a unique key
Changes: It is not recommended to change a Primary key. A Unique key can be changed much easily.
Usage: Primary Key is used to identify a row in a table. A Unique key is used to prevent duplicate non-null values in a column.

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

What is the datatype of ROWID?
ROWID Pseudocolumn in Oracle is of ROWID datatype. It is a string that represents the address of a row in the database.

What is the difference between where clause and having clause?
We use where clause to filter elements based on some criteria on individual records of a table.

E.g. We can select only employees with first name as John.
SELECT ID, Name FROM Employee WHERE name = ‘John’
We use having clause to filter the groups based on the values of aggregate functions.
E.g. We can group by department and only select departments that have more than 10 employees.
SELECT deptId, count(1) FROM Employee GROUP BY deptId HAVING count(*) > 10.

How will you calculate the number of days between two dates in MySQL?
We can use DATEDIFF function for this purpose. The query to get the number of days between two dates in MySQL is as follows:
SELECT DATEDIFF('2016-12- 31', '2015-01-01');

What are the different types of Triggers in MySQL?
MySQL	supports	six	types	of triggers. These are as follows:
Before Insert: This trigger runs before inserting a new row in a table.
After Insert: This triggerruns after inserting a new row in a table.
Before Update: This trigger runs before updating an existing row in a table.
After Update: This trigger runs after updating an existing row in a table.
Before Delete: This trigger runs before deleting an existing row in a table.
After Delete: This trigger runs after deleting an existing row in a table.

179.	What are the differences between Heap table and temporary table in MySQL?
        Duration: Heap tables are stored in memory. Therefore a Heap table remains in existence even if the session is disconnected. When we restart Database, Heap tables get cleaned up.
        Temporary tables are valid only during a session. Once the session is disconnected, temporary table is cleaned up.
        Privilege: We need special privilege to create a Temporary table. Heap tables are just another form of storage in MySQL.
        Sharing: Temporary tables are not shared between clients. Each connection will have a unique temporary table. But Heap tables can be shared between clients.

What is a Heap table in MySQL?
In MySQL there are tables that are present in memory. These are called Heap tables. During table creation we specify TYPE as HEAP for HEAP tables.
Heap tables provide very fast access to data. We can not store BLOB or TEXT datatype in a HEAP table. These tables also do not support AUTO_INCREMENT. Once we restart the Database, data in HEAP tables is lost.

What is the difference between BLOB and TEXT data type in MySQL?
BLOB is a Binary large Object. We can store a large amount of binary data in a BLOB data type column. TEXT is non-binary, character based string data type. We can store text data in TEXT column. We have to define a character set with a TEXT column.
TEXT can be easily converted into plain text.
BLOB has four types: TINYBLOB, BLOB, MEDIUMBLOB and LONGBLOB. Where as, TEXT
has its own four types: TINYTEXT,	TEXT, MEDIUMTEXT, LONGTEXT.

What will happen when AUTO_INCREME on an INTEGER column reaches MAX_VALUE in MySQL?
Once a column reaches the MAX_VALUE,		the AUTO_INCREMENT	stops working. It gives following error in log:
ERROR: 1467 (HY000): Failed to
read	auto-increment	value	from storage engine

What are the advantages of MySQL as compared with Oracle DB?
Some of the main advantages of MySQL over Oracle DB are as follows:
Cost: MySQL is an Open Source and free RDBMS software. Oracle is usually a paid option for RDBMS.
Space: MySQL uses around 1 MB to run whereas Oracle may need as high as 128 MB to run the database server.
Flexibility: MySQL can be used to run a small website as well as very large scale systems. Oracle is generally used in medium to large scale systems.
Management: In MySQL, database administration is much easier due to self- management features like- automatic space expansion,
auto-restart and dynamic configuration changes. In Oracle dedicated DBA has to work on managing the Database.
Portable: MySQL is easily portable to different hardware and operating system. Migrating Oracle from one platform to another is a tougher task.

What are the disadvantages of MySQL?
Some of the main disadvantages of MySQL are as follows:
Dependent on Additional S/W: MySQL has less number of features in standard out-of-box version. So we have to add additional software to get more features. It gets difficult to find, decide and use the additional software with MySQL. SQL Compliance: MySQL is not full SQL compliant. Due to this developers find it difficult to cope with the syntax of SQL in MySQL. Transaction handling: Some users complain that DB transactions are not handled properly in MySQL.

What is the difference between CHAR and VARCHAR datatype in MySQL?
Some of the main differences between CHAR and VARCHAR datatypes in MySQL are as follows:
Size:	In	a	CHAR	type column, length is fixed. In a

VARCHAR	type	column length can vary.
Storage: There are different mechanisms to store and retrieve CHAR and VARCHAR data types in MySQL.
Maximum Size: A CHAR data type can hold maximum
255 characters. A VARCHAR datatype can store up to 4000 characters.
Speed: CHAR datatype is 50% faster than VARCHAR datatype in MySQL.
Memory Allocation: A CHAR datatype column uses static memory allocation. Since the length of data stored in a VARCHAR can vary, this datatype uses dynamic memory allocation.

What is the use of 'i_am_a_dummy flag' in MySQL?
In MySQL, there is falg "ia_am_a_dummy" that can be used to save beginner developers from erroneous query like 'DELETE FROM table_name'. If we run this query it will delete all the data from table names table_name. With     'i_am_a_dummy      flag', MySQL will not permit running such a query. It will prompt user to create a query with WHERE clause so that only specific data is deleted. We can achieve similar functionality with 'safe_updates' option in MySQL. This flag also works on UPDATE statement to restrict updates on a table without WHERE clause.

How can we get current date and time in MySQL?
We can use following query in MySQL to get the current date:
SELECT CURRENT_DATE();
We can use following query in MySQL to get the current time as well as date:
SELECT NOW();

What is the difference between timestamp in Unix and MySQL?
In Unix as well as in MySQL, timestamp is stored as a 32-bit integer.
A timestamp is the number of seconds from the Unix Epoch on January 1st, 1970 at UTC.
In MySQL we can represent the timestamp in a readable format.
Timestamp format in MySQL is YYYY-MM-DD HH:MM:SS

How will you limit a MySQL query to display only top 10 rows?
We can use LIMIT clause in MySQL to limit a query to a range of rows.
Following query will give top 10 rows from the table with table_name:
SELECT * FROM <table_name> LIMIT 0,10;
Following query will give 6 rows starting from the 4th row in table with table_name:
SELECT * FROM <table_name> LIMIT 3,6;

What is automatic initialization and updating for TIMESTAMP in a MySQL table?
In MySQL, there is a TIMESTAMP datatype that provides features like automatic initialization and updating to current time and date. If a column is auto-initialized, then it will be set to current timestamp on inserting a new row with no value for the column. If a column is auto-updated, then its value will be updated to current timestamp when the value of any other column in the same row is updated. We can mark a column as DEFAULT to prevent this auto- initialize and auto-update behavior.

How can we get the list of all the indexes on a table?
We can use following command to get the list of all the indexes on a table in MySQL:
SHOW         INDEX	FROM table_name; At maximum we can use 16 columns in a multi-column index of table.

What is SAVEPOINT in MySQL?
SAVEPOINT is a statement in SQL. We can use SAVEPOINT <savepoint_name> statement to create a point of time in a Database transaction with a name. Later we can use this savepoint to rollback the transaction upto that point of time.

17. What is the difference between ROLLBACK TO SAVEPOINT and RELEASE SAVEPOINT?
    We     use     ROLLBACK     TO SAVEPOINT statement to undo the effect of a transaction upto the SAVEPOINT mentioned in ROLLBACK statement.
    RELEASE SAVEPOINT is simply used to delete the SAVEPOINT with a name from a transaction. There is commit or rollback for SAVEPOINT in RELEASE
    statement.In both the cases we should have first created a SAVEPOINT. Else we will get the error while doing ROLLBACK or RELEASE of a SAVEPOINT.

How will you search for a String in MySQL column?
We can use REGEXP operator to search for a String in MySQL column. It is regular expression search on columns with text type value. We can define different types of regular expressions and search them in a text with the REGEXP expression that can match our crietria.

How can we find the version of the MySQL server and the name of the current database by SELECT query?
We can use built in functions VERSION() and DATABASE() in MySQL to get the version of MySQL server and the name of database in MySQL.
Query is as follows: SELECT	VERSION(), DATABASE();

What is the use of IFNULL() operator in MySQL?
We use IFNULL operator in MySQL to get a non-null value for a column with null value.
IFNULL(expr1, expr2)
If expr1 is not null then expr1 is returned. If expr1 is null then expr2 is returned.
Eg.	SELECT	name, IFNULL(id,'Unknown') AS 'id' FROM user;
If id is not null then id is returned. If id is null then Unknown is returned.

How will you check if a table exists in MySQL?
We can use CHECK TABLE query to see the existence of a table in MySQL.
Query is as follows: CHECK TABLE <table_name>;

How will you see the structure of a table in MySQL?
We can use DESC query to see the structure of a table in MySQL. It will return the name of columns and their datatype in a table. Query is as follows: DESC <table_name>;

What are the objects that can be created by CREATE statement in MySQL?
We can create following objects by CREATE statement in MySQL:
DATABASE USER TABLE INDEX
VIEW TRIGGER EVENT FUNCTION PROCEDURE

24. How will you see the current user logged into MySQL connection?
    We can use USER() command to get the user logged into MySQL connection.
    Command is as follows: SELECT USER();
    How can you copy the structure of a table into another table without copying the data?
    It is a  trick question. But it has practical use in day to day work.
    Query for this is as follows: CREATE TABLE table_name AS SELECT * FROM USER WHERE 1 > 2;
    In this example condition in WHERE clause will be always false. Due to this no data is retrieved by SELECT query.

What is the difference between Batch and Interactive modes of MySQL?
In Interactive mode, we use command line interface and enter queries one by one. MySQL will execute the query and return the result in command line interface. In Batch mode of MySQL we can write all the queries in a SQL file. Then we can run this SQL file from MySQL command line or from Scheduler Job. MySQL will execute all the queries and return the result.
How can we get a random number between 1 and 100 in MySQL?
In MySQL we have a RAND() function that returns a random number between 0 and 1.
SELECT RAND();
If we want to get a random number between 1 and 100, we can use following query:
SELECT RAND() * 100;