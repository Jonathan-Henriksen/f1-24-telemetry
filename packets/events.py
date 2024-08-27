import struct
from enums import EventCodes, ButtonFlags

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import Union, List


_FASTEST_LAP_FORMAT = '<Bf'
_FASTEST_LAP_FORMAT_SIZE = struct.calcsize(_FASTEST_LAP_FORMAT)
@dataclass
class FastestLap:
    vehicle_index: int                  # uint8     |   Vehicle index of car achieving fastest lap
    lap_time: float                     # float     |   Lap time is in seconds

_RETIREMENT_FORMAT = '<B'
_RETIREMENT_FORMAT_SIZE = struct.calcsize(_RETIREMENT_FORMAT)
@dataclass
class Retirement:
    vehicle_index: int                  # uint8     |   Vehicle index of car retiring

_TEAM_MATE_IN_PITS_FORMAT = '<B'
_TEAM_MATE_IN_PITS_FORMAT_SIZE = struct.calcsize(_TEAM_MATE_IN_PITS_FORMAT)
@dataclass
class TeamMateInPits:
    vehicle_index: int                  # uint8     |   Vehicle index of team mate

_RACE_WINNER_FORMAT = '<B'
_RACE_WINNER_FORMAT_SIZE = struct.calcsize(_RACE_WINNER_FORMAT)
@dataclass
class RaceWinner:
    vehicle_index: int                  # uint8     |   Vehicle index of the race winner

_PENALTY_FORMAT = '<7B'
_PENALTY_FORMAT_SIZE = struct.calcsize(_PENALTY_FORMAT)
@dataclass
class Penalty:
    penalty_type: int                   # uint8     |   Penalty type – see Appendices
    infringement_type: int              # uint8     |   Infringement type – see Appendices
    vehicle_index: int                  # uint8     |   Vehicle index of the car the penalty is applied to
    other_vehicle_index: int            # uint8     |   Vehicle index of the other car involved
    time: int                           # uint8     |   Time gained, or time spent doing action in seconds
    lap_num: int                        # uint8     |   Lap the penalty occurred on
    places_gained: int                  # uint8     |   Number of places gained by this

_SPEED_TRAP_FORMAT = '<Bf3Bf'
_SPEED_TRAP_FORMAT_SIZE = struct.calcsize(_SPEED_TRAP_FORMAT)
@dataclass
class SpeedTrap:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle triggering speed trap
    speed: float                        # float     |   Top speed achieved in kilometres per hour
    is_overall_fastest_in_session: int  # uint8     |   Overall fastest speed in session = 1, otherwise 0
    is_driver_fastest_in_session: int   # uint8     |   Fastest speed for driver in session = 1, otherwise 0
    fastest_vehicle_index_in_session: int # uint8     |   Vehicle index of the vehicle that is the fastest in this session
    fastest_speed_in_session: float     # float     |   Speed of the vehicle that is the fastest in this session

_START_LIGHTS_FORMAT = '<B'
_START_LIGHTS_FORMAT_SIZE = struct.calcsize(_START_LIGHTS_FORMAT)
@dataclass
class StartLights:
    num_of_lights: int                  # uint8     |   Number of lights showing

_DRIVE_THROUGH_PENALTY_SERVED_FORMAT = '<B'
_DRIVE_THROUGH_PENALTY_SERVED_FORMAT_SIZE = struct.calcsize(_DRIVE_THROUGH_PENALTY_SERVED_FORMAT)
@dataclass
class DriveThroughPenaltyServed:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle serving drive through

_STOP_GO_PENALTY_SERVED_FORMAT = '<B'
_STOP_GO_PENALTY_SERVED_FORMAT_SIZE = struct.calcsize(_STOP_GO_PENALTY_SERVED_FORMAT)
@dataclass
class StopGoPenaltyServed:
    vehicle_index: int                  # uint8     |   Vehicle index of the vehicle serving stop go

