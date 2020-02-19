class Stack():
	def __init__(self):
		self.items = []
	def push(self, data):
		self.items.append(data)
	def is_empty(self):
		return self.items == []
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[-1]
	def get_stack(self):
		return self.items

# st1 = Stack()
# st1.push(3)
# st1.push(5)
# st1.push(6)
# st1.push(3)
# st1.push(5)
# st1.push(6)
# print(st1.get_stack())
