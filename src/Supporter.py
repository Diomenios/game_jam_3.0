import arcade
import CONST
import random
import math

class Supporter():
    def __init__(self, max_health, damage, boost_speed, type, cashprize):
        # sprite inititialisation
        self.sprites =(
        arcade.Sprite("sprites/npc/all_"+type.lower()+"_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 0,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/npc/all_"+type.lower()+"_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 66,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/npc/all_"+type.lower()+"_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 122,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/npc/all_"+type.lower()+"_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 188,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/npc/all_"+type.lower()+"_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 254,image_y = 0,image_width = 66,image_height = 66)
        )
        self.sprite = self.sprites[0]

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
        self.type = type
        self.damage = damage

        self._sprite_count = 0
        self._tempo_sprite = 0

        self.boost_speed = boost_speed
        self.cashprize = cashprize


    def update(self):
        """ Move the supporter """
        x = self.sprite.center_x
        y = self.sprite.center_y


        self.change_animations()

        self.sprite.center_x = self.sprite.change_x * self.boost_speed + x
        self.sprite.center_y = self.sprite.change_y * self.boost_speed + y

    def change_animations(self):

        change_x = self.sprite.change_x
        change_y = self.sprite.change_y

        if self.hit_points > 0:
            if self._tempo_sprite == 0:
                self.sprite = self.sprites[self._sprite_count%4]
                self._sprite_count += 1
                self._tempo_sprite = CONST.TEMPO_ANIMATION
            else:
                self._tempo_sprite -= 1

            self.sprite.change_x = change_x
            self.sprite.change_y = change_y
        else:
            self.sprite = self.sprites[4]



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
                                         height=CONST.SUPPORTER_HEALTHBAR_HEIGHT,
                                         color=arcade.color.WHITE)

        # Calculate width based on health
        health_width = CONST.SUPPORTER_HEALTHBAR_WIDTH * (self.hit_points / self.max_health)

        arcade.draw_rectangle_filled(center_x=self.sprite.center_x - 0.5 * (CONST.SUPPORTER_HEALTHBAR_WIDTH - health_width),
                                     center_y=self.sprite.center_y + CONST.SUPPORTER_HEALTHBAR_OFFSET_Y,
                                     width=health_width,
                                     height=CONST.SUPPORTER_HEALTHBAR_HEIGHT,
                                     color=arcade.color.BLUE)
