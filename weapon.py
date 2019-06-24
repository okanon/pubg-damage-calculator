# -*- coding: utf-8 -*-

from enum import Enum
from ratio import *

class Weapon(Enum):
	AKM = {AR: 49, ARMO: 7}
	GROZA = {AR: 49, ARMO: 7}
	MK47_MUTANT = {AR: 49, ARMO: 7}
	BERYL_M762 = {AR: 47, ARMO: 7}
	AUG_A3 = {AR: 43, ARMO: 5}
	G36C = {AR: 43, ARMO: 5}
	M16A4 = {AR: 43, ARMO: 5}
	M416 = {AR: 43, ARMO: 5}
	SCARL = {AR: 43, ARMO: 5}
	DP28 = {LMG: 51, ARMO: 7}
	M249 = {LMG: 45, ARMO: 5}
	MK14 = {DMR: 61, ARMO: 7}
	SLR = {DMR: 58, ARMO: 7}
	SKS = {DMR: 53, ARMO: 7}
	QBU = {DMR: 48, ARMO: 5}
	MINI14 = {DMR: 46, ARMO: 5}
	VSS = {SR: 41, ARMO: None}
	AWM = {SR: 105, ARMO: None}
	M24 = {SR: 79, ARMO: None}
	KAR98K = {SR: 75, ARMO: None}
	WIN94 = {SR: 66, ARMO: None}
	CROSSBOW = {CROSS_BOW: 105, ARMO: None}
	TOMMYGUN = {SMG: 40, ARMO: None}
	UMP45 = {SMG: 39, ARMO: None}
	PP19_BIZON = {SMG: 35, ARMO: None}
	MP5K = {SMG: 33, ARMO: None}
	VECTOR = {SMG: 31, ARMO: None}
	MICRO_UZI = {SMG: 26, ARMO: None}
	S1897 = {SG: 24, ARMO: None}
	S686 = {SG: 24, ARMO: None}
	S12K = {SG: 22, ARMO: None}
	SAWEDOFF = {SG: 20, ARMO: None}
	DEAGLE = {PISTOL: 62, ARMO: None}
	R1895 = {PISTOL: 55, ARMO: None}
	R45 = {PISTOL: 55, ARMO: None}
	P1911 = {PISTOL: 41, ARMO: None}
	P92 = {PISTOL: 35, ARMO: None}
	P18C = {PISTOL: 23, ARMO: None}
	SKORPION = {PISTOL: 22, ARMO: None}
	PAN = {MELEE: 80, ARMO: None}
	CROWBAR = {MELEE: 60, ARMO: None}
	MACHETE = {MELEE: 60, ARMO: None}
	SICKLE = {MELEE: 60, ARMO: None}
	JUMPING_PUNCH = {PUNCH: 38, ARMO: None}
	PUNCH_ = {PUNCH: 18, ARMO: None}

