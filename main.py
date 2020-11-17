"""
SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)

version 2.10.11

"""
import mysql.connector
import time
import getpass
from mysql.connector import connection
from mysql.connector import errorcode
from prettytable import PrettyTable
from prettytable import from_db_cursor
from datetime import datetime


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
        print(f"\nLOGGED IN AS: {usr_name}@{host}")
        now = datetime.now()
        print(f"TIME: {now.strftime('%H:%M:%S %p')}")
        print(f"\nServer version: {cnx.get_server_info()}") 
        connection_status = True
        break
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password!\n")
            continue
        else:
            print(f"\n{error}\n")
            time.sleep(2)
            break
else:
    print("Wrong credentials entered 3 times.")
    print("Exiting...\n")
    time.sleep(2)
    quit()


def main():
    to_user()
    while True:
        print("COMMAND|> ", end="")
        try:
            cmd = input()
            if "()" not in cmd:
                print("Not a valid command!")
            else:
                if cmd == "exit()":
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
        elif not database_name:
            print("\nPlease enter values properly!\n")
        else:
            command = f"USE {database_name}"
            cursor.execute(command)

            db = database_name

            print(f"\nQuery OK, now using database '{database_name}'.\n")
    except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def show_db():
    try:
        command = f"SHOW DATABASES"
        cursor.execute(command)
        table = from_db_cursor(cursor)
        table.align = "l"
        print(table)
        print("")
    except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def create_db():
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "/c" in database_name:
            print("Query cancelled, for creation of database.")
        elif not database_name:
                print("\nPlease enter values properly!\n")
        else:
            command = f"CREATE DATABASE {database_name}"
            cursor.execute(command)
            cnx.commit()

            print(f"\nQuery OK, Created database '{database_name}'.\n")
    except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def delete_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if "/c" in database_name:
            print("Query cancelled, for deletion of database.")
        elif not database_name:
                print("\nPlease enter values properly!\n")
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
    except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


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
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def create_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> NAME OF TABLE TO BE CREATED: ")
            if "/c" in table_name:
                print("Query cancelled, for creation of table.")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                no_of_columns = input("       -> NO. OF COLUMNS: ")
                if "/c" in no_of_columns:
                    print("Query cancelled, for creation of table.")
                elif not no_of_columns:
                    print("\nPlease enter values properly!\n")
                else:
                    no_of_columns = int(no_of_columns)
                    columns = ""
                    for i in range(1, no_of_columns):
                        column_value_type = input(f"       -> COLUMN ({i}) NAME AND DATA-TYPE: ")
                        if "/c" in column_value_type:
                            print("Query cancelled, for creation of table.")
                        elif not column_value_type:
                            print("\nPlease enter values properly!\n")
                        else:
                            columns += column_value_type + ', '

                    column_value_type = input(f"       -> COLUMN ({i + 1}) NAME AND DATA-TYPE: ")
                    if "/c" in column_value_type:
                        print("Query cancelled, for creation of table.")
                    elif not column_value_type:
                        print("\nPlease enter values properly!\n")
                    else:
                        columns += column_value_type
                
                        primary_key = input("       -> PRIMARY KEY: ")
                        if "/c" in primary_key:
                            print("Query cancelled, for creation of table.")
                        elif not primary_key:
                            print("\nPlease enter values properly!\n") 
                        else:
                            command = f"CREATE TABLE {table_name}({columns}, PRIMARY KEY ({primary_key}))"
                            print(command)
                            cursor.execute(command)
                            cnx.commit()

                            print(f"\nQuery OK, Created the '{table_name}' table.\n")
        except ValueError:
            print("\nERROR! Please enter values properly!\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def describe_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("Query cancelled, for schema of table.")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                command = f"DESCRIBE {table_name}"
                cursor.execute(command)
                table = from_db_cursor(cursor)
                table.align = "l"
                print(table)
                print("")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def delete_tb():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("      -> NAME OF TABLE TO BE DELETED: ")
            if "/c" in table_name:
                print("Query cancelled, for schema of table.")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                opt = input(f"\n      -> IRREVERSIBLE CHANGE! Do you really want to delete the table '{table_name}'? (y/n) ")
                if opt == 'y' or opt == 'Y':
                    command = f"DROP TABLE {table_name}"
                    cursor.execute(command)
                    cnx.commit()

                    print(f"\nQuery OK, deleted the table ({table_name})\n")
                else:
                    print("\nQuery cancelled, for deletion of table.\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def add_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("Query cancelled, for creation of database.")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column = input("       -> NEW COLUMN NAME AND DATA-TYPE: ")
                if "/c" in column:
                    print("Query cancelled, for creation of database.")
                elif not column:
                    print("\nPlease enter values properly!\n")
                else:
                    command = f"ALTER TABLE {table_name} ADD {column}"
                    cursor.execute(command)
                    cnx.commit()

                    column_name = column.split()[0]
                    data_type = column.split()[1]

                    print(f"\nQuery OK, added column '{column_name}' with data-type '{data_type}' to the table '{table_name}'.\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def modify_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column = input("       -> EXISTING COLUMN NAME: ")
                if "/c" in column:
                    print("\nQuery cancelled, for modification of table.\n")
                elif not column:
                    print("\nPlease enter values properly!\n")
                else:
                    data_type = input("       -> NEW DATA-TYPE FOR THE COLUMN: ")
                    if "/c" in data_type:
                        print("\nQuery cancelled, for modification of table.\n")
                    elif not data_type:
                        print("\nPlease enter values properly!\n")
                    else:
                        command = f"ALTER TABLE {table_name} MODIFY {column} {data_type}"
                        cursor.execute(command)
                        cnx.commit()

                        print(f"\nQuery OK, modified column '{column}' to new data-type '{data_type}' in table '{table_name}'.\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def delete_column():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column = input("       -> NAME OF COLUMN TO BE DELETED: ")
                if "/c" in column:
                    print("\nQuery cancelled, for modification of table.\n")
                elif not column:
                    print("\nPlease enter values properly!\n")
                else:
                    opt = input(f"\n      -> IRREVERSIBLE CHANGE! Do you really want to delete the table '{table_name}'? (y/n) ")
                    if opt == 'y' or opt == 'Y':
                        command = f"ALTER TABLE {table_name} DROP {column}"
                        cursor.execute(command)
                        cnx.commit()
                    
                        print(f"\nQuery OK, Deleted column '{column}' from table '{table_name}'.\n")
                    else:
                        print("\nQuery cancelled, for deletion of table.\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def reveal():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                cursor.execute(f"SELECT * FROM {table_name}")
                table = from_db_cursor(cursor)
                table.align = "l"
                print(table)

        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def insert():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for modification of table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column_name = input("       -> COLUMN NAMES: ")
                if "/c" in column_name:
                    print("\nQuery cancelled, for modification of table.\n")
                elif not column_name:
                    print("\nPlease enter values properly!\n")
                else:
                    values = input("       -> VALUES: ")
                    if "/c" in values:
                        print("\nQuery cancelled, for modification of table.\n")
                    elif not values:
                        print("\nPlease enter values properly!\n")
                    else:
                        command = f"INSERT INTO {table_name} ({column_name}) VALUES ({values})"
                        cursor.execute(command)
                        cnx.commit()
                        print(f"\nQuery OK, inserted value(s) '{values}' in column(s) '{column_name}' in table '{table_name}'\n")
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
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                condition = input("       -> CONDITION: ")
                if "/c" in condition:
                    print("\nQuery cancelled, for updatation of table.\n")
                elif not condition:
                    print("\nPlease enter values properly!\n")
                else:
                    attribute = input("       -> COLUMN/FIELD TO BE UPDATED: ")
                    if "/c" in attribute:
                        print("\nQuery cancelled, for updatation of table.\n")
                    elif not attribute:
                        print("\nPlease enter values properly!\n")
                    else:
                        updated_value = input("       -> VALUE OF DATA-ITEM TO BE UPDATED: ")
                        if "/c" in updated_value:
                            print("\nQuery cancelled, for updatation of table.\n")
                        elif not updated_value:
                            print("\nPlease enter values properly!\n")
                        else:
                            command = f"UPDATE {table_name} SET {attribute}={updated_value} WHERE {condition}"
                            cursor.execute(command)
                            cnx.commit()
                            print(f"\nQuery OK, updated the row(s)/record(s) in column/field ({attribute}) to {updated_value} where "
                                f"condition '{condition}' was satisfied.\n")

        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def search():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for searching of row(s) table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column_name = input("       -> COLUMN NAME: ")
                if "/c" in column_name:
                    print("\nQuery cancelled, for updatation of table.\n")
                elif not column_name:
                    print("\nPlease enter values properly!\n")
                else:
                    value = input("       -> VALUE: ")
                    if "/c" in value:
                        print("\nQuery cancelled, for updatation of table.\n")
                    elif not value:
                        print("\nPlease enter values properly!\n")
                    else:
                        if value == "NULL":
                            command = f"SELECT * FROM {table_name} WHERE {column_name} IS {value}"
                        else:
                            command = f"SELECT * FROM {table_name} WHERE {column_name}={value}"
                        cursor.execute(command)
                        data = cursor.fetchall()
                        if len(data) == 0:
                            print("Data not present in the table!")
                        else:
                            cursor.execute(command)
                            table = from_db_cursor(cursor)
                            table.align = "l"
                            print(table)
                            print("")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def delete():
    if not db:
        print("\nNo database is in use!\n")
    else:
        try:
            table_name = input("       -> TABLE NAME: ")
            if "/c" in table_name:
                print("\nQuery cancelled, for searching of row(s) table.\n")
            elif not table_name:
                print("\nPlease enter values properly!\n")
            else:
                column_name = input("       -> COLUMN/FIELD NAME: ")
                if "/c" in column_name:
                    print("\nQuery cancelled, for searching of row(s) table.\n")
                elif not column_name:
                    print("\nPlease enter values properly!\n")
                else:
                    value = input("       -> DATA-ITEM VALUE: ")
                    if "/c" in value:
                        print("\nQuery cancelled, for searching of row(s) table.\n")
                    elif not value:
                        print("\nPlease enter values properly!\n")
                    else:
                        if "NULL" in value:
                            command = f"DELETE FROM {table_name} WHERE {column_name} IS {value}"
                        else:
                            command = f"DELETE FROM {table_name} WHERE {column_name}={value}"
                            cursor.execute(command)
                            cnx.commit()
                            
                            print(f"\nQuery OK, deleted the row(s)/record(s) containing the value {value}.\n")
        except mysql.connector.Error as error:
            err = str(error.msg).split("; ")[0]
            print(f"\nERROR! {err}\n")


def bye():
    print("Closing...")
    time.sleep(1)
    print("Bye...\n")
    cursor.close()
    cnx.close()


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

exit() > To quit the program.
""")


def to_user():
    print("""
+----------------------------------------------------------------+
| WELCOME TO SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)           |
| Version: 2.10.11                                               |
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
""")


def show_w():
    print("""
THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

For license info visit: https://www.gnu.org/licenses/
""")


def show_c():
    print("""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

For license info visit: https://www.gnu.org/licenses/
""")


if __name__ == "__main__":
    main()
