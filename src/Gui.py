import arcade
import CONST

class Gui():

  def __init__(self):
    self.dollars_sprite = arcade.Sprite("sprites/gui/dollars.png", CONST.SPRITE_SCALING_DOLLARS)
    self.votes_sprite = arcade.Sprite("sprites/gui/votes_pannel.png", CONST.SPRITE_SCALING_VOTES)
    self.items_bar_sprite = arcade.Sprite("sprites/gui/items_bar.png", CONST.SPRITE_SCALING_ITEMS_BAR)

    self.dollars_sprite.center_x = CONST.DOLLARS_CENTER_X
    self.dollars_sprite.center_y = CONST.DOLLARS_CENTER_Y

    self.votes_sprite.center_x = CONST.VOTES_CENTER_X
    self.votes_sprite.center_y = CONST.VOTES_CENTER_Y

    self.items_bar_sprite.center_x = CONST.ITEMS_BAR_CENTER_X
    self.items_bar_sprite.center_y = CONST.ITEMS_BAR_CENTER_Y

  def draw (self, dollars_count, votes_count):
    self.dollars_sprite.draw()
    self.votes_sprite.draw()
    self.items_bar_sprite.draw()

    self.draw_count_bar(votes_count)

    self.draw_dollars_text(dollars_count)
    self.draw_votes_text(votes_count)
  
  def draw_dollars_text(self, dollars_count) :

    dollars_string = f"{dollars_count}$"
    arcade.draw_text(dollars_string,
                        start_x = self.dollars_sprite.center_x + CONST.DOLLARS_TEXT_OFFSET_X,
                        start_y = self.dollars_sprite.center_y - CONST.DOLLARS_TEXT_OFFSET_Y,
                        font_size = CONST.FONT_SIZE,
                        color = arcade.color.BLACK)

  def draw_votes_text (self, votes_count) :

    votes_string = f"{votes_count}"
    arcade.draw_text(votes_string,
                        start_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X,
                        start_y = self.votes_sprite.center_y - CONST.VOTES_TEXT_OFFSET_Y, 
                        font_size = CONST.FONT_SIZE,
                        color = arcade.color.BLACK)

  def draw_count_bar (self, votes_count) :
    """ Draw the votes bar """
    arcade.draw_rectangle_filled(center_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X + CONST.VOTES_OFFSET_X,
                                  center_y = self.votes_sprite.center_y + CONST.VOTES_OFFSET_Y,
                                  width = CONST.VOTES_WIDTH,
                                  height = CONST.VOTES_HEIGHT,
                                  color = arcade.color.SPANISH_BLUE)

    # Calculate width based on health
    health_width = CONST.VOTES_WIDTH * (votes_count / CONST.MAX_VOTES)

    arcade.draw_rectangle_filled(center_x = self.votes_sprite.center_x + CONST.VOTES_TEXT_OFFSET_X - 0.5 * (CONST.VOTES_WIDTH - health_width) + CONST.VOTES_OFFSET_X,
                                  center_y = self.votes_sprite.center_y + CONST.VOTES_OFFSET_Y, 
                                  width = health_width,
                                  height = CONST.VOTES_HEIGHT,
                                  color = arcade.color.OU_CRIMSON_RED)

