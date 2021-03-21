import arcade
import CONST

class Capitol():

    def __init__(self):
        self.sprite = arcade.Sprite("sprites/land/capitol-base.png", CONST.SPRITE_SCALING_CAPITOL)

        self.max_shield = CONST.CAPITOL_SHIELD
        self.shield = 0

        self.sprite.center_y = CONST.SCREEN_HEIGHT/2
        self.sprite.center_x = CONST.SCREEN_WIDTH/2

        self.max_hit_point = CONST.CAPITOL_HIT_POINT
        self.hit_point = CONST.CAPITOL_HIT_POINT

    def hit(self, damage):
        if self.shield != 0 :
            if self.shield <= damage :

                damage -= self.shield
                self.shield = 0
                self.switch_on_shield_view()
                self.hit_point -= damage
            else :
                self.shield -= damage
        else :
            self.hit_point -= damage

    def add_shield_points(self, shield_points):

        new_shield_points = self.shield() + shield_points
        self.shield = new_shield_points if new_shield_points <= self.max_shield else self.max_shield

    def draw(self):
        self.sprite.draw()
        self.draw_health_bar()

        if self.shield > 0 :
            self.draw_shield_bar()
            self.draw_shield_number()
        else:
            self.draw_health_number()


    def draw_health_number(self):

        """ Draw how many hit points we have """

        health_string = f"{self.hit_point}/{self.max_hit_point}"
        arcade.draw_text(health_string,
                            start_x = self.sprite.center_x + CONST.HEALTH_NUMBER_OFFSET_X,
                            start_y = self.sprite.center_y + CONST.HEALTH_NUMBER_OFFSET_Y,
                            font_size = CONST.FONT_SIZE,
                            color = arcade.color.WHITE)

    def draw_health_bar(self):
        """ Draw the health bar """

        # Draw the 'unhealthy' background
        if self.hit_point < self.max_hit_point:
            arcade.draw_rectangle_filled(center_x = self.sprite.center_x,
                                         center_y = self.sprite.center_y + CONST.HEALTHBAR_OFFSET_Y,
                                         width = CONST.HEALTHBAR_WIDTH,
                                         height = CONST.HEALTHBAR_HEIGHT,
                                         color = arcade.color.OU_CRIMSON_RED)

        # Calculate width based on health
        health_width = CONST.HEALTHBAR_WIDTH * (self.hit_point / self.max_hit_point)

        arcade.draw_rectangle_filled(center_x = self.sprite.center_x - 0.5 * (CONST.HEALTHBAR_WIDTH - health_width),
                                     center_y = self.sprite.center_y + CONST.HEALTHBAR_OFFSET_Y,
                                     width = health_width,
                                     height = CONST.HEALTHBAR_HEIGHT,
                                     color = arcade.color.PAKISTAN_GREEN)

    def draw_shield_bar(self):

        # Calculate width based on health
        shield_width = CONST.HEALTHBAR_WIDTH * (self.shield / self.max_shield)

        arcade.draw_rectangle_filled(center_x = self.sprite.center_x - 0.5 * (CONST.HEALTHBAR_WIDTH - shield_width),
                                     center_y = self.sprite.center_y + CONST.HEALTHBAR_OFFSET_Y,
                                     width = shield_width,
                                     height = CONST.HEALTHBAR_HEIGHT,
                                     color = arcade.color.SPANISH_BLUE)

    def draw_shield_number(self):

        """ Draw how many shield points we have """

        shield_string = f"shield({self.shield})"
        arcade.draw_text(shield_string,
                            start_x = self.sprite.center_x + CONST.HEALTH_NUMBER_OFFSET_X + CONST.SHIELD_BAR_OFFSET_X,
                            start_y = self.sprite.center_y + CONST.HEALTH_NUMBER_OFFSET_Y,
                            font_size = CONST.FONT_SIZE,
                            color = arcade.color.WHITE)

    def switch_on_shield_view(self):

        if self.shield > 0 :
            self.sprite = arcade.Sprite("sprites/land/capitol-shield.png", CONST.SPRITE_SCALING_CAPITOL)
            self.sprite.center_y = CONST.SCREEN_HEIGHT/2
            self.sprite.center_x = CONST.SCREEN_WIDTH/2

        else :
            self.sprite = arcade.Sprite("sprites/land/capitol-base.png", CONST.SPRITE_SCALING_CAPITOL)
            self.sprite.center_y = CONST.SCREEN_HEIGHT/2
            self.sprite.center_x = CONST.SCREEN_WIDTH/2
