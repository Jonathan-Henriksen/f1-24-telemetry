import struct

from .packet_header import PacketHeader
from dataclasses import dataclass
from typing import List

_CAR_DAMAGE_FORMAT = "<4f26B"

@dataclass
class CarDamage:
	tyres_rear_left_wear: float          	# float		|	Tyre wear (percentage)
	tyres_rear_right_wear: float            # float     |   Tyre wear (percentage)
	tyres_front_left_wear: float            # float     |   Tyre wear (percentage)
	tyres_front_right_wear: float           # float     |   Tyre wear (percentage)
	tyres_rear_left_damage: int             # uint8     |   Tyre damage (percentage)
	tyres_rear_right_damage: int			# uint8     |   Tyre damage (percentage)
	tyres_front_left_damage: int            # uint8     |   Tyre damage (percentage)
	tyres_front_right_damage: int           # uint8     |   Tyre damage (percentage)
	brakes_rear_left_damage: int			# uint8     |   Brakes damage (percentage)
	brakes__rear_right_damage: int          # uint8     |   Brakes damage (percentage)
	brakes__front_left_damage: int          # uint8     |   Brakes damage (percentage)
	brakes__front_right_damage: int         # uint8     |   Brakes damage (percentage)
	wing_front_left_damage: int             # uint8     |   Front left wing damage (percentage)
	wing_front_right_damage: int            # uint8     |   Front right wing damage (percentage)
	wing_rear_damage: int                   # uint8     |   Rear wing damage (percentage)
	floor_damage: int                       # uint8     |   Floor damage (percentage)
	diffuser_damage: int                    # uint8     |   Diffuser damage (percentage)
	sidepod_damage: int                     # uint8     |   Sidepod damage (percentage)
	drs_fault: int                          # uint8     |   Indicator for DRS fault, 0 = OK, 1 = fault
	ers_fault: int							# uint8     |   Indicator for ERS fault, 0 = OK, 1 = fault
	gearbox_damage: int                     # uint8     |   Gear box damage (percentage)
	engine_damage: int                      # uint8     |   Engine damage (percentage)
	engine_mguh_wear: int                   # uint8     |   Engine wear MGU-H (percentage)
	engine_es_wear: int                     # uint8     |   Engine wear ES (percentage)
	engine_ce_wear: int                     # uint8     |   Engine wear CE (percentage)
	engine_ice_wear: int                    # uint8     |   Engine wear ICE (percentage)
	engine_mguk_wear: int                   # uint8     |   Engine wear MGU-K (percentage)
	engine_tc_wear: int                     # uint8     |   Engine wear TC (percentage)
	engine_blown: int                       # uint8     |   Engine blown, 0 = OK, 1 = fault
	engine_seized: int                      # uint8     |   Engine seized, 0 = OK, 1 = fault

@dataclass # 953 bytes
class CarDamagePacket:
	header: PacketHeader                   	#           |   Header
	car_damage_list: List[CarDamage]      	# [22]      |   List of car damage data for 22 cars

	def player_data(self):
		return self.car_damage_list[self.header.player_car_index]

def unpack_car_damage(packet_header: PacketHeader, data: bytes):
    car_damage_list = []

    for unpacked_car_damage in struct.iter_unpack(_CAR_DAMAGE_FORMAT, data):
        car_damage_list.append(CarDamage(*unpacked_car_damage))

    return CarDamagePacket(packet_header, car_damage_list)