from packetHeader import PacketHeader
from dataclasses import dataclass

# Define the CarMotionData struct
@dataclass
class CarMotionData:
    m_worldPositionX: float          # World space X position - metres
    m_worldPositionY: float          # World space Y position
    m_worldPositionZ: float          # World space Z position
    m_worldVelocityX: float          # Velocity in world space X – metres/s
    m_worldVelocityY: float          # Velocity in world space Y
    m_worldVelocityZ: float          # Velocity in world space Z
    m_worldForwardDirX: int          # World space forward X direction (normalised int16)
    m_worldForwardDirY: int          # World space forward Y direction (normalised int16)
    m_worldForwardDirZ: int          # World space forward Z direction (normalised int16)
    m_worldRightDirX: int            # World space right X direction (normalised int16)
    m_worldRightDirY: int            # World space right Y direction (normalised int16)
    m_worldRightDirZ: int            # World space right Z direction (normalised int16)
    m_gForceLateral: float           # Lateral G-Force component
    m_gForceLongitudinal: float      # Longitudinal G-Force component
    m_gForceVertical: float          # Vertical G-Force component
    m_yaw: float                     # Yaw angle in radians
    m_pitch: float                   # Pitch angle in radians
    m_roll: float                    # Roll angle in radians

# Define the PacketMotionData struct
@dataclass
class PacketMotionData:
    m_header: PacketHeader              # Header
    m_carMotionData: list[CarMotionData] # Data for all cars on track (22 cars)

