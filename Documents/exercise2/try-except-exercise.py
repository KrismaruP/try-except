# Making the file name be an input.
fname = input('Enter a file name: ')
try:
    fhand = open(fname)
#This line is going to traceback if that file doesn't exist, so we have it in a try and except block.
except: 
    print('File cannot be opened:', fname)
#If the line blows up, it will jump down into the except code.
    quit()
#quit is a special function that stops executing becuse you've detected some kind of an error. This is a way to termninate the entire Python program silently with no traceback.

count = 0
#count operation.
for line in fhand :
    line = line.rstrip()
    if line.startswith('From:') :
        count = count + 1
print('There were', count, 'For lines in', fname)