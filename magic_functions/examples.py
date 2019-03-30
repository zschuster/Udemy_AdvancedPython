# create dictionary class that inherits from dict class
class Dictionary(dict):
	def __add__(self, other):
		self.update(other)
		return Dictionary(self)


if __name__ == '__main__':

	dict_1 = Dictionary({'name': 'Zach'})
	dict_2 = Dictionary({'hobby':'golf'})

	print(dict_1)
	print(dict_2)

	print('\n dict_1 + dict_2')
	print(dict_1 + dict_2)
