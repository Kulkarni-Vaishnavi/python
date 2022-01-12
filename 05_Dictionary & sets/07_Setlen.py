s = set()

s.add(45)
s.add(45.00)
s.add('45')

print(s)

print(len(s))  # output 2 bcoz 45 and 45.00 are same
