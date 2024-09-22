#readlines method..
f1=open("demo1.txt","r")
data=f1.readlines()
for s in data:
    print(s)
f1.close()