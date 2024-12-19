a=float(input("Enter a number"))

if type(a) == int:
    if a % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
        print("Invalid number.")