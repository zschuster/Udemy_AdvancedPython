from threading import Thread
import threading


# we will print the current thread inside the function and outside the
# function to show how python uses threads.
def is_even():
	print('in function: ', threading.current_thread().getName())
	print(4 % 2 == 0)


t = Thread(target=is_even)
t.start()

print('in main script: ', threading.current_thread().getName())
