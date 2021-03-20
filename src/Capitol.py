import arcade
import CONST

class Capitol(arcade.Sprite):
    def setup(self):
        self.shield = CONST.CAPITOL_SHIELD
        self.hit_point = CONST.CAPITOL_HIT_POINT

    def hit(self, damage):
        self.hit_point -= damage
