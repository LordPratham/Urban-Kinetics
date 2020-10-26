import mysql.connector
from mysql.connector import errorcode

for i in dir(errorcode):
    code = "errorcode."+str(i)
    code = eval(code)
    if code==1049:
        print(i)
try:
    con = mysql.connector.connect(host='localhost', user='root',password='123478')
    # cursor = con.cursor()
    # cursor.execute("create database if not exists trainer")
    # cursor.execute("use trainer")
    # cursor.close()
    # con.close()
    # print("done")
    # dir(errorcode)

except mysql.connector.Error as e:
    # print(e.errno,e.msg)
    if e.errno == 1045:
        print("hi")