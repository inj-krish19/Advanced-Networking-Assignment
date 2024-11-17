"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 1 : Create a TCP client server program where the client sends a string, server replies back the same string

-----------------------------------------------------------------

"""

import socket

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Create a TCP client server program where the client sends a string, server replies back the same string"

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )

server.listen(1)

print( f"\nQuestion : {question}\n" )

clients = []

print( f"\nServer Is Running On {host}:{port}\n" )

client,client_address = server.accept()

if client_address not in clients:
    print( f"Connected With : {client_address}" )  
    clients.append( client_address)

while message != "Bye" and reply.decode( encoder ) != "Bye":
    
    reply = client.recv(1024)

    print( f"\nClient {client_address} : {reply.decode( encoder )}")
    
    message = reply.decode( encoder )
    
    client.send( message.encode() )     
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Create a TCP client server program where the client sends a string, server replies back the same string


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 56087)

Client ('127.0.0.1', 56087) : Hello

Client ('127.0.0.1', 56087) : Hii

Client ('127.0.0.1', 56087) : Are you Copying

Client ('127.0.0.1', 56087) : What

Client ('127.0.0.1', 56087) : Nah You are boring me

Client ('127.0.0.1', 56087) : Bye

"""        