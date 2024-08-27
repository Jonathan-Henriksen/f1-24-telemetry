from enum import Enum

class PacketIDs(Enum):
    MOTION = 0           # Contains all motion data for player’s car – only sent while player is in control
    SESSION = 1          # Data about the session – track, time left
    LAP_DATA = 2         # Data about all the lap times of cars in the session
    EVENT = 3            # Various notable events that happen during a session
    PARTICIPANTS = 4     # List of participants in the session, mostly relevant for multiplayer
    CAR_SETUPS = 5       # Packet detailing car setups for cars in the race
    CAR_TELEMETRY = 6    # Telemetry data for all cars
    CAR_STATUS = 7       # Status data for all cars
    FINAL_CLASSIFICATION = 8 # Final classification confirmation at the end of a race
    LOBBY_INFO = 9       # Information about players in a multiplayer lobby
    CAR_DAMAGE = 10      # Damage status for all cars
    SESSION_HISTORY = 11 # Lap and tyre data for session
    TYRE_SETS = 12       # Extended tyre set data
    MOTION_EX = 13       # Extended motion data for player car
    TIME_TRIAL = 14      # Time Trial specific data