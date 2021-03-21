import CONST
import math
from Supporter import Supporter

class Redneck(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.REDNECK_MAX_HEALTH, CONST.REDNECK_DAMAGE, boost_speed, "Redneck", CONST.REDNECK_SPEED, CONST.REDNECK_CASHPRIZE)
        self.boost_speed = boost_speed
        self.is_on_player = False

    def update(self, player_x, player_y):
        """ Move the redneck """
        x_diff = player_x - self.sprite.center_x
        y_diff = player_y - self.sprite.center_y

        angle = math.atan2(y_diff, x_diff)

        self.sprite.change_x = math.cos(angle) * self.speed * self.boost_speed
        self.sprite.change_y = math.sin(angle) * self.speed * self.boost_speed


        x = self.sprite.center_x
        y = self.sprite.center_y

        self.change_animations()

        if player_x > self.sprite.center_x:
            self.sprite.center_x = self.sprite.change_x + x
        elif player_x < self.sprite.center_x:
            self.sprite.center_x = self.sprite.change_x + x

        if player_y > self.sprite.center_y:
            self.sprite.center_y = self.sprite.change_y + y
        elif player_y < self.sprite.center_y:
            self.sprite.center_y = self.sprite.change_y + y

    def change_animations(self):

        change_x = self.sprite.change_x
        change_y = self.sprite.change_y

        if self.hit_points > 0:
            if self.is_on_player:
                self.sprite = self.sprites[0]
            elif self._tempo_sprite == 0:
                self.sprite = self.sprites[self._sprite_count%4]
                self._sprite_count += 1
                self._tempo_sprite = CONST.TEMPO_ANIMATION
            else:
                self._tempo_sprite -= 1

            self.sprite.change_x = change_x
            self.sprite.change_y = change_y
        else:
            self.sprite = self.sprites[4]
