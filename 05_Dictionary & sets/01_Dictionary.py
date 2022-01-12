MyDict = {
    "Harry": "A Coder",    #key-value
    "fast": "A quick manner",
    "list": [1,2,5,7] ,  # can also contain lists 
    "mydic" : {"harry": "youtuber"} , # nested dictionaries
    "tup" : (1,2,3)
  #  "tup" : (1,2,3) cannot contain duplicate keys
}

print(MyDict["Harry"])
print(MyDict["fast"])
print(MyDict["list"])
print(MyDict["mydic"])
print(MyDict["mydic"]["harry"])
print(MyDict["tup"])

MyDict["list"] = [4,8,9,3]  # they are mutable
print(MyDict["list"])