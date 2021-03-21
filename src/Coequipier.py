import arcade
import CONST
import math
from Weapon import Weapon
from Bullets import Bullets
import time

class Coequipier():
    def __init__(self):
        # sprite inititialisation
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        self.count = 0

        self.sprite.center_x = CONST.SCREEN_WIDTH // 2
        self.sprite.center_y = CONST.SCREEN_HEIGHT // 2

        self.sound = arcade.Sound("audios/gun-1-bis.mp3")

        # weapon
        self.weapon = Weapon()
        self.range = CONST.SUPPORT_RANGE

    def fire(self, dest_x,dest_y):
        bullet = None
        if not self.count%self.weapon.rate :
            # Create a bullet
            bullet = Bullets(self.sprite.center_x,self.sprite.center_y,dest_x,dest_y,self.weapon.ammo_dmg,self.weapon.ammo_vel,self.weapon.ammo_hit_point, "Coequipier")
            self.sound.play(CONST.MUSIC_VOLUME*0.5)
            time.sleep(0.03)
        self.count += 1

        return bullet
