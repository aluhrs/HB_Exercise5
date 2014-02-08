# open the file and read it
f = open("twain.txt")
filetext = f.read(1)

# loop through each letter
# count each time a letter appears
# print the counts on the screen
# in alphabetical order

counter = 0

for char in filetext:
	if ord(string.lower(char)) == ord(string.lower(char)):
		
		counter =+ 1
	else:	
		print 0
print counter	


f.close()