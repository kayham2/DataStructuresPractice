from LinkedList_new import LinkedList

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class CircularLinkedList():
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		tail = self.head
		if self.head is None:
			self.head = new_node
			new_node.next = self.head
		else:
			while tail.next is not self.head:
				tail = tail.next
			tail.next = new_node
			new_node.next = self.head
		return

	def prepend(self, data):
		new_node = Node(data)
		tail = self.head
		while tail.next is not self.head:
			tail = tail.next
		new_node.next = self.head
		tail.next = new_node
		self.head = new_node
		return

	def display_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
			if current is self.head:
				break
		return

	def remove_node(self, data):
		tail = self.head
		current = self.head
		prev = None
		while tail.next is not self.head:
			tail=tail.next

		if self.head.data == data:
			self.head = self.head.next
			tail.next = self.head
			return

		while current.next != self.head and current.data != data:
			prev = current
			current = current.next
		prev.next = current.next
		return

	def length(self):
		current = self.head
		count = 1
		while current.next is not self.head:
			count +=1
			current = current.next
		return count

	def split_list(self):
		if self.length() == 0:
			return
		elif self.length()==1:
			return self.head

		current = self.head
		prev = None
		x = self.length()//2
		while x > 0:
			prev = current
			current = current.next
			x = x-1
		prev.next = self.head
		
		new_list = CircularLinkedList()
		
		while current.next is not self.head:
			new_list.append(current.data)
			current = current.next
		new_list.append(current.data)

		self.display_list()
		print("\n")
		new_list.display_list()
		return 

	def josephus(self, step):
		current = self.head

		while current:
			x = 1
			while x< step:
				current = current.next
				x +=1
			tmp = current.next
			self.remove_node(current.data)
			self.head = tmp
			current = tmp

			if self.length() ==1:
				break
		return

	def is_circular_linked_list(self, li):
		current = li.head
		while current:
			current = current.next
			if current == li.head:
				return True
				break
		return False


cllist = CircularLinkedList()
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.prepend("A")
cllist.append("E")
cllist.append("F")
cllist.append("G")
cllist.append("H")
cllist.append("I")
cllist.append("J")
cllist.append("K")
# cllist.append(1)
# cllist.append(2)
# cllist.append(3)
# cllist.append(4)
#cllist.display_list()

# cllist.remove_node("C")
#print("\n")

# cllist.josephus(2)
print(cllist.is_circular_linked_list(cllist))
#cllist.display_list()

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(cllist.is_circular_linked_list(llist))


# cllist.split_list()




