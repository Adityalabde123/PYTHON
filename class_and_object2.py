#get value from after object creation and get it from user...
class student:
    def accept(self,rno,name,per):
        self.rno=rno
        self.name=name
        self.per=per
    def disp(self):
        print("STUDENT ROLL NO:",self.rno)
        print("NAME=",self.name)
        print("PERCENTAGE=",self.per)

ob=student()
rno=input("enter roll no")
name=input("enter name")
per=input("enter per")
ob.accept(rno,name,per)
ob.disp()