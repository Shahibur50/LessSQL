"""
School Database Management System (SDBMS)
Version: 2.15.11
Copyright (C) 2020 Shahibur Rahaman

Licensed under GNU GPLv3
"""

import mysql.connector
import sys
import time
import getpass
from mysql.connector import errorcode
from prettytable import PrettyTable
from prettytable import from_db_cursor
from datetime import datetime

NO_DB_COMMANDS = ["use_db;", "show_db;", "create_db;", "delete_db;", "exit;", "show_w;", "show_c;"]

DB_COMMANDS = ["show_tb;", "create_tb;", "describe_tb;", "delete_tb;", "add_column;", "modify_column;",
               "delete_column;", "reveal;", "search;", "insert;", "update;", "delete;"]

HELP_COMMANDS = ["help;", "/h", "?"]

PT = PrettyTable()

is_connection = False
db = None
cursor = None
cnx = None
cmd = None


def main():
    global cmd
    connector()
    if is_connection:
        to_user()  # Showing the user info related to the program
        while True:
            print("COMMAND|> ", end="")
            try:
                cmd = input()
                execute(cmd)
            except EOFError:
                continue
            except KeyboardInterrupt:
                print("\nSession forcefully closed by the user!\n")
                break
        cursor.close()
        cnx.close()
    else:
        print("Please check if the server is online.")
        close()


def connector():
    global is_connection, db, cursor, cnx

    for _ in range(3):
        try:
            usr_name = input("USER-NAME: ")
            passwd = getpass.getpass()
            host = "localhost"
        except EOFError:
            print("")
            continue

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
            is_connection = True
            break
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password!\n")
                continue
            print(f"\n{err}\n")
            time.sleep(2)
            break
    else:
        print("Wrong credentials entered 3 times.")
        print("Exiting...\n")
        time.sleep(2)
        sys.exit()


def is_valid(command):
    valid = False
    if len(command) == 0:
        print("ERROR! Please enter values properly!")
    elif ";" not in command:
        print("ERROR! Not a valid command!")
    elif command not in NO_DB_COMMANDS and command not in DB_COMMANDS:
        print("Command not found!")
    else:
        valid = True
    return valid


def execute(command):
    if is_valid(command) and command in NO_DB_COMMANDS and not db:
        run(command)
    elif is_valid(command) and command in DB_COMMANDS and db:
        run(command)
    elif is_valid(command) and command in DB_COMMANDS and not db:
        print("\nERROR! No database is in use!\n")
    else:
        print("UNEXPECTED ERROR!")


def run(command):
    if command == "use_db;":
        use_db()
    elif command == "show_db;":
        show_db()
    elif command == "create_db;":
        create_db()
    elif command == "delete_db;":
        delete_db()
    elif command == "show_tb;":
        show_tb()
    elif command == "create_tb;":
        create_tb()
    elif command == "describe_tb;":
        describe_tb()
    elif command == "delete_tb;":
        delete_tb()
    elif command == "add_column;":
        add_column()
    elif command == "modify_column;":
        modify_column()
    elif command == "delete_column;":
        delete_column()
    elif command == "reveal;":
        reveal()
    elif command == "insert;":
        insert()
    elif command == "update;":
        update()
    elif command == "delete;":
        delete()
    elif command == "exit" or command == "exit;":
        close()
    elif command == "show_w;":
        show_w()
    elif command == "show_c;":
        show_c()
    elif command in HELP_COMMANDS:
        program_help()


def check(variable_to_check):
    """
    Function to check whether the user
    cancelled the input statement or has
    given no input at all.
    :param variable_to_check:
    :return: next_step
    """
    take_next_step = True  # Boolean variable to check and make the program process further ahead.

    if "/c" in variable_to_check:
        print("\nQuery cancelled!\n")
        take_next_step = False
    elif len(variable_to_check) == 0:
        take_next_step = False
        print("\nPlease enter values properly!\n")

    return take_next_step


