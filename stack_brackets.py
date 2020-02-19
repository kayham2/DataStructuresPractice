### Checking to see if the brackets are matched
from stack1 import Stack
import sys

def matched(bracket, bracket2):
	print(bracket, bracket2)
	if bracket == "{" and bracket2 == "}":
		return True
	elif bracket == "(" and bracket2 == ")":
		return True
	elif bracket == "[" and bracket2 == "]":
		return True
	else:
		return False

def balance_brackets(string):
	st1 = Stack()
	is_balanced = True
	index = 0
	while index < len(string) and is_balanced:
		char = string[index]
		if char in "{([":
			st1.push(char)
		else:
			if st1.is_empty():
				return False
			elif char not in "}])":
				pass
			elif matched(st1.pop(), char):
				is_balanced = True
			else:
				print("enter")
				return False
		index +=1

	if st1.is_empty():
		return is_balanced
	else:
		return False

	return is_balanced

if balance_brackets(sys.argv[1]):
	print("Balanced")
else:
	print("Not balanced")


