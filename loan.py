#Task 1


loan= float(input("How much will you loan ? "))
years= int(input("How long?"))

month = years * 12
p = loan / month
r = loan 
total = 0
print("|MONTH\t\t|\tMONTHLY PAYMENT\t\t|\tINTEREST\t\t|\tPRINCIPLE\t\t|\tREMAINING LOAN\t\t|")

for x in range (1, month + 1):
    
        r -= p
        i  = r*0.00259
        m = i + p
        total += i
        #print(x,  round (p, 2), round(r, 2), round (i, 2), round(m, 2))

        print(f"|   {x}\t\t|\t{round (m, 2)}\t\t\t|\t{round(i, 2)}\t\t\t|\t{round (p, 2)}\t\t\t|\t{round (r, 2)}\t\t\t|")
print(total)