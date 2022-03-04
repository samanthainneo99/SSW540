"""
@author: Samantha Inneo

Description: This assignment takes in user input of a file name, and calculates the average DSPAM confidence by
    finding the correct lines in the file and computing the average.
"""
#This function computes the average of a list of numbers
def averagenum(nums):
    total = 0
    for num in nums:
        total += num
    total= total/len(nums)    
    return total



prompt = "Please enter the name of the file:"
filename = input(prompt) #captures the users name and stores it in 'name' for use later


try: #makes sure the file opens correctly
    file = open(filename)
except FileNotFoundError:
    print('File cannot be opened:', filename)
    exit()

numbers = [] 
for line in file:
    #strips the tailing characters
    line = line.rstrip()
    if line.find('X-DSPAM-Confidence: ', 0, len(line)) != -1: #checks if each line in the file is the DSPAM Confidence
        numbers.append(float(line[20:])) #add the line's DSPAM Confidence into the numbers list so I can find the average


print('Average spam confidence: ' + str(averagenum(numbers)))
