import random

choices = {1: "Scissors", 2: "Paper", 3: "Rock"}
outcomes = {
    (1, 2): "Python won",
    (2, 3): "Python won",
    (3, 1): "Python won",
    (2, 1): "You won",
    (3, 2): "You won",
    (1, 3): "You won"
}

a = random.randint(1, 3)
b = int(input("Enter a number (1 for Scissors, 2 for Paper, 3 for Rock): "))

print(f"Python chose {choices[a]}")
print(f"You chose {choices[b]}")

if a == b:
    print("Draw")
else:
    print(outcomes.get((a, b), "Invalid input"))
