#get the string and print string method from class.reverse the string and modify in main function..
class string:
    def get_string(self,string):
        self.string=string
        
    def print_string(self):
         print("string=",str.upper(self.string))
         print("string=",self.string[::-1])
         print("string=",str.lower(self.string))


ob=string()
name=input("enter string")
ob.get_string(name)
ob.print_string()       