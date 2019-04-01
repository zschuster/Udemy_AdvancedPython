from threading import Thread
import threading
import numpy as np


# define a function that calls multiple functions to understand how python
# uses threads
def calling_function():
	exponentiate()
	log_exponentials()


def exponentiate():
	for num in range(5):
		print(2**num)
	print("exponentiate: ", threading.current_thread().getName())


def log_exponentials():
	for num in range(5):
		print(np.log(2**num))
	print("log_exponentials: ", threading.current_thread().getName())


t = Thread(target=calling_function)
print("__main__: ", threading.current_thread().getName())
t.start()
