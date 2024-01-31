##사진첨 만들기!우호와앙ㅇ✨✨✨📸 

#---------------------#
from tkinter import*
from datetime import datetime
#---------------------#

class Gallery :
    def __init__(self,listbox,lbl_img,lbl_info,file_name) :
        self.listbox = listbox
        self.lbl_img = lbl_img
        self.lbl_info = lbl_info
        self.file_name = file_name
        #
        f = open(self.file_name,'r',encoding = "UTF8")
        data = f.readlines()
        for line in data :
            img_name  = line.split(',')
            self.listbox.insert(END,img_name[0])
            f.close()
            
        def img_insert(self,text_box) :
            self.data = datatime.today().strftime("%Y/%M/%D:%H:%M:%S")
            f = open(self.file_name,'a',encoding="UTF8")
            photo_info = text_box.get('1.0',END)
            f.write("%s,%s\n"%(photo_info[:-1],self.data))
            title = photo_info.split('.')
            self.listbox.insert(END,title[0])
            f.close()
            text_box.delete('1,0',END)
        def img_show(self,event):
            index = self.listbox.curseletion()
            photoname = self.listbox.get(index[0])
            img = Photoimage(file = ghotoname)
            self.lbl_img['image'],self.lbl_img.image = img,img

            f = open(self.file_name,'r',encoding = "UTF8")
            data =f.readlines()
            line = line.split(',')
            if line[0] == photoname:
                    if len(line[1]>=10):
                        str_len = len(line[1])
                        str_line = str_len//10
                        count,index,memo = 0,0,
                        while count <= str_line:
                            if count < str_line:
                                    memo +=line[1][index :index + 10]+'\n'
                                    index +=10
                            else:
                                memo += line[1][index:]
                            count +=1
                    else:
                        memo = line[1]
                        
                    self.string = "File name %s\nMemo:%s\n data:%s"%(line[0],memo,line[2])
                    self.lbl_info['text'] = self.string
                    f.close()
win = Tk()
win.title("완전멋진 사진첩 지존이다")
listbox = Listbox(win)
file_name = "자연.txt"

img = PhotoImage(file = "basic.png")
img_lbl = Label(win,image = img,width = 500,height = 300,relief="solid")
info_lbl = Label(win,text = " ",width = 45,height = 10,bg = "black",fg = "white")
guide_lbl = Label(win,text = "파일명과 메모를\n쉼표(,)로 구분지어 작성한 후\nsave 버튼을 눌러 클릭하세요",
                            width = 45,height = 10,bg = "yellow",fg = "red")
img_list = Listbox(win,width = 50,height = 20)
text_box = Text(win,width = 30,height = 15 )
save_btn = Button(win,text = "save",bg = "yellow",fg = "red",command = lambda: img_insert(text_box))

gallery = Gallery(img_list,img_lbl,info_lbl,file_name)

img_lbl.grid(row = 0,column = 0)
info_lbl.grid(row = 1,column = 0,columnspan = 3)
guide_lbl.grid(row = 1,column=1,columnspan = 2)
img_list.grid(row = 0,column=1,columnspan = 2)
text_box.grid(row = 2,column=1)
save_btn.grid(row = 2,column=2)


listbox.grid(row = 2,column = 2)
win.mainloop()
 



