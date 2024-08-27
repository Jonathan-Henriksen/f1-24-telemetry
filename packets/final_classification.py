import struct

from packets.packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_FINAL_CLASSIFIATION_FORMAT = '<6BLd27B'
_FINAL_CLASSIFIATION_FORMAT_SIZE = struct.calcsize(_FINAL_CLASSIFIATION_FORMAT)

@dataclass
class FinalClassification:
    position: int                           # uint8     |    Finishing position
    num_of_laps: int                        # uint8     |    Number of laps completed
    grid_position: int                      # uint8     |    Grid position of the car
    points: int                             # uint8     |    Number of points scored
    num_pit_stops: int                      # uint8     |    Number of pit stops made
    result_status: int                      # uint8     |    Result status - 0 = invalid, 1 = inactive, 2 = active, 3 = finished, 4 = didnotfinish, 5 = disqualified, 6 = not classified, 7 = retired
    best_lap_time_in_ms: int                # uint32    |    Best lap time of the session in milliseconds
    total_race_time: float                  # double    |    Total race time in seconds without penalties
    penalties_time: int                     # uint8     |    Total penalties accumulated in seconds
    num_of_penalties: int                   # uint8     |    Number of penalties applied to this driver
    num_of_tyre_stints: int                 # uint8     |    Number of tyre stints up to maximum
    tyre_stints_actual: List[int]           # uint8[8]  |    Actual tyres used by this driver
    tyre_stints_visual: List[int]           # uint8[8]  |    Visual tyres used by this driver
    tyre_stints_end_laps: List[int]         # uint8[8]  |    The lap number stints end on

@dataclass # 1020 bytes
class FinalClassificationPacket:
    header: PacketHeader                    #           |   Header
    num_cars: int                           # uint8     |   Number of cars in the final classification
    final_classifications: List[FinalClassification]#  |   List of final classification data for all cars

def unpack_final_classification(packet_header: PacketHeader, data: bytes):
    uint8_format = '<B'
    uint8_size = struct.calcsize(uint8_format)

    # Car Index
    num_cars = struct.unpack(uint8_format, data[:uint8_size])

    # Tyre Sets
    final_classification_list_format_size = (_FINAL_CLASSIFIATION_FORMAT_SIZE * num_cars)
    final_classification_list_bytes = data[uint8_size:uint8_size + final_classification_list_format_size]

    final_classification_list = []

    for unpacked_final_classification in struct.iter_unpack(_FINAL_CLASSIFIATION_FORMAT, final_classification_list_bytes):
        final_classification_list.append(FinalClassification(*unpacked_final_classification))

    return FinalClassificationPacket(packet_header, num_cars, final_classification_list)