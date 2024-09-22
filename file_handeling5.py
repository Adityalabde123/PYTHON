#writeline method..(copy contains from one file into another files)
f1=open("demo1.txt","r")
f2=open("demo2.txt","w")
while True:
    s=f1.readline()
    if s=="":
        break
    f2.write(s)
f1.close()
f2.close()
print("FILE COPY SUCCESSFULLY")