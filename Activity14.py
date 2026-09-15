#age (integer) 
#is_employed (boolean) 
#credit_score (integer) 
#annual_income (float) 
#has_collateral (boolean) 

age = int(input("Enter your age   > "))
is_employed = bool(input("Are you employed  (True/False)   >"))
credit_score = int(input("What is your credit score    >"))
annual_income = float(input("What is your annual income    >"))
has_collateral = bool(input("Do you have a collateral    >"))

if age >= 21 and is_employed == True:
    print("Pasok")
    #high credit
    if credit_score>=750:
        print("HIGH")
        if annual_income >= 100000:
          print(" HIGH salary")
          base_rate = 4.5
          print(base_rate)
        else:
            base_rate = 5.0
            print(base_rate)
#fair credit
    elif credit_score >= 600 and credit_score< 750:
        print("Credit Score less than 750")
        if has_collateral == True:
            base_rate = 7.0
            print(base_rate)
        elif annual_income <= 40000:
          base_rate = 9.5
          print(base_rate)
        else:
            base_rate = 8.0
            print(base_rate)

#low credit
    elif credit_score <= 600:
        print("Failed Credit To Low")

    else:
        print("Bawal")