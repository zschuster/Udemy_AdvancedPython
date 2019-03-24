
# The purpose of this script is to get acquainted with unary operator methods

class Operations:
	def __init__(self, *args):
		if len(args) == 0:
			self.numbers = (0, 0)
		else:
			self.numbers = args

	def __add__(self, other):
		added = tuple(x + y for x, y in zip(self.numbers, other.numbers))
		return Operations(*added)

	def __mul__(self, other):
		mul = (x * y for x, y in zip(self.numbers, other.numbers))
		return Operations(*mul)


if __name__ == '__main__':
	# using class Addition

	# define objects for addition
	obj1 = Operations(3, 4, 5)
	obj2 = Operations(7, 8, 9)

	print("Addition")
	print((obj1 + obj2).numbers)

	# define objects for multiplication
	obj3 = Operations(3, 3, 3)
	obj4 = Operations(5, 6, 7)

	print("\nMultiplication")
	print((obj3 * obj4).numbers)
