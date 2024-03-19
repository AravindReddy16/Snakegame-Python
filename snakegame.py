from turtle import *
import random
a=700.00
b=600.00
setup(a,b)
l=[]
s=Turtle()
f=s.clone()
g=s.clone()
o=s.clone()
g.hideturtle()
f.hideturtle()
o.hideturtle()
bgcolor('blue')
s.color('red')
s.shape('square')
s.speed(0)
f.color('green')
f.shape('circle')
f.speed(0)
g.penup()
g.speed(0)
s.penup()
o.penup()
x=Vec2D(a-360,b-310)
y=Vec2D(-(a-360),-(b-310))
def score():
    g.goto(-340,270)
    g.color('black')
    g.write(arg=f'score: {len(l)-1}',align='left',font=('arial',15,'normal'))
def feed():
    x=random.randint(-270,270)
    y=random.randint(-270,270)
    f.penup()
    f.goto(x,y)
    i=f.stamp()
    l.append(i)
    g.clear()
    s.shapesize(stretch_len=len(l))
def move():
    while True:
        s.forward(5)
        m=f.pos()[0]
        n=f.pos()[1]
        if (s.pos()[0]>=(m-18) and s.pos()[0]<=(m+18)) and (s.pos()[1]>=(n-18) and s.pos()[1]<=(n+18)):
            f.clearstamp(l[-1])
            feed()
        if s.pos()[0]>=x[0] or s.pos()[1]>=x[1] or s.pos()[0]<=y[0] or s.pos()[1]<=y[1]:
            o.write(arg=f'Game Over',align='center',font=('arial',30,'normal'))
            break
        score()
def upside():
    s.setheading(90)
def downside():
    s.setheading(270)
def right():
    s.setheading(360)
def left():
    s.setheading(180)
listen()
onkey(upside,'w')
onkey(downside,'s')
onkey(right,'d')
onkey(left,'a')
feed()
move()
mainloop()