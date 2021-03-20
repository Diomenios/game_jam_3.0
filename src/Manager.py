import arcade
import CONST
from Player import Player
from Supporter import Supporter
from Bullets import Bullets
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
        self.spawn_interval = 0.5

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
        #self.capitol = Capitol()


    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        #self.capitol.draw()
        #self.coequipier.draw()
        for b in self.bullets:
            b.draw()
        for s in self.supporters:
            s.draw()



    def on_update(self, delta_time):
        self.time = self.time + 1
        
        # Create supporter
        if self.time % (self.spawn_interval * 60) == 0:
            s = Supporter(CONST.SUPPORTER_MAX_HEALTH)
            self.supporters.append(s)


        # Distribute events
        self.distribute_events()

        self.player.update()
        for b in self.bullets:
            b.update()
        for s in self.supporters:
            s.update()
            # Draw supporter's health bar
            s.draw_health_bar()

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
                    s.hit_point -= b.damage
                    b.last_touch = s
                    b.hit_point -= 1
                    break;

        self.bullets = [b for b in self.bullets if b.hit_points <= 0]
        self.supporters = [s for s in self.supporters if s.hit_points <= 0]





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
        if key == arcade.key.UP:
            self.up_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.dirkey_change = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.dirkey_change = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.dirkey_change = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.dirkey_change = True




    def distribute_events(self):
        # Player
        if self.dirkey_change:
            self.player.update_keys(self.up_pressed, self.down_pressed, self.left_pressed, self.right_pressed)
        self.player.auto_fire = self.leftclick_pressed
