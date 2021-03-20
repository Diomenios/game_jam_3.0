import arcade
import CONST

class Weapon():
    def __init__(self,l):
        self.rate = 10
        self.ammo_vel = 0
        self.ammo_dmg = 0
        self.ammo_hit_point = 0
        self.nb_bullet = 1
