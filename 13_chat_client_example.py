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

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(address) #connect to address

while(True):
    message=client.recv(size_of_byte) #messages could be taken via client with receive "recv()" method

    if message==disconnect_message:
        client.send(disconnect_message.encode(format_information))
        print("Exiting!")
        break
    else:
        print(f"{message}\n")
        message=input("The message: ")
        client.send(message.encode(format_information))


client.close()