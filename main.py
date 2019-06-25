# -*- coding: utf-8 -*-

from hook.pubg import PUBG

cc = PUBG("M24", 0, 0) #helmet NO_HELMET, vest NO_VEST

cc.calc(1) #range 1m
cc.calc(150) #range 150m
cc.calc(500) #range 500m
