import arcade
import CONST
import math
from Weapon import Weapon

class Coequipier():
    def __init__(self):
        # sprite inititialisation
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        self.count = 0

        self.sprite.center_x = CONST.SCREEN_WIDTH // 2
        self.sprite.center_y = CONST.SCREEN_HEIGHT // 2

        # weapon
        self.weapon = Weapon(1)

    def fire(self, dest_x,dest_y):
        bullet = None
        if self.count%self.weapon.rate :
            # Create a bullet
            bullet = arcade.Sprite("sprites/player/ammo-1.png", CONST.SPRITE_SCALING_LASER)

            # Position the bullet at the player's current location
            start_x = self.sprite.center_x
            start_y = self.sprite.center_y
            bullet.center_x = start_x
            bullet.center_y = start_y


            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Angle the bullet sprite so it doesn't look like it is flying
            # sideways.
            bullet.angle = math.degrees(angle)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the bullet travels.
            bullet.change_x = math.cos(angle) * CONST.BULLET_VEL
            bullet.change_y = math.sin(angle) * CONST.BULLET_VEL
        return bullet
