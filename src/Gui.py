import arcade
import CONST

class Gui():

  def __init__(self, dollars_count, votes_count):

    self.col1_upgrade_state = 0
    self.col1_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL1_SPRITES[self.col1_upgrade_state],1)
    self.col1_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2 - 70
    self.col1_upgrade_sprite.center_y = 35

    self.col2_upgrade_state = 0
    self.col2_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL2_SPRITES[self.col2_upgrade_state],1)
    self.col2_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2
    self.col2_upgrade_sprite.center_y = 35

    self.col3_upgrade_state = 0
    self.col3_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL3_SPRITES[self.col3_upgrade_state],1)
    self.col3_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2 + 70
    self.col3_upgrade_sprite.center_y = 35

    self.dollars_sprite = arcade.Sprite("sprites/gui/dollars.png", CONST.SPRITE_SCALING_DOLLARS)
    self.weapon_sprite = arcade.Sprite(CONST.WEAPON_SPRITE[0], CONST.SPRITE_SCALING_WEAPON)
    self.votes_sprite = arcade.Sprite("sprites/gui/votes_pannel.png", CONST.SPRITE_SCALING_VOTES)
    self.items_bar_sprite = arcade.Sprite("sprites/gui/items_bar.png", CONST.SPRITE_SCALING_ITEMS_BAR)

    self.dollars_sprite.center_x = CONST.DOLLARS_CENTER_X
    self.dollars_sprite.center_y = CONST.DOLLARS_CENTER_Y

    self.votes_sprite.center_x = CONST.VOTES_CENTER_X
    self.votes_sprite.center_y = CONST.VOTES_CENTER_Y

    self.items_bar_sprite.center_x = CONST.ITEMS_BAR_CENTER_X
    self.items_bar_sprite.center_y = CONST.ITEMS_BAR_CENTER_Y

    self.dollars_count = dollars_count
    self.votes_count = votes_count

  def select_upgrade(self, upgrade):
    if upgrade == self.col1_upgrade_sprite and self.dollars_count >= self.col1_upgrade_price:
        self.col1_upgrade_state += 1
        self.dollars_count -= self.col1_upgrade_price
        return self.col1_upgrade_name
    elif upgrade == self.col2_upgrade_sprite and self.dollars_count >= self.col2_upgrade_price:
        self.col2_upgrade_state += 1
        self.dollars_count -= self.col2_upgrade_price
        return self.col2_upgrade_name
    elif upgrade == self.col3_upgrade_sprite and self.dollars_count >= self.col3_upgrade_price:
        self.col3_upgrade_state += 1
        self.dollars_count -= self.col3_upgrade_price
        return self.col3_upgrade_name
    else:
        return None

    return

  def draw (self):
    self.dollars_sprite.draw()
    self.votes_sprite.draw()

    """ UPGRADES """
    if self.col1_upgrade_state < len(CONST.UPGRADES_COL1_NAMES):
        self.col1_upgrade_name = CONST.UPGRADES_COL1_NAMES[self.col1_upgrade_state]
        self.col1_upgrade_price = CONST.UPGRADES_COL1_PRICES[self.col1_upgrade_state]
        self.col1_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL1_SPRITES[self.col1_upgrade_state],1)
        self.col1_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2 - 70
        self.col1_upgrade_sprite.center_y = 35
        self.col1_upgrade_sprite.color = (150,150,150) if self.dollars_count < self.col1_upgrade_price else (220,255,220)
        self.col1_upgrade_sprite.draw()
        self.draw_update_count(self.col1_upgrade_price, self.col1_upgrade_sprite.center_x, self.col1_upgrade_sprite.center_y)

    if self.col2_upgrade_state < len(CONST.UPGRADES_COL2_NAMES):
        self.col2_upgrade_name = CONST.UPGRADES_COL2_NAMES[self.col2_upgrade_state]
        self.col2_upgrade_price = CONST.UPGRADES_COL2_PRICES[self.col2_upgrade_state]
        self.col2_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL2_SPRITES[self.col2_upgrade_state],1)
        self.col2_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2
        self.col2_upgrade_sprite.center_y = 35
        self.col2_upgrade_sprite.color = (150,150,150) if self.dollars_count < self.col2_upgrade_price else (220,255,220)
        self.col2_upgrade_sprite.draw()
        self.draw_update_count(self.col2_upgrade_price, self.col2_upgrade_sprite.center_x, self.col2_upgrade_sprite.center_y)

    if self.col3_upgrade_state < len(CONST.UPGRADES_COL3_NAMES):
        self.col3_upgrade_name = CONST.UPGRADES_COL3_NAMES[self.col3_upgrade_state]
        self.col3_upgrade_price = CONST.UPGRADES_COL3_PRICES[self.col3_upgrade_state]
        self.col3_upgrade_sprite = arcade.Sprite(CONST.UPGRADES_COL3_SPRITES[self.col3_upgrade_state],1)
        self.col3_upgrade_sprite.center_x = CONST.SCREEN_WIDTH / 2 + 70
        self.col3_upgrade_sprite.center_y = 35
        self.col3_upgrade_sprite.color = (150,150,150) if self.dollars_count < self.col3_upgrade_price else (220,255,220)
        self.col3_upgrade_sprite.draw()
        self.draw_update_count(self.col3_upgrade_price, self.col3_upgrade_sprite.center_x, self.col3_upgrade_sprite.center_y)

    self.weapon_sprite.center_x = CONST.WEAPON_CENTER_X
    self.weapon_sprite.center_y = CONST.WEAPON_CENTER_Y
    self.weapon_sprite.draw()

    self.draw_count_bar()

    self.draw_dollars_text()
    self.draw_votes_text()

  def draw_dollars_text(self) :

    dollars_string = f"{self.dollars_count}$"
    arcade.draw_text(dollars_string,
                        start_x = self.dollars_sprite.center_x + CONST.DOLLARS_TEXT_OFFSET_X,
                        start_y = self.dollars_sprite.center_y,
                        font_size = 24,
                        anchor_x="left",
                        anchor_y="center",
                        color = arcade.color.BLACK)

  def draw_votes_text (self):

    votes_string = f"{self.votes_count}"
    arcade.draw_text(votes_string,
                        start_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X + CONST.VOTES_OFFSET_X,
                        start_y = self.votes_sprite.center_y + CONST.VOTES_OFFSET_Y,
                        font_size = 24,
                        anchor_x="center",
                        anchor_y="center",
                        color = arcade.color.BLACK)

  def draw_count_bar (self):
    """ Draw the votes bar """
    arcade.draw_rectangle_filled(center_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X + CONST.VOTES_OFFSET_X,
                                  center_y = self.votes_sprite.center_y + CONST.VOTES_OFFSET_Y,
                                  width = CONST.VOTES_WIDTH,
                                  height = CONST.VOTES_HEIGHT,
                                  color = arcade.color.SPANISH_BLUE)

    # Calculate width based on health
    health_width = CONST.VOTES_WIDTH * (self.votes_count / CONST.MAX_VOTES)

    arcade.draw_rectangle_filled(center_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X - 0.5 * (CONST.VOTES_WIDTH - health_width) + CONST.VOTES_OFFSET_X,
                                  center_y = self.votes_sprite.center_y + CONST.VOTES_OFFSET_Y,
                                  width = health_width,
                                  height = CONST.VOTES_HEIGHT,
                                  color = arcade.color.OU_CRIMSON_RED)

  def draw_update_count(self, price, center_x, center_y):
    """ Draw the votes bar """

    votes_string = f"{price}$"
    arcade.draw_text(votes_string,
                        start_x = center_x + CONST.UPGRADE_TEXT_OFFSET_X,
                        start_y = center_y + CONST.UPGRADE_TEXT_OFFSET_Y,
                        font_size = CONST.UPGRADE_TEXT_SIZE,
                        anchor_x="center",
                        anchor_y="center",
                        color = arcade.color.BLACK)
