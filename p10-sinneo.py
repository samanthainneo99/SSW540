"""
@author: Samantha Inneo

Description: This file takes in a txt file representing an email box and 
    determines how mnay emails were sent each day of the week. Then, it plots 
    the results on a graph 
"""



prompt = "Please enter the name of the file:"
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()

    