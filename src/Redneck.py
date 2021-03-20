import CONST
import math
from Supporter import Supporter

class Redneck(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.REDNECK_MAX_HEALTH, CONST.REDNECK_DAMAGE, boost_speed, "Redneck")
        self.boost_speed = boost_speed

    def update(self, player_x, player_y):
        """ Move the redneck """
        x_diff = player_x - self.sprite.center_x
        y_diff = player_y - self.sprite.center_y

        angle = math.atan2(y_diff, x_diff)

        change_x = math.cos(angle) * CONST.SUPPORTER_INIT_VEL * self.boost_speed
        change_y = math.sin(angle) * CONST.SUPPORTER_INIT_VEL * self.boost_speed

        if player_x > self.sprite.center_x:
            self.sprite.center_x += change_x
        elif player_x < self.sprite.center_x:
            self.sprite.center_x += change_x

        if player_y > self.sprite.center_y:
            self.sprite.center_y += change_y
        elif player_y < self.sprite.center_y:
            self.sprite.center_y += change_y
