#----------------------------*** IMPORTING BUILTIN MODULES ***------------------------------------

import subprocess
import sys
import os
import getpass
import webbrowser


#------------*** FUNCTION TO CHECK WHETHER THE NEEDED THIRD PARTY MODULE IS INSTALLED ***----------
def userModule(package):

    import importlib

    try:
        removableIndex = package.index("==")
        trypackage = package[:removableIndex]

        globals()[package]=importlib.import_module(trypackage)


    except ImportError:
        subprocess.check_call([sys.executable,"-m","pip","install",package])


    finally:
        if "==" in package:
            removableIndex = package.index("==")
            package = package[:removableIndex]

        #globals()[package]=importlib.import_module(package)

#------------------*** IMPORTING THIRD PARTY MODULES ***--------------------------

try:
    import mysql.connector
except ModuleNotFoundError:
    userModule("mysql-connector==2.2.9")
    userModule("mysql-connector-python==8.0.21")
    import mysql.connector


try:
    from cryptography.fernet import Fernet
except ModuleNotFoundError:
    userModule("cryptography==3.1.1")
    from cryptography.fernet import Fernet


#------------------*** CHECKING AND CREATING NEEDED FILES AND FOLDERS ***------------------

if not os.path.isdir(r"./Dependencies"):
    os.mkdir(r"./Dependencies")

    os.mkdir(r"./Dependencies/Encryption")

    if not os.path.isfile(r"./Dependencies/userpassword.txt"):
        with open(r"./Dependencies/userpassword.txt","w") as writeFile:
            pass

else:
    if not os.path.isdir(r"./Dependencies/Encryption"):
        os.mkdir(r"./Dependencies/Encryption")

    if not os.path.isfile(r"./Dependencies/userpassword.txt"):
        with open(r"./Dependencies/userpassword.txt","w") as writeFile:
            pass

#------------------*** ASKING USER WHETHER HE/SHE HAS MYSQL INSTALLED***--------------------------------  

while True:

    hasSql = input("""
    DO YOU HAVE MYSQL?
    PRESS Y FOR YES, N FOR NO : -   """)

    if hasSql.upper()=="Y":
        print("Thank You So Much! ")
        break
    elif hasSql.upper()=="N":
        webbrowser.open("https://dev.mysql.com/downloads/installer/")
        break
    else:
        print("INVALID CHOICE! ")

#-----------*** FUNCTIONS FOR ENCRYPTING AND DECRYPTING USER'S CONFIDENTIAL AND SENSITIVE DATA ***--------

def writeKey():
    if not os.path.isfile(r"./Dependencies/Encryption/key.key") or \
        len(open(r"./Dependencies/Encryption/key.key").read())==0:
        key=Fernet.generate_key()
        with open(r"./Dependencies/Encryption/key.key","wb") as writeKeyFile:
            writeKeyFile.write(key)

def loadKey():
    with open(r"./Dependencies/Encryption/key.key","rb") as loadKeyFile:
        return loadKeyFile.read()
 
def encrypt(data,key):
    f = Fernet(key)
    encryptedData = f.encrypt(data.encode())
    with open(r'./Dependencies/userpassword.txt','wb') as encryptedPass:
        encryptedPass.write(encryptedData)

def decrypt(encrypted,key):

    f = Fernet(key)
    decryptedData = f.decrypt(encrypted)
    return decryptedData.decode()


writeKey()
key = loadKey()
f = Fernet(key)


#-----------*** INPUTING USER'S MYSQL SERVER PASSWORD ***--------------
with open(r'./Dependencies/userpassword.txt','r+') as savedPass:
    userPass=savedPass.read()
    if len(userPass)==0:
        userPass = getpass.getpass(prompt="Enter the password for your MYSQL Account :- ")
        encrypt(userPass,key)

#-----------*** CHECKING WHETHER THE PASSWORD ALREADY EXISTS ***------------------
    else :
        usingExisting = input("""
        Password to Your MYSQL Already Exists, 
        DO You want to use That?
        Press Y for Yes, N for No :-  """)
        if usingExisting.upper() =="Y":
            userPass=decrypt(userPass.encode(),key)

#-----------*** CHANGING THE EXISTING PASSWORD IF THE USER STILL WANTS ***-------------------
        elif usingExisting.upper()=="N":
            userPass = getpass.getpass(prompt="Enter the password for your MYSQL Account :- ")
            encrypt(userPass,key)


#------------------*** CONNECTING TO MYSQL connectionObject ***--------------------------------
while True:

    try:  
        con = mysql.connector.connect(host='localhost', user='root',password=userPass)
        break

#----------*** HANDELING ACCESS DENIES ERROR DUE TO INCORRECT PASSWORD FOR MYSQL ***---------

    except mysql.connector.errors.ProgrammingError:
        choice = input("""
        PASSWORD MISMATCHED!!!
        If You Want To Re-Enter Password, Press Y 
        Otherwise, If You Want To Quit, Press Q :- """)

        if choice.upper()=="Y":
            with open(r'./Dependencies/userpassword.txt','r+') as savedPass:

                userPass = getpass.getpass(prompt="""
            PLEASE RE-ENTER THE PASSWORD :- """)
                encrypt(userPass,key)
        elif choice.upper()=="Q":
            exit()
        else:
            print(f"""
        NO Choice Such As {choice} Please Try Again!\n""")


#------------------------------------------------------
     
cursor = con.cursor()
cursor.close()
con.close()
print("done")

print(os.getcwd())

