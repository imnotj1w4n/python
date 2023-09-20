import turtle
r=input()
n=input()
n=int(n)
r=int(r)
t=turtle.Turtle()
t.shape("turtle")
t.circle(r,n)
st1=t.stamp()
t.circle(r,n)
st2=t.stamp()
t.circle(r,n)
st3=t.stamp()
t.circle(r,n)

st4=t.stamp()
t.clearstamp(st1)
t.clearstamp(st3)

##turtle.done()
##
