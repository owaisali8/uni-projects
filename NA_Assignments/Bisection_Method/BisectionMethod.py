#Syed Owais Ali - 23053
import math

def f(x):
    r = float(eval(fx))
    return r


def root(a,b):
    if(f(a)>0 and f(b)<0):
        return True
    elif(f(a)<0 and f(b)>0):
        return True
    else:
        return False
    
    
def bisection_method(a, b, tolerance):
    if(root(a,b) == False):
        print('Root does not exist in interval',f'[{a},{b}]')
        return
    mid_list = [0,0]
    f_mid_list = [0,0]
    i = 1
    mid = (a+b)/2
    f_mid = f(mid)
    mid_list[i] = mid
    f_mid_list[i] = f_mid
    while(abs(f_mid)>tolerance):
        if(f_mid == 0):
            break
        if(f_mid >0):
            b = mid
        elif(f_mid <0):
            a = mid
        mid = (a+b)/2
        i+=1
        f_mid = f(mid)
        
        mid_list.append(mid)
        f_mid_list.append(f_mid)
        
    print('Root of the function:',mid)
    print('Number of iterations:',i)
    file_write(i,mid_list,f_mid_list)
   
   
def file_write(i,list1,list2):
    file = open('DATA.txt','w')
    file.write(f'{fx}\n')
    file.write("{:<15}{:<30}{:<15}".format('i','m','f(m)'))
    file.write('\n')
    for k in range(1,i+1):
        file.write("{:<15}{:<30}{:<15}\n".format(k,list1[k],list2[k]))
    file.close()
    
    
    
def main():
    global fx
    fx = str(input("Enter function in python expression in terms of x: "))
    a = float(input("Enter interval a: "))
    b = float(input("Enter interval b: "))
    tol = float(input("Enter tolerance: "))
    bisection_method(a,b,tol)
    


if __name__ == '__main__':
    main()