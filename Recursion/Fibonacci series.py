#  Fibonacci series 

#using Iterative method

def fib(n):
    t0=1
    t1=1
    if n<=1:
        return n;
    else:
        for i in range(2,n):
            s = t0+t1;
            t0=t1;
            t1=s;
            
    return s;
    
#using Recursive method

def rfib(n):
    if n<=1:
        return n;
    else:
        return rfib(n-2)+rfib(n-1);
    

print("The result from iterative method: ",fib(6))
print("The result from iterative method: ",rfib(6))