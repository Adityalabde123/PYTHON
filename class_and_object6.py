#del the date..(slips)
class student:
    def accept(self):
        self.rno=input("enter roll no")
        self.name=input("enter name")
        print("Enter marks of 3 subjects")
        self.m=[]
        for i in range(0,3):
            val=input("enter marks")
            self.m.append(val)
    def disp(self):
        s=0
        for i in range(0,3):
            s=s+int(self.m[i])
        print("roll no=",self.rno)
        print("name=",self.name)
        print("total marks=",s)
        print("percentage=",s/3)
    
    def __del__(self):
        del self.rno
        del self.name
        del self.s
        print("Memory free...")

ob=student()
ob.accept()
ob.disp()


