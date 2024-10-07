#accessing a file which does not exist..
try:
    f1=open("sqz.txt","r")
    s.read(f1)
    print(s)
except FileNotFoundError as e:
    print("FILE NOT FOUND",e)