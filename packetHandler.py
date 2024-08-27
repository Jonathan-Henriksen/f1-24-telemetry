from data.packetHeader import *

def PrintHeader(packetHeader: PacketHeader):
    packetId = PacketID(packetHeader.m_packetId).name
    print('Received ' + packetId + ' packet')