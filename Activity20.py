#Pass

from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Enter your Username >")
    password = getpass("Enter your Password >")

    if username == "hakdog" and password == "123456":
        isLogin =True
        print("You may enter0")
    else:
        isLogin = False
        print("You cannot enter0")