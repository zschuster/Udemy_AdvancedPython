import socket

host = 'localhost'
port = 8080

# create socket and connect to address that server is listening on
s = socket.socket()
s.connect((host, port))

# send a file name to the server
file_name = 'server_side_file.txt'
s.send(file_name.encode())

# receive file back from server
read_file = s.recv(1024)

# print contents of requested file
print('File Contents:\n{}'.format(read_file.decode()))
s.close()
