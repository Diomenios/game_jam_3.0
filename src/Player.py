import arcade
import math
from Weapon import Weapon
import CONST
from Weapon import Weapon
from Bullets import Bullets

class Player():
    def __init__(self):
        # sprite initialisation
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        self.up_pressed = 0
        self.down_pressed =  0
        self.left_pressed = 0
        self.right_pressed = 0
        self.auto_fire = 0
        self.stun = 0
        self.count = 0

        # position at begining
        self.sprite.center_x = CONST.PLAYER_X
        self.sprite.center_y = CONST.PLAYER_Y
        self.vel = CONST.PLAYER_INIT_VEL

        # weapon
        self.weapon = Weapon(1)



    def update(self):
        """ Update the player sprite """
        # Calculate speed based on the keys pressed
        self.sprite.change_x = 0
        self.sprite.change_y = 0

        if not self.stun:
            if self.up_pressed and not self.down_pressed:
                self.sprite.change_y = self.vel
            elif self.down_pressed and not self.up_pressed:
                self.sprite.change_y = -self.vel
            if self.left_pressed and not self.right_pressed:
                self.sprite.change_x = -self.vel
            elif self.right_pressed and not self.left_pressed:
                self.sprite.change_x = self.vel

            # Move player.
            # Remove these lines if physics engine is moving player.
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

    def update_keys(self, up_pressed, down_pressed, left_pressed, right_pressed):
        """ Update the Key pressed """
        self.up_pressed = up_pressed
        self.down_pressed = down_pressed
        self.left_pressed = left_pressed
        self.right_pressed = right_pressed

    def fire(self, dest_x,dest_y):
        bullet = None
        if self.auto_fire and not self.count%self.weapon.rate :
            # Create a bullet
            bullet = Bullets(self.sprite.center_x,self.sprite.center_y,dest_x,dest_y,self.weapon.ammo_dmg,self.weapon.ammo_vel,self.weapon.ammo_hit_point)

        self.count += 1
        return bullet
