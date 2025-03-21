'''
@author: tahacolak
'''
#Theoritical Informations will be added!
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


socket_host=socket.gethostbyname(socket.gethostname())
socket_port=12345
client_socket.connect(socket_host,socket_port)

message=client_socket.recv(1024)

print(message.decode("utf-8"))

client_socket.close()