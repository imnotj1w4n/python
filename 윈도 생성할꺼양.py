from tkinter import*

win = Tk()

List =["info","warning","error","questhead","hourglass","gray12"]

for i in range(7):
    lbl = Label(win,bitmap = List[i])
    lbl.pack(side = 'left')

win.mainloop()
