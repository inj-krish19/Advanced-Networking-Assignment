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

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

client.connect( ( host, port ))

print( f"\nServer Always Replies with length of your input\nYou are connected with {host}:{port} \n" )  
    
while message != "Bye" and reply.decode( encoder ) != "Bye" :
    
    message = input("\nYou : ")
    
    client.send( message.encode() )
    
    reply = client.recv( 1024 )
    
    print( f"\nServer : {reply.decode( encoder ) }")
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Server Always Replies with length of your input
You are connected with localhost:65432


You : hello

Server : Length Of hello Is 5

You : what

Server : Length Of what Is 4

You : you are returning length

Server : Length Of you are returning length Is 24

You : nice i like this feature or question

Server : Length Of nice i like this feature or question Is 36

You : Bye

Server : Length Of Bye Is 3

"""        