class Node():
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Doubly_Linked_list():
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		current = self.head

		if self.head is None:
			new_node.prev = None
			new_node.next = None
			self.head = new_node

		else:
			while current.next:
				current = current.next
			current.next = new_node
			new_node.prev = current
			new_node.next = None
		return

	def prepend(self, data):
		new_node = Node(data)

		if self.head is None:
			new_node.prev = None
			new_node.next = None
			self.head = new_node
		else:
			current = self.head
			new_node.next = current
			current.prev = new_node
			new_node.prev = None
			self.head = new_node
		return

	def display_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
		return

	def delete (self, data):
		current = self.head
		prev = None
		if self.head is None:
			return
		elif self.head.next is None:
			self.head = None
			return
		elif self.head.data == data:
			self.head = self.head.next
			self.head.prev = None
		else:
			while current.next and current.data != data:
				prev = current
				current = current.next
			if current.data != data:
				return
			elif current.next is None:
				prev.next = None
				current.prev = None
			else:
				prev.next = current.next
				current.prev = None
				current.next = None
			return	

	def reverse(self):
		current = self.head
		prev = None
		while current:
			prev = current.prev
			current.prev = current.next
			current.next = prev
			current = current.prev
		if prev:
			self.head = prev.prev
		return

	def remove_duplicates(self):
		current = self.head
		prev = None
		li = []

		while current:
			if current.data in li:
				tmp = current.next
				prev.next = current.next
				current.next = None
				current.prev = None
				current = tmp
			else:
				li.append(current.data)
				prev = current
				current = current.next
		return

	def pairs_with_sums(self, number):
		current = self.head
		current2 = None
		pairs = list()

		while current.next:
			current2 = current.next
			while current2.next:
				if current.data + current2.data == number:
					pairs.append(f"({current.data}, {current2.data})")
				current2 = current2.next
			current = current.next
		return pairs


dllist = Doubly_Linked_list()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
# dllist.append(8)
# dllist.append(4)
# dllist.append(10)
# dllist.append(12)
# dllist.append(12)
dllist.display_list()

print("\n")

# dllist.delete(5)
# dllist.reverse()
# dllist.remove_duplicates()

print(dllist.pairs_with_sums(5))
# dllist.display_list()

