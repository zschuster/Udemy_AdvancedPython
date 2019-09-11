import tkinter as tk
from threading import Thread
import socket


def receive():
	while True:
		try:
			msg = sock.recv(1024).decode('utf8')
			msg_list.insert(tk.END, msg)
		except ConnectionError:
			print('There is an error while receiving message')
			break


def send():
	msg = my_msg.get()
	my_msg.set('')

	# send message to server
	sock.send(bytes(msg, 'utf8'))

	if msg == '#quit':
		sock.close()
		window.quit()


def on_closing():
	my_msg.set('#quit')
	send()


# create chat room GUI
window = tk.Tk()
window.title('Chat Room')

# set background color
window.configure(bg='gray')

# create a frame for messages
message_frame = tk.Frame(window, height=100, width=100, bg='white')

my_msg = tk.StringVar()
my_msg.set('')

scroll_bar = tk.Scrollbar(message_frame)

msg_list = tk.Listbox(
	message_frame, height=15,
	width=100, bg='white',
	yscrollcommand=scroll_bar.set
)

scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
message_frame.pack()

button_label = tk.Label(
	window, text='Enter your message here!',
	fg='blue', font='aerial', bg='white'
)
button_label.pack()

entry_field = tk.Entry(window, textvariable=my_msg, fg='red', width=50)
entry_field.pack()

send_button = tk.Button(
	window, text='Send', bg='green',
	font='Aerial', fg='white', command=send
)
send_button.pack()

quit_button = tk.Button(
	window, text='Quit', bg='green',
	font='Aerial', fg='white', comman=on_closing
)
quit_button.pack()

window.protocol('WM_DELETE_WINDOW', func=on_closing)

host = '127.0.0.1'
port = 8080

sock = socket.socket()
sock.connect((host, port))

receive_thread = Thread(target=receive)
receive_thread.start()

tk.mainloop()
