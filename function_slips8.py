#count uppercase and lowercase
def count_char(s):
    c1=0
    c2=0
    for ch in s:
        if ch>='A' and ch<="Z":
            c1=c1+1
        else:
            c2=c2+1
    print("upper=",c1)
    print("lower=",c2)

s=input("enter string:")
count_char(s)