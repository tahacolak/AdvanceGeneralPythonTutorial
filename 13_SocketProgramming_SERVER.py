'''
@author: tahacolak
'''
#Theoritical Informations will be added!

import socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Address Family tells us to IPv4 Adress Info and TCP Protocol Info 

#statically assigning
#local_host="127.0.01" 

#socket_host=socket.gethostname()#hostname

socket_host=socket.gethostbyname(socket.gethostname())
socket_port=12345
print(socket_host)

#Client Connection:
server_socket.bind(socket_host,socket_port)

server_socket.listen() #listen to Clients' Line-Demand

while(True):
    client_socket,client_addr=server_socket.accept()

    print(f"Connection is established->{client_addr}")

    print(client_socket,client_addr)

    client_socket.send("hello fellas".encode("utf-8"))
    server_socket.close()
    break #finish duration of listening
#for now, if you implement all of these codes successfully you shall go to project location
