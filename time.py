import time # type: ignore
timespan=time.strftime('%H:%M:%S')
print(timespan)
present=int(time.strftime('%H'))
if present<12:
    print("Good Morning")
elif present<18:
    print("Good Aternoon")
else:
    print("Good Night")


