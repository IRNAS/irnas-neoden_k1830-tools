# Neoden K1830 network communication overview
Neoden K1830 is a network controlled machine, using an ethernet switch inside the unit to interconnect various PnP components. The following details have been collected thus-far.

* 192.168.1.100 - Raspberry Pi eth0 - local ethernet with PoE running control software
* 192.168.1.30 (UDP 8030)
* 192.168.1.31 (UDP 8031)
* 192.168.1.32 (UDP 8032) - X/Y motion control
* 192.168.1.33 (UDP 8033)
* 192.168.1.34 (UDP 8034)
* 192.168.1.35 (UDP 8035)
* 192.168.1.40 (UDP 8040, 8140) - Left camera
* 192.168.1.41 (UDP 8041, 8141) - Right camera
* 192.168.1.42 (UDP 8042, 8142) - Front IC camera
* 192.168.1.43 (UDP 8043, 8143) - Back IC camera

![image](https://user-images.githubusercontent.com/1584734/139555084-8796b364-a976-424d-a748-d2da2b7e7dd4.png)
![image](https://user-images.githubusercontent.com/1584734/139555091-bc09ede0-d9da-4385-866e-b560f3f493dd.png)

All communication is UDP based, with ports defined uniquely per end-point IP address for bi-directional communication.

# UDP packet format
The packet format which appears to be used is specific for each endpoint in the network or at least type of equipment at the endpoint. First two bytes appear to serve as a sequence byte as well as a payload type specifier, followed by the payload of various lengths:
`<sequence byte><payload type><payload of X length>`

# Communication with 192.168.1.31
Every 200ms there is a request from `.100` to `.31` of 5 byte length of incremental content of `Data: 9201ffffff, Data: 9301000000, Data: 9401ffffff, Data: 9501000000`

Each response is a 94 byte packet, where some values appear to be jumping around the static value from packet to packet, but are in general (full UDP packet, see last 94 bytes): 
```
0000   00 00 00 00 ff 00 00 00 00 00 00 00 be 5b ce 07   .............[..
0010   ce 07 ce 07 ce 07 ce 07 ce 07 ce 07 ce 07 00 00   ................
0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 ba 07   ................
0030   be 07 b9 07 e5 07 b2 07 b1 07 ca 07 d6 07 00 00   ................
0040   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0050   00 00 00 00 00 00 00 00 00 00 00 00 00 00         ..............
```

# Communication with 192.168.1.32 - X/Y motion control
Every 200ms there is a request from `.100` to `.32` of 2 byte length of incremental content of `Data: a100`, where the first byte is an 8 bit or both bytes are a 16 bit sequence number.

Each response is a 36 byte packet, where some values appear to be jumping around the static value from packet to packet, but are in general (full UDP packet, see last 36 bytes): 
```
0000   00 01 10 12 00 00 00 00 49 0c 04 42 36 5e ff 41   ........I..B6^.A
0010   00 00 00 00 1e 81 01 44 48 e9 01 44 00 00 00 00   .......DH..D....
0020   00 60 29 45                                       .`)E
```

Initialize request is 13 bytes long:

```
0000   a7 03 01 01 00 4c fe 03 42 e3 7f 01 44            .....L..B...D
```

Motion control requests are of 29 bytes length:
```
0000   48 04 01 01 00 d9 2e 3d 43 9d 0f b5 43 00 00 61   H......=C...C..a
0010   44 00 00 61 44 00 a0 8c 45 00 a0 8c 45            D..aD...E...E
```

```
0000   0f 04 01 01 00 3e 3a d5 43 d5 08 d3 43 00 00 61   .....>:.C...C..a
0010   44 00 00 61 44 00 a0 8c 45 00 a0 8c 45            D..aD...E...E
```

```
0000   f3 04 01 01 00 18 44 ec 42 6f 82 e0 43 00 00 61   ......D.Bo..C..a
0010   44 00 00 61 44 00 a0 8c 45 00 a0 8c 45            D..aD...E...E
```

```
0000   fb 04 01 01 00 d5 38 65 43 e9 16 a0 43 00 00 61   ......8eC...C..a
0010   44 00 00 61 44 00 a0 8c 45 00 a0 8c 45            D..aD...E...E
```

# Communicating with 192.168.1.33 - Feeder 
Communication only happens upon request, appears that the byte in sequence to trigger the feeder must be set to 01 to trigger it.

Feeder 0 trigger request as a 36 byte packet:
```
0000   02 01 01 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00 00 00                                       ....
```
Feeder 1 trigger request as a 36 byte packet:
```
0000   04 01 00 01 00 00 00 00 00 00 00 00 00 00 00 00   ................
0010   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0020   00 00 00 00                                       ....
```

# Communication with 192.168.1.35
Every 200ms there is a request from `.100` to `.35` of 2 byte or 6 byte length of incremental content of `Data: a100`, where the first byte is an 8 bit sequence number and second byte is the payload type of 00 or 01. Sequence numbers are retained from packet to packet type.

2 byte request:
```
0000   67 01                                             g.
```

6 byte request, which does not appear to change except sequence:
```
0000   69 02 00 00 00 01                                 i.....
```

Each response is a 29 byte packet, where values are static initially, but are in general: 
```
0000   00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00   ................
0010   00 00 00 00 00 00 00 00 00 00 00 00 00            .............  
```

# Communication with camera units 192.168.1.40/41 and 42/43
Every 300ms there is a request from `.100` to `.4*` where `*=[0:3]` of 3 types, to 804* port and the stream of data to 814*:

25 byte request:
```
0000   0d 04 00 00 00 e0 01 00 00 e0 01 00 00 03 00 00   ................
0010   00 06 00 00 00 01 00 00 00                        .........
```

followed by 2 replies of 6 bytes:

```
0000   01 01 00 01 00 00                                 ......
```

2 byte request:
```
0000   0e 01                                             ..
```

7 byte image capture request:
```
0000   0f 05 00 01 00 00 00                              .......                                              .
```
or
```
0000   1b 05 00 01 00 00 00                              .......
```

followed by a 6 byte reply:

```
0000   01 00 00 01 00 00                                 ......
```

For `*=0 *=1:` a continuous stream of 484 byte packets for 480 packets to port `814*` over next 200ms, where values seem to be changing:
```
0000   03 00 00 00 12 13 13 13 13 13 12 12 12 12 12 13   ................
0010   13 11 13 13 13 11 11 12 12 13 13 14 13 13 12 13   ................
0020   13 13 13 13 12 12 12 13 13 13 12 13 12 13 13 12   ................
0030   12 13 12 14 13 12 12 12 13 13 12 13 13 12 13 13   ................
0040   13 13 12 13 13 13 12 13 13 13 12 12 12 12 12 12   ................
0050   13 13 12 13 12 13 12 12 12 12 13 13 13 13 12 12   ................
0060   13 12 13 13 12 13 13 13 12 12 11 13 11 12 12 13   ................
0070   13 12 13 13 12 12 12 13 13 12 13 13 12 13 12 13   ................
0080   13 12 12 13 13 12 12 13 12 12 12 13 13 13 12 13   ................
0090   13 13 13 13 13 13 12 13 13 12 12 13 12 12 13 12   ................
00a0   12 12 14 12 13 14 12 12 13 13 12 13 13 13 12 12   ................
00b0   13 13 13 13 13 13 12 12 13 13 13 13 13 12 13 13   ................
00c0   12 12 13 14 12 13 12 12 12 13 13 13 13 13 13 11   ................
00d0   12 12 12 13 13 14 13 13 13 12 12 13 12 13 13 13   ................
00e0   13 13 12 14 12 13 13 14 13 14 13 13 14 13 13 14   ................
00f0   13 13 13 13 13 13 11 13 13 14 14 14 13 13 14 13   ................
0100   14 14 14 15 13 15 13 15 14 14 13 14 14 14 14 15   ................
0110   14 15 15 14 14 15 14 15 14 15 16 15 14 14 15 15   ................
0120   15 16 15 14 15 15 15 15 15 15 16 14 15 15 15 15   ................
0130   15 15 15 15 16 15 15 16 15 16 17 16 16 17 18 18   ................
0140   17 19 19 19 1a 1a 1b 1c 1a 1c 1c 1c 1d 1d 1d 21   ...............!
0150   1d 20 20 21 21 23 23 26 24 25 25 26 26 2a 28 28   .  !!##&$%%&&*((
0160   29 29 2a 2a 2b 2d 2c 31 2e 2f 31 2f 2f 31 32 32   ))**+-,1./1//122
0170   33 32 31 34 35 36 37 35 38 37 37 39 39 37 3c 39   32145675877997<9
0180   3c 3f 3c 3d 40 3f 3e 3f 42 44 45 42 44 47 45 47   <?<=@?>?BDEBDGEG
0190   4a 4b 48 47 4a 4c 4c 4e 49 4d 51 51 4f 53 53 55   JKHGJLLNIMQQOSSU
01a0   55 58 56 54 56 59 5b 5a 5b 5a 5c 57 5c 60 5f 61   UXVTVY[Z[Z\W\`_a
01b0   60 63 5e 63 64 64 60 61 62 61 66 67 69 68 6a 68   `c^cdd`abafgihjh
01c0   69 66 68 69 6d 6e 74 72 79 76 7b 77 77 75 70 6e   ifhimntryv{wwupn
01d0   6f 6e 6b 67 67 68 66 64 64 6a 60 66 67 6a 66 69   onkgghfddj`fgjfi
01e0   68 66 61 67                                       hfag
```

The above data has a 4 byte header, where first two bytes are static `0300` and the second two bytes are a `uint16_t` counter. Most likely each udp packet is thus a one line of a camera image of length 480 bytes and there are then 480 lines, giving a 480x480 image.


For `*=2 *=3:` a continuous stream of 964 byte packets for 960 packets to port `814*` over next 45ms, which means that this produces an 960x960 image, following the same pattern.

Example of the decoded camera image of the position calibration marker
![camera](https://user-images.githubusercontent.com/1584734/139570979-71b1dcfe-73ba-4847-bfab-0bfbaa9150c0.png)


