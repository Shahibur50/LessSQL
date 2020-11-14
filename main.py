"""
STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS)

version 1.9.7 (Beta)

"""
from mysql.connector import connection
from mysql.connector import errorcode
from prettytable import PrettyTable
from prettytable import from_db_cursor
from datetime import datetime
import time
import mysql.connector
import getpass

PT = PrettyTable()
connection = False

usr_name = input("USER-NAME: ")
db = False
passwd = getpass.getpass()
host = "localhost"

try:
    cnx = mysql.connector.connect(user=usr_name,
                                  password=passwd,
                                  host=host)
    cursor = cnx.cursor()
    print("Connecting to the server...")
    time.sleep(2)
    print("\nCONNECTION ESTABLISHED!")

    now = datetime.now()
    print(now.strftime('%H:%M:%S %p'))
    
    connection = True
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password!")
    else:
        print(f"\n{err}\n")


def main():
    if not connection:
        exec('quit()')
    to_user()
    while True:
        print("COMMAND|> ", end="")
        try:
            cmd = input()
            if "()" not in cmd:
                print("Not a valid command!")
            else:
                if cmd == "quit()":
                    bye()
                    break
                elif cmd == "help()":
                    exec('instructions()')
                else:
                    exec(cmd)
        except NameError:
            print("ERROR! Command not found!\n")
            continue
        except KeyboardInterrupt:
            print("\nSession forcefully closed by the user!\n")
            break


    cursor.close()
    cnx.close()


def show_db():
    try:
        command = f"SHOW DATABASES"
        cursor.execute(command)
        Table = from_db_cursor(cursor)
        Table.align = "l"
        print(Table)
        print("")
    except mysql.connector.Error as err:
        print(f"\n{err}\n")


def create_db():
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "\c" in database_name:
            print("Query cancelled, for creation of database.")
        else:
            command = f"CREATE DATABASE {database_name}"
            cursor.execute(command)
            cnx.commit()

            print(f"\nQuery OK, Created database '{database_name}'.\n")
    except mysql.connector.errors.ProgrammingError:
        print("\nError! Please enter values properly.\n")
    except mysql.connector.Error as err:
        print(f"\n{err}\n")
 

def delete_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "\c" in database_name:
                print("Query cancelled, for deletion of database.")
        else:
            command = f"DROP DATABASE {database_name}"
            cursor.execute(command)
            cnx.commit()
            
            if db == database_name:
                db = False
            
            print(f"\nQuery OK, Deleted database '{database_name}'.\n")
    except mysql.connector.Error as err:
        print("\nDatabase does not exist!\n")


def use_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "\c" in database_name:
                print("Query cancelled, for usage of database.")
        else:
            command = f"USE {database_name}"
            cursor.execute(command)

            db = database_name

            print(f"\nQuery OK, now using database '{database_name}'.\n")
    except mysql.connector.errors.ProgrammingError:
        print(f"\nERROR! Unable to find the requested database.\n")


def show_tb():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            command = f"SHOW TABLES"
            cursor.execute(command)
            Table = from_db_cursor(cursor)
            Table.align = "l"
            print(Table)
            print("")
        except mysql.connector.Error as err:
            print(f"\n{err}\n")


def create_tb():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> NAME OF TABLE TO BE CREATED: ")
            no_of_columns = int(input("       -> NO. OF COLUMNS: "))
            columns = ""
            for _ in range(no_of_columns - 1):
                column_value_type = input("       -> COLUMN NAME AND DATA-TYPE: ")
                columns += column_value_type + ', '

            column_value_type = input("       -> COLUMN NAME AND DATA-TYPE: ")
            columns += column_value_type

            print(columns)
            command = f"CREATE TABLE {table_name}({columns})"
            cursor.execute(command)
            cnx.commit()

            print(f"\nQuery OK, Created the '{table_name}' table.\n")
        except ValueError:
            print("\nERROR! Please insert values properly!\n")
        except mysql.connector.errors.ProgrammingError:
            print("\nERROR! You have an error in your syntax!\n")


def describe_tb():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            command = f"DESCRIBE {table_name}"
            cursor.execute(command)
            Table = from_db_cursor(cursor)
            Table.align = "l"
            print(Table)
            print("")
        except mysql.connector.Error as err:
            print(f"\n{err}\n")


def delete_tb():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("      -> NAME OF TABLE TO BE DELETED: ")
            
            command = f"DROP TABLE {table_name}"
            cursor.execute(command)
            cnx.commit()

            print(f"\nQuery OK, deleted the table ({table_name})\n")
        except mysql.connector.errors.ProgrammingError:
            print("\nERROR! Table not found!\n")
        except mysql.connector.Error as err:
            print(f"\n{err}\n")


