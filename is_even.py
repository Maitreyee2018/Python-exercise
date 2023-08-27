#This program decide whether an integer value even - odd without using multiply, division, modulo.

def is_even(k):
    is_even=True
    for i in range(1,k+1):
        if is_even==True:
            is_even=False
        else:
            is_even=True
    return is_even


k=int(input("Enter a integer: "))
print(is_even(k))
