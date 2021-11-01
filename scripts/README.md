# Neoden K1830 scripts overview
Various scripts have been implemented to test communication, process data and determine the payloads. Some can run on the actual machine to test things out. Note this is all very basic and not complete in any sense.

## Wireshark PCAP analysis
Wirshark is used to inspect the various PCAP captures and filters are put in place to select the right communication. `File->Export packet dissections->As JSON` option is used to create a .json capture of the communication for processing with python.

## Machine control tests
Python scripts are used to test various machine operations, these are found as `udp_server` or `udp_receiver` for various actions. For example, running at the same time on the machine: `scripts/udp_server_motion_move.py`, `scripts/udp_server_camera_request.py` and `scripts/udp_receiver_camera.py` will move the machine, request images and then receive adn save images.
