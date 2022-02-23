"""
@author: Samantha Inneo

Description: This program takes in string input and determines the plurals for all the words.
"""

def plural(strs):
    pluralList = []
    strs = strs.split(" ")
    for str in strs:
        if(not str.isalpha()): #checks for valid input
            return 'Contains non alphabetic input. Run Program again without invalid text.'
        if(str.endswith(('ay', 'ey', 'iy', 'oy', 'uy'))):
            pluralList.append(str + 's') #for these cases, add an s
        elif(str.endswith(('o', 'ch', 's', 'sh', 'x', 'z'))):
            pluralList.append(str + 'es') #for these cases, add an es
        elif(str.endswith('y')):
            pluralList.append(str[:-1] + 'ies') #for this case, change y to ies
        else: #no special cases, just add an s
            pluralList.append(str + 's')
    return pluralList


prompt = "Please enter a list of space separated words to be made plural: "
lst = input(prompt) #get user input of string list

print(plural(lst)) #print the plural words