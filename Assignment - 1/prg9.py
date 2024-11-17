from socket import *

server = socket( AF_INET, SOCK_DGRAM )

server.connect( ("localhost",65432) )

print( f"\nSystem 's Hostname Is {gethostname()} ")

"""

System 's Hostname Is KRISH

"""