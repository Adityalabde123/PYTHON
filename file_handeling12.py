#write an python programme to read last(at the end) lines of the file..
f1=open("demo2.txt","r")
n=int(input("enter last n line number"))
lines=f1.readlines()
for s in lines[-n:]:
    print(s,end='')
    f1.close()