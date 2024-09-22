#count the frequency of words in a file..
f1=open("demo6.txt","r")
s=f1.read()
s1=s.split(" ")
a1=[]
for s2 in s1:
    if s2 not in a1:
        print(s2,"count=",s1.count(s2))
        a1.append(s2)
f1.close()