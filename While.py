time= int(input("Enter time in seconds:"))
#Countdown Timer: asks the user for a time in seconds and then counts down to zero using a while loop.
while time>=0:
    
    time=time-1
    if time<0:
        break
    print(time)
