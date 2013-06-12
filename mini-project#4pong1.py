# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0]
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
paddle1_vel = 0
paddle2_vel = 0
# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
     
    #if we collide on the left/right gutter, reset ball
    
    if((ball_pos[0] <= BALL_RADIUS + PAD_WIDTH) or (ball_pos[0] >= WIDTH -1 - BALL_RADIUS - PAD_WIDTH)):
        
        if((ball_pos[1] > paddle1_pos -PAD_HEIGHT/2) and (ball_pos[1] < paddle1_pos + PAD_HEIGHT/2)):
            ball_vel[0] = -ball_vel[0]
            return
        elif((ball_pos[1] > paddle2_pos -PAD_HEIGHT/2) and (ball_pos[1] < paddle2_pos + PAD_HEIGHT/2)):
            ball_vel[0] = -ball_vel[0]
            return
        else:
            ball_pos = [WIDTH/2, HEIGHT/2]
    
    #set velocity to random value
    ball_vel[0] = random.randrange(120, 240)/80
    ball_vel[1] = -random.randrange(60, 180)/80
    
    if( right == False):
        ball_vel[0] = -ball_vel[0]
        
       
    print ball_vel
        
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

# define event handlers

def new_game(right):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(right)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
   
    #did we cross the bottom of screen
    if(ball_pos[1] >= HEIGHT -1 - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    #did we cross the top of screen
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    
    #did we collide on the left gutter
    if(ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        ball_init(True)
    #did we collide on the left gutter
    if(ball_pos[0] >= WIDTH - 1 - BALL_RADIUS - PAD_WIDTH):
        ball_init(False)
    
    # update paddle's vertical position, keep paddle on the screen
    if(((paddle1_pos + paddle1_vel) >= PAD_HEIGHT/2) and ((paddle1_pos + paddle1_vel) <= (HEIGHT - PAD_HEIGHT/2))):
        paddle1_pos += paddle1_vel
    if(((paddle2_pos + paddle2_vel) >= PAD_HEIGHT/2) and ((paddle2_pos + paddle2_vel) <= (HEIGHT- PAD_HEIGHT/2))):
        paddle2_pos += paddle2_vel
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "Green", "Green")
    
    # draw paddles
    c.draw_line([PAD_WIDTH/2, paddle1_pos-PAD_HEIGHT/2], [PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT/2], PAD_WIDTH, "Blue")
    c.draw_line([WIDTH-PAD_WIDTH/2, paddle2_pos-PAD_HEIGHT/2], [WIDTH-PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT/2], PAD_WIDTH, "Blue")
       
    # update ball
            
    # draw ball and scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    vel = 1
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += -vel
    elif key==simplegui.KEY_MAP["s"]:
       paddle1_vel += vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += vel
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += -vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    vel = 1
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel += vel
    elif key==simplegui.KEY_MAP["s"]:
       paddle1_vel += -vel
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += -vel
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel += vel

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
new_game(True)


# start frame
frame.start()
