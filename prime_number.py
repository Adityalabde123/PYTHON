n=int(input("enter number"))
f=0
for i in range(2,n) :
    if n%i==0 :
        f=1;


if f==0 :
    print("number is prime")
else :
    print("number is not prime")