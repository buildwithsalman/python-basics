def fact_n(n):
    fac = 1
    for i in range (1,n+1):
        fac *= i 
    print(fac)

val = int(input("Enter the value:"))
fact_n(val)