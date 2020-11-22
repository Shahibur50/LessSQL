# School_DataBase_Management_System (SDBMS)

 A database management system based on MySQL, with a goal to simplify the usage of a RDBMS for data-management in schools.
 > This program simplifies the process/way of using databases in MySQL by asking the user about data to be queried or updated and converting those answers given by users into MySQL query language, so that any person could simply use databases without having to learn SQL.

# Documentation Under-development...

# COMMANDS FOR DATABASE MANIPULATION:

## **`show_db()`**
### *Function:* `See all of the existing database.`
### *Example:*

<pre>
COMMAND|> show_db()
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| project            |
| sys                |
+--------------------+
</pre>

#

<h2>
create_db()
</h2>

<i><h3>
Function: Creates a new database.
</h3></i>

<i><h3>
Syntax:
</h3></i>

<pre>
COMMAND|> create_db()
       -> DATABASE NAME: {New database name}
</pre>

<i><h3>
Example:
</h3></i>

<pre>
COMMAND|> create_db()
       -> DATABASE NAME: demo_db

Query OK, Created database 'demo_db'.
</pre>

#

<h2>
use_db()
</h2>

<i><h3>
Function: Use an existing database.
</h3></i>

<i><h3>
Syntax:
</h3></i>

<pre>
COMMAND|> use_db()
       -> DATABASE NAME: {Enter the database name to be used}
</pre>

<i><h3>
Example:
</h3></i>

<pre>
COMMAND|> use_db()
       -> DATABASE NAME: demo_db  

Query OK, now using database 'demo_db'.
</pre>

#

<h2>
delete_db()
</h2>

<i><h3>
Function: Delete an existing database.
</h3></i>

<i><h3>
Syntax:
</h3></i>

<pre>
COMMAND|> delete_db()
       -> DATABASE NAME: {Enter the database name to be deleted} 

       -> IRREVERSIBLE CHANGE! Do you really want to delete the table 'demo_db'? (y/n) {Enter either 'y' to delete or 'n' to cancel it.}
</pre>

<i><h3>
Example:
</h3></i>

<pre>
COMMAND|> delete_db()
       -> DATABASE NAME: demo_db    

       -> IRREVERSIBLE CHANGE! Do you really want to delete the databse 'demo_db'? (y/n) y
Query OK, Deleted database 'demo_db'.
</pre>


<b><h3>
Or,
</b></h3>

<pre>
COMMAND|> delete_db()
       -> DATABASE NAME: demo_db

       -> IRREVERSIBLE CHANGE! Do you really want to delete the databse 'demo_db'? (y/n) n

Query cancelled, for deletion of the database 'demo_db'.
</pre>

