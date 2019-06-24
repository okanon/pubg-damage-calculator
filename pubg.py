# -*- coding: utf-8 -*-

from decimal import Decimal as deci
from decimal import ROUND_HALF_DOWN, ROUND_CEILING

from ratio import ARMOR
from weapon import Weapon


class PUBG(object):
	
	head = ["HEAD","NECK"]
	no_armor = ["UPPER_ARM","FORE_ARM","WRIST","THIGH","CALF","ANKLE"]

	def __init__(self, weap, h=0, v=0):
		for name, member in Weapon.__members__.items():
			if weap.replace("-", "").upper() in name:
				self.target = member
				self.target_name = name
				break
			continue
		
		self.helmet = self.__pos(h)
		self.vest = self.__pos(v)

	def __pos(self, val):
		return "lv{0}".format(val)

	def __distance(self, _range=1):
		_range = 1 if _range == 0 else _range
		return list(self.target.value.keys())[0].dist(_range, sorted(self.target.value.values())[0])

	def __tokill(self, dmg):
		return deci(str(100 / dmg)).quantize(deci("0"), rounding=ROUND_CEILING)
		
	def calc(self, d=1):
		d = round(d)
		
		out = "--- {0} damage ---\nHELMET: {1}, VEST: {2}, RANGE: {3}m\n".format(self.target_name.replace("-", " "), self.helmet.capitalize(), self.vest.capitalize(), d)
		for name, member in list(self.target.value.keys())[0].__members__.items():
			
			if name in self.no_armor:
				damage = list(self.target.value.values())[0] * self.__distance(d) * member.value;
			else:
				if name in self.head:
					damage = list(self.target.value.values())[0] * self.__distance(d) * member.value * ARMOR[self.helmet.upper()].value;
				else:
					damage = list(self.target.value.values())[0] * self.__distance(d) * member.value * ARMOR[self.vest.upper()].value;

			damage = deci(str(damage)).quantize(deci("0.1"), rounding=ROUND_HALF_DOWN)
			out += "\n{0}: {1}({2})".format(name, damage, self.__tokill(damage))

		print(out)

