#all set function and eg

#printing normal set:
a={"java","php","python"}
for val in a:
    print(val)

       #OR
a=set(["java","python","php"])
print(a)

#add element in the set..(add() function)
a={"java","tcs","php"}
a.add("cpp")
print(a)

a.update(["python","c"]) #add multiple element in the set...(update() function)
print(a)

#remove the elemnt from set from various function and parametrs..
#pop function..
a={"java","python","tcs","100"}
val=a.pop()
val1=a.pop()
val3=a.pop()
val4=a.pop()
print("deleted value=",val)
print("deleted value=",val1)
print("deleted value=",val3)
print("deleted value=",val4)
print(a)

#discard function..
a={"java","python","tcs","100"}
val=a.discard("java")
print(a)

#remove function..
a={"java","python","tcs","100"}
## val=a.remove("cpp")
print(a) ##It's gets error because value key is not present in set..

#clear function..
a={"java","python","tcs","100"}
a.clear()
print(a)

#Union of sets (|)OR operator..
a={11,22,33,44}
b={33,55,66}
c=a|b
print(c)

#Union of sets with union function..
a={11,22,33,44}
b={33,55,66}
c=a.union(b)
print(c)

#intersection operator with (&)and operator..
a={11,22,33,44}
b={33,55,66}
c=a&b
print(c)

#intersetion operator with intersection operator..
a={11,22,33,44}
b={33,55,66}
c=a.intersection(b)
print(c)

#intersectioon update..
a={11,22,33,44}
b={33,55,66}
a.intersection_update(b)
print(a)
print(b)

#differance of two sets using(-)operator..
a={11,22,33,44}
b={33,55,66}
c=a-b
print(c)

#differance of two sets using differance function..
a={11,22,33,44}
b={33,55,66}
c=a.difference(b)
print(c)

#differance_update()
a={11,22,33,44}
b={33,55,66}
a.difference_update(b)
print(a)
print(b)
b.difference_update(a)
print(a)
print(b)

#Symmetric differance
a={11,22,33,44}
b={33,55,66}
c=a.symmetric_difference(b)
print(c)

#Symmetric differance_update
a={11,22,33,44}
b={33,55,66}
a.symmetric_difference(b)
print(a)
print(b)

#issuperset..
a={11,22,33,44}
b={33,55,66}

if(b.issuperset(a)):
    print("a set is present in  b")
else:
    print("not present ")

#is subset()
a={11,22,33,44}
b={33,55,66}
if(a.issubset(b)):
   print("a set is present in b")
else:
   print("not present")

#disjoint
a={11,22,33,44}
b={33,55,66}

if(a.isdisjoint(b)):
    print("not common element ")
else:
    print("present common element")
    