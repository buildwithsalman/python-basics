num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if(num1>num2 and num1>num3):
    print(num1," is the greatest number")
elif(num2>num3):
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")
print("your numbers were:",num1, num2, num3)