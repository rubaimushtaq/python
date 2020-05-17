import p5 as p

r1 = 300.0
r2 = 175.0
r3 = 5.0
x1 = 0
y1 = 0

width = 600
height = 600

points = []

prop = 0.9

t = 0


def setup():
    p.size(width, height)


def draw():
    global r1, r2, x1, y1, t, prop, points
    p.translate(width/2, height/2)
    p.background(255)
    p.no_fill()
    p.stroke(0)
    p.ellipse((x1, y1), 2*r1, 2*r1)
    x2 = (r1-r2)*p.cos(t)
    y2 = (r1 - r2)*p.sin(t)
    p.ellipse((x2, y2), 2*r2, 2*r2)
    x3 = x2 + prop*(r2-r3)*p.cos(-((r1-r2)/r2)*t)
    y3 = y2 + prop*(r2 - r3)*p.sin(-((r1-r2)/r2)*t)
    p.fill(255, 0, 0)
    p.ellipse((x3, y3), 2*r3, 2*r3)
    points = [[x3 ,y3]] + points[:2000]
    for i,d in enumerate(points):
        if i < len(points)-1:
            p.stroke(255,0,0)
            p.line((d[0], d[1]), (points[i+1][0], points[i+1][1]))
    t += 0.1


if __name__ == '__main__':
    p.run()
