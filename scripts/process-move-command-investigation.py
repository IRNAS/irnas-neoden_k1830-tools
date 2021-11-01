# Read wireshark dissection json and process
import json
import struct
 
# Opening JSON file
f = open('move-req-dissection.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Iterating through the json
# list
for i in data:
    status = i["_source"]["layers"]["data"]["data.data"]
    if i["_source"]["layers"]["data"]["data.len"] != "29":
        continue
    status=status.replace(':', '')
    #print(status)
    array=bytearray.fromhex(status)
    print(array.hex())
    unpacked = struct.unpack_from('<BIffffff',array)
    print(unpacked)
    seq=unpacked[0] # sequence number
    frame=unpacked[1] # 65796
    pos_x=unpacked[2] 
    pos_y=unpacked[3]
    speed_x=unpacked[4] # 150
    speed_y=unpacked[5] # 150
    accel_x=unpacked[6] # 1500
    accel_y=unpacked[7] # 1500
    #print("{:5.3f} {:5.3f}".format(unpacked[2],unpacked[3]))

    seq=0 # sequence number
    frame=65796
    pos_x=44.924537658691406
    pos_y=1.2785402536392212
    speed_x=150 # 150
    speed_y=150 # 150
    accel_x=1500 # 1500
    accel_y=1500 # 1500
    packet=struct.pack('<BIffffff',seq,frame,pos_x,pos_y,speed_x,speed_y,accel_x,accel_y)
    print(packet.hex())



 
