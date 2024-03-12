# Enumerate function in python

# upon list
list1 = ["One", "Two", "Three", "Four", "Five"]
for index, i in enumerate (list1):
    print(index,i)

# upon tuple
tuple1 = ("One", "Two", "Three", "Four", "Five")
for index, i in enumerate (tuple1):
    print(index,i)

# upon string
str = "Tony stark"
for index, i in enumerate (str):
    print(index,i)


# changing the start index
list1 = ["One", "Two", "Three", "Four", "Five"]
for index, i in enumerate (list1, start=1):
    print(index,i)