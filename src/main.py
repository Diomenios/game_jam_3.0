"""
Sprite Collect Coins

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins
"""

import random
import arcade
import math
import time

import CONST
from Player import Player
from Supporter import Supporter

class Game(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT, CONST.SCREEN_TITLE)

        # Variables that will hold sprite lists
        self.player_list = None
        self.supporter_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.score_text = None

        # Don't show the mouse cursor
        self.set_mouse_visible(True)

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.sound.load_sound(":resources:sounds/laser1.wav")
        self.hit_sound = arcade.sound.load_sound(":resources:sounds/phaseJump1.wav")

        arcade.set_background_color(arcade.color.AMAZON)

        arcade.schedule(self.spawn_supporter,5)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.supporter_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = Player(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        self.player_sprite.setup()
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(CONST.COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png", CONST.SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(CONST.SCREEN_WIDTH)
            coin.center_y = random.randrange(CONST.SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def spawn_supporter(self,_delta_time):
        print("Hello")
        supporter = Supporter(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        supporter.setup()
        self.supporter_list.append(supporter)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.supporter_list.draw()

        # Put the text on the screen.
        output = f"Coins: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_press(self, x, y, button, modifiers):
        """ Called whenever the mouse button is clicked. """

        # Create a bullet
        bullet = arcade.Sprite("sprite/player/ammo-1.png", CONST.SPRITE_SCALING_LASER)

        # Position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in self.view_bottom and self.view_left.
        dest_x = x
        dest_y = y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        bullet.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * CONST.BULLET_SPEED
        bullet.change_y = math.sin(angle) * CONST.BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        
        arcade.draw_line(self.player_sprite.center_x, self.player_sprite.center_y, x, y, arcade.color.WOOD_BROWN, 3)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.coin_list.update()
        self.player_list.update()
        self.supporter_list.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Call update on all sprites
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > self.width or bullet.top < 0 or bullet.right < 0 or bullet.left > self.width:
                bullet.remove_from_sprite_lists()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

        for i in self.player_list:
            i.update_keys(self.up_pressed, self.down_pressed, self.left_pressed, self.right_pressed)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False

        for i in self.player_list:
            i.update_keys(self.up_pressed, self.down_pressed, self.left_pressed, self.right_pressed)


def main():
    """ Main method """
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
