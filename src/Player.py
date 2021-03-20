import arcade
import math
from Weapon import Weapon
import CONST
from Weapon import Weapon
from Bullets import Bullets

class Player():
    def __init__(self):
        # sprite initialisation
        self.sprites =(
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 0,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 66,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 122,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 188,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 254,image_y = 0,image_width = 66,image_height = 66),
        arcade.Sprite("sprites/player/all_player_mv.png", scale = CONST.SPRITE_SCALING_PLAYER,image_x = 375,image_y = 0,image_width = 66,image_height = 66),
        )
        self.sprite = self.sprites[0]

        self.up_pressed = 0
        self.down_pressed =  0
        self.left_pressed = 0
        self.right_pressed = 0
        self.auto_fire = 0
        self.stun = 0
        self.count = 0

        self._sprite_count = 0
        self._tempo_sprite = 0

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
        x = self.sprite.center_x
        y = self.sprite.center_y

        if not self.stun:
            change_y = 0
            change_x = 0
            if self.up_pressed and not self.down_pressed:
                change_y = self.vel
            elif self.down_pressed and not self.up_pressed:
                change_y = -self.vel
            if self.left_pressed and not self.right_pressed:
                change_x = -self.vel
            elif self.right_pressed and not self.left_pressed:
                change_x = self.vel

            # change sprite
            if not change_x == 0 or not change_y == 0 :
                if self._tempo_sprite == 0 :
                    self.sprite = self.sprites[self._sprite_count%4]
                    self._sprite_count += 1
                    self._tempo_sprite = CONST.TEMPO_ANNIMATION
                else:
                    self._tempo_sprite += -1
            else:
                if self.auto_fire:
                    self.sprite = self.sprites[5]
                else:
                    self.sprite = self.sprites[0]
                self._tempo_sprite = 0
                self._sprite_count = 0


            # Move player.
            # Remove these lines if physics engine is moving player.
            self.sprite.change_x = change_x
            self.sprite.change_y = change_y
            self.sprite.center_x = x + self.sprite.change_x
            self.sprite.center_y = y + self.sprite.change_y

            # Check for out-of-bounds
            if self.sprite.left < 0:
                self.sprite.left = 0
            elif self.sprite.right > CONST.SCREEN_WIDTH - 1:
                self.sprite.right = CONST.SCREEN_WIDTH - 1

            if self.sprite.bottom < 0:
                self.sprite.bottom = 0
            elif self.sprite.top > CONST.SCREEN_HEIGHT - 1:
                self.sprite.top = CONST.SCREEN_HEIGHT - 1
        else:
            self.sprite = self.sprites[4]
            self.sprite.center_x = x
            self.sprite.center_y = y

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
        if self.auto_fire:
            if not self.count%self.weapon.rate :
                # Create a bullet
                bullet = Bullets(self.sprite.center_x,self.sprite.center_y,dest_x,dest_y,self.weapon.ammo_dmg,self.weapon.ammo_vel,self.weapon.ammo_hit_point)
            self.count += 1
        else:
            self.count = 0

        return bullet
