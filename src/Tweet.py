import arcade
import math
import random
import CONST

class Tweet():

    def __init__(self):
        # sprite initialisation
        self.sprite = arcade.Sprite("sprites/tweet/tweet.png", CONST.SPRITE_SCALING_TWEET)
        self.sprite.alpha = 200

        self.sprite.center_x = CONST.TWEET_CENTER_X
        self.sprite.center_y = CONST.TWEET_CENTER_Y
        self.start_time = random.randint(CONST.TWEET_START_TIME, CONST.TWEET_END_TIME)
        self.duration = CONST.TWEET_DURATION
        self.end_time = self.start_time + self.duration
        self.count = 0
        self.sound = arcade.Sound("audios/stop_the_count2.mp3")
        self.activated = False
        self.no_sound = True

    def draw(self):
        self.sprite.draw()

    def update(self):
        if self.count < self.start_time or self.count > self.end_time:
            self.sprite.scale = 0
            self.activated = False
        elif self.count >= self.start_time and self.count < (self.start_time+self.duration*0.05):
            self.sprite.scale = min(CONST.SPRITE_SCALING_TWEET,max(0,(self.count-self.start_time)/(self.duration*0.05)*CONST.SPRITE_SCALING_TWEET))
            self.activated = True
            if self.no_sound:
                self.sound.play(CONST.MUSIC_VOLUME*16)
                self.no_sound = False
        elif self.count <= self.end_time and self.count > (self.end_time-self.duration*0.05):
            self.sprite.scale = min(CONST.SPRITE_SCALING_TWEET,max(0,(self.end_time-self.count)/(self.duration*0.05)*CONST.SPRITE_SCALING_TWEET))
            self.activated = True
        else:
            self.sprite.scale = CONST.SPRITE_SCALING_TWEET
            self.activated = True
        self.count += 1
