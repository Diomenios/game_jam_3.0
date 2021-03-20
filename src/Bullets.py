import arcade
import CONST

class Bullets():

    def __init__(self,start_x,start_y):
        # sprite initialisation
        self.sprite = arcade.Sprite("sprite/player/ammo-1.png", CONST.SPRITE_SCALING_BULLET)

        self.center_x = start_x
        self.center_y = start_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.sprite.angle = math.degrees(angle-90) # 90 degree add for the sprite format

        self.sprite.change_x = math.cos(angle) * CONST.BULLET_SPEED
        self.sprite.change_y = math.sin(angle) * CONST.BULLET_SPEED

    def draw():
        self.sprite.draw()
