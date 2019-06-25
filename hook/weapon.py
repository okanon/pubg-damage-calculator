
from enum import Enum
from .ratio import *

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
   MK14 = {DMR: 61, ARMO: 7}
   SLR = {DMR: 58, ARMO: 7}
   SKS = {DMR: 53, ARMO: 7}
   QBU = {DMR: 48, ARMO: 5}
   MINI14 = {DMR: 46, ARMO: 5}
   VSS = {DMR: 41, ARMO: 9}
   AWM = {SR: 105, ARMO: 300}
   M24 = {SR: 79, ARMO: 7}
   KAR98K = {SR: 75, ARMO: 7}
   WIN94 = {SR: 66, ARMO: 45}
   DP28 = {LMG: 51, ARMO: 7}
   M249 = {LMG: 45, ARMO: 5}
   CROSSBOW = {CROSS_BOW: 105, ARMO: 1}
   TOMMYGUN = {SMG: 40, ARMO: 45}
   UMP45 = {SMG: 39, ARMO: 45}
   PP19_BIZON = {SMG: 35, ARMO: 9}
   MP5K = {SMG: 33, ARMO: 9}
   VECTOR = {SMG: 31, ARMO: 9}
   MICRO_UZI = {SMG: 26, ARMO: 9}
   S1897 = {SG: 24, ARMO: 12}
   S686 = {SG: 24, ARMO: 12}
   S12K = {SG: 22, ARMO: 12}
   SAWEDOFF = {SG: 20, ARMO: 12}
   DEAGLE = {PISTOL: 62, ARMO: 7}
   R1895 = {PISTOL: 55, ARMO: 7}
   R45 = {PISTOL: 55, ARMO: 7} #real armo is .45acp
   P1911 = {PISTOL: 41, ARMO: 45}
   P92 = {PISTOL: 35, ARMO: 9}
   P18C = {PISTOL: 23, ARMO: 9}
   SKORPION = {PISTOL: 22, ARMO: 9}
   PAN = {MELEE: 80, ARMO: 0}
   CROWBAR = {MELEE: 60, ARMO: 0}
   MACHETE = {MELEE: 60, ARMO: 0}
   SICKLE = {MELEE: 60, ARMO: 0}
   PUNCH_ = {PUNCH: 18, ARMO: 0}
   JUMPING_PUNCH = {PUNCH: 38, ARMO: 0}

