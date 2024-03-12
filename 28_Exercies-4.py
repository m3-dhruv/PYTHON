# Check it is Prime number or not

import math
num = int(input("Enter any number :"))
isPrime=True
for i in range(2,int(math.sqrt(num))+1):
 if num % i == 0:
  isPrime=False

if isPrime:
  print(num," Number is Prime ")
else:
  print(num," Number is not Prime ")
  


# another way (using a function)
  
def is_Prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2==0 and num%3==0 :
        return False
    
    i = 5
    while i*i<=num:
        if num%i==0 or num%(i+2)==0:
            return False
        i+=6
        return True

number = int(input("enter a number :"))
if is_Prime(number):
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")