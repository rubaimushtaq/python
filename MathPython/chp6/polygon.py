import p5 as p


def setup():
    p.size(600, 600)


def draw():
    p.translate(width/2, height/2)
    p.begin_shape()
    for i in range(6):
        p.vertex(100*p.cos(p.radians(60*i)), 100*p.sin(p.radians(60*i)))
        p.rotate(p.radians(60))
    p.end_shape('CLOSE')


if __name__ == '__main__':
    p.run()