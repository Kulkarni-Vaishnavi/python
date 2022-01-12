MyDict = {
    "Harry": "A Coder",    #key-value
    "fast": " In a quick manner",
    "list": [1,2,5,7] ,  # can also contain lists 
    "mydic" : {"harry": "youtuber"} , # nested dictionaries
    "tup" : (1,2,3),
    1:2
}
upd = {
    "above": "higher place",
    "quick": "speed"
}
# dictionary methods
print(MyDict.keys()) # prints the keys of dictionary
print(list(MyDict.keys())) # converting keys into list

print(MyDict.values()) # prints the values of dictionary
print(list(MyDict.values())) # converting values into list

print(MyDict.items()) # prints (key,value) for all contents in dictionary

MyDict.update(upd) # updates mydict permanantly
print(MyDict)

print(MyDict.get(1))  
print(MyDict[1]) 

print(MyDict.get(5))   # returns none if key is not present
# print(MyDict[5]) --> throws an error if key is not present
