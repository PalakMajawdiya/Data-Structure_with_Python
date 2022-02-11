# Program for Power function

def power(m,n):
    if n==0:
        return 1;
    else:
        return power(m,n-1)*m;


#Optimized version of power function

def power1(m,n):
    if n==0:
        return 1;
    elif n%2==0:
        return power1(m*m,n/2);
    else:
        return m*power1(m*m,(n-1)/2);
        

res = power(2,9)
print("Result from normal function is: ",res)

res1 = power1(2,9)
print("The result from optimized version is: ",res1)