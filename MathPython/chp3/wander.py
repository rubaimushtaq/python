import turtle
from random import randint

t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.clear()

def wander():
    while True:
        t.fd(3)
        if t.xcor()>=200 or t.xcor()<=-200 or t.ycor()<=-200 or t.ycor()>=200:
            t.lt(randint(90,180))

wander()

input('')
