import socket

from enums import PacketIDs
from packets import *

_PORT = 9999
_IP = '0.0.0.0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((_IP, _PORT))

def start_server():
    print(f"Listening for UDP packets on port {_PORT}...")
    while True:
        data, _ = sock.recvfrom(2048)
        handle_packet(data)

def handle_packet(data: bytes):
    if len(data) >= PACKET_HEADER_FORMAT_SIZE:
            packet_header = PacketHeader(data)

            match packet_header.packet_id:

                case PacketIDs.CAR_DAMAGE.value:
                    car_damage_packet = unpack_car_damage(packet_header, data)

                    print(f"Received and unpacked Car Damage packet with data for {len(car_damage_packet.car_damage_list)} cars")

                case PacketIDs.CAR_STATUS.value:
                    car_status_packet = unpack_car_status(packet_header, data)

                    print(f"Received and unpacked Car Status packet with data for {len(car_status_packet.car_status_list)} cars")

                case PacketIDs.CAR_TELEMETRY.value:
                    car_telemetry_packet = unpack_car_telemetry(packet_header, data[PACKET_HEADER_FORMAT_SIZE:])

                    print(f"Received and unpacked Car Telemetry packet with data for {len(car_telemetry_packet.car_telemetry_list)} cars")

                case PacketIDs.TYRE_SETS.value:
                    tyre_sets_packet = unpack_tyre_sets(packet_header, data)

                    print(f"Received and unpacked Tyre Sets packet for car index {tyre_sets_packet.car_index}")

                case _:
                    print(f"Packet of type {PacketIDs(packet_header.packet_id)} was received but not implemented")

if __name__ == '__main__':
    start_server()

