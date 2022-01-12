letter = '''Dear <|Name|>,
Greetings from ABC coding club. We are here to inform
You are Selected!

Date: <|Date|>'''

name = input("Enter your name:")
date = input("Enter date:")
letter = letter.replace("<|Name|>", name)  #need to assign to letter so save the changes
letter = letter.replace("<|Date|>", date)

print(letter)
