##solve using 2 method..
s=input("enter string")
c1=0
c2=0
for ch in s:
    if ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
        c1+=1
    else:
        c2+=1
print("vowels count=",c1)
print("consonants count=",c2)


##another way
s=input("enter string")
c1=0
c2=0
v="aeiouAEIOU"
for ch in s:
    if ch in v:
        c1+=1
    else:
        c2+=1
print("vowels count=",c1)
print("consonant count=",c2)
