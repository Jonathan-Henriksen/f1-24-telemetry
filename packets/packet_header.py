import struct
from dataclasses import dataclass

PACKET_HEADER_FORMAT = '<HBBBBBQfIIbb'
PACKET_HEADER_FORMAT_SIZE = struct.calcsize(PACKET_HEADER_FORMAT)

@dataclass
class PacketHeader:
    packet_format: int               # uint16    |    2024
    game_year: int                   # uint8     |    Game year - last two digits e.g. 24
    game_major_version: int          # uint8     |    Game major version - "X.00"
    game_minor_version: int          # uint8     |    Game minor version - "1.XX"
    packet_version: int              # uint8     |    Version of this packet type, all start from 1
    packet_id: int                   # uint8     |    Identifier for the packet type, see below
    session_uid: int                 # uint64    |    Unique identifier for the session
    session_time: float              # float     |    Session timestamp
    frame_identifier: int            # uint32    |    Identifier for the frame the data was retrieved on
    overall_frame_identifier: int    # uint32    |    Overall identifier for the frame the data was retrieved on, doesn't go back after flashbacks
    player_car_index: int            # int8      |    Index of player's car in the array
    secondary_player_car_index: int  # int8      |    Index of secondary player's car in the array (splitscreen) 255 if no second player

    def __init__(self, data: bytes):
        unpacked_data = struct.unpack(PACKET_HEADER_FORMAT, data[0:PACKET_HEADER_FORMAT_SIZE])
        self.__dict__.update(dict(zip(self.__annotations__.keys(), unpacked_data)))