from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class CarSetupData:
    m_frontWing: int               # Front wing aero
    m_rearWing: int                # Rear wing aero
    m_onThrottle: int              # Differential adjustment on throttle (percentage)
    m_offThrottle: int             # Differential adjustment off throttle (percentage)
    m_frontCamber: float           # Front camber angle (suspension geometry)
    m_rearCamber: float            # Rear camber angle (suspension geometry)
    m_frontToe: float              # Front toe angle (suspension geometry)
    m_rearToe: float               # Rear toe angle (suspension geometry)
    m_frontSuspension: int         # Front suspension
    m_rearSuspension: int          # Rear suspension
    m_frontAntiRollBar: int        # Front anti-roll bar
    m_rearAntiRollBar: int         # Rear anti-roll bar
    m_frontSuspensionHeight: int   # Front ride height
    m_rearSuspensionHeight: int    # Rear ride height
    m_brakePressure: int           # Brake pressure (percentage)
    m_brakeBias: int               # Brake bias (percentage)
    m_engineBraking: int           # Engine braking (percentage)
    m_rearLeftTyrePressure: float  # Rear left tyre pressure (PSI)
    m_rearRightTyrePressure: float # Rear right tyre pressure (PSI)
    m_frontLeftTyrePressure: float # Front left tyre pressure (PSI)
    m_frontRightTyrePressure: float# Front right tyre pressure (PSI)
    m_ballast: int                 # Ballast
    m_fuelLoad: float              # Fuel load

@dataclass
class PacketCarSetupData:
    m_header: PacketHeader        # Header
    m_carSetups: List[CarSetupData] # List of car setups for all cars
    m_nextFrontWingValue: float   # Value of front wing after next pit stop - player only