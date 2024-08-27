import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_TYRE_SETS_FORMAT = '<BBBBBBBHB'
_TYRE_SETS_FORMAT_SIZE = struct.calcsize(_TYRE_SETS_FORMAT)

@dataclass
class TyreSet:
    compound: int                   # uint8     |   Actual tyre compound used
    compound_visual: int            # uint8     |   Visual tyre compound used
    wear: int                       # uint8     |   Tyre wear (percentage)
    available: int                  # uint8     |   Whether this set is currently available
    recommended_session: int        # uint8     |   Recommended session for tyre set
    num_of_laps_left: int           # uint8     |   Laps left in this tyre set
    num_of_laps_recommended: int    # uint8     |   Max number of laps recommended for this compound
    lap_delta_time: int             # uint16    |   Lap delta time in milliseconds compared to fitted set
    fitted: int                     # uint8     |   Whether the set is fitted or not


@dataclass # 231 bytes
class TyreSetsPacket:
    header: PacketHeader            #           |   Header
    car_index: int                  # uint8     |   Index of the car this data relates to
    tyre_sets: List[TyreSet]        # [20]      |   20 sets of data (13 dry + 7 wet)
    fitted_index: int               # uint8     |   Index into array of fitted tyre

def unpack_tyre_sets(packet_header: PacketHeader, data: bytes):
    uint8_format = '<B'
    uint8_size = struct.calcsize(uint8_format)

    # Car Index
    car_index = struct.unpack(uint8_format, data[:uint8_size])

    # Tyre Sets
    tyre_sets_list_format_size = (_TYRE_SETS_FORMAT_SIZE * 20)
    tyre_sets_bytes = data[uint8_size:uint8_size + tyre_sets_list_format_size]

    tyre_sets_list = []

    for unpacked_tyre_set in struct.iter_unpack(_TYRE_SETS_FORMAT, tyre_sets_bytes):
        tyre_sets_list.append(TyreSet(*unpacked_tyre_set))

    # Fitted Index
    fitted_index = struct.unpack(uint8_format, data[uint8_size + tyre_sets_list_format_size:])

    return TyreSetsPacket(packet_header, car_index, tyre_sets_list, fitted_index)