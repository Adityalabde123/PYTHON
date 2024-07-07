#check number is in range or not........
def check_num(n):
    if n>=100 and n<=200:
        print("number is in the range 100-200")
    else:
        print("number is out of boundry")
    
n=int(input("enter number is in the range 100-200"))
check_num(n)