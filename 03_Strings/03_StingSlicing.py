name = "Arjun"
print(name[1])

# name[2] = 'a' --> not acceptable because strings are immutable

print(name[0:3]) #starts from 0 and prints 3 characters
print(name[2:]) # starts from index 2 and prints till end
print(name[:5]) # same as 1st case 

# python also includes negative indexing
print(name[-1])
print(name[-4: -1])  # same as name[1:4]


