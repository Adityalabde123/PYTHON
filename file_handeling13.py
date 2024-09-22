#write an python code to read a file line by line and store it into a list..
f1=open("demo1.txt","r")
a1=[]
while True:
    s=f1.readline()
    if s=="":
        break
    a1.append(s)
print(a1)
f1.close()