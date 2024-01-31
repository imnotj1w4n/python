from tkinter import*

win = Tk()
canvas =  Canvas(win,bg = "white",width = 570,height = 570)
canvas.pack()

canvas.create_line(500,50,500,500,fill = "red",width = 5)
canvas.create_line(50,50,50,500,fill = "red",width = 5)
canvas.create_line(100,50,100,500,fill = "red",width = 5)
canvas.create_line(150,50,150,500,fill = "red",width = 5)
canvas.create_line(200,50,200,500,fill = "red",width = 5)
canvas.create_line(250,50,250,500,fill = "red",width = 5)
canvas.create_line(300,50,300,500,fill = "red",width = 5)
canvas.create_line(350,50,350,500,fill = "red",width = 5)
canvas.create_line(400,50,400,500,fill = "red",width = 5)
canvas.create_line(450,50,450,500,fill = "red",width = 5)

canvas.create_line(50,50,500,50,fill = "blue",width = 5)
canvas.create_line(50,100,500,100,fill = "blue",width = 5)
canvas.create_line(50,150,500,150,fill = "blue",width = 5)
canvas.create_line(50,200,500,200,fill = "blue",width = 5)
canvas.create_line(50,250,500,250,fill = "blue",width = 5)
canvas.create_line(50,300,500,300,fill = "blue",width = 5)
canvas.create_line(50,350,500,350,fill = "blue",width = 5)
canvas.create_line(50,400,500,400,fill = "blue",width = 5)
canvas.create_line(50,450,500,450,fill = "blue",width = 5)
canvas.create_line(50,500,500,500,fill = "blue",width = 5)

win.mainloop()
