UDP Server written in python, with the purpose of listening for incoming telemetry UDP packets from the F1 24 game.

All models and enums have been implemented as specified in the official documentation(see below), including some basic functions to unpack udp packets into python classes for convenience.

This project only serves as a base upon which to build more complex programs and should be easily expandable from the 'match' statement in main.py, to only be handling the needed packet types.

Official Documentation -> https://answers.ea.com/t5/General-Discussion/F1-24-UDP-Specification/m-p/13745520
