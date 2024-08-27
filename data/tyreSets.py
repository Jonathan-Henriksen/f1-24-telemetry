from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

from dataclasses import dataclass
from typing import List

@dataclass
class TyreSetData:
    m_actualTyreCompound: int    # Actual tyre compound used
    m_visualTyreCompound: int    # Visual tyre compound used
    m_wear: int                  # Tyre wear (percentage)
    m_available: int             # Whether this set is currently available
    m_recommendedSession: int    # Recommended session for tyre set
    m_lifeSpan: int              # Laps left in this tyre set
    m_usableLife: int            # Max number of laps recommended for this compound
    m_lapDeltaTime: int          # Lap delta time in milliseconds compared to fitted set
    m_fitted: int                # Whether the set is fitted or not

@dataclass
class PacketTyreSetsData:
    m_header: PacketHeader               # Header

    m_carIdx: int                       # Index of the car this data relates to

    m_tyreSetData: List[TyreSetData]    # 20 sets of data (13 dry + 7 wet)

    m_fittedIdx: int                    # Index into array of fitted tyre
