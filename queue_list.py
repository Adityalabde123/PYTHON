a=[]
ch=0
while ch!=4:
    print("\n1-insert\n2-delete\n3-display\n4-exit")
    ch=int(input("enter choice"))
    if ch==1:
        num=input("enter number")
        a.append(num)
        print(a)
    elif ch==2:
        del a[0]
    else:
        print(a)
    