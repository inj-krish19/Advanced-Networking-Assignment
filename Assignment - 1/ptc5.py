from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
message = "192.0.2.1"

client = socket( AF_INET, SOCK_STREAM )

client.connect( (host, port ))

print( f"\nServer started at {host}:{port}")

print( f"\nYou : {message}")

client.send( message.encode( encoder) )

message = client.recv(1024)

print( f"\nServer : {message.decode(encoder)} ")

"""

Server started at localhost:65432

You : 192.0.2.1

Server : 192.0.2.1 's ip is 00:1A:2B:3C:4D:5E 

"""