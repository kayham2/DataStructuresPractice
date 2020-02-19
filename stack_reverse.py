##Reverses a string using Stacks
from stack1 import Stack
import sys

def reverse_str(string):
	final = ""
	st1 = Stack()

	for char in string:
		st1.push(char)
	while st1.is_empty() == False:
		final += str(st1.pop())

	return final

print(reverse_str(sys.argv[1]))