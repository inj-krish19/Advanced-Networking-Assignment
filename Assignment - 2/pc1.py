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

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

client.connect( ( host, port ) )

print( f"\nServer Always Replies as same as input\nYou are connected with {host}:{port} \n" )  

while message != "Bye" and reply.decode(encoder) != "Bye":
    
    message = input("\nYou : ")

    client.send( message.encode() )     
    
    reply = client.recv(1024)
    
    print( f"\nServer : {reply.decode(encoder) }")
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------

Server Always Replies as same as input
You are connected with localhost:65432


You : Hello

Server : Hello

You : Hii

Server : Hii

You : Are you Copying

Server : Are you Copying

You : What

Server : What

You : Nah You are boring me

Server : Nah You are boring me

You : Bye

Server : Bye

"""        