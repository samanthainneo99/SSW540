"""
@author: Samantha Inneo

Description: This function takes in a text file and reads each line to calculate total words,
    total distinct words, the top 25 most frequent words and counts, and character frequency.
"""

from string import punctuation
from operator import itemgetter

def removePunc(str): #function to remove punctuation as described in the assignment spec
    punc_translator = str.maketrans({key: None for key in punctuation})
    cleanString = str.translate(punc_translator)
    return cleanString

def removeCaps(str): #function to remove uppercase letters as described in the assignment spec
    return str.lower()   
 

prompt = "Please enter the name of the file: "
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()

words = dict() #this dictionary will hold all the words
letters = dict() #this dictionary will keep track of letter usage
wordcount = 0 #increments for every new word, since dictionary doesn't have repeats
for line in file:
    line = removeCaps(removePunc(line)).strip() #I use strip so new line characters are removed, calling two functions above
    holder = line.split(" ") #list that temporarily holds each line's content, split on spaces
    for word in holder:
        words[word] = words.get(word, 0) + 1   #add the line's sender into the senders dictionary or increment if it already exists
        wordcount +=1 #increment the total word count
        for letter in word: #while looking at each word, add or increment the value for each letter            
            letters[letter] = letters.get(letter, 0) + 1


if(len(words) == 0): #checks if there were any lines in the file
    print('Your file is empty.')
else:
    print("The total number of words was: " + str(wordcount)) #print the wordcount
    print("The total number of distinct words was: " + str(len(words))) #print the size of the dictionary
    maximum = max(words, key=words.get) #finds the key with the highest value 
    print("The most used word is: " + maximum + ". It was used " + str(words[maximum]) + " times.\n\n") #print the most used word and its usage

    maxUsedWords=sorted(words.items(), key=itemgetter(1), reverse=True) #sort the dictionary on value, not key
    print("The 25 most common words are: ")
    for word in maxUsedWords[slice(0,25)]: #print the first 25 most used words
        print(word)
    print("\n\n")

    maxUsedLetters=sorted(letters.items(), key=itemgetter(1), reverse=True) #sort the dictionary on value, not key
    print("The character frequency is: ")  
    for letter in maxUsedLetters: #print the value sorted letter dictionary
        print(letter)

