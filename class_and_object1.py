class student:
    def accept(self):
        self.rno=input("enter roll no:")
        self.name=input("enter name:")
        self.per=input("enter per:")
    def disp(self):
        print("Roll no=",self.rno)
        print("name=",self.name)
        print("per=",self.per)

        ob=student()
        ob.accept()
        ob.disp()