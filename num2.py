list = []
for i in range(-100, 100, 2):
    list.append(i)

for i in range(-100, 100, 3):
    list.append(i)

for i in range(-100, 100, 6):
    list.remove(i)

final = set(list)

print(final)
