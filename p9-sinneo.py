
"""
@author: Samantha Inneo

Description: This function uses regular expressions to find all capitalized words in a text 
file and return them in alphabetical order. 
"""
import re
from string import punctuation


def removePunc(str): #function to remove punctuation as described in the assignment 8 spec
    punc_translator = str.maketrans({key: None for key in punctuation})
    cleanString = str.translate(punc_translator)
    return cleanString

prompt = "Please enter the name of the file: "
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()
    
words = dict() #dictionary to hold the words
for line in file:
    line = line.rstrip()
    line = removePunc(line) #I remove punctuation because the example had no punctuation in it.
    x = re.findall('[A-Z][a-z]\S*', line) #The RE that gets Capitalized words, but not ALL CAPS WORDS
    alpha = [] #I use this later to hold the list of words
    for innerlist in x:
        if type(innerlist) is list: #I do this to collapse the lists inward [['a', 'b'], ['c', 'd']] becaomes ['a', 'b', 'c', 'd']
                # If the element is of type list, iterate through the sublist
                for item in innerlist:
                    alpha.append(item)
        else: #if it is just one list, add each item to alpha list
            alpha.append(innerlist)
    for word in alpha:
        words[word]=words.get(word, 0) #for every word in the alpha list, add it to words dictionary
if(len(words) == 0): #nothing was added to the dictionary
    print("No capital letters found in the file.")
else:
    print(list(words.keys()))
