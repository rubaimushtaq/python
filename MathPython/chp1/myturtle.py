import turtle


t = turtle.Turtle()
t.shape('turtle')
t.speed(0)
t.clear()


def square(x=100):
    for _ in range(4):
        t.fd(x)
        t.right(90)


def squareCircle():
    for _ in range(60):
        square(50)
        t.right(5)


def triangle(y=100):
    for _ in range(3):
        t.forward(y)
        t.right(120)


def star(z=100):
    for _ in range(5):
        t.fd(z)
        t.left(144)


input('')
