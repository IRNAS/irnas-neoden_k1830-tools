import socket
import yaml

# This script replays yaml file from Wireshark capture

with open("camera.yaml") as file:
    packets_list = yaml.load(file, Loader=yaml.FullLoader)

UDP_IP = "127.0.0.1"
UDP_PORT = 8140

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

for packet, payload in packets_list.items():
    print(packet)
    sock.sendto(payload, (UDP_IP, UDP_PORT))