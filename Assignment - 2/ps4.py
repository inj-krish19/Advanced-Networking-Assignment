"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 4 : Create a TCP Encryption Application
    
-----------------------------------------------------------------

"""

import socket
from random import randint

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Create a TCP Encryption Application"

server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

server.bind( ( host, port ) )

server.listen(3)

limit = 128
salt = randint(0, limit )

def encryption( query ):

    encoded = ""    

    for character in query:
        encoded += chr( ( ord( character ) + salt ) % limit )
    
    return encoded
    
def decryption( query ):

    decoded = ""    

    for character in query:
        if ord(character) < limit:
            decoded += chr( ord(character) + ( limit - salt) )
        else:
            decoded += chr( ord(character) - salt )
            
    return decoded

print( f"\nQuestion : {question}\n" )

clients = []

print( f"\nServer Is Running On {host}:{port}\n" )

client,client_address = server.accept()

if client_address not in clients:
    clients.append( client_address)
    print( f"Connected With : {client_address}" ) 
    
while message != "Bye" and reply.decode( encoder ) != "Bye" :
    
    reply = client.recv( 1024 )
    
    print( f"\nClient {client_address} : {reply.decode( encoder )} ",end="")
    
    message = reply.decode( encoder )
    
    if message.startswith("Decrypt "):
        message = decryption( message[8:] )
        print( f"which has decrypted value {message}")
    else:
        message = encryption( message )
        print( f"which has decrypted value {message}")
        
    client.send( message.encode( encoder ) )
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Create a TCP Encryption Application


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 63245)

Client ('127.0.0.1', 63245) : hello which has decrypted value 3077:

Client ('127.0.0.1', 63245) : ohh wow which has decrypted value :33kB:B

Client ('127.0.0.1', 63245) : Decrypt 3077: which has decrypted value hello

Client ('127.0.0.1', 63245) : Decrypt :33kB:B which has decrypted value ohh wow

Client ('127.0.0.1', 63245) : nice i like it which has decrypted value 94.0k4k7460k4?

Client ('127.0.0.1', 63245) : Decrypt 94.0k4k7460k4? which has decrypted value nice i like it

D0ient ('127.0.0.1', 63245) : Bye which has decrypted value 

"""        