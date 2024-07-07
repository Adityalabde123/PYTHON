def add(a,b,c=33): #passinng the value to the one argumnt..
    d=a+b+c
    return d

print("ADDITION=",add(11,22))

                        #OR
def add(a,b=22,c=33): #here we passing the value to two argument..
    d=a+b+c
    return d

print("ADDITION=",add(11,44,55))#here ignoring the actual parameter values and accepting this value..
