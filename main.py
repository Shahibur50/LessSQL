"""
STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS)

version 1.8.6 (Beta)

Copyright (C) 2020  Shahibur Rahaman

Licensed under GNU GPLv3
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
db = input('DATABASE: ')
passwd = getpass.getpass()
host = "localhost"

try:
    cnx = mysql.connector.connect(user=usr_name,
                                  database=db,
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
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist!")
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


def show_tb():
    command = f"SHOW TABLES"
    cursor.execute(command)
    Table = from_db_cursor(cursor)
    Table.align = "l"
    print(Table)
    print("")


def create_tb():
    try:
        table_name = input("       -> NAME OF TABLE TO BE CREATED: ")
        no_of_columns = int(input("      -> NO. OF COLUMNS: "))
        columns = ""
        for _ in range(no_of_columns - 1):
            column_value_type = input("       -> COLUMN NAME AND VALUE-TYPE: ")
            columns += column_value_type + ', '

        column_value_type = input("       -> COLUMN NAME AND VALUE-TYPE: ")
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


def delete_tb():
    try:
        table_name = input("      -> NAME OF TABLE TO BE DELETED: ")
        
        command = f"DROP TABLE {table_name}"
        cursor.execute(command)
        cnx.commit()

        print(f"\nQuery OK, deleted the table ({table_name})\n")
    except mysql.connector.errors.ProgrammingError:
        print("\nERROR! Table not found!\n")


def insert():
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


def reveal():
    try:
        table_name = input("       -> TABLE NAME: ")
        cursor.execute(f"SELECT * FROM {table_name}")
        
        Table = from_db_cursor(cursor)
        Table.align = "l"
        print(Table)
    
    except mysql.connector.errors.ProgrammingError:
        print(f"ERROR! Table not found!")


def update():
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



def search():
    try:
        table_name = input("       -> TABLE NAME: ")
        column_name = input("       -> COLUMN NAME: ")
        value = input("VALUE: ")

        if value == "NULL":
            command = f"SELECT * FROM {table_name} WHERE {column_name} IS {value}"
        else:
            command = f"SELECT * FROM {table_name} WHERE {column_name}={value}"
        cursor.execute(command)
        Table = from_db_cursor(cursor)
        Table.align = "l"
        print(Table)
    
    except mysql.connector.errors.ProgrammingError:
        print("Data not found!")
    finally:
        print("")



def delete():
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
    finally:
        print("")


def instructions():
    print("""
                                  INSTRUCTIONS
                                  ------------

COMMANDS FOR SOFTWARE INFO:

show_w() > Warranty info for this software.
show_c() > Terms and conditions for redistribution of this software
show_v() > To show info related to this software.
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
Version: 1.8.6 (Beta)

Copyright (C) 2020 Shahibur Rahaman

This program comes with ABSOLUTELY NO WARRANTY; for details type `show_w()'.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'show_c()' for details.

Server version: {cnx.get_server_info()}
You are connected to'{db}' database

Commands end with ()

For program info type 'version()'; For help type 'help()'
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

IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

For license info visit: https://www.gnu.org/licenses/gpl-3.0.html
""")


def show_c():
    print("""
All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

For license info visit: https://www.gnu.org/licenses/gpl-3.0.html
""")

def show_v():
    print("""
VERSION: 1.8.6 (Beta)
SCHOOL DATABASE MANAGEMENT SYSTEM (SDBMS)

Copyright (C) 2020  Shahibur Rahaman
License GPLv3+: GNU GPL version 3 or later

This program is a database management system based on MySQL, with a goal
to simplify the usage of a RDBMS for record keeping of students in schools.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For license info visit: https://www.gnu.org/licenses/gpl-3.0.html
""")


def bye():
    print("Closing...")
    time.sleep(1)
    print("Bye...\n")

if __name__ == "__main__":
    main()
