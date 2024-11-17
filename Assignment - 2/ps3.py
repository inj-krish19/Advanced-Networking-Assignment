"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 3 : Create a TCP client server program where the client sends a string, server calculates the length and replies

-----------------------------------------------------------------

"""

import socket

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Create a TCP client server program where the client sends a string, server calculates the length and replies"

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )

server.listen(1)

print( f"\nQuestion : {question}\n" )

clients = []

print( f"\nServer Is Running On {host}:{port}\n" )

client,client_address = server.accept()

if client_address not in clients:
    clients.append( client_address)
    print( f"Connected With : {client_address}" ) 
    
while message != "Bye" and reply.decode( encoder ) != "Bye" :
    
    reply = client.recv( 1024 )
    
    print( f"\nClient {client_address} : {reply.decode() }")
    
    message = f"Length Of {reply.decode()} Is " + str( len( reply.decode( encoder ) ) )
 
    client.send( message.encode() )
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Create a TCP client server program where the client sends a string, server calculates the length and replies


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 56389)

Client ('127.0.0.1', 56389) : hello

Client ('127.0.0.1', 56389) : what

Client ('127.0.0.1', 56389) : you are returning length

Client ('127.0.0.1', 56389) : nice i like this feature or question

Client ('127.0.0.1', 56389) : Bye

"""        