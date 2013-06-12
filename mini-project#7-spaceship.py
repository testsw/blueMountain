# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
angular_acceleration = 3.14/32




class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.thrust_center = [0, 0]
        self.thrust_center[1] = self.image_center[1]
        self.thrust_center[0] = self.image_center[0] + self.image_size[0]
        self.forward = [0,0]
       
        self.cannon_tip = [self.image_center[0] + self.pos[0], self.pos[1]]
       
        
    def draw(self,canvas):
        if self.thrust == True:
            canvas.draw_image(self.image, self.thrust_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        

    def update(self):
        global WIDTH, HEIGHT
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.vel[0] *= (1 - 0.01)
        self.vel[1] *= (1 - 0.01)
        
        self.angle += self.angle_vel
        self.forward = angle_to_vector(self.angle)
        
        self.cannon_tip = [self.forward[0]*45 + self.pos[0],
              self.forward[1]*45+ self.pos[1]]
    
        # wrap around
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
        if self.thrust:
            self.vel[0] += 0.1 * self.forward[0]
            self.vel[1] += 0.1 * self.forward[1]
    
    def shoot(self):
        global a_missile, cannon_tip
        velocity = [0, 0]
        
        velocity[0] = self.vel[0] + 3 * self.forward[0]
        velocity[1] = self.vel[1] + 3 * self.forward[1]
        a_missile = Sprite(self.cannon_tip, velocity, 0, 0, missile_image, missile_info, missile_sound)

    
        
    def turn_right(self, acceleration):
        self.angle_vel += acceleration
        
    def turn_left(self, acceleration):
        self.angle_vel -= acceleration
        
        
    def set_thrust(self, on):
        self.thrust = on
        
        if self.thrust:
            ship_thrust_sound.rewind()
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
        
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        global WIDTH, HEIGHT
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.angle += self.angle_vel
        self.forward = angle_to_vector(self.angle)
        
        # wrap around
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
        
    
           
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    canvas.draw_text('Lives', [WIDTH/1.5, HEIGHT/7.5], 30, "White")    
    canvas.draw_text('Score', [WIDTH/1.2, HEIGHT/7.5], 30, "White")   
   
    canvas.draw_text(str(lives), [WIDTH/1.5, HEIGHT/5], 40, "White")    
    canvas.draw_text(str(score), [WIDTH/1.2, HEIGHT/5], 40, "White")   
   
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
#key down handler
def on_key_down(key):
    global angular_acceleration, my_ship
    
    if key==simplegui.KEY_MAP["right"]:
        my_ship.turn_right(angular_acceleration)
    elif key==simplegui.KEY_MAP["left"]:
       my_ship.turn_left(angular_acceleration)
    elif key==simplegui.KEY_MAP["up"]:
        my_ship.set_thrust(True)
    elif key==simplegui.KEY_MAP["space"]:
        my_ship.shoot()

#key up handler
def on_key_up(key):
    global angular_acceleration, my_ship
    if key==simplegui.KEY_MAP["right"]:
       my_ship.turn_right(-angular_acceleration)
    elif key==simplegui.KEY_MAP["left"]:
       my_ship.turn_left(-angular_acceleration)
    elif key==simplegui.KEY_MAP["up"]:
         my_ship.set_thrust(False)
        
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    SLOWEST = 0.005
    FASTEST = 0.1
    pos = [random.choice(range(WIDTH)), random.choice(range(HEIGHT))]
    ang_vel = ( random.random() * ( FASTEST - SLOWEST ) + SLOWEST ) * random.choice([-1, 1])
    angle = random.choice([0, 2*3.14])
    velocity = [random.random()*random.choice(range(7))*0.5, random.random()*random.choice(range(6))*0.5]
    a_rock = Sprite(pos, velocity, angle, ang_vel, asteroid_image, asteroid_info)
   
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0.2, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 10, 0.1, asteroid_image, asteroid_info)
a_missile = Sprite([0,0], [0,0], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(on_key_down)
frame.set_keyup_handler(on_key_up)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
