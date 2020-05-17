def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def average(a, b):
    return (a + b)/2.0


def guess():
    lower = -1.0
    upper = 0.0
    for _ in range(20):
        midpt = average(lower, upper)
        if (midpt == 0.0):
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt

    return midpt


x = guess()

print(x, f(x))
