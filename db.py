import dotenv
import psycopg2
import os

dotenv.load_dotenv('.env')

def create_connection():
    connection = psycopg2.connect(
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )

    cursor = connection.cursor()

    return connection, cursor

def close_connection(connection, cursor):
    connection.commit()
    cursor.close()
    connection.close()
