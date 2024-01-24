##사진첨 만들기!우호와앙ㅇ✨✨✨📸 

#---------------------#
from tkinter import*
win = Tk()
win.title("완전멋진 사진첩 지존이다")
listbox = Listbox(win)
from datetime import datetime
#---------------------#

class Gallery :
    def _init_(self,listbox,lbl_imfo,file_name) :
        self.listbox = listbox
        self.lbl_img = lbl_img
        self.lbl_info = lbl_info
        self.file_name = file_name
        #
        f = open(self.file_name,'r',encoding = "UTF8")
        data = f.readlines()
        for line in data :
            ing_name  = line.split(',')
            self.listbox.insert(END,img_name[0])
            f.close()
            
        def img_insert(self,text_box) :
            self.data = datatime.today()strtime("%Y/%M/%D:%H:%M:%S")
            f = open(self.file_name,'a',encoding="UTF8")
            photo_info = text_box.get('1.0',END)
            f.write("%s,%s\n"%(photo_info[:-1],self.data))
            title = photo_info.split('.')
            self.listbox.insert(END,title[0])
            f.close()
            text_box.delete('1,0',END)



    
img = PhotoImage(file = "basic.png")
img_lbl = Label(win,image = img,width = 500,height = 300,relief="solid")
info_lbl = Label(win,text = " ",width = 45,height = 10,bg = "black",fg = "white")
guide_lbl = Label(win,text = "파일명과 메모를\n쉼표(,)로 구분지어 작성한 후\nsave 버튼을 눌러 클릭하세요",
                            width = 45,height = 10,bg = "yellow",fg = "red")
img_list = Listbox(win,width = 50,height = 20)
text_box = Text(win,width = 30,height = 15 )
save_btn = Button(win,text = "save",bg = "yellow",fg = "red",command = lambda: setImg.img_insert(text_box))

img_lbl.grid(row = 0,column = 0)
info_lbl.grid(row = 1,column = 0,columnspan = 3)
guide_lbl.grid(row = 1,column=1,columnspan = 2)
img_list.grid(row = 0,column=1,columnspan = 2)
text_box.grid(row = 2,column=1)
save_btn.gride(row = 2,column=2)


listbox.pack()
win.mainloop()
























































##for i in range(10) :
##    listbox.insert(i, str(i))
##print(listbox.curselection())
##print(listbox.get(0, 9))
##listbox.pack()
##win.mainloop()

    ##코드나뉴기(오늘은 멋지다)##

##def double_click(event) :
##    index = listbox.curselection()
##    print("today:",listbox.get(index[0]))
##
##def left_click(event) :
##    index = listbox.curselection()
##    if index :
##        if index[0] == 0 :
##            print("yesterday :Sun")
##        else :
##            print("yesterday :", listbox.get(index[0]-1))
##
##def right_click(event) :
##    index = listbox.curselection()
##    if index :
##        if index[0] == 6:
##            print("Tomorrow : mon")
##        else :
##            print("tomorrow:",listbox.get(index[0]+1))
##
##day = ["mon","tue","w","thu","fri","sat","sun"]
##
##for i in range(7):
##    listbox.insert(i, day[i])
##
##listbox.bind("<Double-Button-1>",double_click)
##listbox.bind("<Button-1>",left_click)
##listbox.bind("<Button-3>",right_click)

   ##코드나뉴기(꽃)##

##def double_click(event) :
##    index = listbox.curselection()
##    lbl['text'] = listbox.get(index[0])
##
##flower = ["rose","lily","pansy","sunflower"]
##lbl= Label(win,text = "",bg = "pink",fg = "blue")
##for i in range(4):
##    listbox.insert(i, flower[i])
##
##listbox.bind("<Double-Button-1>",double_click)
##lbl.pack()
   ##코드나뉴기##

##from datetime import datetime
##print(datetime.today())
##print(datetime.now())

                                        
