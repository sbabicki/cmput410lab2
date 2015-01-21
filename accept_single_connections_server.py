# References Used:
#
# http://www.binarytides.com/python-socket-programming-tutorial/ 
# Article by Silver Moon
#
#

import socket

HOST = ''
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

while 1:
	
	# accept connection (blocking call)
	conn, addr = s.accept()
	
	#display client information
	print 'Connected with ' + addr[0] + ':' + str(addr[1])

	data = conn.recv(1024)
	reply = "OK..."+data
	
	# if (data != None)
	if not data:
		break
	conn.sendall(reply)

conn.close()
s.close()