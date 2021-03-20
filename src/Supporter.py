import arcade
import CONST
import random
import math

class Supporter():
    def __init__(self):
        # sprite inititialisation
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)

        # position at begining
        side = random.randint(0, 3)
        x = random.random()
        if side == 1:
            self.sprite.center_x = 0
            self.sprite.center_y = int(x * CONST.SCREEN_HEIGHT)
        elif side == 2:
            self.sprite.center_x = CONST.SCREEN_WIDTH
            self.sprite.center_y = int(x * CONST.SCREEN_HEIGHT)
        elif side == 3:
            self.sprite.center_x = int(x * CONST.SCREEN_WIDTH)
            self.sprite.center_y = 0
        else:
            self.sprite.center_x = int(x * CONST.SCREEN_WIDTH)
            self.sprite.center_y = CONST.SCREEN_HEIGHT

        dest_x = CONST.SCREEN_WIDTH/2
        dest_y = CONST.SCREEN_HEIGHT/2

        x_diff = dest_x - self.sprite.center_x
        y_diff = dest_y - self.sprite.center_y

        angle = math.atan2(y_diff, x_diff)

        self.sprite.change_x = math.cos(angle) * CONST.SUPPORTER_INIT_VEL
        self.sprite.change_y = math.sin(angle) * CONST.SUPPORTER_INIT_VEL


    def update(self):
        """ Move the supporter """
        self.sprite.center_x += self.sprite.change_x
        self.sprite.center_y += self.sprite.change_y

        # Check for out-of-bounds
        if self.sprite.left < 0:
            self.sprite.left = 0
        elif self.sprite.right > CONST.SCREEN_WIDTH - 1:
            self.sprite.right = CONST.SCREEN_WIDTH - 1

        if self.sprite.bottom < 0:
            self.sprite.bottom = 0
        elif self.sprite.top > CONST.SCREEN_HEIGHT - 1:
            self.sprite.top = CONST.SCREEN_HEIGHT - 1

    def draw(self):
        self.sprite.draw()
