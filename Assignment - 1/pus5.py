from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"

arp_table = {
    "192.0.2.1": "00:1A:2B:3C:4D:5E",
    "192.0.2.2": "00:1A:2B:3C:4D:5F",
    "192.0.2.3": "00:1A:2B:3C:4D:60",
    "203.0.113.10": "00:1A:2B:3C:4D:61",
}

server = socket( AF_INET, SOCK_DGRAM )

server.bind( (host, port ))

print( f"\nServer started at {host}:{port}")

message, client_address = server.recvfrom(1024)

print( f"\nClient : {message.decode(encoder)}")

server.sendto( f"{message.decode(encoder)} 's ip is {arp_table.get(message.decode(encoder),'IP Address Not Found')}".encode( encoder ) , client_address )

"""

Server started at localhost:65432

Client : 192.0.2.1

"""