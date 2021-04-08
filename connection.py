import psycopg2
from data import data

def connect(connection_data = None):
    if connection_data is None:
        connection_data = data
    connection = psycopg2.connect(**connection_data)
    connection.autocommit = True
    return connection

if __name__ == '__main__':
    connection = connect()
    connection.close()

