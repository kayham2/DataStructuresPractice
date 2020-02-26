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
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node
			new_node.prev = current
			new_node.next = None

	def prepend(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			new_node.prev = None
			new_node.next = None
		else:
			current = self.head
			self.head = new_node
			new_node.next = current
			current.prev = new_node
		return

	def add_after(self, data, key):
		new_node = Node(data)
		current = self.head
		while current:
			if current.next is None and current.data == key:
				self.append(new_node.data)
				return
			elif current.data == key:
				tmp = current.next
				current.next = new_node
				new_node.prev = current
				new_node.next = tmp
				tmp.prev = new_node
				return
			current = current.next
		return


	def add_before(self, data, key):
		new_node = Node(data)
		current = self.head
		while current:
			if current.prev is None and current.data == key:
				self.prepend(new_node.data)
				return
			elif current.data == key:
				tmp = current.prev
				tmp.next = new_node
				new_node.prev = tmp
				new_node.next = current
				current.prev = new_node
				return
			current	= current.next
		return
	

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next


dllist = DoublyLinkedList()
dllist.append("A")
dllist.append("B")
dllist.append("C")
dllist.append("D")
dllist.add_before("E", "A")

dllist.print_list()