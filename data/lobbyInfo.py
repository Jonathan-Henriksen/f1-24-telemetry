from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class LobbyInfoData:
    m_aiControlled: int       # Whether the vehicle is AI (1) or Human (0) controlled
    m_teamId: int             # Team id - see appendix (255 if no team currently selected)
    m_nationality: int        # Nationality of the driver
    m_platform: int           # 1 = Steam, 3 = PlayStation, 4 = Xbox, 6 = Origin, 255 = unknown
    m_name: str               # Name of participant in UTF-8 format – null terminated
    m_carNumber: int          # Car number of the player
    m_yourTelemetry: int      # The player's UDP setting, 0 = restricted, 1 = public
    m_showOnlineNames: int    # The player's show online names setting, 0 = off, 1 = on
    m_techLevel: int          # F1 World tech level
    m_readyStatus: int        # 0 = not ready, 1 = ready, 2 = spectating

@dataclass
class PacketLobbyInfoData:
    m_header: PacketHeader                 # Header
    m_numPlayers: int                     # Number of players in the lobby data
    m_lobbyPlayers: List[LobbyInfoData]   # List of lobby player data
