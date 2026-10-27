z=int(input("Enter size> "))


n = 1
 
for i in range(z):
    for x in range(i + z):
        print(n, end=" ")
        n = n +1
    print()
