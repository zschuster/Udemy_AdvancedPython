import socket

host = 'localhost'
port = 8080

# instantiate a socket class and bind to host and port
s = socket.socket()
s.bind((host, port))

# have server start listening on localhost:8080
s.listen(1)

print('the server is listening for client requests on port {}'.format(port))

# establish connection
conn, address = s.accept()
print('connection has been established from {}'.format(address))

# we will set the server up to return a requested file

try:
	file_name = conn.recv(1024)
	with open(file_name, 'rb') as file:
		read_file = file.read()
	conn.send(read_file)
	conn.close()
except LookupError:
	conn.send('File not found on server'.encode())
	conn.close()
