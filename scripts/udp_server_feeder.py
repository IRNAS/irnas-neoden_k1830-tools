import socket
import struct
import time

# This script runs through feeders 1-15 in sequence as a demo of control

UDP_IP = "192.168.1.33"
UDP_PORT = 8033

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind(('', UDP_PORT))

# Sequence variable must be incrementing packet from packet
seq=0
# Packet type is statically defined
packet_type=1

# Create an aray of fields for feeder values
# Sending 1 turns the feeder valve on
# Sending 255 turns the feeder valve off

feeders = [0]*34

for x in range(0,14):
    # Turn on feeder
    feeders[x]=1
    # Make packet and send
    buf = struct.pack('BB%sB' % len(feeders),seq,packet_type,*feeders)
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    seq+=1

    time.sleep(0.2)

    # Turn off feeder
    feeders[x]=255
    # Make packet and send
    buf = struct.pack('BB%sB' % len(feeders),seq,packet_type,*feeders)
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    seq+=1

    # Reset feeders structure to 0 
    feeders = [0]*34

    time.sleep(0.5)

sock.sendto(buf, (UDP_IP, UDP_PORT))
