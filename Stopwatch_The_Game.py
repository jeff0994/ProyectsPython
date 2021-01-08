# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:33:44 2021

@author: Yefry Lopez

You need intall Simplegui

You can see the code in action here: 
    https://py3.codeskulptor.org/#user306_YTAa8q66OLDKlLV.py
"""

# template for "Stopwatch: The Game"
import simplegui
# define global variables
variable = 0
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    A = t//600
    var3 = t //10
    var5 = var3 % 60
    B = var5 // 10
    C = var5 % 10
    D = t % 10
    
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global start
    timer.start()
     
def stop():
    global start, x, y
    if timer.is_running():
        y += 1
        timer.stop()
        if variable % 10 == 0:
            x += 1
    
def reset():
    global variable
    global x
    global y
    variable = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global variable
    global x
    global y
    variable += 1
# define draw handler
def draw_handler(canvas):
    global variable
    global x 
    global y
    string = str(x) + "/" + str(y)
     
    canvas.draw_text(format(variable), (120, 90), 30, 'White',"sans-serif")
    canvas.draw_text(string, (250, 20), 18, 'White',"sans-serif")

# create frame
frame = simplegui.create_frame('Stopwatch', 300, 150)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
start = frame.add_button('Start', start, 100)
stop = frame.add_button('Stop', stop, 100)
reset = frame.add_button('Reset', reset, 100)


# start frame
frame.start()



# Please remember to review the grading rubric