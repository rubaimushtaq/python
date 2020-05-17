import p5 as p

def setup():
    p.size(600, 600)


def draw():
    p.line((1, 0), (40, 50))
    p.ellipse((400, 400), 100, 20)

if __name__ == '__main__':
    p.run()
