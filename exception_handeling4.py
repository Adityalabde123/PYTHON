#IndexError..
try:
    a=[11,22,33,44]
    print(a[4])
except IndexError as e:
    print("error=",e)