week=["sunday","monday","tuesday","wednesday","friday","saturday"]
day=input("Enter the day you want to choose: ")
day=day.lower()
if day=="sunday":
    print("It takes 5 days for holiday")
    del week[:1]
    print(week)
elif day=="monday":
    print("It take 4 days for holiday")
    del week[:2]
    print(week)
elif day=="tuesday":
    print("It takes 3 days for holiday")
    del week[:3]
    print(week)
elif day=="wednesday":
    print("It takes 2 days for holiday")
    del week[:4]
    print(week)
elif day=="friday":
    print("Holiday is Day after tomorrow🎉")
    del week[:5]
    print(week)
else:
    print("Its holiday enjoy!!")

    
