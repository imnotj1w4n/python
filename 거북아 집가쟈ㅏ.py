import turtle
import random
p = random.randint(1,3)
print("%s"%p)
########집 만들기#########
t = turtle.Turtle('turtle')
t.write('완전멋진 지완이의 타자게임',font = ('Arial',10))
t.goto(0,0)
t.write('0',font = ('Arial',30))
t.goto(250,0)
t.write('50',font = ('Arial',30))
t.goto(500,0)##길
t.write('100',font = ('Arial',30))
t.goto(700,0)##바닥
t.goto(700,200)##벽
t.goto(500,200)##천장
t.goto(500,0)##벽
t.fillcolor("Black")
t.begin_fill()
t.goto(500,200)##지붕
t.goto(600,300)##지
t.goto(700,200)##붕
t.end_fill()
t.penup()
t.goto(0,0)
#######################

score = 0##점수
rate = 0##정확도 계산에 필요한 변수
nn= 5##몇번 입력하ㅕㄱ는가
n = ["배고프당","시큐브코딩","씨언어어려웡","태장중"]##단어모음
g = ["강아지","고양이"]
v = ["사과","바나나"]

##############(주제:아무거나)##################
if p==1:

 if nn == 5:
    i=random.choice(n)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

    
if nn == 4:
    i=random.choice(n)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn == 3:
    i=random.choice(n)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 2:
    i=random.choice(n)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 1:
    i=random.choice(n)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
     if a==i:
        score +=1

##############(주제:아무거나)##################
if p==2:

 if nn == 5:
    i=random.choice(v)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

    
if nn == 4:
    i=random.choice(v)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn == 3:
    i=random.choice(v)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 2:
    i=random.choice(v)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 1:
    i=random.choice(v)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
     if a==i:
        score +=1

##############(주제:아무거나)##################
if p==3:

 if nn == 5:
    i=random.choice(g)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

    
if nn == 4:
    i=random.choice(g)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn == 3:
    i=random.choice(g)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 2:
    i=random.choice(g)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
    if a==i:
        score +=1

if nn== 1:
    i=random.choice(g)
    a = turtle.textinput("i",'%s(%s//5)'%(i,score))
    nn-=1
    if a==i:
     t.forward(100)
     if a==i:
        score +=1

        
#################끝###############################3
t.goto (-100,0)
t.write('%s/5번 성공햇어용!'%score,font = ('Arial',30))
t.goto (-100,-50)
h = score*20
t.write('정확도:%d'%h,font = ('Arial',30))
t.goto (-100,-150)

if h==0:
    t.write('걍 노숙할게 ㅋㅋ',font = ('Arial',30))
    
if h==20:
    t.write('으악 너무 멀어!!! 그냥 등딱지에서 자야징 ㅋㅋ',font = ('Arial',30))
    
if h==40:
    t.write('엄......',font = ('Arial',30))
    
if h==60:
    t.write('이정도면 잘햇징ㅇㅇ',font = ('Arial',30))
    
if h==80:
    t.write('거의 다 왓는뎅 ㄲㅂ',font = ('Arial',30))
    
if h==100:
    t.write('도착!!',font = ('Arial',30))
################################################################## ######   #########
    
