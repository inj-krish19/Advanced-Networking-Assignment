"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 4 :  Create a TCP Encryption Application
    
-----------------------------------------------------------------

"""

import socket

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
encrypted_value = "{encrypted_value}"

client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

client.connect( ( host, port ) )

print( f"\nServer Always Replies with length of your input\nAt for each decryption there should be like Decrypt {encrypted_value} \nSpecial Characters Not Supported in Encryption\nYou are connected with {host}:{port} \n" )  

while message != "Bye" and reply.decode( encoder ) != "Bye" :
    
    message = input( "\nYou : ")
    
    client.send( message.encode( encoder ) )
    
    reply = client.recv( 1024 )
    
    print( f"\nServer : {reply.decode( encoder )}")
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Server Always Replies with length of your input
At for each decryption there should be like Decrypt {encrypted_value}
Special Characters Not Supported in Encryption
You are connected with localhost:65432


You : hello

Server : 3077:

You : ohh wow

Server : :33kB:B

You : Decrypt 3077:

Server : hello

You : Decrypt :33kB:B

Server : ohh wow

You : nice i like it

Server : 94.0k4k7460k4?

You : Decrypt 94.0k4k7460k4?

Server : nice i like it

You : Bye

D0rver :


"""        