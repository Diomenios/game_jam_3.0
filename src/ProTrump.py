import CONST
from Supporter import Supporter

class ProTrump(Supporter):
    def __init__(self, boost_speed):
        super().__init__(CONST.PROTRUMP_MAX_HEALTH, CONST.PROTRUMP_DAMAGE, boost_speed, "ProTrump", CONST.PROTRUMP_SPEED, CONST.PROTRUMP_CASHPRIZE)
