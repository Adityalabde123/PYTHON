#Multiple exception in one code block..
try:
    a=int(input("enter no.1:"))
    b=int(input("enter no.2:"))
    c=a/b
    print("Division=",z)#here z is undefined
except ZeroDivisionError as e:
    print("Zero divide error=",e)
except IndentationError as e2:
    print("error=",e2)
except NameError as e3:
    print("name ERRor",e3)

    