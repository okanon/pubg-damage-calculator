
from enum import Enum

class ARMO(Enum):
   MM5 = 5
   MM7 = 7
   MM9 = 9
   GA12 = 12
   ACP45 = 45
   M300 = 300
   BOLT = 1

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
   def dist(self, r, target):
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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.MM7.value:
         return 1 if not 120 < r else 1 - ((r - 120) * 0.0003948) if not 500 < r else 1 - (380 * 0.0003948)
      elif list(target.value.values())[1] == ARMO.MM5.value:
         return 1 if not 120 < r else 1 - ((r - 120) * 0.0006079) if not 400 < r else 1 - (280 * 0.0006079)
      elif list(target.value.values())[1] == ARMO.MM9.value:
         return 1 #drop-off damage is not defined

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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.MM7.value:
         return 1 if not 100 < r else 1 - ((r - 100) * 0.0002046) if not 590 < r else 1 - (490 * 0.0002046)
      elif list(target.value.values())[1] == ARMO.M300.value:
         return 1 if not 150 < r else 1 - ((r - 150) * 0.0001822) if not 700 < r else 1 - (550 * 0.0001822) 
      elif list(target.value.values())[1] == ARMO.ACP45.value:
         return 1 if not 100 < r else 1 - ((r - 100) * 0.0001797) if not 500 < r else 1 - (400 * 0.0001797)

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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.ACP45.value:
         return 1 if not 80 < r else 1 - ((r - 80) * 0.0001765) if not 250 < r else 1 - (170 * 0.0001765)
      elif list(target.value.values())[1] == ARMO.MM9.value:
         return 1 if not 50 < r else 1 - ((r - 50) * 0.002) if not 200 < r else 1 - (150 * 0.002)

class SG(Enum):
   HEAD = 1.496
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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.GA12.value:
         return 1 if not 2 < r else 1 - ((r - 1) * 0.003345) if not 300 < r else 0

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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.MM7.value:
         return 1 if not 60 < r else 1 - ((r - 60) * 0.0010443) if not 300 < r else 1 - (240 * 0.0010443)
      elif list(target.value.values())[1] == ARMO.MM5.value:
         return 1 if not 70 < r else 1 - ((r - 70) * 0.0006225) if not 390 < r else 1 - (320 * 0.0006225)

class PISTOL(Enum):
   HEAD = 1.998
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
   def dist(self, r, target):
      if list(target.value.values())[1] == ARMO.MM7.value: #deagle, r1895, r45
         return 1 if not 2 < r else 1 - ((r - 1) * 0.0003498) if not 1000 < r else 0

      if list(target.value.values())[1] == ARMO.MM9.value:
         if list(target.value.values())[0] == 22:
            return 1 if not 2 < r else 1 - ((r - 1) * 0.00201342) if not 149 < r else 1 - (149 * 0.00201342)
         elif list(target.value.values())[0] == 23:
            return 1 if not 2 < r else 1 - ((r - 1) * 0.0022779) if not 439 < r else 0
         return 1 if not 2 < r else 1 - ((r - 1) * 0.00120627) if not 829 < r else 0

      if list(target.value.values())[1] == ARMO.ACP45.value: #p1911
         return 1 if not 2 < r else 1 - ((r - 1) * 0.0009008) if not 1000 < r else 0

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
   def dist(self, r, target):
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
   def dist(self, r, target):
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
   def dist(self, r, target):
      return 1 if r == 1 else 1 - (r * 0.00020028) if not 1000 < r else 0

class ARMOR(Enum):
   LV0 = 1
   LV1 = 0.7 
   LV2 = 0.6
   LV3 = 0.45

