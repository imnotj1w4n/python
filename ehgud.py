from tkinter import*

win = Tk()
canvas =  Canvas(win,bg = "white",width = 550,height = 550)
canvas.pack()

canvas.create_line(500,50,500,500,fill = "black",width = 5)
canvas.create_line(50,50,50,500,fill = "black",width = 5)
canvas.create_line(100,50,100,500,fill = "black",width = 5)
canvas.create_line(150,50,150,500,fill = "black",width = 5)
canvas.create_line(200,50,200,500,fill = "black",width = 5)
canvas.create_line(250,50,250,500,fill = "black",width = 5)
canvas.create_line(300,50,300,500,fill = "black",width = 5)
canvas.create_line(350,50,350,500,fill = "black",width = 5)
canvas.create_line(400,50,400,500,fill = "black",width = 5)
canvas.create_line(450,50,450,500,fill = "black",width = 5)

canvas.create_line(50,50,500,50,fill = "black",width = 5)
canvas.create_line(50,100,500,100,fill = "black",width = 5)
canvas.create_line(50,150,500,150,fill = "black",width = 5)
canvas.create_line(50,200,500,200,fill = "black",width = 5)
canvas.create_line(50,250,500,250,fill = "black",width = 5)
canvas.create_line(50,300,500,300,fill = "black",width = 5)
canvas.create_line(50,350,500,350,fill = "black",width = 5)
canvas.create_line(50,400,500,400,fill = "black",width = 5)
canvas.create_line(50,450,500,450,fill = "black",width = 5)
canvas.create_line(50,500,500,500,fill = "black",width = 5)

canvas

canvas.create_polygon(275,100,100,450,450,450,fill = "black")
