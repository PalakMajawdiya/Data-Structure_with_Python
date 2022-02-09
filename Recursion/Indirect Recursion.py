# Indirect Recursion: If there are more than one function and they are calling each other in a circular manner then it is indirect recusrion

n = int(input("Enter a no: "))

def funA(n):
    if n>0:
        print(n)
        funB(n-1)
        
def funB(n):
    if n>1:
        print(n)
        funA(round((n/2)))
        
funA(n)