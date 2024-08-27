import struct
from enums import EventCodes

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import Union, List


_FASTEST_LAP_FORMAT = '<Bf'
@dataclass
class FastestLap:
    vehicle_index: int                  # uint8     |   Vehicle index of car achieving fastest lap
    lap_time: float                     # float     |   Lap time is in seconds

_RETIREMENT_FORMAT = '<B'
@dataclass
class Retirement:
    vehicle_index: int                  # uint8     |   Vehicle index of car retiring

_TEAM_MATE_IN_PITS_FORMAT = '<B'
@dataclass
class TeamMateInPits:
    vehicle_index: int                  # uint8     |   Vehicle index of team mate

_RACE_WINNER_FORMAT = '<B'
@dataclass
class RaceWinner:
    vehicle_index: int                  # uint8     |   Vehicle index of the race winner

_PENTALTY_FORMAT = '<7B'
@dataclass
class Penalty:
    penalty_type: int                   # uint8     |   Penalty type – see Appendices
    infringement_type: int              # uint8     |   Infringement type – see Appendices
    vehicle_index: int                  # uint8     |   Vehicle index of the car the penalty is applied to
    other_vehicle_index: int            # uint8     |   Vehicle index of the other car involved
    time: int                           # uint8     |   Time gained, or time spent doing action in seconds
    lap_num: int                        # uint8     |   Lap the penalty occurred on
    places_gained: int                  # uint8     |   Number of places gained by this

_SPEED_TRAP_FORMAT = '<Bf4B'
@dataclass
class SpeedTrap:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle triggering speed trap
    speed: float                        # float     |   Top speed achieved in kilometres per hour
    is_overall_fastest_in_session: int  # uint8     |   Overall fastest speed in session = 1, otherwise 0
    is_driver_fastest_in_session: int   # uint8     |   Fastest speed for driver in session = 1, otherwise 0
    fastest_vehicle_index_in_session: int # uint8     |   Vehicle index of the vehicle that is the fastest in this session
    fastest_speed_in_session: float     # uint8     |   Speed of the vehicle that is the fastest in this session

_START_LIGHTS_FORMAT = '<B'
@dataclass
class StartLights:
    num_of_lights: int                  # uint8     |   Number of lights showing

_DRIVE_THROUGH_PENALTY_SERVED_FORMAT = '<B'
@dataclass
class DriveThroughPenaltyServed:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle serving drive through

_STOP_GO_PENALTY_SERVED_FORMAT = '<B'
@dataclass
class StopGoPenaltyServed:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle serving stop go

_FLASHBACK_FORMAT = '<Lf'
@dataclass
class Flashback:
    flashback_frame_identifier: int     # uint32    |   Frame identifier flashed back to
    flashback_session_time: float       # float     |   Session time flashed back to

_BUTTONS_FORMAT = '<L'
@dataclass
class Buttons:
    button_status: int                  # uint32    |   Bit flags specifying which buttons are being pressed

_OVERTAKE_FORMAT = '<2B'
@dataclass
class Overtake:
    overtaking_vehicle_index: int       # uint8     |   Vehicle index of the vehicle overtaking
    being_overtaken_vehicle_index: int  # uint8     |   Vehicle index of the vehicle being overtaken

_SAFETY_CAR_FORMAT = '<2B'
@dataclass
class SafetyCar:
    safety_car_type: int                # uint8     |   0 = No Safety Car, 1 = Full Safety Car, 2 = Virtual Safety Car, 3 = Formation Lap Safety Car
    event_type: int                     # uint8     |   0 = Deployed, 1 = Returning, 2 = Returned, 3 = Resume Race

_COLLISION_FORMAT = '<2B'
@dataclass
class Collision:
    vehicle_1_index: int                # uint8     |   Vehicle index of the first vehicle involved in the collision
    vehicle_2_index: int                # uint8     |   Vehicle index of the second vehicle involved in the collision

@dataclass
class EventPacket:
    header: PacketHeader                #           |   Header
    event_string_code: List[int]        # uint8[4]  |   Event string code
    event_details: Union[
        FastestLap,
        Retirement,
        TeamMateInPits,
        RaceWinner,
        Penalty,
        SpeedTrap,
        StartLights,
        DriveThroughPenaltyServed,
        StopGoPenaltyServed,
        Flashback,
        Buttons,
        Overtake,
        SafetyCar,
        Collision
    ]

def unpack_event_packet(packet_header: PacketHeader, data: bytes):
    event_string_code_format = '<4B'
    event_string_code_format_size = struct.calcsize(event_string_code_format)

    event_string_code_bytes = data[:event_string_code_format_size]
    unpacked_event_string_code = struct.unpack(event_string_code_format, event_string_code_bytes)

    event_code_string = bytes(unpacked_event_string_code).decode('ascii')

    event_data = data[event_string_code_format_size:]

    event_packet = EventPacket(packet_header)

    match (event_code_string):
        case EventCodes.BUTTON_STATUS.value:
            unpacked_button_status = struct.unpack(_BUTTONS_FORMAT, event_data)
            event_packet.event_details = Buttons(*unpacked_button_status)

            print(f"Buttons pressed = {event_packet.event_details.button_status}")
        
        case _:
            print(f"Unknown event received: {event_code_string}")

    return event_packet