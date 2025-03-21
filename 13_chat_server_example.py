'''
@author: tahacolak

Author Notes:
'''
import socket 

server_id=socket.gethostbyname(socket.gethostname())
port_number=40400 #assigning sample port number

address=(server_id,port_number)

format_information="utf-8"
size_of_byte=1024
disconnect_message="Q"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(address)
server.listen()

print("Server is being worked...")

client_socket, client_address=server.accept()
client_socket.send("Server connection is established!".encode("utf-8"))

while(True):
    message=client_socket.recv(size_of_byte) #messages could be taken via client with receive "recv()" method

    if message==disconnect_message:
        client_socket.send(disconnect_message.encode(format_information))
        print("Exiting!")
        break
    else:
        print(f"{message}\n")
        message=input("The message: ")
        client_socket.send(message.encode(format_information))


server.close()
