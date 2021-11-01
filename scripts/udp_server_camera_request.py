import socket
import struct
import time

# This script request an image from a camera

UDP_IP = "192.168.1.40"
UDP_PORT = 8040

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind(('', UDP_PORT))

# Sequence variable must be incrementing packet from packet
seq=20



while True:
    buf = struct.pack('B',seq)+bytearray("04000000e0010000e0010000030000000600000001000000")
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    print("Capture image")
    seq+=1

    time.sleep(0.1)
    
    # Packet type is statically defined
    packet_type=5
    # Make packet and send
    buf = struct.pack('BBBBBBB',seq,packet_type,0,1,0,0,0)
    sock.sendto(buf, (UDP_IP, UDP_PORT))
    print("Requesting image")
    seq+=1

    time.sleep(5)

