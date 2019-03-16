
# Implement a singly linked list and traverse through said list

class Node:
    def __init__(self, dataval=None):
        self.data_value = dataval
        self.next_value = None


class SLinkedList:
    def __init__(self, head_value=Node()):
        self.head_value = head_value

    # add method to print out the elements of list
    def listprint(self):
        printval = self.head_value
        while printval is not None:
            print(printval.data_value)
            printval = printval.next_value


listl = SLinkedList(head_value=Node("Mon"))
# listl.head_value = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

# link the first and second nodes
listl.head_value.next_value = e2

# link second and third nodes
e2.next_value = e3

# traverse through list with listprint method
listl.listprint()

"""
Note that this implementation works poorly if the head_value of the first element
(node) is not set to something other than None
"""


