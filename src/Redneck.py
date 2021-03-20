import CONST
from Supporter import Supporter

class Redneck(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.REDNECK_MAX_HEALTH, CONST.REDNECK_DAMAGE, boost_speed, "Redneck")
        self.boost_speed = boost_speed

    def update(self, player_x, player_y):
        """ Move the redneck """
        if player_x > self.sprite.center_x:
            self.sprite.center_x += CONST.SUPPORTER_INIT_VEL * self.boost_speed
        elif player_x < self.sprite.center_x:
            self.sprite.center_x -= CONST.SUPPORTER_INIT_VEL * self.boost_speed

        if player_y > self.sprite.center_y:
            self.sprite.center_y += CONST.SUPPORTER_INIT_VEL * self.boost_speed
        elif player_y < self.sprite.center_y:
            self.sprite.center_y -= CONST.SUPPORTER_INIT_VEL * self.boost_speed
