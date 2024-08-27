from packetHeader import PacketHeader
from dataclasses import dataclass
from typing import List

@dataclass
class LapData:
    m_lastLapTimeInMS: int                # Last lap time in milliseconds
    m_currentLapTimeInMS: int             # Current time around the lap in milliseconds
    m_sector1TimeMSPart: int              # Sector 1 time milliseconds part
    m_sector1TimeMinutesPart: int         # Sector 1 whole minute part
    m_sector2TimeMSPart: int              # Sector 2 time milliseconds part
    m_sector2TimeMinutesPart: int         # Sector 2 whole minute part
    m_deltaToCarInFrontMSPart: int        # Time delta to car in front milliseconds part
    m_deltaToCarInFrontMinutesPart: int   # Time delta to car in front whole minute part
    m_deltaToRaceLeaderMSPart: int        # Time delta to race leader milliseconds part
    m_deltaToRaceLeaderMinutesPart: int   # Time delta to race leader whole minute part
    m_lapDistance: float                  # Distance vehicle is around current lap in metres
                                          # Could be negative if line hasn’t been crossed yet
    m_totalDistance: float                # Total distance travelled in session in metres
                                          # Could be negative if line hasn’t been crossed yet
    m_safetyCarDelta: float               # Delta in seconds for safety car
    m_carPosition: int                    # Car race position
    m_currentLapNum: int                  # Current lap number
    m_pitStatus: int                      # 0 = none, 1 = pitting, 2 = in pit area
    m_numPitStops: int                    # Number of pit stops taken in this race
    m_sector: int                         # 0 = sector1, 1 = sector2, 2 = sector3
    m_currentLapInvalid: int              # Current lap invalid - 0 = valid, 1 = invalid
    m_penalties: int                      # Accumulated time penalties in seconds to be added
    m_totalWarnings: int                  # Accumulated number of warnings issued
    m_cornerCuttingWarnings: int          # Accumulated number of corner cutting warnings issued
    m_numUnservedDriveThroughPens: int    # Num drive through penalties left to serve
    m_numUnservedStopGoPens: int          # Num stop go penalties left to serve
    m_gridPosition: int                   # Grid position the vehicle started the race in
    m_driverStatus: int                   # Status of driver - 0 = in garage, 1 = flying lap
                                          # 2 = in lap, 3 = out lap, 4 = on track
    m_resultStatus: int                   # Result status - 0 = invalid, 1 = inactive, 2 = active
                                          # 3 = finished, 4 = did not finish, 5 = disqualified
                                          # 6 = not classified, 7 = retired
    m_pitLaneTimerActive: int             # Pit lane timing, 0 = inactive, 1 = active
    m_pitLaneTimeInLaneInMS: int          # If active, the current time spent in the pit lane in ms
    m_pitStopTimerInMS: int               # Time of the actual pit stop in ms
    m_pitStopShouldServePen: int          # Whether the car should serve a penalty at this stop
    m_speedTrapFastestSpeed: float        # Fastest speed through speed trap for this car in kmph
    m_speedTrapFastestLap: int            # Lap no the fastest speed was achieved, 255 = not set


@dataclass
class PacketLapData:
    m_header: PacketHeader                # Header

    m_lapData: List[LapData]              # Lap data for all cars on track

    m_timeTrialPBCarIdx: int              # Index of Personal Best car in time trial (255 if invalid)
    m_timeTrialRivalCarIdx: int           # Index of Rival car in time trial (255 if invalid)