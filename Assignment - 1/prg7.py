import uuid

mac = uuid.getnode()

mac_address = ":".join(('%012X' % mac)[i:i+2] for i in range(0,12,2))

print( f"\nMAC Address of system is {mac_address}")

"""

MAC Address of system is AF:7F:4B:4D:38:C5

"""