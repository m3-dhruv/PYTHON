# Program to calculate factorial of entered number

num = int(input("Enter any number :"))
fact = 1
n = num
while num>1:
 fact = fact * num
 num-=1
print("Factorial of ", n , " is :",fact)

# another way (using function)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
number = int(input("Enter a number :"))
result = factorial(number)
print("Factorial of",number,"is :", result)