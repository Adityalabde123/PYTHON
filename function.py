#simple addition programme..
def add(a,b):
    c=a+b
    print("ADDITION=",c)

add(11,22)
add(11.55,22.22)
add("sai","ram")#concatnation of string..

                  #OR
def add(a,b):
    c=a+b
    return c

print("ADDITION=",add(11,22))
