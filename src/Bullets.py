import arcade
import math
import CONST

class Bullets():

    def __init__(self,start_x,start_y,dest_x,dest_y):
        # sprite initialisation
        self.sprite = arcade.Sprite("sprites/player/ammo-1.png", CONST.SPRITE_SCALING_BULLET)

        self.sprite.center_x = start_x
        self.sprite.center_y = start_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.sprite.angle = math.degrees(angle-(math.pi/2)) # 90 degree add for the sprite format

        self.sprite.change_x = math.cos(angle) * CONST.BULLET_VEL
        self.sprite.change_y = math.sin(angle) * CONST.BULLET_VEL

    def draw(self):
        self.sprite.draw()

    def update(self):
        self.sprite.update()
