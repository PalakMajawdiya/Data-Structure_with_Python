# Factorial of a number using Recursion

#If a recursive function goes into infinite loop then it terminates when stack overflow

def fact(n):
    if n==0 or n==1:
        return 1;
    else:
        return fact(n-1)*n;
        

n = int(input("Enter no. to calculate factorial: "))
print(fact(n))
