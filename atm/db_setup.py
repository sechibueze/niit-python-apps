import sqlite3
from db_config import database_name
# Connect
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

# Create tables
query = 'CREATE TABLE IF NOT EXISTS customers(' \
        'customer_id INTEGER NOT NULL PRIMARY KEY, ' \
        'email VARCHAR(100) NOT NULL UNIQUE,' \
        'fullname VARCHAR(100) NOT NULL,' \
        'pin VARCHAR(4) NOT NULL ,' \
        'balance INTEGER NOT NULL '\
        ' )'

cursor.execute(query)
connection.commit()

print('Table created')