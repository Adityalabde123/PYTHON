#number is perfect or not..
def isperfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s=s+i

    if s==n:
        print("number is perfect")
    else:
        print("number is not perfect")

n=int(input("enter number"))
isperfect(n)