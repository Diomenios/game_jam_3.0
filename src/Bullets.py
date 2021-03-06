import arcade
import math
import CONST

class Bullets():

    def __init__(self,start_x,start_y,dest_x,dest_y,dmg,vel,hp, sender):
        # sprite initialisation
        if dmg == 1:
            path = "sprites/player/ammo-1.png"
        elif dmg == 2:
            path = "sprites/player/ammo-2.png"
        else:
            path = "sprites/player/ammo-3.png"
        self.sprite = arcade.Sprite(path, CONST.SPRITE_SCALING_BULLET)

        self.sprite.center_x = start_x
        self.sprite.center_y = start_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.sprite.angle = math.degrees(angle-(math.pi/2)) # 90 degree add for the sprite format

        self.sprite.change_x = math.cos(angle) * vel
        self.sprite.change_y = math.sin(angle) * vel

        # bullet variable
        self.damage = dmg
        self.hit_points = hp
        self.last_touch = None
        self.sender = sender

    def draw(self):
        self.sprite.draw()

    def update(self):
        self.sprite.update()
