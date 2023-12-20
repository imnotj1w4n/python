from tkinter import*

win = Tk()
img = PhotoImage(file = 'pizza.png')
lbl2 = Label(win, text = "pizza",fg = "red",bg= "yellow")
lbl = Label(win,image = img)
lbl.pack()
lbl2.pack()
win.mainloop()
