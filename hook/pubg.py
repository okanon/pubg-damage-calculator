# -*- coding: utf-8 -*-

from decimal import Decimal as deci
from decimal import ROUND_HALF_DOWN, ROUND_CEILING

from .ratio import ARMOR
from .weapon import Weapon

import sys


class PUBG(object):
	
	#flag = True
	
	__na = "N/A"
	__head = ["HEAD","NECK"]
	__no_armor = ["UPPER_ARM","FORE_ARM","WRIST","THIGH","CALF","ANKLE"]

	def __init__(self, weap, h=0, v=0):
		for name, member in Weapon.__members__.items():
			if weap.replace("-", "").upper() in name:
				self.target = member
				self.target_name = name.replace("_", "") if name[-1:] == "_" else name.replace("_", " ")
				break
			continue
		
		self.helmet = self.__pos(h)
		self.vest = self.__pos(v)

	"""
	def __call__(self):
		if self.flag:
			self.flag = False
	"""

	"""This is feature .."""
	def deco_PUBG(flag):
		def _deco_PUBG(func):
			def wrap(*args, **kwargs):
				if not flag:
					print("")
			return wrap
	
	def __pos(self, val):
		return "lv{0}".format(val)

	def __distance(self, _range=1):
		_range = 1 if _range == 0 else _range
		return list(self.target.value.keys())[0].dist(_range, self.target)

	def __tokill(self, dmg):
		if type(dmg) is str:
			return self.__na
		return deci(str(100 / dmg)).quantize(deci("0"), rounding=ROUND_CEILING)
		
	#@deco_PUBG(flag)
	def calc(self, d=1):
		d = round(d)
		
		try:
			out = "--- {0} damage ---\nHELMET: {1}, VEST: {2}, RANGE: {3}m\n".format(
				self.target_name.replace("-", " "), 
				self.helmet.capitalize() if not int(self.helmet[-1:]) == 0 else self.__na,
				self.vest.capitalize() if not int(self.helmet[-1:]) == 0 else self.__na, d
			)
		except AttributeError:
			print("Weapon is not found.")
			sys.exit(-1)

		d = self.__distance(d)
		for name, member in list(self.target.value.keys())[0].__members__.items():
			try:
				if name in self.__no_armor:
					damage = list(self.target.value.values())[0] * d * member.value;
				else:
					if name in self.__head:
						damage = list(self.target.value.values())[0] * d * member.value * ARMOR[self.helmet.upper()].value;
					else:
						damage = list(self.target.value.values())[0] * d * member.value * ARMOR[self.vest.upper()].value;

				if damage < 0.05:
					damage = self.__na
				else:
					damage = deci(str(damage)).quantize(deci("0.1"), rounding=ROUND_HALF_DOWN)
				out += "\n{0}: {1}({2})".format(name, damage, self.__tokill(damage))
			except KeyError:
				print("Armor level is injustice.")
				sys.exit(-1)

		print(out)

