import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_MOTION_DATA_FORMAT = '<6f6h6f'

@dataclass
class MotionData:
    world_position_x: float                 # float     |    World space X position - metres
    world_position_y: float                 # float     |    World space Y position
    world_position_z: float                 # float     |    World space Z position
    world_velocity_x: float                 # float     |    Velocity in world space X – metres/s
    world_velocity_y: float                 # float     |    Velocity in world space Y
    world_velocity_z: float                 # float     |    Velocity in world space Z
    world_forward_dir_x: int                # uint16    |    World space forward X direction (normalised int16)
    world_forward_dir_y: int                # uint16    |    World space forward Y direction (normalised int16)
    world_forward_dir_z: int                # uint16    |    World space forward Z direction (normalised int16)
    world_right_dir_x: int                  # uint16    |    World space right X direction (normalised int16)
    world_right_dir_y: int                  # uint16    |    World space right Y direction (normalised int16)
    world_right_dir_z: int                  # uint16    |    World space right Z direction (normalised int16)
    g_force_lateral: float                  # uint16    |    Lateral G-Force component
    g_force_longitudinal: float             # float     |    Longitudinal G-Force component
    g_force_vertical: float                 # float     |    Vertical G-Force component
    yaw: float                              # float     |    Yaw angle in radians
    pitch: float                            # float     |    Pitch angle in radians
    roll: float                             # float     |    Roll angle in radians

@dataclass # 1349 bytes
class MotionDataPacket:
    header: PacketHeader                    #           |   Header
    car_motion_data: List[MotionData]       # [22]         |   Data for all cars on track (22 cars)

def unpack_motion_data(packet_header: PacketHeader, data: bytes):
    motion_data_list = List[MotionData]

    for unpacked_motion_data in struct.iter_unpack(_MOTION_DATA_FORMAT, data):
        motion_data_list.append(MotionData(*unpacked_motion_data))

    return MotionDataPacket(packet_header, motion_data_list)