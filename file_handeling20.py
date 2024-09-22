#write an python programme to get an size of plain file..'
f1=open("demo1.txt","r")
s=f1.read()
print("size=",len(s))
f1.close()