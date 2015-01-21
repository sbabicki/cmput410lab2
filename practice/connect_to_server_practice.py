# References Used:
#
# http://www.binarytides.com/python-socket-programming-tutorial/ 
# Article by Silver Moon
#
#

import socket

def create_socket():
	
	# socket is created and socket descriptor is returned
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	return s

# connect socket s to host at port	
def connect(s, host, port):
	
	# get the ip address of a given remote host
	remote_ip = socket.gethostbyname(host)
	
	# connect to ip on a given port
	s.connect((remote_ip, port))
	print ("\nSocket connected to "+host+" (IP address: "+remote_ip+") on port %d\n" %port)

# send GET request for given location
def send_get_request(s, path):
	
	# send data
	message = "GET "+path+" HTTP/1.1\r\n\r\n"
	s.sendall(message)
	print ("Message \""+message[:-4]+"\" sent\n")
	
	# recieve data
	reply = s.recv(4096)
	print("Reply:\n"+reply)

	
	
if __name__ == '__main__':
	
	s = create_socket()
	connect(s, "www.google.ca", 80)
	send_get_request(s, "/")
	
	# close the socket
	s.close