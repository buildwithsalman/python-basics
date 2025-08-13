n = int(input("Enter the number you want factorial for :"))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    print(fac)