import socket

host = 'localhost'
port = 8080

# instantiate a socket class and bind to host and port
s = socket.socket()
s.bind((host, port))

# have server start listening on localhost:8080
s.listen(100)

# establish connection
conn, address = s.accept()

# send message to client upon request
# must send message in binary format, hence encode method
conn.send('You have successfully made a request!'.encode())

conn.close()
