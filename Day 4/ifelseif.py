sum=int(input("1 for ADD AND 2 FOR SUB AND 3 FOR DIVIDE 4 FRO MULTIPLY AND 5 FOR AVERAGE"))
x=float(input("Enter first number:"))
y=float(input("Enter second number"))

if sum==1 or sum==6:
        print("ADD: ",x+y)
elif sum==2:
        print("SUB: ",x-y)
elif sum==3:
        print("Multiply",x*y)
elif sum==4:
        print("Divide", x/y)
elif sum==5:
        print("Average", (x+y)/2)
else:
        print("The number is invalid")
