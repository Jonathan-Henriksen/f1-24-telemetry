from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class FinalClassificationData:
    m_position: int                   # Finishing position
    m_numLaps: int                   # Number of laps completed
    m_gridPosition: int              # Grid position of the car
    m_points: int                    # Number of points scored
    m_numPitStops: int               # Number of pit stops made
    m_resultStatus: int              # Result status - 0 = invalid, 1 = inactive, 2 = active
                                     # 3 = finished, 4 = didnotfinish, 5 = disqualified
                                     # 6 = not classified, 7 = retired
    m_bestLapTimeInMS: int           # Best lap time of the session in milliseconds
    m_totalRaceTime: float           # Total race time in seconds without penalties
    m_penaltiesTime: int             # Total penalties accumulated in seconds
    m_numPenalties: int              # Number of penalties applied to this driver
    m_numTyreStints: int             # Number of tyre stints up to maximum
    m_tyreStintsActual: List[int]    # Actual tyres used by this driver
    m_tyreStintsVisual: List[int]    # Visual tyres used by this driver
    m_tyreStintsEndLaps: List[int]   # The lap number stints end on

@dataclass
class PacketFinalClassificationData:
    m_header: PacketHeader                       # Header
    m_numCars: int                              # Number of cars in the final classification
    m_classificationData: List[FinalClassificationData]  # List of final classification data for all cars