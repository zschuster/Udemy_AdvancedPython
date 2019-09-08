import socket

host = 'localhost'
port = 8080

# create socket and connect to address that server is listening on
s = socket.socket()
s.connect((host, port))

# get message from server (up to 1024 bytes)
message = s.recv(1024)

while message:
	print('message : {}'.format(message.decode()))

	# update message
	message = s.recv(1024)

s.close()
