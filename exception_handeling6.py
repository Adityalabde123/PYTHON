#all exception in one statement..
try:
    a=int(input("enter no1:"))
    b=int(input("enter no2"))
    c=a/b
    print("Division=",z)
except(ZeroDivisionError,NameError,ArithmeticError,IndexError) as e:
    print("error=",e)