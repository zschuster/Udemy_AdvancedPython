import socket
from threading import Thread

clients = dict()
addresses = dict()

host = 'localhost'
port = 8080

s = socket.socket()
s.bind((host, port))


def broadcast(msg, prefix=''):
	# send message to all clients in chat
	for cl in clients:
		cl.send(bytes(prefix + msg, 'utf8'))


def handle_client(connection):

	# take in name that is inputted by client
	name = connection.recv(1024).decode('utf8')

	# send welcome message
	welcome_msg = 'Welcome, {}! You can type #quit to leave the chat room'.format(name)
	connection.send(bytes(welcome_msg, 'utf8'))

	# send message to all clients that new user is available
	broad_msg = name + ' has joined the chat room.'
	broadcast(broad_msg)

	# add client to dict
	clients[connection] = name

	# handle the message that client inputs
	while True:
		client_message = connection.recv(1024)

		if client_message != bytes('#quit', 'utf8'):
			broadcast(client_message.decode('utf8'), name + ': ')

		else:
			connection.send(bytes('You have left the chat room', 'utf8'))
			connection.close()
			del clients[connection]

			# let all clients know user has left
			broadcast('{} has left the chat'.format(name))


def accept_client_conns():
	while True:
		client_conn, client_address = s.accept()
		print('{} has connected'.format(client_address))

		# interface with incoming client
		client_conn.send('Welcome to the chat room! What is your name?'.encode('utf8'))
		addresses[client_conn] = client_address

		# create a thread for client
		Thread(target=handle_client, args=(client_conn, )).start()


if __name__ == '__main__':
	s.listen(5)
	print('The server is now listening at {}:{}'.format(host, port))

	t1 = Thread(target=accept_client_conns)
	t1.start()
	t1.join()
