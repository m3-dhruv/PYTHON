# IF STATEMENT

a = int(input("Enter your age: "))
print("Your age is:", a)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")

print("Done")


# IF-ELSE
 
applePrice = 200
budget = int(input("Enter your budget: "))
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")



# IF-ELSE-ELIF
    
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")



# NESTED IF 

number = int(input("Enter the number: "))
if (number < 0):
    print("Number is negative.")
elif (number > 0):
    if (number <= 10):
        print("Number is between 1-10")
    elif (number > 10 and number <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")