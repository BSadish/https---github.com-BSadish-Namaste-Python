week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
day = input("Enter the day: ").lower()

if day in week:
    days_left = (week.index("saturday") - week.index(day)) % 7
    print(f"It takes {days_left} day(s) for the holiday.")
else:
    print("Invalid day input.")
