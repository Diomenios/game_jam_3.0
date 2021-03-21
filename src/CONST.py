# --- Constants ---
TEMPO_ANIMATION = 10
SPRITE_SCALING_COIN = .15
SPRITE_SCALING_CAPITOL = 2
MAX_VOTES = 538
MUSIC_VOLUME = 0.25

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Redneck Rumble"


# player Constants
SPRITE_SCALING_PLAYER = 0.8
PLAYER_X = SCREEN_WIDTH /4
PLAYER_Y = SCREEN_HEIGHT/4
PLAYER_INIT_VEL = 2

# bullet Constants
SPRITE_SCALING_BULLET = 0.8
BULLET_INIT_VEL = 10

# capitol Constants
CAPITOL_SHIELD = 200
CAPITOL_HIT_POINT = 100

# Supporter Constants
SPRITE_SCALING_SUPPORTER = .25
SUPPORTER_HEALTHBAR_WIDTH = 25
SUPPORTER_HEALTHBAR_HEIGHT = 3
SUPPORTER_HEALTHBAR_OFFSET_Y = 12
PROTRUMP_MAX_HEALTH = 10
REDNECK_MAX_HEALTH = 15
REDNECK_PROBABILITY = 0.1
BOSS_MAX_HEALTH = 300
PROTRUMP_DAMAGE = 10
REDNECK_DAMAGE = 15
BOSS_DAMAGE = 1200
PROTRUMP_CASHPRIZE = 20
REDNECK_CASHPRIZE = 50
BOSS_CASHPRIZE = 400
PROTRUMP_SPEED = 2
REDNECK_SPEED = 3
BOSS_SPEED = 0.2
REDNECK_HP_DECREASE = 10/60

# Health Bar Drawing Text
HEALTH_NUMBER_OFFSET_X = -25
FONT_SIZE = 12
HEALTH_NUMBER_OFFSET_Y = 60
SHIELD_BAR_OFFSET_X = -5

# Health Bar Drawing life bar
HEALTHBAR_WIDTH = 100
HEALTHBAR_HEIGHT = 20
HEALTHBAR_OFFSET_Y = 50

# Coequipier constants
SUPPORT_RANGE = 300


# Tweet constants
TWEET_START_TIME = 120 * 60
TWEET_END_TIME = 180 * 60
TWEET_DURATION = 30 * 60
SPRITE_SCALING_TWEET = 0.40
TWEET_CENTER_X = SCREEN_WIDTH / 2
TWEET_CENTER_Y = SCREEN_HEIGHT - 100
TWEET_SPEED_BOOST = 2

# Weapon icon position
WEAPON_CENTER_X = 100
WEAPON_CENTER_Y = 50
SPRITE_SCALING_WEAPON = 1
WEAPON_SPRITE = ["sprites/player/weapon-1.png","sprites/player/weapon-2.png","sprites/player/weapon-3.png"]

# Dollars icons position
DOLLARS_CENTER_X = 30
DOLLARS_CENTER_Y = SCREEN_HEIGHT - 25
SPRITE_SCALING_DOLLARS = 1

DOLLARS_TEXT_OFFSET_X = 25
DOLLARS_TEXT_OFFSET_Y = 10

# Votes pannel position
VOTES_CENTER_X = SCREEN_WIDTH - 250
VOTES_CENTER_Y = SCREEN_HEIGHT - 50
SPRITE_SCALING_VOTES = 0.15

VOTES_TEXT_OFFSET_X = 100
VOTES_TEXT_OFFSET_Y = 5
VOTES_WIDTH = 170
VOTES_HEIGHT = 30
VOTES_OFFSET_Y = 5
VOTES_OFFSET_X = 30

# Items bar position
ITEMS_BAR_CENTER_X = SCREEN_WIDTH/2
ITEMS_BAR_CENTER_Y = 60
SPRITE_SCALING_ITEMS_BAR = 1

# Upgrades
UPGRADES_COL1_NAMES = ["PL_ATK_2X", "PL_SPD_2X", "PL_ATK_2X", "PL_SPD_2X", "PL_PT"]
UPGRADES_COL1_SPRITES = ["sprites/gui/upgrade_double_damage.png","sprites/gui/upgrade_double_speed.png","sprites/gui/upgrade_double_damage.png", "sprites/gui/upgrade_double_speed.png", "sprites/gui/upgrade_pierce_through.png"]
UPGRADES_COL1_PRICES = [200, 200, 400, 400, 800]
UPGRADES_COL2_NAMES = ["SUPPORT","SUPPORT_ATK_2X", "SUPPORT_SPD_2X", "SUPPORT_RNG_2X"]
UPGRADES_COL2_SPRITES = ["sprites/gui/upgrade_support.png","sprites/gui/upgrade_double_damage.png","sprites/gui/upgrade_double_speed.png","sprites/gui/upgrade_double_range.png"]
UPGRADES_COL2_PRICES = [600, 600, 1200, 1200]
UPGRADES_COL3_NAMES = ["SHIELD","SHIELD","SHIELD"]
UPGRADES_COL3_SPRITES = ["sprites/gui/upgrade_shield.png","sprites/gui/upgrade_shield.png","sprites/gui/upgrade_shield.png"]
UPGRADES_COL3_PRICES = [400,800,1600]

UPGRADE_TEXT_OFFSET_X = 0
UPGRADE_TEXT_OFFSET_Y = 40
UPGRADE_TEXT_SIZE = 15

# Strike Button
STRIKE_BUTTON_X = SCREEN_WIDTH/2
STRIKE_BUTTON_Y = SCREEN_HEIGHT -45

SPRITE_STRIKE_SCALLING = 0.5
