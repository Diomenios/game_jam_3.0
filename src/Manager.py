import arcade
import arcade.gui

import random
import math
import CONST
from moviepy.editor import *
import pygame
import time

from Player import Player
from Supporter import Supporter
from Bullets import Bullets
from ProTrump import ProTrump
from Redneck import Redneck
from Boss import Boss
from Capitol import Capitol
from Coequipier import Coequipier
from Tweet import Tweet
from Gui import Gui

class Manager(arcade.Window):
    def __init__(self):
        # show history
        pygame.display.set_caption('Redneck Rumble')

        clip = VideoFileClip("video/begin_cut.mp4")
        clip.preview()

        pygame.quit()

        # Objects
        self.player = None
        self.supporters = []
        self.bullets = []
        self.capitol = None
        self.coequipier = None
        self.gui = None

        # Game parameters
        self.score = 0
        self.time = 0
        self.spawn_interval = 1
        self.boost_speed = 1
        self.win_state = 0
        self.off = 0
        self.retry = 0
        self.weapon_count = 0

        # Interaction parameters
        self.dirkey_change = False
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.leftclick_pressed = False
        self.leftclick_x = 0
        self.leftclick_y = 0
        self.mouse_x = 0
        self.mouse_y = 0

        self.background = None
        self.music_list = []
        self.current_song_index = 0
        self.current_player = None
        self.music = None


        super().__init__(CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT, CONST.SCREEN_TITLE)


    def setup(self):

        self.player = Player()
        self.capitol = Capitol()
        self.coequipier = None
        self.gui = Gui(0,CONST.MAX_VOTES)
        self.supporters = []
        self.bullets = []

        self.tweet = Tweet()

        arcade.set_background_color(arcade.color.AMAZON)
        self.background = arcade.load_texture("sprites/bg/bg.jpg")
        
        self.music_list = ["audios/background_music.mp3"]
        self.current_song_index = 0
        self.music = arcade.Sound(self.music_list[self.current_song_index], streaming=True)
        self.play_song()


    def end_game(self):
        arcade.close_window()
        self.off = 1

        if self.win_state:
            clip = VideoFileClip("video/win_cut.mp4")
            clip.preview()
        else:
            clip = VideoFileClip("video/game_over_cut.mp4")
            clip.preview()

        pygame.quit()
        exit()
        
    def advance_song(self):
        self.current_song_index += 1
        if self.current_song_index >= len(self.music_list):
            self.current_song_index = 0
    
    def play_song(self):
        #if self.music:
        #    self.music.stop(self.current_player)
        self.current_player = self.music.play(CONST.MUSIC_VOLUME)
        time.sleep(0.03)


    def on_draw(self):
        if not self.off:
            arcade.start_render()

            self.capitol.draw()
            self.player.draw()
            self.gui.draw()
            self.tweet.draw()


            #self.coequipier.draw()
            for b in self.bullets:
                b.draw()
            for s in self.supporters:
                s.draw()





    def on_update(self, delta_time):
        if not self.off:
            self.time = self.time + 1
            self.gui.votes_count = int(CONST.MAX_VOTES - (self.time/60*2))

            # Create supporter
            if self.time % (self.spawn_interval * 60) == 0:
                r = random.random()
                if r < CONST.REDNECK_PROBABILITY:
                    s = Redneck(1)
                else:
                    s = ProTrump(1)
                self.supporters.append(s)


            # Distribute events
            self.distribute_events()

            self.player.update()
            self.tweet.update()

            for s in self.supporters:
                s.boost_speed = max(1,self.tweet.activated * CONST.TWEET_SPEED_BOOST)
            self.boost_speed = max(1,self.tweet.activated * CONST.TWEET_SPEED_BOOST)

            for b in self.bullets:
                b.update()
            for s in self.supporters:
                if s.type == "Redneck":
                    s.update(self.player.sprite.center_x, self.player.sprite.center_y)
                else:
                    s.update()

            # Fire a bullet
            bullet = self.player.fire(self.mouse_x,self.mouse_y)
            if bullet != None:
                self.bullets.append(bullet)

            if self.coequipier is not None:
                nearest = None
                dist = 1e9
                for s in self.supporters:
                    d = math.sqrt((s.sprite.center_x-CONST.SCREEN_WIDTH/2)**2 + (s.sprite.center_y-CONST.SCREEN_HEIGHT/2)**2)
                    if d < dist and d < self.coequipier.range :
                        dist = d
                        nearest = s
                if nearest is not None:
                    bullet = self.coequipier.fire(nearest.sprite.center_x,nearest.sprite.center_y)
                    if bullet != None:
                        self.bullets.append(bullet)

                self.player.update()
                self.tweet.update()

                for s in self.supporters:
                    s.boost_speed = max(1,self.tweet.activated * CONST.TWEET_SPEED_BOOST)
                self.boost_speed = max(1,self.tweet.activated * CONST.TWEET_SPEED_BOOST)

            for b in self.bullets:
                b.update()
                for s in self.supporters:
                    if arcade.check_for_collision(b.sprite, s.sprite) and b.last_touch != s:
                        s.hit_points -= b.damage
                        if s.hit_points <= 0:
                            self.gui.dollars_count += s.cashprize
                        b.last_touch = s
                        b.hit_points -= 1
                        break
            self.bullets = [b for b in self.bullets if b.hit_points > 0]
            self.supporters = [s for s in self.supporters if s.hit_points > 0]

            # Collisions player <-> supporters
            stunned = False
            for s in self.supporters:
                if arcade.check_for_collision(self.player.sprite, s.sprite):
                    if s.type == "Redneck":
                        s.hit_points -= CONST.REDNECK_HP_DECREASE
                        s.is_on_player = True
                    self.player.stun = True
                    stunned = True
            if not stunned:
                self.player.stun = False
            self.supporters = [s for s in self.supporters if s.hit_points > 0]

            # Collisions capitol <-> supporters
            for s in self.supporters:
                if arcade.check_for_collision(self.capitol.sprite, s.sprite):
                    self.capitol.hit(s.damage)
                    s.hit_points = 0
            self.supporters = [s for s in self.supporters if s.hit_points > 0]

            # Collisions capitol <-> bullets
            for b in self.bullets:
                if arcade.check_for_collision(self.capitol.sprite, b.sprite) and b.sender != "Coequipier":
                    b.hit_points = 0
            self.bullets = [b for b in self.bullets if b.hit_points > 0]

            print(len(self.bullets))

            """ ENDING CONDITIONS """
            if self.capitol.hit_point <= 0:
                self.win_state = 0
                self.end_game()

            """ WIN CONDITIONS """
            if self.gui.votes_count <= 0:
                self.win_state = 1
                self.end_game()
                
            if self.music.get_stream_position(self.current_player) == 0.0:
                self.advance_song()
                self.play_song()

    def upgrade(self, action):
        if action == "PL_ATK_2X":
            self.player.weapon.ammo_dmg *= 2
        elif action == "PL_SPD_2X":
            self.weapon_count +=1
            self.player.weapon.rate /= 2
            self.gui.weapon_sprite = arcade.Sprite(CONST.WEAPON_SPRITE[self.weapon_count], CONST.SPRITE_SCALING_WEAPON)
        elif action == "PL_PT":
            self.player.weapon.ammo_hit_point += 1
        elif action == "SUPPORT":
            self.coequipier = Coequipier()
        elif action == "SUPPORT_ATK_2X":
            self.coequipier.weapon.ammo_dmg *= 2
        elif action == "SUPPORT_SPD_2X":
            self.coequipier.weapon.rate /= 2
        elif action == "SUPPORT_RNG_2X":
            self.coequipier.range *= 2
        elif action == "SHIELD":
            self.capitol.shield += 30

    """ EVENTS """

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.leftclick_pressed = True
            self.leftclick_x = x
            self.leftclick_y = y

        a = arcade.SpriteList()
        a.append(self.gui.col1_upgrade_sprite)
        a.append(self.gui.col2_upgrade_sprite)
        a.append(self.gui.col3_upgrade_sprite)
        upgrade = arcade.get_sprites_at_point((x,y), a)
        if len(upgrade) > 0:
            upgrade = upgrade[-1]
            action = self.gui.select_upgrade(upgrade)
            self.upgrade(action)


    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.leftclick_pressed = False

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Z:
            self.up_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.S:
            self.down_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.Q:
            self.left_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.D:
            self.right_pressed = True
            self.dirkey_change = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.Z:
            self.up_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.S:
            self.down_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.Q:
            self.left_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.D:
            self.right_pressed = False
            self.dirkey_change = True

    def distribute_events(self):
        # Player
        if self.dirkey_change:
            self.player.update_keys(self.up_pressed, self.down_pressed, self.left_pressed, self.right_pressed)
        self.player.auto_fire = self.leftclick_pressed
