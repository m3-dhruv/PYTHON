a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
c = int(input("Enter c number : "))

if(a>b) and(a>c):
    print("a is greater number")
elif(b>c) and (b>a):
    print("b is greater number")
else:
    print("c is grater number")