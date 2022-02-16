#Tower of Hanoi

def TOH(n,A,B,C):
    if n>0:
        TOH(n-1,A,C,B)
        print("(",A,",",C,")")
        TOH(n-1,B,A,C)
        

n = int(input("Enter no. of discs to be transfer from A to C: "))
print("Steps to transfer",n," discs from A to C are: ")
TOH(n,1,2,3)


