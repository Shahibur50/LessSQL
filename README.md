# ``School DataBase Management System (SDBMS)``

 A database management system based on MySQL, with a goal to simplify the usage of a RDBMS for data-management in schools.
 > This program simplifies the process/way of using databases in MySQL by asking the user about data to be queried or updated and converting those answers given by users into MySQL query language, so that any person could simply use databases without having to learn a lot about SQL.

<br>

# ``********** Documentation for SDBMS ***********``

## ``NOTE!``
### Please first install and setup a mysql server in your computer to use this software.

> ### Download MySQL installer from here: https://dev.mysql.com/downloads/installer/

<br>

# **STARTING SCREEN OF SDBMS:**

```
USER-NAME: {user-name}  # Enter your user-name here, usually its 'root' for default installtion.
Password: {password}  # Enter your password here, created during installation
Connecting to the server...

CONNECTION ESTABLISHED!

LOGGED IN AS: {user-name}@{host-name}
TIME: {time}

Server version: {your server's version}

+----------------------------------------------------------------+
| WELCOME TO SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)           |
| Version: 2.11.11                                               |
|                                                                |
| Copyright (C) 2020  Shahibur Rahaman                           |
|                                                                |
| This program comes with ABSOLUTELY NO WARRANTY;                |
| for details type show_w()                                      |
| This is free software, and you are welcome to redistribute it  |
| under certain conditions; type show_c() for details.           |
|                                                                |
| Commands end with ()                                           |
|                                                                |
| To cancel any input statement type /c                          |
|                                                                |
| For help type help(); To exit the program type exit()          |
+----------------------------------------------------------------+

COMMAND|>
```

<br>

# **COMMANDS FOR DATABASE MANIPULATION:**

## 1. **`show_db()`**
- ### *Function:* `See all of the existing database.`
- ### *Example:*

```
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
```

<br>

## 2. **`create_db()`**
- ### *Function:* `Creates a new database.`
- ### *Syntax:*

```
COMMAND|> create_db()
        -> DATABASE NAME: {New database name}
```

- ### *Example:*
```
COMMAND|> create_db()
       -> DATABASE NAME: demo_db

Query OK, Created database 'demo_db'.
```

<br>

## 3. **`use_db()`**
- ### *Function:* `Use an existing database.`
- ### *Syntax:*

```
COMMAND|> use_db()
       -> DATABASE NAME: {Enter the database name to be used}
```

- ### *Example:*

```
COMMAND|> use_db()
       -> DATABASE NAME: demo_db  

Query OK, now using database 'demo_db'.
```

<br>

## 4. **`delete_db()`**
- ### *Function:* `Delete an existing database.`
- ### *Syntax:*

```
COMMAND|> delete_db()
       -> DATABASE NAME: {Enter the database name to be deleted} 

       -> IRREVERSIBLE CHANGE! Do you really want to delete the table 'demo_db'? (y/n) {Enter either 'y' to delete or 'n' to cancel it.}
```

- ### *Example:*

```
COMMAND|> delete_db()
       -> DATABASE NAME: demo_db    

       -> IRREVERSIBLE CHANGE! Do you really want to delete the databse 'demo_db'? (y/n) y
Query OK, Deleted database 'demo_db'.
```

## **Or,**

```
COMMAND|> delete_db()
       -> DATABASE NAME: demo_db

       -> IRREVERSIBLE CHANGE! Do you really want to delete the databse 'demo_db'? (y/n) n

Query cancelled, for deletion of the database 'demo_db'.
```

#

<br>

#
# **COMMANDS FOR TABLE MANIPULATION:**

## 1. **`show_tb()`**
- ### *Function:* `Shows tables present in an existing database.`
- ### *Example:*

```
COMMAND|> show_tb()
+-------------------+
| Tables_in_demo_db |
+-------------------+
| attendance        |
+-------------------+
```

<br>

## 2. **`create_tb()`**
- ### *Function:* `Creates a new table.`
- ### *Syntax:*
**\* Remember to put a space between column name and column's data-type.**
```
COMMAND|> create_tb()
       -> NAME OF TABLE TO BE CREATED: {New table name}
       -> NO. OF COLUMNS: {Enter the no. of columns or fields}
       -> COLUMN (1) NAME AND DATA-TYPE: {1st column name} {1st column's data-type}
       -> COLUMN (2) NAME AND DATA-TYPE: {2nd column name} {2nd column's data-type}
       ...
       -> PRIMARY KEY: {Enter the Primary Key name (The primary key always has the unique data and it's value cannot be NULL.)}
```

- ### *Example:*

```
COMMAND|> create_tb()
       -> NAME OF TABLE TO BE CREATED: Attendance
       -> NO. OF COLUMNS: 5
       -> COLUMN (1) NAME AND DATA-TYPE: Roll INT
       -> COLUMN (2) NAME AND DATA-TYPE: Name VARCHAR(20)
       -> COLUMN (3) NAME AND DATA-TYPE: Class VARCHAR(3)
       -> COLUMN (4) NAME AND DATA-TYPE: Section CHAR(1)
       -> COLUMN (5) NAME AND DATA-TYPE: Remarks CHAR(1)
       -> PRIMARY KEY: Roll

Query OK, Created the 'Attendance' table.
```

