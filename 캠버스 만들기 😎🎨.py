from tkinter import*
s=0
pensize=2

pen_color = "black"
def paint(event):
    global pen_color
    global pensize
    x1,y1 = event.x ,event.y
    x2,y2 = x1 +5 ,y1+5
    canvas.create_line(x1,y1,x2,y2,width = pensize,fill = pen_color)


def sizeup():
   global pensize
   pensize=pensize+2
def sized():
    global pensize
    pensize-=2
   
##    
##c_color = "white"

def change_color(color):
    global pen_color

    pen_color = color
   

def clear_c():
    canvas.delete("all")

def mod(cm):
    if cm == "pen":
        s=1
    if cm == "canvas":
        s=2

win = Tk()
win.title("캠버스 :D")
win.geometry("500x500+200+200")
canvas = Canvas(win,bg = "white",width = 500,height = 475)

red = Button(win,text = "red",fg="white",command = lambda:change_color("red"),bg="red")
wht = Button(win,text = "white",command = lambda:change_color("white"),bg="white")
blk = Button(win,text = "black",fg="white",command = lambda:change_color("black"),bg="black")
blu = Button(win,text = "blue",fg="white",command = lambda:change_color("blue"),bg="blue")
gre= Button(win,text = "green",fg="white",command = lambda:change_color("green"),bg="green")
yel= Button(win,text = "yellow",command = lambda:change_color("yellow"),bg="yellow")
p= Button(win,text = "+",command = lambda:sizeup(),bg="white")
m= Button(win,text = "-",command = lambda:sized(),bg="white")
cl = Button(win,text = "X",bg="white",command = clear_c)
canvas.grid(row = 0,column = 0,columnspan=9)
##ps=Button(win,text = "pen_color",bg = pen_color,command = lambda:mod("pen"))
##cs=Button(win,text = "canvas_color",bg = c_color,command = lambda:mod("canvas"))

wht.grid(row=1,column=0)
blk.grid(row=1,column=1)
blu.grid(row=1,column=2)
gre.grid(row=1,column=3)
yel.grid(row=1,column=4)
red.grid(row=1,column=5)
cl.grid(row=1,column=6)
p.grid(row=1,column=7)
m.grid(row=1,column=8)
##ps.grid(row=1,column=9)
##cs.grid(row=1,column=10)




win.bind("<B1-Motion>",paint)

win.mainloop()
