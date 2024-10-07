#ZeroDivisionError
try:
    a=int(input("enter no1:"))
    b=int(input("enter no2"))
    c=a/b
    print("division=",c)
except ZeroDivisionError as e:
    print("error=",e)