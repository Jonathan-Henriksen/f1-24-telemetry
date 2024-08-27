import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_CAR_STATUS_FORMAT = '<BBBBBfffHHBBHBBBBfffBfffB'

@dataclass
class CarStatus:
    traction_control: int                   # uint8     |   Traction control - 0 = off, 1 = medium, 2 = full
    anti_lock_brakes: int                   # uint8     |   0 (off) - 1 (on)
    fuel_mix: int                           # uint8     |   Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    front_brake_bias: int                   # uint8     |   Front brake bias (percentage)
    pit_limiter_status: int                 # uint8     |   Pit limiter status - 0 = off, 1 = on
    fuel_in_tank: float                     # float     |   Current fuel mass
    fual_capacity: float                    # float     |   Fuel capacity
    fuel_remaining_laps: float              # float     |   Fuel remaining in terms of laps (value on MFD)
    rpm_max: int                            # uint16    |   Car's max RPM, point of rev limiter
    rpm_idle: int                           # uint16    |   Car's idle RPM
    gears_max: int                          # uint8     |   Maximum number of gears
    drs_allowed: int                        # uint8     |   0 = not allowed, 1 = allowed
    drs_activation_distance: int            # uint16    |   0 = DRS not available, non-zero - DRS will be available in [X] metres
    tyre_compound: int                      # uint8     |   Tyre compound used by the car
    tyre_compound_visual: int               # uint8     |   Visual tyre compound (may differ from actual)
    tyre_age_laps: int                      # uint8     |   Age in laps of the current set of tyres
    fia_flags: int                          # uint8     |   FIA flags - -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow
    engine_power_ice: float                 # float     |   Engine power output of ICE (W)
    engine_power_mguk: float                # float     |   Engine power output of MGU-K (W)
    ers_stored_energy: float                # float     |   ERS energy store in Joules
    ers_deploy_mode: int                    # uint8     |   ERS deployment mode - 0 = none, 1 = medium, 2 = hotlap, 3 = overtake
    ers_harvested_this_lap_mguk: float      # float     |   ERS energy harvested this lap by MGU-K
    ers_harvested_this_lap_mguh: float      # float     |   ERS energy harvested this lap by MGU-H
    ers_deployed_this_lap: float            # float     |   ERS energy deployed this lap
    network_paused: int                     # uint8     |   Whether the car is paused in a network game

@dataclass # 1239 bytes
class CarStatusPacket:
    header: PacketHeader                    #           |   Header
    car_status_list: List[CarStatus]             # [22]      |   List of car status data for all cars

    def player_data(self):
        return self.car_status_list[self.header.player_car_index]

def unpack_car_status(packet_header: PacketHeader, data: bytes):
    car_status_list = []

    for unpacked_car_status in struct.iter_unpack(_CAR_STATUS_FORMAT, data):
        car_status_list.append(CarStatus(*unpacked_car_status))

    return CarStatusPacket(packet_header, car_status_list)