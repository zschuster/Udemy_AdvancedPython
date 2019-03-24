
class EAO:
	def __init__(self, x=0):
		self.x = x

	def __str__(self):
		return "{}".format(self.x)

	def __iadd__(self, other):
		if other.__class__.__name__ == 'EAO':
			tmp = self.x + other.x
			return EAO(tmp)

		if other.__class__.__name__ == 'int':
			tmp = self.x + other.numerator
			return EAO(tmp)


if __name__ == '__main__':

	obj = EAO(5)
	obj1 = EAO(10)

	print("obj: {}".format(obj.x))
	print("obj1: {}".format(obj1.x))

	obj += obj1
	print("\nobj += obj1: {}".format(obj.x))

	obj2 = EAO(4)
	print("\nobj2: {}".format(obj2.x))
	obj2 += 6

	print("\nobj2 += int(6): {}".format(obj2.x))
