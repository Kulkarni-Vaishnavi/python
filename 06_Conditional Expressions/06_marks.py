n1 = int(input("Enter marks of subject 1:"))
n2 = int(input("Enter marks of subject 2:"))
n3 = int(input("Enter marks of subject 3:"))

per = (n1+n2+n3)/3
if(n1<33 or n2<33 or n3<33 or per<40):
    print("You are falied  and percentage is:"+str(per))
else:
    print("You are passed and percentage is:" +str(per))