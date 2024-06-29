import sqlite3


DATABASE = 'tmp/films.db'
DEBUG = True
SECRET_KEY = 'abcd' # в дальнейшем будет заменен на более сложный
USERNAME = 'admin'
PASSWORD = '123'

def connect_db():
    conn = sqlite3.connect()
