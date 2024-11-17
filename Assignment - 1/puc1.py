from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
message = "Hii I am pinging at your address"

client = socket( AF_INET, SOCK_DGRAM )

client.connect( (host, port) )

print( f"\nClient wants to connect at {host}:{port}")

print( f"\nYou : {message}")

client.sendto( message.encode( encoder ), (host, port) )

message, server_address = client.recvfrom(1024)

print( f"\nServer : {message.decode(encoder)}")

"""

Client wants to connect at localhost:65432

You : Hii I am pinging at your address

Server : Hii I am pinging at your address

"""