def add(a,b,c):
    d=a+b+c
    print("Addition=",d)

z=[11,22,33]
add(*z)

t=(50,20,60)
add(*t)

s={100,200,300}
add(*s)

d={'a':5,'b':10,'c':15}
add(**d)#for dictionary we use double astrik..