<br>

## 3. **`describe_tb()`**
- ### *Function:* `Shows the structure or schema of an exixting table.`
- ### *Syntax:*

```
COMMAND|> describe_tb()
       -> TABLE NAME: {Enter the table name.} 
```

- ### *Example:*

```
COMMAND|> describe_tb()
       -> TABLE NAME: attendance 
+---------+----------------+------+-----+---------+-------+
| Field   | Type           | Null | Key | Default | Extra |
+---------+----------------+------+-----+---------+-------+
| Roll    | b'int'         | NO   | PRI | None    |       |
| Name    | b'varchar(20)' | YES  |     | None    |       |
| Class   | b'varchar(3)'  | YES  |     | None    |       |
| Section | b'char(1)'     | YES  |     | None    |       |
| Remarks | b'char(1)'     | YES  |     | None    |       |
+---------+----------------+------+-----+---------+-------+
```

<br>

## 4. **`delete_tb()`**
- ### *Function:* `Deletes an existing table.`
- ### *Syntax:*

```
COMMAND|> delete_tb()
      -> NAME OF TABLE TO BE DELETED: {Enter the table name}

      -> IRREVERSIBLE CHANGE! Do you really want to delete the table 'demo_tb'? (y/n) {Enter either 'y' to delete or 'n' to cancel it.}
```

- ### *Example:*

```
COMMAND|> delete_tb()
      -> NAME OF TABLE TO BE DELETED: demo_tb  

      -> IRREVERSIBLE CHANGE! Do you really want to delete the table 'demo_tb'? (y/n) y

Query OK, deleted the table (demo_tb)
```

## **Or,**

```
COMMAND|> delete_tb()
      -> NAME OF TABLE TO BE DELETED: demo_tb

      -> IRREVERSIBLE CHANGE! Do you really want to delete the table 'demo_tb'? (y/n) n

Query cancelled, for deletion of table.
```

#

<br>

#
# **COMMANDS FOR COLUMN MANIPULATION:**

## 1. **`add_column()`**
- ### *Function:* `Adds a new column to an existing table.`
- ### *Syntax:*

```
COMMAND|> add_column()
       -> TABLE NAME: {Enter the table name}
       -> NEW COLUMN NAME AND DATA-TYPE: {Column name} {column's data-type} 
```

- ### *Example:*

```
COMMAND|> add_column()
       -> TABLE NAME: attendance 
       -> NEW COLUMN NAME AND DATA-TYPE: Email VARCHAR(30) 

Query OK, added column 'Email' with data-type 'VARCHAR(30)' to the table 'attendance'.
```

<br>

## 2. **`modify_column()`**
- ### *Function:* `Modifies an existing column in a table.`
- ### *Syntax:*

```
COMMAND|> modify_column()
       -> TABLE NAME: {Enter the table name}
       -> EXISTING COLUMN NAME: {Enter the existing column name}
       -> NEW DATA-TYPE FOR THE COLUMN: {Enter the new data type for the column}
```

- ### *Example:*

```
COMMAND|> modify_column()
       -> TABLE NAME: attendance
       -> EXISTING COLUMN NAME: Email
       -> NEW DATA-TYPE FOR THE COLUMN: VARCHAR(50)

Query OK, modified column 'Email' to new data-type 'VARCHAR(50)' in table 'attendance'.
```

<br>

## 3. **`delete_column()`**
- ### *Function:* `Deletes an existing column in a table.`
- ### *Syntax:*

```
COMMAND|> delete_column()
       -> TABLE NAME: {Enter the table name}
       -> NAME OF COLUMN TO BE DELETED: {Enter the column name}

      -> IRREVERSIBLE CHANGE! Do you really want to delete the column 'Email'? (y/n) {Enter either 'y' to delete or 'n' to cancel it.}
```

- ### *Example:*

```
COMMAND|> delete_column()
       -> TABLE NAME: attendance
       -> NAME OF COLUMN TO BE DELETED: Email

      -> IRREVERSIBLE CHANGE! Do you really want to delete the column 'Email'? (y/n) y

Query OK, Deleted column 'Email' from table 'attendance'.
```

## **Or,**

```
COMMAND|> delete_column()
       -> TABLE NAME: attendance
       -> NAME OF COLUMN TO BE DELETED: Email

      -> IRREVERSIBLE CHANGE! Do you really want to delete the column 'Email'? (y/n) n

Query cancelled, for deletion of column.
```

#

<br>

#
# **COMMANDS FOR IN-TABLE QUERIES:**

## 1. **`reveal()`**
- ### *Function:* `Shows all of the rows/records present in a table.`
- ### *Syntax:*

```
COMMAND|> reveal()
       -> TABLE NAME: {Enter the table name}
```

- ### *Example:*

