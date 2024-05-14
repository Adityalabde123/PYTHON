##length
a=[11,22,33,44,11,66]
print("length=",len(a))

#minimum
print("Min=",min(a))

##maximum
print("max=",max(a))

#number count
print("number count=",a.count(11))

##printing list into another list
s="college"
a=list(s)
print(a)

##convert tuple into list
s=(11,22,33,44,55)
a=list(a)
print(a)

print(type(s))
print(type(a))

##extend list
a=[11,22,33]
b=[44,55,66]
a.extend(b)
print(a)
print(a[0])
print(a[3])

##append list
a=[11,22,33]
b=[44,55,66]
a.append(b)
print(a)
print(a[0])
print(a[3])

##index
a=[11,22,33,44,55,66]
print("Index position=",a.index(22))

##list insert
a=[11,22,33,44,55,66]
a.insert(2,99)
print("list",a)

##list pop
a=[11,22,33,44,55,66]
print("element=",a.pop())

##reverse
a=[11,22,33,44,55,66]
a.reverse()
print(a)

#sort
a=[88,22,33,44,55,66]
a.sort()
print(a)

