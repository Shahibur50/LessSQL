"""
SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)

version 1.10.1 (Beta)

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
connection_status = False

for i in range(3):
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

        connection_status = True
        break
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password!")
            continue
        else:
            print(f"\n{error}\n")
            time.sleep(2)
            break


def main():
    if not connection_status:
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


def use_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "/c" in database_name:
            print("Query cancelled, for usage of database.")
        else:
            command = f"USE {database_name}"
            cursor.execute(command)

            db = database_name

            print(f"\nQuery OK, now using database '{database_name}'.\n")
    except mysql.connector.errors.ProgrammingError:
        print(f"\nERROR! Unable to find the requested database.\n")


def show_db():
    try:
        command = f"SHOW DATABASES"
        cursor.execute(command)
        table = from_db_cursor(cursor)
        table.align = "l"
        print(table)
        print("")
    except mysql.connector.Error as error:
        print(f"\n{error}\n")


def create_db():
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "/c" in database_name:
            print("Query cancelled, for creation of database.")
        else:
            command = f"CREATE DATABASE {database_name}"
            cursor.execute(command)
            cnx.commit()

            print(f"\nQuery OK, Created database '{database_name}'.\n")
    except mysql.connector.errors.ProgrammingError:
        print("\nError! Please enter values properly.\n")
    except mysql.connector.Error as error:
        print(f"\n{error}\n")


def delete_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "/c" in database_name:
            print("Query cancelled, for deletion of database.")
        else:
            opt = input(f"\n       -> IRREVERSIBLE CHANGE! Do you really want to delete the table '{database_name}'? (y/n) ")
            if opt == 'y' or opt == 'Y':
                command = f"DROP DATABASE {database_name}"
                cursor.execute(command)
                cnx.commit()
                if db == database_name:
                    db = False
                print(f"\nQuery OK, Deleted database '{database_name}'.\n")
            else:
                print("\nQuery cancelled, for deletion of database.\n")
    except mysql.connector.errors.ProgrammingError:
        print("\nERROR! Database not found!\n")
    except mysql.connector.Error as error:
        print(f"\n{error}\n")


def show_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            command = f"SHOW TABLES"
            cursor.execute(command)
            table = from_db_cursor(cursor)
            table.align = "l"
            print(table)
            print("")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def create_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> NAME OF TABLE TO BE CREATED: ")
            if "/c" in table_name:
                print("Query cancelled, for creation of table.")
            else:
                no_of_columns = input("       -> NO. OF COLUMNS: ")
                if "/c" in no_of_columns:
                    print("Query cancelled, for creation of table.")
                else:
                    no_of_columns = int(no_of_columns)
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
            print("\nERROR! Please enter values properly!\n")
        except mysql.connector.errors.ProgrammingError:
            print("\nERROR! You have an error in your syntax!\n")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def describe_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("Query cancelled, for schema of table.")
            else:
                command = f"DESCRIBE {table_name}"
                cursor.execute(command)
                table = from_db_cursor(cursor)
                table.align = "l"
                print(table)
                print("")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def delete_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("      -> NAME OF TABLE TO BE DELETED: ")
            if "/c" in table_name:
                print("Query cancelled, for schema of table.")
            else:
                opt = input(f"\n      -> IRREVERSIBLE CHANGE! Do you really want to delete the table '{table_name}'? (y/n)\n")
                if opt == 'y' or opt == 'Y':
                    command = f"DROP TABLE {table_name}"
                    cursor.execute(command)
                    cnx.commit()

                    print(f"\nQuery OK, deleted the table ({table_name})\n")
                else:
                    print("\nQuery cancelled, for deletion of table.\n")
        except mysql.connector.errors.ProgrammingError:
            print("\nERROR! Table not found!\n")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def add_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("Query cancelled, for creation of database.")
            else:
                column = input("       -> NEW COLUMN NAME AND DATA-TYPE: ")
                if "/c" in column:
                    print("Query cancelled, for creation of database.")
                else:
                    command = f"ALTER TABLE {table_name} ADD {column}"
                    cursor.execute(command)
                    cnx.commit()

                    column_name = column.split()[0]
                    data_type = column.split()[1]

                    print(
                        f"\nQuery OK, added column '{column_name}' with data-type '{data_type}' to the table '{table_name}'.\n")
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def modify_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            else:
                column = input("       -> EXISTING COLUMN NAME: ")
                if "/c" in column:
                    print("\nQuery cancelled, for modification of table.\n")
                else:
                    data_type = input("       -> NEW DATA-TYPE FOR THE COLUMN: ")
                    if "/c" in data_type:
                        print("\nQuery cancelled, for modification of table.\n")
                    else:
                        command = f"ALTER TABLE {table_name} MODIFY {column} {data_type}"
                        cursor.execute(command)
                        cnx.commit()

                        print(f"\nQuery OK, modified column '{column}' to new data-type '{data_type}' in table '{table_name}'.\n")
        except mysql.connector.errors.ProgrammingError:
            print("Syntax Error!")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def delete_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            else:
                column = input("       -> NAME OF COLUMN TO BE DELETED: ")
                if "/c" in column:
                    print("\nQuery cancelled, for modification of table.\n")
                else:
                    command = f"ALTER TABLE {table_name} DROP {column}"
                    cursor.execute(command)
                    cnx.commit()
                    
                    print(f"\nQuery OK, Deleted column '{column}' from table '{table_name}'.\n")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def reveal():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            else:
                cursor.execute(f"SELECT * FROM {table_name}")
                table = from_db_cursor(cursor)
                table.align = "l"
                print(table)

        except mysql.connector.errors.ProgrammingError:
            print(f"ERROR! Table not found!")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def insert():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            else:
                column = input("       -> COLUMN NAMES: ")
                if "/c" in column:
                    print("\nQuery cancelled, for modification of table.\n")
                else:
                    values = input("       -> VALUES: ")
                    if "/c" in values:
                        print("\nQuery cancelled, for modification of table.\n")
                    else:
                        command = f"INSERT INTO {table_name} ({column}) VALUES ({values})"
                        cursor.execute(command)
                        cnx.commit()
                        print("")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def update():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for updatation of table.\n")
            else:
                condition = input("       -> CONDITION: ")
                if "/c" in condition:
                    print("\nQuery cancelled, for updatation of table.\n")
                else:
                    attribute = input("       -> COLUMN/FIELD TO BE UPDATED: ")
                    if "/c" in attribute:
                        print("\nQuery cancelled, for updatation of table.\n")
                    else:
                        updated_value = input("       -> VALUE OF DATA-ITEM TO BE UPDATED: ")
                        if "/c" in updated_value:
                            print("\nQuery cancelled, for updatation of table.\n")
                        else:
                            command = f"UPDATE {table_name} SET {attribute}={updated_value} WHERE {condition}"
                            cursor.execute(command)
                            cnx.commit()
                            print(f"\nQuery OK, updated the row(s)/record(s) in column/field ({attribute}) to {updated_value} where "
                                f"condition '{condition}' was satisfied.\n")

        except mysql.connector.errors.ProgrammingError:
            print("\nData not found!\n")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def search():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for searching of row(s) table.\n")
            else:
                column_name = input("       -> COLUMN NAME: ")
                if "/c" in table_name:
                    print("\nQuery cancelled, for updatation of table.\n")
                else:
                    value = input("       -> VALUE: ")
                    if "/c" in table_name:
                        print("\nQuery cancelled, for updatation of table.\n")
                    else:
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
                            table = from_db_cursor(cursor)
                            table.align = "l"
                            print(table)
                            print("")

        except mysql.connector.errors.ProgrammingError:
            print("Data not found!")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def delete():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for searching of row(s) table.\n")
            else:
                column_name = input("       -> COLUMN/FIELD NAME: ")
                if "/c" in table_name:
                    print("\nQuery cancelled, for searching of row(s) table.\n")
                else:
                    value = input("       -> DATA-ITEM VALUE: ")
                    if "/c" in table_name:
                        print("\nQuery cancelled, for searching of row(s) table.\n")
                    else:
                        if "NULL" in value:
                            command = f"DELETE FROM {table_name} WHERE {column_name} IS {value}"
                        else:
                            command = f"DELETE FROM {table_name} WHERE {column_name}={value}"
                            cursor.execute(command)
                            cnx.commit()
                            
                            print(f"\nQuery OK, deleted the row(s)/record(s) containing the value {value}.\n")
        except mysql.connector.errors.ProgrammingError:
            print("Data not found!")
        except mysql.connector.Error as error:
            print(f"\n{error}\n")


def instructions():
    print("""
                                INSTRUCTIONS
                                ------------

