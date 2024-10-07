#ArithmaticError
try:
    a=5/0
    print("Division=",a)
except ArithmeticError as e:
    print("error=",e)