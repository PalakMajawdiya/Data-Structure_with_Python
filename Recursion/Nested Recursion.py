# Nested Recursion

def fun(n):
    if n>100:
        return n-10;
    else:
        return fun(fun(n+11));
        


r = fun(90)
print(r)