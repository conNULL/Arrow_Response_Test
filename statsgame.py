import tkinter
from tkinter import  Canvas
from tkinter import PhotoImage
import random
import time
import threading


def kp(event):
    global arrow
    gameboard.delete(arrow)
    if event.keysym == 'Up':
        if(check(0)):
            next()
        return

    if event.keysym == 'Down':
        if(check(1)):
            next()
        return    
        
    if event.keysym == 'Left':
        if(check(2)):
            next()
        return
        
    if event.keysym == 'Right':
        if(check(3)):
            next()
        return
        
def check(dir):
    global cur
    return (cur == dir)
def next():
    global cur
    global arrow
    global gameboard
    global start
    global tdisp
    global dn
    delays = [1, 3, 2.5, 1.7, 2.6, 5, 0.6, 1.1, 1.2, 2.4]
    
    fin = time.time()
    resp = round(fin - start, 3)
    gameboard.delete(tdisp)
    tdisp = gameboard.create_text(600, 600, anchor = "ne", text = resp, fill = 'red', font = ("Times", 50))
    gameboard.delete(arrow)
    n = random.randint(1, 3)
    cur = (cur + n) % 4
    gameboard.unbind_all('<KeyPress>')
    time.sleep(delays[dn])
    dn += 1
    gameboard.bind_all('<KeyPress>', kp)     
    if(cur == 0):    
        arrow = gameboard.create_image(650, 200, anchor= "ne", image = upI) 
    elif(cur == 1):    
        arrow = gameboard.create_image(650, 200, anchor= "ne", image = downI) 
    elif(cur == 2):    
        arrow = gameboard.create_image(650, 200, anchor= "ne", image = leftI) 
    elif(cur == 3):    
        arrow = gameboard.create_image(650, 200, anchor= "ne", image = rightI)   
        
    start = time.time()
    return
        
if  __name__ == "__main__":
    global arrow
    global cur
    global start 
    global tdisp  
    global dn
    top = tkinter.Tk()
    gameboard = Canvas(top, bg = "black", width = 1000, height = 750)
    downI = PhotoImage(file = "Down.png")
    cur = 1
    upI = PhotoImage(file = "Up.png")
    leftI = PhotoImage(file = "Left.png")
    rightI = PhotoImage(file = "Right.png")
    dn = 0
    arrow = gameboard.create_image(650, 200, anchor= "ne", image = downI)
   # gameboard.delete(down)
   
    tdisp = gameboard.create_text(0, 0, anchor = "ne", text = '', fill = 'red')   
    gameboard.pack()
    gameboard.bind_all('<KeyPress>', kp) 
    start = time.time()
    top.mainloop()
