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

server = socket( AF_INET, SOCK_STREAM )

server.bind( (host, port) )

server.listen(1)

print( f"\nServer started at {host}:{port}")

client, client_address = server.accept()

message = client.recv(1024)

print( f"\nClient : {message.decode()}")

client.send( f"{message.decode(encoder)} 's ip is {dns_table.get(message.decode(encoder),'Domain Not Found')}".encode( encoder ) )

"""

Server started at localhost:65432

Client : www.example.com

"""