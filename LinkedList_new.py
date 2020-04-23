class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		current = self.head
		if self.head is None:
			self.head = new_node
			return
		else:
			while current.next:
				current = current.next
			current.next = new_node
			new_node.next = None
			return	

	def prepend(self, data):
		new_node = Node(data)
		current = self.head
		if self.head is None:
			self.head = new_node
			return
		else:
			new_node.next = current
			self.head = new_node
			return

	def display_list(self):
		current = self.head
		while current:
			print(current.data)
			current = current.next
		return

	def insert_after_node(self, data1, data2):
		new_node = Node(data2)
		current = self.head

		while current.data != data1 and current.next:
			current = current.next
		if current.data != data1:
			return
		if current.next is None:
			new_node.next = None
		else:
			new_node.next = current.next
		current.next = new_node
		return

	def deletion(self, data1):
		current = self.head
		if self.head.data == data1:
			self.head = self.head.next
			return
		else:
			while current.data != data1 and current.next:
				tmp = current
				current = current.next
			if current.data != data1:
				return
			else:
				tmp.next = current.next
			return

	def deletion_position(self, index):
		count = 0
		x = 0
		current = self.head
		while current:
			current = current.next
			count +=1
		if index > count-1 or index < 0:
			return
		elif index == 0:
			self.head = self.head.next
			return
		current = self.head
		while x < index and current.next:
			tmp = current
			current = current.next
			x += 1
		tmp.next = current.next
		return

	def length(self):
		count = 0
		current = self.head
		while current:
			count +=1
			current = current.next
		return count

	def length_rec(self, node):
		if node is None:
			return 0
		return 1 + self.length_rec(node.next)

	def node_swap(self, data1, data2):
		prev1 = None
		current1 = self.head

		prev2 = None
		current2 = self.head

		if data1==data2:
			return

		while current1.data != data1 and current1.next:
			prev1 = current1
			current1 = current1.next

		while current2.data != data2 and current2.next:
			prev2 = current2
			current2 = current2.next

		if not current1 or not current2:
			return

		#if One of the nodes is the head node

		if prev1:
			prev1.next = current2
		else:
			self.head = current2

		if prev2:
			prev2.next = current1
		else:
			self.head = current1

		current1.next, current2.next = current2.next, current1.next
		return

	def reverse(self):
		current = self.head
		prev = None
		temp = None

		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		self.head = prev

	def merge_sorted_lists(self, s_list):
		new_list = LinkedList()
		cur1 = self.head
		cur2 = s_list.head

		if cur1.data < cur2.data:
			new_list.append(cur1.data)
			cur1 = cur1.next
		else:
			new_list.append(cur2.data)
			cur2 = cur2.next

		while cur1 and cur2:
			if cur1.data < cur2.data:
				new_list.append(cur1.data)
				cur1 = cur1.next
			else:
				new_list.append(cur2.data)
				cur2 = cur2.next

		while cur1:
			new_list.append(cur1.data)
			cur1 = cur1.next
		while cur2:
			new_list.append(cur2.data)
			cur2 = cur2.next
		return new_list

	def remove_duplicates(self):
		li = []
		current = self.head
		prev = None
		while current:
			if current.data in li:
				prev.next = current.next
				current = current.next
			else:
				li.append(current.data)
				prev = current
				current = current.next
		return

	def nth_to_last(self, key):
		current = self.head
		index = self.length() - key
		while index > 0 and current:
			current = current.next
			index -= 1
		return current.data

	def count_occurences(self, val):
		current = self.head
		count = 0

		while current:
			if current.data==val:
				count += 1
			current = current.next

		return count

	def rotate(self, key):
		current = self.head
		tail = self.head

		while current.data != key and current:
			current = current.next

		while tail.next:
			tail = tail.next

		if not current:
			return

		tail.next = self.head
		self.head = current.next
		current.next = None

	def is_palindrome(self):
		current = self.head
		string = ""

		while current:
			string += current.data
			current = current.next

		return string == string[::-1]

	def move_tail_to_head(self):
		current = self.head
		prev = None
		while current.next:
			prev = current
			current = current.next
		current.next = self.head
		prev.next = None
		self.head = current
		return

	def sum_two_lists(self, l2):
		cur1 = self.head
		cur2 = l2.head

		sum_list = LinkedList()
		carry = 0
	
		while cur1 or cur2:
			if cur1:
				i = cur1.data
			else:
				i = 0
			if cur2:
				j = cur2.data
			else:
				j = 0


			s = i + j + carry

			if s > 10:
				carry = 1
				remainder = s%10
				sum_list.append(remainder)
			else:
				carry = 0
				sum_list.append(s)

			if cur1:
				cur1 = cur1.next
			if cur2:
				cur2 = cur2.next

		if cur1 is None and cur2 is None:
			if carry == 1:
				sum_list.append(carry)
		return sum_list.display_list()





llist = LinkedList()
llist2 = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.prepend(0)
# llist.insert_after_node(1, 1.5)
# llist.display_list()
#llist.deletion(2)
#llist.deletion_position(1)
# print("\n")
#print(llist.length_rec(llist.head))
#llist.node_swap(0, 1.5)
#llist.reverse()

llist.append(5)
llist.append(6)
llist.append(3)
llist2.append(8)
llist2.append(4)
llist2.append(9)

# llist2.append(2)
# llist2.append(3)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)
# llist2.display_list()
# print("\n")
# (llist.merge_sorted_lists(llist2)).display_list()

llist.display_list()
print("\n")
llist2.display_list()
# llist.remove_duplicates()
# print(llist.nth_to_last(9))
# print(llist.count_occurences(1))

# llist.rotate(3)
# llist.display_list()
# print(llist.is_palindrome())
# llist.move_tail_to_head()
print("\n")
llist.sum_two_lists(llist2)









