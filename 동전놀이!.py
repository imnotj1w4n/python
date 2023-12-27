from tkinter import*
from random import*
win = Tk()

win.title("동전 맞ㅈ히기")



def click():
 
 coin = randint(0,1)

 if coin == 0:
        cc = PhotoImage(file = "f.png")
        
 else :
        cc = PhotoImage(file = "b.png")

## img_c['image'] = cc
## img_c.image = cc
 
## if (XD == 0 and coin == 0)or(XD == 1 and coin == 1):
##        lbl ['text'] = "정답!:D" 
## else :
##        lbl ['text'] = "틀렷당 :v"

cc = PhotoImage(file = "f.png")
basic_img = PhotoImage(file = 'ready.png')
lbl = Label(win,text = "")
btn_f = Button(win,text = "front",width = 20,command = click())
btn_b = Button(win,text = "back",width = 20,command = click())
img_c= Label(win,image = basic_img,relief = 'solid')

img_c.grid(row = 0,column = 0,columnspan = 2)
lbl.grid(row = 1,column = 0)
btn_f.grid(row = 2,column = 0)
btn_b.grid(row = 2,column = 1)

    
        
