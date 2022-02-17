"""
@author: Samantha Inneo

Description: This program creates a random number for the user to guess between 1 and 20.
             The user has 6 attempts to guess the correct number before the game is over
"""
import random

'''This function checks if the 'guess' is equal to, greater than, or less than the 
   'correct' number'''
def guessChecker(correct, guess):
    if correct == guess: #the numbers are the same
        return 0
    elif correct < guess: #the guess is too high   
        return 1
    else:   #the guess is too low   
        return -1


prompt = "Hello! What is your name? "
name = input(prompt) #captures the users name and stores it in 'name' for use later

print("Well, " + name + ", I am thinking of a number between 1 and 20.")
tries = 0 #keeps track of how many valid guesses the user has made for the for loop
correct =  random.randint(1, 20) #sets the random number the user is trying to guess
while tries < 6:
    valid = False #I use this for checking input to keep prompting when necessary
    while valid == False:
        try:
            # asks the user to enter their guess, then stores their input in val1   
            prompt = 'Take a guess. '
            val1 = input(prompt)
            if(float(val1)): #checks if the input is a valid number
                guess = float(val1)
                valid = True #sets valid to true to break this loop since input is valid
                if guess > 20 or guess < 1:
                    print('Incorrect Input. Guess must be a number between 1 and 20.')
                    valid = False #if the number is >20 or <1 it is not valid
        except:
            #this except catches non number input, tells the user it was incorrect,
            #and reprompts by sending it back to the beginning of this while loop
            print('Incorrect Input. Guess must be a number between 1 and 20.')
    tries+=1 #increases the number of valid guesses made
    if(guessChecker(correct, guess) == 0):
        print("Good job, " + name + "! You guessed my number in "+ str(tries) + " guesses!")
        tries = 7 #set higher than 6 so the loop stops
    elif (guessChecker(correct, guess) == -1): #guess is too low, guess again
        print("Your guess is too low.")  
    elif (guessChecker(correct, guess) == 1): #guess is too high, guess again
        print("Your guess is too high.")  
    if tries == 6: #user failed to guess the correct number in 6 tries, end program
        print("The number I was thinking of was " + str(correct)) 