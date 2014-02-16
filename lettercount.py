"""Write a program, lettercount.py, that opens a file named on the command line 
and counts how many times each letter occurs in that file. 
Your program should then print those counts to the screen, in alphabetical order.
display:
3
1
etc
"""

from sys import argv

script, filename = argv

# open the file and read it
# then close it
f = open(filename, "r")
filetext = f.read()
f.close()

# create an empty dictionary

d = {}

# loop through each character
# lowercase each character
# determine whether the char is a letter
# if the letter is in the dictionary
# add 1 to the values
# if the letter is not in the dictionary
# add it and assign it a value of 1

for char in filetext:
	lowercase = char.lower()
	if ord(lowercase) >= ord("a") and ord(lowercase) <= ord('z'):
		if d.get(lowercase):
			d[lowercase] += 1
		if not d.get(lowercase): 
			d[lowercase] = 1

# print the keys(frequency of the letters appearing in the text) on the screen
# in alphabetical order

for key in sorted(d.keys()):
	print "%d" % (d[key])


