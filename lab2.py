# References Used:
#
# http://www.binarytides.com/python-socket-programming-tutorial/ 
# Article by Silver Moon
#

import socket
from thread import *

HOST = "localhost"
PORT = 9999

# socket is created and socket descriptor is returned
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("\nSocket created\n")

# bind socket to a host and port
s.bind((HOST, PORT))
print("Socket bind complete\n")

# put socket in listening mode to listen for incoming connections
s.listen(10)
print("Socket now listening\n")

# 1 thread for each connected client
def client_thread(conn):
	
	#conn.send("Welcome message\n")
	
	while 1:
		
		# recieve data from client
		data = conn.recv(1024)
		reply = data[:-2] + " Sasha\r\n"
		if not data:
			break
		
		# send reply if data is recieved	
		conn.sendall(reply)
	
	# close the connection with that client
	conn.close()
	
while 1:

	# accept connection (blocking call)
	conn, addr = s.accept()

	#display client information
	print 'Connected with ' + addr[0] + ':' + str(addr[1])
	
	# starts new thread
	# args -> 1) function to be run, 2) tuple of args for that function
	start_new_thread(client_thread, (conn,))

# close the socket	
s.close()