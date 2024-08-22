#area and  volume of rectangle...
class rectangle:
    def accept(self):
        self.l=float(input("enter length"))
        self.w=float(input("enter width"))
        self.h=float(input("enter height"))
    def compute(self):
        a=self.l*self.w
        v=self.l*self.w*self.h
        print("area=",a)
        print("volume=",v)
ob=rectangle()
ob.accept()
ob.compute()