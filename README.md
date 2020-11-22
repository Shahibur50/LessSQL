<Body bgcolor="blue">

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
