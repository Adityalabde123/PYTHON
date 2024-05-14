##list with same element
a=["c","cpp","java","python"]
print(a)

#list with differant element
a=["c","cpp",50,55.66,"java"]
print(a)


#list within a list elemenmt
a=["c","cpp",11,[22,33,44],"java"]
print(a)

#printing the specific element with index value..
a=["c","cpp",11,[22,33,44],"java"]
print(a[0])

##(short list) convert element into variable.
a=["c","cpp","java","python"]
x,y,z,w=a
print(x)

##printing through -ve indexing  
a=["c","cpp",11,[22,33,44],"java"]
print(a[-1])

##slicing an element in the list
a=["c","cpp","java","python"]
b=a[1:4]
print(b)

##modifynig the list.
a=["c","cpp","java","python"]
a[3]=95
print(a)

##deleting an element.
a=["c","cpp","java","python"]
del(a[3])
print(a)