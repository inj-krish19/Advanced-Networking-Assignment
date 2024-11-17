from socket import *

server = socket( AF_INET, SOCK_DGRAM )

server.connect( ("localhost",65432) )

print( f"\nSystem 's IP Address Is {server.getsockname()[0]} and Port Is {server.getsockname()[1]} ")

"""

System 's IP Address Is 127.0.0.1 and Port Is 55366 

"""