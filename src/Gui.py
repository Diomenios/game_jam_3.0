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

  def draw(self):
    self.dollars_sprite.draw()
    self.votes_sprite.draw()
    self.items_bar_sprite.draw()



