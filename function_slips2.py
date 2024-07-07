#sum of all the numbers in the list..
def sum_list(a):
    s=0
    for val in a:
        s=s+val
    return s
    
b=[11,7,65,4,3,2]
print("sum of all element",sum_list(b))

           #OR
def sum_list(a):
    s=0
    for val in a:
        s=s+val
    return s
a=[]
n=int(input("enter limit"))
for i in range(0,n):
    num=int(input("enter number:"))
    a.append(num)
print("sum of list element=",sum_list(a))