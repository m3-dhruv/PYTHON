import time 

# time.time()
print("time.time function")
def usingWhile():
  i = 0
  while i<500:
    i = i +1
    print(i) 

def usingFor():
  for i in range(500):
    print(i)

init = time.time()
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)

#time.sleep()
print("time.sleep function")
print(4)
time.sleep(3)
print("This is printed after 3 seconds")
 
#time.strftime()
print("time.strftime function")
t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time) 