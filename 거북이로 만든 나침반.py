import turtle
t = turtle.Turtle('turtle')
t.penup()
t.setx(200)
t.write('동',font=('Arial,30'))
t.setx(-200)
t.write('서',font=('Arial,30'))
t.setx(0)
t.sety(-200)
t.write('남',font=('Arial,30'))
t.sety(200)
t.write('북',font=('Arial,30'))
t.goto(0, 0)
t.pendown()
t.pencolor('blue')
a = turtle.textinput('','방향을 입력해 주세요')
t.speed(1)

if a == '동':
    t.goto(200,0)
    
if a == '서':
    t.goto(-200,0)
    
if a == '남':
    t.goto(0,200)
    
if a == '북':
    t.goto(0,-200)

else :
    t.rt(360)
