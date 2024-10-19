#print fibbonaci series
def show(n):
    f=0
    s=1
    for i in range(n+1):
            f=s
            f=f+s               
            s=f
            yield f
n=int(input("enter limit"))
for i in show(n):
    print(i)