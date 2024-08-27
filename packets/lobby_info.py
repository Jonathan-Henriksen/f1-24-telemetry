import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_LOBBY_INFO_FORMAT = '<4B48c3BHB'

@dataclass
class LobbyInfo:
    ai_controlled: int                  # uint8     |    Whether the vehicle is AI (1) or Human (0) controlled
    team_id: int                        # uint8     |    Team id - see appendix (255 if no team currently selected)
    nationality: int                    # uint8     |    Nationality of the driver
    platform: int                       # uint8     |    1 = Steam, 3 = PlayStation, 4 = Xbox, 6 = Origin, 255 = unknown
    name: str                           # char[48]  |    Name of participant in UTF-8 format – null terminated
    car_number: int                     # uint8     |    Car number of the player
    your_telemetry: int                 # uint8     |    The player's UDP setting, 0 = restricted, 1 = public
    show_online_names: int              # uint8     |    The player's show online names setting, 0 = off, 1 = on
    tech_level: int                     # uint16    |    F1 World tech level
    ready_status: int                   # uint8     |    0 = not ready, 1 = ready, 2 = spectating

@dataclass # 1306 bytes
class LobbyInfoPacket:
    header: PacketHeader                #           |   Header
    num_of_players: int                 # uint8     |   Number of players in the lobby data
    players: List[LobbyInfo]            # [22]      |   List of lobby player data

def unpack_lobby_info(packet_header: PacketHeader, data: bytes):
    uint8_format = '<B'
    uint8_format_size = struct.calcsize(uint8_format)

    # Num of Players
    num_of_players = struct.unpack(uint8_format, data[:uint8_format])

    # Players
    lobby_info_bytes = data[uint8_format_size:]

    lobby_info_list = List[LobbyInfo]
    
    for unpacked_lobby_info in struct.iter_unpack(_LOBBY_INFO_FORMAT, lobby_info_bytes):
        lobby_info_list.append(LobbyInfo(*unpacked_lobby_info))

    return LobbyInfoPacket(packet_header, num_of_players, lobby_info_list)