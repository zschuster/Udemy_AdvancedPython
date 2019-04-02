from threading import Thread
import threading
import math


# create some function that takes 1 argument
def sqrt_num(x):
	"""
	Take the square root of x
	:param x: a list of real positive numbers
	:return: printed square roots of numbers in x
	"""
	print(threading.current_thread().getName(), 'has begun.')
	for num in x:
		print(math.sqrt(num))

	print(threading.current_thread().getName(), 'has ended.')


thread_1 = Thread(target=sqrt_num, args=[(1, 9, 16)])
thread_2 = Thread(target=sqrt_num, args=[(100, 225, 400)])
thread_1.start()
thread_2.start()

# This shows how it can be messy when multiple threads are running in parallel
