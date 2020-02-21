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

	def split_list(self):
		new_list = CircularLinkedList()
		size = len(cllist)
		if size <= 1:
			return
		mid = size//2
		count = 0
		current1 = self.head
		prev = None
		while current1 and count < mid:
			count += 1
			prev = current1
			current1 = current1.next
			
		tmp = current1
		current2 = tmp
		prev.next = self.head
		
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

	def josephus_circle(self, step):
		current = self.head
		prev = None
		index = 1
		while len(self) > 1:
			while index < step:
				prev = current
				current = current.next
				index +=1
			if current	== self.head:
				self.head = prev
			print(f"REMOVED: {current.data}")
			prev.next = current.next
			current = prev.next
			index = 1

		return self.print_list()
		
	def is_circ_ll(self, input_list):
		current = input_list.head
		while current:
			current = current.next
			if current == None:
				return False
			elif current == self.head:
				return True

			


from LinkedList_new import LinkedList


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(8)


cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
# cllist.append(5)
# cllist.append(6)
# cllist.append(7)
# cllist.append(8)
# cllist.append(9)
# cllist.append(10)
# cllist.print_list()
# print ("\n")
# cllist.josephus_circle(2)


print(cllist.is_circ_ll(cllist))

