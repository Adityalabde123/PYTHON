#readline method..
f1=open("demo1.txt","r")
while True:
    s=f1.readline()
    if s=="":
         break
    print(s)
f1.close()
