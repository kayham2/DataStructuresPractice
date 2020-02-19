## Convert an integer number to binary
from stack1 import Stack
import sys

def int_to_bin(number):
	st1 = Stack()
	string = int(number)
	bin_num = ""
	while string >= 1:
		st1.push(str(string%2))
		string = string//2
	while st1.is_empty() == False:
		bin_num += st1.pop()
	return bin_num

print(int_to_bin(sys.argv[1]))




