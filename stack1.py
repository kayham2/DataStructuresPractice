class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)
		return

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if self.is_empty():
			return
		else:
			return self.items[-1]

	def get_stack(self):
		return self.items



# stk1 = Stack()
# print(stk1.peek())
# stk1.push(1)
# stk1.push(2)
# stk1.push(3)
# stk1.pop()
# print(stk1.get_stack())
# print(stk1.peek())



