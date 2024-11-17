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

client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )

client.connect( ( host, port ) )

print( f"\nServer replies status as per file received or not \nYou are connected with {host}:{port} \n" )  

while message != "Bye" and reply.decode(encoder) != "Bye":
    
    message = input("\nWrite File Name for sending to Server : ")

    try:
        
        with open(message,'r') as file:
            message = file.read()
    
        print( f"\nFile Content : {message} ")
    
        client.sendto( message.encode(), (host, port) )     
        
        reply,client_address = client.recvfrom(1024)
        
        print( f"\nServer : {reply.decode(encoder) }")

    except FileNotFoundError as e:
        print( f"\nFile Not Found")
    
    
"""

-------------------------------------------------------------

    Output : 
        
-------------------------------------------------------------


Server replies status as per file received or not
You are connected with localhost:65432


Write File Name for sending to Server : notfound.txt

File Not Found

Write File Name for sending to Server : input.txt

File Content : This is sample content

Server : File Is saved at server as output.txt

Write File Name for sending to Server : thank you

File Not Found

Write File Name for sending to Server : Bye

File Not Found

"""        