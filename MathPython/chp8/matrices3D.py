import p5 as p

xmin = -5
xmax = 5

ymin = -5
ymax = 5

rangex = xmax-xmin
rangey = ymax-ymin

width = 600
height = 600

xscl = width/rangex
yscl = -height/rangey



def setup():
    p.size(width, height)
    p.no_fill()
    


def draw():
    p.background(0)
    p.translate(width/2, height/2)
    # grid(xscl, yscl)

    rot = p.remap(mouse_x, (0, width), (0, p.TWO_PI))
    tilt = p.remap(mouse_y, (0, height), (0, p.TWO_PI))
    rot_matrix = rottilt(rot, tilt)
    
    newmatrix = multmatrix(fmatrix, rot_matrix)
    
    p.no_fill()
    p.stroke_weight(2)
    p.stroke(255, 0, 0)
    graphPoints2(newmatrix, edges)

fmatrix = [
    [0, 0, 0], [1, 0, 0], [1, 2, 0], [2, 2, 0], [2, 3, 0], [1, 3, 0], [1, 4, 0],
    [3, 4, 0], [3, 5, 0], [0, 5, 0], [0, 0, 1], [1, 0, 1], [1, 2, 1], [2, 2, 1],
    [2, 3, 1], [1, 3, 1], [1, 4, 1], [3, 4, 1], [3, 5, 1], [0, 5, 1]
]

edges = [
    [0, 1], [1, 2], [2, 3],
    [3, 4], [4, 5], [5, 6],
    [6, 7], [7, 8], [8, 9],
    [9, 0], [10, 11], [11, 12],
    [12, 13], [13, 14], [14, 15],
    [15, 16], [16, 17], [17, 18],
    [18, 19], [19, 10], [0, 10],
    [1, 11], [2, 12], [3, 13],
    [4, 14], [5, 15], [6, 16],
    [7, 17], [8, 18], [9, 19]
]

transformation_matrix = [[0, -1], [1, 1]]

def graphPoints(matrix):
    p.begin_shape()
    for pt in matrix:
        p.vertex(pt[0]*xscl, pt[1]*yscl)
    p.end_shape('CLOSE')

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

def rottilt(rot, tilt):
    rotmatrix_Y = [[p.cos(tilt), 0.0, p.sin(tilt)],
                   [0.0, 1.0, 0.0],
                   [-p.sin(tilt), 0.0, p.cos(tilt)]]
    rotmatrix_X = [[1.0, 0.0, 0.0], 
                   [0.0, p.cos(rot), p.sin(rot)],
                   [0.0, -p.sin(rot), p.cos(rot)]
    ]
    return multmatrix(rotmatrix_X, rotmatrix_Y)

def graphPoints2(pointList, edges):
    for e in edges:
        p.line((pointList[e[0]][0]*xscl, pointList[e[0]][1]*yscl),
             (pointList[e[1]][0]*xscl, pointList[e[1]][1]*yscl))

def grid(xscl, yscl):
    p.stroke_weight(1)
    p.stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        p.line((i*xscl, ymin*yscl), (i*xscl, ymax*yscl))
    for i in range(ymin, ymax+1):
        p.line((xmin*xscl, i*yscl), (xmax*xscl, i*yscl))
    p.stroke(0)
    p.line((0, ymin*yscl), (0, ymax*yscl))
    p.line((xmin*xscl, 0), (xmax*xscl, 0))

if __name__ == '__main__':
    p.run()
