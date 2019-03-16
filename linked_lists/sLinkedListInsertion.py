
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None


class SLinkedList:
	def __init__(self):
		self.head = None

	# iterate over entire list and print each element
	def listprint(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next

	# insert element at beginning of list
	def insert_beg(self, data):
		new_node = Node(data)

		# make sure connections are proper
		new_node.next = self.head
		self.head = new_node

	# insert element at end of list
	def insert_end(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return
		# we need to get to the last node
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

	# insert element in between to nodes
	def insert_between(self, node, data):
		if node is None:
			print("Node is not in the list")
			return

		new_node = Node(data)

		# new_node will be put after node
		new_node.next = node.next
		node.next = new_node


# create and test singly linked list implementation
s_list = SLinkedList()
s_list.head = Node("Mon")
n2 = Node("Tue")
n3 = Node("Wed")

# make connections
s_list.head.next = n2
n2.next = n3

# test insert_beg
s_list.insert_beg("Sun")

# test insert_end
s_list.insert_end("Thurs")

# test insert_between
s_list.insert_between(s_list.head.next.next, "Tue night")

s_list.listprint()