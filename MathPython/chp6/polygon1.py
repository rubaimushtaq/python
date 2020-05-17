import p5 as p 

def setup():
    p.size(600, 600)

def draw():
    p.translate(width/2, height/2)
    polygon(3,100)

def polygon(sides, sz):
    p.begin_shape()
    for i in range(sides):
        step = p.radians(360/sides)
        p.vertex(sz*p.cos(i*step), sz*p.sin(i*step))
    p.end_shape('CLOSE')

if __name__ == '__main__':
    p.run()
