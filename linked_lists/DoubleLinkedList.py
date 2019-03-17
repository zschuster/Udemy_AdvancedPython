class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	# Add element to list
	def add(self, new_val):
		new_node = Node(new_val)

		# make sure connections are set properly
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	# insert data/node after 'node'
	def insert(self, prev_node, data):
		if prev_node is None:
			return

		new_node = Node(data)
		# make sure connections are proper
		new_node.next = prev_node.next
		prev_node.next = new_node
		new_node.prev = prev_node
		if new_node.next is not None:
			new_node.next.prev = new_node

	# append node to end of list
	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return

		# iterate over entire list to get last element
		last = self.head
		while last.next is not None:
			last = last.next

		# make sure connections are proper
		last.next = new_node
		new_node.prev = last

	# remove a given node
	def remove(self, node):
		# if node.prev is None:
		# 	self.x = node.next
		# else:
		if node.prev is not None:
			node.prev.next = node.next

		# if node.next is None:
		# 	self.y = node.prev
		# else:
		if node.next is not None:
			node.next.prev = node.prev

	# method to print out entire list (can start from node arg)
	def listprint(self, node = None):
		if node is None:
			node = self.head

		while node is not None:
			print(node.data)
			last = node
			node = node.next

d_list = DoublyLinkedList()

# add elements
d_list.add(12)
d_list.add(8)
d_list.add(62)

# insert element after 8
d_list.insert(d_list.head.next, 'inserted')

# append the data "appended"
d_list.append('appended')

# print out list to verify
d_list.listprint()

# remove the second node (data = 8 in that node)
print('\nremoving head.next from list\n')
d_list.remove(d_list.head.next)

# verify
d_list.listprint()