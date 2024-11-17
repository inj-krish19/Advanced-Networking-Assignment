"""

NAME - SHAH KRISH J.
ROLL NO. - 47
SEM - V
SUBJECT - ADVANCED NETWORKING
COURSE - COMPUTER SCIENCE
ASSIGNMENT - 2

Question 5 : Create a simulation of FTP protocol using TCP
    
-----------------------------------------------------------------

"""

import socket

host = "localhost"
port = 65432
encoder = "utf-8"

message = ""
reply = b""
question = "Create a simulation of FTP protocol using TCP"

server = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

server.bind( ( host, port ) )

print( f"\nQuestion : {question}\n" )

clients = []

print( f"\nServer Is Running On {host}:{port}\n" )

while message != "Bye" and reply.decode( encoder ) != "Bye":
    
    reply,client_address = server.recvfrom(1024)

    if client_address not in clients:
        print( f"Connected With : {client_address}" )  
        clients.append( client_address)
        
    print( f"\nClient {client_address} File Content : {reply.decode( encoder )}")
    
    try:
    
        with open("output.txt", "w") as file:
            file.write( reply.decode( encoder ) )
            print("\nFile Reached to Destination")
            
            message = f"File Is saved at server as output.txt"
            
            server.sendto( message.encode( encoder ), client_address)        
        
    except FileNotFoundError as e:
        print("\nUnable To Reach File at Destination")
    
        message = f"File Sent Successfully"
        
        server.sendto( message.encode( encoder ), client_address )        
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Question : Create a simulation of FTP protocol using TCP


Server Is Running On localhost:65432

Connected With : ('127.0.0.1', 55384)

Client ('127.0.0.1', 55384) File Content : This is sample content

File Reached to Destination

"""  