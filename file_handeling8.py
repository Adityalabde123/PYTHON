#compute the number of lines,character,words min a file..
f1=open("demo1.txt","r")
c1=0
c2=0
c3=0
while True:
    s=f1.readline()
    c3=c3+len(s)
    if s=="":
        break
    c1=c1+1
    s1=s.split(" ")
    for a in s1:
        c2=c2+1

print("LINES=",c1)
print("WORDS=",c2)
print("CHAR=",c3)