# Password_Authenticator
# Instagram @py_coder_wall
# Like | Comment | Share

import getpass
database = {"py_coder_hub":"09876","coderx":"55555"}
username = input("Enter username :")
password = getpass.getpass(prompt="Enter password :",stream=None)
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter password again")
        break
print ("Verified")    



