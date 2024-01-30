list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
l2 = [100,200,300]

print("sort method")
list1.sort()
print(list1)

print("reverse method")
list1.reverse()
print(list1)

print("index method")
print(list1.index(2))

print("count method")
print(list1.count(9))

print("copy method")
newl = list1.copy()
print(newl)

print("append method")
list1.append(67)
print(list1)

print("insert method")
list1.insert(0, 100)
print(list1)

print("extend method")
list1.extend(l2)
print(list1)