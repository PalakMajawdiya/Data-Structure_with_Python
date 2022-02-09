# Nested Recursion

def Sum(n):
    if n==0:
        return 0;
    else:
        return Sum(n-1)+n;
        

n = int(input("Enter no. to calculate sum: "))
print(Sum(n))
