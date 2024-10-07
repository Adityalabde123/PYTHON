#addition of two incompitable types..
try:
    a=33
    b="om"
    c=a+b
    print("addtion=",c)

except TypeError as e:
    print("error=",e)