import arcade
import CONST
import random
import math

class Supporter(arcade.Sprite):
    def setup(self):
        f = random.randint(0, 3)  
        x = random.random()
        if f == 1:
            self.center_x = 0
            self.center_y = int(x * CONST.SCREEN_HEIGHT)
        elif f == 2:
            self.center_x = CONST.SCREEN_WIDTH
            self.center_y = int(x * CONST.SCREEN_HEIGHT)
        elif f == 3:
            self.center_x = int(x * CONST.SCREEN_WIDTH)
            self.center_y = 0
        else:
            self.center_x = int(x * CONST.SCREEN_WIDTH)
            self.center_y = CONST.SCREEN_HEIGHT
            
        dest_x = CONST.SCREEN_WIDTH/2
        dest_y = CONST.SCREEN_HEIGHT/2

        x_diff = dest_x - self.center_x
        y_diff = dest_y - self.center_y
        
        print(x_diff)
        print(y_diff)
        angle = math.atan2(y_diff, x_diff)
        
        self.change_x = math.cos(angle) * CONST.MOVEMENT_SPEED
        self.change_y = math.sin(angle) * CONST.MOVEMENT_SPEED
        
        print(self.change_x)
        print(self.change_y)

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