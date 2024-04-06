
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# Map function
map_func = list(map(lambda x : x * x, list1))
print("Map function: ", map_func)

# Filter Function
filter_func = list(filter(lambda x : x > 2, list1))
print("Filtered List: ", filter_func)

# Reduce Function
from functools import reduce
reduce_func = reduce((lambda x, y : x + y), list1)
print("Reduced Value: ", reduce_func)   