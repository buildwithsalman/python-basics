a = float(input("Enter first number:"))
o = input("Enter the operation you want to perform(+,-,*,/,%(for remainder),**(for power):)")
b = float (input("Enter second number:"))

if ( o == "+"):
    result = a + b 
elif ( o == "-"):
    result = a - b
elif ( o == "*"):
    result = a * b
elif ( o == "**"):
    result = a ** b
elif ( o == "%"):
    result = a % b
elif ( o == "/"):
    if (b != 0):
        result = a / b
    else:
        result = ("Error: denominator cannot be zero")
else:
    result = ("invalid operation")
print("result: ", result)

