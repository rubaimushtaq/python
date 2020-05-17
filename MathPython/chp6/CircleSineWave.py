import p5 as p

r1 = 100
r2 = 10
t = 0
circleList = []

def setup():
    p.size(600, 600)

def draw():
    global t, circleList
    p.background(200)
    p.translate(width/4, height/2)
    p.no_fill()
    p.stroke(0)
    p.ellipse((0, 0), 2*r1, 2*r1)
    p.fill(255, 0,0)
    y = r1*p.sin(t)
    x = r1*p.cos(t)
    circleList = [y] + circleList[:249]
    p.ellipse((x, y), r2, r2)
    p.stroke(0,255,0)
    p.line((x, y),(200, y))
    p.fill(0,255,0)
    p.ellipse((200,y), 10, 10)
    for i,c in enumerate(circleList):
        p.ellipse((200+i, c), 15, 15)
    t += 0.1

if __name__ == '__main__':
    p.run()