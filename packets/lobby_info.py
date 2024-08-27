import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_LOBBY_INFO_FORMAT = '<4B48s3BHB'
_LOBBY_INFO_FORMAT_SIZE = struct.calcsize(_LOBBY_INFO_FORMAT)

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

_NUM_OF_PLAYERS_FORMAT = '<B'
_NUM_OF_PLAYERS_FORMAT_SIZE = struct.calcsize(_NUM_OF_PLAYERS_FORMAT)
@dataclass # 1306 bytes
class LobbyInfoPacket:
    header: PacketHeader                #           |   Header
    num_of_players: int                 # uint8     |   Number of players in the lobby data
    players: List[LobbyInfo]            # [22]      |   List of lobby player data

def unpack_lobby_info(packet_header: PacketHeader, data: bytes):
    # Num of Players
    num_of_players_bytes = data[:_NUM_OF_PLAYERS_FORMAT_SIZE]

    num_of_players = struct.unpack(_NUM_OF_PLAYERS_FORMAT, num_of_players_bytes)

    offset = _NUM_OF_PLAYERS_FORMAT_SIZE

    # Players
    lobby_info_bytes = data[offset:offset + (_LOBBY_INFO_FORMAT_SIZE * num_of_players[0])]

    lobby_info_list = []
    for unpacked_lobby_info in struct.iter_unpack(_LOBBY_INFO_FORMAT, lobby_info_bytes):
        lobby_info = LobbyInfo(*unpacked_lobby_info)

        name = unpacked_lobby_info[4].rstrip(b'\x00').decode('utf-8')
        lobby_info.name = name
        
        lobby_info_list.append(lobby_info)

    return LobbyInfoPacket(packet_header, num_of_players, lobby_info_list)