from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"
domain = "192.0.2.1"

client = socket( AF_INET, SOCK_DGRAM )

client.connect( (host, port) )

print( f"\nClient is pinging at {host}:{port}")

print( f"\nYou : {domain}")

client.sendto( domain.encode( encoder ) , (host, port) )

domain, server_address = client.recvfrom( 1024 )

print( f"\nServer : {domain.decode( encoder )} ")

"""

Client is pinging at localhost:65432

You : 192.0.2.1

Server : 192.0.2.1 's ip is 00:1A:2B:3C:4D:5E 

"""