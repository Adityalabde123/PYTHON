#write a list to file..
f1=open("demo7.txt","w")
a1=["java","php","Cpp"]
for s in a1:
    f1.write(s+"\n")
f1.close()
print("write successfully")