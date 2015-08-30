a = 42
if a < 10:
	print 'the number is less than 10'
else:
	print 'the number is greater or equal to 10'

b = 1

if a + b == 4:
	print 'printed when a + b equals 4'
print 'always printed'

greetings = 1
while greetings <= 3:
	print 'Hello! ' * greetings
	greetings = greetings + 1

names = ['Alice', 'Bob', 'Charley']
for name in names: 
	print 'Hello, ' + name

n = 10 # to repeat an action exactly n times
for i in range(n):
  print i

print range(5, 12) # print from 5 to 12 without including 12

# Problem: Given Two positive integers a and b (a < b < 10000)
# Return: The sum of all odd integers from a through b, inclusively

a = 4362
b = 8686
suma = 0
while a <= b:
	if a%2 == 1:
		suma = suma + a
		a = a + 1 
	else:
		a = a + 1
print suma



