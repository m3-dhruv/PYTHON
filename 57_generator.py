def my_gen():
    for i in range(50):
        yield i

gen = my_gen()

for j in gen:
    print(j)

