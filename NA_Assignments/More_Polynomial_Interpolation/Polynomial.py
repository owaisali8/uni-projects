# Group Members:
# Syed Owais Ali-23053
# Mohammad Mohsin-22837

from numpy import *
import matplotlib.pyplot as plt
from tabulate import tabulate

global fun, interval, n, l_fun, spline


def p(x):
    return eval(l_fun)


def f(x):
    return eval(fun)


def plot(x_values, y_values):

    plt.figure(2)
    x = linspace(interval[0], interval[1], 100)
    y = eval(fun)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Lagrange Polynomial Graph')
    error_eq = f"{fun}-{l_fun}"
    plt.plot(x, eval(error_eq), color="red", label="f(x)-P(x)")
    plt.plot(x, eval(l_fun), color='blue', label="Lagrange Polynomial P(x)")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    
    plt.figure(1)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Function Graph')
    x = linspace(interval[0], interval[1], 100)
    plt.plot(x, y, color='green', label=f"f(x) = {fun}")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    
    plt.figure(3)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Cubic Spline Graph')
    plt.plot(x, spline(x), color='pink', label=f"Spline Function S(x)")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    
    
    plt.figure(4)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Combined Graph [-2,2] 100 data points')
    x = linspace(interval[0], interval[1], 100)
    plt.plot(x, y, color='green', label=f"f(x) = {fun}")
    plt.plot(x, eval(l_fun), color='blue', label="Lagrange Polynomial P(x)")
    plt.plot(x, spline(x), color='pink', label=f"Spline Function S(x)")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.legend()
    
    
    plt.figure(5)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Combined Graph [-3,3] 100 data points')
    x = linspace(-3, 3, 100)
    plt.plot(x, y, color='green', label=f"f(x) = {fun}")
    plt.plot(x, eval(l_fun), color='blue', label="Lagrange Polynomial P(x)")
    plt.plot(x, spline(x), color='pink', label=f"Spline Function S(x)")
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
    p = lagrange(x, y)
    eq = Polynomial(p)
    eq = eq.coef
    l_fun = ""
    for i in range(len(eq) - 1):
        l_fun += str(eq[i]) + "*" + f"x**{(len(eq) - i - 1)} +"
    l_fun += str(eq[len(eq) - 1])
    
    with open("Lagrange.txt",'w') as file:
        file.write('Lagrange Polynomial\n')
        file.write(f'Degree Of Polynomial: {p.o}\n')
        file.write(f'Root(s) Of Polynomial: {p.r}\n')
        file.write(f"\nP(x)={l_fun}")


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


def newton_divided_diff(x_values,y_values):
    file = open("DividedDiff.txt",'w')
    file.write('Newton Divided Difference\n')
    title = ["i","xi","f(xi)"]
    data=[]
    
    for i in range(len(x_values)):
        data.append([x_values[i],y_values[i]])
        
    for i in range(1,n+1):
        title.append(f"f[xi-{i}]")
    
    for i in range(1,n+2):
        for j in range(1,n+2-i):
            if i ==1:
                data[j].append(divided_diff(data,j,i))
            else:
                 data[j].append(divided_diff(data,j+1,i))

    file.write(tabulate(data, headers = title,tablefmt="simple",showindex="always",numalign="right",floatfmt=".25f"))
    file.close()
    

def divided_diff(data,j,i):
    try:
        return (data[j][i]-data[j-1][i])/((data[j][0]-data[j-1][0])*i)
    except IndexError:
        return 0

    
def cubic_spline(x_values,y_values):
    global spline
    from scipy.interpolate import CubicSpline
    spline = CubicSpline(x_values, y_values, bc_type='natural')
    S_fun = []
    for i in range(10):
        xi = x_values[i]
        a = spline.c.item(3,i)
        b = spline.c.item(2,i)
        c = spline.c.item(1,i)
        d = spline.c.item(0,i)
        S_fun.append(f'S{i} = {a}+{b}*(x-{xi})+{c}*(x-{xi})**2 + {d}*(x-xi)**3')
    
    print()
    print("Spline Functions: ")
    for s in S_fun:
        print(s,'\n')
    
    with open("CubicSpline.txt",'w') as file:
        file.write('Natural Cubic Spline\n')
        for s in S_fun:
            file.write(f'{s}\n')


def main():
    global fun, interval, n
    fun = "exp(x) + 2**(-x)+ 2*cos(x)-6"
    interval = [-2, 2]
    print(fun)
    n = int(input("Enter n: "))

    x_values = compute_x()
    y_values = compute_y(x_values)

    lagrange_polynomial(x_values)
    print(f'Lagrange polynomial:\n{l_fun}')
    newton_divided_diff(x_values,y_values)
    cubic_spline(x_values,y_values)
    plot(x_values, y_values)


if __name__ == '__main__':
    main()
