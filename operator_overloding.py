# * operator..
class demo:
    def accept(self):
        self.s1=input("enter string")
        self.n=int(input("enter number"))
    def __mul__(self,obj):
        print("string=",self.s1*self.n)
ob=demo()
ob1=demo()
ob.accept()
ob*ob1