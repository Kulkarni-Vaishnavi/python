text = input("Enter a text:")

if("subscribe now" in text) :
    spam = True

elif("Get money" in text) :
    spam = True

elif("click this" in text) :
    spam = True

else :
    spam = False 

if(spam) :
    print("This is a spam")

else :
    print("This is not a spam")