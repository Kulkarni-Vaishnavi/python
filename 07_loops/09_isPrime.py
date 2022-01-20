
num = int(input("Enter a number :"))

prime = True

for i in range(2,num):

    if(num%i == 0 and num!=2):
        prime = False
        break

if not prime:
    print(num,'is not a prime')
else:
    print(num,'is prime')