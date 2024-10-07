#trying to access a non existance index of a sequence..
try:
    a=[10,20,30,40]
    print("value",a[8])
except IndexError as e:
    print("error",e)