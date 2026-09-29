age = int(input("Enter your age  >"))
mv = float(input("Enter your monthly revenue  >"))
cs = int(input("Enter your credit score  >"))
years = float(input("How long does your business been running  >"))
has_defaults = bool(input("Have you been defaults (True or False)  >"))
item = input("Enter your collateral   >")
value = float(input("Enter the value of collateral  >"))


maxloan = 0
baseloan = 0

if age >= 21 and has_defaults == False and years >=2.0:
    print("Baseline Passed")
    if cs>=720: #tier1
        maxloan = mv * 3
        print(maxloan)
        if mv >= 50000:
            baseloan = maxloan * 0.015
            print(baseloan)
        else:
            baseloan = maxloan * 0.025
            print(baseloan)

    #collateral
        if value >= maxloan:
            print("Valid")
        else:
            print("Rejected")


#Surcharge
        if value % 5000 != 0:
            baseloan += 250
            print(" additional 250")
        else:
            print("divisible by 5000")

    elif cs <= 620 and cs < 720:
        maxloan = mv * 1.5
        print(maxloan)
        if years >= 5.0:
            baseloan = maxloan * 0.02
            print(baseloan)
        else:
            baseloan = maxloan * 0.035
            print(baseloan)

    elif cs <620:
        print("rejected")

    else:
        print("Credit score is to low")
else:
    print("Baseline Failed")