



from string import punctuation
from operator import itemgetter

def removePunc(str):
    punc_translator = str.maketrans({key: None for key in punctuation})
    cleanString = str.translate(punc_translator)
    return cleanString

def removeCaps(str):
    return str.lower()   
 

prompt = "Please enter the name of the file: "
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()

words = dict()
wordcount = 0 
for line in file:
    ''' this is the code given in the assignment to remove punctuation'''
    line = removeCaps(removePunc(line)).strip() #I use strip so new line characters are removed
    holder = line.split(" ")
    for word in holder:
        words[word] = words.get(word, 0) + 1   #add the line's sender into the senders dictionary or increment if it already exists
        wordcount +=1
        # print(word + ' is used ' + str(words[word]) + ' times in the file.') 

if(len(words) == 0):
    print('Your file is empty.')
else:
    print("The total number of words was " + str(wordcount))
    print("The total number of distinct words was " + str(len(words)))
    maximum = max(words, key=words.get) #finds the key with the highest value 
    print("The most used word is: " + maximum + " and it was used " + str(words[maximum]) + " times.")
    maxUsed=sorted(words.items(), key=itemgetter(1), reverse=True)
    slicer=slice(0,25)
    print("The 25 most common words are: ")
    for word in maxUsed[slicer]:
        print(word[0])

