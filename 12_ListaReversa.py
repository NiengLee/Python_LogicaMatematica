#   This code organize a list by a reverse way

import random

k = 8
list = []

for i in range(k):
    val = int(random.random() * 100)
    list.append(val)
    print(val)
print("\n")
for i in range(k-1,-1,-1):
    print(list[i])