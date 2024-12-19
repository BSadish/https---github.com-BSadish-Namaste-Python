import random

position = 0


while True:
    input("Press Enter to roll the dice user.")
    roll = random.randint(1, 6) 
    

    print(f"You rolled a {roll}")  
    
    position += roll
    
   
    if position == 14:
        print("Oops! You landed on 14. Moving back to 3.")
        position = 3
    elif position == 17:
        print("Oops! You landed on 17. Moving back to 9.")
        position = 9
    elif position == 19:
        print("Oops! You landed on 19. Moving back to 7.")
        position = 7
    elif position == 24:
        print("Oops! You landed on 24. Moving back to 1.")
        position = 1
    
    print(f"Your current position is {position}")
    
    if position >= 30:
        print("Congratulations! You've reached the end and won the game!")
        break
