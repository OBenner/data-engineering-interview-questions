# Tableau
+ [What is data visualization in Tableau?](#What-is-data-visualization-in-Tableau)
+ [What is the difference between various BI tools and Tableau?](#What-is-the-difference-between-various-BI-tools-and-Tableau)
+ [What are different Tableau products?](#What-are-different-Tableau-products)
+ [What is a parameter in Tableau?](#What-is-a-parameter-in-Tableau)
+ [Tell me something about measures and dimensions?](#Tell-me-something-about-measures-and-dimensions)
+ [What are continuous and discrete field types?](#What-are-continuous-and-discrete-field-types)
+ [What is aggregation and disaggregation of data?](#What-is-aggregation-and-disaggregation-of-data)
+ [What are the different types of joins in Tableau?](#What-are-the-different-types-of-joins-in-Tableau)
+ [Tell me the different connections to make with a dataset?](#Tell-me-the-different-connections-to-make-with-a-dataset)
+ [What are the supported file extensions in Tableau?](#What-are-the-supported-file-extensions-in-Tableau)
+ [What are the supported data types in Tableau?](#What-are-the-supported-data-types-in-Tableau)
+ [What are sets?](#What-are-sets)
+ [What are groups in Tableau?](#What-are-groups-in-Tableau)
+ [What are shelves?](#What-are-shelves)
+ [Tell me something about Data blending in Tableau?](#Tell-me-something-about-Data-blending-in-Tableau)
+ [How do you generally perform load testing in Tableau?](#How-do-you-generally-perform-load-testing-in-Tableau)
+ [Why would someone not use Tableau?](#Why-would-someone-not-use-Tableau)
+ [What is Tableau data engine?](#What-is-Tableau-data-engine)
+ [What are the various types of filters in Tableau?](#What-are-the-various-types-of-filters-in-Tableau)
+ [What are dual axes?](#What-are-dual-axes)
+ [What is the difference between a tree and heat map?](#What-is-the-difference-between-a-tree-and-heat-map)
+ [What are extracts and schedules in Tableau server?](#What-are-extracts-and-schedules-in-Tableau-server)
+ [What are the components in a dashboard?](#What-are-the-components-in-a-dashboard)
+ [What is a TDE file?](#What-is-a-TDE-file)
+ [What is the story in Tableau?](#What-is-the-story-in-Tableau)
+ [What are different Tableau files?](#What-are-different-Tableau-files)
+ [How do you embed views into webpages?](#How-do-you-embed-views-into-webpages)
+ [What is the maximum num of rows Tableau can utilize at one time?](#What-is-the-maximum-num-of-rows-Tableau-can-utilize-at-one-time)
+ [Mention what is the difference between published data sources and embedded data sources in Tableau?](#Mention-what-is-the-difference-between-published-data-sources-and-embedded-data-sources-in-Tableau)
+ [What is the DRIVE Program Methodology?](#What-is-the-DRIVE-Program-Methodology)
+ [How to use groups in a calculated field?](#How-to-use-groups-in-a-calculated-field)
+ [Explain when would you use Joins vs Blending in Tableau?](#Explain-when-would-you-use-Joins-vs-Blending-in-Tableau)
+ [What is Assume referential integrity?](#What-is-Assume-referential-integrity)
+ [What is a Calculated Field and How Will You Create One?](#What-is-a-Calculated-Field-and-How-Will-You-Create-One)
+ [How Can You Display the Top Five and Bottom Five Sales in the Same View?](#How-Can-You-Display-the-Top-Five-and-Bottom-Five-Sales-in-the-Same-View)
+ [What is the Rank Function in Tableau?](#What-is-the-Rank-Function-in-Tableau)
+ [What is the difference between Tableau and other similar tools like QlikView or IBM Cognos?](#What-is-the-difference-between-Tableau-and-other-similar-tools-like-QlikView-or-IBM-Cognos)

[Table of Contents](#Tableau)

## What is data visualization in Tableau?
Data visualization is a way to represent data that is visually appealing and interactive. With advancements in technology, the number of business intelligence tools has increased which helps users understand data, data sets, data points, charts, graphs, and focus on its impact rather than understanding the tool itself.

[Table of Contents](#Tableau)

## What is the difference between various BI tools and Tableau?
The basic difference between the traditional BI tools and Tableau lies in the efficiency and speed.
The architecture of Traditional BI tools has hardware limitations. While Tableau does not have any sort of dependencies
The traditional BI tools work on complex technologies while Tableau uses simple associative search to make it dynamic.
Traditional BI tools do not support multi-thread, in-memory, or multi-core computing while Tableau supports all these features after integrating complex technologies.
Traditional BI tools have a pre-defined data view while Tableau does a predictive analysis for business operations.

[Table of Contents](#Tableau)

## What are different Tableau products?
Tableau like other BI tools has a range of products:
Tableau Desktop: Desktop product is used to create optimized queries out from pictures of data. Once the queries are ready, you can perform those queries without the need to code. Tableau desktop encompasses data from various sources into its data engine and creates an interactive dashboard.
Tableau Server: When you have published dashboards using Tableau Desktop, Tableau servers help in sharing them throughout the organization. It is an enterprise-level feature that is installed on a Windows or Linux server.
Tableau Reader: Tableau Reader is a free feature available on Desktop that lets you open and views data visualizations. You can filter or drill down the data but restricts editing any formulas or performing any kind of actions on it. It is also used to extract connection files.
Tableau Online: Tableau online is also a paid feature but doesn’t need exclusive installation. It comes with the software and is used to share the published dashboards anywhere and everywhere.
Tableau Public: Tableau public is yet another free feature to view your data visualizations by saving them as worksheets or workbooks on Tableau Server.

[Table of Contents](#Tableau)

## What is a parameter in Tableau?
The parameter is a variable (numbers, strings, or date) created to replace a constant value in calculations, filters, or reference lines. For example, you create a field that returns true if the sales are greater than 30,000 and false if otherwise. Parameters are used to replace these numbers (30000 in this case) to dynamically set this during calculations. Parameters allow you to dynamically modify values in a calculation. The parameters can accept values in the following options:
All: Simple text field
List: List of possible values to select from
Range: Select values from a specified range

[Table of Contents](#Tableau)

## Tell me something about measures and dimensions?
In Tableau, when we connect to a new data source, each field in the data source is either mapped as measures or dimensions. These fields are the columns defined in the data source. Each field is assigned a dataType (integer, string, etc.) and a role (discrete dimension or continuous measure).
Measures contain numeric values that are analyzed by a dimension table. Measures are stored in a table that allows storage of multiple records and contains foreign keys referring uniquely to the associated dimension tables.
While Dimensions contain qualitative values (name, dates, geographical data) to define comprehensive attributes to categorize, segment, and reveal the data details.

[Table of Contents](#Tableau)

## What are continuous and discrete field types?
Tableau’s specialty lies in displaying data differently either in continuous format or discrete. Both of them are mathematical terms used to define data where continuous means without interruptions and discrete means are individually separate and distinct.
While the blue color indicates discrete behavior, the green color indicates continuous behavior. On one hand, the discrete view defines the headers and can be easily sorted, while continuous defines the axis in a graph view and cannot be sorted.
Discrete View Tableau

[Table of Contents](#Tableau)

## What is aggregation and disaggregation of data?
Aggregation of data means displaying the measures and dimensions in an aggregated form. The aggregate functions available in the Tableau tool are:
SUM (expression): Adds up all the values used in the expression. Used only for numeric values.
AVG (expression): Calculates the average of all the values used in the expression. Used only for numeric values.
Median (expression): Calculates the median of all the values across all the records used in the expression. Used only for numeric values.
Count (expression): Returns the number of values in the set of expressions. Excludes null values.
Count (distinct): Returns the number of unique values in the set of expressions.
Tableau, in fact, lets you alter the aggregation type for a view.

Disaggregation of data means displaying each and every data field separately.

[Table of Contents](#Tableau)

## What are the different types of joins in Tableau?
Tableau is pretty similar to SQL. Therefore, the types of joins in Tableau are similar:
Left Outer Join: Extracts all the records from the left table and the matching rows from the right table.
Right Outer Join: Extracts all the records from the right table and the matching rows from the left table.
Full Outer Join: Extracts the records from both the left and right tables. All unmatched rows go with the NULL value.
Inner Join: Extracts the records from both tables.

[Table of Contents](#Tableau)

## Tell me the different connections to make with a dataset?
There are two types of data connections in Tableau:
LIVE: Live connection is a dynamic way to extract real-time data by directly connecting to the data source. Tableau directly creates queries against the database entries and retrieves the query results in a workbook.
EXTRACT: A snapshot of the data, extract the file (.tde or .hyper file) contains data from a relational database. The data is extracted from a static source of data like an Excel Spreadsheet. You can schedule to refresh the snapshots which are done using the Tableau server. This doesn’t need any connection with the database.

[Table of Contents](#Tableau)

## What are the supported file extensions in Tableau?
The supported file extensions used in Tableau Desktop are:
Tableau Workbook (TWB): contains all worksheets, story points, dashboards, etc.
Tableau Data Source (TDS): contains connection information and metadata about your data source
Tableau Data Extract (TDE): contains data that has been extracted from other data sources.
Tableau Packaged Workbook (TWBX): contains a combination of the workbook, connection data, and metadata, and the data itself in the form of TDE.  It can be zipped and shared.
Tableau Packaged Data Source (TDSX): contains a combination of different files.
Tableau Bookmark (TBM): to earmark a specific worksheet.

[Table of Contents](#Tableau)

## What are the supported data types in Tableau?
The following data types are supported in Tableau:
DataType	Possible Values
Boolean	True/False
Date	Date Value (December 28, 2016)
Date & Time	Date & Timestamp values (December 28, 2016
06:00:00 PM)
Geographical Values	Geographical Mapping (Beijing, Mumbai)
Text/String	Text/String
Number	Decimal (8.00)
Number	Whole Number (5)

[Table of Contents](#Tableau)

## What are sets?
Sets are custom fields created as a subset of the data in your Tableau desktop. Sets can be computed based on conditions or created manually based on the dimensions of the data source. 
For example, A set of customers that earned revenue more than some value. Now, set data may update dynamically based on the conditions applied. Learn More

[Table of Contents](#Tableau)

## What are groups in Tableau?
Groups are created to visualize larger memberships using dimensions. Groups can create their own fields to categorize values in that specific dimension.

[Table of Contents](#Tableau)

## What are shelves?
Tableau worksheets contain various named elements like columns, rows, marks, filters, pages, etc. which are called shelves. You can place fields on shelves to create visualizations, increase the level of detail, or add context to it.

[Table of Contents](#Tableau)

## Tell me something about Data blending in Tableau?
Data blending is viewing and analyzing data from multiple sources in one place. Primary and secondary are two types of data sources that are involved in data blending.

[Table of Contents](#Tableau)

## How do you generally perform load testing in Tableau?
Load testing in Tableau is done to understand the server’s capacity with respect to its environment, data, workload, and use. It is preferable to conduct load testing at least 3-4 times in a year because with every new user, upgrade, or content authoring, the usage, data, and workload change.
Tabjolt was created by Tableau to conduct point-and-run load and performance testing specifically for Tableau servers. Tabjolt:
Automates the process of user-specified loads
Eliminates dependency on script development or script maintenance
Scales linearly with an increase in the load by adding more nodes to the cluster

[Table of Contents](#Tableau)

## Why would someone not use Tableau?
The limitations of using Tableau are:
Not cost-effective: Tableau is not that cost-effective when we compare it well with the other available data visualization tools. In addition to this, it has software upgrades, proper deployment, maintenance, and also training people for using the tool.
Not so secure: When it comes to data, everyone is extra cautious. Tableau focussed on security issues but fails to provide centralized data-level security. It pushes for row-level security and creates an account for every user which makes it more prone to security glitches.
BI capabilities are not enough: Tableau lacks basic BI capabilities like large-scale reporting, building data tables, or creating static layouts. It has limited result-sharing capabilities, email notification configuration is limited to admins, and the vendor doesn’t support trigger-based notifications.

[Table of Contents](#Tableau)

## What is Tableau data engine?
An analytical database that computes instant query responses, predictive analysis of the server, and integrated data. The data engine is useful when you need to create, refresh, or query extracts. It can be used for cross-database joins as well.

[Table of Contents](#Tableau)

## What are the various types of filters in Tableau?
Tableau has 6 different types of filters:
Extract Filter: This filter retrieves a subset of data from the data source.
Dimension Filter: This filter is for non-aggregated data (discrete).
Data Source Filter: This filter refrains users from viewing sensitive information and thus reduces data feeds.
Context Filter: This filter creates datasets by applying presets in Tableau.
Measure Filter: This filter applies various operations like sum, median, avg, etc.
Table Calculation Filter: This filter is applied after the view has been created.

[Table of Contents](#Tableau)

## What are dual axes?
Dual axes are used to analyze two different measures at two different scales in the same graph. This lets you compare multiple attributes on one graph with two independent axes layered one above the other.
To add a measure as a dual-axis, drag the field to the right side of the view and drop it when you see a black dashed line appear. You can also right-click (control-click on Mac) the measure on the Columns or Rows shelf and select Dual Axis.

[Table of Contents](#Tableau)

## What is the difference between a tree and heat map?
Both the maps help in analyzing data. While a heat map visualizes and compares different categories of data, a treemap displays a hierarchical structure of data in rectangles. Heat map visualizes measures against dimensions by depicting them in different colors. Similar to a text table with values defined in different colors.
Heatmap In Tableau
Treemap visualizes the hierarchy of data in nested rectangles. Hierarchy levels are displayed from larger rectangles to smaller ones.
Example - Below treemap shows aggregated sales totals across a range of product categories:
TreeMap in Tableau

[Table of Contents](#Tableau)

## What are extracts and schedules in Tableau server?
Data extracts are the subsets of data created from data sources. Schedules are scheduled refreshes made on extracts after publishing the workbook. This keeps the data up-to-date. Schedules are strictly managed by the server administrators.

[Table of Contents](#Tableau)

## What are the components in a dashboard?
The components displayed in a dashboard are:
Horizontal: Horizontal view allows the users to combine the worksheets and dashboard elements from left to right and edit the height of the elements.
Vertical: Vertical view allows the users to combine the worksheets and dashboard elements from top to bottom and edit the width of the elements.
Text: All the textual fields.
Image Extract: To extract an image Tableau applies some code, extracts the image, and saves it in a workbook in the XML format.
Web URL: Hyperlink that points to a web page, file, or other web resources outside of Tableau

[Table of Contents](#Tableau)

## What is a TDE file?
TDE is Tableau Desktop Extension with extension .tde. TDE file points to a file that contains data from external sources like MS Excel, MS Access, or CSV files. TDE makes it easier to analyze and discover data.

[Table of Contents](#Tableau)

## What is the story in Tableau?
Creating a story is effective in Tableau which is created by combining various charts to portray a plot of viewers. A story is a sheet that contains all the methods used to create those worksheets. To create a story:
Click the New Story on the dashboard.
Choose the right size of the story from the bottom-left corner or choose a custom size.
Start building the story by double-clicking the sheet and add it to the story point.
Add a caption to the story by clicking Add a caption.
You can update the highlights by clicking Update in the toolbar. You can also add layout options, format a story, or fit the story to your dashboard.

[Table of Contents](#Tableau)

## What are different Tableau files?
Workbooks: Workbooks contain one or more worksheets and dashboard elements.
Bookmarks: Contains a single worksheet that is easier to share.
Packaged Workbooks: Contains a workbook along with supporting local file data and background images.
Data Extraction Files: Extract files that contain a subset of data.
Data Connection Files: Small XML file with various connection information.

[Table of Contents](#Tableau)

## How do you embed views into webpages?
You can easily integrate interactive views from your Tableau Server or Tableau online onto webpages, blogs, web applications, or internet portals. But to have a look at the views, the permissions demand the viewer to create an account on the Tableau Server. To embed views, click the Share button on the top of the view and copy the embed code to paste it on the web page.
You can also customize the embedded code or Tableau Javascript APIs to embed views.

[Table of Contents](#Tableau)

## What is the maximum num of rows Tableau can utilize at one time?
The maximum number of rows or columns is indefinite because even though Tableau contains petabytes of data, it intelligently uses only those rows and columns which you need to extract for your purpose.

[Table of Contents](#Tableau)

## Mention what is the difference between published data sources and embedded data sources in Tableau?
Connection information is the details of data that you want to bring into Tableau. Before publishing it, you can create an extract of the same.
Published Data Source: It contains connection information that is independent of any workbook.
Embedded Data Source: It contains connection information which is connected to a workbook

[Table of Contents](#Tableau)

## What is the DRIVE Program Methodology?
DRIVE program methodology creates a structure around data analytics derived from enterprise deployments. The drive methodology is iterative in nature and includes agile methods that are faster and effective.

[Table of Contents](#Tableau)

## How to use groups in a calculated field?
Add the GroupBy clause to SQL queries or create a calculated field in the data window to group fields.
Using groups in a calculation. You cannot reference ad-hoc groups in a calculation.
Blend data using groups created in the secondary data source: Only calculated groups can be used in data blending if the group was created in the secondary data source.
Use a group in another workbook. You can easily replicate a group in another workbook by copy and pasting a calculation.

[Table of Contents](#Tableau)

## Explain when would you use Joins vs Blending in Tableau?
While the two terms may sound similar, there is a difference in their meaning and use in Tableau:
While Join is used to combine two or more tables within the same data source.
Blending is used to combine data from multiple data sources such as Oracle, Excel, SQL server, etc.

[Table of Contents](#Tableau)

## What is Assume referential integrity?
In some cases, you can improve query performance by selecting the option to Assume Referential Integrity from the Data menu. When you use this option, Tableau will include the joined table in the query only if it is specifically referenced by fields in the view.

[Table of Contents](#Tableau)

## What is a Calculated Field and How Will You Create One?
Calculated fields are created using formulas based on other fields. These fields do not exist but are created by you.
You can create these fields to:
Segment data
Convert the data type of a field, such as converting a string to a date.
Aggregate data
Filter results
Calculate ratios

There are three main types of calculations that you can create:
Basic Calculations: Transform values of the data fields at the source level
Level of Detail (LOD) Expressions: Transform values of the data fields at the source level like basic calculations but with more granular access
Table Calculations: Transform values of the data fields only at the visualization level
To create calculate fields:
In Tableau, navigate to Analysis>Create a calculated field. Input details in the calculation editor.
And, done!

[Table of Contents](#Tableau)

## How Can You Display the Top Five and Bottom Five Sales in the Same View?
You can see top five and bottom five sales with the help of these functions:
Drag customer name to row and sales to the column.
Sort Sum(sales) in descending order.
Create a calculated field Rank of Sales.

[Table of Contents](#Tableau)

## What is the Rank Function in Tableau?
Rank function is used to give positions (rank) to any measure in the data set. Tableau can rank measure in the following ways:
Rank: The rank function in Tableau accepts two arguments: aggregated measure and ranking order (optional) with a default value of desc.
Rank_dense: The rank_dense also accepts the two arguments: aggregated measure and ranking order. This assigns the same rank to the same values but doesn’t stop there and keeps incrementing with the other values. For instance, if you have values 10, 20, 20, 30, then ranks will be 1, 2, 2, 3.
Rank_modified: The rank_modified assigns the same rank to similar values.
Rank_unique: The rank_unique assigns a unique rank to each and every value. For example, If the values are 10, 20, 20, 30 then the assigned ranks will be 1,2,3,4 respectively.

[Table of Contents](#Tableau)

## What is the difference between Tableau and other similar tools like QlikView or IBM Cognos?
Tableau is different than QlikView or IBM Cognos for various reasons:
Tableau is an intuitive data visualization tool simplifying the story creation by simple drag and drop techniques. On the other hand, BI tools like QlikView or Cognos convert data into metadata to let the users explore data relations. If your presentation runs around presenting data in aesthetic visualizations then opt for Tableau. If not, and might need a full BI platform then go for Cognos/QlikView
The ease of use or extracting data details is easier in Tableau than compared to extensive BI tools like Cognos. With Tableau, your team members, be it a guy from sales can easily read the data and give insights. But with Cognos, only members with extensive tool knowledge are appreciated and welcomed.
[Table of Contents](#Tableau)