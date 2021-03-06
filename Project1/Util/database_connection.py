from psycopg2 import connect, OperationalError, errors
import os


def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DATABASE"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
            )
        return conn
    except OperationalError as e:
         print(str(e))


connection = create_connection()
print(connection)