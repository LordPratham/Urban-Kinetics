import mysql.connector
from mysql.connector import errorcode

try:

    con = mysql.connector.connect(host='localhost', user='root',password='12345678')
    cursor = con.cursor()

    databaseName = "urban_kinetics"
    usersTableName = "users"
    usersTableFields = "card_num int(5) PRIMARY KEY, name varchar(20)"

    makeOrCheckDatabase = f"create database if not exists {databaseName}"
    cursor.execute(makeOrCheckDatabase)

    useDatabase = f"use {databaseName}"
    cursor.execute(useDatabase)

    makeOrCheckUsersTable = f"create table if not exists {usersTableName}({usersTableFields})"
    cursor.execute(makeOrCheckUsersTable)
    
    def cardNum():
        cursor.execute(f"select * from {usersTableName}")
        cardValue = 1001
        for number in cursor:
            if not cursor:
                cardValue = 1001 

            else:
                print(number)
                cardValue=int(number[0]) + 1
        return cardValue
    
    def query(command):
        cursor.execute(command)
        con.commit()

    insertUserRecord = f"insert into users values({cardNum()}, 'Arsh')"
    query(insertUserRecord)

    cursor.close()
    con.close()
    print("done")
    dir(errorcode)
except mysql.connector.Error as err:
    print(err.errno,err,err.msg)

# for i in dir(errorcode):
#     code = "errorcode."+str(i)
#     code = eval(code)
#     if code==1049:
#         print(i)