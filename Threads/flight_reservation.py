from threading import Thread, Lock, Semaphore


# create a flight reservation class to purchase tickets
class FlightReservation:
	# create a lock for a given thread. Can use the Lock class or the
	# Semaphore class.

	# lock = Lock()
	lock = Semaphore()

	def __init__(self, tickets_left):
		self.tickets_left = tickets_left

	# acquire / set the thread lock
	lock.acquire()

	def buy(self, tickets_requested):
		if self.tickets_left >= tickets_requested:
			print('Your purchase is authorized')
			self.tickets_left -= tickets_requested
		else:
			print('You requested too many tickets!')

	# release the lock
	lock.release()


# we could run into problems in this scenario as all threads are calling the
# same object in parallel. This means all requests could get in before ticket
# totals are updated.
reservations = FlightReservation(15)

thread_1 = Thread(target=reservations.buy, args=[5])
thread_2 = Thread(target=reservations.buy, args=[6])
thread_3 = Thread(target=reservations.buy, args=[5])

thread_1.start()
thread_2.start()
thread_3.start()
