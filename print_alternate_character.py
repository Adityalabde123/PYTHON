#printing the alternate character of string from both the side
s=input("enter string")
print("Alternate characters forward direction")
for i in range(0,len(s),2):
   print(s[i],end="")

print("printing alternate character backward direction")
for i in range(len(s)-1,-1,-2):
   print(s[i],end="")

#anoter way:

s=input("enter string")
s1=""
for i in range(0,len(s)):
   if i%2==0:
      s1=s1+s[i]
      print("altrnate character forward direcrtion=",s1)

s1=""
for i in range(0,len(s)):
   if i%2==0:
      s1=s[i]+s1
      print("alternate character in backward direction=",s1)

#anoterway
s=input("entrer string")

print("alternate character forward direction=",s[::2])
print("alternate character backward direction=",s[::-2])