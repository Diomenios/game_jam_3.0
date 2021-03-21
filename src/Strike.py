import arcade
from arcade.gui import UIManager
import CONST

class Strike(arcade.gui.UIImageButton):

  def __init__(self, center_x, center_y, normal_texture, hover_texture, text=''):
    super().__init__(
      center_x = center_x,
      center_y = center_y,
      normal_texture = normal_texture,
      hover_texture = hover_texture,
      text= ''
    )

    self.sound = arcade.Sound("audios/rekrol-2.mp3")
    self.manager = None
    self.already_clicked = "None"

  def on_click(self):

    if self.already_clicked == "None":
      self.already_clicked = "True"
      self.manager = self.sound.play(CONST.MUSIC_VOLUME*10)

    else :
      self.already_clicked = "False"
      self.sound.stop(self.manager)
