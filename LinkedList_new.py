class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		#Append only if it's the first node
		if self.head == None:
			self.head = new_node
			return

		#Append to the end
		tail = self.head
		while tail.next:
			tail = tail.next
		tail.next = new_node

	def prepend(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		#prepend to an unempty list
		current = self.head
		new_node.next = current
		self.head = new_node
		return

	def print_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
		return

	def insert_after_val(self, val, data):
		new_node = Node(data)
		current = self.head
		if val == None or val == "":
			return
		while current and current.data != val:
			current = current.next
		new_node.next = current.next
		current.next = new_node
		return

	def del_node(self, val):
		if not val or val =="":
			return

		current = self.head
		#If node is head:
		if val==current.data:
			self.head = current.next
			return

		prev = None
		while current and current.data != val:
			prev = current
			current = current.next

		prev.next = current.next
		return

	def length(self):
		count = 0
		current = self.head

		while current:
			count +=1
			current = current.next
		return count

	def swap(self, node1, node2):
		if node1 == node2:
			return
		prev1 = None
		prev2 = None

		current1 = self.head
		current2 = self.head

		while current1 and current1.data != node1:
			prev1 = current1
			current1 = current1.next

		while current2 and current2.data != node2:
			prev2 = current2
			current2 = current2.next

		#if first node is the head
		if prev1 is None:
			self.head = current2
		else:
			prev1.next = current2

		#If second node is head
		if prev2 is None:
			self.head = current1
		else:
			prev2.next = current1

		temp = current2.next
		current2.next = current1.next
		current1.next = temp
		return

	def reverse_list(self):
		prev = None
		current = self.head

		while current:
			tmp = current.next
			current.next = prev
			prev = current
			current = tmp
		self.head = prev
		return self.head

	def merge_two_sorted(self, list2):
		new_list = LinkedList()
		current1 = self.head
		current2 = list2.head

		while current1 and current2:
			if current1.data >= current2.data:
				new_list.append(current2.data)
				current2 = current2.next
			else:
				new_list.append(current1.data)
				current1 = current1.next

		while current1:
			new_list.append(current1.data)
			current1 = current1.next
		while current2:
			new_list.append(current2.data)
			current2 = current2.next
		
		return new_list

	def remove_duplicates(self):
		current = self.head
		prev = None
		duplicates = {}

		while current:
			if current.data in duplicates:
				prev.next = current.next
			else:
				duplicates[current.data] = 1
				prev = current
			current = prev.next
	
		return self

	def nth_to_last(self, x):
		index = 0
		a = b = self.head
		while index < x:
			b = b.next
			index += 1

		while b:
			a = a.next
			b = b.next
		return print(a.data)

	def count_occurences(self, data):
		current = self.head
		count = 0

		while current:
			if current.data == data:
				count +=1
			current = current.next
		return count

	def rotate(self, key):
		tmp = self.head
		current = self.head
		prev = None
		index = 0
		while index < key:
			prev = current
			current = current.next
			index += 1

		self.head = current
		prev.next = None
		tail = current
		while tail.next:
			tail = tail.next

		tail.next = tmp
		return self

	def is_palindrome(self):
		current = self.head
		llist = []
		is_pal = True
		while current:
			llist.append(current.data)
			current = current.next

		current = self.head
		while current:
			if current.data == llist[-1]:
				is_pal = True
				llist.pop()
			else:
				is_pal = False
				break
			current = current.next
		
		return is_pal

	def tail_to_head(self):
		current = self.head
		tail = self.head
		prev = None
		while tail.next:
			prev = tail
			tail = tail.next

		tail.next = current
		prev.next = None
		self.head = tail
		return self

	def sum_two_list(self, list1):
		string1 = ""
		string2 = ""
		current1 = self.head
		current2 = list1.head

		while current1:
			string1 += str(current1.data)
			current1 = current1.next

		while current2:
			string2 += str(current2.data)
			current2 = current2.next

		return(int(string1[::-1])+int(string2[::-1]) )




llist = LinkedList()
# llist.prepend("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.insert_after_val("D", "E")
# #llist.del_node("A")
# #llist.swap("A", "C")
# llist.reverse_list().print_list()

# llist.append(1)
# llist.append(5)
# llist.append(7)
# llist.append(9)
# llist.append(10)

# llist2 = LinkedList()
# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)

# x = llist.merge_two_sorted(llist2)
# x.print_list()

# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
# llist.append(7)

# llist.rotate(3).print_list()

# llist.append("R")
# llist.append("A")
# llist.append("C")
# llist.append("E")
# llist.append("C")
# llist.append("A")
# llist.append("R")


# print(llist.is_palindrome())


# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# llist.tail_to_head().print_list()

llist.append(5)
llist.append(6)
llist.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(llist.sum_two_list(llist2))






