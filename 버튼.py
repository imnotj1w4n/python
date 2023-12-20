from tkinter import*

win = Tk()
lbl = Label(win,text = "hello",fg = 'white',bg = 'yellow')
def click() :
    
 if lbl['text'] == "hello":
    lbl['text']="python"
    lbl['bg'] = 'green'
 else :
     lbl['text'] = "hello"
     lbl['bg'] = "yellow" 




btn = Button(win, text = "버튼이다",command=click)
lbl.pack()
btn.pack()
win.mainloop()
 
