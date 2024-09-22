#write an python code to print each line of a file in reverse order..
f1=open("demo4.txt","r")
while True:
    s=f1.readline()
    if s=="":
        break
    print(s[::-1],end="")   #OR print(s[::-1])
f1.close()