a = "3567"
print(type(a))
print(a)
'''generally we can't typecast str to int if str is "34fbeu6" - alphanumeric
we can only typecast if str contains only numeric'''
a = int(a)   
print(type(a))  
print(a)
a = float(a)
print(type(a))
print(a)

# typecasting can also done by following

print(int(23.8))
print(float(2))
print(str(1234))
print(float("2363"))


