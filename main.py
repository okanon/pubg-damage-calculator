# -*- coding: utf-8 -*-

from hook.pubg import PUBG

cc = PUBG("vss", 0, 0) #helmet NO_HELMET, vest NO_VEST

print(cc.target)

cc.calc(1) #range 1m
cc.calc(150) #range 150m
cc.calc(430)
cc.calc(500) #range 500m
cc.calc(820)
cc.calc(1000) #range 1000m
