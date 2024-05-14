n=int(input("enter number"))
print("\n 1-squre \n 2-cube \n 3-evenodd")
ch=int(input("enter choice"))
if ch==1:
    print("squre=",n*n)
elif ch==2:
    print("cube=",n*n*n)
elif ch==3:
    if(n%2==0):
        print("number is even")
    else:
        print("number is odd")
else:
    print("Invalid choice")