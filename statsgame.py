import tkinter
from tkinter import  Canvas
from tkinter import PhotoImage
import random
import time
import threading


def kp(event):
#Take user input
    
    global arrow
    global gameboard
    gameboard.unbind_all('<KeyRelease>')    
    if event.keysym == 'Up':
        check(1)
        
    elif event.keysym == 'Down':
        check(0)    
        
    elif event.keysym == 'Left':
        check(3)
        
    elif event.keysym == 'Right':
        check(2)
       
    next()
    return

def check(dir):
#Check whether the user was correct and record data.  Also records direction.
    
    global cur
    global correct
    global direcs
    global curd
    if(cur == dir):
        correct.append("correct")
    else:
        correct.append("incorrect")
        
    if(cur == 0):
        direcs.append("UP")
    elif(cur == 1):
        direcs.append("DOWN")
    elif(cur == 2):
        direcs.append("LEFT")
    elif(cur == 3):
        direcs.append("RIGHT")
        
    return

def next():
#Display the next (random) arrow after the next preset delay and measure 
#reaction time.
    
    global cur
    global arrow
    global gameboard
    global start
    global tdisp
    global dn
    global times
    global correct
    global totalresp
    global top
    global curd
    delays = [1.3, 3, 2.5, 1.7, 1.6, 5, 1.6, 1.4, 1.2, 3.6, 1.7, 3, 1.85, 1.38, 1.14, 
              1.28, 1.42, 1.2, 3.67, 1.11, 1.45, 1.34, 1.23, 1.94, 1.77, 1.19, 1.99,
              1, 1.4, 1.5, 1.2, 1.1, 1.4, 1.1, 1.34, 1.23, 1.94, 1.77, 1.19, 1.99,
              1, 1.4, 1.5, 1.2, 1.1, 1.4, 1.1]
    sl = [650, 650, 400, 950, 0, 350, 200, 200]
    fin = time.time()
    resp = round(fin - start, 3)
    gameboard.delete(tdisp)
    gameboard.delete(arrow)
    times.append(resp)
    gameboard.delete(arrow)
    if(resp > 1.2):
        tdisp = gameboard.create_text(600, 600, anchor = "ne", text = resp, fill = 'red', font = ("Times", 50))
    else:

        tdisp = gameboard.create_text(600, 600, anchor = "ne", text = resp, fill = 'white', font = ("Times", 50))        
    top.update()
    n = random.randint(1, 3)
    d = random.randint(1, 3)
    cur = (cur + n) % 4
    curd = (curd + d) % 4
    time.sleep(delays[dn]-1)
    dn += 1
    totalresp += resp
    gameboard.bind_all('<KeyRelease>', kp)     
    if(cur == 0):    
        arrow = gameboard.create_image(sl[curd], sl[curd + 4], anchor= "ne", image = upI) 
    elif(cur == 1):    
        arrow = gameboard.create_image(sl[curd], sl[curd + 4], anchor= "ne", image = downI) 
    elif(cur == 2):    
        arrow = gameboard.create_image(sl[curd], sl[curd + 4], anchor= "ne", image = leftI) 
    elif(cur == 3):    
        arrow = gameboard.create_image(sl[curd], sl[curd + 4], anchor= "ne", image = rightI)   
        
    if totalresp > 30:
        end()
    start = time.time()
    return


def end():
#Save accuracy and reaction time results for each trial in "Results.csv"
    
    global times
    global gameboard
    global tdisp
    global direcs
    global dn
    
    f = open('Results.csv', 'a')
    f.write("\n \n")
    for i in range(len(times)-1):
        f.write(str(times[i+1]))
        f.write(", ")
    f.write(str(times[dn - 1]))
    f.write("\n")
    for i in range(len(correct)-1):
        if(times[i+1] > 2):
            f.write("incorrect")
        else:
            f.write(str(correct[i+1]))
        f.write(", ")

    f.write(str(correct[dn-1]))   
        
    f.write("\n")
    for i in range(len(times)-1):
        f.write(str(direcs[i+1]))
        f.write(", ")
    f.write(str(direcs[dn-1]))
    
    f.close
    gameboard.delete(tdisp)
    tdisp = gameboard.create_text(600, 600, anchor = "ne", text = "DONE!", fill = 'red', font = ("Times", 50))    
    gameboard.unbind_all('<KeyRelease>')    
    
if  __name__ == "__main__":
    global arrow
    global cur
    global start 
    global tdisp  
    global dn
    global times
    global correct
    global direcs
    global totalresp
    global top
    global curd
    correct = []
    times = []
    direcs = []
    totalresp = 0
    top = tkinter.Tk()
    
    gameboard = Canvas(top, bg = "black", width = 1000, height = 750)
    downI = PhotoImage(file = "Down.PNG")
    upI = PhotoImage(file = "Up.PNG")
    leftI = PhotoImage(file = "Left.PNG")
    rightI = PhotoImage(file = "Right.PNG")
    
    cur = 1
    curd = 1
    dn = 0
    
    arrow = gameboard.create_image(650, 200, anchor= "ne", image = downI)
    tdisp = gameboard.create_text(0, 0, anchor = "ne", text = '', fill = 'red') 
    
    gameboard.pack()
    gameboard.bind_all('<KeyRelease>', kp) 
    start = time.time()
    top.mainloop()
