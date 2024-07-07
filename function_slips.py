#find max of three numbers...
def maximum(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c
    
a=input("enter no.1:")
b=input("enter no.2:")
c=input("enter no.3:")

print("MAXIMUM no=",maximum(a,b,c))