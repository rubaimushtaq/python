import p5 as p
import math as m

xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax-xmin
rangey = ymax-ymin

width = 600
height = 600


def setup():
    global xscl, yscl
    p.size(width, height)
    xscl = width/rangex
    yscl = -height/rangey


def draw():
    global xscl, yscl
    p.background(255)
    p.translate(width/2, height/2)
    grid(xscl, yscl)
    graphFunction()

def f(x):
    return m.sin(x)


def graphFunction():
        x=xmin
        while x<=xmax:
            p.stroke(255,0,0)
            p.fill(0)
            p.line((x*xscl,f(x)*yscl),((x+0.1)*xscl,f(x+0.1)*yscl))
            x+=0.1

def grid(xscl, yscl):
    p.stroke_weight(1)
    p.stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        p.line((i*xscl, ymin*yscl), (i*xscl, ymax*yscl))
    for i in range(ymin, ymax+1):
        p.line((xmin*xscl, i*yscl), (xmax*xscl, i*yscl))
    p.stroke_weight(1)
    p.stroke(0, 255, 255)
    for i in range(xmin, xmax+1):
        p.line((i*xscl, ymin*yscl), (i*xscl, ymax*yscl))
    for i in range(ymin, ymax+1):
        p.line((xmin*xscl, i*yscl), (xmax*xscl, i*yscl))
    p.stroke(0)
    p.line((0, ymin*yscl), (0, ymax*yscl))
    p.line((xmin*xscl, 0), (xmax*xscl, 0))
    
    
    

if __name__ == '__main__':
    p.run()
