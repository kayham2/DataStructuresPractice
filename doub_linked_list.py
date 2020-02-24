class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
	def append(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			new_node.prev = None
			return
		else:
			current = self.head
			while current.next:
				current = current.next
			new_node.prev = current
			new_node.next = None
			current.next = new_node
		return

	def prepend(self, data):
		pass
	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.print_list()