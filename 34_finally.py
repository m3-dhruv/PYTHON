# Finally block is always executed

def fun1():

    try:
        lst = [1,2,3,4,5]
        i = int(input("Enter a number : "))
        print(lst[i])
        return 1
    
    except:
        print("Error !!!")
        return 0

    finally:
        print("I am always executed")

x = fun1()
print(x)