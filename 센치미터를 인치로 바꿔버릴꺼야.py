from tkinter import*

win = Tk()

def haha(event) :
    lbl['text'] = int(ent.get())*39/100








lbl = Label(win,text = "inch")
ent = Entry(win)
ent.bind("<Return>",haha)

ent.pack()
lbl.pack()