_FLASHBACK_FORMAT = '<If'
_FLASHBACK_FORMAT_SIZE = struct.calcsize(_FLASHBACK_FORMAT)
@dataclass
class Flashback:
    flashback_frame_identifier: int     # uint32    |   Frame identifier flashed back to
    flashback_session_time: float       # float     |   Session time flashed back to

_BUTTONS_FORMAT = '<I'
_BUTTONS_FORMAT_SIZE = struct.calcsize(_BUTTONS_FORMAT)
@dataclass
class Buttons:
    button_status: int                  # uint32    |   Bit flags specifying which buttons are being pressed

_OVERTAKE_FORMAT = '<2B'
_OVERTAKE_FORMAT_SIZE = struct.calcsize(_OVERTAKE_FORMAT)
@dataclass
class Overtake:
    overtaking_vehicle_index: int       # uint8     |   Vehicle index of the vehicle overtaking
    being_overtaken_vehicle_index: int  # uint8     |   Vehicle index of the vehicle being overtaken

_SAFETY_CAR_FORMAT = '<2B'
_SAFETY_CAR_FORMAT_SIZE = struct.calcsize(_SAFETY_CAR_FORMAT)
@dataclass
class SafetyCar:
    safety_car_type: int                # uint8     |   0 = No Safety Car, 1 = Full Safety Car, 2 = Virtual Safety Car, 3 = Formation Lap Safety Car
    event_type: int                     # uint8     |   0 = Deployed, 1 = Returning, 2 = Returned, 3 = Resume Race

_COLLISION_FORMAT = '<2B'
_COLLISION_FORMAT_SIZE = struct.calcsize(_COLLISION_FORMAT)
@dataclass
class Collision:
    vehicle_1_index: int                # uint8     |   Vehicle index of the first vehicle involved in the collision
    vehicle_2_index: int                # uint8     |   Vehicle index of the second vehicle involved in the collision

