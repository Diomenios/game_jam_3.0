import CONST
from Supporter import Supporter

class Boss(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.BOSS_MAX_HEALTH, CONST.BOSS_DAMAGE, boost_speed, "Boss", CONST.BOSS_SPEED, CONST.BOSS_CASHPRIZE)
