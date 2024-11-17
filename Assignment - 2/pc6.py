"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 6 : Clients sends a string, Server calculates Hash value and replies back to Client using TCP
    
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

    client.send( message.encode( encoder ) )     
    
    reply = client.recv(1024)
    
    print( f"\nServer : {reply.decode(encoder) }")
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------

Server Always Replies as same as input
You are connected with localhost:65432


You : hello world

Server : IFMMPXPSME1_J?dYg7nZ$5\

You : oh my god converting in hash

Server : PINZHPEDPOWFSUJOHJOIB

You : its amazing

Server : JUTBNB[JOHf\yW@1lyJHH

You : Bye

Server : #ZF@y
h"HP␦
?!6 9PX>

"""        