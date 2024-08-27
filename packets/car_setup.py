import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_CAR_SETUP_FORMAT = "<4B4f9B4fBf"
_CAR_SETUP_FORMAT_SIZE = struct.calcsize(_CAR_SETUP_FORMAT)

@dataclass
class CarSetup:
    wing_front: int                     # uint8     |   Front wing aero
    wing_rear: int                      # uint8     |   Rear wing aero
    diff_throttle_on: int               # uint8     |   Differential adjustment on throttle (percentage)
    diff_throttle_off: int              # uint8     |   Differential adjustment off throttle (percentage)
    camber_front: float                 # float     |   Front camber angle (suspension geometry)
    camber_rear: float                  # float     |   Rear camber angle (suspension geometry)
    toe_front: float                    # float     |   Front toe angle (suspension geometry)
    toe_rear: float                     # float     |   Rear toe angle (suspension geometry)
    suspension_front: int               # uint8     |   Front suspension
    suspension_rear: int                # uint8     |   Rear suspension
    anti_roll_bar_front: int            # uint8     |   Front anti-roll bar
    anti_roll_bar_rear: int             # uint8     |   Rear anti-roll bar
    suspension_height_front: int        # uint8     |   Front ride height
    suspension_height_rear: int         # uint8     |   Rear ride height
    brake_pressure: int                 # uint8     |   Brake pressure (percentage)
    brake_bias: int                     # uint8     |   Brake bias (percentage)
    engine_braking: int                 # uint8     |   Engine braking (percentage)
    tyre_pressure_rear_left: float      # float     |   Rear left tyre pressure (PSI)
    tyre_pressure_rear_right: float     # float     |   Rear right tyre pressure (PSI)
    tyre_pressure_front_left: float     # float     |   Front left tyre pressure (PSI)
    tyre_pressure_front_right: float    # float     |   Front right tyre pressure (PSI)
    ballast: int                        # uint8     |   Ballast
    fuel_load: float                    # float     |   Fuel load

@dataclass # 1133 bytes
class CarSetupPacket:
    header: PacketHeader                #           |   Header
    car_setups: List[CarSetup]          # [22]      |   List of car setups for all cars
    next_front_wing_value: float        # float     |   Value of front wing after next pit stop - player only

    def player_data(self):
        return self.car_setups[self.header.player_car_index]
    
def unpack_car_setup(packet_header: PacketHeader, data: bytes):
    car_setup_bytes = data[:(_CAR_SETUP_FORMAT_SIZE * 22)]
    remaining_bytes = data[(_CAR_SETUP_FORMAT_SIZE * 22):]

    car_setups_list = List[CarSetup]
    for unpacked_car_setup in struct.iter_unpack(_CAR_SETUP_FORMAT, car_setup_bytes):
        car_setups_list.append(CarSetup(*unpacked_car_setup))

    next_front_wing_value = struct.unpack('<f', remaining_bytes)

    return CarSetupPacket(packet_header, car_setups_list, *next_front_wing_value)