from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"

server = socket( AF_INET, SOCK_STREAM )

server.bind( (host, port) )

server.listen(1)

print( f"\nServer started at {host}:{port}")

client, client_address = server.accept()

message = client.recv(1024)

print( f"\nClient : {message.decode()}")

client.send( f"{message.decode(encoder)} 's length is {len(message.decode(encoder))}".encode( encoder ) )

"""

Server started at localhost:65432

Client : I am pinging at Server

"""