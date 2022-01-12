story = "a book should be read with the same spirit with which it has been written"
print(story)

# string functions
print(len(story))
print(story.capitalize())
print(story.endswith("written")) # returns bool
print(story.count("r")) 
print(story.count("A")) # returns -1 because it is case sensitive
print(story.find("with")) # returns index of 1st occurance
print(story.replace("has" , "have"))
print(story.center(90,'*'))