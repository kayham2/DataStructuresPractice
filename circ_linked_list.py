class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class CircularLinkedList:
	def __init__(self):
		self.head = None
	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			new_node.next = new_node
		else:
			current = self.head
			while current.next != self.head:
				current = current.next
			current.next = new_node
			new_node.next = self.head
		return

	def prepend(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			new_node.next = self.head
		else:
			current = self.head
			tail = self.head
			while tail.next != self.head:
				tail = tail.next
			new_node.next = current
			self.head = new_node
			tail.next = new_node
		return

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
			if current == self.head:
				break
		return

	def remove(self, key):
		if key == self.head.data:
			tail = self.head
			while tail.next != self.head:
				tail = tail.next
			tail.next = self.head.next
			self.head = tail.next
		else:
			current = self.head
			prev = None
			while current.next != self.head:
				prev = current
				current = current.next
				if current.data == key:
					prev.next = current.next
					return
		return

	def split_list(self, key):
		new_list = CircularLinkedList()
		size = len(cllist)
		if size <= 1:
			return

		current1 = self.head
		while current1.data != key:
			current1 = current1.next
		tmp = current1.next
		current2 = tmp
		current1.next = self.head
		
		while current2.next != self.head:
			new_list.append(current2.data)
			current2 = current2.next
		new_list.append(current2.data)	
		self.print_list()
		print('\n')
		new_list.print_list()
		return

	def __len__(self):
		current = self.head
		if not current:
			return 0
		else:
			count = 0
			while current:
				count += 1
				current = current.next
				if current == self.head:
					break
			return count
			







cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")

cllist.split_list("B")

