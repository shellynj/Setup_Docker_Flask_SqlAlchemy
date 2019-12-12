import os

user = os.environ['postgres']
password = os.environ['Shelly_NJIT_2019']
host = os.environ['localhost']
database = os.environ['POSTGRES_DB']
port = os.environ['5432']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'