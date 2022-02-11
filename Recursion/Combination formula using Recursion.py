#  Fibonacci series 

# using recursive method
def fact(n):
    if n==0:
        return 1;
    else:
        return fact(n-1)*n
        
def nCr(n,r):
    num = fact(n)
    den = fact(r)*fact(n-r);
    
    return num/den
    
print("The result is: ",nCr(5,3))