def use_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if check(database_name):
            command = f"USE {database_name}"
            cursor.execute(command)
            db = database_name
            print(f"\nQuery OK, now using database '{database_name}'.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def show_db():
    try:
        command = "SHOW DATABASES"
        cursor.execute(command)
        table = from_db_cursor(cursor)
        table.align = "l"
        print(table, "\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def create_db():
    try:
        database_name = input("       -> DATABASE NAME: ")
        if check(database_name):
            command = f"CREATE DATABASE {database_name}"
            cursor.execute(command)
            cnx.commit()
            print(f"\nQuery OK, Created database '{database_name}'.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def delete_db():
    global db
    try:
        database_name = input("       -> DATABASE NAME: ")
        if check(database_name):
            opt = input(f"\n       -> IRREVERSIBLE CHANGE! Do you really want to delete the database "
                        f"'{database_name}'? (y/n) ")
            if opt in ('y', 'Y'):
                command = f"DROP DATABASE {database_name}"
                cursor.execute(command)
                cnx.commit()
                if db == database_name:
                    db = False
                print(f"\nQuery OK, Deleted database ({database_name}).\n")
            else:
                print(f"\nQuery cancelled, for deletion of the database ({database_name}).\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def show_tb():
    try:
        command = "SHOW TABLES"
        cursor.execute(command)
        table = from_db_cursor(cursor)
        table.align = "l"
        print(table, "\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def create_tb():
    try:
        table_name = input("       -> NAME OF TABLE TO BE CREATED: ")
        if check(table_name):
            no_of_columns = input("       -> NO. OF COLUMNS: ")
            if check(no_of_columns):
                no_of_columns = int(no_of_columns)
                columns = ""
                column_num = 0

                for column_num in range(1, no_of_columns):
                    column_value_type = input(
                        f"       -> COLUMN ({column_num}) NAME AND DATA-TYPE: ")
                    if check(column_value_type):
                        columns += column_value_type + ', '
                column_value_type = input(f"       -> COLUMN ({column_num + 1}) NAME AND DATA-TYPE: ")

                if check(column_value_type):
                    columns += column_value_type
                    primary_key = input("       -> PRIMARY KEY: ")
                    if check(primary_key):
                        command = f"CREATE TABLE {table_name}({columns}, PRIMARY KEY ({primary_key}))"
                        cursor.execute(command)
                        cnx.commit()
                        print(f"\nQuery OK, Created table ({table_name}).\n")
    except ValueError:
        print("\nERROR! Please enter values properly!\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def describe_tb():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            command = f"DESCRIBE {table_name}"
            cursor.execute(command)
            table = from_db_cursor(cursor)
            table.align = "l"
            print(table)
            print("")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def delete_tb():
    try:
        table_name = input("      -> NAME OF TABLE TO BE DELETED: ")
        if check(table_name):
            opt = input(f"\n      -> IRREVERSIBLE CHANGE! Do you really want to delete the"
                        f" table '{table_name}'? (y/n) ")
            if opt in ('y', 'Y'):
                command = f"DROP TABLE {table_name}"
                cursor.execute(command)
                cnx.commit()
                print(f"\nQuery OK, deleted the table ({table_name})\n")
            else:
                print("\nQuery cancelled, for deletion of table.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def add_column():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_data = input(
                "       -> NEW COLUMN NAME AND DATA-TYPE: ")
            if check(column_data):
                command = f"ALTER TABLE {table_name} ADD {column_data}"
                cursor.execute(command)
                cnx.commit()

                column_name = column_data.split()[0]
                data_type = column_data.split()[1]

                print(f"\nQuery OK, added column '{column_name}' with data-type '{data_type}'"
                      f" to the table '{table_name}'.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def modify_column():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_name = input("       -> EXISTING COLUMN NAME: ")
            if check(column_name):
                data_type = input(
                    "       -> NEW DATA-TYPE FOR THE COLUMN: ")
                if check(data_type):
                    command = f"ALTER TABLE {table_name} MODIFY {column_name} {data_type}"
                    cursor.execute(command)
                    cnx.commit()
                    print(f"\nQuery OK, modified column ({column_name}) to new data-type ({data_type})"
                          f" in table ({table_name}).\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def delete_column():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_name = input("       -> NAME OF COLUMN TO BE DELETED: ")
            if check(column_name):
                opt = input(f"\n      -> IRREVERSIBLE CHANGE! Do you really want to delete the column "
                            f"({column_name})? (y/n) ")
                if opt in ('y', 'Y'):
                    command = f"ALTER TABLE {table_name} DROP {column_name}"
                    cursor.execute(command)
                    cnx.commit()
                    print(f"\nQuery OK, Deleted column ({column_name}) from table ({table_name}).\n")
                else:
                    print("\nQuery cancelled, for deletion of column.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def reveal():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            cursor.execute(f"SELECT * FROM {table_name}")
            table = from_db_cursor(cursor)
            table.align = "l"
            print(table)
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def insert():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_name = input("       -> COLUMN NAMES: ")
            if check(column_name):
                values = input("       -> VALUES: ")
                if check(values):
                    command = f"INSERT INTO {table_name} ({column_name}) VALUES ({values})"
                    cursor.execute(command)
                    cnx.commit()
                    print(f"\nQuery OK, inserted value(s) ({values}) in column(s) ({column_name})"
                          f" in table ({table_name})\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def update():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            condition = input("       -> CONDITION: ")
            if check(condition):
                attribute = input("       -> COLUMN/FIELD TO BE UPDATED: ")
                if check(attribute):
                    updated_value = input(
                        "       -> VALUE OF DATA-ITEM TO BE UPDATED: ")
                    if check(updated_value):
                        command = f"UPDATE {table_name} SET {attribute}={updated_value} WHERE {condition}"
                        cursor.execute(command)
                        cnx.commit()
                        print(f"\nQuery OK, updated the row(s)/record(s) in column/field ({attribute})"
                              f" to ({updated_value}) where condition ({condition}) was satisfied.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def search():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_name = input("       -> COLUMN NAME: ")
            if check(column_name):
                value = input("       -> VALUE: ")
                if check(value):
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
                        print(table, "\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def delete():
    try:
        table_name = input("       -> TABLE NAME: ")
        if check(table_name):
            column_name = input("       -> COLUMN/FIELD NAME: ")
            if check(column_name):
                value = input("       -> DATA-ITEM VALUE: ")
                if check(value):
                    if "NULL" in value:
                        command = f"DELETE FROM {table_name} WHERE {column_name} IS {value}"
                    else:
                        command = f"DELETE FROM {table_name} WHERE {column_name}={value}"
                    cursor.execute(command)
                    cnx.commit()
                    print(f"\nQuery OK, deleted the row(s)/record(s) containing the value {value}.\n")
    except mysql.connector.Error as err:
        err = str(err.msg).split("; ")[0]
        print(f"\nERROR! {err}\n")


def close():
    print("Exiting...")
    time.sleep(1)
    print("Bye...\n")


def program_help():
    print("""
                                INSTRUCTIONS
                                ------------

COMMANDS FOR DATABASE MANIPULATION:

use_db()    > To use a database.
show_db()   > To show all of the databases.
create_db() > To create a new database.
delete_db() > To delete an existing database.

____________________________________________________________________________________
____________________________________________________________________________________

COMMANDS FOR TABLE MANIPULATION:

show_tb()     > To show tables present in a database.
create_tb()   > To create a new table.
describe_tb() > To see the schema(structure) of a table.
delete_tb()   > To delete a table completely.

____________________________________________________________________________________
____________________________________________________________________________________

COMMANDS FOR COLUMN MANIPULATION:

add_column()    > To add a new column to an existing table.
modify_column() > To change data-type of a column in a table.
delete_column() > To delete an exiting column inside a table.

____________________________________________________________________________________
____________________________________________________________________________________

COMMANDS FOR IN-TABLE QUERIES:

reveal() > To show all of the data stored in a specific table.
search() > To search for a particular row in a table.

____________________________________________________________________________________
____________________________________________________________________________________

COMMANDS FOR  IN-TABLE MANIPULATION:

insert() > To insert data in a table.
update() > To modify or change value of a data-item present in a column/field.
delete() > To delete row(s)/record(s).

____________________________________________________________________________________
____________________________________________________________________________________

COMMAND TO EXIT THE PROGRAM:

exit() > To quit the program.

------------------------------------------------------------------------------------
For more help visit: https://github.com/Shahibur50/School_DataBase_Management_System
------------------------------------------------------------------------------------
""")


def to_user():
    print("""
+-----------------------------------------------------------------+
| WELCOME TO SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)            |  
| Version: 2.15.11                                                |
|                                                                 |
| Copyright (C) 2020  Shahibur Rahaman                            |
|                                                                 |
| This program comes with ABSOLUTELY NO WARRANTY;                 |
| for details type show_w()                                       |
| This is free software, and you are welcome to redistribute it   |
| under certain conditions; type show_c() for details.            |
|                                                                 |
| For more info visit:                                            |
| https://github.com/Shahibur50/School_DataBase_Management_System |
|                                                                 |
| Commands end with ()                                            |
|                                                                 |
| To cancel any input statement type /c                           |
|                                                                 |
| For help type help(); To exit the program type exit()           |
+-----------------------------------------------------------------+
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
