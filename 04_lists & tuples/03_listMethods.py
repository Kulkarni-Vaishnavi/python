l1 = [53,21,9,67,19]
print(l1)

# list functions

l1.sort() # no need of assigning it to l1 
          # it directly reflects the 
          # original list
print(l1)

l1.reverse()
print(l1)

l1.append(45)
print(l1)

l1.insert(1,8) # adds at index 1
print(l1)
l1.insert(4,27)
print(l1)

l1.pop(4) #delete element at index 4
print(l1)

l1.remove(9) 
print(l1)

#  l1.remove(58) ->returns error if wee try to remove 
# element which is not present in list



