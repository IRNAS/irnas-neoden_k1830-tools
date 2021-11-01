# Read wireshark dissection json and process
import json
import struct
 
# Opening JSON file
f = open('move-dissection.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)

# Closing file
f.close()

# Iterating through the json
# list
for i in data:
    status =i["_source"]["layers"]["data"]["data.data"]
    status=status.replace(':', '')
    status=status[16:32]
    #print(status)
    array=bytearray.fromhex(status)
    #print(array)
    unpacked = struct.unpack_from('ff',array)
    print(unpacked)



 
