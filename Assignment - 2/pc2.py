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

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

client.connect( ( host, port ) )

print( f"\nServer Always Replies With Uppercase of input\nYou are connected with {host}:{port} \n" )    

while message != "Bye" and reply.decode( encoder ) != "Bye" :
    
    message = input( "\nYou : ")
    
    client.send( message.encode() )
    
    reply = client.recv( 1024 )
    
    print( f"\nServer : {reply.decode( encoder )}")
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------

Server Always Replies With Uppercase of input
You are connected with localhost:65432


You : hii

Server : HII

You : hello

Server : HELLO

You : what

Server : WHAT

You : are you just giving me uppercase

Server : ARE YOU JUST GIVING ME UPPERCASE

You : ohk i got it. but you are boring me

Server : OHK I GOT IT. BUT YOU ARE BORING ME

You : bye

Server : BYE

You : Bye

Server : BYE

"""        