import arcade
import CONST
from Player import Player
from Supporter import Supporter
#from Bullet import Bullet
#from Capitol import Capitol
#from Coequipier import Coequipier

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
        #for s in supporters:
        #    s.draw()
            
 
    
    def on_update(self, delta_time):
        self.time = self.time + 1
        
        # Distribute events
        self.distribute_events()
        
        self.player.update()
        for b in self.bullets:
            b.update()
        
        # Fire a bullet
        bullet = self.player.fire(self.mouse_x,self.mouse_y)
        if bullet != None:
            self.bullets.append(bullet)
            
                  
    
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