# -*- coding: utf-8 -*-
"""
@author: Samantha Inneo

Description: This program takes in a number grade and converts it to the 
apprporiate letter grade
"""

'''I use this boolean to end the program.  Once it is sest to True, a valid 
answer has been given. While it remains false, the while loop continues,
 reprompting the user for their input'''
valid = False
while valid == False:
  

#if any code in the try fails, go to the except. Otherwise complete the try
    try:
        # asks the user to enter their grade, then stores their input in grade   
       prompt = 'Please enter a positive number between 0 and 100: '
       grade = input(prompt)
       #attempt to turn the input into an float.  
       #If it fails, invalid input was given, ask for a different input.
       intgrade = float(grade)

       #these if and elif statements give the limits for each letter grade
       if intgrade >= 92 and intgrade <= 100:
            valid = True
            print('Your grade is an A.')
       elif intgrade >= 90 and intgrade <= 100:
            valid = True
            print('Your grade is an A-')
       elif intgrade >= 87 and intgrade <= 100:
            valid = True
            print('Your grade is a B+')
       elif intgrade >= 83 and intgrade <= 100:
            valid = True
            print('Your grade is a B')
       elif intgrade >= 80 and intgrade <= 100:
            valid = True
            print('Your grade is a B-')
       elif intgrade >= 70 and intgrade <= 100:
            valid = True
            print('Your grade is a C')    
       elif intgrade < 70 and intgrade >= 0:
            valid = True
            print('Your grade is an F') 
       else:
           #this else statement is only reached if the input is above 100 or 
           #below 0, it tells the user it was incorrect, and reprompts by 
           #sending it back to the beginning of the while
          print('Incorrect Input.')
    except:
        #this except catches non number input, tells the user it was incorrect,
        #and reprompts by sending it back to the beginning of the while
       print('Incorrect Input.')

