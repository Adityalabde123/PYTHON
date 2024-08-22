#we are going to overload the constructor with variable length arg...
class emp:
    def __init__(self,*val):
        self.val=val
    
    def disp(self):
        print("emp info=",self.val)
    
ob=emp(101,"Aditya") #calling with two value..
ob.disp()

ob1=emp(101,"Aditya",150000) #calling with three value..
ob1.disp()