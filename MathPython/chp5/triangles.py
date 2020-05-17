import p5 as p
import math as m

def setup():
    p.size(600, 600)
    p.rect_mode('CENTER')

t = 0

def draw():
    global t
    p.background(255)
    p.translate(width/2, height/2)
    for i in range(90):
        p.rotate(p.radians(360/90))
        with p.push_matrix():
            p.translate(200, 0)
            p.rotate(p.radians(t+2*i*360/90))
            tri(100)
        t+=0.01

def tri(length):
    p.no_fill()
    p.triangle((0, -length),(-length*m.sqrt(3)/2, length/2),(length*m.sqrt(3)/2, length/2))

if __name__ == '__main__':
    p.run()