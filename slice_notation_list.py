a=[11,22,33,44,55,66,77]
print(a[2:5])
print(a[:5])
print(a[-5:4])
print(a[1:8:2])
print(a[::3])
print(a[-2:1:-3])

##slice and coping list
l1=[10,20,30,40,50]
l2=l1[0:3]
print(l2)

#slice
l1[:3]=[7,8,9]
print(l1)

#slice deletion
l1=[10,20,30,40,50]
del l1[2:5]
print(l1)

