from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
message = "Hii i am pinging to Server"

client = socket( AF_INET, SOCK_DGRAM )

client.connect( (host, port) )

print( f"\nClient is pinging at {host}:{port}")

print( f"\nYou : {message}")

client.sendto( message.encode( encoder ) , (host, port) )

message, server_address = client.recvfrom( 1024 )

print( f"\nServer : {message.decode( encoder )} ")

"""

Client is pinging at localhost:65432

You : Hii i am pinging to Server

Server : Hii i am pinging to Server 's uppercase is HII I AM PINGING TO SERVER 

"""