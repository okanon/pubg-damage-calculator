# -*- coding: utf-8 -*-

from enum import Enum

class ARMO(Enum):
	MM5 = 5
	MM7 = 7
	MM300 = 300

class AR(Enum):
	HEAD = 2.35
	NECK = 1.76
	CLAVICLES = 1
	UPPER_CHEST = 1.1
	LOWER_CHEST = 1
	STOMACH = 0.95 
	PELVIS = 1
	UPPER_ARM = 0.54
	FORE_ARM = 0.45
	WRIST = 0.27
	THIGH = 0.54
	CALF = 0.45
	ANKLE = 0.27

	@classmethod
	def dist(self, r, armo):
		return 1 if not 80 < r else 1 - ((r - 80) * 0.0005958) if not 500 < r else 1 - (420 * 0.0005958)

class DMR(Enum):
	HEAD = 2.35
	NECK = 1.76
	CLAVICLES = 1.05
	UPPER_CHEST = 1.15
	LOWER_CHEST = 1.05
	STOMACH =  0.996
	PELVIS = 1.05
	UPPER_ARM = 0.57
	FORE_ARM = 0.47
	WRIST = 0.28
	THIGH = 0.57
	CALF = 0.47
	ANKLE = 0.28

	@classmethod
	def dist(self, r, armo):
		if armo == ARMO.MM7:
			return 1 if not 120 < r else 1 - ((r - 120) * 0.0003948) if not 500 < r else 1 - (380 * 0.0003948)
		else:
			return 1 if not 120 < r else 1 - ((r - 120) * 0.0006079) if not 400 < r else 1 - (280 * 0.0006079)

class SR(Enum):
	HEAD = 2.5
	NECK = 1.87
	CLAVICLES = 1.3
	UPPER_CHEST = 1.43
	LOWER_CHEST = 1.3
	STOMACH = 1.23
	PELVIS = 1.1
	UPPER_ARM = 0.57
	FORE_ARM = 0.47
	WRIST = 0.28
	THIGH = 0.57
	CALF = 0.47
	ANKLE = 0.28

	@classmethod
	def dist(self, r, armo):
		return 1 if not 50 < r else 1 - ((r - 50) * 0.001) if not 300 < r else 1 - (250 * 0.001)

class SMG(Enum):
	HEAD = 1.8
	NECK = 1.35
	CLAVICLES = 1
	UPPER_CHEST = 1.1
	LOWER_CHEST = 1
	STOMACH = 0.95
	PELVIS = 1
	UPPER_ARM = 0.75
	FORE_ARM = 0.62
	WRIST = 0.37
	THIGH = 0.75
	CALF = 0.62
	ANKLE = 0.37

	@classmethod
	def dist(self, r, armo):
		return 1 if not 50 < r else 1 - ((r - 50) * 0.001) if not 300 < r else 1 - (250 * 0.001)

class SG(Enum):
	HEAD = 1.45
	NECK = 1.08
	CLAVICLES = 0.96
	UPPER_CHEST = 1.06
	LOWER_CHEST = 0.96
	STOMACH = 0.92
	PELVIS = 0.96
	UPPER_ARM = 0.52
	FORE_ARM = 0.43
	WRIST = 0.26
	THIGH = 0.52
	CALF = 0.43
	ANKLE = 0.26

	@classmethod
	def dist(self, r, armo):
		return 1 if not 50 < r else 1 - ((r - 50) * 0.001) if not 300 < r else 1 - (250 * 0.001)

class LMG(Enum):
	HEAD = 2.3
	NECK = 1.72
	CLAVICLES = 1
	UPPER_CHEST = 1.1
	LOWER_CHEST = 1
	STOMACH = 0.95
	PELVIS = 1
	UPPER_ARM = 0.54
	FORE_ARM = 0.45
	WRIST = 0.27
	THIGH = 0.54
	CALF = 0.45
	ANKLE = 0.27

	@classmethod
	def dist(self, r, armo):
		return 1 if not 50 < r else 1 - ((r - 50) * 0.001) if not 300 < r else 1 - (250 * 0.001)

class PISTOL(Enum):
	HEAD = 1.98
	NECK = 1.49
	CLAVICLES = 0.99
	UPPER_CHEST = 1.09
	LOWER_CHEST = 0.99
	STOMACH = 0.94
	PELVIS = 0.99
	UPPER_ARM = 0.59
	FORE_ARM = 0.5
	WRIST = 0.27
	THIGH = 0.59
	CALF = 0.5
	ANKLE = 0.27

	@classmethod
	def dist(self, r, armo):
		return 1 if not 50 < r else 1 - ((r - 50) * 0.001) if not 300 < r else 1 - (250 * 0.001)

class PUNCH(Enum):
	HEAD = 1.5
	NECK = 1.12
	CLAVICLES = 1
	UPPER_CHEST = 1.1
	LOWER_CHEST = 1
	STOMACH = 0.94
	PELVIS = 1
	UPPER_ARM = 0.72
	FORE_ARM = 0.59
	WRIST = 0.36
	THIGH = 0.72
	CALF = 0.59
	ANKLE = 0.36

	@classmethod
	def dist(self, r, armo):
		return 1

class MELEE(Enum):
	HEAD = 1.5
	NECK = 1.125
	CLAVICLES = 1
	UPPER_CHEST = 1.1
	LOWER_CHEST = 1
	STOMACH = 0.95
	PELVIS = 1
	UPPER_ARM = 0.72
	FORE_ARM = 0.6
	WRIST = 0.36
	THIGH = 0.72
	CALF = 0.6
	ANKLE = 0.36

	@classmethod
	def dist(self, r, armo):
		return 1

class CROSS_BOW(Enum):
	HEAD = 2.3
	NECK = 1.71
	CLAVICLES = 0.997
	UPPER_CHEST = 1.1
	LOWER_CHEST = 0.997
	STOMACH = 0.95
	PELVIS = 0.997
	UPPER_ARM = 0.6
	FORE_ARM = 0.5
	WRIST = 0.3
	THIGH = 0.6
	CALF = 0.5
	ANKLE = 0.3

	@classmethod
	def dist(self, r, armo):
		return 1 if r == 1 else 1 - (r * 0.0002)

class ARMOR(Enum):
	LV0 = 1
	LV1 = 0.7 
	LV2 = 0.6
	LV3 = 0.45

