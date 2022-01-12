n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
n3 = int(input("Enter 3rd number:"))
n4 = int(input("Enter 4th number:"))

if(n1 > n2):
    a = n1
else:
    a = n2

if(n3 > n4):
    b = n3
else:
    b = n4

if(a > b):
    print(str(a) + " is greatest") # must to type to string

else:
    print(str(b) + " is greatest")