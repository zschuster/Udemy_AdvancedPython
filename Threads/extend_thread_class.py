from threading import Thread
import threading


# create a class to build an asterisk pyramid
class ThreadPyramid(Thread):
	def run(self):
		print("Egyptian Pyramid")
		print(threading.current_thread().getName())
		for i in range(1, 11):
			print('* ' * i)


if __name__ == '__main__':

	pyramid = ThreadPyramid()
	print('pyramid.start\n')
	print(pyramid.start())
