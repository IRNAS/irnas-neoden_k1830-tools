# Read wireshark dissection json and process
import json
import struct
 
# Opening JSON file
f = open('move00-dissection.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Iterating through the json
# list
for i in data:
    status =i["_source"]["layers"]["data"]["data.data"]
    #print(status)
    status=status.replace(':', '')
    array=bytearray.fromhex(status)
    #print(array)
    unpacked = struct.unpack_from('BBBBBffIffIBBBB',array)
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



 
