#write an python code to read line by line store into in variable...
f1=open("demo2.txt","r")
a1=""
while True:
    s=f1.readline()
    if s=="":
        break
    a1=a1+s
print(a1)
f1.close()