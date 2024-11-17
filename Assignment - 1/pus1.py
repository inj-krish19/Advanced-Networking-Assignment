from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"

server = socket( AF_INET, SOCK_DGRAM )

server.bind( (host, port) )

print( f"\nServer started at {host}:{port}")

message, client_address = server.recvfrom( 1024 )

print( f"\nClient : {message.decode( encoder) }")

server.sendto( message.decode( encoder ).encode( encoder ) , client_address )

"""

Server started at localhost:65432

Client : Hii I am pinging at your address

"""