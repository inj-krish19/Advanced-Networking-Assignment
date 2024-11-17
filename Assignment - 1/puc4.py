from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
domain = "www.example.com"

client = socket( AF_INET, SOCK_DGRAM )

client.connect( (host, port) )

print( f"\nClient is pinging at {host}:{port}")

print( f"\nYou : {domain}")

client.sendto( domain.encode( encoder ) , (host, port) )

domain, server_address = client.recvfrom( 1024 )

print( f"\nServer : {domain.decode( encoder )} ")

"""

Client is pinging at localhost:65432

You : www.example.com

Server : www.example.com 's ip is 192.0.2.1 

"""