import arcade
import CONST
import random

class Player(arcade.Sprite):
    def setup(self):
        self.center_x = CONST.SCREEN_WIDTH/2
        self.center_y = CONST.SCREEN_HEIGHT/2
        
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def update(self):
        """ Move the player """
        # Calculate speed based on the keys pressed
        self.change_x = 0
        self.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.change_y = CONST.MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.change_y = -CONST.MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.change_x = -CONST.MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.change_x = CONST.MOVEMENT_SPEED
        
        # Move player.
        # Remove these lines if physics engine is moving player.
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
            
    def update_keys(self, up_pressed, down_pressed, left_pressed, right_pressed):
        self.up_pressed = up_pressed
        self.down_pressed = down_pressed
        self.left_pressed = left_pressed
        self.right_pressed = right_pressed
        