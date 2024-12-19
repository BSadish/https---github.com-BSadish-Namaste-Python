science=int(input("Enter the marks of science"))
maths=int(input("Enter the marks of maths"))
health=int(input("Enter the marks of health"))
computer=int(input("Enter the marks of computer"))
english=int(input("Enter the marks of english"))

if science > 100 or maths > 100 or health > 100 or computer > 100 or english > 100:
    print("The marks cannot be more than 100 for each subject.")
else:
    total=science+maths+health+computer+english   
    grade=(total/500)*4
    print(grade)
    if(grade<=4 and grade>=3.6):
     print("Your grade is A+")
    elif(grade<3.6 and grade>=3.2):
     print("Your grade is A")
    elif(grade<3.2 and grade>=2.8):
     print("Your grade is B")
    elif(grade<2.8 and grade>=2.4):
     print("Your grade is C")
    else:
     print("Your are fail")
     