from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import Union, List
from enum import Enum

class EventCode(Enum):
    SESSION_STARTED = "SSTA"           # Sent when the session starts
    SESSION_ENDED = "SEND"             # Sent when the session ends
    FASTEST_LAP = "FTLP"               # When a driver achieves the fastest lap
    RETIREMENT = "RTMT"                # When a driver retires
    DRS_ENABLED = "DRSE"               # Race control has enabled DRS
    DRS_DISABLED = "DRSD"              # Race control has disabled DRS
    TEAM_MATE_IN_PITS = "TMPT"         # Your team mate has entered the pits
    CHEQUERED_FLAG = "CHQF"            # The chequered flag has been waved
    RACE_WINNER = "RCWN"               # The race winner is announced
    PENALTY_ISSUED = "PENA"            # A penalty has been issued – details in event
    SPEED_TRAP_TRIGGERED = "SPTP"      # Speed trap has been triggered by fastest speed
    START_LIGHTS = "STLG"              # Start lights – number shown
    LIGHTS_OUT = "LGOT"               # Lights out
    DRIVE_THROUGH_SERVED = "DTSV"      # Drive through penalty served
    STOP_GO_SERVED = "SGSV"            # Stop go penalty served
    FLASHBACK = "FLBK"                 # Flashback activated
    BUTTON_STATUS = "BUTN"             # Button status changed
    RED_FLAG = "RDFL"                  # Red flag shown
    OVERTAKE = "OVTK"                  # Overtake occurred
    SAFETY_CAR = "SCAR"                # Safety car event – details in event
    COLLISION = "COLL"                 # Collision between two vehicles has occurred

@dataclass
class FastestLapEvent:
    vehicleIdx: int  # Vehicle index of car achieving fastest lap
    lapTime: float   # Lap time is in seconds

@dataclass
class RetirementEvent:
    vehicleIdx: int  # Vehicle index of car retiring

@dataclass
class TeamMateInPitsEvent:
    vehicleIdx: int  # Vehicle index of team mate

@dataclass
class RaceWinnerEvent:
    vehicleIdx: int  # Vehicle index of the race winner

@dataclass
class PenaltyEvent:
    penaltyType: int          # Penalty type – see Appendices
    infringementType: int    # Infringement type – see Appendices
    vehicleIdx: int          # Vehicle index of the car the penalty is applied to
    otherVehicleIdx: int     # Vehicle index of the other car involved
    time: int                # Time gained, or time spent doing action in seconds
    lapNum: int              # Lap the penalty occurred on
    placesGained: int        # Number of places gained by this

@dataclass
class SpeedTrapEvent:
    vehicleIdx: int                    # Vehicle index of the vehicle triggering speed trap
    speed: float                       # Top speed achieved in kilometres per hour
    isOverallFastestInSession: int     # Overall fastest speed in session = 1, otherwise 0
    isDriverFastestInSession: int      # Fastest speed for driver in session = 1, otherwise 0
    fastestVehicleIdxInSession: int    # Vehicle index of the vehicle that is the fastest in this session
    fastestSpeedInSession: float       # Speed of the vehicle that is the fastest in this session

@dataclass
class StartLightsEvent:
    numLights: int  # Number of lights showing

@dataclass
class DriveThroughPenaltyServedEvent:
    vehicleIdx: int  # Vehicle index of the vehicle serving drive through

@dataclass
class StopGoPenaltyServedEvent:
    vehicleIdx: int  # Vehicle index of the vehicle serving stop go

@dataclass
class FlashbackEvent:
    flashbackFrameIdentifier: int  # Frame identifier flashed back to
    flashbackSessionTime: float    # Session time flashed back to

@dataclass
class ButtonsEvent:
    buttonStatus: int  # Bit flags specifying which buttons are being pressed

@dataclass
class OvertakeEvent:
    overtakingVehicleIdx: int    # Vehicle index of the vehicle overtaking
    beingOvertakenVehicleIdx: int  # Vehicle index of the vehicle being overtaken

@dataclass
class SafetyCarEvent:
    safetyCarType: int    # 0 = No Safety Car, 1 = Full Safety Car
                          # 2 = Virtual Safety Car, 3 = Formation Lap Safety Car
    eventType: int        # 0 = Deployed, 1 = Returning, 2 = Returned
                          # 3 = Resume Race

@dataclass
class CollisionEvent:
    vehicle1Idx: int  # Vehicle index of the first vehicle involved in the collision
    vehicle2Idx: int  # Vehicle index of the second vehicle involved in the collision

@dataclass
class PacketEventData:
    header: PacketHeader           # Header
    eventStringCode: List[int]    # Event string code, see below
    eventDetails: Union[
        FastestLapEvent,
        RetirementEvent,
        TeamMateInPitsEvent,
        RaceWinnerEvent,
        PenaltyEvent,
        SpeedTrapEvent,
        StartLightsEvent,
        DriveThroughPenaltyServedEvent,
        StopGoPenaltyServedEvent,
        FlashbackEvent,
        ButtonsEvent,
        OvertakeEvent,
        SafetyCarEvent,
        CollisionEvent
    ]  # Event details - should be interpreted differently for each type