"""
@author: Samantha Inneo

Description: This file takes in a txt file representing an email box and 
    determines how mnay emails were sent each day of the week. Then, it plots 
    the results on a graph 
"""
import matplotlib.pyplot as plt
from dateutil.parser import parse
from calendar import *

# I use this to parse the lines to check if they are dates
def is_date(string):
    try: 
        parse(string)
        return True

    except ValueError:
        return False

prompt = "Please enter the name of the file:"
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daysofweek = dict()
for line in file:
    #strips the tailing characters
    line = line.rstrip()
    if line.find('Date: ', 0):
        if is_date(line): #checksd to make sure the line is a date before we do any work
            date = parse(line) #parse will convert line to a date type 
            daysofweek[days[date.weekday()]] = daysofweek.get(days[date.weekday()], 0) + 1  #.weekday returns the number associated with a weekday, so I use the days list to make it readbable
            # daysofweek = (days[date.weekday()])
# print(daysofweek)
print("Your mailbox breakdown by day: ")
print("Sunday: " + str(daysofweek.get('Sunday')) + " Monday: " + str(daysofweek.get('Monday')) + " Tuesday: " + 
    str(daysofweek.get('Tuesday')) + " Wednesday: " + str(daysofweek.get('Wednesday')) + " Thursday: " + str(daysofweek.get('Thursday')) + 
    " Friday: " + str(daysofweek.get('Friday')) + " Saturday: " + str(daysofweek.get('Saturday')) )

'''Graphing portion'''
# I make lists of the keys (weekdays) and their values (# sent) so I can use them in the bar graph
keys = list(daysofweek.keys())
values = list(daysofweek.values())
keys.reverse() #I reverse them so it reads the order of the week days in the mbox example, but this is not necessary
values.reverse()

plt.bar(range(len(daysofweek)), values, tick_label=keys) #create a bar graph with my data
plt.show() #display graph