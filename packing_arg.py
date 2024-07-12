def add(*z):
    print(z)
    s=sum(z)
    print("addition=",s)

add(10,20,30,40,50)
add(10,20,30)


#pack into dictionary
def show(**t):
    print(t)

show(rno='101',name='aditya',per='66')