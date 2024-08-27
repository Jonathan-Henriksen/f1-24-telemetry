import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_CAR_TELEMETRY_FORMAT = '<HfffBBHBBH4H4B4BH4f4B'
_CAR_TELEMETRY_FORMAT_SIZE = struct.calcsize(_CAR_TELEMETRY_FORMAT)

@dataclass
class CarTelemetry:
    speed: int                                  # uint16    |   Speed of car in kilometres per hour
    throttle: float                             # float     |   Amount of throttle applied (0.0 to 1.0)
    steer: float                                # float     |   Steering (-1.0 (full lock left) to 1.0 (full lock right))
    brake: float                                # float     |   Amount of brake applied (0.0 to 1.0)
    clutch: int                                 # uint8     |   Amount of clutch applied (0 to 100)
    gear: int                                   # uint8     |   Gear selected (1-8, N=0, R=-1)
    engine_rpm: int                             # uint16    |   Engine RPM
    drs: int                                    # uint8     |   0 = off, 1 = on
    rev_lights_percent: int                     # uint8     |   Rev lights indicator (percentage)
    rev_lights_bit_value: int                   # uint16    |   Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
    brakes_rear_left_temperature: int           # uint16    |   Brakes temperature (celsius)
    brakes_rear_right_temperature: int          # uint16    |   Brakes temperature (celsius)
    brakes_front_left_temperature: int          # uint16    |   Brakes temperature (celsius)
    brakes_front_right_temperature: int         # uint16    |   Brakes temperature (celsius)
    tyres_rear_left_temperature_surface: int    # uint8     |   Tyres surface temperature (celsius)
    tyres_rear_right_temperature_surface: int   # uint8     |   Tyres surface temperature (celsius)
    tyres_front_left_temperature_surface: int   # uint8     |   Tyres surface temperature (celsius)
    tyres_front_right_temperature_surface: int  # uint8     |   Tyres surface temperature (celsius)
    tyres_rear_left_temperature_inner: int      # uint8     |   Tyres inner temperature (celsius)
    tyres_rear_right_temperature_inner: int     # uint8     |   Tyres inner temperature (celsius)
    tyres_front_left_temperature_inner: int     # uint8     |   Tyres inner temperature (celsius)
    tyres_front_right_temperature_inner: int    # uint8     |   Tyres inner temperature (celsius)
    engine_temperature: int                     # uint16    |   Engine temperature (celsius)
    tyres_rear_left_pressure: float             # float     |   Tyres pressure (PSI)
    tyres_rear_right_pressure: float            # float     |   Tyres pressure (PSI)
    tyres_front_left_pressure: float            # float     |   Tyres pressure (PSI)
    tyres_front_right_pressure: float           # float     |   Tyres pressure (PSI)
    tyres_rear_left_surface_type: int           # uint8     |   Driving surface, see appendices
    tyres_rear_right_surface_type: int          # uint8     |   Driving surface, see appendices
    tyres_front_left_surface_type: int          # uint8     |   Driving surface, see appendices
    tyres_front_right_surface_type: int         # uint8     |   Driving surface, see appendices

@dataclass # 1352 bytes
class CarTelemetryPacket:
    header: PacketHeader                        #           |   Header
    car_telemetry_list: List[CarTelemetry]         # [22]      |   List of car telemetry data for all cars
    mfd_panel_index: int                        # uint8     |   Index of MFD panel open - 255 = MFD closed
    mfd_panel_index_secondary_player: int       # uint8     |   Index of MFD panel open for secondary player
    suggested_gear: int                         # int8      |   Suggested gear for the player (1-8), 0 if no gear suggested

    def player_data(self):
        return self.car_telemetry_list[self.header.player_car_index]
    
def unpack_car_telemetry(packet_header: PacketHeader, data: bytes):
    car_telemetry_bytes = data[:(_CAR_TELEMETRY_FORMAT_SIZE * 22)]
    remaining_bytes = data[(_CAR_TELEMETRY_FORMAT_SIZE * 22):]

    car_telemetry_list = List[CarTelemetry]

    for unpacked_car_telemetry in struct.iter_unpack(_CAR_TELEMETRY_FORMAT, car_telemetry_bytes):
        car_telemetry_list.append(CarTelemetry(*unpacked_car_telemetry))

    remaining_fields = struct.unpack('<BBb', remaining_bytes)

    return CarTelemetryPacket(packet_header, car_telemetry_list, *remaining_fields)