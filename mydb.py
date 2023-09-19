# pip install mysql-connector-python

import mysql.connector

data_base = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ukL5Vp!&",
    auth_plugin='mysql_native_password'
)

# prepare a cursor object
cursor_object = data_base.cursor()

# create a database
cursor_object.execute("CREATE DATABASE elderco")

print("All done!")