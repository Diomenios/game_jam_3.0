import arcade
import CONST

class Weapon():
    def __init__(self):
        self.rate = 20
        self.ammo_vel = CONST.BULLET_INIT_VEL
        self.ammo_dmg = 1
        self.ammo_hit_point = 1
        self.nb_bullet = 1
