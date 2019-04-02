import threading
from threading import Thread


# We will create our own class and target it with a new thread
class SquareNumbers:

	def __init__(self, numbers):
		self.numbers = numbers

	def square_numbers(self):
		if threading.current_thread().getName() == 'Thread-1':
			print([x**2 for x in self.numbers])
		else:
			print('This is not Thread-1!')


if __name__ == '__main__':

	# create an instance of our class
	to_square = SquareNumbers([num for num in range(1, 11)])
	thread = Thread(target=to_square.square_numbers)
	thread.start()
