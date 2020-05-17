import p5 as p

def setup():
    p.size(600, 600)
    p.rect_mode('CENTER')
    p.color_mode('HSB')


def draw():
    p.background(0)
    p.translate(20, 20)
    for x in range(30):
        for y in range(30):
            d = p.dist((30*x, 30*y), (mouse_x, mouse_y))
            p.fill(0.5*d, 255, 255)
            p.rect((30*x, 30*y), 25, 25)


if __name__ == '__main__':
    p.run()