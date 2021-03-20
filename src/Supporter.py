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

        x_diff = dest_x - self.center_x
        y_diff = dest_y - self.center_y

        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * CONST.MOVEMENT_SPEED
        self.change_y = math.sin(angle) * CONST.MOVEMENT_SPEED

    def update(self):
        """ Move the supporter """
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > CONST.SCREEN_WIDTH - 1:
            self.right = CONST.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > CONST.SCREEN_HEIGHT - 1:
            self.top = CONST.SCREEN_HEIGHT - 1

    def draw(self):
        self.sprite.draw()
