# Group Members:
# Syed Owais Ali-23053
# Mohammad Mohsin-22837

from numpy import *
import matplotlib.pyplot as plt

global fun, interval, n, l_fun


def p(x):
    return eval(l_fun)


def f(x):
    return eval(fun)


def plot(x_values, y_values):
    x = linspace(interval[0]-0.5, interval[1]+0.5, 100)
    y = eval(fun)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Lagrange Polynomial Graph')
    plt.plot(x, eval(l_fun), color='blue', label="Lagrange Polynomial P(x)")
    x = linspace(interval[0], interval[1], 100)
    plt.plot(x, y, color='green', label=f"f(x) = {fun}")
    error_eq = f"{fun}-{l_fun}"
    plt.plot(x, eval(error_eq), color="red", label="f(x)-P(x)")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    plt.show()


def lagrange_polynomial(x_values):
    from scipy.interpolate import lagrange
    from numpy.polynomial import Polynomial
    global l_fun
    x = array(x_values)
    y = eval(fun)
    eq = Polynomial(lagrange(x, y))
    eq = eq.coef
    l_fun = ""
    for i in range(len(eq) - 1):
        l_fun += str(eq[i]) + "*" + f"x**{(len(eq) - i - 1)} +"
    l_fun += str(eq[len(eq) - 1])


def compute_x():
    v = (abs(interval[0]) + abs(interval[1])) / n
    num_list = []
    for i in range(n + 1):
        num_list.append(interval[0] + v * i)
    return num_list


def compute_y(x_values):
    num_list = []
    for num in x_values:
        num_list.append(f(num))
    return num_list


def main():
    global fun, interval, n
    fun = "exp(x) + 2**(-x)+ 2*cos(x)-6"
    interval = [-2, 2]
    n = 10

    x_values = compute_x()
    y_values = compute_y(x_values)

    lagrange_polynomial(x_values)
    print(f'Lagrange polynomial:\n{l_fun}')
    plot(x_values, y_values)


if __name__ == '__main__':
    main()
