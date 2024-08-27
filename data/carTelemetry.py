from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class CarTelemetryData:
    m_speed: int                          # Speed of car in kilometres per hour
    m_throttle: float                     # Amount of throttle applied (0.0 to 1.0)
    m_steer: float                        # Steering (-1.0 (full lock left) to 1.0 (full lock right))
    m_brake: float                        # Amount of brake applied (0.0 to 1.0)
    m_clutch: int                         # Amount of clutch applied (0 to 100)
    m_gear: int                           # Gear selected (1-8, N=0, R=-1)
    m_engineRPM: int                      # Engine RPM
    m_drs: int                            # 0 = off, 1 = on
    m_revLightsPercent: int               # Rev lights indicator (percentage)
    m_revLightsBitValue: int              # Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
    m_brakesTemperature: List[int]        # Brakes temperature (celsius)
    m_tyresSurfaceTemperature: List[int] # Tyres surface temperature (celsius)
    m_tyresInnerTemperature: List[int]   # Tyres inner temperature (celsius)
    m_engineTemperature: int              # Engine temperature (celsius)
    m_tyresPressure: List[float]          # Tyres pressure (PSI)
    m_surfaceType: List[int]             # Driving surface, see appendices

@dataclass
class PacketCarTelemetryData:
    m_header: PacketHeader                 # Header
    m_carTelemetryData: List[CarTelemetryData] # List of car telemetry data for all cars
    m_mfdPanelIndex: int                  # Index of MFD panel open - 255 = MFD closed
    m_mfdPanelIndexSecondaryPlayer: int   # Index of MFD panel open for secondary player
    m_suggestedGear: int                  # Suggested gear for the player (1-8), 0 if no gear suggested