# + operator..
class demo:
    def accept(self,a,b):
        self.a=a
        self.b=b
        
    def __add__(self,bbj):
        print(self.a+self.b)
ob=demo()
ob1=demo()
ob.accept("aditya","labade")
ob+ob1

ob3=demo()
ob4=demo()
ob3.accept(11,22)
ob3+ob4  