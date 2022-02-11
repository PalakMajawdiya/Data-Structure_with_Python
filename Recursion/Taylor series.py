# Taylor series using horner's rule

def ex(x,n):
    s = 1;
    num =1 ;
    den = 1;
    
    for i in range(1,n+1):
        num = num*x;
        den = den*i;
        s = s+num/den;
        print(s)
      
    
    return s;
print("The series is: ")   
print("The result of series is: ",ex(3,10))