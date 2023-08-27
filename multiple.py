#This program takes two integers and returns True if the second one is a multiple of first one, returns False otherwise.

def is_multiple(m,n):
    if n%m==0:
        return True
    else:
        return False


m=int(input("Enter first number:"))
n=int(input("Enter first number:"))
print(is_multiple(m,n))
 
   
