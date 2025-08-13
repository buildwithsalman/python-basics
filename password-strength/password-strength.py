a = input("Enter your password: ")

has_alpha = False
has_digit = False
has_special = False

for char in a :
    if char.isalpha():
        has_alpha = True
    elif char.isdigit():
        has_digit = True
    elif not char.isalnum():
        has_special = True

if (len(a)<6):
    print("Password is too short. Try at least 6 characters.")
elif ( has_alpha and has_digit and has_special):
    print("password is strong")
elif ( has_alpha and has_digit):
    print("Password is moderate. Add special characters for more strength.")

else:
    print("Password is weak. Use letters, numbers, and symbols.")