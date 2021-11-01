import socket
import struct
import numpy as np
import matplotlib.pyplot as plt

UDP_IP = "127.0.0.1"
UDP_PORT = 8140

#sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# wait for image to start
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    length = len(data)
    
    #print(data)
    # decode header
    type_a,type_b,seq=struct.unpack_from('BBH', data)
    print("waiting: message length: %i a %i b %i" % (len(data), type_a, type_b))
    if type_a==1 and type_b == 1:
        # image transfer started
        break

# create image storage
rows, cols = (480, 480)
arr = [[0]*cols]*rows

# receive image
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    length = len(data)

    # decode header
    type_a,type_b,seq=struct.unpack_from('BBH', data)
    print("receiving: message length: %i a %i b %i" % (len(data),type_a,type_b))
    

    if type_a==3 and type_b == 0:
        # valid image frame received
        # enter data into storage
        arr[seq]=list(data[4:483])
        pass
    elif type_a==1 and type_b == 0:
        break
    else:
        break

img=np.array(arr, dtype=np.uint8)
print(img.size)
plt.imshow(img,cmap="gray")

# show  or save the image
plt.show()
#plt.savefig("camera.png")