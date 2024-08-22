#create an  calculator (Arithmatic).....
class calculator:
    def add(self,a,b):
         return a+b
    def sub(self,a,b):
         return a-b
    def mul(self,a,b):
         return a*b
    def div(self,a,b):
         return a/b

ob= calculator()
a=float(input("enter first no="))
b=float(input("enter second no="))
print("addition=",ob.add(a,b))
print("Substraction=",ob.sub(a,b))
print("Multiplication=",ob.mul(a,b))
print("Division=",ob.div(a,b))
