sub1 = int(input('Enter marks of DS:'))
sub2 = int(input('Enter marks of ADE:'))
sub3 = int(input('Enter marks of DM:'))
sub4 = int(input('Enter marks of OOP:'))
sub5 = int(input('Enter marks of COA:'))

per = (sub1+sub2+sub3+sub4+sub5)/5

if(per >=90):
    print("your percentage is:"+ str(per))
    print("A+ grade, exellent")
    
elif(per >=80):
    print("your percentage is:"+ str(per))
    print("A grade, well done")
elif(per >=70):
    print("your percentage is:"+ str(per))
    print("A grade, good job")
elif(per >=60):
    print("your percentage is:"+ str(per))
    print("A grade, can do better")
elif(per >=50):
    print("your percentage is:"+ str(per))
    print("A grade, can do much better")
else:
    print("your percentage is:"+ str(per))
    print("fail, better luch next time")