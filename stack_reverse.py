##Reverses a string using Stacks
from stack1 import Stack
import sys

string = sys.argv[1]
final = ""

s1 = Stack()
for char in string:
	s1.push(char)

while s1.is_empty() is False:
	final += s1.pop()
	

print(final)
