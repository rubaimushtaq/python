import p5 as p

width = 600
height = 600


def setup():
    p.size(width, height)
    p.no_stroke()
    p.no_loop()


def draw():
    p.background(255)
    p.translate(width/2, height/2)
    points = []
    t = 0
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01
    for i, s in enumerate(points):
        p.stroke_weight(0.01)
        p.stroke(255, 0, 0)
        if i < len(points)-1:
            p.line((s[0], s[1]), (points[i+1][0], points[i+1][1]))


def harmonograph(t):
    a1 = a2 = a3 = a4 = 100
    f1, f2, f3, f4 = 2.01, 3, 3, 2
    p1, p2, p3, p4 = -p.PI/2, 0, -p.PI/16, 0
    d1, d2, d3, d4 = 0.00085, 0.0065, 0, 0
    x = a1*p.cos(f1*t+p1)*p.exp(-d1*t) + a3*p.cos(f3*t+p3)*p.exp(-d3*t)
    y = a2*p.sin(f2*t + p2)*p.exp(-d2*t) + a4*p.sin(f4*t+p4)*p.exp(-d4*t)
    return[x, y]


if __name__ == '__main__':
    p.run()
