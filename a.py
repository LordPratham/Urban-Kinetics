import getpass
from cryptography.fernet import Fernet
# passw=getpass.getpass()
# print(passw)
# mypass=getpass.getpass("PASSWORD :")
# print("pass is")
# print(type(mypass))
# print(type(b"hi"))
# print(b"abc".decode())
key = Fernet.generate_key()
print(key)
a = b"gAAAAABfjhCRE58icTvHbdRpbnIaNd6Ws9hOyaZDChC7xdYmmGubGG5zzcg3V9z52fnmWnF4y0nGlShiTVf-g8Eb1bM-MrMbtw=="
f=Fernet("a2UuGRXqW-KNH6qVlCU8CFH8LJq_XsrCqcxDa6LeA2Q=")
# ae=f.encrypt(a.encode())
# print(ae)
ad=f.decrypt(a)
print(ad.decode())
print(len(ad.decode()))
print('IF YOU WANT TO RE-ENTER PASSWORD, PRESS'.title())