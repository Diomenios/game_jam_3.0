import arcade
import CONST

class Player():
    def __init__(self):
        # sprite inititialisation
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", CONST.SPRITE_SCALING_PLAYER)
        self.up_pressed = 0
        self.down_pressed =  0
        self.left_pressed = 0
        self.right_pressed = 0
        self.auto_fire = 0
        self.stun = 0

        # position at begining
        self.sprite.center_x = CONST.PLAYER_X
        self.sprite.center_y = CONST.PLAYER_Y
        self.vel = CONST.PLAYER_INIT_VEL

        # weapon
        self.weapon = Weapon(1)



    def update(self):
        """ Update the player sprite """
        # Calculate speed based on the keys pressed
        self.sprite.change_x = 0
        self.sprite.change_y = 0

        if not self.stun:
            if self.up_pressed and not self.down_pressed:
                self.sprite.change_y = self.vel
            elif self.sprit.down_pressed and not self.up_pressed:
                self.sprite.change_y = -self.vel
            if self.left_pressed and not self.right_pressed:
                self.sprite.change_x = -self.vel
            elif self.right_pressed and not self.left_pressed:
                self.sprite.change_x = self.vel

            # Move player.
            # Remove these lines if physics engine is moving player.
            self.sprite.center_x += self.change_x
            self.sprite.center_y += self.change_y

            # Check for out-of-bounds
            if self.sprite.left < 0:
                self.sprite.left = 0
            elif self.sprite.right > CONST.SCREEN_WIDTH - 1:
                self.sprite.right = CONST.SCREEN_WIDTH - 1

            if self.sprite.bottom < 0:
                self.sprite.bottom = 0
            elif self.sprite.top > CONST.SCREEN_HEIGHT - 1:
                self.sprite.top = CONST.SCREEN_HEIGHT - 1

    def update_keys(self, up_pressed, down_pressed, left_pressed, right_pressed):
        """ Update the Key pressed """
        self.up_pressed = up_pressed
        self.down_pressed = down_pressed
        self.left_pressed = left_pressed
        self.right_pressed = right_pressed

    def fire(dest_x,dest_y):
        bullet = None
        if auto_fire and not self.count%self.weapon.rate :
            # Create a bullet
            bullet = arcade.Sprite("sprite/player/ammo-1.png", CONST.SPRITE_SCALING_LASER)

            # Position the bullet at the player's current location
            start_x = self.sprite.center_x
            start_y = self.sprite.center_y
            bullet.center_x = start_x
            bullet.center_y = start_y


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
        self.count += 1
        return bullet
