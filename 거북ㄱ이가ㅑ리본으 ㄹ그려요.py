import turtle
t=turtle.Turtle()


t.speed(1)
t.rt(90)
stmp1 = t.stamp()
t.forward(30)
stmp2 = t.stamp()
t.forward(50)
t.undo()
t.clearstamp(stmp1)
t.penup()
t.goto(-20,0)
t.dot(10)
t.goto(20,0)
t.dot(10)
t.goto(15,-40)
t.rt(75)
t.pendown()
t.circle(-50,45)

turtle.done

