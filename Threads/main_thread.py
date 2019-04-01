import threading

if __name__ == '__main__':

	thread_name = threading.current_thread().getName()

	# print thread name
	print(thread_name)

	# switch thread name and make sure it was assigned properly
	threading.current_thread().name = "Coco"
	print('new name: ', threading.current_thread().name)

	# check step to see if main thread is running
	if threading.current_thread() == threading.main_thread():
		for num in range(10):
			if num % 2 == 0:
				print(num)
