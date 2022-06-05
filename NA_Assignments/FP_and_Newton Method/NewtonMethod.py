#Syed Owais Ali-23053

from numpy import *
from sympy import *
import matplotlib.pyplot as plt
from tabulate import tabulate
import time

def f(x):
    r = float(eval(fx))
    return r
    
    
def newton_method(p0,tol):
    p_list = [[p0,f(p0)]]
    
    if(f_prime(p0) == 0):
        print("f(x)' is 0, Give new Intial guess (p0).")
        return
    t1 = time.time()
    p = p0 - (f(p0)/f_prime(p0))
    i = 1
    relative_error = abs((p-p0)/p)
    p_list.append([p,f(p)])
    while(relative_error>tol):
        temp = p
        p = p - (f(p)/f_prime(p))
        i+=1
        relative_error = abs((p-temp)/p)
        p_list.append([p,f(p)])
        if(f_prime(p) ==0 or relative_error ==0):
            break
    
    t2 = time.time()
    t = t2-t1
    
    print('Root of the function:',p)
    print('Number of iterations:',i)
    print('CPU Time: ',t)
    file_write(p,i,p_list)
    plot(p0,p,p_list)
    
    
def plot(p0,p,p_list):
    from numpy import cos
    from numpy import sin
    from numpy import tan
    from numpy import exp
    from numpy import e
    from numpy import log
    import random
    
    x= linspace(int(p0-2), int(p0+2), 500)
    y = eval(fx)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Newton Method')
    plt.plot(x,y, color ='green',label = f"{fx}")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(p0,f(p0),'bo',label ="p0")
    plt.plot(p,0,'ro',label ="p")
    no_of_colors=len(p_list)
    color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
            for j in range(no_of_colors)]
    
    for i in range(1,len(p_list)):
        x0 = p_list[i-1][0]
        y0 = p_list[i-1][1]
        x1 = p_list[i][0]
        y1 = 0
        x = [x0,x1]
        y = [y0,y1]
        plt.plot(x,y,c= color[i], linestyle='dashed', label=f"p{i-1}")
    
    plt.legend()
    plt.show()
    


def file_write(p,i,list1):
    for i in range(1,len(list1)):
        pn = list1[i-1][0]
        pn_1 = list1[i][0]
        c = abs(pn_1-p)/abs(pn-p)
        list1[i].append(c)
    
    file = open('NewtonData.txt','w')
    file.write(f'{fx}\n')
    title = ["i","p","f(p)","Asymptotic Constant"]
    file.write(tabulate(list1, headers = title,tablefmt="simple",showindex="always",numalign="right",floatfmt=".20f"))
    file.close()


def main():
    global fx,f_prime
    fx = str(input("Enter function in python expression in terms of x: "))
    p0 = float(input("Intial guess P0 "))
    tol = float(input("Enter tolerance: "))
    x = Symbol('x')
    f_prime_x = diff(eval(fx))
    f_prime = lambdify(x,f_prime_x)
    newton_method(p0,tol)
    

if __name__ == '__main__':
    main()