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
		return


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

	def delete_node(self, key):
		current = self.head
		prev = None
		while current:
			if current.data == key and current == self.head:
				if current.next is None:
					self.head = None
					current = None
					return
				nxt = current.next
				self.head = nxt
				current.next = None
				current = None
				return
			else:
				if current.data == key:
					if current.next is None:
						prev = current.prev
						prev.next = None
						current = None
						return
					prev = current.prev
					nxt = current.next
					prev.next = current.next
					nxt.prev = prev
					return
			current = current.next
		return

	def reverse(self):
		current = self.head
		tmp = None
		while current:
			tmp = current.prev
			current.prev = current.next
			current.next = tmp
			current = current.prev
		if tmp:
			self.head = tmp.prev
		return

	def remove_duplicates(self):
		current = self.head
		tmp = None
		dups = []
		while current:
			if current.data in dups:
				tmp = current.prev
				tmp.next = current.next
				if current.next:
					current.next.prev = tmp
			else:
				dups.append(current.data)
			current = current.next
		return

	def pairs_with_sums(self, sum_val):
		current = self.head
		pairs = []
		while current:
			tmp = current.next
			while tmp:
				if(tmp.data + current.data == sum_val):
					pairs.append(f"{current.data} and {tmp.data}")
					break
				else:
					tmp = tmp.next
			current = current.next
		return pairs

	def print_list(self):
		current = self.head
		while current:
			print(current.data, "Hi")
			current = current.next
		return


dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)



# dllist.add_before(0, 1)
# dllist.delete_node(2)
#dllist.reverse()
print(dllist.pairs_with_sums(0))

#dllist.print_list()