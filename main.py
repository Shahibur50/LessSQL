import mysql.connector
from prettytable import PrettyTable
import time

PT = PrettyTable()

cnx = mysql.connector.connect(host="localhost",
                              user="root",
                              passwd="hornbill",
                              database="project")
cursor = cnx.cursor()


def main():
    to_user()
    
    while True:
        print("COMMAND: ", end="")
        try:
            cmd = input()
            if "()" not in cmd:
                print("Not a valid command!")
            else:
                if cmd == "quit()":
                    quit()
                    break
                else:
                    exec(cmd)
        except NameError:
            print("Command not found!\n")
            continue
    cursor.close()


def insert():
    table_name = input("TABLE NAME: ")
    column = input("COLUMN NAMES: ")
    values = input("VALUES: ")
    command = f"INSERT INTO {table_name} ({column}) VALUES ({values})"
    cursor.execute(command)
    cnx.commit()
    print("")


def create():
    try:
        table_name = input("NEW TABLE NAME: ")
        no_of_columns = int(input("NO. OF COLUMNS: "))
        columns = ""
        for column in range(no_of_columns - 1):
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
        cursor.close()
        cnx.close()
        print("")


def reveal():
    try:
        table_name = input("TABLE NAME: ")
        
        cursor.execute(f'DESC {table_name}')
        all_fields = cursor.fetchall()
        main_fields = [field[0] for field in all_fields]
        print(main_fields)
        PT.field_names = main_fields

        cursor.execute(f"SELECT * FROM {table_name}")
        all_rows = cursor.fetchall()
        for rows in all_rows:
            PT.add_row(rows)
        
        print(PT)
        
    except mysql.connector.errors.ProgrammingError:
        print("Table not found!")
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

        command = f"SELECT * FROM {table_name} WHERE {column_name}={value}"
        print(command)
        cursor.execute(command)
        rows = cursor.fetchall()
        sep_rows = rows[0]
        main_rows = [rows for rows in sep_rows]
        PT.add_row(main_rows)
        
        print(PT)

    except mysql.connector.errors.ProgrammingError:
        print("Data not found!")
    finally:
        print("")


def to_user():
    print("""
STUDENT DATABASE MANAGEMENT SYSTEM (SDBMS) version 1.6.2

Usage instructions:

insert() : To insert data into a specific table.
create() : To create a new table.
delete() : To delete a table completely.
reveal() : To show all of the data stored in the specific table.
search() : To search for a particular data/row in a table.
quit()   : Quit the program.
""")

def quit():
    time.sleep(1)
    print("Bye...\n")

if __name__ == "__main__":
    main()
