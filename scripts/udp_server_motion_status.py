import socket
import struct
import time

# This script runs through feeders 1-15 in sequence as a demo of control

UDP_IP = "192.168.1.32"
UDP_PORT = 8032

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind(('', UDP_PORT))

# Sequence variable must be incrementing packet from packet
seq=0
# Packet type is statically defined
packet_type=0

while True:

    # Make packet and send
    buf = struct.pack('BB',seq,packet_type)
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    seq+=1

    time.sleep(0.2)

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    length = len(data)

    unpacked = struct.unpack_from('BBBBBffIffIBBBB',data)
    unpacked[0] # does not change
    unpacked[1] # 1,2 values
    unpacked[2] # around 20
    unpacked[3] # around 20
    unpacked[4] # always 0
    unpacked[5] # set x
    unpacked[6] # actual x
    unpacked[7] # zero
    unpacked[8] # set y
    unpacked[9] # actual y
    print("{:5.3f} {:5.3f} {:5.3f} {:5.3f}".format(unpacked[5],unpacked[6],unpacked[8],unpacked[9]))