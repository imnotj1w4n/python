from tkinter import*

pen_color = "black"
def paint(event):
    global pen_color
    x1,y1 = event.x ,event.y
    x2,y2 = x1 +5 ,y1+5
    canvas.create_line(x1,y1,x2,y2,width = 3,fill = pen_color)

    
def change_color(color):
    global pen_color
    pen_color = color
    
def clear_c():
    print(":D")
    
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
p= Button(win,text = "+",command = lambda:change_color("yellow"),bg="white")
m= Button(win,text = "-",command = lambda:change_color("yellow"),bg="white")
cl = Button(win,text = "X",bg="white",command = clear_c)
canvas.grid(row = 0,column = 0,columnspan=9)


wht.grid(row=1,column=0)
blk.grid(row=1,column=1)
blu.grid(row=1,column=2)
gre.grid(row=1,column=3)
yel.grid(row=1,column=4)
red.grid(row=1,column=5)
cl.grid(row=1,column=6)
p.grid(row=1,column=7)
m.grid(row=1,column=8)




win.bind("<B1-Motion>",paint)

win.mainloop()
