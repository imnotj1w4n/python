from tkinter import*

win = Tk()

def click():
    lbl['text'] = "my name is"+ ent1.get()+"and i'm"+ent2.get()+"years old"  






btn = Button (win,text = " 자기소개 끋",command = click) 
ent1 = Entry(win)
ent2 = Entry(win)
ent1.bind("<Return>")
ent2.bind("<Return>")
lbl = Label(win,text="나는 자기소개ㅡㄹ 하는 그 머시기다 이름이랑 나이를 적아라")

ent1.pack()
ent2.pack()
lbl.pack()
btn.pack()

