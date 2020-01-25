import socket,pdb
PORT=9851

def make_socket(add):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.setblocking(0)
	s.bind(add)
	s.listen(MAX_CLIENTS)
	print("Opened connection is",add)
	return s
class Request:
    def __init__ (self):
		self.request={}
	def handle_incoming_request(soc,msg):
		if "add" in msg:
			soc.send('')
