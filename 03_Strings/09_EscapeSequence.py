letter = "Dear Harry! This Python Course is nice. Thanks!"

# formatting it in a good way

# Method1
let = "Dear Harry!\n\tThis Python Course is nice.\nThanks!"
print(let)

# Method2
letter = letter.replace("Dear Harry!", "Dear Harry!\n")
letter = letter.replace("This Python Course is nice.", "\tThis Python Course is nice.")
letter = letter.replace("Thanks!", "\nThanks!")

print (letter)