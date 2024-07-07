#accept an list and display it's unique..

def unique(a):
    b=set(a)
    return b

a=[]
n=int(input("enter limit"))
for i in range(0,n):
    val=input("enter element")
    a.append(val)
print("list elemnt",unique(a))
