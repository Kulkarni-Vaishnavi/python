n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
n3 = int(input("Enter 3rd number:"))
n4 = int(input("Enter 4th number:"))

l1 = [n1,n2,n3,n4]
Sum = l1[0] + l1[1] + l1[2] + l1[3]
print(Sum)

#Method2:

print(sum(l1))