def add_column():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column = input("       -> NEW COLUMN NAME AND DATA-TYPE: ")
            
            command = f"ALTER TABLE {table_name} ADD {column}"
            cursor.execute(command)
            cnx.commit()
            
            column_name = column.split()[0]
            data_type = column.split()[1]

            print(f"\nQuery OK, added column '{column_name}' with data-type '{data_type}' to the table '{table_name}'.\n")
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def delete_column():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column = input("       -> NAME OF COLUMN TO BE DELETED: ")
            
            command = f"ALTER TABLE {table_name} DROP {column}"
            cursor.execute(command)
            cnx.commit()
            print("")
        
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def modify_column():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column = input("       -> EXISTING COLUMN NAME: ")
            data_type = input("       -> NEW DATA-TYPE FOR THE COLUMN: ")
            
            command = f"ALTER TABLE {table_name} MODIFY {column}"
            cursor.execute(command)
            cnx.commit()
            
            print(f"\nQuery OK, modified column '{column}' to new data-type '{data_type}' in table '{table_name}'.\n")
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def insert():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column = input("       -> COLUMN NAMES: ")
            values = input("       -> VALUES: ")
            
            command = f"INSERT INTO {table_name} ({column}) VALUES ({values})"
            cursor.execute(command)
            cnx.commit()
            print("")
        
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.errors.DataError:
            print("Column count doesn't match value count")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def reveal():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            cursor.execute(f"SELECT * FROM {table_name}")
            Table = from_db_cursor(cursor)
            Table.align = "l"
            print(Table)
    
        except mysql.connector.errors.ProgrammingError:
            print(f"ERROR! Table not found!")
        except mysql.connector.Error as err:
                    print(f"\n{err}\n")


def update():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column_name = input("       -> COLUMN/FIELD TO BE CHECKED: ")
            value = input("       -> VALUE OF DATA-ITEM TO BE CHECKED: ")
            attribute = input("       -> COLUMN/FIELD TO BE UPDATED: ")
            updt_value = input("       -> VALUE OF DATA-ITEM TO BE UPDATED: ")

            if "NULL" in value:
                command = f"UPDATE {table_name} SET {attribute}={updt_value} WHERE {column_name} IS {value}"
            else:
                command = f"UPDATE {table_name} SET {attribute}={updt_value} WHERE {column_name}={value}" 
            cursor.execute(command)
            cnx.commit()
            print(f"\nQuery OK, updated the row(s)/record(s) in column/field ({attribute}) to {updt_value} where data-item in ({column_name}) = {value}.\n")
        
        except mysql.connector.errors.ProgrammingError:
            print("\nData not found!\n")
        except mysql.connector.Error as err:
            print(f"\n{err}\n")


def search():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column_name = input("       -> COLUMN NAME: ")
            value = input("       -> VALUE: ")

            if value == "NULL":
                command = f"SELECT * FROM {table_name} WHERE {column_name} IS {value}"
            else:
                command = f"SELECT * FROM {table_name} WHERE {column_name}={value}"
            cursor.execute(command)
            data = cursor.fetchall()
            if len(data) == 0:
                print("Data not present in the table")
            else:
                cursor.execute(command)
                Table = from_db_cursor(cursor)
                Table.align = "l"
                print(Table)
        
        except mysql.connector.errors.ProgrammingError:
            print("Data not found!")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def delete():
    if db == False:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            column_name = input("       -> COLUMN/FIELD NAME: ")
            value = input("       -> DATA-ITEM VALUE: ")

            if "NULL" in value:
                command = f"DELETE FROM {table_name} WHERE {column_name} IS {value}"
            else:
                command = f"DELETE FROM {table_name} WHERE {column_name}={value}" 
            cursor.execute(command)
            cnx.commit()
            print(f"Query OK, deleted the row(s)/record(s) containing the value {value}.")
        
        except mysql.connector.errors.ProgrammingError:
            print("Data not found!")
        except mysql.connector.Error as err:
                print(f"\n{err}\n")


def instructions():
    print("""
                                INSTRUCTIONS
                                ------------

COMMANDS FOR DATABASE MANIPULATION:

use_db()    > To use a database.
show_db()   > To show all of the databases.
create_db() > To create a new database.
delete_db() > To delete an existing database.
______________________________________________________________________________

COMMANDS FOR IN-TABLE QUERIES AND MANIPULATION:

insert() > To insert data into a specific table.
delete() > To delete a row.
reveal() > To show all of the data stored in the specific table.
search() > To search for a particular row in a table.
update() > To modify or change value of a data-item present in a coulmn/field.
______________________________________________________________________________

COMMANDS TO SHOW, CREATE AND DELETE TABLES:

show_tb()   > To show tables present in a database.
create_tb() > To create a new table.
delete_tb() > To delete a table completely.
______________________________________________________________________________

COMMAND TO EXIT THE PROGRAM:

quit() > To quit the program.
""")


def to_user():
    print(f"""
WELCOME TO SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)
Version: 1.9.7 (Beta)

Server version: {cnx.get_server_info()}
You are currently not connected to any database.

Commands end with ()

For help type 'help()'
""")


def bye():
    print("Closing...")
    time.sleep(1)
    print("Bye...\n")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    main()