COMMANDS FOR DATABASE MANIPULATION:

use_db()    > To use a database.
show_db()   > To show all of the databases.
create_db() > To create a new database.
delete_db() > To delete an existing database.

_______________________________________________________________________________
_______________________________________________________________________________

COMMANDS FOR TABLE MANIPULATION:

show_tb()     > To show tables present in a database.
create_tb()   > To create a new table.
describe_tb() > To see the schema(structure) of a table.
delete_tb()   > To delete a table completely.

_______________________________________________________________________________
_______________________________________________________________________________

COMMANDS FOR COLUMN MANIPULATION:

add_column()    > To add a new column to an existing table.
modify_column() > To change data-type of a column in a table.
delete_column() > To delete an exiting column inside a table.

_______________________________________________________________________________
_______________________________________________________________________________

COMMANDS FOR IN-TABLE QUERIES:

reveal() > To show all of the data stored in a specific table.
search() > To search for a particular row in a table.

_______________________________________________________________________________
_______________________________________________________________________________

COMMANDS FOR  IN-TABLE MANIPULATION:

insert() > To insert data in a table.
update() > To modify or change value of a data-item present in a column/field.
delete() > To delete row(s)/record(s).

_______________________________________________________________________________
_______________________________________________________________________________

COMMAND TO EXIT THE PROGRAM:

quit() > To quit the program.
""")


def to_user():
    print(f"""
WELCOME TO SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)
Version: 1.10.1 (Beta)

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
