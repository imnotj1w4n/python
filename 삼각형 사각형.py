import turtle
t=turtle.Turtle()

t1 = (0,)
t2 = (50,150,200,175)

t.goto(t2[0],t1[0])
t.goto(t2[0],t2[0])
t.goto(t1[0],t2[0])
t.goto(t1[0],t1[0])

t.penup()

t.forward(t2[0])
t.forward(t2[0])
t.forward(t2[0])

t.pendown()

t.goto(t2[2],t1[0])
t.goto(t2[3],t2[0])
t.goto(t2[1],t1[0])



