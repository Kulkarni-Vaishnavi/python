b = {6,23,9,76}
print(type(b))

# addig values to set
b.add(2)
b.add(5)
# b.add([4,5,7]) --> cannot insert list in a set
# b.add({4:5}) same as above
print(b)

# length of set
print(len(b))

# removes element
b.remove(9)
# b.remove(19) -->throws error when tried to remove elementwhich is not present
print(b)

print(b.pop()) # removes random element
print(b)

