import turtle
import random
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
score = 0
rate = 0
nn= 5
n = ["배고프당","시큐브코딩","씨언어어려웡","태장중"]


#######게임##################
if
i=random.choice(n)
a = turtle.textinput("i",'%s(%s//5)'%(i,score))
nn=-1
if a==i:
 t.forward(100)
score =+1
###########################
