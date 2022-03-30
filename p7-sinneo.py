"""
@author: Samantha Inneo

Description: This assignment takes in a file name and determines how many unique email 
    senders are in the file, and how many emails each person has sent.
"""
filename= "mbox.txt"
try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()



senders = dict()
for line in file:
    #strips the tailing characters
    line = line.rstrip()
    if line.find('From: ', 0, len(line)) != -1 or line.find('FROM: ', 0, len(line)) != -1: #checks if each line in the file is From: 
        senders[line[5:]] = senders.get(line[5:], 0) + 1   #add the line's sender into the senders dictionary or increment if it already exists


if len(senders) == 0: #there is either nothing in the file or no From: lines
    print('File contains no From: lines. No maximum')
else:
    maximum = max(senders, key=senders.get) #finds the key with the highest value 
    print(str(len(senders)) + ' unique senders') #counts how many unique users there are
    print('The user with the max number of emails is: ' + maximum + ' with ' + str(senders[maximum]) + ' emails')