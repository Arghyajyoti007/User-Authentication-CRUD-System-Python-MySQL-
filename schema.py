import mysql.connector
conn_obj = mysql.connector.connect(host="localhost", user="root", password="Arghya@123") # to connect with MySql
cur_obj = conn_obj.cursor() # to execute the sql qeuries, hit SQL

try:
    #cur_obj.execute("create database New_PythonDB")
    dbms = cur_obj.execute("show databases") # To run the given query
except:
    conn_obj.rollback()  # it is used if the operation is failed then it will not reflect in your database

for x in cur_obj:
    print(x)

conn_obj.close() # closing the object is very important at last
