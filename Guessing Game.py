#Guessing Game
import random
Guess=int(input("Enter your Guess:"))
Computer_Generated=random.randint(0,10)
while Guess>0:
    if Guess< Computer_Generated:
        print("Your guess is too low")
        Guess=int(input("Enter your Guess:"))
    elif Guess>Computer_Generated:
        print("Your guess is too High")
        Guess=int(input("Enter your Guess:"))
    else:
        print("You guess is correct")
        break