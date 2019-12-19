import os

# Python program to explain os.environ object

# importing os module
import os
import pprint

# Get the list of user's
# environment variables
## env_var = os.environ

# Print the list of user's
# environment variables
## print("User's Environment variable:")
## pprint.pprint(dict(env_var), width=1)




#DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{"user"}:{"password"}@{"localhost"}:{5432}/{"POSTGRES_DB"}'
#DATABASE_CONNECTION_URI = f'postgresql+psycopg2://postgres:password@postgres:5432/example'
DATABASE_CONNECTION_URI = f'postgresql+psycopg2://postgres:password@localhost:5432/example'



print("DATABASE_CONNECTION_URI")
print(DATABASE_CONNECTION_URI)

# set FLASK_APP=app.py
# C:\Users\User\AppData\Local\Programs\Python\Python38-32