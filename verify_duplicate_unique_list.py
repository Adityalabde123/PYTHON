a=[]
print("enter 5 value")
for i in range(5):
  num=input("enter number")
  a.append(num)
print("list element",a)


b=set(a)
if len(b) == 5:   #it checks duplicate or not because list does not accept duplicate value
  print("all are unique")
else:
  print("DUPLICATE") 
  