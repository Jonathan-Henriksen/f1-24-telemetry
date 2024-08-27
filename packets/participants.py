import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_PARTICIPANT_FORMAT = '<7B48c2BHB'

@dataclass
class Participant:
    ai_controlled: int                      # uint8     |   Whether the vehicle is AI (1) or Human (0) controlled
    driver_id: int                          # uint8     |   Driver id - see appendix, 255 if network human
    network_id: int                         # uint8     |   Network id – unique identifier for network players
    team_id: int                            # uint8     |   Team id - see appendix
    my_team: int                            # uint8     |   My team flag – 1 = My Team, 0 = otherwise
    race_number: int                        # uint8     |   Race number of the car
    nationality: int                        # uint8     |   Nationality of the driver
    name: str                               # char      |   Name of participant in UTF-8 format – null terminated (m_name[48]). Will be truncated with … (U+2026) if too long
    your_telemetry: int                     # uint8     |   The player's UDP setting, 0 = restricted, 1 = public
    show_online_names: int                  # uint8     |   The player's show online names setting, 0 = off, 1 = on
    tech_level: int                         # uint16    |   F1 World tech level    
    platform: int                           # uint8     |   1 = Steam, 3 = PlayStation, 4 = Xbox, 6 = Origin, 255 = unknown

@dataclass # 1350 bytes
class ParticipantsPacket:
    header: PacketHeader                    #           |   Header
    num_active_cars: int                    # uint8     |   Number of active cars in the data – should match number of cars on HUD
    participants: List[Participant]         #           |   List of participants

def unpack_participants(packet_header: PacketHeader, data: bytes):
    num_active_cars_format = '<B'
    num_active_cars_format_size = struct.calcsize(num_active_cars_format)

    num_active_cars = struct.unpack(num_active_cars_format, data[:num_active_cars_format_size])

    participants_list = List[Participant]
    for unpacked_participant in struct.iter_unpack(_PARTICIPANT_FORMAT, data[num_active_cars_format_size:]):
        participants_list.append(Participant(*unpacked_participant))

    return ParticipantsPacket(packet_header, num_active_cars, participants_list)