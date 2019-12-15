#Guesse the number game
import random
import sys

def input_number(x):#Function to check if the user inputs a number.
    while True:
        try:
            return int(input(x))
        except ValueError:# If anything is typed except for a number the valueerror will show up.
            print("That was not a number")

while True:
    print ("Do you want to guess a number? y/n")
    start = input()
    if start == ('y'):
        print ("Ok, now what is your name?")
        name = input()
        print ("Hi! " + name + " I'm thinking of a number between 1 and 20")

        hidden = random.randrange(1, 20)
        print (hidden)

        for Every_Try in range (1, 6):
            guess = int(input_number("Please enter your guess: "))
            
            if guess < hidden:
                print("Your guess is too low")
            elif guess > hidden:
                print("Your guess is too high")
            else:
                break
        if guess == hidden:
            print("Hit! Awesome u guessed the right asnwer " + name)   
        else:
            print ("the correct answer was " + str(hidden))
    elif start == ('n'):
        sys.exit()
    else:
        print ("Please pick y or n")
