from plotting import draw_plot


def solve(f, xs, x0, y0, exact_y, eps):
    print()
    methods = [("Modified Euler", improved_euler_method),
               ("4th order Runge-Kutta", fourth_order_runge_kutta_method),
               ("Milne", milne_method)]

    for name, method in methods:
        print(name + ":")

        ys = method(f, xs, y0, eps)
        print("y:\t[", *map(lambda x: round(x, 5), ys), "]")
        print("y_exact:\t[", *map(lambda x: round(exact_y(x, x0, y0), 5), xs), "]")

        if method is milne_method:
            inaccuracy = max([abs(exact_y(x, x0, y0) - y) for x, y in zip(xs, ys)])
            print(f"Error (max|y_iexact - y_i|): {inaccuracy}")
        else:
            xs2 = []
            for x1, x2 in zip(xs, xs[1:]):
                xs2.extend([x1, (x1 + x2) / 2, x2])
            ys2 = method(f, xs2, y0, eps)

            p = 4 if method is fourth_order_runge_kutta_method else 1
            inaccuracy = max([abs(y1 - y2) / (2 ** p - 1) for y1, y2 in zip(ys, ys2)])
            print(f"Error (by Runge rule): {inaccuracy}")

        print('-' * 30 + '\n')

        draw_plot(xs, ys, exact_y, x0, y0, name)


def improved_euler_method(f, xs, y0, eps):
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(1, len(xs)):
        y_pred = ys[i - 1] + h * f(xs[i - 1], ys[i - 1])
        y_corr = ys[i - 1] + h * f(xs[i], y_pred)
        ys.append(0.5 * (y_pred + y_corr))
    return ys


def fourth_order_runge_kutta_method(f, xs, y0, eps):
    ys = [y0]
    h = xs[1] - xs[0]
    for i in range(1, len(xs)):
        k1 = h * f(xs[i - 1], ys[i - 1])
        k2 = h * f(xs[i - 1] + h / 2, ys[i - 1] + k1 / 2)
        k3 = h * f(xs[i - 1] + h / 2, ys[i - 1] + k2 / 2)
        k4 = h * f(xs[i - 1] + h, ys[i - 1] + k3)
        ys.append(ys[i - 1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    return ys


def milne_method(f, xs, y0, eps=1e-7):
    ys = fourth_order_runge_kutta_method(f, xs[:4], y0, eps)
    h = xs[1] - xs[0]
    for i in range(4, len(xs)):
        pre_y = ys[i - 4] + 4 * h / 3 * \
                (2 * f(xs[i - 3], ys[i - 3]) -
                 f(xs[i - 2], ys[i - 2]) +
                 2 * f(xs[i - 1], ys[i - 1]))
        cor_y = get_cor_y(xs, ys, f, pre_y, i, h)
        while abs(pre_y - cor_y) > eps:
            pre_y = cor_y
            cor_y = get_cor_y(xs, ys, f, pre_y, i, h)
        ys.append(cor_y)
    return ys


def get_cor_y(xs, ys, f, pre_y, i, h):
    return ys[i - 2] + h / 3 * \
        (f(xs[i - 2], ys[i - 2]) +
         4 * f(xs[i - 1], ys[i - 1]) +
         f(xs[i], pre_y))
