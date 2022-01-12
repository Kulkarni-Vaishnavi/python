dict = {
    "kon": "who",
    "phanka": "fan",
    "laal": "red",
    "vastu": "item"
}

print("Options are",dict.keys())
a = input("Enter the hindi word:")

# print("meaning of ",a," is:",dict[a])
# the above line throws error when try to
# access key which is not present

print("meaning of ",a," is:",dict.get(a)) # this returns none if key is not present



