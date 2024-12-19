import random

position1 = 0
position2=0
position3=0


while True:
    input("Your turn Sadish")
    roll = random.randint(1, 6) 
    

    print(f"You rolled a {roll} sadish")  
    
    
    position1 += roll
    
   
    if position1 == 14:
        print("Oops! You landed on 14. Moving back to 3.")
        position1 = 3
    elif position1 == 17:
        print("Oops! You landed on 17. Moving back to 9.")
        position1 = 9
    elif position1 == 19:
        print("Oops! You landed on 19. Moving back to 7.")
        position1 = 7
    elif position1 == 24:
        print("Oops! You landed on 24. Moving back to 1.")
        position1 = 1
    elif position1 ==29:
         print("Oops! You landed on 29. Moving back to 2.")
         position1==2
    
    print(f"Your current position is {position1} sadish\n")
    
    if position1 >= 30:
        print("Congratulations! You've reached the end and won the game Sadish!")
        break



    # second player
    input("Your turn Prabesh")
    roll = random.randint(1, 6) 
    

    print(f"You rolled a {roll} ujjwal")  
    
    position2 += roll
    
   
    if position2 == 14:
        print("Oops! You landed on 14. Moving back to 3.")
        position2 = 3
    elif position2 == 17:
        print("Oops! You landed on 17. Moving back to 9.")
        position2 = 9
    elif position2 == 19:
        print("Oops! You landed on 19. Moving back to 7.")
        position2 = 7
    elif position2 == 24:
        print("Oops! You landed on 24. Moving back to 1.")
        position2 = 1
    elif position2 ==29:
         print("Oops! You landed on 29. Moving back to 2.")
         position2==2
    
    print(f"Your current position is {position2} ujjwal\n")
    
    if position2 >= 30:
        print("Congratulations! You've reached the end and won the game ujjwal!")
        break


    #Third player

    # input("Your turn prasun")

    # roll = random.randint(1, 6) 
    

    # print(f"You rolled a {roll} prasun")  
    
    # position3 += roll
    
   
    # if position3 == 14:
    #     print("Oops! You landed on 14. Moving back to 3.")
    #     position3 = 3
    # elif position3 == 17:
    #     print("Oops! You landed on 17. Moving back to 9.")
    #     position3 = 9
    # elif position3 == 19:
    #     print("Oops! You landed on 19. Moving back to 7.")
    #     position3 = 7
    # elif position3 == 24:
    #     print("Oops! You landed on 24. Moving back to 1.")
    #     position3 = 1
    # elif position3 ==29:
    #      print("Oops! You landed on 29. Moving back to 2.")
    #      position3==2
    
    # print(f"Your current position is {position3} prasun\n")
    
    # if position3 >= 30:
    #     print("Congratulations! You've reached the end and won the game prasun!")
    #     break
