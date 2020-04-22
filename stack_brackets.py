### Checking to see if the brackets are matched
import sys
from stack1 import Stack

string1 = sys.argv[1]

def is_match(x):
	if x == "}" and s1.peek() == "{":
		return True
	elif x == "]" and s1.peek() == "[":
		return True
	elif x == ")" and s1.peek() == "(":
		return True
	else:
		return False

s1 = Stack()
for char in string1:
	if char is None:
		break
	elif char in "{[(":
		s1.push(char)
	elif is_match(char):
		s1.pop()

if s1.is_empty() and string1 != "":
	print("Balanced")
else:
	print("Not Balanced")
