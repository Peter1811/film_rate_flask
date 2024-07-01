import dotenv
import psycopg2
import os

from time import ctime
from typing import Tuple, Union


def create_connection() -> Tuple[Union[psycopg2.extensions.connection, None], Union[psycopg2.extensions.cursor, None]]:
    try:
        dotenv.load_dotenv('.env', override=True)
        connection = psycopg2.connect(
            dbname=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        cursor = connection.cursor()
        return connection, cursor
    
    except psycopg2.OperationalError as connecting_error:
        print(ctime() + 'error with connecting to database: ' + connecting_error)
        return None, None

    except psycopg2.InternalError as cursor_error:
        print(ctime() + 'error with cursor creating: ' + cursor_error)
        return None, None


def close_connection(connection: psycopg2.extensions.connection, cursor: psycopg2.extensions.cursor) -> None:
    cursor.close()
    connection.close()
