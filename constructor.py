#init method..
class emp:
    def __init__(self,eno,ename,sal):
        self.eno=eno
        self.ename=ename
        self.sal=sal
    
    def disp(self):
        print("emp no=",self.eno)
        print("emp name=",self.ename)
        print("emp sal=",self.sal)
    
ob=emp(101,"ADITYA",150000)
ob.disp()