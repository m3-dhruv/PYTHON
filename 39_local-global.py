#local and global variable in python 

gv = 5  #global variable
x = 2   #global variable

def lc():
    lc = 10  #local variable
    print(f"Local Variable: {lc}")

print(f"Global Variable: {gv}")
lc()

def globalkw():
    global x   # globalkeyword use to make a global variable in function
    x = 20   

globalkw()
print(x) 