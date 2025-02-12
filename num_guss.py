# loop
# user need to guess a number
# the number is exact the number the computer selected
# if the number is greater than the number than show "the selected number is greater"
# if num is smaller then show "the number is smaller than the real number"
# if num is exact to the number then print "guess is right"

import random as rd

num = rd.randint(1,100)
guess = 0
while True:
    
    try:
     user = int(input("Guess a number from 1 to 100:").upper())

     if num > user:
        print("The number is greater then your number".upper())

     elif num < user:
        print("The number is less than your number".upper())
     elif num == user:
        print("your guess is correct")
        break

     if num != user:
        guess += 1 
    except ValueError:
        print("enter a valid input:".upper())


print(f"number of efforts you have taken: {guess+1}".upper())
