import p5 as p
from numpy import arange

xmin = -2
xmax = 2

ymin = -2
ymax = 2

rangex = xmax-xmin
rangey = ymax-ymin

width = 600
height = 600

xscl = width/rangex
yscl = -height / rangey

def setup():
    p.size(width, height)
    p.color_mode('HSB')
    p.no_stroke()

def draw():
    p.translate(width/2, height/2)
    for x in arange(xmin, xmax, .01): 
        for y in arange(ymin, ymax, .01):
            z = [x, y]
            col = mandelbrot(z, 100)
            if col == 100:
                p.fill(0)
            else:
                p.fill((255-15*col), 255, 255)
            p.rect((x*xscl, y*yscl), 1, 1)


def mandelbrot(z, num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1 = cAdd(cMult(z1, z1), z)
        count += 1
    return num


def cAdd(a, b):
    return(a[0]+b[0], a[1]+b[1])


def cMult(u, v):
    return [u[0]*v[0]-u[1]*v[1], u[1]*v[0]+u[0]*v[1]]


def magnitude(z):
    return p.sqrt(z[0]**2+z[1]**2)


if __name__ == '__main__':
    p.run()
