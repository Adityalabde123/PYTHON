def add(*a):#variable length arg is used to for multiple argument calling..

    print(a)
    s=0
    for val in a:
        s=s+val
    print("ADDITION=",s)

add(11,22,33)
add(11,22,33,44,55)#here we accept thousand of value..
