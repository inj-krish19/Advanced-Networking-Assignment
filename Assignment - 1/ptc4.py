from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
message = "www.example.com"

client = socket( AF_INET, SOCK_STREAM )

client.connect( (host, port ))

print( f"\nServer started at {host}:{port}")

print( f"\nYou : {message}")

client.send( message.encode( encoder) )

message = client.recv(1024)

print( f"\nServer : {message.decode(encoder)} ")

"""

Server started at localhost:65432

You : www.example.com

Server : www.example.com 's ip is 192.0.2.1 

"""