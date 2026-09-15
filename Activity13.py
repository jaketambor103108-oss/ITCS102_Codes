#Age 

name = input("Input NAME ----->")
age = int(input("Input AGE ----->"))


print("Hi, ",name, "That age is considered as ")
if age >=1 and age <=5:
	print("Infant")
elif age >5 and age <=12:
	print("KId")
elif age >12 and age <=19:
	print("Teenager")
elif age >19 and age <=29:
	print("Early adulthood")
elif age >29 and age <=48:
	print("Adult")
elif age >48 and age <=59:
	print("Advance adult")
elif age >59 and age <=150:
	print("Senior")
else:
	print("Invalid")