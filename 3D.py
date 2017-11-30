from tkinter import*
from math import*

win = Tk()

#win.attributes("-alpha", 0)



def call(event):
    canvas.focus_set()
    global prev
    prev = event.x
    print ("Cliked at " + str(event.x) + ' ' + str(event.y))

def drag(event1):
    ep = float(event1.x)
    global prev
    before = prev
    if(before > ep):
        print('Left Drag recorded ' + str(before - ep))
        global d, e, f
        canvas.delete(d, e, f)
        theta = (3.14/180)*(before - ep)*(float(53/250))
        if((before - ep)<250):
            f = canvas.create_oval((150 - 200*sin(theta)) + 150 *(1 - cos(theta)), 150, (350 - (350 *(1 - cos(theta))) - 200*sin(theta)), 350, fill = "yellow")
            e = canvas.create_oval((150 - 100*sin(theta) + 150 *(1 - cos(theta))), 150, (350 - (350 *(1 - cos(theta))) - 100*sin(theta)), 350, fill = "red")
            d = canvas.create_oval((150 + (150 *(1 - cos(theta) ))), 150, (350 - (350 *(1 - cos(theta) ))), 350, fill = "blue")
        elif((before - ep)>250):
            d = canvas.create_oval((150 + (150 *(1 - cos(theta) ))), 150, (350 - (350 *(1 - cos(theta) ))), 350, fill = "blue")
            e = canvas.create_oval((150 - 100*sin(theta) + 150 *(1 - cos(theta))), 150, (350 - (350 *(1 - cos(theta))) - 100*sin(theta)), 350, fill = "red")
            f = canvas.create_oval((150 - 200*sin(theta)) + 150 *(1 - cos(theta)), 150, (350 - (350 *(1 - cos(theta))) - 200*sin(theta)), 350, fill = "yellow")


    else:
        print('Right Drag recorded' + str(ep - before))
        canvas.delete(d, e, f)
        theta = (ep - before)*(float(53/250))
        if((ep - before)<250):
            f = canvas.create_oval((150 + 200*sin(float(3.14/180)*theta) + 150 *(1 - cos(float(3.14/180)*theta))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta))) + 200*sin(float(3.14/180)*theta)), 350, fill = "yellow")
            e = canvas.create_oval((150 + 100*sin(float(3.14/180)*theta) + 150 *(1 - cos(float(3.14/180)*theta))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta))) + 100*sin(float(3.14/180)*theta)), 350, fill = "red")
            d = canvas.create_oval((150 + (150 *(1 - cos(float(3.14/180)*theta) ))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta) ))), 350, fill = "blue")
        elif((ep - before)>250):
            d = canvas.create_oval((150 + (150 *(1 - cos(float(3.14/180)*theta) ))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta) ))), 350, fill = "blue")
            e = canvas.create_oval((150 + 100*sin(float(3.14/180)*theta) + 150 *(1 - cos(float(3.14/180)*theta))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta))) + 100*sin(float(3.14/180)*theta)), 350, fill = "red")
            f = canvas.create_oval((150 + 200*sin(float(3.14/180)*theta) + 150 *(1 - cos(float(3.14/180)*theta))), 150, (350 - (350 *(1 - cos(float(3.14/180)*theta))) + 200*sin(float(3.14/180)*theta)), 350, fill = "yellow")

   
def setxf(event):
    global prev
    prev = event.x

canvas = Canvas(win, width = 500, height = 500)
canvas.pack()
canvas.bind("<Button-1>", call)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", setxf)
'''c = canvas.create_oval(150, 150, 350, 350, fill = "blue")
l = canvas.create_oval(247, 247, 253, 253, fill = "white")
ch = input("")
canvas.delete(c)'''

f = canvas.create_oval(150, 150, 350, 350, fill = "yellow")
e = canvas.create_oval(150, 150, 350, 350, fill = "red")
d = canvas.create_oval(150, 150, 350, 350, fill = "blue")
l = canvas.create_oval(247, 247, 253, 253, fill = "white")
'''ch = input("")
canvas.delete(d, e, f)

f = canvas.create_oval(150, (150 - 200*sin(float(3.14/180)*10) + 150 *(1 - cos(float(3.14/180)*10))), 350, (350 - (350 *(1 - cos(float(3.14/180)*10))) - 200*sin(float(3.14/180)*10)), fill = "yellow")
e = canvas.create_oval(150, (150 - 100*sin(float(3.14/180)*10) + 150 *(1 - cos(float(3.14/180)*10))), 350, (350 - (350 *(1 - cos(float(3.14/180)*10))) - 100*sin(float(3.14/180)*10)), fill = "red")
d = canvas.create_oval(150, (150 + (150 *(1 - cos(float(3.14/180)*10) ))), 350,  (350 - (350 *(1 - cos(float(3.14/180)*10) ))), fill = "blue")
l = canvas.create_oval(247, 247, 253, 253, fill = "white")
'''
win.mainloop()
