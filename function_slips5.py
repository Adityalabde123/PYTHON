#check the number is prime or not..
def isprime(n):
    f=0
    for i in range(2,n):
        if n%i==0:
            f=1
            break
    if f==0:
        print("number is prime")
    else:
        print("number is not prime")

n=int(input("enter number"))
isprime(n)