# -*- coding: utf-8 -*-
"""
@author: Samantha Inneo

Description: This program takes in input of 3 numbers and returns to the user
            which one is the largest, without using the built in max function
"""

'''This function takes in 3 numbers and returns the maximum number'''
def maxOfThree(first, second, third):
    if first >= second and first >= third :
        return first
    if second >= first and second >= third :
        return second
    if third >= second and third >= first :
        return third
    
'''I use this boolean to stop asking for input.  Once it is sest to True, a 
   valid input has been given. While it remains false, the while loop
   continues, reprompting the user for their input'''
valid = False
while valid == False:
    try:
        # asks the user to enter their grade, then stores their input in grade   
       prompt = 'Please enter the first value: '
       val1 = input(prompt)
       if(float(val1)): #checks if the input is a valid number
           valid = True #sets valid to true to break this loop

    except:
        #this except catches non number input, tells the user it was incorrect,
        #and reprompts by sending it back to the beginning of this while loop
       print('Incorrect Input. Input must be a number.')
valid = False  #I reset this to false to do the next input     
while valid == False:       
    try:
        prompt = 'Please enter the second value: '
        val2 = input(prompt)
        if(float(val2)): #checks if the input is a valid number
            valid = True #sets valid to true to break this loop
    except:
        #this except catches non number input, tells the user it was incorrect,
        #and reprompts by sending it back to the beginning of this while loop
        print('Incorrect Input. Input must be a number.')
valid = False  #I reset this to false to do the next input               
while valid == False:     
    try:    
        prompt = 'Please enter the third value: '
        val3 = input(prompt)
        if(float(val3)): #checks if the input is a valid number
            valid = True #sets valid to true to break this loop
    except:
         #this except catches non number input, tells the user it was incorrect,
         #and reprompts by sending it back to the beginning of this while loop
         print('Incorrect Input. Input must be a number.')   
# this prints in the format shown by the professor         
print("The maximum of ", val1, val2, val3, " is ", maxOfThree(val1, val2, val3) )         