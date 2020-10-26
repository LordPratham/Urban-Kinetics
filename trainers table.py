import mysql.connector
from mysql.connector import errorcode

try:

    con = mysql.connector.connect(host='localhost', user='root',password='12345678')
    cursor = con.cursor()

    databaseName = "urban_kinetics"


    def trainersTableInitialiser():
        global trainersTableName
        global trainersTableFields
        global trainersNameList
        global trainersExperience
        global trainersSpeciality
        global trainersAge


        trainersTableName = "trainers"
        trainersTableFields = "sr_no int(5) PRIMARY Key, name varchar(20),\
            experience varchar(20), speciality varchar(50), age int(2)"

        trainersNameList = ['Thomas', 'Stephen','Lewis','Samuel', 'Kane']
        trainersExperience = ['2 Years','5 Years','8 Years','10 Years','6 Years', '3 Years']
        trainersSpeciality = ['Weight Loss', 'Muscle Gain', 'Aesthetics','Calisthenics','Aerobics']
        trainersAge = [26, 28, 32, 35, 30, 29]

        makeOrCheckDatabase = f"create database if not exists {databaseName}"
        cursor.execute(makeOrCheckDatabase)

        useDatabase = f"use {databaseName}"
        cursor.execute(useDatabase)

        makeOrCheckTrainersTable = f"create table if not exists {trainersTableName}({trainersTableFields})"
        cursor.execute(makeOrCheckTrainersTable)

        def query(command):
            cursor.execute(command)
            con.commit()


        for i in range(len(trainersNameList)):
            insertTrainersRecord = f"insert into {trainersTableName} value({i+1001}, '{trainersNameList[i]}', \
                '{trainersExperience[i]}', '{trainersSpeciality[i]}', '{trainersAge[i]}')"

            query(insertTrainersRecord)

    trainersTableInitialiser()





    cursor.close()
    con.close()
    print("done")
    dir(errorcode)
except mysql.connector.Error as err:
    if err.errno == 1062:
        print("""
        TABLE ALREADY MADE AND,
        THE DATA YOU WANT TO ENTER IS CLASHING WITH THE EXISTING ONE!!!""")


# for i in dir(errorcode):
#     code = "errorcode."+str(i)
#     code = eval(code)
#     if code==1049:
#         print(i)