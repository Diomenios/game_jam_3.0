import arcade
import CONST

class Capitol():
    def __init__(self):
        self.sprite = arcade.Sprite("sprites/land/capitol-base.png", CONST.SPRITE_SCALING_CAPITOL)
        self.shield = CONST.CAPITOL_SHIELD
        self.hit_point = CONST.CAPITOL_HIT_POINT

    def hit(self, damage):
        self.hit_point -= damage
