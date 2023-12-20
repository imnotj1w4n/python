from tkinter import*

win = Tk()
def message(event) :
    lbl['text'] = int(lbl['text']) + int(entry.get())
    entry.delete(0,END)
def Click():
    lbl ['text'] = 0
    
entry = Entry(win)
entry.bind("<Return>",message)
lbl = Label(win,text = "")
lbl.pack()
entry.pack()
btn = Button(win,text = "지워버려@!",command = Click)
btn.pack()
win.mainloop()
