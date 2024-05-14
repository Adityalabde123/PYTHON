#if string's first charater is repeat in an string then it replace with specific character..
s=input("enter string")
s1=s[0]
for i in range(1,len(s)):
    if s[i]==s[0]:
        s1=s1+"*"
    else:
        s1=s1+s[i]

print("Result=",s1)