_EVENT_STRING_CODE_FORMAT = '<4B'
_EVENT_STRING_CODE_FORMAT_SIZE = struct.calcsize(_EVENT_STRING_CODE_FORMAT)
@dataclass
class EventPacket:
    header: PacketHeader                #           |   Header
    event_string_code: List[int]        # uint8[4]  |   Event string code
    event: Union[
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

def unpack_event_packet(packet_header, data: bytes):
    event_string_code_bytes = data[:_EVENT_STRING_CODE_FORMAT_SIZE]
    unpacked_event_string_code = struct.unpack(_EVENT_STRING_CODE_FORMAT, event_string_code_bytes)

    event_string_code = bytes(unpacked_event_string_code).decode('ascii')

    event_bytes = data[_EVENT_STRING_CODE_FORMAT_SIZE:]
    event_packet = EventPacket(packet_header, unpacked_event_string_code, None)

    match event_string_code:
        case EventCodes.FASTEST_LAP.value:
            fastest_lap_bytes = event_bytes[:_FASTEST_LAP_FORMAT_SIZE]
            unpacked_fastest_lap = struct.unpack(_FASTEST_LAP_FORMAT, fastest_lap_bytes)

            event_packet.event = FastestLap(*unpacked_fastest_lap)

        case EventCodes.RETIREMENT.value:
            retirement_bytes = event_bytes[:_RETIREMENT_FORMAT_SIZE]
            unpacked_retirement = struct.unpack(_RETIREMENT_FORMAT, retirement_bytes)

            event_packet.event = Retirement(*unpacked_retirement)

        case EventCodes.TEAM_MATE_IN_PITS.value:
            team_mate_in_pits_bytes = event_bytes[:_TEAM_MATE_IN_PITS_FORMAT_SIZE]
            unpacked_team_mate_in_pits = struct.unpack(_TEAM_MATE_IN_PITS_FORMAT, team_mate_in_pits_bytes)

            event_packet.event = TeamMateInPits(*unpacked_team_mate_in_pits)

        case EventCodes.RACE_WINNER.value:
            race_winner_bytes = event_bytes[:_RACE_WINNER_FORMAT_SIZE]
            unpacked_race_winner = struct.unpack(_RACE_WINNER_FORMAT, race_winner_bytes)

            event_packet.event = RaceWinner(*unpacked_race_winner)

        case EventCodes.PENALTY_ISSUED.value:
            penalty_bytes = event_bytes[:_PENALTY_FORMAT_SIZE]
            unpacked_penalty = struct.unpack(_PENALTY_FORMAT, penalty_bytes)

            event_packet.event = Penalty(*unpacked_penalty)

        case EventCodes.SPEED_TRAP_TRIGGERED.value:
            speed_trap_bytes = event_bytes[:_SPEED_TRAP_FORMAT_SIZE]
            unpacked_speed_trap = struct.unpack(_SPEED_TRAP_FORMAT, speed_trap_bytes)

            event_packet.event = SpeedTrap(*unpacked_speed_trap)

        case EventCodes.START_LIGHTS.value:
            start_lights_bytes = event_bytes[:_START_LIGHTS_FORMAT_SIZE]
            unpacked_start_lights = struct.unpack(_START_LIGHTS_FORMAT, start_lights_bytes)

            event_packet.event = StartLights(*unpacked_start_lights)

        case EventCodes.DRIVE_THROUGH_SERVED.value:
            drive_through_bytes = event_bytes[:_DRIVE_THROUGH_PENALTY_SERVED_FORMAT_SIZE]
            unpacked_drive_through = struct.unpack(_DRIVE_THROUGH_PENALTY_SERVED_FORMAT, drive_through_bytes)

            event_packet.event = DriveThroughPenaltyServed(*unpacked_drive_through)

        case EventCodes.STOP_GO_SERVED.value:
            stop_go_bytes = event_bytes[:_STOP_GO_PENALTY_SERVED_FORMAT_SIZE]
            unpacked_stop_go = struct.unpack(_STOP_GO_PENALTY_SERVED_FORMAT, stop_go_bytes)

            event_packet.event = StopGoPenaltyServed(*unpacked_stop_go)

        case EventCodes.FLASHBACK.value:
            flashback_bytes = event_bytes[:_FLASHBACK_FORMAT_SIZE]
            unpacked_flashback = struct.unpack(_FLASHBACK_FORMAT, flashback_bytes)

            event_packet.event = Flashback(*unpacked_flashback)

        case EventCodes.OVERTAKE.value:
            overtake_bytes = event_bytes[:_OVERTAKE_FORMAT_SIZE]
            unpacked_overtake = struct.unpack(_OVERTAKE_FORMAT, overtake_bytes)

            event_packet.event = Overtake(*unpacked_overtake)

        case EventCodes.SAFETY_CAR.value:
            safety_car_bytes = event_bytes[:_SAFETY_CAR_FORMAT_SIZE]
            unpacked_safety_car = struct.unpack(_SAFETY_CAR_FORMAT, safety_car_bytes)

            event_packet.event = SafetyCar(*unpacked_safety_car)

        case EventCodes.COLLISION.value:
            collision_bytes = event_bytes[:_COLLISION_FORMAT_SIZE]
            unpacked_collision = struct.unpack(_COLLISION_FORMAT, collision_bytes)

            event_packet.event = Collision(*unpacked_collision)

        case EventCodes.BUTTON_STATUS.value:
            buttons_bytes = event_bytes[:_BUTTONS_FORMAT_SIZE]
            unpacked_buttons = struct.unpack(_BUTTONS_FORMAT, buttons_bytes)

            event_packet.event = Buttons(*unpacked_buttons)

            pressed_buttons = [flag.name for flag in ButtonFlags if flag & event_packet.event.button_status]
            print(f"Buttons pressed = {pressed_buttons}")
        
        case _:
            print(f"Received event of type {EventCodes(event_string_code).name}")

    return event_packet