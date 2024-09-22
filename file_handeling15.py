#write an python code to find an longest word in file...
f1=open("demo2.txt","r")
s=f1.read()
s2=s.split(" ")
s3=""
for s2 in s3:
    if len(s2)>len(s3):
        s3=s2
    print(s3)
    f1.close()