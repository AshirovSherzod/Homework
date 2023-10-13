import os
from random import *
os.system("cls")

class Counter:
    def __init__(self):
        self.soul_precent = [20,50,100]
        self.count_terorist = 0
        self.count_spesnast = 0
        self.count_match = 0

        self.T_head = 100
        self.T_arm = 50
        self.T_leg = 50
        self.T_body = 20

        self.S_head = 100
        self.S_arm = 50
        self.S_leg = 50
        self.S_body = 20

class Terorist(Counter):
    def __init__(self):
        super().__init__()

