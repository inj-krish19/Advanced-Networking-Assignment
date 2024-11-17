from socket import *

host = "localhost"
port = 65432
encoder = "utf-8"

dns_table = {
    "www.example.com": "192.0.2.1",
    "mail.example.com": "192.0.2.2",
    "ftp.example.com": "192.0.2.3",
    "www.example.org": "203.0.113.10",
}

server = socket( AF_INET, SOCK_DGRAM )

server.bind( (host, port ))

print( f"\nServer started at {host}:{port}")

message, client_address = server.recvfrom(1024)

print( f"\nClient : {message.decode(encoder)}")

server.sendto( f"{message.decode(encoder)} 's ip is {dns_table.get(message.decode(encoder),'Domain Not Found')}".encode( encoder ) , client_address )

"""

Server started at localhost:65432

Client : www.example.com

"""