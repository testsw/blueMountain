# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random, simplegui
# initialize global variables used in your code
global answer 
answer = random.randrange(0, 100)
global attempt 
attempt = 7
global level
level = 100

# define event handlers for control panel

def range100():
    # button that changes range to range [0,100) and restarts
    global attempt, answer, level
    
    attempt = 7
    level = 100
    answer = random.randrange(0, 100)
    print "Starting game with Range: 0 -100..."
    print "You have", attempt, "chances to guess..."
    
    #print answer
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global attempt, answer, level
    
    attempt = 10
    level = 1000
    answer = random.randrange(0, 1000)
    print "Starting game with Range: 0 -1000..."
    print "You have", attempt, "chances to guess..."
    
    #print answer
    
    
def get_input(guess):
    # main game logic goes here	
    global attempt, answer, level
    attempt -= 1
    
    print "You guessed: ", guess
    print "Remaining guesses: ", attempt
    
    if(int(guess) == answer):
        print "Correct!"
        print
    else:
        if( attempt == 0):
            print
            print " Chances exhausted. game over!"
            print
            if(level == 100):
                range100()
            else:
                range1000()
        elif(int(guess) > answer):
            print "Lower"
        else:
            print "Higher"

    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)

# register event handlers for control elements
frame.add_button("Range: 0- 100", range100, 110)
frame.add_button("Range: 0- 1000", range1000, 110)
frame.add_input("Guess a number", get_input, 110)


# start frame
range100()
frame.start()


# always remember to check your completed program against the grading rubric
