import arcade
import CONST

class Capitol():

    def __init__(self):
        self.sprite = arcade.Sprite("sprites/land/capitol-base.png", CONST.SPRITE_SCALING_CAPITOL)

        self.max_shield = CONST.CAPITOL_SHIELD    
        self.shield = CONST.CAPITOL_SHIELD

        self.sprite.center_y = CONST.SCREEN_HEIGHT/2
        self.sprite.center_x = CONST.SCREEN_WIDTH/2

        self.max_hit_point = CONST.CAPITOL_HIT_POINT
        self.hit_point = CONST.CAPITOL_HIT_POINT-10

    def hit(self, damage):
        if self.shield != 0 :
            if self.shield < damage :
                
                self.shield = 0
                damage -= self.shield
            else :

                self.shield -= damage

        self.hit_point -= damage

    def draw(self):
        self.sprite.draw()
        self.draw_health_bar()
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
                                         color = arcade.color.RED)

        # Calculate width based on health
        health_width = CONST.HEALTHBAR_WIDTH * (self.hit_point / self.max_hit_point)

        arcade.draw_rectangle_filled(center_x = self.sprite.center_x - 0.5 * (CONST.HEALTHBAR_WIDTH - health_width),
                                     center_y = self.sprite.center_y + CONST.HEALTHBAR_OFFSET_Y,
                                     width = health_width,
                                     height = CONST.HEALTHBAR_HEIGHT,
                                     color = arcade.color.BLUE)