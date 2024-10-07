#write an python error to demonstrate the zero division error and overflow error...
try:
    a=int(input("enter no1:"))
    b=int(input("enter no2:"))
    c=a/b
    d=a**b
    print("division=",c)
    print("Power=",d)

except(ZeroDivisionError,OverflowError) as e:
    print("error=",e)