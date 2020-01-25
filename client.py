import socket
HOST = ""
PORT = 9851
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
  out_data = input()
  client.sendall(bytes(out_data,'UTF-8'))
  in_data =  client.recv(1024)
  print("From HOST :" ,in_data.decode())
client.close()
