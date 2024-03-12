# raising custome errors

a = int(input("Enter any value between 1 to 10 : "))

if (a<1 or a>10):
    raise ValueError("value should be between 1 and 10")
else:
    print("no error found")