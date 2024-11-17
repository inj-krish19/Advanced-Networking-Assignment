"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 2 : Create a TCP client server program where the client sends a string, server converts to upper case and replies

-----------------------------------------------------------------

"""

import socket

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Create a TCP client server program where the client sends a string, server converts to upper case and replies"

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )

server.listen(3)

print( f"\nQuestion : {question}\n" )

clients = []

client,client_address = server.accept()

print( f"\nServer Is Running On {host}:{port}\n" )

if client_address not in clients:
    print( f"Connected With : {client_address}" )
    clients.append( client_address )

while message != "Bye" and reply.decode( encoder ) != "Bye":
    
    reply = client.recv( 1024 )
    
    print( f"\nClient {client_address} : {reply.decode(encoder)}")
    
    message = reply.decode( encoder ).upper()
    
    client.send( message.encode() )
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Create a TCP client server program where the client sends a string, server converts to upper case and replies


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 56091)

Client ('127.0.0.1', 56091) : hii

Client ('127.0.0.1', 56091) : hello

Client ('127.0.0.1', 56091) : what

Client ('127.0.0.1', 56091) : are you just giving me uppercase

Client ('127.0.0.1', 56091) : ohk i got it. but you are boring me

Client ('127.0.0.1', 56091) : bye

Client ('127.0.0.1', 56091) : Bye

"""        