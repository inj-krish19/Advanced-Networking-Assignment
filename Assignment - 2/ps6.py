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
from random import randint

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Clients sends a string, Server calculates Hash value and replies back to Client using TCP"

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )

server.listen(1)

print( f"\nQuestion : {question}\n" )

clients = []

print( f"\nServer Is Running On {host}:{port}\n" )

limit = 128
salt = randint(0, limit)

def encryption( query ):
    
    hash_value = ""
    
    for index in range(26):
        try:
            hash_value += chr( ( ord( query[index] ) + salt ) % 128 )
        except IndexError as e:
            hash_value += chr( randint(0, limit) )
    
    return hash_value

client,client_address = server.accept()

if client_address not in clients:
    print( f"Connected With : {client_address}" )  
    clients.append( client_address)

while message != "Bye" and reply.decode( encoder ) != "Bye":
    
    reply = client.recv(1024)

    message = encryption( reply.decode(encoder) )
    
    print( f"\nClient {client_address} : {reply.decode( encoder )} after encryption it is {message}")
    
    client.send( message.encode( encoder ) )     
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Clients sends a string, Server calculates Hash value and replies back to Client using TCP


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 64882)

Client ('127.0.0.1', 64882) : hello world after encryption it is IFMMPXPSME1_J?dY
g7nZ$5\

Client ('127.0.0.1', 64882) : oh my god converting in hash after encryption it is PINZHPEDPOWFSUJOHJOIB

Client ('127.0.0.1', 64882) : its amazing after encryption it is JUTBNB[JOHf\yW@1lyJHH

Client ('127.0.0.1', 64882) : Bye after encryption it is #ZF@yU
h"HP
?!6 9PX>

""" 