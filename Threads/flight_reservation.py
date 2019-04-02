from threading import Thread


# create a flight reservation class to purchase tickets
class FlightReservation:

	def __init__(self, tickets_left):
		self.tickets_left = tickets_left

	def buy(self, tickets_requested):
		if self.tickets_left >= tickets_requested:
			print('Your purchase is authorized')
			self.tickets_left -= tickets_requested
		else:
			print('You requested too many tickets!')


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
