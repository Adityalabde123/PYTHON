def prime(n):
    for num in range(n+1):
        f=0
        for i in range(2,num):
            if num%i==0:
                f=1
        if f==0:
            yield num
    
n=int(input("enter limit"))
for i in prime(n):
    print(i)