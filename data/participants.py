from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class ParticipantData:
    m_aiControlled: int      # Whether the vehicle is AI (1) or Human (0) controlled
    m_driverId: int          # Driver id - see appendix, 255 if network human
    m_networkId: int         # Network id – unique identifier for network players
    m_teamId: int            # Team id - see appendix
    m_myTeam: int            # My team flag – 1 = My Team, 0 = otherwise
    m_raceNumber: int        # Race number of the car
    m_nationality: int       # Nationality of the driver
    m_name: str              # Name of participant in UTF-8 format – null terminated
    m_yourTelemetry: int     # The player's UDP setting, 0 = restricted, 1 = public
    m_showOnlineNames: int   # The player's show online names setting, 0 = off, 1 = on
    m_techLevel: int         # F1 World tech level    
    m_platform: int          # 1 = Steam, 3 = PlayStation, 4 = Xbox, 6 = Origin, 255 = unknown

@dataclass
class PacketParticipantsData:
    m_header: PacketHeader              # Header
    m_numActiveCars: int               # Number of active cars in the data – should match number of cars on HUD
    m_participants: List[ParticipantData] # List of participants
