from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class LapHistoryData:
    m_lapTimeInMS: int                 # Lap time in milliseconds
    m_sector1TimeMSPart: int          # Sector 1 milliseconds part
    m_sector1TimeMinutesPart: int     # Sector 1 whole minute part
    m_sector2TimeMSPart: int          # Sector 2 time milliseconds part
    m_sector2TimeMinutesPart: int     # Sector 2 whole minute part
    m_sector3TimeMSPart: int          # Sector 3 time milliseconds part
    m_sector3TimeMinutesPart: int     # Sector 3 whole minute part
    m_lapValidBitFlags: int           # 0x01 bit set-lap valid, 0x02 bit set-sector 1 valid
                                      # 0x04 bit set-sector 2 valid, 0x08 bit set-sector 3 valid

@dataclass
class TyreStintHistoryData:
    m_endLap: int                    # Lap the tyre usage ends on (255 if current tyre)
    m_tyreActualCompound: int        # Actual tyres used by this driver
    m_tyreVisualCompound: int        # Visual tyres used by this driver

@dataclass
class PacketSessionHistoryData:
    m_header: PacketHeader                     # Header

    m_carIdx: int                            # Index of the car this lap data relates to
    m_numLaps: int                           # Number of laps in the data (including current partial lap)
    m_numTyreStints: int                     # Number of tyre stints in the data

    m_bestLapTimeLapNum: int                 # Lap the best lap time was achieved on
    m_bestSector1LapNum: int                 # Lap the best Sector 1 time was achieved on
    m_bestSector2LapNum: int                 # Lap the best Sector 2 time was achieved on
    m_bestSector3LapNum: int                 # Lap the best Sector 3 time was achieved on

    m_lapHistoryData: List[LapHistoryData]   # 100 laps of data max
    m_tyreStintsHistoryData: List[TyreStintHistoryData]  # Up to 8 tyre stints
