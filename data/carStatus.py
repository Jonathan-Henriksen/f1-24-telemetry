from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class CarStatusData:
    m_tractionControl: int                # Traction control - 0 = off, 1 = medium, 2 = full
    m_antiLockBrakes: int                 # 0 (off) - 1 (on)
    m_fuelMix: int                        # Fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
    m_frontBrakeBias: int                 # Front brake bias (percentage)
    m_pitLimiterStatus: int               # Pit limiter status - 0 = off, 1 = on
    m_fuelInTank: float                   # Current fuel mass
    m_fuelCapacity: float                 # Fuel capacity
    m_fuelRemainingLaps: float            # Fuel remaining in terms of laps (value on MFD)
    m_maxRPM: int                        # Car's max RPM, point of rev limiter
    m_idleRPM: int                       # Car's idle RPM
    m_maxGears: int                      # Maximum number of gears
    m_drsAllowed: int                    # 0 = not allowed, 1 = allowed
    m_drsActivationDistance: int         # 0 = DRS not available, non-zero - DRS will be available in [X] metres
    m_actualTyreCompound: int            # Tyre compound used by the car
    m_visualTyreCompound: int            # Visual tyre compound (may differ from actual)
    m_tyresAgeLaps: int                  # Age in laps of the current set of tyres
    m_vehicleFiaFlags: int               # FIA flags - -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow
    m_enginePowerICE: float              # Engine power output of ICE (W)
    m_enginePowerMGUK: float             # Engine power output of MGU-K (W)
    m_ersStoreEnergy: float              # ERS energy store in Joules
    m_ersDeployMode: int                 # ERS deployment mode - 0 = none, 1 = medium, 2 = hotlap, 3 = overtake
    m_ersHarvestedThisLapMGUK: float     # ERS energy harvested this lap by MGU-K
    m_ersHarvestedThisLapMGUH: float     # ERS energy harvested this lap by MGU-H
    m_ersDeployedThisLap: float          # ERS energy deployed this lap
    m_networkPaused: int                 # Whether the car is paused in a network game

@dataclass
class PacketCarStatusData:
    m_header: PacketHeader                 # Header
    m_carStatusData: List[CarStatusData]  # List of car status data for all cars