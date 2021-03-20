import CONST
from Supporter import Supporter

class Redneck(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.REDNECK_MAX_HEALTH, CONST.REDNECK_DAMAGE, boost_speed, "Redneck")
