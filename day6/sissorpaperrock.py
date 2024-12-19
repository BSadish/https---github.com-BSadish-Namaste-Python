# print 1 for sessor 2 for paper and 3 for rock
import random

choices = {1: "Scissors", 2: "Paper", 3: "Rock"}

a = random.randint(1, 3)

b = int(input("Enter a number (1 for Scissors, 2 for Paper, 3 for Rock): "))

print(f"Python chose {choices[a]}")
print(f"You chose {choices[b]}")


if a == b:
    print("Draw")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("Python won")
elif (b == 1 and a == 2) or (b == 2 and a == 3) or (b == 3 and a == 1):
    print("You won")
else:
    print("Invalid input")



