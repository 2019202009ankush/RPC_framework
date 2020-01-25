
def gen_code(lis):
    #client stub
    import socket
    HOST = ""
    PORT = 9851
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    out_data = lis[0]+" "+lis[1]+" "+lis[2]

    client.sendall(bytes(out_data,'UTF-8'))
    in_data =  client.recv(1024)
    client.close()
    f=open("temp.py","w")
    f.write("def fun"+"(a,b):\n")
    f.write("\t"+"return "+in_data.decode())
    f.close()
