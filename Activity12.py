import getpass

username = 'dipinili'
password = 'akonalangsana'

u = input("Enter username ---->   ")
p = getpass.getpass("Enter password ---->   ")

if username == u and password == p :
	print("LAkAS")
else:
	print("WAWA")