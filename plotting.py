import matplotlib.pyplot as plt


def draw_plot(xs, ys, func, x0, y0, name, dx=0.01):
    plt.title(name)
    xss, yss = [], []
    a = xs[0]
    b = xs[-1]
    a -= dx
    b += dx
    x = a
    while x <= b:
        xss.append(x)
        yss.append(func(x, x0, y0))
        x += dx
    plt.plot(xss, yss, 'g')
    for i in range(len(xs)):
        plt.scatter(xs[i], ys[i], c='r')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()
