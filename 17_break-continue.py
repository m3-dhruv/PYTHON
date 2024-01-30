print ("break")
for i in range(50):
    print(i)
    if i == 7:
        break

print("continue")
for i in range(4):
    if i == 2:
        continue
    print(i)