s=input("enter string:")
v=['a','e','i','o','u']
c=0
for ch in s:
    if ch in v:
        c=c+1
print("vowels count=",c)