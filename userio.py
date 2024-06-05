from functions import *
from methods import solve


def launch():
    hello = "Computational Mathematics Lab 4: Function approximation"
    print("-" * len(hello))
    print(hello)
    print("-" * len(hello))
    print()
    workout()


def close_application_appropriately():
    print("\nClosing application...")
    exit()


def get_input():
    try:
        return input("$ ").strip().replace(",", ".")
    except (EOFError, KeyboardInterrupt):
        close_application_appropriately()


def workout():
    f, exact_y = select_ode()
    xs, x0, y0, eps = read_data()
    solve(f, xs, x0, y0, exact_y, eps)


def select_ode():
    print('Select ODE: ')
    print('1. y + (1 + x)y^2')
    print('2. x + y')
    print('3. sin(x) - y')
    print()
    print("Choose 1, 2 or 3.")
    while True:
        try:
            input_func = int(get_input())
            if input_func == 1:
                f = f1
                exact_y = y1
                break
            elif input_func == 2:
                f = f2
                exact_y = y2
                break
            elif input_func == 3:
                f = f3
                exact_y = y3
                break
            else:
                print("Please, chose one of the available options.")
        except ValueError:
            print("Please, chose one of the available options.")
    return f, exact_y


def read_data():
    x0 = read_x0()
    h = read_h()
    n = read_n()
    xs = [x0 + i * h for i in range(n)]
    y0 = read_y0()
    eps = read_eps()
    return xs, x0, y0, eps


def read_x0():
    print("Enter x0:")
    while True:
        try:
            x0 = float(get_input())
            break
        except ValueError:
            print("Please, enter a valid number.")
    return x0


def read_h():
    print("Enter h (> 0):")
    while True:
        try:
            h = float(get_input())
            if h <= 0:
                print("h has to be positive.")
                continue
            break
        except ValueError:
            print("Please, enter a valid number.")
    return h


def read_n():
    print("Enter n (int >= 2:")
    while True:
        try:
            n = int(get_input())
            if n < 2:
                print("n has to be at least 2.")
                continue
            break
        except ValueError:
            print("Please, enter a valid number.")
    return n


def read_y0():
    print("Enter y0:")
    while True:
        try:
            y0 = float(get_input())
            break
        except ValueError:
            print("Please, enter a valid number.")
    return y0


def read_eps():
    print("Enter eps (0 < eps < 1):")
    while True:
        try:
            eps = float(get_input())
            if eps <= 0 or eps >= 1:
                print("eps has to be greater than 0 and less than 1.")
                continue
            break
        except ValueError:
            print("Please, enter a valid number.")
    return eps
