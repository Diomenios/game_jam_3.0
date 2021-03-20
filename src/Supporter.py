import arcade
import CONST
import random
import math

class Supporter():
    def __init__(self, max_health):
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

        self.max_health = max_health
        self.hit_points = max_health


    def update(self):
        """ Move the supporter """
        self.sprite.center_x += self.sprite.change_x
        self.sprite.center_y += self.sprite.change_y

    def draw(self):
        self.sprite.draw()
        self.draw_health_bar()

    def draw_health_bar(self):
        """ Draw the health bar """
        # Draw the 'unhealthy' background
        if self.hit_points < self.max_health:
            arcade.draw_rectangle_filled(center_x=self.sprite.center_x,
                                         center_y=self.sprite.center_y + CONST.SUPPORTER_HEALTHBAR_OFFSET_Y,
                                         width=CONST.SUPPORTER_HEALTHBAR_WIDTH,
                                         height=3,
                                         color=arcade.color.WHITE)

        # Calculate width based on health
        health_width = CONST.SUPPORTER_HEALTHBAR_WIDTH * (self.hit_points / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.sprite.center_x - 0.5 * (CONST.SUPPORTER_HEALTHBAR_WIDTH - health_width),
                                     center_y=self.sprite.center_y - 10,
                                     width=health_width,
                                     height=CONST.SUPPORTER_HEALTHBAR_HEIGHT,
                                     color=arcade.color.BLUE)
