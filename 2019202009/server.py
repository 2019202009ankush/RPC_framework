import socket, threading,sys
class handle_req(threading.Thread):
	def __init__(self,addr,sock):
		threading.Thread.__init__(self)
		self.self_socket = sock
		self.add=addr
	def sum(self,a,b):
		a=int(a)
		b=int(b)
		return a+b
	def mul(self,a,b):
		a=int(a)
		b=int(b)
		return a*b
	def div(self,a,b):
		a=int(a)
		b=int(b)
		return a/b
	def minus(self,a,b):
		a=int(a)
		b=int(b)
		return a-b
	def run(self):
		msg = ''
		while True:
			data = self.self_socket.recv(2048)
			msg = data.decode()
			#server sekleton
			if 'sum' in msg:
				lis=msg.split()
				c=self.sum(lis[1],lis[2])
				self.self_socket.send(str(c).encode())
			elif 'mul' in msg:
				lis=msg.split()
				c=self.mul(lis[1],lis[2])
				self.self_socket.send(str(c).encode())
			elif 'minus' in msg:
				lis=msg.split()
				c=self.minus(lis[1],lis[2])
				self.self_socket.send(str(c).encode())
			elif 'div' in msg:
				lis=msg.split()
				c=self.div(lis[1],lis[2])
				self.self_socket.send(str(c).encode())
HOST =''
PORT = 9851
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
while True:
	server.listen(1)
	sock, addr = server.accept()
	nth = handle_req(addr, sock)
	nth.start()
