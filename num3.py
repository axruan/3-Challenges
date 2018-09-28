import random as r

list = []
for i in range(0, 11, 1):
    num = r.randrange(0, 101)
    if num%3 != 0:
        list.append(num)

list.sort(reverse = True)
print(list)
