## Convert an integer number to binary
from stack1 import Stack
import sys

s1 = Stack()
string = ""
number = int(sys.argv[1])
while number >=1:
	s1.push(number%2)
	number = number//2
	print(number)

while s1.is_empty() == False:
	string += str(s1.pop())

print(string)






