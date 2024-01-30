def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater")

def isLesser(a, b):
  pass
  

a = int(input("enter a first number "))
b = int(input("enter a second number "))
isGreater(a, b)
calculateGmean(a, b)