```
COMMAND|> reveal()  
       -> TABLE NAME: attendance 
+------+-----------------+-------+---------+---------+------------+
| Roll | Name            | Class | Section | Remarks | Date       |
+------+-----------------+-------+---------+---------+------------+
| 1    | Joe gates       | XI    | D       | P       | 2020-11-23 |
| 2    | linus sebastian | XI    | D       | A       | 2020-11-23 |
| 3    | Drake jobs      | XI    | D       | P       | 2020-11-23 |
| 4    | Alan Turing     | XI    | D       | P       | 2020-11-23 |
| 5    | John morgan     | XI    | D       | P       | 2020-11-23 |
+------+-----------------+-------+---------+---------+------------+
```

## 2. **`search()`**
- ### *Function:* `Searches for row(s)/record(s) present in a table.`
- ### *Syntax:*

```
COMMAND|> search()
       -> TABLE NAME: {Enter the table name}
       -> COLUMN NAME: {Enter the column name}
       -> VALUE: {Enter the value to be searched in the column mentioned earlier}
```

- ### *Example 1:*

```
COMMAND|> search()
       -> TABLE NAME: attendance 
       -> COLUMN NAME: Name
       -> VALUE: 'Joe gates'
+------+-----------+-------+---------+---------+------------+
| Roll | Name      | Class | Section | Remarks | Date       |
+------+-----------+-------+---------+---------+------------+
| 1    | Joe gates | XI    | D       | P       | 2020-11-23 |
+------+-----------+-------+---------+---------+------------+
```

- ### *Example 2:*

```
COMMAND|> search()    
       -> TABLE NAME: attendance
       -> COLUMN NAME: Remarks
       -> VALUE: 'P'
+------+-------------+-------+---------+---------+------------+
| Roll | Name        | Class | Section | Remarks | Date       |
+------+-------------+-------+---------+---------+------------+
| 1    | Joe gates   | XI    | D       | P       | 2020-11-23 |
| 3    | Drake jobs  | XI    | D       | P       | 2020-11-23 |
| 4    | Alan Turing | XI    | D       | P       | 2020-11-23 |
| 5    | John morgan | XI    | D       | P       | 2020-11-23 |
+------+-------------+-------+---------+---------+------------+
```

- ### *Example 3:*

```
COMMAND|> search()   
       -> TABLE NAME: attendance
       -> COLUMN NAME: Remarks
       -> VALUE: 'A'
+------+-----------------+-------+---------+---------+------------+
| Roll | Name            | Class | Section | Remarks | Date       |
+------+-----------------+-------+---------+---------+------------+
| 2    | linus sebastian | XI    | D       | A       | 2020-11-23 |
+------+-----------------+-------+---------+---------+------------+
```

#

<br>

#
# **COMMANDS FOR IN-TABLE MANIPULATION:**

## 1. **`insert()`**
- ### *Function:* `Inserts data in a row/record in a table.`
- ### *Syntax:*

### **\* Remember to use comma between two values.**
### **\* Enter values releatively for column names and thier values.**

- ### *Syntax:*

```
COMMAND|> insert()
       -> TABLE NAME: {Enter the table name}
       -> COLUMN NAMES: {Enter the column name(s) to which the data has to be inserted} 
       -> VALUES: {Enter the values relative to the column names}
```

- ### *Example:*

```
COMMAND|> insert()   
       -> TABLE NAME: attendance
       -> COLUMN NAMES: Roll, Name, Class, Section, Remarks, Date 
       -> VALUES: 6, 'Taran Duncun', 'XI', 'D', 'A', '2020-11-23'

Query OK, inserted value(s) (6, 'Taran Duncun', 'XI', 'D', 'A', '2020-11-23') in column(s) 'Roll, Name, Class, Section, Remarks, Date' in table 'attendance'
```

<br>

## 2. **`update()`**
- ### *Function:* `Modifies data-item present in a row in a table`
- ### *Syntax:*

```
COMMAND|> update()
       -> TABLE NAME: {Enter the table name}
       -> CONDITION: {Enter the condition for updating}
       -> COLUMN/FIELD TO BE UPDATED: {Enter the column name under which the data has to be updated}
       -> VALUE OF DATA-ITEM TO BE UPDATED: {Enter the value to be updated in column mentioned earlier}
```

- ### *Example:*

```
COMMAND|> update()
       -> TABLE NAME: attendance
       -> CONDITION: Name = 'Taran Duncun' 
       -> COLUMN/FIELD TO BE UPDATED: Remarks
       -> VALUE OF DATA-ITEM TO BE UPDATED: 'P'

Query OK, updated the row(s)/record(s) in column/field (Remarks) to ('P') where condition (Name = 'Taran Duncun') was satisfied.
```

<br>

## 3. **`delete()`**
- ### *Function:* `Deletes complete row(s)/record(s) present in a table`
- ### *Syntax:*

```
COMMAND|> delete()
       -> TABLE NAME: {Enter the table name}
       -> COLUMN/FIELD NAME: {Enter the column name to be checked for deletion}
       -> DATA-ITEM VALUE: {Enter the data-item value present in the column mentioned above}
```

- ### *Example:*

```
COMMAND|> delete()   
       -> TABLE NAME: attendance
       -> COLUMN/FIELD NAME: Name
       -> DATA-ITEM VALUE: 'Linus sebastian'

Query OK, deleted the row(s)/record(s) containing the value 'Linus sebastian'.
```
