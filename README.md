# School_DataBase_Management_System (SDBMS)

 A database management system based on MySQL, with a goal to simplify the usage of a RDBMS for data-management in schools.
 > This program simplifies the process/way of using databases in MySQL by asking the user about data to be queried or updated and converting those answers given by users into MySQL query language, so that any person could simply use databases without having to learn a lot about SQL.

# Documentation Under-development...

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
