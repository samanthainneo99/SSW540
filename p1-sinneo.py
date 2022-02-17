# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:39:56 2022

@author: Samantha Inneo

Description: This is a simple program that prompts the user for their first and 
last name, then returns 'Hello <first> <last>'

"""

# asks the user to enter their first name, then stores their input in first   
prompt = 'Please enter your first name: '
first = input(prompt)

'''
This while loop checks for invalid inputs.  If first has any non letter 
characters, it will reprompt the user for their first name.This will handle
both numbers and file extensions
'''
while first.isalpha() == False:
    prompt = 'Please enter your first name: '
    first = input(prompt)
    

    
# asks the user to enter their last name, then stores their input in last   
prompt = 'Please enter your last name: '
last = input(prompt)

'''
This while loop checks for invalid inputs.  If last has any non letter 
characters, it will reprompt the user for their last name. This will handle
both numbers and file extensions
'''
while last.isalpha() == False:
    prompt = 'Please enter your last name: '
    last = input(prompt)  

#prints the desired output
print("Hello " + first + " " + last)
