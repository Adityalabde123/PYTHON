#find the record..
d={"om":55,"sai":88,"ram":99}
nm=input("enter name")

if nm in d:
    print("per=",d[nm])
else:
    print("record not found")