# Tree Recursion: If a function calls iteself more than one time then it is Tree Recursion

n = int(input("Enter no.: "))

def fun(n):
    if n>0:
        print(n)
        fun(n-1)
        fun(n-1)
    
    
fun(n)