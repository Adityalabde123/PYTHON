#count the number of lines in file..
f1=open("demo2.txt","r")
c=0
while True:
  s=f1.readline()
  c=c+1
  if s=="":    
    break
print("number of lines",c)
f1.close()
