import sys
import mysql.connector
from mysql.connector import Error

def execute_sql_script(sql_file_path, host, user, password, database):
    try:
        connection = mysql.connector.connect()

        if connection.is_connected():
            print("Connected to MySQL database")

            cursor = connection.cursor()

            with open(sql_file_path, 'r') as file:
                sql_script = file.read()

            for command in sql_script.strip().split(';'):
                if command.strip():
                    cursor.execute(command)
                    print(f"Executed: {command.strip()}")

            connection.commit()
            print("All changes committed successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python execute_sql_script.py <script> <host> <user> <password> <database>")
    else:
        _, script, host, user, password, database = sys.argv
        execute_sql_script(script, host, user, password, database)
