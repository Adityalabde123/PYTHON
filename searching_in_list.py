a=["java","php","ds","cpp","python"]
s=input("enter subject name to search")
if s in a:
  k=a.index(s)
  print("subject found on position",k)
else:
 print("subject not found")