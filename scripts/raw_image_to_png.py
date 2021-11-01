import numpy as np
import matplotlib.pyplot as plt

# Simple script to plot the raw binary capture from the camera

# raw input is from Wireshark Follow UDP stream export as raw
raw = np.fromfile("camera.raw", dtype=np.uint8,offset=0)
# stream starts with a packet of 6 bytes that represents an image start
header=raw[0:6]
print("Header:" + str(header))

# create an empty array
img=np.empty([480,480])
# offset for header
off=6
# insert data into a 2d array based on sequence numbers
for x in range(0,480):
  line_counter=raw[off+x*484+2]+raw[off+x*484+3]*256
  img[line_counter]=raw[off+x*484+4:off+x*484+5+479]


print(img.size)
plt.imshow(img,cmap="gray")

# show  or save the image
#plt.show()
plt.savefig("camera.png")