import os

user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
host = os.getenv('PG_HOST')
database = os.getenv('PG_DB')
port = os.getenv('PG_PORT')

DATABASE_CONNECTION_URI = f'postgresql://postgres:hydrogen@localhost:5432/flasksql'
