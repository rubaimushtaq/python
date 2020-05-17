import p5 as p

width = 600
height = 600

def setup():
    p.size(width, height)
    
t = 0

def draw():
    global t
    p.background(255)
    p.translate(width/2, height/2)
    p.rotate(p.radians(t))
    for _ in range(12):
        p.rect((200, 0),50, 50)
        p.rotate(p.radians(360/12))
    t += 2

if __name__ == '__main__':
    p.run()
