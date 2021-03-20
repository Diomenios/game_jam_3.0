import arcade
import random
import CONST
from Player import Player
from Supporter import Supporter
from Bullets import Bullets
from ProTrump import ProTrump
from Redneck import Redneck
from Boss import Boss
from Capitol import Capitol
from Coequipier import Coequipier

class Manager(arcade.Window):
    def __init__(self):
        # Objects
        self.player = None
        self.supporters = []
        self.bullets = []
        self.capitol = None
        self.coequipier = None

        # Game parameters
        self.score = 0
        self.time = 0
        self.spawn_interval = 1
        self.boost_speed = 1

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

        super().__init__(CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT, CONST.SCREEN_TITLE)

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)

        self.player = Player()
        self.capitol = Capitol()
        self.supporters = []
        self.bullets = []
        self.coequipier = None


    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.capitol.draw()

        #self.coequipier.draw()
        for b in self.bullets:
            b.draw()
        for s in self.supporters:
            s.draw()



    def on_update(self, delta_time):
        self.time = self.time + 1

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

        # Remove bullets & supporters
        self.bullets = [b for b in self.bullets if b.sprite.right > 0 and b.sprite.left < (CONST.SCREEN_WIDTH - 1) and b.sprite.bottom > 0 and b.sprite.top < (CONST.SCREEN_HEIGHT - 1)]

        # Collisions bullets <-> supporters
        for b in self.bullets:
            for s in self.supporters:
                if arcade.check_for_collision(b.sprite, s.sprite) and b.last_touch != s:
                    s.hit_points -= b.damage
                    b.last_touch = s
                    b.hit_points -= 1
                    break;
        self.bullets = [b for b in self.bullets if b.hit_points > 0]
        self.supporters = [s for s in self.supporters if s.hit_points > 0]

        # Collisions player <-> supporters
        stunned = False
        for s in self.supporters:
            if arcade.check_for_collision(self.player.sprite, s.sprite):
                if s.type == "Redneck":
                    s.hit_points -= CONST.REDNECK_HP_DECREASE
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





    """ EVENTS """

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.leftclick_pressed = True
            self.leftclick_x = x
            self.leftclick_y = y

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
