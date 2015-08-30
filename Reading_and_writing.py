# r - read mode (the file is opened for reading)
# w - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)
# a - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)

# f = open('input.txt', 'r')
# his code told Python to open the file input.txt in r mode and store the result of this operation in a file object called f.

f = open('example.txt', 'r')
i = 0
text = f.readlines()
length = len(text)

while i <= length:
	if i%2==1:
		print text[i]
		i = i +1
	else:
		i = i + 1


