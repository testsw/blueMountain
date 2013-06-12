# template for "Stopwatch: The Game"

import simplegui

# define global variables
interval = 100
time = 0
time_str = "0:00:0"
success_rate = "0/0"
success = 0
attempt = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = int(t / 600)
    rem = t % 600
    seconds = int(rem / 10 )
    tenths = rem % 10
    
    global time_str
    
    if(minutes > 0):
        time_str = str(minutes) + ":"
    else:
        time_str = "0:"
        
    if(seconds > 9):
        time_str = time_str + str(seconds) + ":"
    elif(seconds > 0):
        time_str = time_str + "0" + str(seconds) + ":"
    else:
        time_str = time_str + "00:"
    
    if(tenths > 0):
        time_str = time_str + str(tenths)
    else:
        time_str = time_str + "0"   
        
    return time_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset():
    global time, success, attempt, success_rate
    time = 0
    success = 0
    attempt = 0
    success_rate = "0/0"
    timer.stop()
    
def stop():
    global time
    if(timer.is_running() == False):
        return
    
    timer.stop()
    update_stats(time)
    
def start():
    timer.start()

def update_stats(tm):
    global success, attempt, success_rate
    
    attempt = attempt + 1
    if(tm % 10 == 0):
        success = success + 1
    success_rate = str(success) + "/" + str(attempt)

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1
    
# define draw handler
def draw(canvas):
    global time
    format(time)
    canvas.draw_text(time_str, [75, 130], 36, "Red")
    canvas.draw_text(success_rate, [190, 30], 30, "Green")
    
# create frame
frame = simplegui.create_frame("StopWatch", 250, 250)
frame.add_button("Stop", stop, 50)
frame.add_button("Start", start, 50)
frame.add_button("Reset", reset, 50)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.set_draw_handler(draw)

# start frame
frame.start()
timer.stop()


# unit test for format
#for n in [0, 11, 321, 613, 6600]:
#    print format(n)

# Please remember to review the grading rubric
