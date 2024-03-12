a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
x = {9}

# union()
print(a.union(b))

# intersection()
print(a.intersection(b))

# symmetric_difference()
print(a.symmetric_difference(b))

# difference
print(a.difference(b))

print(a.isdisjoint(b))       # isdisjoint()

print(a.issuperset(b))       # issuperset()
 
print(a.issubset(b))         # issubset()

a.add("x")                   # add()
print(a)

print(x.update(a))           # update  

print(a.remove(5))           # remove
print(a.discard(5))          # discard

print(a.pop())               # pop

print(a.clear())          # clear

del b                     # del
print(b)