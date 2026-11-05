# while loop

isLong = True


while isLong == True:
    x=bool(input("Is it long (True or False) > "))

    if x== True:
        print("Continue loop")
        continue
    elif x == False:
        break

