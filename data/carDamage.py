from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class CarDamageData:
    m_tyresWear: List[float]                   # Tyre wear (percentage)
    m_tyresDamage: List[int]                   # Tyre damage (percentage)
    m_brakesDamage: List[int]                  # Brakes damage (percentage)
    m_frontLeftWingDamage: int                 # Front left wing damage (percentage)
    m_frontRightWingDamage: int                # Front right wing damage (percentage)
    m_rearWingDamage: int                      # Rear wing damage (percentage)
    m_floorDamage: int                         # Floor damage (percentage)
    m_diffuserDamage: int                      # Diffuser damage (percentage)
    m_sidepodDamage: int                       # Sidepod damage (percentage)
    m_drsFault: int                            # Indicator for DRS fault, 0 = OK, 1 = fault
    m_ersFault: int                            # Indicator for ERS fault, 0 = OK, 1 = fault
    m_gearBoxDamage: int                       # Gear box damage (percentage)
    m_engineDamage: int                        # Engine damage (percentage)
    m_engineMGUHWear: int                      # Engine wear MGU-H (percentage)
    m_engineESWear: int                        # Engine wear ES (percentage)
    m_engineCEWear: int                        # Engine wear CE (percentage)
    m_engineICEWear: int                       # Engine wear ICE (percentage)
    m_engineMGUKWear: int                      # Engine wear MGU-K (percentage)
    m_engineTCWear: int                        # Engine wear TC (percentage)
    m_engineBlown: int                         # Engine blown, 0 = OK, 1 = fault
    m_engineSeized: int                        # Engine seized, 0 = OK, 1 = fault

@dataclass
class PacketCarDamageData:
    m_header: PacketHeader                    # Header
    m_carDamageData: List[CarDamageData]      # List of car damage data for 22 cars
