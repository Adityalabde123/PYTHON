#variable length arg...
def add(*val):
    ans=0
    for n in val:
        ans=ans+n
        print("ADDITION=",ans)
 
add(11,22)
add(11,22,33)
add(11,22,33.33)