import socket
import struct

from data.packetHeader import *
from packetHandler import *

# Define the UDP port and address
UDP_PORT = 9999
UDP_IP = '0.0.0.0'  # Listen on all network interfaces

# Define the header format
HEADER_FORMAT = '<HBBBBBQfIIbb'
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    print(f"Listening for UDP packets on port {UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)

        if len(data) >= HEADER_SIZE:

            unpacked_data = struct.unpack(HEADER_FORMAT, data[:HEADER_SIZE])

            packetHeader = PacketHeader(*unpacked_data)
            
            PrintHeader(packetHeader)
        else:
            print(f"Received packet from {addr} with insufficient data")

if __name__ == '__main__':
    main()