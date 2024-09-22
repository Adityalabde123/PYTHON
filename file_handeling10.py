#write a python programme to read first n lines of a file...
f1=open("demo2.txt","r")
s=f1.readlines()
n=int(input("enter the number of lines you have to read."))
for i in range(0,n):
    print(s[i],end="")
f1.close()