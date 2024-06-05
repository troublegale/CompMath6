from numpy import exp, sin, cos


def f1(x, y):
    return y + (1 + x) * y ** 2


def y1(x, x0, y0):
    return -exp(x) / (x * exp(x) - (x0 * exp(x0) * y0 + exp(x0)) / y0)


def f2(x, y):
    return x + y


def y2(x, x0, y0):
    return exp(x - x0) * (y0 + x0 + 1) - x - 1


def f3(x, y):
    return sin(x) - y


def y3(x, x0, y0):
    return (2 * exp(x0) * y0 - exp(x0) * sin(x0) + exp(x0) * cos(x0)) / (2 * exp(x)) + (sin(x)) / 2 - (cos(x)) / 2
