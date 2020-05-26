import p5 as p 

xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax-xmin
rangey = ymax-ymin

width = 600
height = 600

xscl = width/rangex
yscl = -height/rangey

transformation_matrix = [[0, -1], [1, 0]]

def setup():
    p.size(width, height)
    p.no_fill()

def draw():
    p.background(255)
    p.translate(width/2, height/2)
    grid(xscl, yscl)
    ang = p.remap(mouse_y, (0, width), (0, p.TWO_PI))
    rot_matrix = [[p.cos(ang), -p.sin(ang)], [p.sin(ang), p.cos(ang)]]
    newmatrix = transpose(multmatrix(rot_matrix, transpose(fmatrix)))
    graphPoints(fmatrix)
    p.stroke(255, 0, 0)
    graphPoints(newmatrix)

fmatrix = [[0, 0], [1, 0], [1, 2], [2, 2], [2, 3], [1, 3], [1, 4], [3, 4], [3, 5], [0, 5]]

def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        output.append([])
        for j in range(m):
            output[i].append(a[j][i])
    return output


def graphPoints(matrix):
    p.begin_shape()
    for pt in matrix:
        p.vertex(pt[0]*xscl, pt[1]*yscl)
    p.end_shape('CLOSE')


def grid(xscl, yscl):
    p.stroke_weight(1)
    p.stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        p.line((i*xscl, ymin*yscl), (i*xscl, ymax*yscl))
    for i in range(ymin, ymax+1):
        p.line((xmin*xscl, i*yscl), (xmax*xscl, i*yscl))
    p.stroke_weight(1)
    p.stroke(0, 255, 255)
    for i in range(xmin, xmax+1):
        p.line((i*xscl, ymin*yscl), (i*xscl, ymax*yscl))
    for i in range(ymin, ymax+1):
        p.line((xmin*xscl, i*yscl), (xmax*xscl, i*yscl))
    p.stroke(0)
    p.line((0, ymin*yscl), (0, ymax*yscl))
    p.line((xmin*xscl, 0), (xmax*xscl, 0))

def multmatrix(a, b):
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix 

if __name__ == '__main__':
    p.run()