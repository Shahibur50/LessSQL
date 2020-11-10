"""
STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS)

version 1.7.5 (Beta)

Copyright (C) 2020  Shahibur Rahaman

Licensed under GNU GPLv3
"""

import mysql.connector
from mysql.connector import connection
from prettytable import PrettyTable
import time
from mysql.connector import errorcode
import getpass
from datetime import datetime

PT = PrettyTable()

connection = False

usr_name = input("USER-NAME: ")
db = input('DATABASE: ')
passwd = getpass.getpass()
host = input("HOST: ")
try:
    cnx = mysql.connector.connect(user=usr_name,
                                  database=db,
                                  password=passwd,
                                  host=host)
    cursor = cnx.cursor()
    print("Checking connectivity...")
    time.sleep(2)
    print("\nCONNECTION ESTABLISHED!")
    print("Server version:", db_Info := cnx.get_server_info())
    print("\nYou are connected to" + " '" + db + "' " "database.")
    
   

    now = datetime.now()
    print(now.strftime('%H: %M: %S %p'))
    
    connection = True
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


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
                    cursor.close()
                    cnx.close()
                    break
                else:
                    if cmd == "help()":
                        instructions()
                    else:
                        exec(cmd)
        except NameError:
            print("Command not found!\n")
            continue
        except KeyboardInterrupt:
            print("\nSession forcefully closed by the user!\n")
            break
    cursor.close()
    cnx.close()


def insert():
    try:
        table_name = input("TABLE NAME: ")
        column = input("COLUMN NAMES: ")
        values = input("VALUES: ")
        command = f"INSERT INTO {table_name} ({column}) VALUES ({values})"
        cursor.execute(command)
        cnx.commit()
        print("")
    except mysql.connector.errors.ProgrammingError:
        print("Something is wrong with your values!")


def create():
    try:
        table_name = input("NEW TABLE NAME: ")
        no_of_columns = int(input("NO. OF COLUMNS: "))
        columns = ""
        for _ in range(no_of_columns - 1):
            column_value_type = input("COLUMN NAME AND VALUE-TYPE: ")
            columns += column_value_type + ', '

        column_value_type = input("COLUMN NAME AND VALUE-TYPE: ")
        columns += column_value_type

        print(columns)
        command = f"CREATE TABLE {table_name}({columns})"
        cursor.execute(command)
        cnx.commit()
    except ValueError:
        print("Please insert values properly!")
    finally:
        print("")


def reveal():
    try:
        table_name = input("TABLE NAME: ")
        
        cursor.execute(f'DESC {table_name}')
        all_fields = cursor.fetchall()
        main_fields = [field[0] for field in all_fields]
        PT.field_names = main_fields

        cursor.execute(f"SELECT * FROM {table_name}")
        all_rows = cursor.fetchall()
        for rows in all_rows:
            PT.add_row(rows)
        
        print(PT)
        PT.clear_rows()

    except mysql.connector.errors.ProgrammingError:
        print("Table not found!")
    finally:
        print("")


def update():
    try:
        table_name = input("TABLE NAME: ")
        column_name = input("COLUMN/FIELD TO BE CHECKED: ")
        value = input("VALUE OF DATA-ITEM TO BE CHECKED: ")
        attribute = input("COLUMN/FIELD TO BE UPDATED: ")
        updt_value = input("VALUE OF DATA-ITEM TO BE UPDATED: ")

        if "NULL" in value:
            command = f"UPDATE {table_name} SET {attribute}={updt_value} WHERE {column_name} IS {value}"
        else:
            command = f"UPDATE {table_name} SET {attribute}={updt_value} WHERE {column_name}={value}"
        
        cursor.execute(command)
        cnx.commit()
        print(f"Query OK, updated the row(s)/record(s) in column/field {attribute} containing the data/value {value} to {updt_value}.")
    except mysql.connector.errors.ProgrammingError:
        print("Data not found!")
    finally:
        print("")


def search():
    try:
        table_name = input("TABLE NAME: ")
        column_name = input("COLUMN NAME: ")
        value = input("VALUE: ")
        
        cursor.execute(f'DESC {table_name}')
        all_fields = cursor.fetchall()
        main_fields = [field[0] for field in all_fields]
        PT.field_names = main_fields

        if value == "NULL":
            command = f"SELECT * FROM {table_name} WHERE {column_name} IS {value}"
        else:
            command = f"SELECT * FROM {table_name} WHERE {column_name}={value}"
        cursor.execute(command)
        rows = cursor.fetchall()
        sep_rows = rows[0]
        main_rows = [rows for rows in sep_rows]
        PT.add_row(main_rows)
        
        print(PT)
        PT.clear_rows()

    except mysql.connector.errors.ProgrammingError:
        print("Data not found!")
    finally:
        print("")



def delete():
    try:
        table_name = input("TABLE NAME: ")
        column_name = input("COLUMN/FIELD NAME: ")
        value = input("DATA-ITEM VALUE: ")

        if "NULL" in value:
            command = f"DELETE FROM {table_name} WHERE {column_name} IS {value}"
        else:
            command = f"DELETE FROM {table_name} WHERE {column_name}={value}"
        
        cursor.execute(command)
        cnx.commit()
        print(f"Query OK, deleted the row(s)/record(s) containing the value {value}.")
    except mysql.connector.errors.ProgrammingError:
        print("Data not found!")
    finally:
        print("")


def instructions():
    print("""
Usage instructions:

insert() : To insert data into a specific table.
create() : To create a new table.
delete() : To delete a row.
reveal() : To show all of the data stored in the specific table.
search() : To search for a particular row in a table.
update() : To modify or change value of a data-item present in a coulmn/field.
quit()   : To quit the program.
""")


def to_user():
    print("""
WELCOME TO STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS) :)
Version: 1.7.5 (Beta)
Commands end with ()

Copyright (C) 2020 Shahibur Rahaman

For details type 'details()'; For help type 'help()'
""")


def details():
    print("""
VERSION: 1.7.5 (Beta)
STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS)
Copyright (C) 2020 Shahibur Rahaman

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it,
under certain conditions.

Licensed under the GNU GPLv3 license
For license info visit: https://www.gnu.org/licenses/gpl-3.0.html
""")


def bye():
    print("Closing...")
    time.sleep(1)
    print("Bye...\n")

if __name__ == "__main__":
    main()
