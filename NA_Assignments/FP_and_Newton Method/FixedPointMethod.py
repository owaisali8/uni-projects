#Syed Owais Ali-23053
from numpy import *
import matplotlib.pyplot as plt
from tabulate import tabulate
import time

def f(x):
    r = float(eval(fx))
    return r
    
   
def fixed_point(p0,tol):
    p_list = [[p0,f(p0)]]
    t1 = time.time()
    p = f(p0)
    i = 1
    relative_error = abs((p-p0)/p)
    p_list.append([p,f(p)])
    while(relative_error>tol):
        try:
            temp = p
            p = f(p)
            i+=1
            relative_error = abs((p-temp)/p)
            p_list.append([p,f(p)])
            if(relative_error ==0):
                break
            elif(p == inf or f(p) == inf):
                print("g(x)is diverging.")
                return
        except OverflowError:
            print("g(x) is diverging.")
            return
    
    t2 = time.time()
    t = t2-t1
    
    print('Root of the function:',p)
    print('Number of iterations:',i)
    print('CPU Time: ',t)
    file_write(p,i,p_list)
    plot(p0,p,p_list)


def plot(p0,p,p_list):
    import random
    x= linspace(-5, 5, 500)
    y = eval(fx)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Fixed-Point Method')
    plt.plot(x,y, color ='green',label = f"{fx}")
    plt.plot(x,x,color ='grey',label="y=x")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(p,p,'bo',label ="p")
    
    no_of_colors=len(p_list)
    color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
            for j in range(no_of_colors)]
    for i in range(1,len(p_list)):
        x0 = p_list[i-1][0]
        y0 = 0
        x1 = p_list[i-1][0]
        y1 = p_list[i][1]
        x = [x0,x1]
        y = [y0,y1]
        plt.plot(x,y,c=color[i], linestyle='dashed', label=f"p{i-1}")
        plt.plot([x1,y1],[y1,y1],c=color[i], linestyle='dashed')
    
    plt.legend()
    plt.show()


def file_write(p,i,list1):
    for i in range(1,len(list1)):
        pn = list1[i-1][0]
        pn_1 = list1[i][0]
        c = abs(pn_1-p)/abs(pn-p)
        list1[i].append(c)
        if(c==0):
            break
    
    file = open('FixedPointData.txt','w')
    file.write(f'{fx}\n')
    title = ["i","p","f(p)","Asymptotic Constant"]
    file.write(tabulate(list1, headers = title,tablefmt="simple",showindex="always",numalign="right",floatfmt=".20f"))
    file.close()

    
def main():
    global fx
    fx = str(input("Enter function in python expression in terms of x=g(x): "))
    p0 = float(input("Intial guess P0 "))
    tol = float(input("Enter tolerance: "))
    fixed_point(p0,tol)
    

if __name__ == '__main__':
    main()