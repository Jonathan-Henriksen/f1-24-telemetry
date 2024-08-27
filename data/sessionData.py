from packetHeader import PacketHeader
from dataclasses import dataclass

# Define the MarshalZone struct
@dataclass
class MarshalZone:
    m_zoneStart: float  # Fraction (0..1) of way through the lap the marshal zone starts
    m_zoneFlag: int     # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow

# Define the WeatherForecastSample struct
@dataclass
class WeatherForecastSample:
    m_sessionType: int                # uint8 - 0 = unknown, see appendix
    m_timeOffset: int                 # uint8 - Time in minutes the forecast is for
    m_weather: int                    # uint8 - Weather (0 = clear, 1 = light cloud, etc.)
    m_trackTemperature: int           # int8 - Track temp in degrees Celsius
    m_trackTemperatureChange: int     # int8 - Track temp. change (0 = up, 1 = down, 2 = no change)
    m_airTemperature: int             # int8 - Air temp. in degrees Celsius
    m_airTemperatureChange: int       # int8 - Air temp. change (0 = up, 1 = down, 2 = no change)
    m_rainPercentage: int             # uint8 - Rain percentage (0-100)

# PacketSessionData struct
@dataclass
class PacketSessionData:
    m_header: PacketHeader                # Header
    m_weather: int                        # uint8 - Weather (0 = clear, 1 = light cloud, etc.)
    m_trackTemperature: int               # int8 - Track temp. in degrees Celsius
    m_airTemperature: int                 # int8 - Air temp. in degrees Celsius
    m_totalLaps: int                      # uint8 - Total number of laps in this race
    m_trackLength: int                    # uint16 - Track length in metres
    m_sessionType: int                    # uint8 - Session type (0 = unknown, etc.)
    m_trackId: int                        # int8 - Track ID (-1 for unknown)
    m_formula: int                        # uint8 - Formula (0 = F1 Modern, etc.)
    m_sessionTimeLeft: int                # uint16 - Time left in session (seconds)
    m_sessionDuration: int                # uint16 - Session duration (seconds)
    m_pitSpeedLimit: int                  # uint8 - Pit speed limit (km/h)
    m_gamePaused: int                     # uint8 - Whether the game is paused
    m_isSpectating: int                   # uint8 - Whether the player is spectating
    m_spectatorCarIndex: int              # uint8 - Index of the car being spectated
    m_sliProNativeSupport: int            # uint8 - SLI Pro support (0 = inactive, 1 = active)
    m_numMarshalZones: int                # uint8 - Number of marshal zones to follow
    m_marshalZones: list[MarshalZone]     # List of marshal zones – max 21
    m_safetyCarStatus: int                # uint8 - Safety car status (0 = no safety car, etc.)
    m_networkGame: int                    # uint8 - Network game (0 = offline, 1 = online)
    m_numWeatherForecastSamples: int      # uint8 - Number of weather forecast samples to follow
    m_weatherForecastSamples: list[WeatherForecastSample]  # Array of weather forecast samples (max 64)
    m_forecastAccuracy: int               # uint8 - 0 = Perfect, 1 = Approximate
    m_aiDifficulty: int                   # uint8 - AI Difficulty rating (0-110)
    m_seasonLinkIdentifier: int           # uint32 - Identifier for season
    m_weekendLinkIdentifier: int          # uint32 - Identifier for weekend
    m_sessionLinkIdentifier: int          # uint32 - Identifier for session
    m_pitStopWindowIdealLap: int          # uint8 - Ideal lap to pit for current strategy
    m_pitStopWindowLatestLap: int         # uint8 - Latest lap to pit for current strategy
    m_pitStopRejoinPosition: int          # uint8 - Predicted position to rejoin
    m_steeringAssist: int                 # uint8 - Steering assist (0 = off, 1 = on)
    m_brakingAssist: int                  # uint8 - Braking assist (0 = off, 1 = low, etc.)
    m_gearboxAssist: int                  # uint8 - Gearbox assist (1 = manual, etc.)
    m_pitAssist: int                      # uint8 - Pit assist (0 = off, 1 = on)
    m_pitReleaseAssist: int               # uint8 - Pit release assist (0 = off, 1 = on)
    m_ERSAssist: int                      # uint8 - ERS assist (0 = off, 1 = on)
    m_DRSAssist: int                      # uint8 - DRS assist (0 = off, 1 = on)
    m_dynamicRacingLine: int              # uint8 - Dynamic racing line (0 = off, 1 = corners, etc.)
    m_dynamicRacingLineType: int          # uint8 - Racing line type (0 = 2D, 1 = 3D)
    m_gameMode: int                       # uint8 - Game mode ID
    m_ruleSet: int                        # uint8 - Ruleset
    m_timeOfDay: int                      # uint32 - Local time of day (minutes since midnight)
    m_sessionLength: int                  # uint8 - Session length (0 = None, etc.)
    m_speedUnitsLeadPlayer: int           # uint8 - Speed units for lead player (0 = MPH, 1 = KPH)
    m_temperatureUnitsLeadPlayer: int     # uint8 - Temperature units for lead player (0 = Celsius, etc.)
    m_speedUnitsSecondaryPlayer: int      # uint8 - Speed units for secondary player
    m_temperatureUnitsSecondaryPlayer: int# uint8 - Temperature units for secondary player
    m_numSafetyCarPeriods: int            # uint8 - Number of safety cars during session
    m_numVirtualSafetyCarPeriods: int     # uint8 - Number of virtual safety cars
    m_numRedFlagPeriods: int              # uint8 - Number of red flags
    m_equalCarPerformance: int            # uint8 - Equal car performance (0 = off, 1 = on)
    m_recoveryMode: int                   # uint8 - Recovery mode (0 = None, 1 = Flashbacks, etc.)
    m_flashbackLimit: int                 # uint8 - Flashback limit (0 = Low, etc.)
    m_surfaceType: int                    # uint8 - Surface type (0 = Simplified, 1 = Realistic)
    m_lowFuelMode: int                    # uint8 - Low fuel mode (0 = Easy, 1 = Hard)
    m_raceStarts: int                     # uint8 - Race starts (0 = Manual, 1 = Assisted)
    m_tyreTemperature: int                # uint8 - Tyre temperature (0 = Surface only, etc.)
    m_pitLaneTyreSim: int                 # uint8 - Pit lane tyre sim (0 = On, 1 = Off)
    m_carDamage: int                      # uint8 - Car damage (0 = Off, 1 = Reduced, etc.)
    m_carDamageRate: int                  # uint8 - Car damage rate (0 = Reduced, etc.)
    m_collisions: int                     # uint8 - Collisions (0 = Off, 1 = Player-to-Player off, etc.)
    m_collisionsOffForFirstLapOnly: int   # uint8 - Collisions off for first lap only (0 = Disabled, etc.)
    m_mpUnsafePitRelease: int             # uint8 - Multiplayer unsafe pit release (0 = On, etc.)
    m_mpOffForGriefing: int               # uint8 - Multiplayer off for griefing (0 = Disabled, etc.)
    m_cornerCuttingStringency: int        # uint8 - Corner cutting stringency (0 = Regular, etc.)
    m_parcFermeRules: int                 # uint8 - Parc Ferme rules (0 = Off, 1 = On)
    m_pitStopExperience: int              # uint8 - Pit stop experience (0 = Automatic, etc.)
    m_safetyCar: int                      # uint8 - Safety car (0 = Off, etc.)
    m_safetyCarExperience: int            # uint8 - Safety car experience (0 = Broadcast, etc.)
    m_formationLap: int                   # uint8 - Formation lap (0 = Off, 1 = On)
    m_formationLapExperience: int         # uint8 - Formation lap experience (0 = Broadcast, etc.)
    m_redFlags: int                       # uint8 - Red flags (0 = Off, etc.)
    m_affectsLicenceLevelSolo: int        # uint8 - Affects license level (solo)
    m_affectsLicenceLevelMP: int          # uint8 - Affects license level (MP)
    m_numSessionsInWeekend: int           # uint8 - Number of sessions in weekend
    m_weekendStructure: list[int]         # List of session types to show weekend structure
    m_sector2LapDistanceStart: float      # Sector 2 start distance (meters)
    m_sector3LapDistanceStart: float      # Sector 3 start distance (meters)
