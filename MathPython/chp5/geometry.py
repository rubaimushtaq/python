import p5 as p

width = 600
height = 600


def setup():
    p.rect_mode('CENTER')
    p.size(width, height)


t = 0


def draw():
    global t
    p.background(255)
    p.translate(width/2, height/2)
    p.rotate(p.radians(t))

    for _ in range(12):
        p.rotate(p.radians(360/12))
        with p.push_matrix():
            p.translate(200, 0)
            p.rotate(p.radians(t))
            p.rect((0, 0), 50, 50)

    t += 1


if __name__ == '__main__':
    p.run()
